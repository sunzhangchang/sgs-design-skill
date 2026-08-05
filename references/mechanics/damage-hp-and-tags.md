# Damage HP And Tag Concepts

This file is a focused slice split from `../mechanics-and-special-cards.md`. Read it only when the index routes here for the current design need.

## Damage, Tags, And Skill Encapsulation Concepts



Use these concepts when splitting existing concepts into subtypes or turning a recurring operation into a compact tag.



### 属性伤害



- Definition: damage has an attribute variable, usually fire or thunder, while ordinary damage remains available.

- Use when: the attribute has meaningful support in cards, skills, or defenses, not merely decorative flavor.

- Priority: high as a model concept; normal in new designs because too much attribute support can warp the environment.

- Guardrails: preserve ordinary damage as a useful baseline. Give each attribute a distinct job and enough but not excessive support. Avoid adding a new attribute unless it has repeated interactions and a clean rule identity.

- Design test: if the only difference is one skill line, use direct wording such as "此伤害+1" or "此伤害不能被防止" instead of defining a new damage type.



### 特殊属性伤害 / 视为造成过伤害



- Definition: a damage subtype carries an extra optional or compulsory rider, or a partial "as if damage happened" event is recorded.

- Use when: the design needs a rare signature damage identity or a controlled fake-damage puzzle that mostly serves the user's own skills.

- Priority: low. It is expressive but narrow and easy to over-combo.

- Guardrails: state whether transmitted/chain damage carries the rider. Do not let fake damage freely trigger broad sell-blood or damage-record skills unless that is the whole design and has a cost.

- Avoid when: the rider helps the damaged player more than it hurts, or when the design depends on other characters' skills to matter.



### 额外牌面信息 / 应变标签



- Definition: a card carries an extra tag or condition, such as a special Slash tag, Yingbian-like condition, or strengthened state.

- Use when: the tag is medium-frequency, easy to check, and gives a card family a recognizable tactical identity.

- Priority: medium.

- Guardrails: define whether transformed/virtual cards may gain the tagged version, whether the tag changes card name/category, and whether the effect is compulsory. Conditions should be achievable but not automatic; extreme conditions are better for comeback cards than universal card vocabulary.

- Avoid when: the tag becomes a pile of unrelated bonuses or requires players to remember invisible card text.



### 技能封装 / 卜算 / 附魔



- Definition: a known skill operation is packaged as a keyword or attached to a card as a temporary callable ability.

- Use when: every player already knows the operation and the keyword greatly shortens repeated text.

- Priority: low to medium. Good encapsulation saves words; bad encapsulation makes rules feel like private jargon.

- Guardrails: define which version of the source skill is being invoked, what parameters mean, and which hidden clauses are included or excluded. Encapsulation should follow ordinary reading order; avoid phrases that require players to mentally expand several skills at once.

- Avoid when: the original skill has context-sensitive side effects, optional follow-ups, or a famous version mismatch.



## HP, Armor, And Dying Concepts



Use these when health presentation itself is the play object. Do not use extra HP, armor, or shattered-gem language merely as balance knobs.



### 残血开局 / 护甲 / 护盾 / 虚血



- Definition: a character starts below max HP, gains a damage buffer, gains a stronger shield-like buffer, or has temporary HP above normal max that cannot be restored once lost.

- Use when: the character is protected by outside power, visibly exhausted, outwardly strong but fragile, or defined by spending max HP/health state.

- Priority: medium for flavorful 残血开局 and simple 护甲; low for many armor variants on ordinary generals.

- Guardrails: explain why the abnormal HP exists in the character, then make skills care about it. Distinguish whether the buffer prevents damage only, HP loss too, whether it affects hand size, and whether it has a cap. Avoid using armor as generic "the design is weak/strong" patching, and be careful with survival-card access because extra buffer plus【桃】【酒】can make a character too hard to finish.



### 体力牌操作 / 勾玉颜色



- Definition: HP cards or gems are shattered, repaired, split, merged, flipped, recolored, or otherwise treated as physical components.

- Use when: the visual operation is central to the fantasy, such as heartbreak, damaged vitality, divided body, unusual awakening, or health-ratio state.

- Priority: low. It is mostly presentation and carries physical/UI edge cases.

- Guardrails: define the exact visible representation, initial state, whether several HP cards can overlap, and what happens if the required card shape is unavailable. If color only represents health ratio, a direct HP/max-HP condition is often clearer. Use these as artful aids for one visible axis, not as a second marker system layered on top of several marks.



### 体力下限 / 额外濒死结算



- Definition: change the HP threshold for entering dying, or force an extra dying-like procedure outside the normal threshold.

- Use when: the character is harder or easier to keep alive in a way max HP cannot express, such as stubborn survival, slow doom, false death, or a vow tied to near-death.

- Priority: low; death-threshold rules are high-stakes and timing-heavy.

- Guardrails: state the threshold, how it interacts with max HP, immediate death, recovery, and leaving dying. Extra dying checks should not let full-health characters convert【桃】 into a pure benefit, nor should they create hidden lethal inserts. Prefer max-HP loss, HP loss, or "when entering dying" riders unless the threshold itself is the point.
