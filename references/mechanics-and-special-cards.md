# Mechanics And Special Cards Reference

Use this reference when designing a general that could borrow from existing 三国杀 cross-server mechanisms, special cards, special zones, extra decks, or equipment vocabulary.

Sources distilled into this file:

- 三国杀各服军争新机制与特殊牌汇总 document, revision records through 2025-04-21.
- User-reviewed package card/mechanism table from selected packages: 游戏模式、国战、军争、OL、SP、手杀、十周年、线下、国际服、江山如故、谋攻篇、蚀心入魔、通用机制 and related packages.
- WAHX mechanism essays on new concepts, used for priority and robustness evaluation rather than wholesale importing.

This file is self-contained. Do not assume any local codebase exists; package labels are preserved only so a user can include or exclude sources.

Do not import mechanisms wholesale by default. Choose one mechanism family that matches the character's play fantasy, simplify its wording, and add costs or constraints that fit the new general.

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

## Resolution Control Concepts

Use these concepts when a design cancels, shortens, or forcibly closes a card/phase/turn flow. The safe question is "what has already entered the event stack, and what cleanup remains?"

### 作废

- Definition: terminate a card's use process at declaration, before normal use-flow triggers and counts fully apply.
- Use when: the fantasy is disruption, bluff exposure, wasted effort, or "try again" without the full frustration of ordinary nullification.
- Priority: medium. The timing is narrow but relatively robust if kept at declaration.
- Guardrails: phrase the timing as "声明使用牌时" or an equally early point. State whether the card is discarded, whether usage count is consumed, and whether the player may use another card afterward. Do not move this later into target confirmation or damage resolution.
- Avoid when: a simpler invalidation, target cancellation, or response tax gives the same play texture.

### 终止结算

- Definition: stop an already-started resolution flow.
- Use when: the current flow has a natural private window and the remaining resolution can be safely cleaned up.
- Priority: low by default, medium only for carefully scoped one-layer flows.
- Guardrails: terminate only one clearly named layer unless the mode defines deeper cleanup. Add a closing action such as discarding the processing card or ending the current flow so cards cannot remain stuck in an intermediate zone. Prefer "于当前结算结束后" when the intent is not to interrupt nested events.
- Avoid when: the skill can interrupt dying, damage, judgment replacement, or multi-skill insertion without a cleanup rule.

### 强制结束阶段/回合

- Definition: after the current resolution, force a phase or turn to end.
- Use when: the design wants a strong debuff, retreat, command halt, or preserved advantage.
- Priority: medium for ending play phase or a defined current phase; low for ending a whole turn unless heavily costed.
- Guardrails: make clear that ongoing resolution finishes first. Ending the play phase is close to a delayed-trick-level control effect; ending the turn also skips discard, which can be a benefit. Repeated or easy access can create oppressive locks.
- Avoid when: direct draw reduction, use restriction, or "skip a named phase" can express the same effect with fewer timing issues.

### 并行操作 / 瞬发式操作

- Definition: a game operation occurs during another normal resolution instead of waiting for the current serial flow to finish. This is broader than ordinary trigger insertion and should usually be mode infrastructure, not a personal skill.
- Use when: an external variable such as time, physical position, live scoring, or a mode UI event must be checked independently from the normal card/skill stack.
- Priority: very low for normal generals; medium only for modes with external timers or non-skill interactive widgets.
- Guardrails: never use it as a casual "any time" skill button. Define whether the parallel action resolves immediately, queues until the current resolution ends, or only records a pending result. Avoid HP loss, damage, dying, card use, skill grants, or target changes inside a parallel window. The safer pattern is "may be performed any time; resolve at phase/turn/end-of-current-resolution timing".
- Avoid when: an ordinary trigger, compulsory listener, or current-resolution-aftereffect can express the same idea.

## Role Reassignment And Control Concepts

Use these concepts only when the design deliberately changes responsibility, authorship, or agency. They are expressive but hostile to ordinary trigger expectations, because "who used it", "who caused it", and "who decided it" are often checked by later skills.

### 修改伤害来源 / 修改使用者

- Definition: a current damage event or card-use event is reassigned so another character is treated as the source or user.
- Use when: the fantasy is scapegoating, commandeering, stealing credit, blame transfer, or forcing someone to bear the consequences of their own scheme.
- Priority: low to medium. It is flavorful for very specific anchors, but its play role is unclear because causing damage can be reward or liability.
- Guardrails: restrict it to one named event, card type, or timing; state whether later "造成伤害", "使用牌", "成为来源/使用者", and usage-count checks follow the reassigned role. Prefer target transfer or damage transfer if preserving the original source would solve the scene. Be especially careful with self-targeting【杀】, lord/loyalist blame, and feedback skills that punish the apparent source.
- Avoid when: the effect is only meant as protection, retaliation, or redirection; simpler cancellation, transfer, or damage prevention is usually cleaner.

### 操控 / 轻量操控

- Definition: one player directly directs another character's choices, cards, or even turn. Light control instead forces one bounded action while leaving the controlled player meaningful choices.
- Use when: possession, manipulation, divine intervention, or puppet-master flavor is the core identity.
- Priority: very low for full-turn or full-hand control; medium-low for one small forced action.
- Guardrails: avoid routine removal of another player's turn or agency. Define who may see hidden information, who pays costs, whether optional skills may be invoked, and how automated/absent players are handled. Prefer "令其使用/打出一张牌", "其选择一项", or "你选择其可执行的一项" over taking a whole turn.
- Avoid when: the user only wants a strong control skill. The negative play experience and variance are usually larger than the design payoff.

## Card Identity And Conversion Concepts

Use these concepts to judge rules that change what a card "is". They save text only when the changed information is frequently checked by the rest of the design.

### 强制更改牌面信息 / 强制转化 / 双视为

- Definition: a compulsory rule changes a card's name, suit, category, or other card information, unlike optional "将...当...使用/打出".
- Use when: the character has a stable relationship with one card identity or one visible card element, and that changed identity repeatedly matters.
- Priority: medium. It has high expressiveness and broad fit, but low robustness because overlapping "视为" effects, category checks, and delayed/equipment cards create many edge cases.
- Guardrails: keep it self-contained, usually only your own hand cards; avoid double "视为" layers; state whether the new information overwrites or merely grants selection permission if the environment needs that distinction; do not use it mainly to produce unrestricted【桃】 or 【酒】.
- Design test: if the changed element is checked only once, write the direct effect instead of introducing a forced identity rule.

### 视为存在牌 / 进行延时锦囊判定

- Definition: a character is treated as having a specific equipment or delayed trick, or directly performs a delayed-trick judgment without that card moving normally.
- Use when: "self-carrying equipment" or a permanent burden is the actual fantasy, especially for the card's rightful owner or an unmistakable artifact theme.
- Priority: low to medium for equipment-like existence; low for delayed-trick existence. The flavor is narrow and existing equipment/delayed tricks have specific allusions.
- Guardrails: define attack range conflicts, replacement/cover rules, whether it counts as a card in the area, and whether leaving/losing that virtual existence triggers effects such as recovery or draw. For delayed tricks, prefer a direct skip-phase, judgment-risk, or current-window penalty when that gives the same play texture with less memory.
- Avoid when: the only goal is to borrow the prestige of a famous equipment or to put a cross-turn debuff on the table.

### 结果反转

- Definition: invert a clearly binary result, such as "hit/fail" or "win/not win".
- Use when: the original procedure is already a two-outcome check and inversion itself is the character's theme.
- Priority: low. It is easy to understand, but often forces non-binary procedures into an artificial pair.
- Guardrails: do not apply it to effects with three or more branches; be especially careful with rare high-risk outcomes such as【闪电】.

### 其他元素的转化

- Definition: describe a non-card resource as being converted into a card or effect, such as life, marks, or equipment-area state becoming a virtual card.
- Use when: it is presentation shorthand for a very simple cost-to-effect relation.
- Priority: low as a rules mechanism, medium as flavor wording after translation.
- Guardrails: in final rules text, usually write the concrete cost and "视为使用/打出" result. Define whether the virtual card has a physical card, whether it triggers use/play timing, and whether it can be obtained or moved by other effects.

## Card Marks And Zone Concepts

Use these concepts when a design stores real cards outside normal hand/equipment/judgment flow. The core question is not "can a card be put there", but who owns the memory burden and how the card returns to play.

### 标记牌 / 武将牌上牌

- Definition: real cards are placed on or near a general as visible records, resources, or thresholds.
- Use when: the card's physical presence reduces memory, creates a visible stockpile, or lets value/suit/type matter later.
- Priority: normal. It is highly reusable and intuitive, but only if the design controls memory and card-flow pressure.
- Guardrails: define owner/source, visibility, cap or threshold, how cards leave, and what happens if the skill is lost. Give the player a real reason to remove or spend the cards; pure hoarding thins the deck and can quietly control draw quality.
- Avoid when: the general already uses several marks, the stored cards never matter as cards, or the only function is a delayed awakening counter.

### 标记 / 跨回合记忆

- Definition: named non-card markers or remembered states created by a skill.
- Use when: the design needs a visible personal token, an identity-defining resource, or a cross-turn state that cannot be expressed by current-turn history.
- Priority: low for plain numeric counters, normal for distinctive tokens with strong character meaning.
- Guardrails: avoid more than one marker axis on an ordinary general. Define acquisition, loss, cap, cleanup, and skill-loss handling. Cross-turn memory without a marker should usually last at most one round; if flip/skip effects can stretch it, add a visible reminder.
- Avoid when: a temporary variable, current-turn condition, hand limit change, or stored card can carry the same information.

### 给别人放牌 / 仁区 / 公共区私有资源

- Definition: a skill places cards in another character's area, or creates a public zone consumed by multiple skills.
- Use when: the design needs short-lived blame, infection, shelter, or shared political/moral resources.
- Priority: low by default. It is easy to understand but fragile because private areas and shared zones create ownership disputes, stalled resources, and package-level balance dependencies.
- Guardrails: for cards put on others, prefer same-turn or current-phase expiry; write ownership if another skill can interact with the same area. For public zones, set a cap, automatic cleanup, death/skill-loss handling, and a way for cards to keep flowing even if the original enabler dies.
- Avoid when: the public zone exists for only one general without enough support, or when several generals can stockpile but only one can spend.

### 专属牌 / 销毁 / 牌盒 / 游戏外牌

