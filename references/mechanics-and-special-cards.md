# Mechanics And Special Cards Reference

Use this reference when designing a general that could borrow from existing 三国杀 cross-server mechanisms, special cards, special zones, extra decks, or equipment vocabulary.

Sources distilled into this file:

- 三国杀各服军争新机制与特殊牌汇总 document, revision records through 2025-04-21.
- User-reviewed package card/mechanism table from selected packages: 游戏模式、国战、军争、OL、SP、手杀、十周年、线下、国际服、江山如故、谋攻篇、蚀心入魔、通用机制 and related packages.

This file is self-contained. Do not assume any local codebase exists; package labels are preserved only so a user can include or exclude sources.

Do not import mechanisms wholesale by default. Choose one mechanism family that matches the character's play fantasy, simplify its wording, and add costs or constraints that fit the new general.

## Mechanism Priority Evaluation

Use this section only to judge whether a mechanism is worth choosing. It does not require writing every referenced mechanism into a new design.

First distinguish concept scale:

- 新概念: small expansion that improves text recognition or play texture without rewriting the game body, such as a concise operation, timing label, or shortcut term. Prefer this scale for ordinary generals.
- 新机制: structural rule update that changes core assumptions, zones, identity, slots, or table procedures. Use only when the character or mode genuinely needs the larger rule burden.

Classify the concept type:

- 创新型: gives a new operation or resolution route. Prioritize only if the action opens real decisions rather than novelty alone.
- 简化型: compresses repeated long text. Prioritize when the shortcut is intuitive and broadly reusable; reject over-compressed jargon that makes players decode more, not less.
- 技术型: has little standalone meaning but binds to another rule, such as compulsory execution or formation handling. Use when it clarifies timing or enforceability; avoid using it as decorative terminology.

Rank candidate mechanisms by three axes:

- 创新性: Does it add a distinct operation, decision, or expressive channel unavailable through simpler existing wording? "Official" or "new" does not by itself mean good.
- 泛用性: Does it match common character anchors, and can most players accept its effect on game experience? A one-character mini-game or a rule that deprives others of their core objective is low priority.
- 周全性: Does it coexist with existing rules, public resources, zones, and common edge cases? Watch for shared-resource congestion, hidden memory burden, unclear timing, and loops that are only "fixed" by banning pairings.

Priority guide:

- High priority: intuitive, reusable, low-conflict, and either genuinely expressive or a clear text saver. Use early when it fits the character.
- Medium priority: useful but context-sensitive, mode-tinted, or carrying some timing/zone burden. Use with explicit guardrails.
- Low priority: narrow mini-game, heavy structural rule, large public-resource footprint, unclear flow, or mostly official precedent without design necessity. Use only when the user's brief strongly points there.

For simplification mechanisms, prefer words that are both visible and self-explanatory. A short keyword is worse than full text if the player must already know several hidden definitions to understand the skill.

## Technical Labels

Use technical labels only when the called rule is clear and useful. They are not flavor words.

### 锁定技

- Role: a technical label binding the whole skill to compulsory execution.
- Use when: all clauses of the skill are mandatory, or the design wants to remove prompts and express unavoidable structure.
- Avoid when: only one clause is compulsory, the skill contains "你可以", or the label is being used merely to imply a drawback.
- Wording guardrail: no half-locked skills. If part A is optional and part B is compulsory, split them, make the whole skill compulsory, or remove the locked label.
- Priority: high泛用 but low周全 if used loosely; be stricter than casual official precedent.

### 阵法技 / 君主技 / 宗族技

- Role: technical labels that call external framework rules, identity display, or mode/package handling.
- Use when: the design environment recognizes the label and the character genuinely belongs to that framework.
- Avoid when: the label does not change readability, targeting, visibility, or family/mode interaction.
- 阵法技 has higher innovation when seat/formation is the actual play object, but lower generality and needs careful edge-case handling.
- 君主技 is narrow; use only for true lord-mode designs.
- 宗族技 is suitable for clan packages when the shared label helps players see family membership or inherit a common design language. The individual skill still needs to work as rules text even if the label is removed.

## Mechanism Selection

Use these patterns by design need:

