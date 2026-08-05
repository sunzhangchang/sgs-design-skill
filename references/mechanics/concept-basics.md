# Mechanism Concept Basics

This file is a focused slice split from `../mechanics-and-special-cards.md`. Read it only when the index routes here for the current design need.

## Mechanism Priority Evaluation



Use this section only to judge whether a mechanism is worth choosing. It does not require writing every referenced mechanism into a new design.



First distinguish concept scale:



- 新概念: small expansion that improves text recognition or play texture without rewriting the game body, such as a concise operation, timing label, or shortcut term. Prefer this scale for ordinary generals.

- 新机制: structural rule update that changes core assumptions, zones, identity, slots, or table procedures. Use only when the character or mode genuinely needs the larger rule burden.



Classify the concept type:



- 创新型: gives a new operation or resolution route. Prioritize only if the action opens real decisions rather than novelty alone.

- 简化型: compresses repeated long text. Prioritize when the shortcut is intuitive and broadly reusable; reject over-compressed jargon that makes players decode more, not less.

- 技术型: has little standalone meaning but binds to another rule, such as compulsory execution or formation handling. Use when it clarifies timing or enforceability; avoid using it as decorative terminology.



Rank candidate mechanisms by three axes:



- 创新性: Does it add a distinct operation, decision, or expressive channel unavailable through simpler existing wording? "Official" or "new" does not by itself mean good.

- 泛用性: Does it match common character anchors, and can most players accept its effect on game experience? A one-character mini-game or a rule that deprives others of their core objective is low priority.

- 周全性: Does it coexist with existing rules, public resources, zones, and common edge cases? Watch for shared-resource congestion, hidden memory burden, unclear timing, and loops that are only "fixed" by banning pairings.



Apply source-neutral definition discipline:



- Do not accept or reject a concept merely because it is official, non-official, standard-looking, or nonstandard-looking. Require a stable rules definition and judge whether that definition improves this design's communication.

- When using a non-mainstream concept, either define it briefly in local wording or write the skill so the definition is self-evident. Unified terminology should reduce misunderstanding; it should not force every design into the same style.



Priority guide:



- High priority: intuitive, reusable, low-conflict, and either genuinely expressive or a clear text saver. Use early when it fits the character.

- Medium priority: useful but context-sensitive, mode-tinted, or carrying some timing/zone burden. Use with explicit guardrails.

- Low priority: narrow mini-game, heavy structural rule, large public-resource footprint, unclear flow, or mostly official precedent without design necessity. Use only when the user's brief strongly points there.



For simplification mechanisms, prefer words that are both visible and self-explanatory. A short keyword is worse than full text if the player must already know several hidden definitions to understand the skill.



## Technical Labels



Use technical labels only when the called rule is clear and useful. They are not flavor words.



### 锁定技



- Role: a technical label binding the whole skill to compulsory execution.

- Use when: all clauses of the skill are mandatory, or the design wants to remove prompts and express unavoidable structure.

- Avoid when: only one clause is compulsory, the skill contains "你可以", or the label is being used merely to imply a drawback.

- Wording guardrail: no half-locked skills. If part A is optional and part B is compulsory, split them, make the whole skill compulsory, or remove the locked label.

- Priority: high泛用 but low周全 if used loosely; be stricter than casual official precedent.



### 阵法技 / 君主技 / 宗族技



- Role: technical labels that call external framework rules, identity display, or mode/package handling.

- Use when: the design environment recognizes the label and the character genuinely belongs to that framework.

- Avoid when: the label does not change readability, targeting, visibility, or family/mode interaction.

- 阵法技 has higher innovation when seat/formation is the actual play object, but lower generality and needs careful edge-case handling.

- 君主技 is narrow; use only for true lord-mode designs.

- 宗族技 is suitable for clan packages when the shared label helps players see family membership or inherit a common design language. The individual skill still needs to work as rules text even if the label is removed.



## Limited, Awakening, Task, And Count Concepts



Use these concepts when a design changes long-term availability, creates a transformation, or asks the player to complete a task. Their names carry strong presentation weight; do not use them merely as strength patches.



### 限定技 / 觉醒技



- Definition: 限定技 is normally once per game; 觉醒技 is a compulsory transformation after a condition is met.

- Use when: the character has a true decisive move, rebirth, transformation, or irreversible turning point.

- Priority: normal for major designs, low for ordinary small payoffs.

