# Game Card Operations For Design

Use this reference when a skill moves, uses, plays, recasts, places, discards, gives, gains, loses, reveals, views, exchanges, judges with, or treats cards as other cards. It distills the reviewed 三国杀官方规则集 3.0 game-card operation glossary into wording and resolution checks.

## Movement And Core Operations

- **移动** changes a card's zone. Movement is the broad result; “弃置”“获得”“交给”“置入” identify different actors, destinations, and causes.
- **使用** makes a card or skill produce effects. A character can use only one card at a time; inserted responses and resolutions must be handled as events rather than simultaneous card uses by that character.
- **打出** means declare a card, move it into the processing area, then move it to the discard pile. Playing a card is not using it and does not automatically create that card's ordinary use effects.
- **重铸** at the play phase's free timing normally requires a card with a recast label: declare it, move it through the processing area to the discard pile, then draw one card. A skill-granted recast must state which cards and timing it authorizes.
- **置于/置入** moves a card directly to a destination. It is not automatically “使用”: placing equipment requires the matching empty slot, while placing a delayed trick into a legal judgment area starts a sourceless use resolution from the target timing under the reviewed rule.
- **扣置** is placement face down. **移出游戏** removes ownership; cards placed on/beside a general card are normally outside the game, and the skill should define their collective name and later handling.

Do not substitute “置入弃牌堆” for “弃置” when the discard actor, discard prohibition, processing-area route, or discard trigger matters.

## Discard, Give, Gain, And Lose

- “A令B弃置牌” means B performs the discard and chooses the card. “A弃置B的牌” means A performs it and chooses.
- When an effect makes a character discard X cards but that character has fewer than X eligible cards, they discard all available cards under the reviewed effect rule. This differs from paying an exact activation cost; check option legality in `description-glossary.md`.
- **交给A** moves cards not owned by A into A's hand. Giving several cards to several characters selects all recipients and the distribution first, gives each at least one, then moves the cards simultaneously.
- **获得** can mean the operation of moving a card into the actor's hand or the result that a card entered that hand. If choosing from another character's zones, choose the zone first; select randomly from a hidden hand and freely from visible equipment/judgment zones.
- A character **loses a card** only when a card they own moves outside their hand and equipment zones. Moving a hand card to equipment means losing a hand card but not losing a card; moving equipment to hand means losing an equipment-zone card but not losing a card.
- “失去过……牌” checks the card's information before it was lost. One batch movement normally counts as one loss event unless the cards are operated sequentially.

## Treating Cards As Other Cards

### 将牌当A牌操作

- The operated card has A's card name for that operation, but its original printed information does not change.
- Unless specifically named otherwise, “当【杀】” means normal【杀】 and “当【无懈可击】” means ordinary【无懈可击】.
- A single material card keeps its other card information. For multiple material cards: same color yields that color but no suit; otherwise the virtual card has no color or suit; points are the sum of the materials' points.
- Several materials used/played as one card count as one used/played card.
- If all materials come from one relevant zone, the virtual operation can count as operating a card from that zone; materials from different zones produce a virtual card that is not in any one zone. Check zone-dependent prohibitions and bonuses explicitly.

### 视为

- “视为使用/打出” creates a virtual card with no owner and no corresponding physical card, so it normally has no color, suit, or points.
- A virtual card copies only the referenced card name unless the rule or skill explicitly supplies additional information. Its effects follow the rules of that card name, but its color, suit, points, ownership, and material-card identity are not copied merely because a real card was used as the reference.
- Under the reviewed glossary, “视为使用【杀】” creates an ordinary colorless/suitless/pointless【杀】without distance restriction unless another rule specifies otherwise. Do not assume that every custom rules environment shares this special default without checking.
- “视为装备着” or “视为拥有技能” creates the stated status without putting a physical card in the zone. The virtual status can be used or affected as stated, but does not create a card that can be moved; a skill only deemed possessed cannot be lost as if physically acquired.
- “将B牌当A牌” and “视为使用A牌” are different: the first has material cards and preserves derived information; the second has no material card.

## Information Operations

- **观看** is private viewing without moving the card. Watching a character's hand means all of it unless narrowed.
- **展示** temporarily turns a face-down card face up, then normally turns it back. The card stays in its zone and remains owned; if a later clause in the same resolution must operate it, keep it identifiable until that operation finishes.
- **亮出** turns a card face up without the same return requirement. A card revealed from the top of the draw pile moves into the processing area.
- Do not use these words interchangeably. State who receives the information, whether the card moves, and whether it remains linked to a later effect.

## Other Operations

- **摸X张牌** gains the top X cards of the draw pile. “补至X张” draws only the positive difference and does nothing when the current count is already at least X.
- **代替** puts A into B's zone and moves B to the discard pile. **替换** puts A into B's zone and gives B to the replacing character.
- **交换** first moves both specified sets to the processing area, then moves each original set to the other side. Empty sets can still make the exchange execute under the reviewed rule.
- **判定** reveals the top card into the processing area, waits for it to take effect, uses its effective suit/points/name as the result, then moves it to the discard pile. The judgment card is not owned by the judging character.
- “A操作所有……牌” is not executed if there are no qualifying cards. This matters when a later “并” clause depends on successful execution.

## Final Operation Check

Before finalizing card-operation text, verify:

- the exact operation verb matches actor, destination, ownership, and trigger intent;
- “使用”“打出”“置入”“弃置”“置入弃牌堆” and “失去” are not treated as synonyms;
- material-based “当作” and material-free “视为” produce the intended color, suit, points, zone, ownership, and card count;
- a virtual card that references a real or face-up hand card copies only its card name unless additional copied information is explicitly stated, and the reference card is not accidentally consumed as material;
- hidden-card selection is random where required and private information is not leaked;
- displayed/viewed/revealed cards remain identifiable for later clauses without silently moving zones;
- batch versus sequential movement produces the intended number of gain/loss/discard triggers;
- equipment slots and delayed-trick legality are checked before direct placement;
- a later workspace “并” clause is blocked when an “operate all” instruction had no qualifying card and therefore did not execute.
