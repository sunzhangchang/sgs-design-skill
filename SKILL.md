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

For fresh design or review, usually read `references/design-heuristics.md`. Read `references/mechanics-index.md` first, then only one focused mechanics file, when the user names a mechanism/package/special card, asks for one, or the draft already uses one. Read `references/naming-titles.md` only for naming tasks or when the design creates a named nonstandard object.

## Interactive Design Protocol

Default to an interactive design conversation unless the user explicitly asks for an immediate complete draft or already provides enough constraints.

Use small steps:

1. Brief: identify character/source, mode, faction/health if known, role fantasy, complexity limit, required/forbidden mechanics, and whether the user wants official-like or experimental language. Ask only the 1-3 missing questions that would most change the design.
2. Anchors: propose 1-3 usable character anchors and separate positive capability from negative compulsion. Ask the user to confirm, reject, or add an anchor.
3. Mechanical direction: propose 2-3 possible resource axes or timing lines. If a route needs special mechanics, read `references/mechanics-index.md` and the one focused slice it routes to after the user chooses or indicates interest.
4. Skeleton: propose the skill count and each skill's job before writing final text. Use two skills for focused designs, three when main play/support/drawback naturally separate, and four only when an identity skill, awakening/limited turn, clan branch, or mode rule genuinely needs its own slot.
5. Draft: write the complete skill group, then explain main play line, internal relationship, risks, and adjustable words. If the user continues, revise from the user's chosen concern rather than restarting.

Do not ask for every possible constraint at once. After each user answer, update the internal working card, state what became clear, and ask the next narrow question or present the next small decision. If the user says to proceed with assumptions, proceed and name the assumptions briefly.

## Core Workflow

Design from the proper发端 first, then translate the character into concise card-game language.

1. Gather the user constraints: character, faction/health, intended role, must-use mechanics, forbidden patterns, target complexity, and whether the user wants a fresh design or a review.
2. Read provided sources. If the user gives URLs or asks for current/external material, browse them and cite the sources used. If the useful material is already bundled, read the relevant file under `references/`.
3. Decide the design发端: 立意驱动, 隐喻驱动, 玩法驱动, or 命题作文. Do not force all characters into the same process.
4. Identify 1-3 character anchors: deeds, temperament, relationships, failure mode, iconic object, or desired play experience. Separate positive capability from negative compulsion.
5. Choose one main mechanical language for each anchor. Do not include every possible motif merely because it exists.
6. For each skill, check the structure: type label, timing, condition, cost/action, effect, and aftereffect/price. For timing-heavy text, first place the trigger on a line: game, turn/phase, card-use/target/resolution, damage/dying/death, or skill resolution; then decide whether the referenced event has not started, is being modified, has become certain, or has already finished. Missing timing, fake costs, and overstuffed effects are common failure points.
7. Draft as many skills as the design actually needs, normally 2-4, with short text, explicit timing, and few moving parts. Prefer one main play line plus optional support, coverage, contrast, or drawback; do not force every skill into the same engine or pad the group to three skills.
8. Check internal relationships without overfitting linkage. A skill may strongly link, weakly support, cover a role gap, create intentional tension, or stand mostly independent if it preserves character fit and table experience. Prefer natural linear/support/implicit links; avoid forced linkage and high-risk insertion links.
9. Check table health: support should create decisions for allies and enemies, not only unconditional resources. Solo play should retain operation through target choice, card type choice, timing, or risk management.
10. Before presenting final skill text, scan every skill description for unresolved placeholders, especially empty card-name brackets. No output may contain `【】`, `【 】`, `【牌名】`, `【某牌】`, or similar blank slots.
11. If the user provides new reference material and asks to improve the skill, read it, extract reusable design knowledge, and merge it into the closest reference file instead of leaving a raw dump. Keep fetched source text in a workspace-local check folder until the user confirms the absorption is correct; only then clean temporary source files, validate, and commit. If the material only restates existing guidance, say so and avoid no-op edits.

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

Avoid unrestricted duplication or creation of survival cards such as【桃】and【酒】unless the whole design is balanced around that pressure.

When using transverse states such as横置/重置, account for state availability: a role initially counts as重置; a横置 role must be重置 before it can be横置 again, and vice versa.

If a draft mentions damage prevention, target changes, dying, phase ending, extra turns, or HP/max-HP adjustment, run the timing recognition check from `references/design-heuristics.md` before final wording.

When a design creates, searches, materializes, or repeatedly references a nonstandard card-like object, name the object explicitly. This includes衍生牌、专属牌、虚拟牌、标记牌、额外牌堆牌, and named card tokens. If a named object is not needed, say so instead of leaving the naming result blank.

Never leave a card-name position blank inside skill text. If the effect needs an existing named card, write the exact card name, such as【杀】、【决斗】、【无中生有】. If the exact card name is not necessary or not known, remove the brackets and write the category directly, such as "一张基本牌", "一张普通锦囊牌", "一张非延时锦囊牌", or "一张伤害类牌". If the design needs a new card name, choose a provisional name and define it in the衍生牌/对象名 line.

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

When the user asks for称号, 战功名, 技能名, 牌名, 标记名, 衍生牌名, or flavor naming, read `references/naming-titles.md`.

## Final Self-Check

Before finalizing a design or review, verify:

- each skill has a clear timing, condition, cost/action, and payoff, unless it is a pure static rule;
- the chosen timing matches whether the event is prevented, modified, confirmed, or already finished;
- internal relationships are natural: strong link, soft support, division of labor, intentional tension, or healthy independence;
- no skill is weakened only to feed another skill;
- no unrestricted【桃】/【酒】creation, free extra turns, broad damage prevention, or oppressive target denial slipped in;
- all marks, stored cards, virtual cards, special zones, and generated card names have visible handling;
- no blank card brackets or placeholder names remain.

## Reference Routing

Choose the smallest reference set that answers the task:

- Read `references/design-heuristics.md` for ordinary design/review tasks that need deeper design principles, timing-point recognition, clan-skill interpretation, locked-skill diagnosis, balance valves, or source-inspired design philosophy.
- Read `references/mechanics-index.md` for named mechanisms, special cards, special zones, extra decks, package-scoped vocabulary, or user-reviewed package material. Then read only the focused file it routes to under `references/mechanics/`. Prefer normal-priority mechanism families, treat low-priority special equipment as object-specific inspiration only, and use 国战 cards cautiously unless the user asks for a 国战 design.
- Read `references/naming-titles.md` when the user asks for称号、战功名、技能名、标记名、衍生牌名, or similar flavor naming.
- Read `references/source-digests.md` when the user asks where principles came from, provides new source material to absorb, or needs a map of absorbed online/offline references.

When adding new material to the skill, update `references/source-digests.md` with a one-line provenance note and update only the reference section that would actually change future designs.

