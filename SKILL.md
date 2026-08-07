---
name: sanguosha-general-designer
description: Design, critique, rebalance, and name 三国杀 custom generals and skill groups. Use when the user asks to create or revise 三国杀武将技能, check skill linkage and balance, design 宗族技, adapt a historical or fictional character into concise 2-4 skill designs, or generate称号/战功/技能名/牌名/标记名/衍生牌名.
---

# Sanguosha General Designer

## Task Modes

Classify the user request before loading references:

- Fresh design: create a new 2-4 skill group from a character, story, play role, or required mechanism.
- Review/rebalance: diagnose an existing draft, compare versions, or solve named problems such as survival, timing insertion, rigidity, or excessive marks.
- Naming: generate or revise称号、战功名、技能名、牌名、标记名, or衍生牌/对象名.
- Reference intake: absorb new articles, documents, or package material into the skill itself.

For every fresh design or review, read `references/rules-priority.md` first, then use `references/README.md` to route only the focused files needed by the current skeleton. The foundational rules distilled from the reviewed `gltjk.com` pages and identity-mode material outrank design heuristics, mechanism essays, package vocabulary, and flavor.

## Workflow

Default to an interactive design conversation unless the user explicitly asks for an immediate complete draft or already provides enough constraints. At each turn, give one sentence of state update, then do exactly one of: ask 1-3 focused questions, present a small set of alternatives, or produce the requested draft/review. Do not repeat the full skill group or all loaded references after every answer. If the user says “直接设计”“按你的判断继续” or gives a complete brief, state assumptions and proceed.

Use this single order:

1. **Rules gate**: read `references/rules-priority.md`; after the skeleton exists, read only the foundational glossaries hit by the draft and record them in the working card.
2. **Brief**: identify character/source, mode, faction/health, role fantasy, complexity, required/forbidden mechanics, and official-like versus experimental language. Ask only what would change the design.
3. **Anchors**: reduce the character to 1-3 usable facts, including positive capability and negative compulsion. Choose the design发端: 立意驱动、隐喻驱动、玩法驱动, or命题作文.
4. **Play line**: choose the primary action, resource, or timing window. Do not start from a linkage diagram. If a special mechanism is named, route through `references/README.md` and `references/mechanics-index.md`.
5. **Skeleton**: choose the number of skills by function, not convention: usually 2-4, but never pad to three. Assign each skill a trigger, job, cost, payoff, and unresolved choice before polishing text.
6. **Rules language**: for each skill, resolve object, timing, agency/cost, resolution, attribution, target, and state availability; then check type label, condition, effect, and aftereffect/price. For timing-heavy text, place the trigger on a game, turn/phase, card-use/target/resolution, damage/dying/death, or skill-resolution line.
7. **Linkage and pressure**: classify each skill pair as strong link, soft support, division of labor, intentional tension, or independent coverage. Strong linkage needs a reason; do not weaken one skill merely to feed another. Test team play, solo play, low-resource turns, and the strongest obvious abuse only after legality is sound.
8. **Output**: use the interim format while decisions remain open; use the full format only for a complete draft/final version. For review, list findings and priorities before the revision.
9. **Intake**: when absorbing new material, preserve the source in `.codex/source-check/`, merge reusable knowledge into the closest reference, validate, and make a local commit unless the user asks to review first.

Before final output, scan for blank card-name placeholders and run the final self-check below. No output may contain `【】`, `【 】`, `【牌名】`, `【某牌】`, or similar blank slots.

## Working Card

Before writing final skills, build a small internal working card. Use it to keep references actionable instead of reciting them:

```text
任务类型：
约束：
人物锚点：
发端：
主定位/副定位：
主资源轴：
时机线：
规则命中：card / gamecard operations / herocard operations / zone / value / description / flow / event / identity environment
技能关系：
主要风险：
```

For simple requests, this card can stay implicit. For reviews, expose the relevant parts as the design explanation.

## Design Rules

Keep skill groups readable. Target 2-4 skills and avoid excessive marks, hidden counters, repeated prompts, or nested delayed effects.

Do not default to exactly three skills. Choose the count by function: 2 for a clean compact design, 3 for a natural main/support/drawback or main/branch/identity split, and 4 only when a separate rule label, clan skill, transformation, or mode mechanic would make a longer combined skill harder to read.

Assume a design should be playable in face-to-face tabletop games unless the user explicitly asks for online-only or mode-only work. Avoid routine random deck search, large mini-games, opaque system checks, excessive skill rewriting, and cross-turn memory that cannot be represented by visible cards or simple current-window history.

Do not design from a linkage diagram first unless the user explicitly asks for a combo engine. Start with character anchors and role shape; let synergy emerge only where it makes the skills more natural. A clean independent defensive skill, drawback, or coverage skill is better than an artificial trigger chain.

Do not solve power problems only by adding "每回合限一次" unless the user accepts that route. Prefer changing costs, targets, card classes, conversion rules, or locked drawbacks.

Use "锁定技" only when the whole skill is compulsory. Do not create half-locked text where only one clause is mandatory; split the skill or rewrite the timing if needed. When a locked skill is appropriate, use it for unavoidable temperament, structural constraints, identity, or negative consequences. Before writing one, choose whether it expresses 性, 名, 象, 局, or 命.

Respect wording conventions when the user defines them. In this workspace, treat "并" as requiring the previous part to execute before the latter part can execute; treat "然后" as allowing the later part if any previous part executed.

