# Skill Description Glossary For Design

Use this reference when finalizing technical labels, optional/mandatory wording, sequential versus simultaneous card operations, damage transfer, HP loss, user/source/channel attribution, recovery, option legality, role references, target references, or visibility. It summarizes the reviewed 三国杀官方规则集 3.0 skill-description glossary while preserving explicit workspace wording conventions.

## Technical Labels And Choice

- Locked skill: a technical label associated with compulsory behavior. A non-state locked effect triggers when it can; a state-like locked effect must apply when it can affect the game.
- Limited skill: can be activated at most once in one game.
- Awakening skill: compulsory at its valid timing and usable only once per game; it usually creates an irreversible state change and gains/loses skills.
- Lord skill: effective only while the character's identity is the lord.

Do not infer optionality from the label alone. In the reviewed glossary, “可以” grants the relevant character a choice. A skill without “可以” may be compulsory even without the printed “锁定技” label. Keep the workspace rule that an intentionally labeled locked skill should be compulsory as a whole; split or rewrite a half-optional locked draft.

“角色的技能” refers only to that character's general skills. Equipment skills are skills the character possesses, but are not included by that narrower phrase. When a design seals, counts, copies, or removes skills, state whether it means general skills, equipment skills, printed skills, or all currently possessed skills.

“任意数量” includes 0. If at least one object must be chosen, write “至少一张/一名” or another explicit lower bound.

## Mandatory And Response Wording

- “可以”: the character may decline the operation or effect.
- “须”: the character must execute the operation if able.
- “需”: the character has a choice about how to provide the required response.
- “需要使用牌”: includes using the card at its normal use timing and using it at a non-use timing created by another rule.

Do not use “须” to express a cost that may be declined. If the entire activation is optional but its selected branch is compulsory, put “可以” at activation and “须/令其” only inside the committed branch.

## Sequential And Simultaneous Operations

“依次…X张牌” means operate one card at a time. Finish all resolution caused by one card before immediately operating the next; there is no free timing window between them beyond events created by those operations.

Without “依次”, an operation on X cards is simultaneous:

- drawing X cards is one draw operation;
- gaining/losing X cards is one movement batch unless another rule separates them;
- discarding X cards as one cost cannot normally be interrupted after the first card to gain a replacement and continue paying;
- “依次使用X张牌” creates a complete use resolution for each card.

Use “依次” only when intermediate state changes should matter. Otherwise simultaneous handling is shorter and avoids extra triggers.

### Workspace Rule For “并/然后”

The reviewed glossary describes “然后” as ordering two non-delayed effects and “并” as simultaneous operations. This workspace has an explicit user-defined dependency convention that overrides that source during design:

- “并” is a gate: the preceding action must execute before the following action can execute;
- “然后” continues when the preceding part executed at least partly.

Therefore, do not import the source's broad simultaneity reading into generated skill text. When true simultaneity matters, describe the objects as one batch or state “同时” only if the target rules environment accepts it; when dependency matters, follow the workspace gate/continuation convention.

## Damage Transfer

Transferring A's incoming damage to B is not merely changing the damaged target in place:

1. prevent A's original damage and terminate that damage resolution;
2. reach the end of that damage resolution;
3. after it finishes, make B receive new damage with the same source, channel, attribute, and the damage value base that A faced before transfer.

The new damage resolves against B's current modifiers, armor, elemental vulnerabilities, chained state, and triggers. It may therefore deal a different final amount from the prevented damage.

Do not use “转移伤害” when the intended rule is only changing a target before damage exists, sharing damage, or changing the damage source. Those are different operations and timings.

## HP Loss, Damage, And Recovery

“扣减体力” is the umbrella result caused by either losing HP or receiving damage.

- Losing HP has no source and does not create a damage event. Death from HP loss does not assign kill rewards or penalties to a source.
- Receiving damage creates a damage event and may have a source, channel, attribute, and downstream damage triggers. Death from damage can create source-based rewards or penalties.

