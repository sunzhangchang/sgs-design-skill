# Value Glossary For Design

Use this reference when a skill calculates or assigns points, HP, maximum HP, hand limit, damage value, distance, attack range, X, differences, extrema, counts, or halves. It summarizes the reviewed 三国杀官方规则集 3.0 value glossary for design use.

## Card Points

Card points run from A to K:

- A = 1;
- number cards equal their printed number;
- J = 11, Q = 12, K = 13.

A point value above K is treated as K; one below A is treated as A. When a virtual card combines or derives points from multiple physical cards, define the calculation and then apply the legal 1-13 boundary. Do not leave “点数之和” uncapped if the result is used as a card's point value.

## HP, HP Value, And Maximum HP

Maximum HP is the character's upper HP bound. When maximum HP is reduced below current HP, adjust current HP down to the new maximum.

Distinguish actual HP from HP value:

- actual HP can fall below 0 during damage and dying resolution;
- HP value is the visible/countable value used as a game parameter and is 0 when actual HP is 0 or lower.

This distinction matters when one effect deals several damage, another checks “体力值”, and dying or recovery triggers resolve before the original event has fully ended. Do not assume a character at -2 HP has a体力值 of -2.

Lost HP value equals maximum HP minus HP value. Under this definition, negative actual HP does not enlarge lost HP beyond the maximum-HP-to-zero gap.

Design checks for maximum-HP changes:

- reducing maximum HP may immediately adjust current HP and therefore create another HP change inside the resolution;
- increasing maximum HP does not by itself state that HP is recovered;
- if a skill tests full HP, empty HP, lost HP, or HP equality after changing maximum HP, specify the intended timing and guard against insertion loops;
- if maximum HP can become 0 or a special lower bound exists, read the HP/dying mechanism reference in addition to this glossary.

## Hand Limit

A character's default hand limit equals their HP value and is normally applied during the discard phase. Modified hand limit has a minimum of 0.

Do not treat hand limit as a continuous requirement to discard outside the discard phase unless the skill explicitly creates such a procedure. A hand-limit reduction may have no immediate card effect if the discard phase has passed or will be skipped.

When a design sets or modifies hand limit, check:

- whether it applies only during the discard phase or is also used by another skill as a parameter;
- whether additions/subtractions stack;
- whether the intended minimum is already protected by the general minimum of 0;
- whether “hand cards greater than hand limit” is checked before or after another simultaneous modifier.

## Damage Value Base

In “造成/受到X点伤害”, X is the damage value base before applicable modifiers finish determining the damage event.

When designing damage increase, reduction, prevention, replacement, or source changes, distinguish:

- the written/base damage value;
- later modifiers;
- the final damage actually dealt;
- HP lost after that damage.

Do not use an after-damage trigger to modify the base of damage that has already resolved.

## Distance

Base distance between two different living characters is the shorter seat path clockwise or counterclockwise. Dead characters no longer participate in this calculation, so their neighbors become closer.

Distance is directional after modifiers: distance from A to B can differ from distance from B to A. A character's distance to self is always 0; distance between different characters has a minimum of 1.

For distance-based skills:

- write “你至其的距离” or “其至你的距离” when direction can matter;
- recalculate after death or seat-changing effects before using the result in a later event;
- do not reduce distance between different characters below 1 unless a special rules framework explicitly permits it;
- distinguish changing distance from changing attack range.

## Attack Range

A character without a weapon has attack range 1. With a weapon, their attack range uses the weapon's printed range, subject to other modifiers.

B is in A's attack range when A's attack range is at least the distance from A to B. Infinite attack range includes every other character.

Attack range and distance are related but not interchangeable. A skill that says “无距离限制”, “攻击范围内”, “攻击范围+1”, or “距离-1” can affect different cards and legality checks. Verify which parameter the intended play actually needs.

## Variables And Assignment

X is a natural-number variable and may equal 0. Unless a minimum is explicitly required, do not silently rewrite X as at least 1 or forbid a zero-card/zero-cost legal choice.

Define X before it is used and specify its duration when it can change. If several clauses recalculate X, say whether each uses the original value or the current value.

The phrases “a parameter is N” and “a parameter is treated as N” differ:

- “为N” assigns a value that may still receive other modifiers;
- “视为N” fixes the final treated value at N regardless of other modifiers.

Use “视为” only when overriding all ordinary modifiers is intended. It is a strong rules operation, especially for distance, range, hand limit, damage, and card points.

## Difference, Extrema, Counts, And Halves

- The difference between two values is the absolute value of their subtraction.
- Global counts ignore dead characters unless a specific rule says otherwise.
- Multiple characters may tie for maximum/minimum numerical value; each qualifies as maximum/minimum.
- Multiple characters may tie for having the most/least of an object; each qualifies.
- If every character has none of an object, there is no character who has the most of that object under the reviewed rule.
- “Game player count” means the number of players who participated at game start, not the number currently alive.
- Half of an odd number rounds down by default.

Do not replace “数值最大” with “某事物最多” casually. The zero-state rule can make their candidate sets differ. When a skill needs exactly one winner, add a tie-breaking or no-result rule instead of assuming maxima are unique.

## Design Checklist

Before finalizing a value-based skill, verify:

- card points remain within A-K after calculation;
- actual HP, HP value, maximum HP, and lost HP are not conflated;
- maximum-HP reduction accounts for immediate HP adjustment;
- hand-limit changes are evaluated at the intended timing;
- base damage and final damage are distinguished;
- distance direction, living seats, minimum 1, and self-distance 0 are respected;
- attack range is not used as a synonym for distance;
- X may be 0 unless explicitly bounded;
- “为” versus “视为” matches modifiable versus final assignment;
- ties, all-zero object counts, initial player count, and floor division are handled.
