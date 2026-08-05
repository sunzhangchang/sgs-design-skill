# Resolution And Control Concepts

This file is a focused mechanics slice. Read it only when `../mechanics-index.md` routes here for the current design need.

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