For conditional chains, resolve the verbs in order. “并” is a gate: if the preceding action cannot execute, stop that branch. “然后” is a continuation: continue if the preceding clause executed at least partly. Never use “然后” merely to make two unrelated effects sound linked, and never use “并” when the latter effect should remain available after a failed cost or target choice.

Avoid unrestricted duplication or creation of survival cards such as【桃】and【酒】unless the whole design is balanced around that pressure.

When using transverse states such as横置/重置, account for state availability: a role initially counts as重置; a横置 role must be重置 before it can be横置 again, and vice versa.

If a draft mentions damage prevention, target changes, dying, phase ending, extra turns, or HP/max-HP adjustment, run the timing recognition check from `references/design-heuristics.md` before final wording.

When a design creates, searches, materializes, or repeatedly references a nonstandard card-like object, name the object explicitly. This includes衍生牌、专属牌、虚拟牌、标记牌、额外牌堆牌, and named card tokens. If a named object is not needed, say so instead of leaving the naming result blank.

Never leave a card-name position blank inside skill text. If the effect needs an existing named card, write the exact card name, such as【杀】、【决斗】、【无中生有】. If the exact card name is not necessary or not known, remove the brackets and write the category directly, such as "一张基本牌", "一张非延时类锦囊牌", or "一张伤害类牌". If the design needs a new card name, choose a provisional name and define it in the衍生牌/对象名 line.

## Clan And Family Skills

For宗族技, first determine the character's life-story orientation, then choose the corresponding design language. Do not automatically use every branch of the family mechanic.

When a clan has several members, design on three layers: family commonality, the individual's branch of that commonality, and linkage with existing clan members. Read `references/design-heuristics.md` for family examples from the referenced essays.

For太原王氏的〖中流〗, use these meanings:

- 装备区: "中流砥柱", for figures defined by公辅、三公、社稷支撑、器任担当.
- 本回合弃牌堆: "中流击水", for figures defined by乱世行动、战功、事功、主动入局.
- 虚拟牌: "中流却遇风波", for figures defined by事变、失利、危局、凭空生波, or talent/desire that turns into backlash.

After choosing an orientation, make the other skills speak that language consistently. Hybridize only when the user's requested character genuinely spans multiple meanings.

## Output Shape

When presenting a design, use this compact form:

```text
武将名 势力 体力/上限

技能名：技能文本。
技能名：技能文本。
技能名：技能文本。

按需要列出2-4个技能；不要为了凑三技能而增加技能。

衍生牌/对象名：若技能创造或依赖非标准牌、专属牌、虚拟牌、标记牌、额外牌堆牌, list each name as【牌名】/【对象名】 with category, brief rule role, and naming reason. This supplements the skill text and does not replace filled card names inside the skills. If the user asked for card names but no named object is recommended, state "不建议新增牌名：" and give the reason plus the simpler wording route.

设计说明：定位、主玩法、联动或分工、强度阀门、单挑空间。
可调参数：若偏强/偏弱，优先改哪些字。
```

When reviewing a user draft, compare versions by:

- main game plan and whether each skill has work to do;
- internal relationships: linkage, division of labor, intentional tension, or healthy independence;
- insertion-timing risks;
- over-strength sources, especially free牌、回血、防伤、额外使用;
- complexity and标记 count;
- whether fixes preserve the user's intended fantasy.

During an interactive draft, use a smaller interim format:

```text
当前结论：已确定的人物锚点、定位和限制。
当前方案：技能数量及每个技能的工作，不写尚未决定的牌名或数字。
联动关系：强联动/软支持/分工/张力/独立覆盖，并说明理由。
待确认：最多3个会改变方案的选择。
```

Only use the full `Output Shape` after the user asks for完整技能组、定稿、最终版或同等意思。对评审请求，先列问题和优先级，再给修改稿；不要把未经用户确认的多个版本混成一个最终答案。

When the user asks for称号, 战功名, 技能名, 牌名, 标记名, 衍生牌名, or flavor naming, read `references/naming-titles.md`.

## Final Self-Check

Before finalizing a design or review, run `references/rules-priority.md` first. Rules legality and the user's explicit conventions outrank character metaphor, linkage, balance targets, mechanism novelty, and official-looking prose. Then verify:

- each skill has a clear timing, condition, cost/action, and payoff, unless it is a pure static rule;
- the chosen timing matches whether the event is prevented, modified, confirmed, or already finished;
- internal relationships are natural: strong link, soft support, division of labor, intentional tension, or healthy independence;
- no skill is weakened only to feed another skill;
- no unrestricted【桃】/【酒】creation, free extra turns, broad damage prevention, or oppressive target denial slipped in;
- all marks, stored cards, virtual cards, special zones, and generated card names have visible handling;
- no blank card brackets or placeholder names remain.
- extra turns, extra phases, skipped procedures, outside-turn durations, nested dying, and maximum-HP-to-0 death follow `references/flow-glossary.md` when relevant.
- event insertion, invalidity, ignoring, counteraction, target cancellation, and effect scope follow `references/event-glossary.md` when relevant.

Also check the conversation state: answer the user's latest requested stage, preserve confirmed choices, and do not reopen a settled question unless a later rule makes it inconsistent.

## Reference Routing

Use `references/README.md` as the single directory map. It routes the rules-first gate, focused foundational glossaries, design heuristics, mechanism slices, naming guidance, and source provenance without requiring the full knowledge base to be loaded at once.

When adding new material to the skill, update `references/source-digests.md` with a one-line provenance note and update only the reference section that would actually change future designs.

