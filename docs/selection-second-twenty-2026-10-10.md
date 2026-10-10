# 第二批新增20位人物：选题与检索说明（2026-10-10）

本轮选择20个新作品，全部提交后把系列从30个扩至50个。延续中国思想、史学、教育与文学美学的系列范围，关注具体可执行方法，不以人格扮演或复制已有文案充当新作品。

## 发布前检索口径

GitHub API 查询中文姓名加 skill 的仓库、连字符英文姓名加 skill 的仓库，以及中文姓名加 filename:SKILL.md 的代码。原始结果及 incomplete_results 保存为 b2-search.json 与 b2-english-search.json。先检索21个候选，再用苏洵替代相关覆盖较多的苏轼；苏轼的原始结果另外保留，不删除未入选证据。

20个入选人物的中文仓库查询中18人返回0，王安石、司马光各返回1。英文查询中李贽、阮籍、李渔存在明显分词误命中；苏洵无仓库命中但已有生成示例。代码命中既含明确人物作品、生成示例，也含正文提及和镜像，不等于独立作品数量。王夫之已有 nuwa-skills/wangfuzhi-skill；王安石、司马光有 perspective 仓库。覆盖较少不等于首创，本项目不复制这些仓库的内容。

检索仅涵盖公开可索引内容与所给名称，别名、拼音变体、非主要分支、私有仓库与索引延迟可能遗漏。下表路径匹配只作为已有覆盖线索，不声称这些作品已通过运行验证。