A character is wounded when HP value is below maximum HP and unwounded when they are equal. Recovery increases HP only up to maximum HP; an unwounded character cannot recover. “回复至Y点” stops at maximum HP if Y exceeds it.

When an option says to recover, check whether at least one affected character can legally recover. Do not treat an impossible recovery as having partly executed merely because the text was selected.

## User, Source, And Channel

- User: the character who uses a card.
- Damage source: the character who deals the damage.
- Channel: the card or skill whose effect causes the damage.

Changing one does not automatically change the others:

- changing a card's user makes later use resolution treat the new character as user; the reviewed rule may still record both old and new characters as having used that card;
- changing damage source does not change the card user;
- if the source has died by the time damage resolves, the damage is treated as sourceless;
- chained damage keeps the channel of the damage that triggered the chain;
- transferred damage keeps the original channel;
- unspecified damage is normal damage; attribute damage is fire or thunder damage;
- chain damage is attribute damage caused by chain transmission, or damage transferred from chain damage. Other attribute damage is not automatically chain damage.

For every damage-related draft, write an attribution card before final wording:

```text
使用者：
来源：
渠道：
属性：
是否连环伤害：
```

Expose only the distinctions that affect gameplay; keep the rest implicit.

## Option Legality

“选择一项” is itself an operation. A choice with all effects impossible cannot be selected.

Distinguish self-paid exact costs from effects imposed on another character:

- “弃置X张牌” as the chooser's own operation usually requires enough legally discardable cards when that branch is chosen;
- “令B弃置X张牌” may remain selectable when B has fewer than X but at least one eligible card, causing B to discard as many as can be executed under the reviewed effect logic;
- prohibitions on discarding particular cards affect whether the branch is executable, not only the final number discarded.

When several characters each choose an option, determine the eligible characters first, then resolve their choices in order. Later state changes do not automatically remove a character already selected for that operation unless the rule says to recheck.

For custom designs, prefer options with parallel readability and explicit feasibility. If an option is meant to remain selectable for partial execution, write that intent clearly rather than relying on obscure shortage behavior.

## Role And Target References

- “A令B…”: A issues the instruction; B performs the action. Costs, card movement, triggers, and attribution belong to the actual actor unless stated otherwise.
- “另一名角色”: a character distinct from the current referenced character, but may include the skill owner depending on sentence context.
- “其他角色”: excludes “you”, the card/skill user.
- “A对B使用【杀】”: B is the nominal target A must choose for that use.
- “目标角色”: during card-use resolution, the card's current resolution target. A recipient of transferred or chained damage is not automatically that card's target character.
- “以此法”: by the method described in this activation of the skill, not every similar event from another activation or source.

Avoid pronouns after target transfer, added targets, multiple sources, or nested instructions. Repeat the role name when two interpretations are plausible.

## Visibility

“可见/不可见” means whether the card may be viewed. It is independent of whether the physical card is face up or face down. A face-down object can be visible to one character, and a face-up placement rule does not by itself settle every information permission.

When a skill reveals, displays, views, hides, or privately shares a card, define who can view it and for how long. Do not use orientation alone as a substitute for visibility rules.

## Final Description Checklist

Before finalizing skill text, verify:

- standard operation verbs, technical labels, role references, and quantities are used consistently; define new wording instead of relying on an unstated local synonym;
- labels, “可以”, “须”, and “需” express the intended agency;
- “任意数量” intentionally permits 0;
- simultaneous versus “依次” operations have the intended trigger count;
- workspace “并/然后” semantics are followed;
- damage transfer creates a new damage event rather than silently retargeting the old one;
- HP loss, damage, and recovery legality are distinct;
- user, source, channel, attribute, and chain status are correct;
- every option has a defined legal/illegal state and shortage behavior;
- actor, other/another character, and target character are unambiguous;
- visibility is not inferred only from face orientation.
