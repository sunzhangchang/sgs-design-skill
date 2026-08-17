from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import time

from .index import SQLiteKnowledgeIndex, ensure_index, load_config, normalize_text
from .linting import findings_as_dict, findings_as_markdown, lint_text
from .routing import VALID_STAGES, VALID_TASKS, build_context, bundle_json


def default_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _read_query(arguments: argparse.Namespace) -> str:
    if getattr(arguments, "query_file", None):
        return Path(arguments.query_file).read_text(encoding="utf-8").strip()
    if getattr(arguments, "query", None):
        return str(arguments.query).strip()
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    return ""


def _context(arguments: argparse.Namespace) -> int:
    root = Path(arguments.root).resolve()
    config = load_config(root)
    query = _read_query(arguments)
    if not query:
        raise SystemExit("context requires --query, --query-file, or stdin")

    state = ensure_index(root, config, rebuild=arguments.rebuild)
    index = SQLiteKnowledgeIndex(state.database)
    defaults = config.get("defaults", {})
    bundle = build_context(
        root=root,
        config=config,
        index=index,
        query=query,
        requested_task=arguments.task,
        requested_stage=arguments.stage,
        max_chars=arguments.max_chars or int(defaults.get("max_chars", 12000)),
        max_chunks=arguments.max_chunks or int(defaults.get("max_chunks", 10)),
        search_chunks=arguments.search_chunks or int(defaults.get("search_chunks", 6)),
        index_rebuilt=state.rebuilt,
        index_elapsed_ms=state.elapsed_ms,
    )

    if arguments.format == "json":
        sys.stdout.write(bundle_json(bundle, include_content=not arguments.plan_only))
    else:
        sys.stdout.write(bundle.as_markdown(plan_only=arguments.plan_only))
    return 0


