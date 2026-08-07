# Design Heuristics For 三国杀 Generals

These notes condense recurring design ideas from the referenced Bilibili design essays. Use them as heuristics, not as canon text to quote at length.

Sources used for this reference:

- https://www.bilibili.com/opus/1107326926420181009
- https://www.bilibili.com/opus/825088145580097537
- https://www.bilibili.com/opus/745737843276513317
- https://www.bilibili.com/opus/693405298689310759
- https://www.bilibili.com/opus/674737966604615718
- https://www.bilibili.com/opus/657130146618146848
- https://www.bilibili.com/opus/767005993036939264
- https://www.bilibili.com/opus/771493374882480193
- https://www.bilibili.com/opus/802610872555929635

## Contents

- `Design Origin`: choose the design发端 before drafting.
- `Anchors`: translate character facts, temperament, and failure modes into rules.
- `Skill Structure`: build and diagnose type, timing, condition, cost/action, effect, and aftereffect.
- `Timing Map`: place triggers on game, turn, card-use, or damage lines, then identify whether the event is pending, being modified, settled, or finished.
- `Effect Role Map`: map character anchors to attack, defense, burst, control, support, neutral, or special roles.
- `Simplicity`: keep the resource axis, memory, and trigger burden low.
- `Tabletop Feasibility`: keep designs executable in face-to-face play unless the brief says otherwise.
- `Linkage Patterns`: build produce/consume, hub/spoke, relay, open-node, or conflict links.
- `Clan And Family Design` and `太原王氏: 中流`: choose family language by individual orientation.
- `Locked Skills`: use locked labels for true compulsory structure and choose the lock type.
- `Support With Solo Play`: keep assist designs playable in duel.
- `Balancing Valves`: tune power through costs, targets, card classes, and source zones before hard limits.
- `Role Shape And Breakpoints`: give each general a specialty, weakness, and interactive opening.
- `Play Experience`: check what the player actually does.
- `Wording Checks`: verify "并/然后", source ownership, and virtual-card flow.

## How To Use This Reference

For fresh design, do not read this as an essay. Use this order across the conversation:

1. `Design Origin`: decide why this general exists.
2. `Anchors`: reduce the character to 1-3 usable anchors.
3. `Effect Role Map`: choose primary and secondary roles.
4. `Skill Structure` and `Timing Map`: place each skill before polishing text.
5. `Simplicity`, `Tabletop Feasibility`, and `Linkage Patterns`: remove brittle parts and choose the relationship between skills.
6. `Balancing Valves`, `Role Shape And Breakpoints`, and `Play Experience`: tune table pressure and solo play.
7. `Wording Checks`: finalize wording and object names.

If the user is still answering early questions, read only the sections needed for the current step. For example, do not read `Balancing Valves` before the rough mechanical direction exists, and do not read naming guidance unless a name or generated object is needed.

For review/rebalance, use this order instead:

1. Identify the user's stated problem and the current main game plan.
2. Check `Skill Structure` and `Timing Map` first if the problem involves insertion, damage, HP changes, target changes, or phase/turn flow.
3. Check `Linkage Patterns` if the problem is stiff combo logic, forced synergy, or skills with no independent job.
4. Check `Balancing Valves` and `Role Shape And Breakpoints` if the problem is strength.
5. Preserve the user's intended fantasy unless the fantasy itself causes the problem.

## Design Origin

Choose the design发端 before drafting skills:

- 立意驱动: start with a narrative or thematic question, then choose the character. Use when the user's main request is an interpretation, tragedy, relationship, or ideological contrast.
- 隐喻驱动: start with a spiritual core or private/emotional analogy, then choose the character. Use when the character is meant to carry an inner conflict, negative trait, or macro-narrative.
- 玩法驱动: start with a core play pattern, then choose the character. Use when the user asks for a mechanical experience such as 消消乐, 任务, 赌, rhythm, or a specific card-flow engine.
- 命题作文: start with fixed external requirements, then identify what still belongs to the character. Use when the user requires a clan skill, a specific official mechanic, strict complexity limits, or adaptation into an existing design language.

Do not confuse origin with final text. A 玩法驱动 design still needs character fit; a 立意驱动 design still needs playable choices.

## Anchors

