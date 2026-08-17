from __future__ import annotations

from dataclasses import dataclass, replace
import json
from pathlib import Path
from typing import Any

from .index import Chunk, SQLiteKnowledgeIndex, normalize_text


VALID_TASKS = {"auto", "fresh-design", "review", "contest", "naming", "intake"}
VALID_STAGES = {"auto", "character", "play", "skeleton", "rules", "evaluation", "output"}


@dataclass
class Selection:
    chunk: Chunk
    priority: float
    reason: str
    source: str


@dataclass
class ContextBundle:
    task: str
    stage: str
    query: str
    selections: list[Selection]
    matched_routes: list[str]
    index_rebuilt: bool
    index_elapsed_ms: float
    total_chars: int

    def as_dict(self, include_content: bool = True) -> dict[str, Any]:
        return {
            "protocol_version": 1,
            "task": self.task,
            "stage": self.stage,
            "query": self.query,
            "matched_routes": self.matched_routes,
            "index": {
                "rebuilt": self.index_rebuilt,
                "elapsed_ms": round(self.index_elapsed_ms, 3),
            },
            "total_chars": self.total_chars,
            "chunks": [
                {
                    "path": selection.chunk.path,
                    "heading": selection.chunk.heading,
                    "lines": [selection.chunk.start_line, selection.chunk.end_line],
                    "kind": selection.chunk.kind,
                    "authority": selection.chunk.authority,
                    "priority": round(selection.priority, 3),
                    "source": selection.source,
                    "reason": selection.reason,
                    "truncated": "[preflight context truncated" in selection.chunk.content,
                    **({"content": selection.chunk.content} if include_content else {}),
                }
                for selection in self.selections
            ],
        }

    def as_markdown(self, plan_only: bool = False) -> str:
        lines = [
            "# Sanguosha Preflight Context",
            "",
            f"- Task: `{self.task}`",
            f"- Stage: `{self.stage}`",
            f"- Matched routes: `{', '.join(self.matched_routes) or 'none'}`",
            f"- Context characters: `{self.total_chars}`",
            f"- Index: `{'rebuilt' if self.index_rebuilt else 'cached'}` ({self.index_elapsed_ms:.1f} ms)",
            "",
            "## Route Plan",
            "",
        ]
        for selection in self.selections:
            lines.append(
                f"- `{selection.chunk.path}#{selection.chunk.heading}` "
                f"[{selection.source}; {selection.reason}]"
            )

        if plan_only:
            return "\n".join(lines).rstrip() + "\n"

        lines.extend(["", "## Compiled Context", ""])
        for selection in self.selections:
            chunk = selection.chunk
            lines.extend(
                [
                    f"### {chunk.path} :: {chunk.heading}",
                    f"<!-- lines {chunk.start_line}-{chunk.end_line}; {selection.reason} -->",
                    "",
                    chunk.content,
                    "",
                ]
            )
        return "\n".join(lines).rstrip() + "\n"


def _matches_terms(query: str, terms: list[str]) -> bool:
    normalized_query = normalize_text(query)
    return any(normalize_text(term) in normalized_query for term in terms)


def classify_task(query: str, config: dict, requested: str) -> str:
    if requested != "auto":
        return requested
    for classifier in config.get("classifiers", []):
        if _matches_terms(query, classifier.get("terms", [])):
            return str(classifier["task"])
    return "fresh-design"


def classify_stage(query: str, task: str, config: dict, requested: str) -> str:
    if requested != "auto":
        return requested
    for classifier in config.get("stage_classifiers", []):
        if _matches_terms(query, classifier.get("terms", [])):
            return str(classifier["stage"])
    if task in {"review", "contest"}:
        return "evaluation"
    if task == "fresh-design":
        return "character"
    return "output"


