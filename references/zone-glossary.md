# Zone Glossary For Design

Use this reference when a skill names a zone, operates another character's cards, depends on ownership, moves cards among hand/equipment/judgment/processing/draw/discard areas, handles a judgment card, or checks “场上”. It summarizes the reviewed 三国杀官方规则集 3.0 zone glossary for design use.

## Core Zones

A zone is a place where cards are located. Keep location, visibility, ownership, and legal operation separate.

- Draw pile: remaining shared game cards after opening hands; cards are face down.
- Discard pile: cards that finish operations such as use, play, or discard generally collect here; cards are face up.
- Processing area: the face-up area in which most game cards are processed. Cards there are not owned by any character.
- Hand area: a character's face-down hand cards. The owner can see their own hand.
- Equipment area: a character's face-up equipment cards in five positions: weapon, armor,【+1坐骑】,【-1坐骑】, and treasure.
- Judgment area: face-up delayed-trick objects attached to a character.

“场上” means all characters' equipment and judgment areas. It does not include hands, draw pile, discard pile, processing area, or cards placed on general cards unless a specific mechanism expands the term.

A character's areas are their hand, equipment, and judgment areas. Being in a character's area does not by itself mean the character owns that card.

## Ownership And “A Character's Cards”

A character owns:

- their hand cards;
- cards in their equipment area.

Cards in a character's judgment area are not owned by that character or by any other character. Cards in the processing area are likewise unowned.

Do not casually use “其区域内的牌”, “其牌”, and “其拥有的牌” as equivalents:

- ordinary operations on “a character's cards” generally mean cards the character owns: hand plus equipment;
- a card currently serving as that character's judgment card is a separate rules object and may be included by wording that changes or views the character's card information;
- cards already placed in the character's judgment area are neither owned cards nor automatically that character's judgment card.

When the intended scope includes judgment-area cards, say so directly, such as “其装备区或判定区里的一张牌” or “其区域内的一张牌”, and verify that the operation legally supports both zones.

Outside required game procedures, a character cannot operate cards they do not own unless a skill or card effect explicitly grants that operation. A card used or played into the processing area cannot be reused merely because the original user once owned it.

## Visibility And Choice

- Draw-pile and hand cards are normally face down; discard, processing, equipment, and judgment-area cards are face up.
- When a character discards their own hand card, they choose from their hand.
- When a character discards another character's hidden hand card, the selected card is random unless the effect first reveals, views, or otherwise grants a legal choice.

The same distinction applies to display/reveal designs: the hand owner may choose their own card when instructed, while another character normally cannot deliberately select an unseen card. Do not write “选择其一张手牌” for an opponent unless the effect gives viewing information or the target chooses.

## Draw-Pile Refill And Exhaustion

When an operation needs X cards from the draw pile:

- if draw-pile cards plus discard-pile cards are fewer than X, the reviewed rules end the game as a draw;
- if the draw pile has between 1 and X-1 cards and the combined total is at least X, randomize the entire discard pile and put it at the bottom of the draw pile before the operation;
- if the draw pile is empty and the discard pile has at least X cards, randomize the entire discard pile into a new draw pile;
- if the draw pile already has at least X cards, do not refill merely because the discard pile is nonempty.

For large draw, reveal, view-top, search, or arrange-top effects, define X before the pile operation. Avoid wording whose X changes while cards are being taken, because refill and draw-ending behavior become unclear.

## Judgment-Area Rules

A character's judgment area cannot contain more than one card of the same delayed-trick identity. Check the delayed-trick identity represented in that area, not only the physical printed card name.

Under the reviewed glossary:

- a diamond card in a judgment area is treated as【乐不思蜀】;
- a black basic or black equipment card in a judgment area is treated as【兵粮寸断】.

A physical equipment card placed in a judgment area as a delayed trick is not therefore equipment in the equipment area. Effects that operate equipment on the table, move delayed tricks, or check card categories must use the card's current rules identity and zone rather than its illustration or original intended slot.

When moving a judgment-area card, verify that the destination can legally contain its represented delayed trick and does not already contain the same name. Do not move it into an equipment position merely because its physical card was originally an equipment card.

## Design Checklist

Before finalizing a zone-based skill, verify:

- exact source and destination zones;
- face-up/face-down status and who may choose the card;
- whether the card currently has an owner;
- whether the operation is use, play, discard, obtain, move, place, or processing;
- whether “场上” is intended to mean equipment plus judgment areas only;
- whether judgment card and judgment-area card are being distinguished;
- legality and duplicate-name handling in the judgment area;
- what happens when the draw/discard piles cannot supply X cards;
- whether cards in the processing area may be referenced at that timing and where they go afterward.