Start from a small set of anchors. Good anchors are concrete enough to become rules: "善清谈" can become reveal/view/name/type; "豪侈逞欲" can become compulsory overreach or compensation; "战功事功" can become using cards that already entered the discard pile this turn.

Make positive and negative anchors interact. A good pattern is:

- active skill creates access or choice;
- family/identity skill opens the repeated operation;
- locked skill taxes excess, forces compensation, or narrows the route.

For sparse historical records, do not merely restate the record. Add one deliberate再创作 angle: contrast, imagined emotional viewpoint, inherited symbol, or a "what problem does this life pose?" question. Keep that angle visible in skill names, costs, or target logic.

Prefer a layered story over repainting one static trait. Let different clauses show different stages, routes, or contradictions if the added complexity pays for itself.

## Skill Structure

Use the six-part structure as a drafting and debugging lens:

- Type label: technical or flavor label such as 锁定技, 限定技, 觉醒技, 转换技, 宗族技, or no label. Use a label only when it clarifies execution, presentation, or family/mode handling.
- Timing: the exact point on a line such as game start/end, turn phases, card use/target/resolution, damage/dying, death, pindian, discard, or skill resolution. Most non-static skills need explicit timing.
- Condition: the gate that must be true, such as hand/HP comparison, target identity, card type, zone state, or whether a previous event happened. Avoid global/deck-structure conditions unless the character or mode truly needs them.
- Cost/action: the commitment that makes the skill really fire, such as discarding cards, losing HP, reducing max HP, giving cards, choosing targets, or viewing cards. If later effects require this action to happen, make that dependency explicit with "若如此做", "并", or equivalent wording.
- Effect: the actual payoff. Keep it focused; if an effect contains new timing, condition, action, and payoff layers, check whether it should become another skill or be simplified.
- Aftereffect/price: the tail consequence, often negative or delayed. Use it to show failure, overreach, backlash, or risk, but avoid attaching a decorative punishment that does not tax the route the skill encourages.

When a draft feels wrong, identify which structural part is failing: missing timing, false cost, overbroad condition, overloaded effect, or unrelated aftereffect.

## Timing Map

Treat timing as both a rules hook and a reading-cost signal. A simple, familiar timing makes a skill easier to trust; a timing that mixes several conditions or inserts into another resolution should earn that complexity.

Before writing exact text, place the skill on a line:

- Game line: game setup, game start, game end. Use for initial identity, starting resources, global premises, or victory-related structures.
- Turn/phase line: before a turn or phase, phase start, phase body, phase end, turn end, after turn. Use "before" mostly for skipping or replacing the next procedure; use phase start to modify the phase; use phase end to summarize what happened in that phase.
- Card-use line: use a card, specify targets, become a target, target is settled, card takes effect, card resolves. Use active target changes at "指定目标时"; defensive target changes at "成为目标时"; use "后" only when the result is known.
- Damage/dying/death line: causing damage, receiving damage, HP loss, entering or resolving dying, death, after damage. Use "造成/受到伤害时" for prevention or damage-number changes; use "造成/受到伤害后" for rewards, sell-blood, or checks that require actual damage.
- Skill-resolution or other created lines: use only when the design really needs to respond to another skill or special event. Prefer resolving after the current flow if the exact insertion point would be hard to explain.

Use this recognition pass before choosing the final phrase:

- If the effect skips, replaces, or blocks a future procedure, the timing usually belongs before that procedure starts.
- If the effect changes a number, target set, validity, or damage amount, the timing usually belongs while that event is being created or settled.
- If the effect rewards, punishes, or summarizes something, the timing usually belongs after the event has actually happened.
- If the condition says "used", "discarded", "damaged", "lost HP", "entered the discard pile", or "became the target", check whether the wording needs the attempt, the confirmed event, or the completed result. Do not use an after-timing for an effect that must prevent the event.

Phase timing shorthand:

- 回合开始前 is mainly for skipping or replacing the turn before the normal turn line exists. 回合开始时 means the turn has started and start-of-turn cleanup or triggers may matter.
- 判定阶段开始时 belongs before delayed tricks resolve; 判定阶段结束时 belongs after their result.
- 摸牌阶段开始时 changes or replaces the draw; 摸牌阶段结束时 should care about the cards just drawn or set up a short next-step effect.
- 出牌阶段开始时 starts a phase route or phase-long effect; 出牌阶段结束时 summarizes what the player did during that phase.
- 弃牌阶段开始时 can change hand limit or spend cards that are likely to be discarded; 弃牌阶段结束时 should care about cards actually discarded.
- 结束阶段 and 回合结束时 are not interchangeable when cleanup matters. If the effect depends on "until end of turn" states, extra turns, or other players' end-turn triggers, explain the intended ordering or choose an earlier, cleaner timing.