- Definition: cards outside the normal deck are introduced, or special cards leave the game after use.
- Use when: a character's artifact, siege engine, law, poison, or unique order deserves a full card object rather than one line of skill text.
- Priority: low for ordinary generals, medium for package centerpieces or modes with explicit extra-card support.
- Guardrails: define where the card comes from, whether it ever enters the main deck/discard pile, whether normal transformation can name it, what "destroy" means in tabletop terms, and whether there can be multiple copies. "销毁" is usually just "移出游戏" unless the environment gives it extra rules.
- Avoid when: a normal skill line or virtual card can express the same play. Special cards often reduce first-glance skill length while increasing total reading and setup cost.

### 判定区/装备区标记牌, 暗置, 蓄谋

- Definition: cards are stored in judgment/equipment-related areas as delayed resources rather than normal delayed tricks or equipment.
- Use when: the area itself is the play object, such as delayed release, hidden transfer, or a plotted future use.
- Priority: low for arbitrary judgment/equipment-area markers; medium for well-defined systems such as 暗置 or 蓄谋 that handle visibility and automatic return.
- Guardrails: do not casually put generic marker cards in judgment or equipment areas; those areas already have movement rules. If using 暗置/蓄谋-like rules, define visibility, when the card returns or is used, whether it can be obtained/moved/discarded, and how it differs visually from any other stored-card mechanic.
- For transformed delayed tricks, follow the conservative convention: delayed trick cards do not transform into other delayed trick identities, while non-delayed cards may be mapped by a clear rule. This prevents multiple identical physical cards from representing different delayed tricks with no memory aid.

### 手牌标签 / 明置暗置 / 连接

- Definition: specific hand cards receive a label, orientation, visibility state, or sub-zone membership.
- Use when: the design needs a card to remain identifiable while still being a hand card.
- Priority: medium for one self-contained label; low for shared or cross-character hand tags.
- Guardrails: protect the ordinary randomness of hand cards. Make labels public or otherwise auditable; define whether labeled cards count as hand cards, can be randomly chosen, and lose labels when moved or when the skill is lost. Do not overload the same physical cue for both 明置/暗置 and another system such as 连接.
- Avoid when: the rule must secretly know "usable hand cards" or other platform-only states that a table cannot verify.

### 标记型数值 / 能力值 / 声明数值

- Definition: a named value, gauge, or declared variable is introduced and later referenced.
- Use when: a temporary X or a compact resource genuinely improves decisions.
- Priority: low for new blue-bar-like resources, medium for temporary declared values.
- Guardrails: prefer ordinary marks unless the value has package-wide support. Declare variables before use and define duration; undefined X should not be silently assumed by players. Cross-turn declared values need a marker or visible aid.
- Avoid when: the value is only a renamed mark, or when several skills share a variable whose ownership and reset timing are unclear.

### 中央区 / 有序弃牌堆

- Definition: a design isolates a current subset of the discard pile, or treats the discard pile as an ordered stack.
- Use when: recent card history is the core resource, or the design repeatedly cares about "cards that just happened" more than the whole discard pile.
- Priority: medium for central-zone-like subsets; medium-low for ordered discard piles because they demand table discipline.
- Guardrails: define whether the zone is a subset of the discard pile or a separate zone; specify when cards enter/leave, who orders simultaneous entries, and how it interacts with "put into discard pile", "discard pile bottom", and shuffle events.
- Design test: if the skill only cares about this turn's discarded cards once, use ordinary "本回合进入弃牌堆的牌" wording. Create a named zone only when multiple skills or repeated checks benefit from the shared vocabulary.

## Non-Game Card And Materialization Concepts

Use these when components that are normally not game cards, such as general cards, HP cards, identity cards, or reserve cards, are treated as cards or card-like objects. This can reduce unused components but carries heavy memory and compatibility cost.

### 对非游戏牌的应用

- Definition: a non-game component is given card-like attributes, can move through game zones, or can be used to represent a card effect.
- Use when: the fantasy is soul-taking, stealing a body/name, using identity as evidence, consuming vitality, or turning unused components into meaningful objects.
- Priority: low to medium. It is innovative and tactile, but most characters cannot justify moving general or identity cards as ordinary resources.
- Guardrails: define the component's card name, suit, point, category, face state, owner, whether it counts as a real card, and how it returns or is removed. Avoid mixing several non-game-card systems in one design. Identity cards and general cards require especially strong flavor because they imply changing who a player is; HP cards are easier to justify but still need visible state handling.

### 物化 / 化形牌

- Definition: a character declares card information, creates or gains a 化形牌, and treats their general card as a card-like object in a zone while a substitute keeps the character's identity stable.
- Use when: a person becomes an artifact, weapon, attack, gift, body double, or final remaining power.
- Priority: medium-low. It is a strong platform concept, but many uses are cleaner as "视为使用", a special card, or a stored-card skill.
- Guardrails: state whether the materialized card keeps skills, whether skills can still be read, what operations on the general card are redirected to the 化形牌, and when it resets (复位). Multi-general modes need a rule for main/deputy cards and simultaneous materializations. Materialized equipment is usually safer than materialized delayed tricks; materialized【桃】/【酒】or broad survival cards need strict limits.

## Public Mark And Public Task Concepts

Use these when a mode or package adds a shared resource or recurring task. They are healthier as mode infrastructure than as a single ordinary general's private complication.

### 公共标记

- Definition: visible shared counters or indicators, often used as mode currency, public buffs, or progress toward a mode objective.
- Use when: the whole table can understand and access the resource, such as campaign morale, anger, supplies, military merit, or public pressure.
- Priority: high for modes and activity packages; low for a lone general.
- Guardrails: define who can gain/spend the markers, whether they belong to players, roles, factions, or the table, and whether there is a cap or cleanup timing. If only a few roles can reliably gain them, treat the result as a side reward rather than a core victory/resource engine. A public marker should support the mode's main play loop, not sit above normal skills as a decorative scoreboard.

### 整肃 / 协力 / 公共任务

- Definition: a player or pair tries to satisfy one of several named task patterns, then receives a reward or records success/failure.
- Use when: the fantasy is discipline, training, coordination, oath, inspection, or a team executing a plan over a short window.
- Priority: medium for concise 整肃-like self/target tasks; low for broad 协力-like cross-turn pair tracking unless the partner's actions clearly matter.
- Guardrails: task cost must not eclipse the reward, and the task should not require players to abandon all normal play unless that tension is the point. Define duration, who is checked, what counts, whether targets or only totals matter, and what happens on failure. Keep the menu small; if the task exists only for one skill, write the exact task in the skill instead of importing a full public-task label.

## Movement And Transfer Concepts

Use these concepts when the design changes where an object goes without ordinary "use", "discard", or "obtain" flow. They are most useful when the destination itself matters.

### 移动 / 置入 / 置于手上

- Definition: move an object between areas, put it into a destination area, or put it specifically into a hand area without using ordinary obtain wording.
- Use when: the character manipulates board layout, same-zone order, delayed objects, extra zones, backup generals, faction markers, or other objects whose exact position matters.
- Priority: medium-high for clear "移动"; low for "置入" and "置于手上" when "获得", "交给", "置于武将牌上", or "置入弃牌堆" is more readable.
- Guardrails: define origin, destination, owner, visibility, and whether the move counts as gaining, discarding, using, replacing, or losing. Do not casually put arbitrary cards into equipment or judgment areas; those areas have existing legality and replacement rules. For hand-area movement, prefer ordinary gain/transfer unless avoiding a loop or trigger is the point.
- Avoid when: the operation only renames a normal card movement and no later rule checks the special route.

### 合纵 / 赠予

- Definition: card-transfer variants. 合纵 makes helping another player also reward the giver; 赠予 frames a card as a gift, burden, or planted object.
- Use when: the fantasy is coalition, diplomacy, aid with self-interest, bait, curse-gift, or espionage by object transfer.
- Priority: high inside 国战 or mode designs built around shifting alliances; medium-low in identity games; low for forced negative equipment unless the brief specifically wants that discomfort.
- Guardrails: state whether the giver gains a reward, whether the receiver may refuse, whether the card is public, and whether equipment can be replaced. Negative gifts should preserve consent or carry a visible cost; forced equipment replacement is high-friction. If the design is not 国战, avoid importing 合纵 assumptions unless the table politics still matter.
- Avoid when: a plain "交给一张牌" plus a small rider expresses the same support.

## Guessing, Randomness, And Out-Of-Game Concepts

Use these concepts when a design asks players to make predictions, accept random results, or reference information outside ordinary public game state. The core quality test is whether the result feels fair to everyone at the table.

### 猜测 / 心理博弈

- Definition: a player predicts a hidden choice, card property, or private intention, then the relevant result is revealed or otherwise made verifiable.
- Use when: the character fantasy is bluffing, testing, reading people, prophecy, or intimidation, and the table can enjoy a short mind game.
- Priority: normal to high for social play. It is intuitive and expressive, but swingy and often worse in fast online environments.
- Guardrails: options, choice, and result must be public or verifiable after resolution. Keep stakes moderate on both success and failure; avoid "guess right wins, guess wrong dies" patterns. Do not let the optimal line become a fixed routine that removes the actual mind game.
- Avoid when: the skill needs secret cooperation, unverifiable self-reporting, or repeatedly pauses the table for low-value decisions.

### 不可见元素 / 系统判定

- Definition: a skill uses information players cannot normally verify, or relies on a platform/system to inspect hidden state without disclosure.
- Use when: the user explicitly wants an online-only design and accepts that it may not work in tabletop play.
- Priority: low for general custom design. It can open new space, but it damages trust and is hard to port across environments.
- Guardrails: prefer applying only to the user's own hidden elements; reveal enough after resolution for players to audit fairness; label the design as online-only if a real table cannot execute it. Never require a player to make unverifiable claims for large rewards.
- Avoid when: the hidden check exposes another player's strategic weakness, creates suspicion of collusion, or could be replaced by a public reveal, guess, judgment, or chosen option.

### 随机执行 / 卜卦

- Definition: one option is selected randomly from a known menu; 卜卦 is a themed top-card/random-sign procedure.
- Use when: fate, omen, chaos, or uncontrollable orders are central to the character, and the random menu is small enough to understand.
- Priority: medium for transparent equal-probability random menus; low when probabilities are hidden, uneven, or platform-controlled.
- Guardrails: state the probability method or use existing public procedures such as judgment, reveal, or dice. Keep branches comparable in value or give players a mitigation choice. For 卜卦-like designs, cap branch count and avoid cross-turn memory unless a physical aid exists.
- Avoid when: "random" merely hides poor balancing, or when a simple judgment would give the same texture with less baggage.

### 军令 / 道具抽签 / 刮彩票