- delayed payoff: 施法, 蓄谋, 历战, 使命技;
- risk/reward overreach: 背水, 妄行, 暴虐值, 奋武技;
- cooperation or table bargaining: 协力, 议事, 谋弈, 锻造, 同心;
- public or special zones: 仁区, 额外牌堆, 幻术牌堆, 蓄谋牌, 【影】;
- hidden or alternate identity: 隐匿, 结党, 休整, 异性双人武将, 双势力;
- resource counters: 护甲, 蓄力标记, 谋略值, 暴虐值, 耐久度;
- state/rhythm switching: 转换技, 韵律技, 连招技, 连招-like order checks;
- attack-position branches: 游击, 搏击, 摧坚, 击伤, 起义军;
- environment or global pressure: 天候, 光环效果, 持恒技;
- source/response puzzles: 智囊, 卜算, 六经, 妙计, 逐鹿.

## Reviewed Package Mechanism Families

Use these distilled package entries as normal design candidates when they match the character anchor. They are inspirations, not mandatory imports.

| Mechanism | Use For | Guardrails | Package Scope |
| --- | --- | --- | --- |
| 弃牌堆引用 | 残局余波、回收旧事、因弃置而起势；可看本回合弃牌堆、阶段弃置牌、特定牌进入弃牌堆后的回收。 | 限定时间窗、花色/类型、每阶段次数；避免无脑回收关键防御牌。 | OL、SP、一将成名、军争、十周年、十周年小程序、国战、国际服、小程序、手杀、江山如故、游戏模式、神话再临、线下、蚀心入魔、谋攻篇、通用机制 |
| 转化/虚拟牌/牌名声明 | 技艺、伪装、号令、临机借势；适合声明牌名、视为使用、把一类牌转为功能牌。 | 限制牌类、目标、时机和是否触发“使用”；谨慎产出【桃】【酒】等生存牌。 | OL、SP、一将成名、军争、十周年、十周年小程序、国战、国际服、小程序、手杀、江山如故、游戏模式、神话再临、线下、蚀心入魔、谋攻篇、通用机制 |
| 区域选牌/多区交互 | 搜检、调度、拆解装备/判定区/手牌的战术角色。 | 明确可选区域和每区最多数量；避免一次性跨区大拆。 | OL、SP、一将成名、军争、十周年、十周年小程序、国际服、小程序、手杀、江山如故、游戏模式、神话再临、线下、蚀心入魔、通用机制 |
| 拼点 | 争锋、试胆、较艺、权谋对赌；适合赢/没赢分支或拼点牌归属变化。 | 给没赢一方补偿或代价；避免纯粹高点数压制。 | OL、SP、一将成名、十周年、十周年小程序、国战、国际服、手杀、江山如故、游戏模式、神话再临、线下、蚀心入魔、谋攻篇、通用机制 |
| 横置/重置/连环 | 连环、牵制、阵型、火雷属性联动；可把横置作为状态门槛或结算资源。 | 遵守横置/重置可用性；不要让横置后的再横置变成空结算。 | OL、SP、一将成名、十周年、十周年小程序、国战、国际服、小程序、手杀、江山如故、游戏模式、神话再临、线下、蚀心入魔、谋攻篇 |
| 武将牌上/私有牌堆 | 记忆、藏物、积累证据、蓄势资源；适合少量命名牌堆。 | 定义进入、上限、离开、可见性、是否可被选取；普通武将少用多堆。 | OL、SP、一将成名、十周年、十周年小程序、国战、国际服、小程序、手杀、江山如故、游戏模式、神话再临、线下、蚀心入魔、通用机制 |
| 目标转移/取消/增减 | 护卫、误导、战术牵引、攻击面控制。 | 高强度语言；限制为特定牌、特定目标数或付出弃牌/失血成本。 | OL、SP、一将成名、十周年、十周年小程序、国战、国际服、小程序、手杀、江山如故、游戏模式、神话再临、线下、蚀心入魔、通用机制 |
| 体力上限/体力流失 | 欲望、代价、透支、不可逆成长/衰败；适合锁定负面或爆发成本。 | 体力上限变化要给恢复路径或明确终局压力；避免与强防御叠成不死。 | OL、SP、一将成名、十周年、十周年小程序、国战、国际服、小程序、手杀、游戏模式、神话再临、线下、蚀心入魔 |
| 获得衍生牌/印牌 | 召唤外物、仪式牌、身份信物、临时资源。 | 定义来源、数量、进入区域、离开规则；避免无限印关键牌。 | OL、一将成名、军争、十周年、国战、国际服、手杀、江山如故、游戏模式、神话再临、线下、通用机制 |
| 重铸 | 滤牌、拆解、换工具、把死牌变选择。 | 适合作为副效果或协作出口；多次重铸会增加操作负担。 | OL、一将成名、十周年、十周年小程序、国战、国际服、小程序、手杀、江山如故、游戏模式、神话再临、线下 |