Card-use timing shorthand:

- 使用牌时 follows the decision to use a card and its ordinary target choice; use it for effects tied to the card itself, not for most target changes.
- 指定目标时 is mainly the user's active window for adding, reducing, or changing targets.
- 成为目标时 is mainly the target's defensive window for avoiding, redirecting, or responding to being chosen.
- 指定目标后/成为目标后 means the target relation is more settled; use these for effects that care who was actually pointed at, but not for basic target editing.
- 生效前 is the window for validity checks, cancellation, or no-effect decisions; 生效时 starts effect resolution; 生效后/结算后 should be used for aftermath that can tolerate the card having already resolved or failed.

Damage timing shorthand:

- 造成伤害前 is an exceptional early gate for changing whether the damage event starts at all; use it sparingly.
- If the skill prevents or reduces damage, put it at "造成伤害时" or "受到伤害时" as appropriate.
- "造成伤害时" belongs more naturally to the source side; "受到伤害时" belongs more naturally to the damaged side. Both are before the damage has become completed aftermath.
- Damage reduced to 0 is normally treated as prevented for downstream "after damage" purposes; do not trigger "受到伤害后" payoffs from fully prevented damage.
- If the skill needs actual lost HP regardless of cause, use HP reduction/loss timing instead of damage timing.
- Treat dying as a closed, high-risk event. Avoid adding broad card-use, draw, or target-changing insertion inside dying unless the entire design is built around that risk.
- Use 进入濒死状态时 for effects that happen before the main rescue process and may fail; use 处于濒死状态时 for rescue-window effects; use 脱离濒死状态时 only for small cleanup or follow-up, because the causing event may still be resolving.

Ordering caution: if a design only works because multiple same-timing skills resolve in a precise order, it is probably too fragile for ordinary custom-general design. Prefer visible prerequisites, current-turn history, or after-resolution text.

Same-timing caution: official/server ordering can differ. When the design needs same-timing resolution, make the dependency visible in the skill's own condition or result instead of relying on hidden priority. As a tabletop baseline, same-owner timing often follows武将技能 before card skills before game rules, and different characters' same-timing skills resolve from the current turn player by seat order, often described as逆时针; if that order changes the design's balance, rewrite the timing.

## Effect Role Map

Translate anchors into game roles before writing exact text. The same mechanical effect may change role by timing, so judge by what the player actually gains at that moment.

- Attack: extra attacks, direct damage, damage increase, response restriction, range/distance compression. Good anchors include martial force, ambush, decisive strike, ranged pressure, revenge, and successful harsh schemes.
- Defense: sell-blood payoff, recovery, extra HP-like buffers, damage prevention/reduction, distance increase, hiding or retreat. Defensive text should still create choices, especially for sell-blood designs.
- Burst: drawing, card access, multiple uses, temporary card economy, or reward after victory. Use as a balance knob carefully; "just draw more" can patch strength but may weaken character identity.
- Control: discard, theft, target/phase/use restriction, hand information pressure, imprisonment, intimidation, or political suppression. Cost aggressive control because it removes others' agency.
- Support: third-person versions of the above roles, such as helping allies attack, defend, draw, recover, move cards, or complete plans. Avoid pure ally-only support if the user wants duel space.
- Neutral/negative: failed schemes, bad temperament, betrayal, isolation, arrogance, or self-harm. Negative effects work best when they constrain the exact strong line rather than randomly punishing play.
- Special: broad invention spaces such as unusual talents, literature, craftsmanship, mysticism, or package-centerpiece gimmicks. Use only one unusual axis at a time unless the brief asks for complexity.

Design flow: collect deeds and scenes, propose several possible roles, choose one primary role plus at most one secondary role, then expand that role into structure. After the first draft, remove anchors that only made the skill longer.

## Simplicity