- Definition: a packaged random or semi-random menu represented by cards, slips, tickets, or other physical aids.
- Use when: a mode or package wants a shared command deck or a reusable tactical order vocabulary.
- Priority: medium for a small public menu like 军令; low for one-character props, large ticket sets, or tools that mostly add spectacle.
- Guardrails: keep the menu small, broadly useful, and similar in value; define whether the recipient may refuse, choose between drawn options, or must execute. If physical components are required, make them replaceable by ordinary cards, dice, or a table.
- Avoid when: the component is one-to-one bound to a single general, creates setup burden, or has huge variance in normal identity games.

### 游戏外元素 / 小游戏 / 无关文本

- Definition: a skill references player traits, real-world objects, physical dexterity, other games, interface features, or text that does not change rules.
- Use when: the design is explicitly casual, festive, mode-specific, or an art-first piece.
- Priority: low for normal generals. It may be charming, but often breaks immersion, privacy, portability, or table pace.
- Guardrails: game-outside references should affect only setup, tie-breakers, or very small bonuses; consider extreme cases and sensitive information. Mini-games must be quick, optional, and strongly tied to the character fantasy. Non-rules text belongs in title, flavor, notes, or art direction, not in the rules box.
- Avoid when: it changes core stats from real-world data, asks for private personal information, forces all players to watch a side activity, or depends on online-only cosmetics such as exclusive emotes.

## Contest, Voting, And Bargaining Concepts

Use these concepts when the design turns cards, choices, or table politics into a contest. The best versions preserve player agency instead of becoming disguised random outcomes.

### 拼点

- Definition: two players reveal one hand card each and compare points, usually resolving win/not-win branches.
- Use when: the fantasy is duel, debate, test of courage, diplomatic pressure, or using excess cards as leverage.
- Priority: high as a clean contest operation.
- Guardrails: remember that pindian is close to zero direct card advantage but can disrupt hands and create alliance play. Do not always attach huge rewards; let the point contest and card choice matter. If using tied/lost branches, define them explicitly because many players expect the traditional win/not-win split.
- Avoid when: the design only wants random high/low resolution; judgment or reveal may be simpler.

### 多人拼点 / 逐鹿 / 对抗拼点

- Definition: more than two players compare points, either individually, by unique highest, or by teams/factions.
- Use when: the scene is truly a group debate, contest for leadership, or factional confrontation.
- Priority: medium-low. It is flashy but dilutes each player's influence.
- Guardrails: define participation, side selection, tie handling, winner count, and who gets exposed/used cards. Avoid rewarding "all non-winners' pindian cards" without a cap. Keep teams meaningful; otherwise it degenerates into identity math rather than card contest.

### 谋弈 / 锻造 / 议事

- Definition: 谋弈 is a two-option prediction game, 锻造 is a collective/randomized crafting contest, and 议事 is reveal-and-vote by card color.
- Use when: prediction, public deliberation, or collective construction is more important than point comparison.
- Priority: high for 议事 when court/public-will flavor fits; medium for 谋弈; low for 锻造 outside artifact-making centerpieces.
- Guardrails: 谋弈 options should be symmetric enough to be a mind game but not so symmetric that they become pure random guessing. 议事 exposes information, which is part of its cost. 锻造 needs a clear reason for helpers/hinderers and should not jump directly into identity certainty.

## Bond And Formation Concepts

Use these concepts when relationship or seat position is the actual play object. Do not add a bond merely because two people knew each other in history; the bond must improve decisions or presentation without making the base design incomplete.

### 羁绊 / 点名配合 / 珠联璧合 / 宗族羁绊 / 同心

- Definition: a skill checks named characters, paired generals, clan membership, oath partners, or other relationship groups for extra effects.
- Use when: the mode makes the partner reasonably controllable, such as 国战双将, lord-related designs, clan packages, or a skill that asks others to participate with you.
- Priority: low in random identity draft; medium to high in 双将、国战、宗族包, or activity modes where the relationship framework is visible and expected.
- Guardrails: make the general functional without the bond. Keep bond bonuses small, visible, and thematically precise; avoid one-in-a-hundred hidden easter eggs that warp the whole text. Define version handling, multi-name variants, skill theft, and whether "same clan" is historical membership or current skill ownership.
- Avoid when: the skill names a single ally who is unlikely to appear, or when the bond becomes stronger than the character's own design.

### 阵法关系 / 阵法召唤

- Definition: seat adjacency, relative position, or unrevealed ally presence creates a formation relationship or reveals/calls allies into it.
- Use when: 国战, 3v3/4v4, or another mode already makes seat geometry strategically meaningful.
- Priority: low outside mode play; medium only when seat manipulation and formation rewards are part of the environment.
- Guardrails: define the check timing, whether hidden identities count, what happens after seat movement, and whether targets must be same faction or merely adjacent. Give a fallback so the general is not blank because of random seating. 阵法召唤 needs a real incentive for allies to reveal; otherwise it becomes decorative text.
- Avoid when: the position condition is hard to arrange and the design has no tools to move, invite, or profit without it.

## Victory, Faction, And Objective Concepts

Use these only when identity or faction is the character's core. They can override the emotional contract of the table, so ordinary designs should prefer rewards, tasks, or awakening over changing who wins.

### 改变胜利条件 / 额外胜利

- Definition: a skill changes identity, adds an alternate win, or declares a winner through a route other than the normal mode objective.
- Use when: the whole design is about betrayal, usurpation, survival-to-the-end, prophetic victory, or multi-game scoring.
- Priority: very low in normal identity games; medium in modes that already track points, rounds, ranks, or explicit alternate objectives.
- Guardrails: do not swap another player's win condition without consent or strong mode framing. Prefer "after the game, also count as winning" or mode score progress over immediately ending the game and nullifying prior play. If a condition is easy, the character becomes a public target; if impossible, it is only noise. Make clear whether normal victory still applies, whether teammates share the alternate result, and whether the game ends immediately.
- Avoid when: the goal is only to make a weak character interesting.

### 君主 / 定鼎 / 溃散

- Definition: 国战-like lord mechanics introduce a faction center, often through early declaration, replacement by a 君主 card, and faction collapse after that center dies.
- Use when: the mode needs a protect-the-center structure, such as 国战 variants, campaign battles, or two-sided activity modes.
- Priority: low outside mode design.
- Guardrails: keep declaration early enough to fit the lord fantasy. Define how faction size, wild ambition, defeat, and remaining allies are recalculated. Do not force an entire team to inherit one player's punishment unless the mode is built around that risk.

### 改变势力 / 双势力武将 / 势力技

- Definition: a character's faction changes, can be chosen, can switch between several factions, or unlocks skills only while in a matching faction.
- Use when: the historical anchor genuinely crosses factions, returns home, defects, or lives between powers.
- Priority: medium in identity designs where faction is mostly flavor or a visible skill condition; low in 国战 when faction equals victory condition.
- Guardrails: define whether the character is one faction at a time, a stacked dual faction, or a switchable faction. State when the choice is made and how faction count is calculated. If the faction choice effectively creates two versions of one general, balance both versions; a switchable design should give the player reasons to move between factions rather than lock one best answer.

### 暴露野心 / 僭位

- Definition: a hidden or ordinary character becomes a 野心家, or an ordinary general transforms into a stronger ambition form after meeting a condition.
- Use when: ambition, rebellion, usurpation, or hidden final-side identity is the core story.
- Priority: low and mostly 国战/mode-specific.
- Guardrails: avoid forcing the player to stay underpowered or single-general until the final stage with no agency. A 僭位-like transformation is usually cleaner than a late reveal if the condition, cost, and new victory position are visible. Account for "jumping ship" in losing or winning positions; the transformation must create risk, not just opportunistic betrayal.

## Allocation And Choice-Control Concepts

Use these concepts when a skill gives flexible distribution or changes whether players may choose.

### 共计 / 分配

- Definition: a total amount is divided among targets or effects, then later clauses may refer to each share.
- Use when: the character expresses large-scale command, charity, devastation, or resource allocation.
- Priority: high for traditional card/damage distribution, medium-low for broad "new-style" distribution of arbitrary objects.
- Guardrails: specify total, valid recipients, minimum/maximum per recipient, and whether assigning 0 is allowed. Be careful distributing HP, max HP, damage, or recovery because simultaneous gain/loss can create insertion and dying-timing problems. For a single unit, direct "令一名角色..." is usually clearer than "分配1".
- Avoid when: the wording only adds grandeur without real flexibility.

### 拒绝 / 放弃

- Definition: a player is allowed to refuse a procedure or decline an otherwise expected action.
- Use when: the design needs strong self-restraint, defiance, or a way to soften a forced interaction.
- Priority: medium.
- Guardrails: treat refusal as a higher-level option; define the result of refusal and whether refusal can be forced by inability. "放弃" reads more voluntary and softer than "拒绝"; choose the word that matches the fantasy.
- Avoid when: "若你未..." or an ordinary optional clause is clearer.

### 强制发动

- Definition: a normally optional skill or choice is made compulsory for a limited time or branch.
- Use when: the design tempts the user into overcommitting, losing control, or weaponizing an awkward skill.
- Priority: medium-low. It is interesting but can feel hostile.
- Guardrails: prefer forcing your own skill, or give meaningful compensation if forcing another player. Balance the forced and non-forced modes; if the skill is always profitable, making it compulsory is meaningless.
- Avoid when: it removes important targeting choices or makes another player execute a long skill against their will.

### 重置技 / 枭雄技

- Definition: a multi-option skill tracks which choices have been used, may reset after all options are used, or permanently leaves one option as the final state.
- Use when: the character has prepared tactics, staged choices, or a "use every plan before returning" rhythm.
- Priority: low to medium. It is flexible but memory-heavy and easy to overbuild.
- Guardrails: keep option count small and visible. Options should not have an obvious fixed order, or the skill becomes a conversion/sequence skill. Make reset conditions reachable but not automatic, and define what happens if an option cannot currently be chosen.
- Avoid when: two options would work better as a conversion skill, or five-plus options make the character a menu.

## Damage, Tags, And Skill Encapsulation Concepts

Use these concepts when splitting existing concepts into subtypes or turning a recurring operation into a compact tag.

### 属性伤害

- Definition: damage has an attribute variable, usually fire or thunder, while ordinary damage remains available.
- Use when: the attribute has meaningful support in cards, skills, or defenses, not merely decorative flavor.
- Priority: high as a model concept; normal in new designs because too much attribute support can warp the environment.
- Guardrails: preserve ordinary damage as a useful baseline. Give each attribute a distinct job and enough but not excessive support. Avoid adding a new attribute unless it has repeated interactions and a clean rule identity.
- Design test: if the only difference is one skill line, use direct wording such as "此伤害+1" or "此伤害不能被防止" instead of defining a new damage type.

