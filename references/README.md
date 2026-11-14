# Reference Map

This directory is a progressive knowledge base. Do not read every file for an ordinary request. Start with the route for the current task, then load the smallest relevant slice.

When local Python execution is available, use `scripts/preflight.py context` to combine relevant sections. Check its coverage and omissions; read missing sections directly before relying on them. The read order below is the human-readable fallback and the authority model used by that engine.

## Read Order

1. Every fresh design or review: [rules-priority.md](rules-priority.md).
2. Every fresh design or review: [design-evaluation-framework.md](design-evaluation-framework.md), the shared design/review loop.
3. Only the current design stage: the needed sections in [design-heuristics.md](design-heuristics.md).
4. A named mechanism, package, special card, or special zone: [mechanics-index.md](mechanics-index.md), then one routed file under `mechanics/`.
5. A contest sample, judge feedback, or contest-style score: [contest-evaluation.md](contest-evaluation.md).
6. A generated name or named nonstandard object: [naming-titles.md](naming-titles.md).
7. Absorbing or incorporating new material: [knowledge-intake.md](knowledge-intake.md), then only the destination it routes.
8. A question about where an existing principle came from: [source-digests.md](source-digests.md).

## Foundational Rule Files

These files distill the reviewed `gltjk.com` rules pages and identity-mode materials. They outrank design heuristics and mechanism essays whenever their subject is involved.

| File | Open when the draft touches |
| --- | --- |
| [card-glossary.md](card-glossary.md) | card category, delayed trick, equipment, card-as-cost, printed/current skills |
| [gamecard-operations.md](gamecard-operations.md) | use/play/recast/place/discard/give/gain/lose, information operations, exchange, judgment, treat-as |
| [herocard-operations.md](herocard-operations.md) | 横置/重置、连环状态、连环伤害继承、翻面 |
| [zone-glossary.md](zone-glossary.md) | zone, ownership, visibility, processing/judgment area, draw/discard pile |
| [value-glossary.md](value-glossary.md) | points, HP/max HP, hand limit, damage value, distance/range, X, extrema |
| [description-glossary.md](description-glossary.md) | agency, sequential operations, transfer, attribution, options, targets, visibility |
| [flow-glossary.md](flow-glossary.md) | turn/phase order, extra/skipped flow, outside-turn scope, dying/death/kill |
| [event-glossary.md](event-glossary.md) | event insertion, response/resolution, invalid/ignore/counteract/cancel, effect scope |
| [identity-card-environment.md](identity-card-environment.md) | identity deck ecology, card availability, opening hand, kill/death rewards, exhaustion |

## Design Files

- [design-evaluation-framework.md](design-evaluation-framework.md): the canonical closed loop, unified working sheet, evaluation order, stress tests, diagnosis, and repair language for both generation and review.
- [design-rating-calibration.md](design-rating-calibration.md): shared evidence anchors for evaluation; load score calibration only for comparison or scored-result work.
- [score-calibration-method.md](score-calibration-method.md): score distributions, evaluator differences, cohort comparisons, and limits on numeric generalization; use only when scores or results matter.
- [design-heuristics.md](design-heuristics.md): a stage-routed option library for design origin, anchors, skill structure, timing, linkage, clan design, locked skills, support, balance, and wording.
- [contest-evaluation.md](contest-evaluation.md): contest-only extensions, sample parsing, judge-feedback evidence, disagreements, and practical contest cases. It supplements rather than replaces the unified framework.
- [naming-titles.md](naming-titles.md): titles, achievements, skill names, card names, mark names, and names for generated objects.

## Mechanism Files

- [mechanics-index.md](mechanics-index.md): progressive routing, package labels, priority levels, and safety cautions.
- `mechanics/`: focused descriptions of special cards and mechanisms. Read only the file routed by the index.

## Provenance And Intake

- [knowledge-intake.md](knowledge-intake.md): the cautious end-to-end procedure for preservation, instruction/data separation, classification, authority conflicts, minimal merging, validation, and local commits.
- [source-digests.md](source-digests.md): concise provenance and reusable lessons from online/offline material.
- Raw source pages retained for checking are under the ignored workspace folder `.codex/source-check/`; they are not a substitute for the distilled references.

## Local Preflight

- [local-preflight.md](local-preflight.md): commands, output protocol, retrieval priority, cache behavior, extension procedure, and backend boundaries. Read only for maintenance or debugging.
