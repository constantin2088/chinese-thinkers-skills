# 新增50位知名人物：作品定位与发现入口（2026-10-10）

本轮将系列由50人扩展到100人。优先考虑广泛的教材、阅读与公众认知入口，同时延续哲学、教育、史学、文学美学、公共治理与系统思想的系列范围。人物的领域和知名度不同；并非每位都是同样广为人知的专业哲学家，惠施、熊十力、牟宗三、唐君毅等更多面向哲学读者。

## 发现与收藏潜力

不再把“GitHub无人发布”当必要条件。孔子、老子、庄子、孙子、王阳明、鲁迅等已有相关作品，我们按频繁发生的任务、可以立刻看懂的成果与独特使用边界设计新的工作流，不复制其他仓库的设定、文案与示例。

人物首页的全部相关推荐折叠展示，保留每个链接，让用途与一分钟示例保持易见。总仓库首页优先展示12个辨识度高且容易试用的入口：孔子学习迁移、孙子民用策略、老子流程减法、庄子视角转换、王阳明行动验收、鲁迅选择性借鉴、毛泽东调查台账、钱学森系统综合、苏轼理解迁移、胡适假说研究、诸葛亮专注计划、曾国藩长期习惯。推荐顺序由 catalog/skills.json 的 discovery_rank 维护，目录生成器读取同一数据；不是实际星数排行。

每个人物仓库首页均展示具体适用问题、交付顺序、一个一分钟示例、安装命令与用途差异。知名度提高识别机会，能复用的工作流才是收藏理由。没有数据支持精确星数、增长率或必然“爆款”的保证，没有购买星标或发送外部推广消息。

## GitHub公开检索快照

对50位人物分别查询中文名加 skill、英文名加 skill，排除本账号，按星数取前20项，并保存时间、查询、total_count、incomplete_results和返回项目。原始数据见 b3-search.json。结果是元数据命中，可能有同名、误分词、集合和工具正文提及，不能当专属Skill数量；别名、拼音变体、非公开项目与索引延迟可能遗漏。以下命中线索不表示已安装或认可其他项目的效果。

已抽读6个同人物项目的README：孔子 nuwa-skills/kongzi-skill、毛选 leezythu/maoxuan-skill、钱学森 DENO0521/Qianxuesen-perspective-Engineering-cybernetics、鲁迅 Qcunyu/Deep-LuXun-skill、王阳明 nuwa-skills/wangyangming-skill、鬼谷子 penyy8540-bit/guiguzi-skill。它们各有思想框架、表达方式、控制论或咨询的入口；其自述来源数量及效果未由本项目验证。本批对应作品的可见产物分别是学习承诺账本、调查事实台账、专家数据接口表、借鉴选择记录、独立行动验收与倾听证据表，范围和输入更集中。已有项目的内容没有复制到本系列。

部分查询明显出现非专属误命中，例如墨子的Mozilla项目、班固的bank工具、惠施的会员汇总、孙中山的中山大学工具、杨绛的江南视角项目。表中保留真实返回数和原始数据，不把它们包装成人物竞争数量。