### 特殊属性伤害 / 视为造成过伤害

- Definition: a damage subtype carries an extra optional or compulsory rider, or a partial "as if damage happened" event is recorded.
- Use when: the design needs a rare signature damage identity or a controlled fake-damage puzzle that mostly serves the user's own skills.
- Priority: low. It is expressive but narrow and easy to over-combo.
- Guardrails: state whether transmitted/chain damage carries the rider. Do not let fake damage freely trigger broad sell-blood or damage-record skills unless that is the whole design and has a cost.
- Avoid when: the rider helps the damaged player more than it hurts, or when the design depends on other characters' skills to matter.

### 额外牌面信息 / 应变标签

- Definition: a card carries an extra tag or condition, such as a special Slash tag, Yingbian-like condition, or strengthened state.
- Use when: the tag is medium-frequency, easy to check, and gives a card family a recognizable tactical identity.
- Priority: medium.
- Guardrails: define whether transformed/virtual cards may gain the tagged version, whether the tag changes card name/category, and whether the effect is compulsory. Conditions should be achievable but not automatic; extreme conditions are better for comeback cards than universal card vocabulary.
- Avoid when: the tag becomes a pile of unrelated bonuses or requires players to remember invisible card text.

### 技能封装 / 卜算 / 附魔

- Definition: a known skill operation is packaged as a keyword or attached to a card as a temporary callable ability.
- Use when: every player already knows the operation and the keyword greatly shortens repeated text.
- Priority: low to medium. Good encapsulation saves words; bad encapsulation makes rules feel like private jargon.
- Guardrails: define which version of the source skill is being invoked, what parameters mean, and which hidden clauses are included or excluded. Encapsulation should follow ordinary reading order; avoid phrases that require players to mentally expand several skills at once.
- Avoid when: the original skill has context-sensitive side effects, optional follow-ups, or a famous version mismatch.

## HP, Armor, And Dying Concepts

Use these when health presentation itself is the play object. Do not use extra HP, armor, or shattered-gem language merely as balance knobs.

### 残血开局 / 护甲 / 护盾 / 虚血

- Definition: a character starts below max HP, gains a damage buffer, gains a stronger shield-like buffer, or has temporary HP above normal max that cannot be restored once lost.
- Use when: the character is protected by outside power, visibly exhausted, outwardly strong but fragile, or defined by spending max HP/health state.
- Priority: medium for flavorful 残血开局 and simple 护甲; low for many armor variants on ordinary generals.
- Guardrails: explain why the abnormal HP exists in the character, then make skills care about it. Distinguish whether the buffer prevents damage only, HP loss too, whether it affects hand size, and whether it has a cap. Avoid using armor as generic "the design is weak/strong" patching, and be careful with survival-card access because extra buffer plus【桃】【酒】can make a character too hard to finish.

### 体力牌操作 / 勾玉颜色

- Definition: HP cards or gems are shattered, repaired, split, merged, flipped, recolored, or otherwise treated as physical components.
- Use when: the visual operation is central to the fantasy, such as heartbreak, damaged vitality, divided body, unusual awakening, or health-ratio state.
- Priority: low. It is mostly presentation and carries physical/UI edge cases.
- Guardrails: define the exact visible representation, initial state, whether several HP cards can overlap, and what happens if the required card shape is unavailable. If color only represents health ratio, a direct HP/max-HP condition is often clearer. Use these as artful aids for one visible axis, not as a second marker system layered on top of several marks.

### 体力下限 / 额外濒死结算

- Definition: change the HP threshold for entering dying, or force an extra dying-like procedure outside the normal threshold.
- Use when: the character is harder or easier to keep alive in a way max HP cannot express, such as stubborn survival, slow doom, false death, or a vow tied to near-death.
- Priority: low; death-threshold rules are high-stakes and timing-heavy.
- Guardrails: state the threshold, how it interacts with max HP, immediate death, recovery, and leaving dying. Extra dying checks should not let full-health characters convert【桃】 into a pure benefit, nor should they create hidden lethal inserts. Prefer max-HP loss, HP loss, or "when entering dying" riders unless the threshold itself is the point.

## Description Shorthand Concepts

Use these only when the shortcut is less confusing than the fully expanded text.

### 对方 / 二元操作指代

- Definition: in a binary interaction, "对方" means the other participant relative to the skill owner, such as the other side of a Slash response, Duel exchange, damage-source/recipient pair, or pindian.
- Use when: a skill repeatedly refers to the other participant in a clean one-on-one operation and the expanded wording would be much longer.
- Priority: medium. The word is highly reusable and readable, but it is more colloquial than most 三国杀 rules text.
- Guardrails: use only for clear binary operations. In one-to-many, treat each pair separately only if the timing already resolves by target; avoid using it for multi-party, substitute-response, or nested operations where there are several plausible "other sides". If the skill can trigger from multiple event types, name examples or write the full roles instead.
- Avoid when: the event has more than two meaningful participants, or when a named role such as "伤害来源", "使用者", "目标角色", or "响应的角色" is just as short.

## Physical State And Turn Flow Concepts

Use these concepts when the design changes card orientation, player order, or the temporal structure of turns.

### 实体性操作

- Definition: a physical component is turned, tapped, flipped, stacked, restored, or otherwise oriented to indicate state.
- Use when: the state must remain visible and the operation is unique on the component.
- Priority: medium for established operations such as 横置/重置 and 翻面; low for new orientation systems.
- Guardrails: each physical cue must be visually unique and must not block reading core information. Define initial state, available inverse operation, and what happens if the target is already in that state. Similar names should not hide different rules; distinguish reset, restore, recover, and unchain-like effects.
- Avoid when: the table already uses that orientation for another memory task, or the state could be represented by an existing mark/card.

### 废除 / 恢复

- Definition: seal a zone, slot, phase, procedure, or other element so it cannot function, then possibly restore it later. For areas, also define what happens to cards already there.
- Use when: the fantasy is mutilation, permanent sacrifice, sealed capacity, ruined equipment ability, or a harsh cost that creates a visible weakness.
- Priority: low for ordinary generals; medium only when self-sacrifice is the core.
- Guardrails: prefer self-abolition over abolishing opponents' equipment slots. Define whether paired slots are abolished together or separately, whether cards are discarded, whether later cards can enter, and how/when recovery happens. Repeated irreversible abolition can make the rest of the game miserable; if recovery is too quick, the rule becomes a verbose stance marker. Non-zone abolition such as abolishing phases, dying flow, or a point of max HP needs explicit memory and should be rare.
- Avoid when: a temporary disable, discard, skip phase, or max-HP loss expresses the same cost.

### 回合变动

- Definition: a rule skips, adds, swaps, or modifies turns/phases/seats.
- Use when: the character fantasy is time control, command seizure, imprisonment, or extreme tempo conversion.
- Priority: low for ordinary generals because it is high impact and environment-sensitive.
- Guardrails: extra turns and forced flip/skip scale upward with every future strong skill. Extra phases inside another turn lack some turn-end cleanup; prefer direct bottom-level actions such as drawing, using a card, or discarding unless phase triggers are the point. Seat swaps are platform/table dependent.
- Avoid when: a smaller action can express the same tempo change without denying another player's turn.

### 预演 / 回溯

- Definition: a design records a game state, runs a temporary future or alternate sequence, then restores part of the state.
- Use when: the brief explicitly asks for experimental, boss, dream, or art-first time-loop play.
- Priority: very low.
- Guardrails: define the snapshot scope: HP, cards, marks, deaths, delayed effects, skill changes, and public zones. If the snapshot does not restore most of those, do not call it full rehearsal or rollback. Keep it short and rare.
- Avoid when: it would require reconstructing a past turn, nesting with other rollback/termination effects, or asking the table to maintain many records.

### 登场/离场操作 / 替换武将 / 休整

- Definition: a character changes general cards, temporarily exits and returns, joins again after defeat, or otherwise breaks the "one chosen general stays until death" baseline.
- Use when: the mode or character is about transformation, substitute generals, boss phases, command-center identity, or a group acting through several bodies.
- Priority: low for ordinary identity generals; medium for activity modes, 1V1, 国战, boss play, or tightly scripted transformations.
- Guardrails: define what happens to HP, max HP, cards, marks, delayed effects, gained skills, temporary skills, chained/flipped state, and pending resolutions. Avoid stacking with long delayed effects or stolen skills unless cleanup is explicit. If the design only wants awakening, prefer an ordinary 觉醒技 or skill change over replacing the general card.
- Avoid when: the scene reads as unexplained death, rebirth, or possession in a normal identity game.

### 流放 / 调离 / 隐匿 / 易位

- Definition: related character-state operations: 流放 removes backup generals in a mode with reserves; 调离 temporarily removes a character from ordinary card/targeting participation; 隐匿 hides or disables a general until reveal; 易位 exchanges general cards or role bodies.
- Use when: the relevant mode already has backup generals, hidden generals, seat/faction structure, or team coordination that makes the operation meaningful.
- Priority: mode-specific and usually low outside that mode.
- Guardrails: 流放 should not eliminate the last mandatory backup choice or remove all drafting counterplay. 调离 needs duration, what can still affect the role, and whether it is offensive denial or defensive shelter. 隐匿 must define what happens to cross-turn skills and entering/revealing triggers. 易位 should be consensual or mode-bounded; in identity games, forced general exchange is socially and strategically hostile.
- Avoid when: the general would be blank without the mode scaffolding, or when the operation only creates surprise instead of decisions.

## Skill Existence And Off-Board Concepts

Use these when a skill exists on a card, in a mode, in a reserve area, or outside the current character. They are useful for mode design and fragile for ordinary generals.

### 技能目标 / 技能卡式目标

- Definition: a skill treats one or more chosen characters as its targets, similar to a card's targets.
- Use when: one active skill is deliberately written like a skill-card and later clauses need to refer to selected roles.
- Priority: low as a general mechanism, medium only for a self-contained skill family that defines its own target rule.
- Guardrails: do not assume every skill has a universal target. Equivalent text can choose one character once or choose two characters in sequence, and broad target rules may distinguish descriptions that otherwise resolve identically. Prefer "你选择的角色", "前者/后者", or a named target list inside the skill. If the design grants or steals skills, do not rely on unknown borrowed skills having meaningful targets.

### 追思·新 / 凌越 / 连环

