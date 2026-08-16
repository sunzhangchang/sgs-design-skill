# Event, Response, And Resolution Glossary For Design

Use this reference when a skill responds to a card, skill, damage, target, equipment, or other event; inserts an effect into an ongoing resolution; makes something invalid, ignored, counteracted, or canceled; or changes the scope of a card/skill effect.

## Core Terms

- An **event** is the complete set of related resolution processes created when a character uses or plays a card, activates a skill, or enters a relevant state.
- A **response** is an event that affects another event. A response may be inserted while the original event is resolving.
- **Resolution** is the process of handling one event. When an inserted event occurs, the current resolution pauses and the inserted event resolves first.
- A **timing** is an instant produced by an event. Put the trigger on the event line before deciding whether the skill acts before, during, or after the relevant operation.
- An **idle timing** is a point where no card, skill, response, or inserted event currently occupies the flow and an ordinary active action may be initiated. A phase can remain active while its idle timing is temporarily unavailable because another event or response window is resolving.
- An **effect** is the concrete change produced by a card or skill text. Do not use “effect” as a substitute for the event that contains it.

## Idle Timing Versus Frequency

Keep activation timing separate from usage frequency:

- "出牌阶段限一次" normally carries the ordinary active-use meaning of once at an idle timing of the owner's Play phase, although the concrete card or skill rule still controls exceptional cases.
- "每回合限一次" and "每轮限一次" only cap frequency within a turn or round. They do not themselves say that the skill uses an idle timing; read the trigger, response permission, or active-use text to find the actual timing.
- An inserted resolution or 【无懈可击】 response window does not become idle merely because it occurs during the owner's Play phase. A skill restricted to ordinary Play-phase idle use cannot be inserted there without a separate legal timing.

For every limited-use skill, identify both fields:

```text
频次范围：阶段 / 回合 / 轮 / 每名角色 / 其他
发动时机：空闲时间点 / 明示事件时机 / 响应窗口 / 静态持续
```

## Four Different Interruptions

Keep these operations distinct in skill text:

- **无效**: a card is invalid to one target, so that target's resolution ends; the target was still legally chosen and the card still counts as used. A non-state skill that is invalid cannot activate; a state-like skill that is invalid cannot produce its influence.
- **无视**: a character ignores a specified condition or defense only within the defined scope of that character's card, skill, or damage resolution. The ignored defense still exists and can affect inserted events caused by other characters.
- **抵消**: during a card's resolution against one target, the card is counteracted and does not take effect for that target. This is not the same as removing the target from the card.
- **取消目标**: in the card-use process, remove one character from the card's targets. Other targets continue; if it was the only target, the card-use process ends.

When a draft says “此牌无效”“无视防具”“抵消此牌” or “取消目标”, verify which object is being changed: the target's resolution, a condition/defense check, the card's effect on that target, or the target list itself.

## Scope Of Ignoring

“无视距离” can remove the distance check for selecting a legal target and can remove distance restrictions on the stated skill use. “无视防具” applies only within the stated user's card/skill resolution or damage from that source; an inserted card or skill event from another character is not automatically covered.

Do not silently remove the underlying object. A character ignoring a defense does not mean the defense has been abolished, discarded, or lost its other triggers. If the effect should persist after the source loses the equipment or skill, write the end point independently of continued possession when the rules environment requires it.

## Design Checks

Before finalizing an event-sensitive skill, write a short event card:

```text
当前事件：使用牌 / 打出牌 / 发动技能 / 伤害 / 牌移动 / 其他
当前结算位置：
响应事件：
插入后是否继续原结算：
被改变的对象：目标 / 效果 / 条件 / 目标列表 / 技能状态
作用范围与结束点：
```

Then verify:

- an inserted event pauses the original resolution and can create further inserted events;
- a target made invalid is still a target, while a canceled target is removed;
- counteracting a card against a target does not automatically cancel that target or the card's other targets;
- ignoring distance or defense has a defined actor, event scope, and duration;
- a source losing a skill, equipment, or life does not accidentally end an already-created effect unless the wording says so;
- damage, target, response, and later resolution are not treated as one undifferentiated event.
