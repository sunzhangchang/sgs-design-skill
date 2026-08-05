# Cards Zones And Movement Concepts

This file is a focused mechanics slice. Read it only when `../mechanics-index.md` routes here for the current design need.

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