- Definition: weak encapsulations built on skill target logic: 追思-like rules stop later selection of the same role, 凌越 checks a size/quantity comparison with a selected role, and 连环 adds or links extra skill targets under a shared condition.
- Use when: the design specifically needs target history, bullying/overmatching by a larger value, or a team-mode link between roles selected by a skill.
- Priority: medium for direct 凌越-like comparison; low for target-history labels and skill-target expansion.
- Guardrails: "每名角色限一次" or direct history wording is often clearer than a named追思 rule. 凌越 can usually avoid skill-target baggage by comparing with "一名角色". 连环-style target expansion is risky because skill rewards are less bounded than card rewards; define target order, symmetry, mandatory/optional linking, and whether added targets receive the same or modified effect.

### 奥秘技 / 隐匿技 / 隐匿标签

- Definition: a skill effect is executed without ordinary declaration, usually before general information is public or because every candidate shares a hiding wrapper.
- Use when: the effect must happen at setup while preserving hidden information, such as initial HP adjustment, hidden-entry state, or equalized opening protection.
- Priority: low and mode-specific.
- Guardrails: the hidden result must be either unobservable or given to all relevant candidates. Do not hide a meaningful choice that other players need to audit. If "隐匿" is only a tag on a broader skill, write which part is hidden and what remains after reveal.

### 主副将技 / 身份技 / 势力技

- Definition: a skill appears on the card but only exists or functions in a matching position, identity, or faction.
- Use when: the mode's visible framework naturally supports the axis, especially 国战主副将 or switchable faction designs.
- Priority: medium for visible two-state axes; low for hidden identity.
- Guardrails: hidden identity skills are hard to balance and reveal. Position/faction skills should be functional in both states, or the user is effectively choosing between two incomplete generals. If a faction skill belongs to a dual-faction design, decide whether the player chooses at setup, switches later, or counts as stacked.

### 发动不属于自己的技能 / 纵横

- Definition: a character borrows, grants, or causes another player to gain a modified version of a skill for a short duration.
- Use when: the fantasy is alliance, teaching, command delegation, possession, or political skill-sharing.
- Priority: low to medium.
- Guardrails: define whose skill version is used, who pays costs, who chooses targets, who is the skill owner/source, whether granted copies stack, and duration. A granted skill should not be so weakened that allies avoid it or so strengthened that it is better to give away than use. Cross-turn grants need a visible reminder.

### 事件牌 / 法则技 / 持恒技

- Definition: a mode card, global rule, or hard-to-disable skill changes the rules outside ordinary personal skill timing.
- Use when: the entire mode is about a law, event, weather, battlefield rule, or deity-like presence.
- Priority: very low for normal generals; medium for modes with explicit event infrastructure.
- Guardrails: do not stack several highest-priority rules without conflict resolution. Leave a defined way for the rule to end, be removed, or be scoped. "Cannot be invalidated" is weaker and safer than "dominates every rule"; use it only when the design would otherwise be invalidated by common seal effects.

### 跨武将效果 / 跨局效果 / 备战技

- Definition: a skill persists across replacement generals, future games, reserve/selection areas, or pre-game setup.
- Use when: 1V1, long campaign, multi-game match, or reserve-general strategy is the mode's real subject.
- Priority: low outside mode play.
- Guardrails: favor comeback or texture rewards over winner snowball. Define where the effect is recorded, when it expires, what happens if the next general or next game cannot use it, and whether it changes selection fairness. In identity games, a reserve-area buff easily becomes a hidden general-spirit bonus; keep it small and optional.

## Recast And Recycling Concepts

Use these concepts when a card or resource is turned into a replacement draw or comparable recycle effect.

### 重铸

- Definition: put a card into the discard pile and draw; later designs may extend the object count, owner, or even non-card objects.
- Use when: a design needs dead-card recycling, flexible filtering, or a low-drama auxiliary benefit.
- Priority: high as a small support operation, medium as a main engine.
- Guardrails: define the rule version if using anything beyond one card you own. Ambiguities include whether multiple cards draw one or equal cards, whether the actor or owner draws when another player's card is recast, and how non-card objects are handled. "依次重铸" is the safest wording when multiple cards are involved.
- Avoid when: it is filler for "give a small reward" but adds no character logic or decision.

## Search And Extra Deck Concepts

Use these concepts when a skill looks through a pile for a matching card or creates a separate searchable supply.

### 检索 / 漫卷 / 发现 / 荐言

- Definition: reveal or inspect cards from a deck, discard pile, or other zone until a qualifying card is found, then obtain or use it. Unordered, semi-ordered, and ordered variants differ in how much choice the searcher has.
- Use when: the character is about records, learning, finding a named tool, selecting from public history, or searching a small bounded subset.
- Priority: medium for narrow public-zone search; low for frequent deep deck search.
- Guardrails: define search zone, order, reveal procedure, stopping condition, failure handling, and where skipped/revealed cards go. Limit depth or frequency; deep ordered search slows the table and can disturb deck order, while unordered discard-pile search can become "pick any strong card" unless tightly constrained by name, category, timing, or count.
- Avoid when: drawing, revealing top cards, or choosing from the discard pile with a simple restriction gives the same play texture.

### 随机检索 / 听用牌堆 / 额外牌堆

- Definition: random search skips the reveal-by-reveal process and outputs a qualifying card; listening/extra decks create a separate finite supply for searchable copies or names.
- Use when: the design is online-only, a mode provides a prebuilt extra deck, or a package needs many "find a named card" effects without repeatedly touching the main deck.
- Priority: very low for normal generals; medium only in modes where the extra deck is a visible shared component.
- Guardrails: random search must state the source pool and be auditable where possible; avoid random access to【桃】【酒】or other survival cards. Extra decks need package scope, card list, duplicate rules, suit/point handling, cleanup, and compatibility with alternate main decks. A partial extra deck changes card ratios, so do not treat it as a perfect replacement for the normal deck.
- Avoid when: the extra deck exists only to imitate online randomness, or when the character can work with a small named special-card set.

## Mechanism Selection

Use these patterns by design need:

- delayed payoff: 施法, 蓄谋, 历战, 使命技, 命运线;
- one-shot or transformation: 限定技, 觉醒技, 昂扬技, 可重置限定技;
- numeric overcommit: 玩点蓄力技, variable count doubling, carefully bounded overpay rewards;
- card identity pressure: 强制更改牌面信息, 强制转化, narrow 视为 rules;
- resolution control: 作废, scoped 终止结算, 强制结束阶段/回合;
- role or blame rewriting: 修改伤害来源, 修改使用者, tightly scoped light 操控;
- card movement or gift politics: 移动, 置入, 置于手上, 合纵, 赠予;
- card recycling or search: 重铸, direct discard-then-draw, current-turn discard reuse, bounded 检索, narrow 荐言;
- non-game-card objects: 对非游戏牌的应用, 物化, 化形牌; use only with explicit card attributes and return rules;
- faction or win-condition pressure: 改变势力, 双势力, 势力技, 僭位; avoid direct alternate victory unless mode-scored;
- skill existence or global rules: 技能目标, 奥秘技, 主副将技, 纵横, 事件牌, 法则技, 持恒技, 备战技;
- HP and body-state language: 残血开局, 护甲, 虚血, 体力下限, 废除/恢复;
- damage and tag language: 属性伤害, 额外牌面信息, 应变标签, narrow 附魔;
- external timing pressure: 并行操作 only for mode-level time/space/UI variables;
- concise binary wording: 对方 when the event is a clean two-party operation;
- risk/reward overreach: 背水, 妄行, 暴虐值, 奋武技;
- cooperation or table bargaining: 拼点, 多人拼点, 协力, 议事, 谋弈, 锻造, 同心;
- public mode resources or tasks: 公共标记, 整肃, concise public tasks;
- relationship or seat scaffolds: 珠联璧合, 宗族羁绊, 同心, 阵法关系, 阵法召唤;
- flexible allocation/choice control: 共计, 分配, 拒绝, 强制发动, 重置技, 枭雄技;
- public or special zones: 标记牌, 仁区, 暗置, 中央区, 额外牌堆, 幻术牌堆, 蓄谋牌, 牌盒, 【影】;
- hidden or alternate identity: 隐匿, 结党, 休整, 替换武将, 流放, 调离, 易位, 异性双人武将, 双势力;
- resource counters: 护甲, 标记, 声明数值, 蓄力标记, 全局计次, 谋略值, 暴虐值, 耐久度;
- state/rhythm switching: 转换技, 韵律技, 连招技, 实体性操作, 连招-like order checks;
- attack-position branches: 游击, 搏击, 摧坚, 击伤, 起义军;
- environment or global pressure: 天候, 光环效果, 持恒技, carefully scoped 回合变动;
- source/response puzzles: 猜测, 谋弈, 智囊, 卜算, 卜卦, 六经, 妙计, 逐鹿;
- fate/random menus: 随机执行, 军令, transparent dice/judgment branches.

## Reviewed Package Mechanism Families

Use these distilled package entries as normal design candidates when they match the character anchor. They are inspirations, not mandatory imports.