Prefer one resource axis per general: card type, source zone, damage state, chained state, equipment movement, or virtual use. Avoid combining several axes unless the user requests a complex design.

Use no marks unless a visible game object cannot carry the memory. If memory is needed, prefer existing history such as "本回合", "本阶段", used-card history, damaged event, current zone, current state, or an actual card placed somewhere visible.

Keep triggers easy to remember. If a skill has more than two "若" clauses, split it or remove one branch.

Text efficiency matters. Strong designs often become shorter over iteration. After drafting, ask what each clause makes the player feel or decide. Delete clauses that only explain the authorial metaphor.

Avoid dynamic text mutation, many ending states, or self-rewriting structures unless the user explicitly wants a high-complexity design. They create reread cost and memory burden.

If using an unusual concept, make the rest of the skill plain. A new mechanic plus a long branching text usually overdraws the player's attention budget.

## Tabletop Feasibility

Default to face-to-face tabletop feasibility unless the user explicitly asks for an online-only, app-only, boss, or mode design.

Avoid effects that require repeatedly searching random qualifying cards from the deck, revealing through half the deck, opaque system-only checks, side mini-games, or heavy skill-text rewriting. If a physical token, public card, current-turn history, judgment, or small visible pile cannot represent the memory, the design probably needs simplification.

Cross-turn memory should be visible and low-volume. Prefer "本回合/本阶段", cards on the general card, current chained/flipped/equipment state, or a small public history over remembering which hidden condition happened several turns ago.

Be conservative with delayed-trick and equipment conversion. Delayed tricks share one judgment area and have ordering concerns; equipment can be moved, replaced, or exchanged by other skills. If the goal is only "borrow the feel" of an equipment or delayed trick, write a direct effect instead of making a card physically become that card.

Avoid nesting high-risk insertions inside dying, HP-change, or current card-use resolution. If a design wants a dramatic interrupt, prefer recording a pending effect and resolving it after the current resolution, or narrow it to prevention/cancellation before the dangerous event fully starts.

## Linkage Patterns

Use internal linkage with restraint. Linkage is a bonus, not a requirement; character fit and readable play come first. Do not make every skill serve the same engine unless the character is explicitly an engine-style centerpiece.

- produce -> consume: one skill stores or generates a resource, another spends it;
- hub -> spoke: a locked or passive skill rewards reaching a particular balance point;
- relay: one event creates the next event, preferably through a visible card movement or state;
- open node: a self-linking node also interacts with other players, preventing solitaire;
- conflict: skills can constrain or consume each other to tell a fall, collapse, or self-harm story.

Use these linkage shapes deliberately:

- Linear trigger: skill A finishes or creates a normal event, then skill B can trigger afterward. This is usually the cleanest visible link.
- Insertion trigger: skill B fires in the middle of skill A's resolution, then returns to A. Use sparingly; it feels tight but can create timing knots, especially around dying, HP change, moving equipment, or current card-use resolution.
- Split design: two skills are parts of one complete engine. Use only when splitting improves readability, separates historical anchors, or prevents a single skill from becoming too long. If both halves are incomprehensible alone, add a short explanation or simplify.
- Support link: one skill raises the probability, resource supply, or output ceiling of another without sharing a timing window. This often feels natural and avoids insertion problems.
- Implicit link: both skills are complete alone but become better through play pattern, such as one skill helping the user empty hand for another. This is elegant but should not hide the basic line from first-time players.
- Mutual exclusion: one skill makes another harder to trigger or asks the player to choose between routes. Use for contradiction, burden, or character tragedy; avoid accidental self-sabotage.
- No-link compensation: a second skill may simply cover defense, survivability, or table presence for a focused first skill. This is acceptable when it solves a real play problem rather than pretending to be synergy.

Use a loose relationship scale instead of forcing a combo:

- Strong linkage: one skill directly produces the resource/event another skill spends. Use when the character fantasy is a coherent engine.
- Soft linkage: one skill improves timing, probability, target quality, or hand shape for another. Prefer this for most ordinary generals.
- Division of labor: skills cover different table needs such as offense plus defense, support plus duel agency, or engine plus breakpoint. This is not a failure of linkage.
- Thematic resonance: skills share a character thesis, image, or failure mode without mechanical dependency. Keep this when mechanical linkage would feel contrived.
- Intentional independence: a skill exists to prevent non-games, reduce passivity, or express a separate anchor. Explain the role instead of inventing a fake trigger connection.

