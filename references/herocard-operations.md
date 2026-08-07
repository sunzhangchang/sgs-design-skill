# General Card Operations For Design

Use this reference when a skill changes a character's transverse state, chain state, general-card face, or other state represented by the general card. It distills the reviewed 三国杀官方规则集 3.0 glossary; the page's embedded image is only a chain-state diagram and adds no independent rule beyond the text.

## Transverse State

- **横置** turns a character's upright general card sideways. **重置** turns a sideways general card upright.
- A character starts in the upright/reset state. Because the operations change a binary state, a skill that says “横置” must make sure the character is currently reset, and a skill that says “重置” must make sure the character is currently横置.
- “横置后再横置” is not two successful transverse operations unless the skill explicitly resets between them or defines a different state operation. Apply the workspace's existing transverse-state convention consistently.

## Chain State And Chain Damage

- A sideways general card means the character is in chain state; resetting removes that chain state.
- When a chained character receives attribute damage that is not itself chain damage, after that damage finishes, the character resets if alive and chain transmission is checked. If any other character remains chained, transmission proceeds from the current turn character in counterclockwise order, checking each character in sequence.
- Each transmitted damage keeps the original attribute, source, and channel, and uses the damage value of the triggering attribute damage. It is a new damage resolution and can be modified, transferred, or responded to separately.
- A character's reset and the decision to trigger chain transmission are checked against whether that character was chained before HP was reduced, not merely against the state after damage modifiers or later operations.
- A transferred damage can change the character that receives the damage, but it does not silently change the chain's original source, channel, attribute, or base value. Read `description-glossary.md` for transfer semantics.

When a skill references chain state, record:

```text
初始横置状态：
造成的伤害：普通 / 属性 / 连环传导
来源与渠道：
属性与伤害值基数：
伤害结束后的重置：
是否触发后续连环：
```

## Flipping The General Card

- **翻面** turns a character's face-up general card face down, or face-down general card face up. It is separate from横置/重置 and does not itself mean entering or leaving chain state.
- A design using face-up/face-down status must specify whether it changes the general card's side, a skill's availability, a character's identity information, or another custom state. Do not use “翻面” as an informal synonym for disabling a skill.

## Final State Check

Before finalizing a skill involving a general-card state, verify:

- the target is in the required state for横置,重置, or翻面;
- the operation can execute under the current state and the workspace's “并/然后” dependency convention;
- chain damage is distinguished from ordinary attribute damage and from transferred damage;
- source, channel, attribute, and damage-value inheritance are explicit where they affect the design;
- reset timing, chain transmission order, nested damage, and death during transmission do not create an accidental second trigger;
-翻面 has not been conflated with横置/重置, skill invalidity, or loss of identity information.