| Mechanism | Use For | Guardrails | Package Scope |
| --- | --- | --- | --- |
| 弃牌堆引用 | 残局余波、回收旧事、因弃置而起势；可看本回合弃牌堆、阶段弃置牌、特定牌进入弃牌堆后的回收。 | 限定时间窗、花色/类型、每阶段次数；避免无脑回收关键防御牌。 | OL、SP、一将成名、军争、十周年、十周年小程序、国战、国际服、小程序、手杀、江山如故、游戏模式、神话再临、线下、蚀心入魔、谋攻篇、通用机制 |
| 转化/虚拟牌/牌名声明 | 技艺、伪装、号令、临机借势；适合声明牌名、视为使用、把一类牌转为功能牌。 | 限制牌类、目标、时机和是否触发“使用”；谨慎产出【桃】【酒】等生存牌。 | OL、SP、一将成名、军争、十周年、十周年小程序、国战、国际服、小程序、手杀、江山如故、游戏模式、神话再临、线下、蚀心入魔、谋攻篇、通用机制 |
| 区域选牌/多区交互 | 搜检、调度、拆解装备/判定区/手牌的战术角色。 | 明确可选区域和每区最多数量；避免一次性跨区大拆。 | OL、SP、一将成名、军争、十周年、十周年小程序、国际服、小程序、手杀、江山如故、游戏模式、神话再临、线下、蚀心入魔、通用机制 |
| 移动/置入/赠牌变体 | 区域调度、对象换位、国战合纵、赠物或负面礼物。 | 写清来源和去向，是否算获得/弃置/使用；非国战设计慎用合纵，负面赠予要能拒绝或有足够代价。 | 国战、SP、神话再临、线下、海外版、通用机制 |
| 非游戏牌/物化 | 武将牌、体力牌、身份牌或备用牌被当作卡牌、装备、魂魄或化形物。 | 给出牌名、花色点数、类别、所有者、移动和复位；多将模式与生存牌严格限缩。 | 线下、SP、游戏模式、通用机制 |
| 公共标记/公共任务 | 模式货币、公共进度、整肃训练、短期协作目标。 | 标记必须支持模式主循环；任务要写清统计对象、时限、成功失败和奖励，避免奖励滚雪球或任务喧宾夺主。 | 国战、手杀、游戏模式、谋攻篇、通用机制 |
| 拼点 | 争锋、试胆、较艺、权谋对赌；适合赢/没赢分支或拼点牌归属变化。 | 给没赢一方补偿或代价；不要迷信“拼点无弱将”；多人拼点要定义赢家、平局和拼点牌归属。 | OL、SP、一将成名、十周年、十周年小程序、国战、国际服、手杀、江山如故、游戏模式、神话再临、线下、蚀心入魔、谋攻篇、通用机制 |
| 羁绊/阵法 | 双将配合、宗族包、座次阵型、关系彩蛋。 | 基础强度不能依赖低概率点名；羁绊奖励宜小，阵法要有可操作的座次或揭示手段。 | 国战、OL、SP、海外版、线下 |
| 胜利/势力/君主 | 叛变、归属变化、双势力、野心家、定鼎溃散。 | 不要轻易改他人胜利条件；国战中势力等于胜利条件，身份局中势力多为契合变量。 | SP、国战、OL、游戏模式、线下、通用机制 |
| 技能存在/假技能 | 技能目标、奥秘、主副将技、势力技、纵横授技、事件牌、法则技、备战。 | 写清技能何时存在、谁发动、谁付费、持续多久；普通武将慎用泛用技能目标、跨局、场外和最高优先级规则。 | 国战、手杀、OL、线下、海外版、游戏模式、通用机制 |
| 登场/离场/备用将操作 | 变身、替补、休整、功成身退、备选武将压制。 | 强模式依赖；写清武将牌变化后的体力、技能、标记和延时效果。身份局谨慎使用换将、休整、易位。 | 游戏模式、国战、OL、线下、通用机制 |
| 检索/额外牌堆 | 寻找工具、熟读典籍、从弃牌堆或额外供给中取指定牌。 | 限制检索深度、区域和牌名；随机检索低优先，额外牌堆要写清牌表、花色点数、比例和兼容性。 | 一将成名、SP、国战、线下、海外版、通用机制 |
| 横置/重置/连环 | 连环、牵制、阵型、火雷属性联动；可把横置作为状态门槛或结算资源。 | 遵守横置/重置可用性；不要让横置后的再横置变成空结算。 | OL、SP、一将成名、十周年、十周年小程序、国战、国际服、小程序、手杀、江山如故、游戏模式、神话再临、线下、蚀心入魔、谋攻篇 |
| 武将牌上/私有牌堆 | 记忆、藏物、积累证据、蓄势资源；适合少量命名牌堆。 | 定义进入、上限、离开、可见性、是否可被选取；普通武将少用多堆。 | OL、SP、一将成名、十周年、十周年小程序、国战、国际服、小程序、手杀、江山如故、游戏模式、神话再临、线下、蚀心入魔、通用机制 |
| 目标转移/取消/增减 | 护卫、误导、战术牵引、攻击面控制。 | 高强度语言；限制为特定牌、特定目标数或付出弃牌/失血成本。 | OL、SP、一将成名、十周年、十周年小程序、国战、国际服、小程序、手杀、江山如故、游戏模式、神话再临、线下、蚀心入魔、通用机制 |
| 修改来源/使用者/操控 | 嫁祸、夺功、借刀、夺取选择权。 | 优先轻量化；写清后续触发归属，不要常态剥夺他人回合或把无法预期的负面结算推给第三方。 | 神话再临、一将成名、SP、线下、通用机制 |
| 体力上限/体力流失 | 欲望、代价、透支、不可逆成长/衰败；适合锁定负面或爆发成本。 | 体力上限变化要给恢复路径或明确终局压力；避免与强防御叠成不死。 | OL、SP、一将成名、十周年、十周年小程序、国战、国际服、小程序、手杀、游戏模式、神话再临、线下、蚀心入魔 |
| 非常规体力/废除恢复 | 残血开局、护甲/护盾/虚血、体力牌操作、体力下限、废除区域。 | 先说明契合再给数值；定义缓冲类型、濒死阈值、区域封印和恢复时机，不把它们当强度补丁。 | 神话再临、OL、手杀、海外版、线下、游戏模式、通用机制 |
| 并行操作 | 外部计时、空间移动、模式互动或即时记录。 | 普通武将极低优先；不在并行窗口内造成伤害、濒死、用牌或改目标，优先排队到当前结算后。 | OL、手杀、游戏模式、通用机制 |
| 获得衍生牌/印牌 | 召唤外物、仪式牌、身份信物、临时资源。 | 定义来源、数量、进入区域、离开规则；避免无限印关键牌。 | OL、一将成名、军争、十周年、国战、国际服、手杀、江山如故、游戏模式、神话再临、线下、通用机制 |
| 重铸 | 滤牌、拆解、换工具、把死牌变选择。 | 明确是一张、多张、依次还是等量；重铸他人牌时说明谁摸牌；多次重铸会增加操作负担。 | OL、一将成名、十周年、十周年小程序、国战、国际服、小程序、手杀、江山如故、游戏模式、神话再临、线下 |

## Mechanism Index

### 三国杀移动版

- 智囊: three ordinary trick names, commonly【无中生有】【过河拆桥】【无懈可击】. Use as a compact "tactical trick set".
- 使命技: has success/failure conditions and corresponding effects; becomes invalid after success or failure. Use for one-life vows, duties, or doomed quests. Prefer a clean task template over mixing large passive text into the label.
- 仁区: a public card zone with a small cap. Use when a character contributes to or consumes a shared moral/political resource. Low priority outside a package that defines cleanup and multiple healthy spenders.
- 背水: a special option that executes other options, then pays a consequence; cannot be chosen if the consequence cannot execute. Use for all-in lines.
- 整肃: target chooses/executes a discipline task, then receives reward if not failed. Subtypes: 擂进 uses increasing point sequence; 变阵 uses same suit sequence; 鸣止 discards all different suits.
- 谋弈: user and target secretly or separately choose options; user succeeds if the target does not pick the matching answer. Use for prediction duels.
- 协力: choose a cooperation route with another role until that role's turn end. Routes include damage total, draw total, discarded suits, or used/played suits.
- 护甲: damage buffer with an upper limit. Use for armor-like survivability that is not recovery.
- 蓄力技: shared charge markers across all charge skills on the same character. Use when multiple effects consume one common battery, but define what happens if charge skills are lost, stolen, or regained.
- 持恒技: cannot be disabled by other skill effects. Use sparingly for immutable rules.
- 追思: a status lasting the game; later effects can require targets without that status. Use for memorial/exclusion logic.
- 旧追思-like skill inheritance: gaining skills from a dying or dead role is an entry/exit-adjacent operation. Use only as a narrow memorial payoff; broad skill theft is unstable.
- 虚拟伤害: incomplete damage event that triggers some "about to cause", "after causing", and "after receiving" timings, but does not reduce HP. Use cautiously for "as if harmed" records.
- 结党 / 休整: special multi-character or temporary-exit handling. Use only for unusual identity designs.
- 六经: map classics to card classes or names. Use when a scholar's canon naturally becomes a card taxonomy.
- 金 / 五灵 marks: large bundled mark sets. Treat as inspiration for a menu, but avoid copying many marks into a normal custom general.

### 三国杀：一将成名

- 转换技 state choice: some packages allow choosing 阴/阳 at game start. Use when opening stance matters.
- 连招技: effects that require a sequence of card use. Use for martial rhythm or practiced routines.
- 击伤: body-part injury menu with escalating later option. Use for targeted maiming or hunter/sniper themes.
- 荐言 / 有序检索: reveal through an ordered zone until a match appears. Use only with depth limits and clear handling for skipped cards.
- 随机检索: online-style random access to a qualifying card. Low priority because the process is opaque and can distort deck ratios, especially around survival cards.

### 三国杀神话再临

- 废除 / 恢复: seal and later restore areas or other elements. Prefer self-cost and define recovery; avoid permanent opponent slot removal.
- 残血开局: starts below max HP. Use only when the extra max HP is part of the character's identity or skill loop.
- 玩点蓄力技-inspired numeric charge: overpay or satisfy doubled conditions to double output numbers. Treat as custom vocabulary unless the user asks for that template.

### 三国杀SP / 星SP

- 对方: shorthand for the other participant in a binary operation. Use for Slash/response, Duel, damage pair, or pindian-like events; avoid multi-party ambiguity.
- 漫卷 / 无序检索: choose from an unordered public zone after checking a condition. Use only with tight name/category limits; otherwise it becomes broad discard-pile tutoring.
- 改变胜利条件: alternate win or identity change. Very low priority in ordinary identity play; prefer post-game bonus win or mode score progress.

### 三国杀OL

- 隐匿: starts as male/no-skill hidden form, then reveals after HP loss or before turn. Use for ambush, disguise, or delayed true form.
- 并行操作-like interaction: live UI or timer actions during another resolution. Keep as mode infrastructure and queue real game effects safely.
- 宗族技: same-clan generals share a clan skill; clan membership follows history, not whether a general owns the skill.
- 金兰武将 / 宗族羁绊: relationship hooks attached to a small named group. Use as a package-visible bonus, not as the main engine of a random identity general.
- 卜算X: 观星-like top-deck viewing with explicit count. Use as a concise divination term.
- 天候: global weather states such as heat, fog, rain, frost. Use for environment-driven generals, but watch passive table burden.
- 锻造: table chooses助力/妨害, compares revealed point totals, and determines crafting quality. Use for smithing, collective projects, or contested production.

### 三国杀国战