def _build_index(arguments: argparse.Namespace) -> int:
    root = Path(arguments.root).resolve()
    config = load_config(root)
    state = ensure_index(root, config, rebuild=arguments.rebuild)
    result = {
        "protocol_version": 1,
        "database": str(state.database),
        "rebuilt": state.rebuilt,
        "chunk_count": state.chunk_count,
        "elapsed_ms": round(state.elapsed_ms, 3),
    }
    if arguments.format == "json":
        sys.stdout.write(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    else:
        sys.stdout.write(
            "# Sanguosha Knowledge Index\n\n"
            f"- Database: `{state.database}`\n"
            f"- State: `{'rebuilt' if state.rebuilt else 'cached'}`\n"
            f"- Chunks: `{state.chunk_count}`\n"
            f"- Elapsed: `{state.elapsed_ms:.1f} ms`\n"
        )
    return 0


def _target_specs(config: dict) -> list[tuple[str, list[str], str]]:
    specs: list[tuple[str, list[str], str]] = []
    for task, task_config in config.get("tasks", {}).items():
        for target in task_config.get("required", []):
            specs.append((str(target["path"]), list(target.get("sections", [])), f"task:{task}"))
    for stage, targets in config.get("stages", {}).items():
        for target in targets:
            specs.append((str(target["path"]), list(target.get("sections", [])), f"stage:{stage}"))
    for route in config.get("routes", []):
        for target in route.get("targets", []):
            specs.append((str(target["path"]), list(target.get("sections", [])), f"route:{route['id']}"))
    return specs


def _doctor(arguments: argparse.Namespace) -> int:
    started = time.perf_counter()
    root = Path(arguments.root).resolve()
    config = load_config(root)
    state = ensure_index(root, config, rebuild=arguments.rebuild)
    index = SQLiteKnowledgeIndex(state.database)
    findings: list[dict[str, str]] = []

    route_ids = [str(route.get("id", "")) for route in config.get("routes", [])]
    duplicates = sorted({route_id for route_id in route_ids if route_ids.count(route_id) > 1})
    for route_id in duplicates:
        findings.append({"severity": "error", "message": f"duplicate route id: {route_id}"})

    for path in config.get("documents", {}):
        if not (root / path).exists():
            findings.append({"severity": "error", "message": f"document metadata references missing file: {path}"})

    known_tasks = set(config.get("tasks", {}))
    for classifier in config.get("classifiers", []):
        task = str(classifier.get("task", ""))
        if task not in known_tasks:
            findings.append({"severity": "error", "message": f"classifier references unknown task: {task}"})

    known_stages = set(config.get("stages", {}))
    for classifier in config.get("stage_classifiers", []):
        stage = str(classifier.get("stage", ""))
        if stage not in known_stages:
            findings.append({"severity": "error", "message": f"classifier references unknown stage: {stage}"})

    for route in config.get("routes", []):
        route_id = str(route.get("id", ""))
        if not route_id or not route.get("terms") or not route.get("targets"):
            findings.append(
                {"severity": "error", "message": f"route requires id, terms, and targets: {route_id or '<empty>'}"}
            )

    for path, sections, owner in _target_specs(config):
        absolute = root / path
        if not absolute.exists():
            findings.append({"severity": "error", "message": f"{owner} references missing file: {path}"})
            continue
        headings = index.all_headings(path)
        normalized_headings = [normalize_text(heading) for heading in headings]
        for section in sections:
            normalized_section = normalize_text(str(section))
            if not any(normalized_section in heading for heading in normalized_headings):
                findings.append(
                    {
                        "severity": "error",
                        "message": f"{owner} references missing section: {path}#{section}",
                    }
                )

    error_count = sum(1 for finding in findings if finding["severity"] == "error")
    result = {
        "protocol_version": 1,
        "ok": error_count == 0,
        "index": {
            "rebuilt": state.rebuilt,
            "chunks": state.chunk_count,
            "elapsed_ms": round(state.elapsed_ms, 3),
        },
        "checked_targets": len(_target_specs(config)),
        "checked_documents": len(config.get("documents", {})),
        "elapsed_ms": round((time.perf_counter() - started) * 1000, 3),
        "findings": findings,
    }

    if arguments.format == "json":
        sys.stdout.write(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    else:
        lines = [
            "# Sanguosha Preflight Doctor",
            "",
            f"- Result: `{'pass' if result['ok'] else 'fail'}`",
            f"- Indexed chunks: `{state.chunk_count}`",
            f"- Checked targets: `{result['checked_targets']}`",
            f"- Checked documents: `{result['checked_documents']}`",
            f"- Elapsed: `{result['elapsed_ms']:.1f} ms`",
        ]
        if findings:
            lines.extend(["", "## Findings", ""])
            lines.extend(f"- **{item['severity'].upper()}**: {item['message']}" for item in findings)
        sys.stdout.write("\n".join(lines).rstrip() + "\n")
    return 0 if result["ok"] else 1


def _lint(arguments: argparse.Namespace) -> int:
    if arguments.file:
        text = Path(arguments.file).read_text(encoding="utf-8")
    elif arguments.text is not None:
        text = arguments.text
    elif not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        raise SystemExit("lint requires --text, --file, or stdin")

    findings = lint_text(text, full_group=arguments.full_group)
    result = findings_as_dict(findings)
    if arguments.format == "json":
        sys.stdout.write(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    else:
        sys.stdout.write(findings_as_markdown(findings))
    return 0 if result["ok"] else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Deterministic local preflight for the Sanguosha design skill."
    )
    parser.add_argument("--root", default=str(default_root()), help="Skill root directory.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    context_parser = subparsers.add_parser("context", help="Route and compile focused references.")
    context_parser.add_argument("--query")
    context_parser.add_argument("--query-file")
    context_parser.add_argument("--task", choices=sorted(VALID_TASKS), default="auto")
    context_parser.add_argument("--stage", choices=sorted(VALID_STAGES), default="auto")
    context_parser.add_argument("--max-chars", type=int)
    context_parser.add_argument("--max-chunks", type=int)
    context_parser.add_argument("--search-chunks", type=int)
    context_parser.add_argument("--plan-only", action="store_true")
    context_parser.add_argument("--rebuild", action="store_true")
    context_parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    context_parser.set_defaults(handler=_context)

    index_parser = subparsers.add_parser("build-index", help="Build or inspect the local cache.")
    index_parser.add_argument("--rebuild", action="store_true")
    index_parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    index_parser.set_defaults(handler=_build_index)

    doctor_parser = subparsers.add_parser("doctor", help="Validate routes and indexed sections.")
    doctor_parser.add_argument("--rebuild", action="store_true")
    doctor_parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    doctor_parser.set_defaults(handler=_doctor)

    lint_parser = subparsers.add_parser("lint", help="Run deterministic skill-text checks.")
    lint_parser.add_argument("--text")
    lint_parser.add_argument("--file")
    lint_parser.add_argument("--full-group", action="store_true")
    lint_parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    lint_parser.set_defaults(handler=_lint)
    return parser


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
    parser = build_parser()
    arguments = parser.parse_args(argv)
    return int(arguments.handler(arguments))