## Mechanism Index

### 三国杀移动版

- 智囊: three ordinary trick names, commonly【无中生有】【过河拆桥】【无懈可击】. Use as a compact "tactical trick set".
- 使命技: has success/failure conditions and corresponding effects; becomes invalid after success or failure. Use for one-life vows, duties, or doomed quests.
- 仁区: a public card zone with a small cap. Use when a character contributes to or consumes a shared moral/political resource.
- 背水: a special option that executes other options, then pays a consequence; cannot be chosen if the consequence cannot execute. Use for all-in lines.
- 整肃: target chooses/executes a discipline task, then receives reward if not failed. Subtypes: 擂进 uses increasing point sequence; 变阵 uses same suit sequence; 鸣止 discards all different suits.
- 谋弈: user and target secretly or separately choose options; user succeeds if the target does not pick the matching answer. Use for prediction duels.
- 协力: choose a cooperation route with another role until that role's turn end. Routes include damage total, draw total, discarded suits, or used/played suits.
- 护甲: damage buffer with an upper limit. Use for armor-like survivability that is not recovery.
- 蓄力技: shared charge markers across all charge skills on the same character. Use when multiple effects consume one common battery.
- 持恒技: cannot be disabled by other skill effects. Use sparingly for immutable rules.
- 追思: a status lasting the game; later effects can require targets without that status. Use for memorial/exclusion logic.
- 虚拟伤害: incomplete damage event that triggers some "about to cause", "after causing", and "after receiving" timings, but does not reduce HP. Use cautiously for "as if harmed" records.
- 结党 / 休整: special multi-character or temporary-exit handling. Use only for unusual identity designs.
- 六经: map classics to card classes or names. Use when a scholar's canon naturally becomes a card taxonomy.
- 金 / 五灵 marks: large bundled mark sets. Treat as inspiration for a menu, but avoid copying many marks into a normal custom general.

### 三国杀：一将成名

- 转换技 state choice: some packages allow choosing 阴/阳 at game start. Use when opening stance matters.
- 连招技: effects that require a sequence of card use. Use for martial rhythm or practiced routines.
- 击伤: body-part injury menu with escalating later option. Use for targeted maiming or hunter/sniper themes.

### 三国杀OL

- 隐匿: starts as male/no-skill hidden form, then reveals after HP loss or before turn. Use for ambush, disguise, or delayed true form.
- 宗族技: same-clan generals share a clan skill; clan membership follows history, not whether a general owns the skill.
- 卜算X: 观星-like top-deck viewing with explicit count. Use as a concise divination term.
- 天候: global weather states such as heat, fog, rain, frost. Use for environment-driven generals, but watch passive table burden.
- 锻造: table chooses助力/妨害, compares revealed point totals, and determines crafting quality. Use for smithing, collective projects, or contested production.

### 三国杀海外版

- 施法: delayed effect with chosen delay count, usually 1-3. X equals chosen delay. Use for rituals or brewing consequences.
- 妄行: user chooses X up to a cap, then pays at turn end if the skill was used. Use for deliberate excess.
- 摧坚: once per turn after using damage card, X depends on target skill count. Use for anti-expert or armor-breaking attacks.
- 游击 / 搏击: extra effect based on whether target is outside or inside attack range. Use for distance-position identity.
- 昂扬技: limited skill that can be refreshed after an "激昂" condition. Use for heroic comeback surges.
- 历战: if used this turn, upgrade/modify the skill at turn end for the whole game. Use for campaign growth.
- 同心: choose a partner until next turn; both execute linked effects. Use for paired or oath designs.
- 异性双人武将: counts as both male and female. Use for dual-character sex-related interactions.
- 暴虐值: charge by causing or receiving damage, cap 5, then consume for effects. Use for violent momentum.
- 武 marks / 布道 skills: large arsenals or spell lists. Use as menu inspiration, but reduce option count for normal designs.