- 珠联璧合: dual-general relationship reward. Use when the pair can be intentionally selected and the base balance accounts for the bonus; avoid treating every historical acquaintance as a bond.
- 阵法技 / 阵法关系: effects based on seat adjacency or relative position. Use only when formation is a real strategic object; provide fallback value if seating fails.
- 阵法召唤: invite or reveal unrevealed allies into a formation. Use when allies have a real reason to respond and revealing is worth the risk.
- 合纵: give a coalition card to another player and usually keep some reward for yourself. Best in 国战 politics; in identity games, translate it into ordinary aid or bargaining instead of importing the label.
- 公共标记: mode currency or public progress. Strong for activity or faction modes when tied to the main loop.
- 君主 / 定鼎 / 溃散: lord-center mechanics. Keep early, mode-bound, and define how wild ambition or faction collapse is recalculated.
- 双势力 / 改变势力: in 国战, faction is a win condition; avoid mid-game faction hopping unless the mode is built for it.
- 主副将技 / 奥秘技: position or hidden setup skills. Use when the mode already has hidden generals and visible main/deputy positions.
- 明置/暗置武将牌 / 变更 / 加入游戏: command-center operations on general cards. Keep them in 国战-like frameworks and define cross-turn effects before moving them into identity play.
- 调离: temporary removal from ordinary card participation, often tied to force-size politics. Define what still affects the role and avoid using it as routine invulnerability.
- 易位: exchange general cards or positions. Best in team or reserve-general modes with consent or clear limits; forced identity-mode exchange is usually hostile.
- 发现 / 半有序检索: search an unordered zone with a forced first match. Safer than broad unordered choice, but still define search start and match handling.
- 纵横: grant a modified version of a skill to selected roles. Define owner, duration, chosen targets, and whether the granted version is weaker or stronger.
- 暴露野心 / 僭位: ambition reveal or transformation. Use only for 野心家-centered designs with visible cost and betrayal risk.

### 三国杀海外版

- 施法: delayed effect with chosen delay count, usually 1-3. X equals chosen delay. Use for rituals or brewing consequences.
- 妄行: user chooses X up to a cap, then pays at turn end if the skill was used. Use for deliberate excess.
- 摧坚: once per turn after using damage card, X depends on target skill count. Use for anti-expert or armor-breaking attacks.
- 游击 / 搏击: extra effect based on whether target is outside or inside attack range. Use for distance-position identity.
- 凌越 / 连环: weak skill-target-related wrappers. Prefer direct comparison for 凌越; use 连环 only in team modes with explicit added-target rules.
- 昂扬技: limited skill that can be refreshed after an "激昂" condition. Use for heroic comeback surges; keep the refresh condition rare enough that it still feels special.
- 历战: if used this turn, upgrade/modify the skill at turn end for the whole game. Use for campaign growth.
- 同心: choose a partner until next turn; both execute linked effects. Use for paired or oath designs, but avoid making it a generic wrapper that forces relationship flavor onto unrelated skills.
- 异性双人武将: counts as both male and female. Use for dual-character sex-related interactions.
- 暴虐值: charge by causing or receiving damage, cap 5, then consume for effects. Use for violent momentum.
- 卜卦: use a top-card or sign-like procedure to determine one of several omen branches. Use only with a small branch set and clear timing.
- 护甲/护盾-like buffers: distinguish what they prevent and whether they affect hand size or HP loss.
- 武 marks / 布道 skills: large arsenals or spell lists. Use as menu inspiration, but reduce option count for normal designs.

### 欢乐三国杀

- 逗猫: passing marker with start/end upkeep. Use for playful recurring attention, but avoid nuisance loops.
- 念影: branch count grows with related-character ownership. Not recommended unless the environment supports collection-based scaling.
- 幻术牌堆 / 幻术牌: copied deck and fake cards with destruction rules. Use only for high-complexity illusion specialists.
- 军令: a small command menu: damage, random discard, no healing, or severe hand/skill restriction. Use as compact military orders.
- 事件牌 / 法则技-like rules: global event infrastructure. Use for modes, not ordinary generals.

### 游戏模式

- 并行操作: operations driven by external time, space, or live mode UI. Prefer recording pending results and resolving after the current flow.

### 三国杀小程序

- 韵律技: conversion skill with 平/仄 states; "转韵" flips state and resets use count. Use for poetry, music, rhythm, or alternating tempo.
- 谋略值 / 妙计: strategy points up to 5; spend 1-3 to use 拆/无懈/无中. Use for tactical resource conversion.
- 逐鹿: multi-player pindian, unique highest point wins. Use for contesting leadership; define ties and exposed-card handling.
- 奋武技: per-round use count equals damage caused plus received plus one, capped. Use for battle heat or revenge momentum; an explicit dynamic use limit may be clearer than a new label.

### 线下

- 议事: participants reveal a hand card; red majority, black majority, or tie determines result. Use for court debate, assembly, or public will.
- 双势力 / 势力技能 / 变更势力: choose or change faction; faction skills only work when current faction matches. Use for allegiance shifts.
- 赠予: give a card as a gift or planted burden. Use for object-based diplomacy or intrigue; let harmful gifts be rejectable or costly, especially when they replace equipment.
- 【影】: special spade-A basic cards that cannot be used or played and leave the game after discard. Use for shadow tokens carried as real cards.
- 蓄谋: set hand cards face down in judgment zone; process later in reverse order. Use for plots that can be disrupted while waiting; keep visibility and return/use timing explicit.
- 额外牌堆: separate finite decks for searchable or named special cards. Use when a mode needs visible extra supply; define list, duplicates, suit/point rules, and compatibility with the chosen main deck.
- 双副类别装备: one equipment occupies two slots and is replaced by either slot. Use for grand artifacts with real opportunity cost.
- 起义军: indicator with increased slash pressure and end-turn obligation. Use for insurgency, faction infection, or forced aggression.
- 体力牌操作 / 勾玉颜色: visual HP operations. Use only when the physical display itself is the fantasy.
- 体力下限 / 额外濒死: dying-threshold extensions. Very low priority; define threshold and leaving-dying rules.
- 备战技: reserve or selection-area effect. Better for long games or 1V1 than ordinary identity play.
- 对非游戏牌的应用 / 物化: general, identity, or HP cards become card-like objects. Define attributes, zone movement, and reset/return.

### Custom/Conceptual Zone Vocabulary

- 标记牌: real cards stored as markers or resources. Use with caps, spending motives, and skill-loss handling.
- 公共标记: shared counters or currency. Use as mode-level infrastructure with public acquisition/spending rules.
- 非游戏牌 / 物化 / 化形牌: non-game components treated as card-like objects. Use only with explicit attributes and return rules.
- 移动 / 置入 / 置于手上: exact card or object relocation. Use when route matters; otherwise prefer 获得、交给、弃置、置于牌上.
- 暗置: a face-down judgment-area storage rule with limited visibility and automatic release. Use for hidden delivery or delayed hand access when the environment supports the rule.
- 中央区: a named subset of recent discard-pile cards. Use when several effects repeatedly care about recent cards; otherwise write the time window directly.
- 有序弃牌堆: discard pile treated as an ordered stack. Use only when the table or platform can maintain order reliably.
- 牌盒: out-of-game box for special cards. Use for modes or package centerpieces; avoid for one-off ordinary generals.
- 检索: reveal or inspect through a zone until a qualifying card appears. Prefer small depth and public zones.
- 听用牌堆 / 额外牌堆: separate search supply. Use as package infrastructure, not a one-general shortcut.

### Conceptual Social/Random Vocabulary

- 猜测: public/verifiable prediction. Use for bluffing and mind games with moderate stakes.
- 合纵 / 赠予: transfer-with-politics vocabulary. Keep package/mode assumptions visible and define consent for negative gifts.
- 羁绊 / 珠联璧合 / 宗族羁绊 / 同心: relationship rewards. Best when partner selection is controllable; keep the base skill functional alone.
- 阵法关系 / 阵法召唤: seat-position relationships. Use for 国战 or team modes with formation tools, not random-seat ordinary identity designs.
- 不可见元素: hidden information not auditable by players. Low priority; usually online-only or self-only.
- 随机执行: random selection among known options. Prefer judgment/dice and equal transparent odds.
- 道具抽签 / 刮彩票: physical random props. Low priority unless the mode provides reusable components.
- 游戏外元素 / 小游戏 / 无关文本: flavor or side activity outside core rules. Keep cosmetic or tiny; avoid normal competitive designs.

### Conceptual Resolution/State Vocabulary

- 作废: declaration-time cancellation of a card use. Use only at the early safe timing.
- 终止结算: stop a current flow. Low priority; needs one-layer scope and cleanup.
- 强制结束: forcibly end a phase or turn after current resolution. Strong tempo tool; cost it carefully.
- 废除 / 恢复: seal and later restore slots, phases, or other elements. Define irreversibility and memory.
- 修改伤害来源 / 修改使用者: reassign event responsibility. Low priority unless blame/credit transfer is the character's core.
- 操控: direct control over another player's choices or turn. Prefer light, bounded control that preserves some agency.
- 对方: binary-operation shorthand. Write full role names when more than two participants exist.
- 属性伤害: fire/thunder-like damage attributes. Use only when the attribute has supporting rules.
- 额外牌面信息: card tags or conditional labels. Keep tags visible and rules-light.
- 技能目标: define only for a self-contained skill or skill family; avoid assuming every skill has targets.
- 实体性操作: orientation/state changes such as 横置、翻面、叠置. Require unique visual cues.
- 登场/离场操作: general-card replacement, rest, re-entry, exile, hidden/reveal, and exchange. Reserve for modes or true transformations.
- 非常规体力: residual HP, armor, shield, virtual HP, HP-card operation, and dying-threshold changes. Use for fit, not balancing by number.
- 事件牌 / 法则技 / 持恒技: global or hard-to-disable rule text. Reserve for mode rules or carefully scoped deity/boss designs.
- 并行操作: parallel game operation during another resolution. Extremely low priority for generals; queue or defer real effects.
- 回合变动: skip, add, or modify turns/phases. Prefer direct actions unless phase triggers matter.
- 预演: snapshot/rollback or rehearsal. Very low priority outside experimental modes.

### Conceptual Count/Task/Choice Vocabulary

- 限定技: once-per-game decisive skill. Use for real "big move" moments, not small bonuses.
- 觉醒技: compulsory lasting transformation. Preserve identity across the change.
- 可重置限定技 / 昂扬技: limited skill with a refresh condition. Match reset rarity to payoff.
- 玩点蓄力技: numeric overpay/condition-doubling template. Keep output small and the doubled timing explicit.
- 使命技: task with success/failure. Keep success and failure ordering explicit.
- 命运线: route or progression system. Reserve for deity, boss, or mode-centerpiece scale.
- 改变胜利条件: very low priority. Prefer mode scoring or post-game additional win over immediately ending the game.
- 改变势力 / 双势力 / 势力技: use when faction is identity, not decoration. Define one-time choice, stacked state, or switch timing.
- 整肃 / 协力: public task templates. Use concise task/reward wording and avoid broad cross-turn tracking unless cooperation is the core.
- 共计 / 分配: divide a total among recipients/effects. Define total, per-target bounds, and simultaneity.
- 拒绝: high-level refusal option. Use to soften or dramatize forced interactions.
- 强制发动: temporary compulsion of an optional skill. Usually safest on the user's own skills.
- 重置技 / 枭雄技: multi-option depletion or final-option systems. Keep option count small and visible.

