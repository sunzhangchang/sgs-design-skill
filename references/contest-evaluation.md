# Contest Design Evaluation

Use this reference when reviewing contest submissions, absorbing judge feedback, or evaluating a draft at contest-level strictness. Contest samples are aesthetic and practical evidence, not rules authority; `rules-priority.md` and the foundational glossaries remain higher priority.

## Read The Whole Sample

Treat the entire sample as context:

- contest/round and the stated design requirement;
- the introductory historical biography or character brief;
- character, title, HP/maximum HP, and skill count;
- skill text and design explanation;
- the three judge scores and comments after the `【字数】` field.

The opening file-format explanation is a parsing instruction, not a requirement for the new design. Do not transfer a sample's HP, skill count, or historical character to a new task unless the user explicitly carries it over.

Separate each sample into:

```text
命题约束：比赛要求、体力、技能数、指定人物
人物语境：简介、生平、关键事迹、性格与失败点
设计实现：技能文本、称号、设计思路
评委证据：三位评委的分数与具体意见
可复用结论：能迁移到其他武将的评价标准
```

Do not average scores blindly. First identify what each judge is measuring: formal structure, actual play, or theme/table practicality. A disagreement is useful evidence about a risk boundary, not automatically an error by one judge.

## Evaluation Rubric

Evaluate in this order, after rules legality:

1. **命题与人物映射**: Does the skill use the biography's actual deed, temperament, relationship, or failure mode? Is the title and design explanation consistent with the mechanism? A clever template without a character connection is a serious deduction.
2. **玩家欲望与主循环**: What does the player want to do each turn? Does the skill create a reason to build, maintain, spend, or risk its resource? If the metaphor is construction or accumulation, continued construction should be attractive rather than rewarding only one-time setup or immediate liquidation.
3. **反馈方向与资源趋势**: Do costs and rewards move in the same narrative direction? Construction, equipment, marks, cards, or stored objects should not accidentally shrink when the fiction says the structure is growing unless the reversal is deliberate.
4. **最优解与反直觉玩法**: Find the strongest low-effort line first. Check free repeated use, defensive-card abuse, high-value trick cards, setup-before-draw bypasses, avoiding the skill entirely, or forcing opponents/allies to choose a negative option. If the rational player should ignore the central action, the fantasy has failed.
5. **结构与操作负担**: Count distinct choices, branches, state changes, searches, and remembered objects. A compact skill with a few meaningful options is preferable to a long list of loosely related options. More than four parallel options needs a strong structural reason; five or more is presumptively a consolidation candidate.
6. **互动与角色定位**: A support/buff skill should create decisions for its user, allies, and enemies. Check meaningful enemy response, unconditional team resources, and whether solo play retains target, timing, card, or risk choices.
7. **面杀可执行性**: Can players verify “本回合/本轮失去过的牌”, remembered categories, hidden information, repeated searches, and multi-step allocation without software? If not, define a visible zone/object or simplify the memory requirement.
8. **规则与结算表达**: Check operation verbs, event timing, target legality, source/channel attribution, and clause executability using the foundational rule files.

## General Decomposition Model

For a new sample, trace the design through this chain instead of jumping from “像不像人物” to “强不强”：

```text
人物事实/命题
  -> 人物锚点（能力、行为、关系、性格、失败点）
  -> 设计隐喻（想让哪一种行动代表这个锚点）
  -> 机制翻译（牌、区域、数值、状态、时机、资源）
  -> 玩家主循环（玩家每次如何启动、维持、转化、收束）
  -> 反馈与代价（收益方向、风险、失败方式、对手回应）
  -> 结算实现（规则合法性、插入、记忆、面杀可验证性）
```

At every arrow, ask whether information was lost or distorted:

- **人物事实 → 锚点**：是否从真实人物提炼出可操作的事实，而不是只取一个名词或典故？
- **锚点 → 隐喻**：玩家做的动作是否真的表现该事实，还是只在技能名/设计思路中解释？
- **隐喻 → 机制**：机制是否保留了隐喻的方向、节奏和代价？“建设”不应默认变成一次性放牌，“精算”不应默认变成无目标摸牌。
- **机制 → 主循环**：玩家理性上是否愿意执行设计者希望的动作？对照“不发动技能”和“直接摸牌/直接用牌”的基线。
- **主循环 → 反馈**：收益是否鼓励下一步正确动作？是否出现先设置再绕过、存牌后只为喂另一技、或负面效果迫使玩家放弃主玩法？
- **反馈 → 结算**：实际触发次数、资源数量、动态比较、信息记忆和插入顺序能否被规则与面杀环境承载？

