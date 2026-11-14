# Design And Evaluation Framework

Use this compact framework for every fresh design, review, or rebalance task. It is the shared spine between generation and evaluation: design with the same questions that will later judge the result. Read `rules-priority.md` first; legality always outranks this framework.

## Contents

- `Closed Loop`: the shared generation/review sequence.
- `Unified Working Sheet`: one state record across interactive turns.
- `Evaluation Order`: the canonical layers from legality to expression.
- `Stress Tests`: counterfactual, strongest-line, empty-line, and tabletop checks.
- `Diagnosis And Repair`: map the first broken layer to a targeted revision.
- `Rating Language`: evidence-first review labels.
- `Comparative Calibration`: use shared criteria and result evidence to compare designs without turning one contest into an absolute scale.
- `Routing After The Framework`: load only the next focused reference.

## Closed Loop

Work through these stages in order, but expose only the current stage during an interactive conversation.

1. **Brief gate**: fix mode, faction/HP if known, complexity, required and forbidden mechanics, support/solo expectations, and official-like versus experimental language.
2. **Character thesis**: select 1-3 concrete facts. Separate capability, behavior/relationship, and compulsion/failure. State one sentence about what the player should feel or repeatedly choose.
3. **Play thesis**: choose the primary player verb, resource direction, timing line, role, and opponent response. The player action must express the character without relying on the skill name or explanation.
4. **Skill skeleton**: give each skill an independent job and choose its relationship to the others. Use 2-4 skills by function; never pad to three.
5. **Rules construction**: resolve object, timing, frequency, agency/cost, sequence, attribution, target, duration, and cleanup through the focused foundational glossaries. Write the resulting rule-sensitive premises into the Unified Working Sheet, including the governing reference or explicit user convention.
6. **Consistency pass**: read each operative clause back against the recorded premises. Check that its objects, permissions, and consequences do not assume a contrary meaning merely to realize the desired effect. For a card outside an ordinary hand/equipment route, separately establish its location, owner if any, who may select it, and what text authorizes its use, play, movement, or transformation. An unknown premise is a rules failure until verified, explicitly adopted as a convention, or avoided by self-contained wording.
7. **Evaluation pass**: only after the consistency pass, test the same thesis against legality, player incentives, feedback, strongest line, interaction, burden, and character fit.
8. **Targeted revision**: repair the first broken layer, then rerun only the affected layer and every downstream layer. Do not rewrite a legal, functioning core merely to make all skills more tightly linked.

If an early layer changes, discard unsupported downstream choices. A polished skill text cannot rescue a broken play thesis.

## Unified Working Sheet

Use one sheet for both design and review:

```text
任务与硬约束：
人物事实：
人物命题：
玩家主动作：
主资源及方向：积累 / 消耗 / 转化 / 循环 / 无资源
主时机线：
主定位 / 副定位：
技能数量与各自工作：
技能关系：强联动 / 软支持 / 分工 / 张力 / 独立覆盖
对手回应与突破口：
规则命中：
规则前提与依据：
一致性核验：
首要风险：
当前阶段：
```

Do not fill unknown fields with invented certainty. Ask only about an unknown that would change the next stage.

## Evaluation Order

Evaluate in this order. Stop and repair a failed earlier layer before polishing a later one.

1. **规则成立**: every object, operation, timing, frequency, target, sequence, attribution, duration, and cleanup has a legal path. Separate phase/turn/round frequency from activation timing. Record the rule-sensitive premises actually used, then reject any operative clause that requires their opposite; location, ownership, visibility, and permission to operate a card are separate facts.
2. **人物成立**: the actual player action expresses a concrete deed, temperament, relationship, contradiction, or failure. Names and explanations are supporting evidence, not substitutes.
3. **主循环成立**: the player has a recognizable repeated decision. Compare it with not using the skill and with the simplest direct benefit such as drawing or dealing damage.
4. **反馈成立**: resource growth, spending, reward, and drawback point in the intended direction. The strongest reward should encourage the character's action rather than bypass it.
5. **结构成立**: every skill has work alone; its linkage, support, division of labor, tension, or independence is intentional. A skill must not be weakened only to feed another.
6. **互动成立**: allies receive meaningful choices, enemies have ordinary pressure points, and a support design retains solo decisions. Universal benefits or target count alone do not create interaction.
7. **强度成立**: test the strongest low-effort line, startup hand, repeated high-value names, survival cards, prevention, target denial, extra actions, and scaling with player count. Prefer visible breakpoints over arbitrary hard limits.
8. **载体成立**: memory, searches, hidden information, dynamic comparisons, inserted events, and generated objects remain auditable in face-to-face play unless the brief permits online-only handling.
9. **表达成立**: standard terms, type labels, timing words, agency, “并/然后”, card/object names, and sentence order accurately expose the resolution without ambiguous actors, permissions, or branches.

## Stress Tests

Run these before final wording:

1. **Remove the name**: without the skill name and design explanation, does the player behavior still resemble the character?
2. **Remove the largest reward**: is there still a meaningful decision, or is the mechanism decorative?
3. **Remove a linked skill**: does every remaining skill retain an independent job?
4. **Take the strongest line**: assume rational players repeatedly choose the best legal card, target, and timing. Does the intended drawback still matter?
5. **Take the empty line**: with low hand, no ally, no valid enemy target, or an awkward phase, does the general retain acceptable agency without gaining free compensation?
6. **Play it on a table**: can all players verify the state and reset point with visible cards, current-window history, or at most one simple marker?
7. **Read it backwards**: for each payoff, trace its required permission and object state back to the clause or foundational rule that supplies them. If the trace depends on an unstated or contrary premise, repair the rule layer before tuning balance.