- Guardrails: a limited skill should feel worth remembering but not force the whole table to pre-emptively kill the character. Awakening should preserve some identity before and after transformation; avoid making the pre-awaken and post-awaken forms feel like unrelated generals. If awakening changes max HP, skill set, or faction-like identity, state all lasting changes precisely.

- Avoid when: the effect is just a one-time minor bonus, a disguised normal skill, or a balance patch for an otherwise bland design.



### 可重置限定技 / 昂扬技 / 蓄势技 / 更始技



- Definition: a once-per-game or high-impact skill can become available again through a condition.

- Use when: the "recharged decisive move" is itself the fantasy, such as renewed morale, stored power, or a rare second wind.

- Priority: medium for hard, flavorful reset conditions; low for easy routine resets.

- Guardrails: reset difficulty should match effect size. Easy resets require smaller effects and may lose the special feeling of a limited skill. Do not combine unrelated reset routes only for strength; if the reset is tied to shuffle/deck exhaustion, check whether the game usually lasts long enough.

- Avoid when: the skill effectively becomes "once per turn with extra animation".



### 重置技能 / 行置 / 视为满足觉醒条件



- Definition: a rule treats a skill as unused, used, or ready to awaken.

- Use when: the character explicitly manipulates skill availability or another character's turning point.

- Priority: low to medium; very context-sensitive.

- Guardrails: distinguish resetting use count from removing delayed effects or rewinding state. Prefer "次数上限+1" or an explicit extra use when that is the real effect. Let a skill reset only the user's own skills unless the brief needs invasive control. For awakening manipulation, change only the condition unless the timing and lasting changes are clear.

- Avoid when: delayed skill effects, conversion states, or cards stored by that skill would require retroactive cleanup.



### 全局计次 / 蓄力技 / 奋武技 / 次数封装 / 轮巡年



- Definition: a skill tracks uses across the game, round, phase, deck cycle, or a dynamic value.

- Use when: long-term rhythm matters more than a simple per-turn cap.

- Priority: medium for direct "每X限N次"; low for decorative count labels or shared gauges.

- Guardrails: state whether count belongs to the character, skill, or named resource, and what happens if the skill is lost, stolen, disabled, or regained. Use 轮/巡/年 only when the table can remember the boundary; 轮 is shared, 巡 is personal, 年/deck-cycle is low-frequency and mode-sensitive.

- Avoid when: an ordinary "每阶段限一次", "每轮限一次", or marker would communicate the same thing.



### 玩点蓄力技 / 数值蓄力



- Definition: a skill distinguishes input numbers from output numbers; when a paid cost or checked condition reaches at least twice the stated input, selected output numbers are doubled for that resolution. This is different from charge-marker skills that store a named resource.

- Use when: the character saves force, overpays, waits for a large condition, or compresses several turns of preparation into one burst.

- Priority: medium-low. It is expressive and flexible, but template-heavy and easy to turn into math spectacle.

- Guardrails: state whether the input is a cost or a condition, which numbers can double, and when the doubled value is locked. Keep output doubling small; damage, healing, extra turns, and unrestricted search become unsafe quickly. Variables should create reachable normal and charged modes instead of "always normal" or "only with support". Avoid combining several colored numbers, conversion states, and option indices unless the user explicitly wants an art-first design.

- Wording test: if the audience may not know the template, expand the rule into concrete text rather than relying on colored-number notation.



### 使命技 / 命运线



- Definition: 使命技 frames success/failure tasks; 命运线 organizes multiple tasks, routes, or unlocks into a larger progression.

- Use when: the character is defined by a vow, doomed task, campaign, mandate, or multi-route destiny.

- Priority: medium for one clear task; low to medium for large route systems outside deity, boss, or mode centerpiece designs.

- Guardrails: separate passive/common effects from task success and failure clauses. Define success/failure priority, whether the skill disappears, and whether the task can reset. For 命运线, use cards or a visible route aid; avoid random skill pools unless the design is meant for mode play.

- Avoid when: the "mission" is a generic upside/downside pair, or the route system exists only to display many borrowed skills.



### 入魔 / 移志技 / 契定技



- Definition: a named delayed transformation or self-bound contract effect.

- Use when: the named concept precisely matches the character's moral fall, changed will, oath, or pact.

- Priority: low. Most can be written as a limited skill, awakening, or lasting state.

- Guardrails: the transformation should change play incentives, not just rename a permanent effect. If a contract carries a forced drawback, the positive reason to accept it must be visible.
