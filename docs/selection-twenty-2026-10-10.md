# 2026-10-10 新增二十位人物：选题与检索说明

本轮新增20个公开 Skill，系列从10个扩至30个。所有内容是原创方法转译，不复制已有 Skill 的人格设定、文案或示例；不宣称历史人物授权或 GitHub 首创。人物范围延续本系列：中国思想、史学、文学美学、教育与科学实践，不把“思想家”限制为一门哲学专业。

## 检索口径
在公开发布前，使用 GitHub API 检索20个中文名加 skill 的仓库、20个连字符英文名加 skill 的仓库，以及20个中文名加 filename:SKILL.md 的代码。查询、命中路径与 incomplete_results 状态保存在 batch20-search.json 和 batch20-english-search.json。API检索只涵盖可索引内容、主要分支和所给名称，不能证明全 GitHub 不存在；别名、拼音写法、未公开内容和索引延迟均可能遗漏。

中文仓库检索19人返回0，叶圣陶返回1；本组英文命名检索均返回0。代码命中更多，但人物提及、生成示例、收录镜像与专门原创作品必须区分。下面“未检出”仅是本次口径与路径审阅结果，不是排他性结论。生成示例路径只表明已有覆盖，未独立验证其运行效果。

## 人物与定位

| 人物 | 中文仓库/代码命中 | 已有覆盖说明 | 新作品与收藏潜力的编辑判断 |
|---|---|---|---|
| [顾炎武](https://github.com/constantin2088/gu-yanwu-practical-skill) | 0 / 6 | 未检出专门人物作品；命中项为其他 Skill 提及 | 研究需要落到实际问题，适合公共事务与应用研究；与陈寅恪的现有证据审查区分 |
| [张载](https://github.com/constantin2088/zhang-zai-responsibility-skill) | 0 / 6 | 未检出专门人物作品；命中项为其他 Skill 提及 | 责任与资源冲突是常见协作问题；关注负担分配，避免空泛道德劝说 |
| [戴震](https://github.com/constantin2088/dai-zhen-concepts-skill) | 0 / 1 | 未检出专门人物作品；命中项为其他 Skill 提及 | 概念偷换与抽象口号常见，可服务组织规则和论证审查 |
| [王充](https://github.com/constantin2088/wang-chong-skepticism-skill) | 0 / 1 | 未检出专门人物作品；命中项为其他 Skill 提及 | 怀疑与证据是广泛需求，给营销和权威主张可用的反例检验 |
| [章学诚](https://github.com/constantin2088/zhang-xuecheng-documentation-skill) | 0 / 2 | 未检出专门人物作品；命中项为其他 Skill 提及 | 知识库和机构资料编纂有明确产物，定位义例与删选，避免通用考证重复 |
| [傅斯年](https://github.com/constantin2088/fu-sinian-evidence-skill) | 0 / 0 | 本次代码检索未检出 | 从材料缺口出发组织研究，适合论文前期和资料工程，与审查已得资料区分 |
| [钱穆](https://github.com/constantin2088/qian-mu-context-skill) | 0 / 21 | 1个人物生成示例（qian_mu），其余主要为其他思想家、通史与写作工具提及 | 大众历史阅读入口较明确，关注通史脉络和同维度比较 |
| [梁漱溟](https://github.com/constantin2088/liang-shuming-community-skill) | 0 / 3 | 1个人物生成示例（liang_shu_ming），另有其他人物提及 | 乡建与社区协作有稳定议题入口，但须验证参与和地方条件 |
| [晏阳初](https://github.com/constantin2088/yan-yangchu-education-skill) | 0 / 1 | 未检出专门人物作品；命中项为其他 Skill 提及 | 成人教育和乡村服务有实际受众，突出课程与服务联动 |
| [叶圣陶](https://github.com/constantin2088/ye-shengtao-writing-skill) | 1 / 8 | 1个专门摄影导师仓库；另有通用中文写作与去套话工具，写作场景存在邻近竞争 | 中文自改高频，人物认知明确；面对邻近写作工具，突出作者自主与表达诚实 |
| [朱光潜](https://github.com/constantin2088/zhu-guangqian-aesthetics-skill) | 0 / 16 | 主要为人文学术写作工具及其收录、中文表达工具引用，未检出专门朱光潜作品 | 美学入门认知明确，可用在作品评论、设计反馈；审美理由与功能测量分开 |
| [宗白华](https://github.com/constantin2088/zong-baihua-artistic-skill) | 0 / 0 | 本次代码检索未检出 | 艺术设计和展陈可形成具体作品，突出情景与空间节奏，避免符号堆砌 |
| [刘勰](https://github.com/constantin2088/liu-xie-composition-skill) | 0 / 5 | 未检出专门人物作品；命中项为其他 Skill 提及 | 文心雕龙入口明确，文章构思高频，突出主旨、材料与篇章关联 |
| [刘知几](https://github.com/constantin2088/liu-zhiji-narrative-skill) | 0 / 9 | 主要为编剧对白 Skill 的多仓收录，未检出专门刘知几作品 | 事件复盘和机构叙事有明确需求，关注遗漏与委托利益，而非重复史料校勘 |
| [沈括](https://github.com/constantin2088/shen-kuo-observation-skill) | 0 / 2 | 1个人物生成示例（shen_kuo），另有毕昇提及 | 科学观察认知较强，可服务测量差异与工程问题；只做安全试验规划 |
| [宋应星](https://github.com/constantin2088/song-yingxing-process-skill) | 0 / 1 | 1个人物生成示例（song_yingxing） | 天工开物入口较清晰，工序、隐性手艺与损耗记录有可复用产物 |
| [徐光启](https://github.com/constantin2088/xu-guangqi-adaptation-skill) | 0 / 1 | 1个人物生成示例（xu_guangqi） | 跨域知识引入与本地适配常见，突出试点与扩展门槛 |
| [冯友兰](https://github.com/constantin2088/feng-youlan-reflection-skill) | 0 / 12 | 1个人物生成示例（feng_you_lan），其余主要为其他人物提及 | 哲学阅读认知明确，行动意义适于自我反思；拒绝人格分级 |
| [郑观应](https://github.com/constantin2088/zheng-guanying-commerce-skill) | 0 / 0 | 本次代码检索未检出 | 产业竞争与能力配套场景明确，避免把商战写成营销口号或投资保证 |
| [颜元](https://github.com/constantin2088/yan-yuan-practice-skill) | 0 / 0 | 本次代码检索未检出 | 学习投入与能力验收有实用入口，强调练习账本，与陶行知的课程任务设计区分 |

已有覆盖入口：[叶圣陶摄影导师](https://github.com/cscb603/yeshengtao-photo-mentor)、[历史人物生成示例目录](https://github.com/111pointer111/claude-marketplace/tree/main/skills/historical-persona-distiller/output)、[人文学术写作](https://github.com/Norman-bury/research-writing-skill)、[编剧对白](https://github.com/jtydhr88/screenwriting-skills)。完整路径以原始快照为准。

## 收藏潜力如何理解
判断依据是人物/著作认知入口、GitHub较少的直接覆盖、任务是否高频、输出是否可立即使用，以及与既有作品的区别。没有可靠数据支持精确星标增长预测，因此不编“预计星数”、增长率或绝对排名。叶圣陶、朱光潜、刘勰、沈括、宋应星有较清晰的大众著作或学校教育入口；章学诚、戴震、颜元等较专门的人选以稀缺方法和具体任务取胜，仍需要真实用户反馈。没有购买星标、发送推广消息或承诺增长。

## 内容与验证标准
每个作品包含6步特定工作流、资料卡、工作表、边界、3个原创虚构示例、8个模型行为评测场景，以及本地确定性辅助工具。每个仓库11项单元测试，合计220项；格式、完整性、本地文档链接和示例工具均实际检查。来源谱系、修改位置、资源缺口、观察配对、依赖循环等工具只处理可明确判断的输入结构，绝不认证事实、艺术价值或人物境界。

来源优先核查原文、机构或出版者的重刊；电子转录不是初版本逐字校勘。钱穆只核查所列序文，刘勰以《神思》为重点；梁漱溟回忆正文抓取不完整，晏阳初的原始演讲完整刊本未取得，郑观应全文及多版本未完全校勘，均在资料卡明示。这些作品只把可核查思想取向与项目原创现代流程分开，不把未读内容写成已证实的方法。详细版本、位置、获取限制与归属见各仓库 references/sources.md。

公开仓库直接发布成 Skill，无需 GitHub Releases。npx 安装发现与 CI 通过说明仓库可发现、结构和工具检查通过；独立客户端模型行为评测尚未执行，也尚无真实用户长期效果验证。评测场景是待执行规范，不能计作模型通过。

系列标识、总仓库回链、推荐和 GitHub About/Topics 从 catalog/skills.json 同步；该目录仍为唯一人工维护入口，模板快照由同步器生成。