Do not assume all skills must be harmonious. A negative or self-consuming link can be more faithful than a smooth value loop.

When a family/identity skill refreshes or reopens skills, attach a soft cost, compensation, or source restriction so the engine has rhythm instead of repeated free action.

Do not stack too many linkage shapes in one 3-4 skill general. Mixed linkage can become attractive on paper but hard to learn at the table. If the player needs to trace several cross-skill arrows before taking a normal turn, reduce one link or make the default line explicit in the design explanation.

Anti-rigidity check: after drafting, ask whether a skill became worse only to trigger another skill, whether a cost exists only to feed an engine, or whether the design would read cleaner if two skills simply handled different jobs. If yes, loosen the link and preserve the cleaner skill.

## Clan And Family Design

Treat a宗族技 as a family design language, not as a generic extra skill. Work through these layers:

1. Family commonality: identify the shared historical/cultural axis of the clan.
2. Individual orientation: decide how this character embodies, bends, rejects, or is crushed by that axis.
3. Mechanical branch: choose one source zone, timing, card class, resource axis, or state that matches the individual orientation.
4. Clan linkage: check whether the new skill can interact with existing family members without becoming a free loop.
5. Naming layer: use skill names, titles, battle achievements, and quotes to carry cultural specificity that would overload skill text.

Do not make every member use every branch of the clan language. A good clan skill should feel consistent across the family while each general's other skills choose a narrower route.

Examples from the referenced门阀士族 notes:

- 颍川荀氏: the core is "见用之节". Distinguish being employed, not being employed, and dying for principle. A skill can turn on the tension between usefulness and integrity, not simply on loyalty.
- 陈留吴氏: the visible family commonality is hand limit. Individual designs can vary by changing hand limit, drawing/discarding to it, or using it as the family support axis.
- 族韩氏: naming and battle achievements can use围棋 language. The family flavor leans toward responding to urgent positions, rescuing key points, and converting board pressure into timely movement. Existing or neighboring skills that gain cards in the Play phase are important linkage candidates.
- 族钟氏: use layered wordplay and historical cross-links. A name can carry several senses at once, such as harm, planning, instruction, and jealousy. Do not reduce the design to one anecdote if the figure's appeal is in accumulated cleverness and hidden relation.
- 太原王氏: see the dedicated `中流` section below. First decide whether the figure is砥柱, 击水, or 遇风波, then select the matching language.

For clan designs, compare with any existing family members the user provides or names. Check family-internal loops, but also look for intentionally resonant external links, such as shared timing, shared card names, or historical counterparts.

If external constraints dominate the design so much that the game expression becomes weak, do not compensate by adding ornamental cultural references inside the skill text. Either simplify the requirement, move culture into title/voice lines/explanation, or choose a clearer mechanical branch.

## 太原王氏: 中流

Use `中流` by selecting one orientation from the character's life, not by using every source:

- 装备区: "中流砥柱", for figures defined by公辅、三公、社稷支撑、器任担当.
- 本回合弃牌堆: "中流击水", for figures defined by乱世行动、战功、事功、主动入局.
- 虚拟牌: "中流却遇风波", for figures defined by事变、失利、危局、凭空生波, or talent/desire that turns into backlash.

After choosing the orientation, make the personal skills use the same design language. For example, do not choose equipment merely because the character is luxurious; equipment in this clan means砥柱, not expensive objects.

## Locked Skills

Choose the locked-skill type before writing the text:

- 性: innate temperament, deep personality, emotion, mission, or worldview. Use for compulsions the character cannot help.
- 名: external title, reputation, label, or judgment from others. Use when the skill represents status imposed by society or posterity.
- 象: objective phenomenon or object-development rule. Use when the skill owner is more like a vessel for an event, artifact, omen, or natural law.
- 局: responsibility and environmental pressure. Use when outside circumstances force the behavior and the character often has no clean escape.
- 命: destiny, obsession, or personal fate that cannot be exceeded. Use when the character has choices locally but is doomed structurally.

Locked skills are technical labels for compulsory skills. Use them only when the whole skill must execute; do not mark a skill locked merely because one clause is always on, and do not rely on "no 可" alone if the skill should visibly be compulsory.

