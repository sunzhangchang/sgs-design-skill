# Rules-First Priority Gate

Read this compact gate for every fresh design and every review before choosing or polishing mechanisms. It does not replace the focused glossaries; it determines which knowledge wins and which glossary must be opened.

## Authority Order

Apply knowledge in this order:

1. The user's explicit current constraints and workspace conventions, including the defined dependency meanings of “并/然后”.
2. The foundational game rules distilled from the reviewed `gltjk.com` rules pages and the user-provided identity-mode material.
3. Character fit, design heuristics, balance, internal relationships, and table experience.
4. Mechanism essays, package-specific vocabulary, unusual cards, and experimental concepts.
5. Flavor resemblance, novelty, and decorative wording.

A lower layer may choose among legal implementations but may not redefine a higher layer. If a character metaphor or desired combo requires an illegal or ambiguous event, timing, zone, value, target, or card operation, repair the implementation rather than weakening the rule interpretation.

## Mandatory Rule Scan

For each proposed skill, identify only the rows it touches and open the linked focused reference before final wording:

| Skill touches | Required reference |
| --- | --- |
| Card category, delayed trick, equipment slot/replacement/dependency, printed versus possessed skill | `card-glossary.md` |
| Use/play/recast/place/discard/give/gain/lose/reveal/view/exchange/judge/treat-as operation | `gamecard-operations.md` |
| Horizontal/reset/chain/flip state of a general card and chain-damage inheritance | `herocard-operations.md` |
| Zone, ownership, visibility, processing/judgment area, draw/discard pile | `zone-glossary.md` |
| Points, HP/max HP, hand limit, damage value, distance/range, X, extrema, division | `value-glossary.md` |
| Optional/mandatory wording, sequential operations, transfer, attribution, options, actor/target | `description-glossary.md` |
| Turn/phase order, extra or skipped flow, outside-turn duration, dying/death/kill | `flow-glossary.md` |
| Event insertion, response/resolution, invalid/ignore/counteract/cancel, effect scope | `event-glossary.md` |
| Identity-deck density, suit/color/name availability, opening hand, kill/death rewards, exhaustion | `identity-card-environment.md` |

Do not load every glossary in full. Use this table as the always-read gate, then load only the references hit by the actual skeleton or draft.

## Legality Before Quality

Review in this order:

1. **Object**: identify the card, character, skill, event, value, or zone being operated.
2. **Timing**: identify the event line and whether the skill acts before, during, or after it.
3. **Agency and cost**: identify who chooses, who acts, what must successfully execute, and whether partial execution is allowed.
4. **Resolution**: identify insertion, target/effect changes, continuation, cleanup, and duration.
5. **Attribution**: identify user, source, channel, owner, area, and kill attribution when relevant.
6. **Design quality**: only then judge character fit, linkage, balance, complexity, and play experience.

If a draft fails layers 1-5, do not defend it using flavor or intended balance. State the rules problem first, then offer a legal implementation that preserves the design anchor as closely as possible.

## Final Rule Gate

Before outputting complete skill text, verify:

- every noun names an existing or explicitly defined game object;
- every timing belongs to a valid event or flow boundary;
- every choice, cost, and later clause has a legal execution path;
- zones, ownership, visibility, values, and targets do not rely on colloquial assumptions;
- inserted events and interrupted resolutions have an explicit continuation point;
- “无效”“无视”“抵消”“取消目标”, and “死亡”“杀死” are not interchanged;
- package or experimental mechanics do not override foundational semantics;
- user-defined conventions are preserved where they explicitly override a reviewed source.