### 欢乐三国杀

- 逗猫: passing marker with start/end upkeep. Use for playful recurring attention, but avoid nuisance loops.
- 念影: branch count grows with related-character ownership. Not recommended unless the environment supports collection-based scaling.
- 幻术牌堆 / 幻术牌: copied deck and fake cards with destruction rules. Use only for high-complexity illusion specialists.
- 军令: a small command menu: damage, random discard, no healing, or severe hand/skill restriction. Use as compact military orders.

### 三国杀小程序

- 韵律技: conversion skill with 平/仄 states; "转韵" flips state and resets use count. Use for poetry, music, rhythm, or alternating tempo.
- 谋略值 / 妙计: strategy points up to 5; spend 1-3 to use 拆/无懈/无中. Use for tactical resource conversion.
- 逐鹿: multi-player pindian, unique highest point wins. Use for contesting leadership.
- 奋武技: per-round use count equals damage caused plus received plus one, capped. Use for battle heat or revenge momentum.

### 线下

- 议事: participants reveal a hand card; red majority, black majority, or tie determines result. Use for court debate, assembly, or public will.
- 双势力 / 势力技能 / 变更势力: choose or change faction; faction skills only work when current faction matches. Use for allegiance shifts.
- 【影】: special spade-A basic cards that cannot be used or played and leave the game after discard. Use for shadow tokens carried as real cards.
- 蓄谋: set hand cards face down in judgment zone; process later in reverse order. Use for plots that can be disrupted while waiting.
- 额外牌堆: separate finite decks for searchable special cards. Use when a design needs named extra cards but should not create infinite supply.
- 双副类别装备: one equipment occupies two slots and is replaced by either slot. Use for grand artifacts with real opportunity cost.
- 起义军: indicator with increased slash pressure and end-turn obligation. Use for insurgency, faction infection, or forced aggression.

## Special Card Design Patterns

### Reviewed Special Cards By Package

Package labels matter. Do not use a package's card names or assumptions when the user excludes that package.

OL:

- 【有难同当】: all targets横置. Use for mass chain state, shared peril, or coerced alliance.
- 【雷公助我】: all targets perform【闪电】judgments; the user draws for damage caused this way. Use for risky global thunder ritual.

SP:

- 【言笑】: delayed judgment-area card; when it resolves, the target obtains all cards in their judgment area. Use for delayed cleansing or storing future release.

国战:

Use cautiously outside 国战. Translate away 明置/暗置、大小势力、队列、阴阳鱼、主副将 unless the user asks for 国战.

- 【以逸待劳】: same-force allies draw two then discard two. Use for team filtering without net universal gain.
- 【知己知彼】: inspect a hidden general card or hand. Outside 国战, map to hand or identity information.
- 【远交近攻】: a different-force visible target draws one, then you draw three. Use for asymmetric diplomacy.
- 【勠力同心】: unchained targets become横置; chained targets draw. Use for chain-state fork.
- 【挟天子以令诸侯】: end play phase and possibly gain an extra turn later. Extra-turn language needs heavy cost.
- 【敕令】: unknown-force roles choose reveal, discard equipment, or lose HP; the card leaves game instead of discard. Use for edict pressure.
- 【火烧连营】: fire damage by seat/formation. Outside 国战, map to adjacent, distance, or formation logic.
- 【联军盛宴】: self chooses recover/draw by another force size; others draw and reset. Use for feast-style asymmetric support.
- 【调虎离山】: temporary removal from distance/seat/targeting/HP-change calculations. Use only with clear duration.

游戏模式:

- 【浮雷】: moving thunder judgment with escalating damage count. Use for accumulating threat that passes between roles.
- 【草木皆兵】: failed judgment reduces target draw and rewards distance-1 roles. Use for panic aura around a target.
- 【增兵减灶】: target draws three, then discards one non-basic or two cards. Use for generous but taxed logistics.
- 【声东击西】: you hand a card to a nearby role, then that role passes cards to a third role. Use for forced relay and distance bargaining.
- 【弃甲曳兵】: target chooses to discard weapon/offensive-mount side or armor/defensive-mount side. Use for equipment taxonomy pressure.
- 【金蝉脱壳】: protects when it is your only hand card, and draws when discarded. Use for last-card escape.
- 【毒】: poisonous hand object that causes HP loss when used or when it leaves hand face-up; one variant can be passed away after drawing. Use for contaminated resource design.
- 【偷梁换柱】: randomly redistributes equipment. Use only when chaos/randomness is central.
- 【强兵足食】/【强易】: special-resource logistics and taxed intelligence theft. Treat as mode-specific unless the resource is redefined.
- 【文和乱武】: all others choose to slash nearest role or lose HP. Use for panic-order pressure.
- 【斗转星移】/【李代桃僵】: random HP or hand redistribution. Use only for fate/chaos designs.
- 【影】: inert real-card token that cannot be used and leaves game after discard. Use for shadow tokens.
- 【笑里藏刀】: target draws by lost HP up to a cap, then you damage them. Use for gift-then-harm.
- 【美人计】: gendered multi-role hand transfer and hand-count damage. Use only when gender politics is central.
- 【草船借箭】: cancels a slash/damage trick against you, then obtains it after resolution. Use for defensive capture.
- 【解甲归田】: target obtains all cards in their equipment area. Use for demobilization or disarm-with-compensation.
- 【逐鹿天下】: reveal equipment from deck/discard, targets sequentially equip. Use for public equipment draft.

线下:

- 【一鼓作气】: this turn, your card uses ignore distance and use-count limits. Strong; attach cost or narrow timing.
- 【万物智联】: redistribute equipment and attach energy recover/consume to gain/loss. Use for high-concept equipment network.
- 【以毒攻毒】: inspect wounded target's hand; if both sides have【毒】, cleanse and draw, otherwise both suffer sourceless damage. Use for mutual-risk diagnosis.
- 【大军压境】: other roles may slash one target with no distance/count limit. Use for siege pressure.
- 【火烧连营】: reveal a target card, discard same-suit hand card to burn/discard; chained state modifies outcome. Use for suit-match burn.
- 【玉石皆碎】: deal 1 damage, then lose 1 HP. Use for simple mutual destruction.
- 【荆襄盛世】: reveal cards by living roles; chosen targets take one each, user gains rest. Use for prosperity distribution.

通用机制:

- 【蓄谋】: delayed plotted card processed later from last placed to first placed. Use for visible delayed schemes.

Use special cards as design vocabulary:

- response fork:【奇正相生】asks for different responses depending on assigned role; good for two-line pressure.
- hand balancing:【调剂盐梅】moves hands toward equality and can recycle if the equality condition holds.
- deck-reveal assault:【兵临城下】reveals top cards and uses the revealed【杀】in sequence.
- area exchange:【瞒天过海】takes from targets' regions and gives cards back.
- poisonous hand object:【毒】punishes face-up loss unless routed away; pair with cleanse cards like【刮骨疗毒】.
- enhanced attack basic:【刺杀】adds a discard tax to【闪】responses.
- equipment-to-draw conversion:【树上开花】turns discards, especially equipment, into draw.
- close-range exchange:【推心置腹】and【逐近弃远】care about distance and region cards.
- revealed-card threat:【趁火打劫】and【出其不意】turn hand information into damage or theft pressure.
- top-deck control:【洞烛先机】looks at top cards, reorders, then draws.
- previous-card mimicry:【随机应变】copies the previous basic/trick used or played this turn.
- attribute/disruption attack: 冰【杀】can trade damage for discarding target cards.
- equipment punishment:【水淹七军】forces equipment discard or thunder damage.

## Equipment And Treasure Vocabulary

Common equipment motifs:

