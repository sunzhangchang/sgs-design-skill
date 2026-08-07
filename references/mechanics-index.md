# Mechanics And Special Cards Index

Use this file as the routing index for 三国杀 cross-server mechanisms, special cards, special zones, extra decks, equipment vocabulary, and package-scoped material.

Do not read every mechanics file before designing. Start here, choose the smallest relevant slice, read only that slice during the current interaction step, and return to the user with a concrete question or draft.

Sources distilled into this reference set:

- 三国杀各服军争新机制与特殊牌汇总 document, revision records through 2025-04-21.
- User-reviewed package card/mechanism table from selected packages: 游戏模式、国战、军争、OL、SP、手杀、十周年、线下、国际服、江山如故、谋攻篇、蚀心入魔、通用机制 and related packages.
- WAHX mechanism essays on new concepts, used for priority and robustness evaluation rather than wholesale importing.

Package labels are preserved only so a user can include or exclude sources. Do not assume a local codebase exists.

## Progressive Use

Use mechanisms interactively:

1. Ask whether the user wants official-like, low-complexity, experimental, package-scoped, or no-special-mechanism design.
2. If the user names a mechanism, read the matching slice below and ask one follow-up only if the package/mode scope or risk tolerance is unclear.
3. If the user only gives a character, first read `design-heuristics.md`; read a mechanics slice only after choosing the character's main resource axis.
4. If the design direction changes during the conversation, switch slices instead of loading more files preemptively.
5. After drafting, check the relevant slice's guardrails plus the short cautions below.

## Fast Lookup By Design Need

- Compulsory drawback, technical label, 限定/觉醒/使命/蓄力/计次: read [concept-basics.md](mechanics/concept-basics.md).
- Cancellation, termination, forced phase/turn ending, source/user reassignment, control, physical state, abolition/recovery, turn-flow, entry/exit: read [resolution-and-control.md](mechanics/resolution-and-control.md).
- Virtual cards, changed card names, tags, marks, stored cards, special zones, non-game cards, public tasks, movement, gifts, recast, search, extra decks: read [cards-zones-and-movement.md](mechanics/cards-zones-and-movement.md).
- Guessing, randomness, contests, voting, bargaining, bonds, formations, victory/faction changes, allocation, refusal, skill existence, hidden/off-board effects, binary shorthand: read [social-choice-and-identity.md](mechanics/social-choice-and-identity.md).
- Attribute damage, fake damage records, card tags, skill encapsulation, HP display, armor, shields, dying thresholds, gem-color logic: read [damage-hp-and-tags.md](mechanics/damage-hp-and-tags.md).
- Package-scoped mechanism lookup by Chinese package name: search [package-index.md](mechanics/package-index.md) for the package or mechanism name first, then read the nearby section.
- Named special cards, package special-card patterns, equipment and treasure vocabulary, low-priority special equipment: read [special-cards-and-equipment.md](mechanics/special-cards-and-equipment.md).
- Standard plus 军争 identity-deck counts, color/suit ecology, equipment/delayed-trick density, opening hand, kill rewards, death discard, or deck exhaustion: read [identity-card-environment.md](identity-card-environment.md).
- Foundational card categories, printed general-card skills versus current skills, delayed/non-delayed trick distinction, equipment positions/replacement, equipment-as-card/cost dependency, or equipment stacking: read [card-glossary.md](card-glossary.md).
- Foundational zones, “场上”, ownership versus area, hidden-hand choice, processing-area cards, judgment-area identity, or draw-pile refill/exhaustion: read [zone-glossary.md](zone-glossary.md).
- Foundational points, HP/HP value/maximum HP/lost HP, hand limit, damage base, distance/range, X, assignment, extrema, counts, or halves: read [value-glossary.md](value-glossary.md).
- Foundational labels/agency, sequential versus simultaneous operations, damage transfer, HP loss/recovery, user/source/channel, option legality, role/target references, or visibility: read [description-glossary.md](description-glossary.md).
- Foundational turn order, extra turns/phases, skipped procedures, phase boundaries, outside-turn scope, dying/death, or kill attribution: read [flow-glossary.md](flow-glossary.md).

## Selection Rule

Choose at most one main mechanism family for an ordinary general. A second mechanism may appear only as a small support tool or drawback. If the source material is only flavor inspiration, translate it into ordinary 三国杀 wording instead of importing the full mechanism.

For custom generals, prefer mechanisms that are:

- intuitive without a long glossary;
- visible or auditable at the table;
- tied to the character's anchor rather than added for novelty;
- robust around timing, ownership, zones, and common cards such as【桃】and【酒】.

Use low-priority or mode-heavy mechanisms only when the user explicitly asks for that style, the character is a mode centerpiece, or the object/mechanism is the character's actual fantasy.

## Short Cautions

- Do not combine several high-burden systems, such as delayed casting, public zones, charge points, special cards, and extra decks, in one normal general.
- Special zones and extra decks need entry, cap, ownership, visibility, and leaving rules.
- Virtual or generated cards need exact names or clear category wording; check survival cards and response timing.
- Package names are not universal permission. 国战 material should be translated cautiously unless the user asks for a 国战 design.
- If a mechanism changes timing, phase/turn flow, damage, dying, card use, or targets, also read the `Timing Map` section in `design-heuristics.md`.
- If a skill names a specific ordinary card, relies on a card color/suit/category appearing, or repeatedly searches the normal deck, check `identity-card-environment.md` instead of assuming all names and categories are equally available.
- If a skill manipulates equipment or card categories, check `card-glossary.md` before choosing movement/conversion wording; “使用”, “置入”, “移动”, “弃置”, and “当其他牌使用” are not equivalent.
- If a skill says “其牌”“其区域内的牌”“场上的牌” or touches the processing/judgment area, check `zone-glossary.md`; zone membership does not automatically imply ownership or permission to choose/operate a card.
- If a skill sets a value, uses HP/max HP, distance/range, X, maximum/minimum, most/least, or half, check `value-glossary.md`; zero, ties, direction, and “为/视为” can change the result.
- If wording uses “任意数量”“依次”“转移”“需/须/可以”, changes attribution, presents options, or refers to targets after transfer/chain, check `description-glossary.md` and preserve the workspace “并/然后” convention.
- If a skill grants, repeats, skips, or ends a turn/phase, works outside every character's turn, or references dying/death/kills, check `flow-glossary.md`; do not equate extra turns with extra phases or death with being killed.

## Future Updates

When adding future mechanism material, update the smallest relevant slice and keep this index current. Extract definition, use case, guardrails, package/mode scope, priority, and one compact wording pattern only when the mechanism has a stable shape.