def _add_targets(
    selections: dict[int, Selection],
    index: SQLiteKnowledgeIndex,
    targets: list[dict],
    priority: float,
    source: str,
    reason: str,
) -> None:
    for target_index, target in enumerate(targets):
        path = str(target["path"])
        sections = [str(section) for section in target.get("sections", [])]
        for chunk in index.chunks_for_target(path, sections):
            normalized_heading = normalize_text(chunk.heading)
            section_index = next(
                (
                    section_position
                    for section_position, section in enumerate(sections)
                    if normalize_text(section) in normalized_heading
                ),
                len(sections),
            )
            ordering_bonus = (len(sections) - section_index) * 0.01
            ordering_bonus += (len(targets) - target_index) * 0.001
            current = selections.get(chunk.chunk_id)
            candidate = Selection(chunk, priority + ordering_bonus, reason, source)
            if current is None or candidate.priority > current.priority:
                selections[chunk.chunk_id] = candidate


def build_context(
    root: Path,
    config: dict,
    index: SQLiteKnowledgeIndex,
    query: str,
    requested_task: str,
    requested_stage: str,
    max_chars: int,
    max_chunks: int,
    search_chunks: int,
    index_rebuilt: bool,
    index_elapsed_ms: float,
) -> ContextBundle:
    task = classify_task(query, config, requested_task)
    stage = classify_stage(query, task, config, requested_stage)
    task_config = config.get("tasks", {}).get(task, {})
    excluded_kinds = set(task_config.get("exclude_kinds", []))
    retrieval_config = config.get("retrieval", {})
    excluded_headings = {
        normalize_text(str(heading)) for heading in retrieval_config.get("exclude_headings", [])
    }
    exclude_level_one = bool(retrieval_config.get("exclude_level_one", True))
    selections: dict[int, Selection] = {}

    _add_targets(
        selections,
        index,
        task_config.get("required", []),
        1000.0,
        "core",
        f"task:{task}",
    )

    matched_routes: list[str] = []
    for route in config.get("routes", []):
        applicable_tasks = set(route.get("tasks", ["fresh-design", "review", "contest"]))
        if task not in applicable_tasks:
            continue
        if not _matches_terms(query, route.get("terms", [])):
            continue
        route_id = str(route["id"])
        matched_routes.append(route_id)
        _add_targets(
            selections,
            index,
            route.get("targets", []),
            900.0,
            "route",
            route_id,
        )

    if task in {"fresh-design", "review", "contest"}:
        _add_targets(
            selections,
            index,
            config.get("stages", {}).get(stage, []),
            800.0,
            "stage",
            f"stage:{stage}",
        )

    retrieval_needed = not matched_routes or len(selections) < max(4, max_chunks // 2)
    if retrieval_needed:
        for hit in index.search(query, max(search_chunks, max_chunks), excluded_kinds):
            if hit.chunk.chunk_id in selections:
                continue
            if exclude_level_one and hit.chunk.level == 1:
                continue
            if normalize_text(hit.chunk.heading) in excluded_headings:
                continue
            selections[hit.chunk.chunk_id] = Selection(
                hit.chunk,
                100.0 + hit.score,
                "local-bm25-ngram",
                "retrieval",
            )

    ordered = sorted(
        selections.values(),
        key=lambda selection: (
            -selection.priority,
            -selection.chunk.authority,
            selection.chunk.path,
            selection.chunk.start_line,
        ),
    )

    chosen: list[Selection] = []
    total_chars = 0
    for selection in ordered:
        required = selection.source in {"core", "route"}
        if len(chosen) >= max_chunks and not required:
            continue
        remaining = max_chars - total_chars
        content_size = len(selection.chunk.content)
        if remaining <= 0:
            continue
        if content_size > remaining:
            suffix = "\n\n[preflight context truncated at the configured character budget]"
            if remaining <= len(suffix):
                continue
            content = selection.chunk.content[: remaining - len(suffix)].rstrip()
            if not content:
                continue
            content += suffix
            selection = Selection(
                replace(selection.chunk, content=content),
                selection.priority,
                selection.reason,
                selection.source,
            )
            content_size = len(content)
        chosen.append(selection)
        total_chars += content_size

    return ContextBundle(
        task=task,
        stage=stage,
        query=query,
        selections=chosen,
        matched_routes=matched_routes,
        index_rebuilt=index_rebuilt,
        index_elapsed_ms=index_elapsed_ms,
        total_chars=total_chars,
    )


def bundle_json(bundle: ContextBundle, include_content: bool = True) -> str:
    return json.dumps(bundle.as_dict(include_content), ensure_ascii=False, indent=2) + "\n"
