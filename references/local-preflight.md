# Local Preflight Engine

Use this reference only when maintaining or debugging local retrieval. Ordinary design and review tasks should run the command directed by `SKILL.md` and consume its compiled context without reading this file.

## Stable Commands

Run from the skill root, or pass `--root` explicitly:

```powershell
python scripts/preflight.py context --task review --stage rules --query "伤害时机与虚拟牌"
python scripts/preflight.py context --task rules --query "规则问题"
python scripts/preflight.py context --task fresh-design --stage play --query "太原王氏中流，辅助且有单挑空间"
python scripts/preflight.py context --task intake --query "吸收新的机制评价资料"
python scripts/preflight.py lint --text "技能文本" --full-group
python scripts/preflight.py doctor
python scripts/preflight.py build-index --rebuild
```

`context` supports `--format json`, `--plan-only`, `--max-chars`, and `--max-chunks`. It never cuts a selected section mid-text. Sections that do not fit are listed in both the plan and compiled output; JSON reports them under `coverage.omitted`. `coverage.complete` means every selected section loaded in full; it does not certify that routing found every relevant reference or that the design is legal. Its protocol version is stable across retrieval backends:

```text
task / stage / matched_routes / index / total_chars / coverage / chunks[]
coverage = complete / omitted_count / omitted[]
omitted[] = path / heading / lines / source / cause
chunks[] = path / heading / lines / authority / source / reason / truncated / content
```

## Architecture

- `config/preflight.json`: task/stage defaults, document authority, deterministic routes, and retrieval policy.
- `scripts/sgs_preflight/index.py`: heading parser, Chinese n-gram tokenizer, temporary SQLite cache, and BM25 retrieval.
- `scripts/sgs_preflight/routing.py`: task/stage classification, priority merge, budget enforcement, and context output.
- `scripts/sgs_preflight/linting.py`: deterministic text checks that do not pretend to replace semantic review.
- `scripts/sgs_preflight/cli.py`: stable command and output boundary.
- `tests/test_preflight.py`: route, budget, cache, and lint regressions.

The cache is stored under the system temporary directory and keyed by the skill root plus source signature. It is not committed and is rebuilt when a reference or configuration file changes. Concurrent processes share a versioned cache through a short lock; only one process builds each source signature.

## Retrieval Priority

The context compiler uses this order:

1. task core, such as the rules gate or intake contract;
2. deterministic routes triggered by explicit concepts;
3. current-stage guidance;
4. local BM25 plus Chinese character n-grams only when deterministic coverage is insufficient.

Approximate retrieval cannot override or suppress a deterministic foundational route. A rules-only task excludes design, contest, provenance, and naming material; it loads a mechanism reference only through its explicit route. Mechanism, contest, provenance, and naming documents are excluded from ordinary approximate retrieval unless the task or a deterministic route asks for them.

## Extension Procedure

When adding a reference:

1. Add the Markdown file under `references/`; it is indexed automatically by headings.
2. Add a `documents` entry only when its kind, authority, or tags differ from the default.
3. Add a deterministic `route` only when missing that reference could change legality or a recurring design decision.
4. Add task/stage defaults only when every request in that task/stage needs the section.
5. Run `doctor --rebuild`, the unit tests, the skill validator, and one representative context query.

When adding a retrieval backend, preserve the context protocol and priority order. Semantic or local-model retrieval may replace the BM25 supplement, but it must not decide foundational authority. Keep rule routing deterministic and testable.

## Operational Boundaries

- The preflight engine selects context; it does not design, evaluate, or absorb knowledge by itself.
- Source material never becomes executable instructions through indexing.
- Lint warnings are prompts for semantic review, not automatic proof that a skill is illegal.
- Do not commit generated caches, platform-specific binaries, or model weights.
- Do not require network access or third-party packages for the default backend.