If a link breaks, name the broken link. Do not vaguely label the whole design “不够贴合” or “强度有问题”.

## Problem Attribution

Classify a finding by its first broken layer; later symptoms may be consequences:

| Finding | First layer to inspect | Typical symptom |
| --- | --- | --- |
| 史料只出现在称号或说明 | 人物事实 → 锚点 | 换一个人物也能使用同一技能 |
| 技能名能解释，玩家动作不能解释 | 锚点 → 隐喻 | 主题“套皮”、典故没有转化为决策 |
| 资源增长方向与故事相反 | 隐喻 → 机制 | “筑坝”越用越少、“传承”只消耗存量 |
| 主技能可被直接摸牌或不开技能替代 | 机制 → 主循环 | 控制效果装饰化、最优解规避核心技能 |
| 选项很多但没有不同价值 | 主循环内部 | 选项堆叠、BUFF机器、操作繁琐 |
| 第二技只为第一技提供原料 | 技能关系 | 人工联动、单技能价值不足 |
| 限制写了但实际收益仍爆炸 | 反馈与代价 | “每回合限三次”仍高产、启动资金越多越强 |
| 实战有趣但面杀无法确认 | 结算实现 | 失去过的牌、动态最多、牌堆标记无法追踪 |
| 结算顺序改变技能是否触发 | 结算实现 | 插入自循环、触发次数不确定、时机点错误 |

## Layered Rating

Use words before numbers. For each layer, assign one of these statuses and cite evidence:

- **成立**：原型、玩法和结算互相支持，主要问题只需调参数。
- **有条件成立**：核心想法成立，但依赖特定牌序、启动手牌、玩家自限或复杂记忆；需要明确阀门。
- **局部成立**：某个技能或局部体验优秀，但主循环、技能关系或人物映射有明显断点。
- **表面成立**：名称和说明能解释，实际玩家行为不按设计意图运行。
- **不成立**：规则、最优解或人物命题直接否定了设计目标。

Suggested review record:

```text
人物层：成立 / 有条件成立 / 局部成立 / 表面成立 / 不成立；证据：
玩法层：成立 / 有条件成立 / 局部成立 / 表面成立 / 不成立；证据：
反馈层：成立 / 有条件成立 / 局部成立 / 表面成立 / 不成立；证据：
互动层：成立 / 有条件成立 / 局部成立 / 表面成立 / 不成立；证据：
实现层：成立 / 有条件成立 / 局部成立 / 表面成立 / 不成立；证据：
首要修复层：
```

Only convert these statuses to a numeric score after explaining the evidence. A high score in one layer cannot erase a failure in a more fundamental layer: illegal/ambiguous resolution first, then player loop, then character expression, then polish and novelty.

## Sample 1 Lessons

The `康绚` submission required “4 HP, 1 skill”, so compression and one recognizable construction metaphor were part of the challenge. The samples show:

- A visible-card “dam” with repeated virtual use had a clear object, but arbitrary high-value cards and equipment-as-card handling created power and rules risks. The player could stop building and exploit existing stock, so the construction fantasy did not create continued desire.
- A conversion skill linked the dam to equipment, but spending equipment made the structure shrink. Its branches were weakly linked and one mode could be bypassed by acting before drawing. Resource direction, branch necessity, and timing bypass must be checked separately.
- A seven-option public effect was cumbersome, grouped repeated draw/discard/transverse/damage effects, and could make the best line be never activating the skill. Universal ally/enemy access does not create interaction by itself; without structure it becomes a buff machine with negative options.
- An extra-turn design scored best because its positive feedback and “天意难违” restriction created a continuing reason to use the mechanism and connected to the character story. Its remaining risks were tabletop tracking of “cards lost last turn”, retrieval/search burden, and the need for a visible auditable memory method.

Transferable conclusion: preserve the character's central action, make the intended action rationally attractive, align resource movement with the metaphor, and make memory/operation costs visible at the table. Do not copy a sample's exact mechanism merely because it scored well.

## Sample 2 Lessons

