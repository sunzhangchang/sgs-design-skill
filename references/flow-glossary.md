# Game Flow Glossary For Design

Use this reference when a design changes turn order, grants extra turns or phases, skips turns or phases, relies on before/within/after timing windows, or interacts with dying, death, and kills. It distills the reviewed 三国杀官方规则集 3.0 flow glossary and game-flow page into design checks rather than reproducing the full procedure.

## Game Start And End

- “游戏开始前亮出武将牌后”“游戏开始前分发起始手牌时” and “游戏开始时” are distinct timing points. Do not collapse setup into one generic start trigger.
- Receiving starting hand cards is not treated as gaining cards for skills whose trigger is obtaining cards. Do not assume an opening deal triggers ordinary gain effects.
- Once a game-ending condition is met, all resolution stops and the game ends. Do not continue queued triggers, responses, or cleanup after that point.

## Turn Order And Turn Scope

- The lord takes the first turn, then turns normally proceed counterclockwise. After one turn ends, the next character in that order starts a turn unless another rule changes the sequence.
- “上家/下家” are seat-order references. In a two-character game, each character is both the other's upper and lower adjacent character, so wording that assumes two distinct adjacent characters needs a special check.
- An extra turn is inserted before or after another turn and changes the future turn sequence. Multiple extra turns may queue; do not describe them as if they were merely extra phases.
- If a skill is activated outside every character's turn, effects scoped only as “本回合内”“此回合结束时” or similar may have no valid turn to reference. State the duration or settlement point explicitly.

When designing an extra-turn effect, identify the anchor turn and insertion side:

```text
锚定回合：
插入位置：该回合开始前 / 该回合结束后
额外回合结束后的下一回合：
是否可能连续插入：
```

## Phases And Skipping

The normal turn has six phases in order: preparation, judgment, draw, play, discard, and end.

- For the ordinary turn procedure, distinguish the boundary timings (“开始前/开始时/结束时/结束后”), the phase interval itself, and the gaps between adjacent phases. A trigger tied to one does not automatically occur at another.
- “阶段内” covers the interval from that phase's start through its end. If “你的……阶段” or the relevant turn owner is omitted, make sure context still identifies whose phase is meant.
- An extra phase is executed immediately at the granted point. It is not a full turn and does not naturally carry the separate “before this phase starts” or “after this phase ends” intervals described for the normal phase sequence.
- If a card or skill mentions “…阶段” without naming whose turn, use the skill owner's phases when the phrase determines that skill's timing; otherwise use the phases of the turn in which the skill was activated. Treat “阶段内” as a time interval, not as an extra activation timing. A granted extra phase has no ordinary phase-start-before or phase-end-after window unless the effect explicitly creates one.
- Skipping a phase or turn means its internal procedure does not execute. Do not trigger an effect from an event that only would have occurred inside the skipped procedure.
- A skipped phase can still leave a timing interval between adjacent phases; however, if adjacent phases are also skipped, their shared interval may disappear. Avoid designs that depend on an unspecified gap around several skipped phases.
- The same phase cannot be skipped twice in one turn. A second attempt should not be treated as another successful skip or another cost payment unless the skill explicitly defines a different event.
- Skipping an entire turn also skips that turn's “after the turn” handling and moves to the next valid “before the turn starts” point. Do not place mandatory cleanup only at the end of a turn that the same design can skip.

Before writing phase-flow text, distinguish these operations:

- gain an extra phase: execute one phase immediately;
- repeat a phase: execute another instance, with its own internal events;
- skip a phase: omit its internal procedure;
- end a phase: terminate the current phase after it has begun;
- gain an extra turn: insert a complete turn and alter turn order.

These are not interchangeable even when they produce a similar amount of actions.

## Ordinary Phase Procedures

The ordinary phase procedures can themselves impose ordering constraints:

- During the judgment phase, resolve the last delayed trick placed in the judgment area first, then repeat the check until none remain. Avoid wording that assumes a different fixed order.
- In the draw phase, finish modifying the draw count and then draw that adjusted number before carrying out a dependent follow-up effect. Do not interleave the follow-up with count modification or partial drawing unless a rule explicitly says so.
- In the discard phase, compare the hand size with the current hand limit and discard the difference. If a skill changes hand limit or modifies discarding, identify which value and operation it affects.
- “出牌阶段” as a skill timing does not mean any instant while the phase remains active. An ordinary active skill limited to the play phase can be used only at an idle timing; when a card, skill, or response is resolving, wait until that event finishes. A phase-limited use restriction counts across the whole phase, even though the phase has multiple separate idle timings.

## Dying, Death, And Kills

- When a living character's HP is reduced to 0 or less, that character enters dying. A newly created dying event can interrupt an unresolved dying procedure; only the character in the innermost current procedure is treated as dying at that moment.
- If maximum HP is reduced to 0, the character dies directly without entering dying or receiving rescue. A design that changes maximum HP must test this route separately from ordinary damage or HP loss.
- Death does not mean setting HP to 0. A character who dies while having positive HP keeps that HP value, and a dead character's HP does not continue changing.
- “Killed” is narrower than “dies”: a damage source kills a character only when its damage makes that character enter dying and the character is not saved in that dying procedure. Death from HP loss, maximum HP becoming 0, or another sourceless route is not automatically attributed as a kill.

For effects that reference dying or death, record:

```text
进入濒死的原因：伤害 / 失去体力 / 其他
当前濒死角色：
是否可能嵌套濒死：
死亡路径：未被救回 / 体力上限降至0 / 其他
是否需要“杀死”与伤害来源：
```

## Design Checklist

Before finalizing a flow-sensitive skill, verify:

- the timing belongs to a specific game, turn, phase, card-use, damage, dying, or death line;
- setup timings, the game-start timing, and the point where a game-ending condition is met are handled distinctly;
- “开始前”“开始时”“阶段内”“结束时”“结束后” are not treated as synonyms;
- a phase active-use skill is not inserted into an occupied resolution, and its phase-limited frequency is counted across all idle timings in that phase;
- phase-procedure follow-up effects wait for prerequisite operations such as adjusted draw counts to finish;
- an extra phase is not accidentally given the full boundary windows of a normal phase in sequence;
- skipped procedures do not produce internal events, and cleanup is not stranded inside a skippable turn or phase;
- an outside-turn effect has an explicit duration and settlement point;
- a duration such as “本回合内” has a real current turn to anchor to; an effect created outside every character's turn cannot silently borrow the next turn or a previous turn;
- nested dying cannot make the skill refer to two characters as the current dying character;
- maximum-HP-to-0 death is handled without a rescue window;
- “死亡”“杀死”“造成伤害”“令其进入濒死” are used only when their attribution requirements are actually met.
