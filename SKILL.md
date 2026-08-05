---
name: sanguosha-general-designer
description: Design, critique, rebalance, and name 三国杀 custom generals and skill groups. Use when the user asks to create or revise 三国杀武将技能, check skill linkage and balance, design 宗族技, adapt a historical or fictional character into concise 2-4 skill designs, or generate称号/战功/技能名.
---

# Sanguosha General Designer

## Core Workflow

Design from the proper发端 first, then translate the character into concise card-game language.

1. Gather the user constraints: character, faction/health, intended role, must-use mechanics, forbidden patterns, target complexity, and whether the user wants a fresh design or a review.
2. Read provided sources. If the user gives URLs or asks for current/external material, browse them and cite the sources used. If the useful material is already bundled, read the relevant file under `references/`.
3. Decide the design发端: 立意驱动, 隐喻驱动, 玩法驱动, or 命题作文. Do not force all characters into the same process.
4. Identify 1-3 character anchors: deeds, temperament, relationships, failure mode, iconic object, or desired play experience. Separate positive capability from negative compulsion.
5. Choose one main mechanical language for each anchor. Do not include every possible motif merely because it exists.
6. Draft 2-4 skills with short text, explicit timing, and few moving parts. Prefer one engine, one support/output skill, and one locked drawback or identity skill when needed.
7. Check internal linkage: each skill should either feed, constrain, convert, or cash out another skill. Avoid isolated "plus one value" text.
8. Check table health: support should create decisions for allies and enemies, not only unconditional resources. Solo play should retain operation through target choice, card type choice, timing, or risk management.
9. If the user provides new mechanism reference material and asks to improve the skill, read it, extract use cases and guardrails, then fold it into `references/mechanics-and-special-cards.md` instead of leaving a raw dump.

## Design Rules

Keep skill groups readable. Target 2-4 skills and avoid excessive marks, hidden counters, repeated prompts, or nested delayed effects.

Do not solve power problems only by adding "每回合限一次" unless the user accepts that route. Prefer changing costs, targets, card classes, conversion rules, or locked drawbacks.

Use "锁定技" only when the whole skill is compulsory. Do not create half-locked text where only one clause is mandatory; split the skill or rewrite the timing if needed. When a locked skill is appropriate, use it for unavoidable temperament, structural constraints, identity, or negative consequences. Before writing one, choose whether it expresses 性, 名, 象, 局, or 命.

Respect wording conventions when the user defines them. In this workspace, treat "并" as requiring the previous part to execute before the latter part can execute; treat "然后" as allowing the later part if any previous part executed.

Avoid unrestricted duplication or creation of survival cards such as【桃】and【酒】unless the whole design is balanced around that pressure.

When using transverse states such as横置/重置, account for state availability: a role initially counts as重置; a横置 role must be重置 before it can be横置 again, and vice versa.

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

设计说明：定位、主联动、强度阀门、单挑空间。
可调参数：若偏强/偏弱，优先改哪些字。
```

When reviewing a user draft, compare versions by:

- main game plan and whether each skill has work to do;
- internal linkage and insertion-timing risks;
- over-strength sources, especially free牌、回血、防伤、额外使用;
- complexity and标记 count;
- whether fixes preserve the user's intended fantasy.

When the user asks for称号, 战功名, 技能名, or flavor naming, read `references/naming-titles.md`.

## References

Read `references/design-heuristics.md` when a task needs deeper design principles, clan-skill interpretation, balance review, or source-inspired design philosophy.

Read `references/mechanics-and-special-cards.md` when a task can benefit from existing 三国杀 mechanisms, special cards, special zones, extra decks, package-scoped vocabulary, or user-reviewed cards from selected packages. Prefer normal-priority mechanism families, treat low-priority special equipment as object-specific inspiration only, and use 国战 cards cautiously unless the user asks for a 国战 design.

Read `references/source-digests.md` when the user asks where the design principles came from, wants to add new source material to the skill, or needs a quick map of absorbed online/offline references.

