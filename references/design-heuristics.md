# Design Heuristics For 三国杀 Generals

These notes condense recurring design ideas from the referenced Bilibili design essays. Use them as heuristics, not as canon text to quote at length.

Sources used for this reference:

- https://www.bilibili.com/opus/1107326926420181009
- https://www.bilibili.com/opus/825088145580097537
- https://www.bilibili.com/opus/745737843276513317
- https://www.bilibili.com/opus/693405298689310759
- https://www.bilibili.com/opus/674737966604615718

## Contents

- `Design Origin`: choose the design发端 before drafting.
- `Anchors`: translate character facts, temperament, and failure modes into rules.
- `Simplicity`: keep the resource axis, memory, and trigger burden low.
- `Linkage Patterns`: build produce/consume, hub/spoke, relay, open-node, or conflict links.
- `Clan And Family Design` and `太原王氏: 中流`: choose family language by individual orientation.
- `Locked Skills`: use locked labels for true compulsory structure and choose the lock type.
- `Support With Solo Play`: keep assist designs playable in duel.
- `Balancing Valves`: tune power through costs, targets, card classes, and source zones before hard limits.
- `Play Experience`: check what the player actually does.
- `Wording Checks`: verify "并/然后", source ownership, and virtual-card flow.

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

## Simplicity

Prefer one resource axis per general: card type, source zone, damage state, chained state, equipment movement, or virtual use. Avoid combining several axes unless the user requests a complex design.

Use no marks unless a visible game object cannot carry the memory. If memory is needed, prefer existing history such as "本回合", "本阶段", used-card history, damaged event, current zone, current state, or an actual card placed somewhere visible.

Keep triggers easy to remember. If a skill has more than two "若" clauses, split it or remove one branch.

Text efficiency matters. Strong designs often become shorter over iteration. After drafting, ask what each clause makes the player feel or decide. Delete clauses that only explain the authorial metaphor.

Avoid dynamic text mutation, many ending states, or self-rewriting structures unless the user explicitly wants a high-complexity design. They create reread cost and memory burden.

If using an unusual concept, make the rest of the skill plain. A new mechanic plus a long branching text usually overdraws the player's attention budget.

## Linkage Patterns

Use internal linkage with restraint:

- produce -> consume: one skill stores or generates a resource, another spends it;
- hub -> spoke: a locked or passive skill rewards reaching a particular balance point;
- relay: one event creates the next event, preferably through a visible card movement or state;
- open node: a self-linking node also interacts with other players, preventing solitaire;
- conflict: skills can constrain or consume each other to tell a fall, collapse, or self-harm story.

Do not assume all skills must be harmonious. A negative or self-consuming link can be more faithful than a smooth value loop.

When a family/identity skill refreshes or reopens skills, attach a soft cost, compensation, or source restriction so the engine has rhythm instead of repeated free action.

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
