from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sqlite3
import tempfile
import time
import unicodedata


HEADING_RE = re.compile(r"^(#{1,3})\s+(.+?)\s*$")
ASCII_TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9_+.-]*")
CJK_RUN_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]+")


@dataclass(frozen=True)
class Chunk:
    chunk_id: int
    path: str
    heading: str
    level: int
    start_line: int
    end_line: int
    kind: str
    authority: int
    content: str
    token_count: int


@dataclass(frozen=True)
class SearchHit:
    chunk: Chunk
    score: float


@dataclass(frozen=True)
class IndexState:
    database: Path
    rebuilt: bool
    chunk_count: int
    elapsed_ms: float


def normalize_text(value: str) -> str:
    return unicodedata.normalize("NFKC", value).casefold()


def tokenize(value: str) -> list[str]:
    normalized = normalize_text(value)
    tokens = [f"w:{token}" for token in ASCII_TOKEN_RE.findall(normalized)]

    for run in CJK_RUN_RE.findall(normalized):
        if len(run) == 1:
            tokens.append(f"c1:{run}")
            continue
        tokens.extend(f"c2:{run[index:index + 2]}" for index in range(len(run) - 1))
        if len(run) >= 3:
            tokens.extend(f"c3:{run[index:index + 3]}" for index in range(len(run) - 2))

    return tokens


def load_config(root: Path) -> dict:
    path = root / "config" / "preflight.json"
    with path.open("r", encoding="utf-8") as stream:
        return json.load(stream)


def _default_document_meta(relative_path: str) -> dict:
    if relative_path.startswith("references/mechanics/"):
        return {"kind": "mechanism", "authority": 45, "tags": []}
    return {"kind": "reference", "authority": 40, "tags": []}


def _source_files(root: Path) -> list[Path]:
    return sorted((root / "references").rglob("*.md"))