## Special Card Design Patterns

### Reviewed Special Cards By Package

Package labels matter. Do not use a package's card names or assumptions when the user excludes that package.

OL:

- 【有难同当】: all targets横置. Use for mass chain state, shared peril, or coerced alliance.
- 【雷公助我】: all targets perform【闪电】judgments; the user draws for damage caused this way. Use for risky global thunder ritual.

SP:

- 【言笑】: delayed judgment-area card; when it resolves, the target obtains all cards in their judgment area. Use for delayed cleansing or storing future release.

国战:

Use cautiously outside 国战. Translate away 明置/暗置、大小势力、队列、阴阳鱼、主副将 unless the user asks for 国战.

- 【以逸待劳】: same-force allies draw two then discard two. Use for team filtering without net universal gain.
- 【知己知彼】: inspect a hidden general card or hand. Outside 国战, map to hand or identity information.
- 【远交近攻】: a different-force visible target draws one, then you draw three. Use for asymmetric diplomacy.
- 【勠力同心】: unchained targets become横置; chained targets draw. Use for chain-state fork.
- 【挟天子以令诸侯】: end play phase and possibly gain an extra turn later. Extra-turn language needs heavy cost.
- 【敕令】: unknown-force roles choose reveal, discard equipment, or lose HP; the card leaves game instead of discard. Use for edict pressure.
- 【火烧连营】: fire damage by seat/formation. Outside 国战, map to adjacent, distance, or formation logic.
- 【联军盛宴】: self chooses recover/draw by another force size; others draw and reset. Use for feast-style asymmetric support.
- 【调虎离山】: temporary removal from distance/seat/targeting/HP-change calculations. Use only with clear duration.

游戏模式:

- 【浮雷】: moving thunder judgment with escalating damage count. Use for accumulating threat that passes between roles.
- 【草木皆兵】: failed judgment reduces target draw and rewards distance-1 roles. Use for panic aura around a target.
- 【增兵减灶】: target draws three, then discards one non-basic or two cards. Use for generous but taxed logistics.
- 【声东击西】: you hand a card to a nearby role, then that role passes cards to a third role. Use for forced relay and distance bargaining.
- 【弃甲曳兵】: target chooses to discard weapon/offensive-mount side or armor/defensive-mount side. Use for equipment taxonomy pressure.
- 【金蝉脱壳】: protects when it is your only hand card, and draws when discarded. Use for last-card escape.
- 【毒】: poisonous hand object that causes HP loss when used or when it leaves hand face-up; one variant can be passed away after drawing. Use for contaminated resource design.
- 【偷梁换柱】: randomly redistributes equipment. Use only when chaos/randomness is central.
- 【强兵足食】/【强易】: special-resource logistics and taxed intelligence theft. Treat as mode-specific unless the resource is redefined.
- 【文和乱武】: all others choose to slash nearest role or lose HP. Use for panic-order pressure.
- 【斗转星移】/【李代桃僵】: random HP or hand redistribution. Use only for fate/chaos designs.
- 【影】: inert real-card token that cannot be used and leaves game after discard. Use for shadow tokens.
- 【笑里藏刀】: target draws by lost HP up to a cap, then you damage them. Use for gift-then-harm.
- 【美人计】: gendered multi-role hand transfer and hand-count damage. Use only when gender politics is central.
- 【草船借箭】: cancels a slash/damage trick against you, then obtains it after resolution. Use for defensive capture.
- 【解甲归田】: target obtains all cards in their equipment area. Use for demobilization or disarm-with-compensation.
- 【逐鹿天下】: reveal equipment from deck/discard, targets sequentially equip. Use for public equipment draft.

线下:

- 【一鼓作气】: this turn, your card uses ignore distance and use-count limits. Strong; attach cost or narrow timing.
- 【万物智联】: redistribute equipment and attach energy recover/consume to gain/loss. Use for high-concept equipment network.
- 【以毒攻毒】: inspect wounded target's hand; if both sides have【毒】, cleanse and draw, otherwise both suffer sourceless damage. Use for mutual-risk diagnosis.
- 【大军压境】: other roles may slash one target with no distance/count limit. Use for siege pressure.
- 【火烧连营】: reveal a target card, discard same-suit hand card to burn/discard; chained state modifies outcome. Use for suit-match burn.
- 【玉石皆碎】: deal 1 damage, then lose 1 HP. Use for simple mutual destruction.
- 【荆襄盛世】: reveal cards by living roles; chosen targets take one each, user gains rest. Use for prosperity distribution.

通用机制:

- 【蓄谋】: delayed plotted card processed later from last placed to first placed. Use for visible delayed schemes.

Use special cards as design vocabulary:

- response fork:【奇正相生】asks for different responses depending on assigned role; good for two-line pressure.
- hand balancing:【调剂盐梅】moves hands toward equality and can recycle if the equality condition holds.
- deck-reveal assault:【兵临城下】reveals top cards and uses the revealed【杀】in sequence.
- area exchange:【瞒天过海】takes from targets' regions and gives cards back.
- poisonous hand object:【毒】punishes face-up loss unless routed away; pair with cleanse cards like【刮骨疗毒】.
- enhanced attack basic:【刺杀】adds a discard tax to【闪】responses.
- equipment-to-draw conversion:【树上开花】turns discards, especially equipment, into draw.
- close-range exchange:【推心置腹】and【逐近弃远】care about distance and region cards.
- revealed-card threat:【趁火打劫】and【出其不意】turn hand information into damage or theft pressure.
- top-deck control:【洞烛先机】looks at top cards, reorders, then draws.
- previous-card mimicry:【随机应变】copies the previous basic/trick used or played this turn.
- attribute/disruption attack: 冰【杀】can trade damage for discarding target cards.
- equipment punishment:【水淹七军】forces equipment discard or thunder damage.

## Equipment And Treasure Vocabulary

Common equipment motifs:

- high-range siege weapons: 大攻车, 霹雳车. Use for siege, durability, and equipment suppression.
- unlimited or modified【杀】: 元戎精械弩, 思召剑, 烈淬刀, 银月枪.
- response restriction: 太极拂尘, 思召剑, 赤血青锋.
- broad defense: 奇门八卦, 国风玉袍, 红棉百花袍, 护心镜.
- damage compression or prevention: 照月狮子盔, 琼梳, 护心镜.
- hand/phase treasures: 金梳, 犀梳, 天机图, 虚妄之冕.
- chain/control treasures: 太公阴符, 乌铁锁链.
- virtual-use treasure: 照骨镜.
- durable/special artifacts: 大攻车 variants, 霹雳车 variants, 双副类别装备.

When borrowing equipment language for a general, decide whether the character creates equipment, borrows equipment, treats a card as equipment, or uses an equipment-like rule without adding new cards.

## Low-Priority Card Vocabulary

Use these only when the general has a concrete object, artifact, mount, weapon, or armor fantasy. Usually borrow one small rule shape instead of creating the whole card or an equipment engine.

- OL: 【菌子（五菇丰登衍生）】、【商鞅变法】、【五菇丰登】、【铁蒺玄舆】、【飞轮战舆】、【束发紫金冠】、【三略】、【传国玉玺】、【八尺琼勾玉】、【平安御守】、【鬼龙斩月刀】、【赤焰镇魂琴】、【修罗炼狱戟】、【鸾凤和鸣剑】、【刑天破军斧】、【金乌落日弓】、【无双方天戟】、【镔铁双戟】、【百辟刀】、【真龙长剑】、【秦弩】、【雷切】、【童子切安纲】、【妖刀村正】、【手里剑】、【七彩神鹿】、【三首】、【玲珑狮蛮带】、【钩镶】、【昔具足】、【绝尘金戈】
- 十周年: 【天雷刃】、【红缎枪】、【混毒弯匕】、【水波剑】
- 国战: 【玉玺】、【定澜夜明珠】、【吴六剑】、【三尖两刃刀】、【飞龙夺凤】、【戢鳞潜翼】、【惊帆】、【六龙骖驾】、【明光铠】、【太平要术】、【盟军大纛】。Use only for explicit 国战 or carefully adapted designs.
- 国际服: 【灵宝仙葫】、【冲应神符】
- 手杀: 【六龙骖驾】、【先天八卦阵】、【仁王金刚盾】、【桐油百韧甲】
- 游戏模式: 【铜雀】、【青囊书】、【传国玉玺】、【信鸽】、【锦盒】、【五行鹤翎扇】、【七宝刀】、【衠钢槊】、【折戟】、【七星宝刀】、【倚天剑】、【无锋剑】、【涯角枪】、【驽马】、【黑光铠】、【烂银甲】、【引蜂衣】、【女装】、【太平要术】、【引蜂甲】、【夜行衣】、【战象】
- 线下: 【扑克牌组（四花色1-13）】、【春秋笔】、【湖海笔】、【马鞭】、【浑天仪】、【铁蒺藜骨朵】、【宣花斧】、【百辟双匕】、【魂·诸葛连弩】、【剑】、【刀】、【斧】、【戟】、【枪】、【弓】、【刑鞭】、【众】、【飞龙夺凤】、【尚方宝剑】、【軨軨】、【魂·八卦阵】

## Design Cautions

Do not combine multiple high-burden systems in one normal general. For example, avoid putting delayed casting, public zones, charge points, and special cards into the same compact custom design.

Menus with many marks or subskills are suitable for boss, deity, or package-centerpiece characters; for ordinary generals, compress to 2-3 options or one visible axis.

Special zones and extra decks need precise movement rules. Define entry, cap, ownership, whether cards count as hand/equipment/judgment, and where they go when discarded.

If a mechanism creates a new card or virtual card, check survival cards, response timing, and whether it triggers "use", "play", "lose", or "enter discard pile" events.

If using official special cards in a custom skill, prefer naming a narrow set rather than "any special card". A small named set is easier to test and balance.

## Adding Future Mechanism References

When the user provides new mechanism material and asks to improve this skill, extract:

- mechanism name and source scope;
- one-sentence definition in 三国杀 rules language;
- when to use it in character design;
- guardrails, especially loops, survival-card generation, extra turns, global listeners, and hidden memory;
- one compact wording template or example if the mechanism has a stable shape;
- whether it is normal priority, low priority, mode-specific, or only flavor vocabulary.

Merge the result into the closest section instead of creating a new one for every source.