- high-range siege weapons: 大攻车, 霹雳车. Use for siege, durability, and equipment suppression.
- unlimited or modified【杀】: 元戎精械弩, 思召剑, 烈淬刀, 银月枪.
- response restriction: 太极拂尘, 思召剑, 赤血青锋.
- broad defense: 奇门八卦, 国风玉袍, 红棉百花袍, 护心镜.
- damage compression or prevention: 照月狮子盔, 琼梳, 护心镜.
- hand/phase treasures: 金梳, 犀梳, 天机图, 虚妄之冕.
- chain/control treasures: 太公阴符, 乌铁锁链.
- virtual-use treasure: 照骨镜.
- durable/special artifacts: 大攻车 variants, 霹雳车 variants, 双副类别装备.

When borrowing equipment language for a general, decide whether the character creates equipment, borrows equipment, treats a card as equipment, or uses an equipment-like rule without adding new cards.

## Low-Priority Card Vocabulary

Use these only when the general has a concrete object, artifact, mount, weapon, or armor fantasy. Usually borrow one small rule shape instead of creating the whole card or an equipment engine.

- OL: 【菌子（五菇丰登衍生）】、【商鞅变法】、【五菇丰登】、【铁蒺玄舆】、【飞轮战舆】、【束发紫金冠】、【三略】、【传国玉玺】、【八尺琼勾玉】、【平安御守】、【鬼龙斩月刀】、【赤焰镇魂琴】、【修罗炼狱戟】、【鸾凤和鸣剑】、【刑天破军斧】、【金乌落日弓】、【无双方天戟】、【镔铁双戟】、【百辟刀】、【真龙长剑】、【秦弩】、【雷切】、【童子切安纲】、【妖刀村正】、【手里剑】、【七彩神鹿】、【三首】、【玲珑狮蛮带】、【钩镶】、【昔具足】、【绝尘金戈】
- 十周年: 【天雷刃】、【红缎枪】、【混毒弯匕】、【水波剑】
- 国战: 【玉玺】、【定澜夜明珠】、【吴六剑】、【三尖两刃刀】、【飞龙夺凤】、【戢鳞潜翼】、【惊帆】、【六龙骖驾】、【明光铠】、【太平要术】、【盟军大纛】。Use only for explicit 国战 or carefully adapted designs.
- 国际服: 【灵宝仙葫】、【冲应神符】
- 手杀: 【六龙骖驾】、【先天八卦阵】、【仁王金刚盾】、【桐油百韧甲】
- 游戏模式: 【铜雀】、【青囊书】、【传国玉玺】、【信鸽】、【锦盒】、【五行鹤翎扇】、【七宝刀】、【衠钢槊】、【折戟】、【七星宝刀】、【倚天剑】、【无锋剑】、【涯角枪】、【驽马】、【黑光铠】、【烂银甲】、【引蜂衣】、【女装】、【太平要术】、【引蜂甲】、【夜行衣】、【战象】
- 线下: 【扑克牌组（四花色1-13）】、【春秋笔】、【湖海笔】、【马鞭】、【浑天仪】、【铁蒺藜骨朵】、【宣花斧】、【百辟双匕】、【魂·诸葛连弩】、【剑】、【刀】、【斧】、【戟】、【枪】、【弓】、【刑鞭】、【众】、【飞龙夺凤】、【尚方宝剑】、【軨軨】、【魂·八卦阵】

## Design Cautions

Do not combine multiple high-burden systems in one normal general. For example, avoid putting delayed casting, public zones, charge points, and special cards into the same compact custom design.

Menus with many marks or subskills are suitable for boss, deity, or package-centerpiece characters; for ordinary generals, compress to 2-3 options or one visible axis.

Special zones and extra decks need precise movement rules. Define entry, cap, ownership, whether cards count as hand/equipment/judgment, and where they go when discarded.

If a mechanism creates a new card or virtual card, check survival cards, response timing, and whether it triggers "use", "play", "lose", or "enter discard pile" events.

If using official special cards in a custom skill, prefer naming a narrow set rather than "any special card". A small named set is easier to test and balance.

## Adding Future Mechanism References

When the user provides new mechanism material and asks to improve this skill, extract:

- mechanism name and source scope;
- one-sentence definition in 三国杀 rules language;
- when to use it in character design;
- guardrails, especially loops, survival-card generation, extra turns, global listeners, and hidden memory;
- one compact wording template or example if the mechanism has a stable shape;
- whether it is normal priority, low priority, mode-specific, or only flavor vocabulary.

Merge the result into the closest section instead of creating a new one for every source.