The `祖暅` requirement was “3 HP, 2 skills”, with biography anchors including astronomy, precise instruments, mathematical calculation, the “祖暅原理”, and the failed water attack. These samples add several checks:

- A top-deck control skill must offer a reason to control rather than simply draw. If the player usually prefers to take the card immediately, the control clause is decorative or creates a bad choice. Test the value of prediction/control against the default draw line at every legal timing.
- A visible-card system embedded in the draw pile can be thematically close to calculation, but repeated marking, swapping, and checking pile ends creates large tabletop and long-game memory costs. A visible zone or direct top/bottom operation is usually easier to audit than persistent marks in the deck.
- A trigger based on “the number of face-up cards in the pile changes” can immediately cause another skill that moves those cards, creating insertion or self-chain risk. Test whether the second skill can trigger the first again before the original resolution finishes.
- “最多”“相同”“牌最多的角色”“两端均有”等 dynamic conditions need tie handling and a precise time snapshot. A skill that checks a changing hand count at the wrong point can generate unintended repeated growth or ambiguity.
- Reassembling familiar templates can be mechanically solid but still score poorly for novelty and character fit. A mathematical theme needs the mechanism to express the actual mathematical idea, not only attach names such as “幂算” or “圆”. Conversely, a water-related effect should be supported by the character's historical role, not merely by a visually similar event.
- Repeated limited-use conversions and “展示若干牌后取最接近组合” can produce high output with startup resources. Check whether the restriction limits power in practice, whether the selected result is too flexible, and whether later top-deck control makes the search effectively deterministic.
- A secondary skill should have its own reason to exist. If it only stores a card so the main skill can get a better draw, or only adds raw draw to compensate for a weak prediction effect, the skills are feeding each other artificially rather than forming a meaningful division of labor.

Transferable conclusion: distinguish control from draw, distinguish visible information from persistent bookkeeping, audit insertion loops and snapshots, and require every named mathematical or historical motif to appear in the actual player decisions.

## Evidence Chain: Prototype To Judgment

Do not write a criterion without an evidence chain. For each useful lesson, record:

```text
人物原型：这段生平/设定要表现什么
具体设计：技能实际让玩家做什么
设计思路：作者认为这个动作如何对应原型
评委反馈：评委在实战、结构、主题或规则上观察到什么
评价结论：以后检查什么，不应机械复制什么
```

### 康绚：浮山堰与筑堰命题

- **〖砺堰〗**：原型是主持浮山堰、逐步修筑且最终因失去维护而崩溃；设计用不同点数的明置手牌表示堰体，准备阶段持续加牌，每回合视为使用一张，未增加则全部弃置；作者思路是“建造—利用—加固—坍塌”。评委实际发现，高价值锦囊和防御牌可以长期白嫖，装备当牌还有规则风险；玩家更愿意一次性亮出可用牌而非持续筑坝。结论是：有实体隐喻不等于主循环成立，必须测试玩家是否真的愿意继续建设，以及虚拟使用覆盖的牌类是否改变强度。
- **〖戍堰〗**：原型同时包含筑堰与抗敌；设计用转换技的摸牌/花色限制代表修堰，用弃置装备使伤害加减代表防御；作者把装备视为堰体。评委指出，先用牌再摸牌可规避限制，两个转换分支联系弱，而且弃装备让“堰”越用越少。结论是：设计思路中的资源必须与技能实际的增长/消耗方向一致，并检查阶段边界是否能绕过限制。
- **〖堰分〗**：原型只在设计思路中写“千里之堤，溃于蚁穴”，技能却做成全场可执行的七项摸牌、弃牌、横置和雷电伤害；没有具体的康绚事迹映射。评委认为选项堆叠、操作繁琐、最优解是不开技能，且最后的终止条款把技能锁成负面或纯BUFF机器。结论是：选项数量、人物关联和主循环必须同时成立；“所有人都能执行”不自动等于互动。
- **〖违天〗**：原型是浮山堰违背自然规律、后来崩溃，也可承接康绚预警未被采纳；设计为回合结束后额外回合，并用上回合失去过的牌替代判定牌但不能改【闪电】。评委认可额外回合形成了正反馈，“天意难违”也有故事对应，但指出“失去过的牌”面杀难追踪，涉及弃牌堆检索且需要明确维系区域。结论是：正反馈和故事限制都成立时可以支撑高强度机制，但记忆必须可见、可核验。