| 新人物与仓库 | 实际任务与交付定位 | 收藏潜力的编辑判断 | 查询命中：中文 / 英文 |
|---|---|---|---|
| [孔子](https://github.com/constantin2088/confucius-learning-skill) | 把学到的变成做到的；把读书笔记转成行动、复盘承诺与协作信用 | 孔子辨识度极高；学习、信用与协作是广泛需求，首屏展示行动账本而非名言合集。 | 11 / 15 |
| [孟子](https://github.com/constantin2088/mencius-values-skill) | 把善意落实到选择；面对利益与原则冲突、把同情转成有边界的行动 | 孟子价值辨析有教材入口；用可执行选择表区别于道德说教。 | 2 / 1 |
| [荀子](https://github.com/constantin2088/xunzi-deliberate-learning-skill) | 设计能坚持的学习系统；学习计划反复中断、选择工具与练习环境 | 荀子劝学认知明确；学习系统、AI辅助与独立验收易展示。 | 1 / 2 |
| [老子](https://github.com/constantin2088/laozi-low-intervention-skill) | 减少多余动作；流程越来越复杂、需要降低控制和协调成本 | 老子具有国际辨识度；反过度设计与流程减法适合开发者展示，区别于已有视角扮演。 | 6 / 9 |
| [庄子](https://github.com/constantin2088/zhuangzi-perspective-skill) | 跳出唯一答案；被单一指标困住、比较不同尺度与生活选择 | 庄子有广泛文化入口；职业与创作视角切换可形成清楚的前后对比。 | 6 / 8 |
| [墨子](https://github.com/constantin2088/mozi-merit-skill) | 让能力证据代替关系；选人、评价项目、比较受益与资源负担 | 墨子与工程、公益及公平评价有明确连接；提供选人证据表区别于空泛兼爱口号。 | 1 / 18 |
| [韩非](https://github.com/constantin2088/han-fei-incentives-skill) | 看清奖励怎样改变行为；指标被刷、奖励被套利、权责与实际表现脱节 | 韩非辨识度高；指标套利与激励失效是管理和产品高频场景。 | 3 / 1 |
| [孙子](https://github.com/constantin2088/sun-tzu-strategy-skill) | 行动前先算清代价；民用项目竞争、资源不足或需要决定做与不做 | 孙子全球辨识度突出；真实项目策略卡易被收藏，但同类竞争多，差异在条件与停止线。 | 12 / 13 |
| [孙膑](https://github.com/constantin2088/sun-bin-matching-skill) | 按条件重新配置资源；民用资源配置、需要在整体目标下重排任务 | 田忌赛马大众入口清楚；任务匹配表有实用性，主动解释寓例条件区别于成功学。 | 0 / 2 |
| [管仲](https://github.com/constantin2088/guan-zhong-foundations-skill) | 先补基础再谈激励；组织激励失效、资源基础与制度要求不匹配 | 管仲知名度与管子经济思想相连；基础条件清单便于经营管理使用。 | 1 / 1 |
| [商鞅](https://github.com/constantin2088/shang-yang-reform-skill) | 改变规则先检查代价；旧规则妨碍新目标、审查变革的实施与公平 | 商鞅变法认知强；规则迁移与变革代价有讨论性，用实施边界体现差异。 | 1 / 1 |
| [鬼谷子](https://github.com/constantin2088/guiguzi-listening-skill) | 先听懂再表达；谈判信息不足、需要澄清对方真实约束 | 鬼谷子名称传播力强；以倾听和明确同意区别于常见操控式营销。 | 6 / 8 |
| [董仲舒](https://github.com/constantin2088/dong-zhongshu-accountability-skill) | 把失误追到治理责任；组织反复出错、检验领导示范和纠错机制 | 董仲舒教材知名；领导示范与制度责任是实用入口，避免把历史宇宙论当现代科学。 | 0 / 0 |
| [贾谊](https://github.com/constantin2088/jia-yi-reserves-skill) | 为突发需求留出余量；日常资源够用但缺少应急余量、需要压力情景 | 贾谊教材与风险思想可见；资源余量计算适合运营与应急规划。 | 0 / 3 |
| [司马迁](https://github.com/constantin2088/sima-qian-history-skill) | 把事件写成有证据的历史；整理机构历史、人物故事或长期变化叙事 | 司马迁全球历史认知入口；有证据的故事适合写作者、研究者与组织复盘。 | 1 / 0 |
| [班固](https://github.com/constantin2088/ban-gu-categories-skill) | 让分类说清材料边界；知识库分类混乱、比较不同历史叙述与门类 | 班固史学与知识分类连接清晰；知识库整理有开发者收藏场景。 | 0 / 5 |
| [诸葛亮](https://github.com/constantin2088/zhuge-liang-focus-skill) | 把志向变成可持续专注；长期目标被杂务冲散、需要学习与行动节奏 | 诸葛亮大众认知极高；一周专注计划是清楚的展示产物。 | 3 / 2 |
| [刘禹锡](https://github.com/constantin2088/liu-yuxi-agency-skill) | 分清条件与行动空间；把失败全怪运气、辨认可以改变与不能控制的部分 | 刘禹锡教材认知与能动性问题相连；行动空间图易理解且不同于励志口号。 | 0 / 0 |
| [白居易](https://github.com/constantin2088/bai-juyi-purpose-skill) | 让表达回应真实问题；文章好看但用途不清、想让写作回应读者与现实 | 白居易耳熟能详；有目的的表达适合公共说明、产品文案与写作训练。 | 0 / 0 |
| [苏轼](https://github.com/constantin2088/su-shi-understanding-skill) | 别把比喻当成掌握；概念讲得懂却不会用、需要从说明转成体验与实践 | 苏轼认知度极高且同类已有覆盖；用概念到实践的能力验收区别于文风模仿。 | 1 / 17 |
| [朱熹](https://github.com/constantin2088/zhu-xi-close-reading-skill) | 把一段材料真正读懂；读长文只剩印象、需要逐段理解和检验先入观点 | 朱熹辨识度与经典阅读相连；逐段释义工具面向学生、研究和文档使用者。 | 1 / 5 |
| [陆九渊](https://github.com/constantin2088/lu-jiuyuan-intentions-skill) | 识别目标背后的动机；目标正确却行动失真、需要审查义利冲突 | 陆九渊心学入口清晰；目标与激励对照表能区别于王阳明知行闭环。 | 0 / 0 |
| [王阳明](https://github.com/constantin2088/wang-yangming-action-skill) | 把知道变成行动证据；明白道理却迟迟不做、需要知行复盘 | 阳明心学流行入口强；备份恢复等具体场景展示知行证据，避免空泛自律。 | 8 / 4 |
| [曾国藩](https://github.com/constantin2088/zeng-guofan-routines-skill) | 让长期目标有恢复机制；长期习惯断断续续、需要稳健积累与复盘 | 曾国藩大众熟悉且自律工具需求大；恢复机制区别于惩罚式打卡。 | 3 / 4 |
| [惠施](https://github.com/constantin2088/hui-shi-definitions-skill) | 找出争论中的尺度变化；双方都说有道理却用不同尺度、需要检查概念边界 | 惠施有庄子辩论入口；概念尺度检查适合产品、研究与讨论，不宣称大众知名度与孔子相同。 | 0 / 2 |
| [张之洞](https://github.com/constantin2088/zhang-zhidong-adaptation-skill) | 分清目的与引入的方法；引入新工具时担心失去原有目标、需要评估取舍 | 张之洞教材与技术引入联系明显；目的工具对照区别于魏源的外部调研。 | 0 / 0 |
| [胡适](https://github.com/constantin2088/hu-shi-hypotheses-skill) | 先把问题研究清楚；讨论被口号带走、需要把问题拆成可证伪假设 | 胡适研究方法知名且与开发调试高度相通；假设与反证表具有复用价值。 | 0 / 8 |
| [鲁迅](https://github.com/constantin2088/lu-xun-selective-learning-skill) | 借鉴之前先辨别；外部经验看起来都好、需要拆分可用与有害部分 | 鲁迅辨识度极高；选择性借鉴、AI内容与模仿边界有现实讨论价值。 | 13 / 5 |
| [陈独秀](https://github.com/constantin2088/chen-duxiu-independent-thinking-skill) | 让主张接受科学检验；观点来自权威或习惯、需要检查自主判断与实际用途 | 新文化运动知名入口；自主判断与科学术语审查可服务信息消费和工具选择。 | 0 / 0 |
| [李大钊](https://github.com/constantin2088/li-dazhao-present-action-skill) | 把时代愿景落在现在；谈未来理想很多、需要明确当下责任与可实施行动 | 李大钊教材认知强；愿景到当下行动表适合学生和公共项目。 | 0 / 0 |
| [毛泽东](https://github.com/constantin2088/mao-zedong-investigation-skill) | 先调查再下结论；民用项目出现争议、报告只有结论而缺少一手事实 | 毛泽东辨识度极高；调查报告与事实台账有直接用途，首屏清楚限定民用分析。 | 33 / 26 |
| [周恩来](https://github.com/constantin2088/zhou-enlai-public-duty-skill) | 把公私边界写清楚；公共资源、亲友请求与岗位职责发生冲突 | 周恩来大众认知强；公私资源与利益冲突是组织中容易理解的具体入口。 | 0 / 0 |
| [邓小平](https://github.com/constantin2088/deng-xiaoping-fact-based-pilots-skill) | 用事实检验小范围改变；旧规则阻碍任务、需要先试后扩而非凭口号改革 | 邓小平和改革开放辨识度强；用可检查试点表呈现区别，避免空泛成功学。 | 0 / 0 |
| [孙中山](https://github.com/constantin2088/sun-yat-sen-preparation-skill) | 把准备知识与实际行动分开；计划看似能做、需要检查知识缺口与实施条件 | 孙中山大众认知极高；准备与执行双验收容易用于学习和项目，区别于王阳明行动复盘。 | 1 / 2 |
| [黄炎培](https://github.com/constantin2088/huang-yanpei-vocational-fit-skill) | 让学习连接真实职业任务；课程与岗位脱节、需要设计有实际产出的学习 | 黄炎培职教与历史认知清晰；技能教育和转岗需求可用作品证据直接展示。 | 1 / 1 |
| [王国维](https://github.com/constantin2088/wang-guowei-aesthetic-scenes-skill) | 把审美判断落到作品细节；评论诗词或创作只有好美、需要说明景与情如何相连 | 人间词话与三种境界具有文化入口；细节评论和改写能展示比名言更实用的能力。 | 0 / 0 |
| [林语堂](https://github.com/constantin2088/lin-yutang-kind-humor-skill) | 让幽默保留体谅；文案或表达想轻松一些、需要避开羞辱和冷酷 | 林语堂文化辨识度高；AI文案的幽默与分寸可展示清楚的修改前后对比。 | 0 / 0 |
| [钱钟书](https://github.com/constantin2088/qian-zhongshu-comparative-reading-skill) | 比较之前先确定可比之处；跨文化或跨作品比较容易变成标签、需要落实文本证据 | 钱钟书知名且跨文化阅读有广泛需求；条件比较表区别于炫典故和人格扮演。 | 0 / 0 |
| [杨绛](https://github.com/constantin2088/yang-jiang-restrained-narrative-skill) | 让克制表达仍有事实与温度；回忆或个人叙事想避免煽情、需要区分所见与猜想 | 杨绛读者认知强；个人叙事与网络伪名言审查有现实需求，明确后人研究的资料限度。 | 0 / 2 |
| [陈鹤琴](https://github.com/constantin2088/chen-heqin-active-curriculum-skill) | 从生活活动设计学习；儿童学习只有讲解、需要设计安全的观察与做中学活动 | 陈鹤琴教育史认知明确；亲子和教师活动卡有可用入口，避免泛化育儿承诺。 | 0 / 0 |
| [张伯苓](https://github.com/constantin2088/zhang-boling-service-capability-skill) | 把服务目的与能力证据相连；公益或团队项目有热情、需要同时核受益与实际能力 | 张伯苓和南开校训有明确入口；公益项目的目的与能力双证据易传播和收藏。 | 0 / 0 |
| [熊十力](https://github.com/constantin2088/xiong-shili-principles-in-use-skill) | 看原则怎样在实际中表现；宣称有原则但实际行为不一致、需要检查抽象承诺与表现 | 熊十力是现代哲学的重要名字；相比大众名人入口较窄，以价值承诺落地提供明确专业用途。 | 0 / 0 |
| [牟宗三](https://github.com/constantin2088/mou-zongsan-judgment-boundaries-skill) | 分清价值判断与专业认知；以好动机代替专业证据、需要明确道德与知识的分工 | 牟宗三在哲学领域知名；价值与专业证据分工适合AI伦理和产品讨论，受众较专业。 | 0 / 0 |
| [唐君毅](https://github.com/constantin2088/tang-junyi-cultural-dialogue-skill) | 让文化对话保留多种视角；跨背景交流陷入文化标签、需要理解自我与他人处境 | 唐君毅在现代哲学中知名；文化对话有实际协作用途，以具体协商记录打开较专业受众。 | 0 / 0 |
| [季羡林](https://github.com/constantin2088/ji-xianlin-cultural-learning-skill) | 互鉴之前先理解材料；文化介绍容易只讲印象、需要核语言语境和互鉴条件 | 季羡林大众文化入口强；互鉴卡、翻译边界与原典核查适合阅读和内容创作。 | 0 / 0 |
| [南怀瑾](https://github.com/constantin2088/nan-huaijin-classics-check-skill) | 读讲解时仍回到原典；通俗讲解很吸引人、需要分清原典与讲者发挥 | 南怀瑾读者群广；以原典对照和讲解边界区别于名言合集，资料只用明确署名回忆。 | 2 / 0 |
| [钱学森](https://github.com/constantin2088/qian-xuesen-system-synthesis-skill) | 把专家意见与数据合成可检验方案；复杂民用项目涉及多专业、需要把意见和模型对齐 | 钱学森全民辨识度高；复杂项目和AI系统设计适用，以接口与验证任务呈现实用差异。 | 7 / 5 |
| [马寅初](https://github.com/constantin2088/ma-yinchu-resource-scenarios-skill) | 把人口与资源放在同一口径下；人数、需求和供给增长不匹配、需要做有条件的资源情景 | 马寅初与人口议题辨识度高；服务容量情景有现实用途，明确不作人口确定预测。 | 0 / 0 |
| [吴敬琏](https://github.com/constantin2088/wu-jinglian-competition-rules-skill) | 先看竞争规则再谈效率；业务竞争被特权、信息不透明或准入障碍扭曲 | 吴敬琏经济学公众辨识度高；平台与采购竞争规则有实际应用，避免泛市场口号。 | 0 / 0 |
| [李泽厚](https://github.com/constantin2088/li-zehou-aesthetic-context-skill) | 从历史条件理解审美感受；作品评价只有个人喜好、需要连接形式与社会历史语境 | 李泽厚与美的历程有广泛阅读入口；审美语境卡连接创作、展览与阅读，区别于王国维景情细读。 | 1 / 0 |

## 资料与归属

古代作品以已读的公开电子章段为依据，不声称初刊、全书或全部异文已经校勘。孙膑的赛马例证来自司马迁《史记》，不冒作孙膑《兵法》原文；管子、鬼谷子等传承和作者归属有限度。董仲舒与惠施的史传、后人记述，陆九渊的书信与门人回顾分别注明。

现代资料包含本人文章、英文译文、访谈、机构报道、亲属或朋友回忆和学术研究，不把后人研究当本人亲笔。邓小平采用公开英文译文，译者未知，不据此认证中文措辞；周恩来用周秉德回忆，不把不同家规条数当固定规则；杨绛资料是李金涛对陈浩文研究的书评；牟宗三仅读论文中文摘要；季羡林用会议报道中的现代与会者回顾；钱学森用机构系统思想介绍，未取得1990年合著论文全文；马寅初用人口研究所回顾，不直接套用历史增长数字；李泽厚用祁志祥实践美学研究相关段落，未校核全套原著。其余完整范围见各仓库 references/sources.md。

47项相关资料在本地读取网页章段，3项因本地证书或读取超时改由网页阅读器核查：孙中山第六章相关原文、牟宗三研究摘要、陈鹤琴研究相关部分。HTTP成功、链接可访问、摘要或后人回顾均不等于全书核查。现代工作流、工作表和虚构示例为项目原创转译，不伪造人物现代观点、引语或书页。

## 质量与发布

每个作品有6步专门流程、3个原创虚构示例、首例5项工作表、资料卡、边界、10个待运行行为评测场景和适用的确定性辅助工具。50个新作品共550项本地单元测试通过，另检查格式、文档完整性、内部链接与真实工具输入输出。500个模型行为场景尚未在独立客户端执行；这些场景不能被记作通过。安装发现、CI及结构检查不证明实际模型分析质量或长期用户效果。

全部从 thinkers-skill-template 创建公开人物仓库，直接提供根目录 SKILL.md 与安装命令，不创建 GitHub Releases。只有实际提交并推送后才登记目录为 published。统一Topics、About Website、系列标识、回链、推荐链接与模板快照沿用现有同步机制。唯一作品目录维护入口仍为 catalog/skills.json。
