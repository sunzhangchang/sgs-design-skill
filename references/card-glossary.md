# Game Card Glossary For Design

Use this reference when a skill changes card category, manipulates equipment slots, uses equipment as another card or as a cost, depends on equipment-provided distance/range/skills, distinguishes delayed from non-delayed tricks, or refers to printed general-card skills versus currently owned skills. It summarizes the reviewed 三国杀官方规则集 3.0 card glossary for design use.

## Non-Game Card Objects

Identity cards and general cards are game components but are not ordinary shared game cards.

- an identity card represents a player's identity and objective; except for the lord, it remains hidden from other characters until revealed because of death under the reviewed identity rules;
- a general card represents the controlled character and carries faction, maximum HP, skills, gender, and other printed attributes.

“A general card's skills” means the skills printed in that card's designated skill boxes, not every skill the current character happens to possess. Losing a currently owned skill does not erase the printed skill from the general card as a reference object. When a design declares, copies, gains, seals, or queries skills, distinguish these scopes explicitly:

- printed skills on a named general card;
- skills the character currently possesses;
- skills gained from another source;
- skills already lost or invalidated.

Do not move or reveal identity/general cards as ordinary game cards unless the design deliberately invokes a non-game-card mechanism and defines visibility, ownership, attributes, movement, and return handling.

## Game Card Categories

Game cards are the shared cards used during play. Every game card has a suit and point number and belongs to one of three top-level categories:

- basic card;
- trick card;
- equipment card.

Do not treat a subtype as a top-level category. Weapon, armor, mount, treasure, delayed trick, and non-delayed trick are narrower classifications under equipment or trick cards.

Basic cards carry their name, illustration, suit, and point and normally provide the game's simplest direct functions. Do not infer that every basic card is usable in every timing; card-specific rules and use/response conditions still apply.

Trick cards divide into:

- delayed trick cards, marked by the delayed/sandglass symbol;
- non-delayed trick cards, without that symbol.

When a skill says “锦囊牌”, it includes both unless the text or rules narrow the category. Under this reviewed glossary, use the exact term “非延时类锦囊牌” when delayed tricks should be excluded. Use “普通锦囊牌” only if the target rules environment defines it equivalently; do not assume the two terms are universally interchangeable.

## Equipment Subtypes And Slots

Equipment cards divide into weapon, armor, mount, and treasure cards. The ordinary equipment area has separate positions for:

- one weapon;
- one armor;
- one【-1坐骑】;
- one【+1坐骑】;
- one treasure.

Different named mounts may occupy the same plus/minus mount position. A character cannot normally keep two cards in the same equipment position.

When a character uses an equipment card while the corresponding position is occupied, the new card enters that position and the old equipment moves through the processing area into the discard pile. A design that cares about replacing, losing, moving, or discarding equipment must distinguish these events instead of treating “装备新牌” as if the old card simply vanished.

Using an equipment card normally targets its user. If a skill makes another character use an equipment card, moves an equipment card directly, or changes its destination, state whether normal target and replacement handling still apply.

## Equipment Use Versus Equipment Operation

An equipment card cannot provide the same distance, attack range, or equipment skill that is being relied upon while that card is simultaneously used as another card, discarded as a skill cost, or otherwise operated on.

Design checks:

- if an equipped weapon or mount is used as the physical card for a conversion, do not count its range/distance to make that converted use legal;
- if a card use has already passed its legality check, later discarding a range-modifying mount does not retroactively invalidate that card use unless a specific rule says otherwise;
- if an equipment card's skill, distance, or range is currently being used to perform an effect, do not also choose that same card as the cost or object of that effect;
- after equipment leaves its area, its equipment skill is no longer available for later events merely caused by the earlier card use.

These are dependency rules, not only wording preferences. For every equipment-as-cost or equipment-as-card design, identify which equipment property is needed at legality check, target selection, resolution, and aftermath.

## Stacking And Interaction

Equipment-skill effects and same-kind effects from general skills may stack unless a specific rule limits them. When a custom skill adds distance, range, target count, or another modifier, do not silently assume an equipment modifier is replaced.

If stacking would produce an unintended breakpoint, write an explicit cap, non-stacking condition, or narrower scope. Avoid vague wording such as “改为” when the intended result is actually additive, and avoid additive wording when the design needs to replace the existing value.

## Design Checklist

Before finalizing a card-category or equipment skill, verify:

- top-level category versus subtype is named correctly;
- delayed tricks are included or excluded intentionally;
- the equipment position and replacement route are clear;
- “使用装备牌”, “置入装备区”, “移动装备牌”, “弃置装备牌”, and “将装备牌当其他牌使用” are not treated as equivalent operations;
- the same equipment is not both supplying a needed property and being operated on at that moment;
- distance, range, target-count, and skill effects account for stacking;
- virtual or transformed equipment has a defined slot, conflict rule, and leaving behavior.