def _signature(root: Path, config_path: Path, sources: list[Path]) -> str:
    records: list[tuple[str, int, int]] = []
    for path in [config_path, *sources]:
        stat = path.stat()
        records.append((path.relative_to(root).as_posix(), stat.st_mtime_ns, stat.st_size))
    encoded = json.dumps(records, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _cache_path(root: Path, schema_version: int, signature: str) -> Path:
    root_key = hashlib.sha256(str(root.resolve()).casefold().encode("utf-8")).hexdigest()[:16]
    directory = Path(tempfile.gettempdir()) / "sgs-design-skill" / root_key
    directory.mkdir(parents=True, exist_ok=True)
    return directory / f"knowledge-v{schema_version}-{signature[:16]}.sqlite3"


def _parse_chunks(root: Path, path: Path, config: dict) -> list[dict]:
    relative = path.relative_to(root).as_posix()
    document_meta = _default_document_meta(relative)
    document_meta.update(config.get("documents", {}).get(relative, {}))
    tags = " ".join(document_meta.get("tags", []))

    lines = path.read_text(encoding="utf-8").splitlines()
    boundaries: list[tuple[int, int, str]] = []
    for index, line in enumerate(lines):
        match = HEADING_RE.match(line)
        if match:
            boundaries.append((index, len(match.group(1)), match.group(2)))

    if not boundaries:
        boundaries = [(0, 1, path.stem)]
    elif boundaries[0][0] > 0:
        boundaries.insert(0, (0, 1, path.stem))

    chunks: list[dict] = []
    for boundary_index, (start, level, heading) in enumerate(boundaries):
        if level == 1 and boundary_index > 0:
            continue
        end = boundaries[boundary_index + 1][0] if boundary_index + 1 < len(boundaries) else len(lines)
        content = "\n".join(lines[start:end]).strip()
        if not content:
            continue
        token_counts = Counter(tokenize(f"{heading}\n{tags}\n{content}"))
        chunks.append(
            {
                "path": relative,
                "heading": heading,
                "level": level,
                "start_line": start + 1,
                "end_line": end,
                "kind": str(document_meta.get("kind", "reference")),
                "authority": int(document_meta.get("authority", 40)),
                "content": content,
                "token_counts": token_counts,
                "token_count": max(1, sum(token_counts.values())),
            }
        )
    return chunks


def _initialize_database(path: Path) -> sqlite3.Connection:
    connection = sqlite3.connect(path)
    connection.executescript(
        """
        PRAGMA journal_mode = OFF;
        PRAGMA synchronous = OFF;
        PRAGMA temp_store = MEMORY;
        CREATE TABLE meta (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );
        CREATE TABLE chunks (
            id INTEGER PRIMARY KEY,
            path TEXT NOT NULL,
            heading TEXT NOT NULL,
            level INTEGER NOT NULL,
            start_line INTEGER NOT NULL,
            end_line INTEGER NOT NULL,
            kind TEXT NOT NULL,
            authority INTEGER NOT NULL,
            content TEXT NOT NULL,
            token_count INTEGER NOT NULL
        );
        CREATE TABLE postings (
            token TEXT NOT NULL,
            chunk_id INTEGER NOT NULL,
            term_frequency INTEGER NOT NULL,
            PRIMARY KEY (token, chunk_id)
        ) WITHOUT ROWID;
        CREATE TABLE terms (
            token TEXT PRIMARY KEY,
            document_frequency INTEGER NOT NULL
        ) WITHOUT ROWID;
        CREATE INDEX chunks_path_heading ON chunks(path, heading);
        CREATE INDEX chunks_kind ON chunks(kind);
        """
    )
    return connection


def _read_meta(path: Path, key: str) -> str | None:
    if not path.exists():
        return None
    try:
        with sqlite3.connect(path) as connection:
            row = connection.execute("SELECT value FROM meta WHERE key = ?", (key,)).fetchone()
            return str(row[0]) if row else None
    except sqlite3.DatabaseError:
        return None


def ensure_index(root: Path, config: dict, rebuild: bool = False) -> IndexState:
    started = time.perf_counter()
    sources = _source_files(root)
    config_path = root / "config" / "preflight.json"
    signature = _signature(root, config_path, sources)
    database = _cache_path(root, int(config.get("schema_version", 1)), signature)
    initial_database_mtime = database.stat().st_mtime_ns if database.exists() else None

    if not rebuild and _read_meta(database, "signature") == signature:
        chunk_count = int(_read_meta(database, "chunk_count") or 0)
        return IndexState(database, False, chunk_count, (time.perf_counter() - started) * 1000)

    lock_path = database.with_suffix(database.suffix + ".lock")
    lock_handle: int | None = None
    wait_deadline = time.monotonic() + 15.0
    while lock_handle is None:
        try:
            lock_handle = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(lock_handle, str(os.getpid()).encode("ascii"))
        except FileExistsError:
            if _read_meta(database, "signature") == signature:
                chunk_count = int(_read_meta(database, "chunk_count") or 0)
                return IndexState(database, False, chunk_count, (time.perf_counter() - started) * 1000)
            if time.monotonic() >= wait_deadline:
                try:
                    if time.time() - lock_path.stat().st_mtime > 30:
                        lock_path.unlink(missing_ok=True)
                        continue
                except OSError:
                    pass
                raise TimeoutError(f"timed out waiting for preflight index lock: {lock_path}")
            time.sleep(0.05)

    temporary = database.with_name(f"{database.name}.{os.getpid()}.tmp")
    temporary.unlink(missing_ok=True)
    try:
        current_valid = _read_meta(database, "signature") == signature
        current_mtime = database.stat().st_mtime_ns if database.exists() else None
        if current_valid and (not rebuild or current_mtime != initial_database_mtime):
            chunk_count = int(_read_meta(database, "chunk_count") or 0)
            return IndexState(database, False, chunk_count, (time.perf_counter() - started) * 1000)

        connection = _initialize_database(temporary)
        document_frequencies: Counter[str] = Counter()
        chunk_id = 0
        try:
            for source in sources:
                for parsed in _parse_chunks(root, source, config):
                    chunk_id += 1
                    connection.execute(
                        """
                        INSERT INTO chunks(
                            id, path, heading, level, start_line, end_line,
                            kind, authority, content, token_count
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            chunk_id,
                            parsed["path"],
                            parsed["heading"],
                            parsed["level"],
                            parsed["start_line"],
                            parsed["end_line"],
                            parsed["kind"],
                            parsed["authority"],
                            parsed["content"],
                            parsed["token_count"],
                        ),
                    )
                    token_counts: Counter[str] = parsed["token_counts"]
                    connection.executemany(
                        "INSERT INTO postings(token, chunk_id, term_frequency) VALUES (?, ?, ?)",
                        ((token, chunk_id, frequency) for token, frequency in token_counts.items()),
                    )
                    document_frequencies.update(token_counts.keys())

            connection.executemany(
                "INSERT INTO terms(token, document_frequency) VALUES (?, ?)",
                document_frequencies.items(),
            )
            average_length = connection.execute("SELECT AVG(token_count) FROM chunks").fetchone()[0] or 1.0
            meta = {
                "signature": signature,
                "chunk_count": str(chunk_id),
                "average_length": str(float(average_length)),
                "schema_version": str(config.get("schema_version", 1)),
            }
            connection.executemany("INSERT INTO meta(key, value) VALUES (?, ?)", meta.items())
            connection.commit()
        finally:
            connection.close()

        if _read_meta(database, "signature") == signature:
            temporary.unlink(missing_ok=True)
        else:
            os.replace(temporary, database)

        old_databases = sorted(
            database.parent.glob("knowledge-v*.sqlite3"),
            key=lambda path: path.stat().st_mtime_ns,
            reverse=True,
        )
        for stale in old_databases[3:]:
            try:
                stale.unlink()
            except OSError:
                pass
    finally:
        temporary.unlink(missing_ok=True)
        if lock_handle is not None:
            os.close(lock_handle)
        lock_path.unlink(missing_ok=True)

    return IndexState(database, True, chunk_id, (time.perf_counter() - started) * 1000)


def _row_to_chunk(row: sqlite3.Row) -> Chunk:
    return Chunk(
        chunk_id=int(row["id"]),
        path=str(row["path"]),
        heading=str(row["heading"]),
        level=int(row["level"]),
        start_line=int(row["start_line"]),
        end_line=int(row["end_line"]),
        kind=str(row["kind"]),
        authority=int(row["authority"]),
        content=str(row["content"]),
        token_count=int(row["token_count"]),
    )


class SQLiteKnowledgeIndex:
    def __init__(self, database: Path):
        self.database = database

    def chunks_for_target(self, path: str, sections: list[str] | None = None) -> list[Chunk]:
        with sqlite3.connect(self.database) as connection:
            connection.row_factory = sqlite3.Row
            rows = connection.execute(
                "SELECT * FROM chunks WHERE path = ? ORDER BY start_line",
                (path,),
            ).fetchall()

        chunks = [_row_to_chunk(row) for row in rows]
        if not sections:
            return chunks

        normalized_sections = [normalize_text(section) for section in sections]
        return [
            chunk
            for chunk in chunks
            if any(section in normalize_text(chunk.heading) for section in normalized_sections)
        ]

    def all_headings(self, path: str) -> list[str]:
        return [chunk.heading for chunk in self.chunks_for_target(path)]

    def search(
        self,
        query: str,
        limit: int,
        excluded_kinds: set[str] | None = None,
    ) -> list[SearchHit]:
        query_counts = Counter(tokenize(query))
        if not query_counts:
            return []

        tokens = list(query_counts)
        placeholders = ",".join("?" for _ in tokens)
        excluded_kinds = excluded_kinds or set()

        with sqlite3.connect(self.database) as connection:
            connection.row_factory = sqlite3.Row
            total_chunks = int(connection.execute("SELECT COUNT(*) FROM chunks").fetchone()[0])
            average_length = float(
                connection.execute("SELECT value FROM meta WHERE key = 'average_length'").fetchone()[0]
            )
            rows = connection.execute(
                f"""
                SELECT p.token, p.chunk_id, p.term_frequency,
                       t.document_frequency, c.*
                FROM postings p
                JOIN terms t ON t.token = p.token
                JOIN chunks c ON c.id = p.chunk_id
                WHERE p.token IN ({placeholders})
                """,
                tokens,
            ).fetchall()

        scores: dict[int, float] = {}
        chunks: dict[int, Chunk] = {}
        k1 = 1.2
        b = 0.75
        for row in rows:
            chunk = _row_to_chunk(row)
            if chunk.kind in excluded_kinds:
                continue
            token = str(row["token"])
            frequency = int(row["term_frequency"])
            document_frequency = int(row["document_frequency"])
            inverse_frequency = math.log(
                1.0 + (total_chunks - document_frequency + 0.5) / (document_frequency + 0.5)
            )
            denominator = frequency + k1 * (
                1.0 - b + b * chunk.token_count / max(1.0, average_length)
            )
            contribution = inverse_frequency * (frequency * (k1 + 1.0) / denominator)
            contribution *= 1.0 + 0.08 * max(0, query_counts[token] - 1)
            scores[chunk.chunk_id] = scores.get(chunk.chunk_id, 0.0) + contribution
            chunks[chunk.chunk_id] = chunk

        normalized_query = normalize_text(query)
        for chunk_id, chunk in chunks.items():
            heading = normalize_text(chunk.heading)
            heading_boost = sum(
                1.2
                for term in CJK_RUN_RE.findall(normalized_query)
                if len(term) >= 2 and term in heading
            )
            authority_boost = max(0, chunk.authority - 40) / 100.0
            scores[chunk_id] += heading_boost + authority_boost

        ranked = sorted(scores, key=lambda item: (-scores[item], chunks[item].path, chunks[item].start_line))
        return [SearchHit(chunks[chunk_id], scores[chunk_id]) for chunk_id in ranked[:limit]]