Locked skills can reduce prompts, force preplanning, and express inevitability. They are useful for negative effects and constraints, not only for bonuses, but they do not mean "negative effect" by themselves.

Do not make a locked drawback random punishment. It should tax the exact route that the active skill tempts the player to overuse.

## Support With Solo Play

Support skills should still work in duel through:

- choosing self vs enemy as target;
- using opponent's zone as cost or source;
- converting card types;
- timing around damage, discard, or equipment movement;
- accepting a locked drawback for a stronger short-term play.

Avoid pure ally-only engines unless the character is explicitly not meant for solo.

## Balancing Valves

Use these before adding hard usage limits:

- require a matching card type or color;
- compensate the affected target;
- force a discard after the generated card resolves;
- make virtual cards cost health or maximum health;
- make the strongest line expose the user to damage, loss, or tempo;
- narrow the valid card names to non-delayed tricks, basic cards, or non-healing cards.

For survival concerns, restrict【桃】and【酒】by excluding them from generated names, making them require an actual same-type card, or attaching a locked post-resolution cost.

Soft limits are often better than hard limits, but they must remain legible. Good soft limits include hand pressure, target compensation, stage timing, source zones, card-type matching, and losing access to a future line.

Avoid global listeners that reward other characters for paying their own costs at equal or greater value with no limit. They can create endless loops and restrict all future design space.

When changing a draft to remove marks, check whether the removed mark carried memory, storage, or prediction. If so, replace that function with visible cards, current-zone state, or a simple timing window rather than pretending the cost disappeared.

## Role Shape And Breakpoints

Do not make a design good at everything merely to show every historical anchor. A general should have one clear superior lane and one clear weaker lane; avoiding total power creep is about specialization, not making every effect mediocre.

Every strong design needs a visible breakpoint that ordinary opponents can pressure without relying on one specific counter-general. Examples include low defense after burst, hand pressure after using the engine, exposure after choosing an aggressive line, or reliance on a target/state/card class that opponents can disrupt.

Avoid both oppressive "no opening" engines and passive not-moving designs. A sell-blood or defensive general should still create decisions through active self-risk, ally incentives, enemy pressure windows, or timing choices; otherwise it becomes either a blank role or a table-stalling fortress.

## Play Experience

Pay attention to what the player actually does:

- A support general should create meaningful offers, rescues, or routes for others, not only distribute resources.
- A heavy engine should have a clear default line for first-time players and deeper timing/card-choice branches for experts.
- "Gamble" can add depth under low text complexity when the target user wants easy reading but repeated play value.
- A character can be designed for multiple modes, but do not flatten the identity merely to make every mode equally strong.

If a strategy is hidden, name it in the design explanation. If the player must reread the skill several times to find the basic line, reduce complexity.

## Wording Checks

Before final output, scan the visible skill text for unresolved placeholders. Never output empty or placeholder card brackets such as `【】`, `【 】`, `【牌名】`, or `【某牌】`. Fill the exact official/new card name, or rewrite the effect with an unbracketed category such as "一张基本牌" or "一张普通锦囊牌".

Check whether each clause can fail. If the latter clause must require the former success, use "并". If the latter can happen after partial execution, use "然后".

Use stable operation pairs:

- "获得/弃": marks;
- "摸/弃置": ordinary game cards from deck/hand/area;
- "置于...上/移去": real cards placed on a character or general card as marker cards;
- "回复/扣减": HP;
- "加/减": maximum HP;
- "获得/失去": skills.

State exact ownership/source when it matters:

- "来自其手牌" for hand-origin logic;
- "装备区里的牌" for equipment-zone logic;
- "本回合进入弃牌堆的牌" for discard-pile logic;
- "视为使用" for virtual cards.

When a skill uses another character's card, decide whether the owner, source, or user receives compensation.

For "视为使用" and source-zone mechanics, separate the virtual card from its base card. Ask:

- where did the real card come from?
- who is the user of the resulting card?
- does the card enter the discard pile, return to equipment, stay on the general card, or get removed?
- does the owner need compensation?

Prefer clear timing words over vague urgency. Avoid obsolete or fuzzy phrasing such as "每当" and "立即" in final skill text. Use "时/后" deliberately: "时" normally belongs before the main event resolves, while "后" belongs after that event's main effect has completed.
