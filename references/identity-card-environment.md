# Identity Mode Card Environment

Use this reference when a design depends on normal identity-mode deck composition, exact card names, colors/suits, equipment density, initial hand size, death rewards, or deck exhaustion. It is a baseline for the standard plus 军争 identity deck described by the cited rules source, not a promise that every server or room uses the same deck.

## Baseline Deck

The reviewed identity deck contains 162 game cards:

- 85 basic cards: 30 normal【杀】, 5 fire【杀】, 9 thunder【杀】, 24【闪】, 12【桃】, and 5【酒】;
- 50 trick cards: 43 non-delayed tricks and 7 delayed tricks;
- 27 equipment cards: 13 weapons, 6 armors, 7 mounts, and 1 treasure.

Non-delayed trick counts:

- 6【过河拆桥】, 5【顺手牵羊】, 3【决斗】, 2【借刀杀人】;
- 4【无中生有】, 7【无懈可击】, 6【铁索连环】, 3【火攻】;
- 1【万箭齐发】, 3【南蛮入侵】, 1【桃园结义】, 2【五谷丰登】.

Delayed trick counts:

- 2【闪电】, 3【乐不思蜀】, 2【兵粮寸断】.

The suits are nearly even overall: 40 spades, 40 clubs, 40 hearts, and 42 diamonds. Colors are also nearly even: 80 black and 82 red. Category-level color is not even:

- basic cards are 34 black and 51 red because all【闪】and【桃】are red, while most normal/elemental【杀】are black;
- trick cards are 30 black and 20 red;
- equipment cards are 16 black and 11 red.

Do not infer category probability from the whole-deck red/black balance. A skill that asks for a red basic card, black trick card, red【杀】, or black equipment has very different practical access.

## Design Implications

- Exact-name access must respect copy count. A singleton or two-copy card is a narrow anchor; broad repeated search, creation, or recursion makes that scarcity meaningless.
-【杀】has 44 copies and is the dominant basic card. Designs that listen to every use, response, discard, or conversion of【杀】need stronger rhythm control than designs tied to rare names.
-【桃】and【酒】have 17 combined copies and carry survival/rescue pressure beyond ordinary card value. Virtual creation, duplication, repeated recycling, and unrestricted naming of them require explicit restriction or an exact compensating cost.
- Equipment is only 27/162 of the deck, and treasure is a singleton. Equipment-zone engines need a setup route, another useful state, or tolerance for games where the required subtype does not appear.
- Delayed tricks are only 7/162. Do not make a normal general depend on naturally drawing a particular delayed trick unless the skill supplies a bounded route or still functions without it.
- Seven【无懈可击】make trick interaction a real table layer. When a skill creates, copies, redirects, or terminates trick resolution, define whether ordinary【无懈可击】interaction remains relevant.
- The near-even suit totals make whole-deck suit comparison broadly stable, but named cards and card categories have skewed suits. Check the actual category before using a suit as a soft limit.

## Identity-Mode Card Flow

The reviewed identity-mode summary provides these card-related baseline rules:

- each character normally starts with four hand cards, dealt from the lord in seat order;
- when a character dies, they reveal identity and discard all cards in their areas;
- the character who kills a rebel draws three cards;
- if the lord kills a loyalist, the lord discards all current cards;
- if an operation requires X cards from the draw pile but the draw pile plus discard pile contain fewer than X cards, that rules summary ends the game as a draw.

These rules matter when designing kill rewards, death triggers, source reassignment, mass discard, discard-pile reuse, deck search, and high-volume draw:

- changing damage source or kill credit can redirect the rebel reward or lord penalty, so define responsibility and timing explicitly;
- a death-trigger skill must account for the dead character's area cards being discarded and must not rely on an unspecified order to reclaim them;
- large search/reveal/draw operations can pressure the finite deck and must state what happens when fewer cards are available;
- opening-hand effects should be judged against a four-card baseline rather than as free abstract resources.

## Scope Cautions

- Treat these counts as the reviewed standard plus 军争 identity environment. Recheck counts when the user specifies another server, package list, mode, or custom deck.
- Card counts describe availability, not guaranteed draw frequency in one game. Avoid exact probability claims unless the active deck and removed cards are known.
- Use this file for card ecology and card-related identity rules. Do not infer faction balance, identity strategy, victory conditions, or selection rules from it.