### 祖暅：数学、天文与水攻考察命题

- **〖定分〗/〖遗缀〗**：原型包括观测天文、牟合方盖、精密计算和“缀术”传承；设计按牌堆顶四张选花色并反复控制同花色牌，受伤/回复后以手牌交换牌堆底牌；作者将定分解释为球体分割、星体偏差或水坝预言，将第二技解释为知识续接。评委认可一技能自联动和二技能的战略意义，但发现同花色高价值锦囊可反复刷牌，卜算常不如直接摸牌，二技能像把关键牌存起来，且实际体验抽象繁琐、看不出牟合方盖或缀术。结论是：要分别比较“控制牌堆”和“直接摸牌”的实际收益，并检查设计思路中的核心名词是否真的改变玩家决策。
- **〖天度〗/〖断圆〗**：原型是持续研究天文、揣度天圆地方、通过交换与逐步揭示探索；设计在牌堆顶/底明置牌并交换，牌堆两端同类别时令角色使用一张并获得另一张。评委指出明置牌堆会造成长期桌面负担，第二技可能直接插入并反复触发第一技；也有人认为这是所有投稿中最接近“割圆”过程的方案，但交换牌不是最合适的实现。结论是：主题最贴合仍不能抵消插入自循环和实体操作成本；应优先用直接看顶/底、弃置错误端等更可审计的动作。
- **〖孜算〗/〖补缀〗**：原型是孜孜计算并传承知识、查漏补缺；设计把摸牌和弃牌改为卜算数量，并在大批量移动后让当前回合角色和自己各摸一张。评委的共同问题是卜算结果通常不如直接摸牌，控制没有实际目标，最后退化成摸牌堆叠；技能没有抓住有用典故。结论是：控制效果必须有明确的下注对象或风险收益，不能用更强的直接收益覆盖一个无意义的控制分支。
- **〖幂算〗/〖察水〗**：原型是祖暅原理、不断逼近圆周率，以及考察水攻的天时地利；设计以弃牌点数和匹配展示牌组合，另一技牌堆拼点后视为使用【水淹七军】并控制牌堆顶。评委认为一技能有启动资金时收益过高，二技能像拼接模板，水攻并非祖暅主动发起且史料对应不足。结论是：重复限制不一定真的限制强度；数学模板和水攻效果都必须经过人物史料筛选，而不是只靠名称相似。
- **〖学究〗/〖幂势〗**：原型是学者研究与“幂势既同则积不容异”；设计为重铸他人牌，以及在回合结束根据本回合获得牌最多者的手牌数量调整自己手牌。评委认为第一技像抢牌而不像祖暅，第二技监控对象过多，“最多”并列有歧义，且结算时间可能被利用出回合末爆发。结论是：动态比较必须固定时间快照并处理并列；若核心体验是数学等量，应让“相等”成为清晰的玩家决策而不是复杂监控。
- **〖精究〗/〖查涛〗**：原型可理解为不断缩小计算区间，以及考察水势；设计让一次弃置的两张牌确定点数区间供重铸，另一技让角色用两张牌当【水淹七军】。评委认为一技能有“缩小区间/一次大制衡”的精益求精意味，但二技能只是强行配合，三血身材又难以承担反复重铸；颜色分支还可能出现低交互或过强效果。结论是：主技能已经有明确玩法时，副技能应补足角色而不是硬喂主技能；反复资源操作要以实际生存能力和手牌留存测试。

These cases show why the evaluation rubric is not a generic popularity scale: the same “控制牌堆”“额外回合”“明置牌”机制 can be praised or criticized depending on whether it expresses the biography, creates the intended player desire, survives the strongest line, and remains auditable in the stated format.

## Contest Review Format

Lead with findings rather than a single score:

```text
命题完成度：
人物语境使用：
主循环与玩家欲望：
资源趋势与正负反馈：
最优解/滥用线：
结构与操作负担：
互动性与单挑空间：
面杀可执行性：
规则与措辞风险：
```

Then distinguish致命问题、主要扣分项、可调问题和具体优点. When judges disagree, report the disagreement explicitly and test both readings: “结构上有意思但实战不清晰”, “主题贴合但玩法最优解反常”, and “玩法成立但人物不像” are distinct diagnoses.
