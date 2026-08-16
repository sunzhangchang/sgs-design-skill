# Contest Design Evaluation

Use this reference when reviewing contest submissions, absorbing judge feedback, or evaluating a draft at contest-level strictness. Contest samples are aesthetic and practical evidence, not rules authority; `rules-priority.md` and the foundational glossaries remain higher priority.

## Read The Whole Sample

Treat the entire sample as context:

- contest/round and the stated design requirement;
- the introductory historical biography or character brief;
- character, title, HP/maximum HP, and skill count;
- skill text and design explanation;
- the three judge scores and comments after the `【字数】` field.

The opening file-format explanation is a parsing instruction, not a requirement for the new design. Do not transfer a sample's HP, skill count, or historical character to a new task unless the user explicitly carries it over.

Separate each sample into:

```text
命题约束：比赛要求、体力、技能数、指定人物
人物语境：简介、生平、关键事迹、性格与失败点
设计实现：技能文本、称号、设计思路
评委证据：三位评委的分数与具体意见
可复用结论：能迁移到其他武将的评价标准
```

Do not average scores blindly. First identify what each judge is measuring: formal structure, actual play, or theme/table practicality. A disagreement is useful evidence about a risk boundary, not automatically an error by one judge.

## Evaluation Rubric

Evaluate in this order, after rules legality:

1. **命题与人物映射**: Does the skill use the biography's actual deed, temperament, relationship, or failure mode? Is the title and design explanation consistent with the mechanism? A clever template without a character connection is a serious deduction.
2. **玩家欲望与主循环**: What does the player want to do each turn? Does the skill create a reason to build, maintain, spend, or risk its resource? If the metaphor is construction or accumulation, continued construction should be attractive rather than rewarding only one-time setup or immediate liquidation.
3. **反馈方向与资源趋势**: Do costs and rewards move in the same narrative direction? Construction, equipment, marks, cards, or stored objects should not accidentally shrink when the fiction says the structure is growing unless the reversal is deliberate.
4. **最优解与反直觉玩法**: Find the strongest low-effort line first. Check free repeated use, defensive-card abuse, high-value trick cards, setup-before-draw bypasses, avoiding the skill entirely, or forcing opponents/allies to choose a negative option. If the rational player should ignore the central action, the fantasy has failed.
5. **结构与操作负担**: Count distinct choices, branches, state changes, searches, and remembered objects. A compact skill with a few meaningful options is preferable to a long list of loosely related options. More than four parallel options needs a strong structural reason; five or more is presumptively a consolidation candidate.
6. **互动与角色定位**: A support/buff skill should create decisions for its user, allies, and enemies. Check meaningful enemy response, unconditional team resources, and whether solo play retains target, timing, card, or risk choices.
7. **面杀可执行性**: Can players verify “本回合/本轮失去过的牌”, remembered categories, hidden information, repeated searches, and multi-step allocation without software? If not, define a visible zone/object or simplify the memory requirement.
8. **规则与结算表达**: Check operation verbs, event timing, target legality, source/channel attribution, and clause executability using the foundational rule files.

## Sample 1 Lessons

The `康绚` submission required “4 HP, 1 skill”, so compression and one recognizable construction metaphor were part of the challenge. The samples show:

- A visible-card “dam” with repeated virtual use had a clear object, but arbitrary high-value cards and equipment-as-card handling created power and rules risks. The player could stop building and exploit existing stock, so the construction fantasy did not create continued desire.
- A conversion skill linked the dam to equipment, but spending equipment made the structure shrink. Its branches were weakly linked and one mode could be bypassed by acting before drawing. Resource direction, branch necessity, and timing bypass must be checked separately.
- A seven-option public effect was cumbersome, grouped repeated draw/discard/transverse/damage effects, and could make the best line be never activating the skill. Universal ally/enemy access does not create interaction by itself; without structure it becomes a buff machine with negative options.
- An extra-turn design scored best because its positive feedback and “天意难违” restriction created a continuing reason to use the mechanism and connected to the character story. Its remaining risks were tabletop tracking of “cards lost last turn”, retrieval/search burden, and the need for a visible auditable memory method.

Transferable conclusion: preserve the character's central action, make the intended action rationally attractive, align resource movement with the metaphor, and make memory/operation costs visible at the table. Do not copy a sample's exact mechanism merely because it scored well.

## Contest Review Format

Lead with findings rather than a single score:

```text
命题完成度：
人物语境使用：
主循环与玩家欲望：
资源趋势与正负反馈：
最优解/滥用线：
结构与操作负担：
互动性与单挑空间：
面杀可执行性：
规则与措辞风险：
```

Then distinguish致命问题、主要扣分项、可调问题和具体优点. When judges disagree, report the disagreement explicitly and test both readings: “结构上有意思但实战不清晰”, “主题贴合但玩法最优解反常”, and “玩法成立但人物不像” are distinct diagnoses.