| 人物与新仓库 | 中文仓库 / 代码 / 英文仓库命中 | 已有覆盖线索 | 新作品用途与收藏潜力的编辑判断 |
|---|---|---|---|
| [王夫之](https://github.com/constantin2088/wang-fuzhi-context-skill) | 0 / 19 / 0 | [nuwa-skills/wangfuzhi-skill:SKILL.md](https://github.com/nuwa-skills/wangfuzhi-skill/blob/355aaaa4ab06cec56ee45c0cb864f643b5284aea/SKILL.md) | 历史决策与管理复盘入口明确；区别于钱穆的通史脉络，重点是类比失效条件。 |
| [龚自珍](https://github.com/constantin2088/gong-zizhen-talent-skill) | 0 / 8 / 0 | [111pointer111/claude-marketplace:skills/historical-persona-distiller/output/gong_zi_zhen/SKILL.md](https://github.com/111pointer111/claude-marketplace/blob/d41ed9c9dbd640a02cdc7b0b48fa8f42aae8b528/skills/historical-persona-distiller/output/gong_zi_zhen/SKILL.md) | 人才评价和反模板创作有广泛受众；龚自珍教材认知提供入口，区别于蔡元培的观点协作。 |
| [魏源](https://github.com/constantin2088/wei-yuan-benchmark-skill) | 0 / 4 / 0 | 本次已审阅路径未见姓名专属入口；其他命中可能仅为正文提及，不能断言全 GitHub 不存在 | 外部调研与民用能力比较是高频任务，区别于徐光启的引入后本地实验。 |
| [康有为](https://github.com/constantin2088/kang-youwei-utopia-skill) | 0 / 3 / 0 | [111pointer111/claude-marketplace:skills/historical-persona-distiller/output/kang_you_wei/SKILL.md](https://github.com/111pointer111/claude-marketplace/blob/d41ed9c9dbd640a02cdc7b0b48fa8f42aae8b528/skills/historical-persona-distiller/output/kang_you_wei/SKILL.md) | 制度想象与产品普惠设计有跨领域入口；与黄宗羲的问责审查区分，侧重愿景的过渡代价。 |
| [谭嗣同](https://github.com/constantin2088/tan-sitong-barriers-skill) | 0 / 8 / 0 | [111pointer111/claude-marketplace:skills/historical-persona-distiller/output/tan_si_tong/SKILL.md](https://github.com/111pointer111/claude-marketplace/blob/d41ed9c9dbd640a02cdc7b0b48fa8f42aae8b528/skills/historical-persona-distiller/output/tan_si_tong/SKILL.md) | 组织反馈与服务可达有具体产物；与蔡元培的异见协调区分，侧重参与门槛与双向回应。 |
| [章太炎](https://github.com/constantin2088/zhang-taiyan-terms-skill) | 0 / 7 / 0 | [111pointer111/claude-marketplace:skills/historical-persona-distiller/output/zhang_tai_yan/SKILL.md](https://github.com/111pointer111/claude-marketplace/blob/d41ed9c9dbd640a02cdc7b0b48fa8f42aae8b528/skills/historical-persona-distiller/output/zhang_tai_yan/SKILL.md) | 古籍读解和术语转译有稳定用户；区别于严复的完整论证翻译，侧重古今义和类别错置。 |
| [李贽](https://github.com/constantin2088/li-zhi-authenticity-skill) | 0 / 13 / 3 | [111pointer111/claude-marketplace:skills/historical-persona-distiller/output/li_zhi/SKILL.md](https://github.com/111pointer111/claude-marketplace/blob/d41ed9c9dbd640a02cdc7b0b48fa8f42aae8b528/skills/historical-persona-distiller/output/li_zhi/SKILL.md) | 真实表达和反迎合高频；与叶圣陶文字自改区分，聚焦表达动机和评价压力。 |
| [王安石](https://github.com/constantin2088/wang-anshi-change-skill) | 1 / 27 / 1 | [zhaohuang321/wang-anshi-perspective](https://github.com/zhaohuang321/wang-anshi-perspective)；[IchenDEV/superman:skills/wang-anshi-perspective/SKILL.md](https://github.com/IchenDEV/superman/blob/c9fe0b743769e24e101a262452f879cab00785f9/skills/wang-anshi-perspective/SKILL.md)；[111pointer111/claude-marketplace:skills/historical-persona-distiller/output/wang_anshi/SKILL.md](https://github.com/111pointer111/claude-marketplace/blob/d41ed9c9dbd640a02cdc7b0b48fa8f42aae8b528/skills/historical-persona-distiller/output/wang_anshi/SKILL.md) | 组织改革有实际需求，王安石知名度高；已有少量作品须透明说明，区别于宋志平的经营管理。 |
| [司马光](https://github.com/constantin2088/sima-guang-restraint-skill) | 1 / 22 / 1 | [zhaohuang321/sima-guang-perspective](https://github.com/zhaohuang321/sima-guang-perspective) | 面子消费与组织长期承诺高频，区别于洪亮吉供需缺口，聚焦支出惯性与可退出性。 |
| [苏洵](https://github.com/constantin2088/su-xun-concessions-skill) | 0 / 5 / 0 | [111pointer111/claude-marketplace:skills/historical-persona-distiller/output/su_xun/SKILL.md](https://github.com/111pointer111/claude-marketplace/blob/d41ed9c9dbd640a02cdc7b0b48fa8f42aae8b528/skills/historical-persona-distiller/output/su_xun/SKILL.md) | 供应合作和连续让步有常见痛点，苏洵教材认知较强；比苏轼的多仓人格覆盖更稀少。 |
| [欧阳修](https://github.com/constantin2088/ouyang-xiu-coalitions-skill) | 0 / 19 / 0 | [111pointer111/claude-marketplace:skills/historical-persona-distiller/output/ouyang_xiu/SKILL.md](https://github.com/111pointer111/claude-marketplace/blob/d41ed9c9dbd640a02cdc7b0b48fa8f42aae8b528/skills/historical-persona-distiller/output/ouyang_xiu/SKILL.md) | 组织合作和利益披露场景明确，区别于蔡元培观点协调，侧重收益变动与规则。 |
| [韩愈](https://github.com/constantin2088/han-yu-mentorship-skill) | 0 / 16 / 0 | [111pointer111/claude-marketplace:skills/historical-persona-distiller/output/han_yu/SKILL.md](https://github.com/111pointer111/claude-marketplace/blob/d41ed9c9dbd640a02cdc7b0b48fa8f42aae8b528/skills/historical-persona-distiller/output/han_yu/SKILL.md) | 择师与有效提问高频且师说认知强，区别于课程学习 Skill，聚焦求教关系与专长匹配。 |
| [柳宗元](https://github.com/constantin2088/liu-zongyuan-intervention-skill) | 0 / 10 / 0 | [111pointer111/claude-marketplace:skills/historical-persona-distiller/output/liu_zongyuan/SKILL.md](https://github.com/111pointer111/claude-marketplace/blob/d41ed9c9dbd640a02cdc7b0b48fa8f42aae8b528/skills/historical-persona-distiller/output/liu_zongyuan/SKILL.md) | 反微管理和减负实用，教材认知强；区别于社区责任分配，重点是干预本身的副作用。 |
| [嵇康](https://github.com/constantin2088/ji-kang-boundaries-skill) | 0 / 8 / 0 | [111pointer111/claude-marketplace:skills/historical-persona-distiller/output/ji_kang/SKILL.md](https://github.com/111pointer111/claude-marketplace/blob/d41ed9c9dbd640a02cdc7b0b48fa8f42aae8b528/skills/historical-persona-distiller/output/ji_kang/SKILL.md) | 职业边界与拒绝沟通高频，嵇康认知有辨识度；区别于一般人格扮演。 |
| [阮籍](https://github.com/constantin2088/ruan-ji-conformity-skill) | 0 / 6 / 1 | [111pointer111/claude-marketplace:skills/historical-persona-distiller/output/ruan_ji/SKILL.md](https://github.com/111pointer111/claude-marketplace/blob/d41ed9c9dbd640a02cdc7b0b48fa8f42aae8b528/skills/historical-persona-distiller/output/ruan_ji/SKILL.md) | 社会比较与职业焦虑入口广；与冯友兰意义反思区分，侧重外部角色脚本，不提供治疗。 |
| [葛洪](https://github.com/constantin2088/ge-hong-breadth-skill) | 0 / 4 / 0 | 本次已审阅路径未见姓名专属入口；其他命中可能仅为正文提及，不能断言全 GitHub 不存在 | 跨领域知识综合有明确产物，区别于傅斯年研究规划，侧重来源范围与冲突保留。 |
| [陈亮](https://github.com/constantin2088/chen-liang-capability-skill) | 0 / 2 / 0 | 本次已审阅路径未见姓名专属入口；其他命中可能仅为正文提及，不能断言全 GitHub 不存在 | AI 工具采购与组织能力验收常见，区别于颜元个人学习，重点在资源可调度与配套。 |
| [洪亮吉](https://github.com/constantin2088/hong-liangji-resources-skill) | 0 / 0 / 0 | 本次已审阅路径未见姓名专属入口；其他命中可能仅为正文提及，不能断言全 GitHub 不存在 | 服务容量与增长压力有实用入口，检索覆盖极低；区别于司马光支出持续性，侧重需求和分配。 |
| [李渔](https://github.com/constantin2088/li-yu-usability-skill) | 0 / 32 / 1 | 本次已审阅路径未见姓名专属入口；其他命中可能仅为正文提及，不能断言全 GitHub 不存在 | 界面与日常空间设计需求广，李渔已有戏剧类引用；本作品聚焦位置和可用性，避开戏剧人格。 |
| [袁枚](https://github.com/constantin2088/yuan-mei-expression-skill) | 0 / 4 / 0 | [111pointer111/claude-marketplace:skills/historical-persona-distiller/output/yuan_mei/SKILL.md](https://github.com/111pointer111/claude-marketplace/blob/d41ed9c9dbd640a02cdc7b0b48fa8f42aae8b528/skills/historical-persona-distiller/output/yuan_mei/SKILL.md) | 诗文自改有明确用户，性灵提供辨识入口；区别于刘勰篇章构造，聚焦风格适题与材料服务情意。 |

## 如何判断收藏潜力

结合著作或教材认知入口、公开覆盖线索、任务发生频率、立即可用的产物和与现有30个作品的差异。王安石、司马光、韩愈、柳宗元、龚自珍、苏洵有较清晰的学校教育入口；洪亮吉、陈亮、葛洪等以资源、实际能力和取材方法提供差异。没有足够数据支持预计星数、增长率或确定排行，最终需要真实使用者反馈。没有购买星标或向外发送推广消息。

## 内容与检查

每个作品含6步专门工作流、资料归属和范围、工作表、边界、3个原创虚构示例（第一例有具体工作表展开）、8个待运行模型行为场景，以及适用的本地确定性辅助工具。20个仓库共220项单元测试，并检查格式、完整性、内部链接和真实工具样例输入。工具处理来源谱系、修改位置、资源缺口、依赖关系和独立表现，不认证事实、价值、人格或真实模型效果。

资料以古代原文电子转录为主，不把电子版称为初刻本校勘。康有为仅核查甲部所列片段，目录明确有未完成内容；谭嗣同以自叙与界说为重点；陈亮使用后世《宋史》引录的上书段落，原信入口正文未完整读取；章太炎仅核查文学总略开篇，葛洪仅用外篇尚博，不提供古代药方和炼丹实践。其他具体范围逐项见 references/sources.md。所有现代流程与示例归本项目设计，不伪托历史人物的现代观点。

直接公开发布成 Skill，不创建 GitHub Releases。安装发现、CI与单元测试通过不能代替独立客户端模型行为评测；160个场景仍为待执行规范，长期真实用户效果尚未验证。

## 系列维护

只维护 catalog/skills.json 的作品和仓库元数据；中英文目录、人物标识、主页回链、统一 Topics、相关推荐和模板目录快照由已有同步流程生成。发布前不把未提交仓库登记为已发布。