## Diagnosis And Repair

Name the first broken layer and choose a matching repair:

| Symptom | First layer | Prefer repairing |
| --- | --- | --- |
| Resolution order changes whether the skill exists | Rules | timing, insertion point, dependency, cleanup |
| A later clause needs a rule premise opposite to the one used in construction | Rules | premise, authorization, zone/ownership distinction, or self-contained wording |
| Biography appears only in names or notes | Character | player verb, cost, target relationship, failure mode |
| Rational play ignores the core action | Main loop | reward location, default action, repeat incentive |
| “Construction” shrinks or “inheritance” only destroys | Feedback | resource direction and maintenance pressure |
| One skill exists only as fuel | Structure | independent job, soft support, division of labor |
| Support is blank in duel or automatic in teams | Interaction | self/enemy branch, target choice, opponent response |
| A written limit fails to contain output | Strength | source, card class, compensation, exposure, breakpoint |
| Players must remember hidden or long histories | Carrier | visible zone, current phase history, simpler snapshot |
| Text needs repeated rereading | Expression | fewer branches, stable verbs, split or remove a clause |

Revise the smallest layer that restores the thesis. Numeric tuning is appropriate only when the loop, structure, and legal implementation already work.

## Rating Language

Use evidence before scores:

- **成立**: the layer works; only parameter or polish changes remain.
- **有条件成立**: the core works under a clear dependency that needs a visible valve or clarification.
- **局部成立**: some play is good, but an important link or role is missing.
- **表面成立**: names or explanations fit, but actual play points elsewhere.
- **不成立**: rules, rational play, or the brief directly defeats the layer.

For reviews, report the first broken layer, concrete evidence, downstream symptoms, and the smallest useful repair. Give numeric scores only when the user or contest requires them, and never average away a rules failure.

## Comparative Calibration

比较多份设计或运用已吸收的结果集时，逐层使用同一组判断维度，再给整体结论。每层先记证据状态，不暗中折算成分数：

| 维度 | 较强证据 | 薄弱或缺失的证据 |
| --- | --- | --- |
| 规则与表达 | 操作均有合法、可追溯的路径，执行者、时机、成本和结束点明确。 | 关键条款依赖未写明的许可、相互矛盾的前提或未解决的分支。规则不成立属于门槛问题，不能靠其他项高分抵消。 |
| 人物契合 | 去掉技能名和设计说明，玩家实际做出的选择仍能表现具体人物锚点。 | 关联主要存在于名称或说明中，实际玩法却更像另一类人物。 |
| 主循环与选择 | 玩家有可重复且有意义的选择，至少在常见局面下优于普通替代行动。 | 理性路线是不开核心技能，或某一选项强到让表面上的选择失去意义。 |
| 反馈与强度 | 成本、收益和限制在最强重复路线下仍能推动预期玩法，并保留明确的失败点。 | 收益绕开预期行动、成本反转资源方向，或名义限制无法控制产出。 |
| 技能结构与互动 | 每项技能各有工作，联动提供支持而不强迫执行；其他角色仍有实际选择或反制空间。 | 技能只充当燃料、联动让技能组变脆，或把广泛影响误当作互动。 |
| 桌面执行 | 状态、历史、选择和清理方式可见且易于核验。 | 隐藏或长期记忆、检索、嵌套结算或反复改写状态，使玩家难以确认当前局面。 |
| 新意（仅在命题要求时） | 机制带来有意义的新选择或人物解释，同时保持清晰和契合。 | 只给熟悉模板换名，或新机制增加复杂度却没有改变有效玩法。 |

每层使用四档：**强项、成立、有条件、缺乏依据**。“强项”需要反复出现或特别直接的证据；“成立”表示常见边界下运作可靠；“有条件”表示仍依赖某项条件或有具体风险；“缺乏依据”表示文本、实战路线或来源材料尚不能支撑该判断。这是一组相对画像：一份设计可以人物契合为强项、桌面执行为有条件。除非用户要求打分，不把画像压成单一总评。

当吸收的来源含有评分或结果时：

1. 保留原评分维度、满分、权重、评委及评语。分数只说明该评委依照该量表作出的判断，不是规则或客观真值。
2. 只比较同一量表下的相同维度。量尺不同才按各自满分归一化；合并前先看每位评委的评分差异。不同量表的总分不可直接比较，规则硬伤也不能被其他项平均抵消。
3. 对照同一维度的高分稿与低分稿，把差异连到具体评语和可观察的玩法行为；分开记录评委原话与归纳出的可迁移标准。
4. 将可迁移标准写入本框架或对应设计选项，并纳入普通设计/评审路由。评分分布、具体投稿、命题限制和未决解释留在赛事资料中。
5. 标注基准所对应的样本范围和可信度。单一小型或主题赛事只能提示相对模式，不能建立普适门槛、因果结论或默认权重。除非用户要求，不把赛事评分权重套到普通评审。

没有可比较的评分集时，仍使用相同维度作定性判断，不自行编造数值校准。

## Routing After The Framework

- Open only the relevant sections of `design-heuristics.md` to generate or tune possible implementations.
- Open `contest-evaluation.md` only for contest requirements, sample parsing, judge disagreement, evidence extraction, or contest-style scoring.
- Open `mechanics-index.md` only when a named or unusual mechanism is actually under consideration.
- Open focused foundational glossaries whenever the skeleton touches their objects; these files decide legality.
