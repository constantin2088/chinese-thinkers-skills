<div align="center">

<img src="assets/banner.svg" alt="中国思想的 AI 工具箱：100 位人物，学习、研究、决策与表达" width="900" />

# Chinese Thinkers as Skills

### 给 AI 一座中国思想的工具箱。

**孔子帮你把学习变成行动，孙子帮你权衡选择，胡适帮你检验假设，钱学森帮你看清系统。**

100 位中国思想家、学者与实践者，各有一套有出处、有步骤、有示例的 **Agent Skill**。

[![Validate series](https://github.com/constantin2088/chinese-thinkers-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/constantin2088/chinese-thinkers-skills/actions/workflows/validate.yml)
[![MIT](https://img.shields.io/badge/License-MIT-dbb86b.svg)](LICENSE)

[60 秒体验](#60秒体验) · [按问题选方法](#作品目录) · [可复制的试用任务](docs/try-it.md) · [English](README.en.md)

</div>

## 60秒体验

**知道很多，行动很少？先试王阳明。** 在项目目录安装：

```bash
npx skills add constantin2088/wang-yangming-action-skill
```

安装时选择你的客户端。然后把具体问题交给它：

```text
用王阳明 Skill 分析：我知道备份很重要，却一直没有验证文件能否恢复。
先区分“不知道怎么做、没准备好、担心风险、目标冲突”，
再给一个 15 分钟内能完成的小文件备份与恢复任务。
输出：知行差距表、实际行动、验收证据、失败后的下一步。
不要把计划已经写好，当成行动已经完成。
```

你要检查的成果应像这样具体：

| 已声称知道 | 最小行动 | 可以验收的证据 | 下一步 |
|---|---|---|---|
| “备份很重要” | 用测试文件做一次备份与恢复 | 恢复后文件内容与原文件一致 | 能恢复再安排真实资料的备份计划 |

*上表为原创虚构示例，展示目标产物，未冒充一次真实模型评测输出。*

还可以试：[胡适：把争论变成假设](docs/try-it.md#hypotheses) · [孙子：做与不做的成本](docs/try-it.md#strategy) · [陈寅恪：矛盾材料互证](docs/try-it.md#evidence) · [叶茂中：从顾客冲突到实验](docs/try-it.md#marketing)。

客户端是否加载和执行 Skill，取决于其支持方式；[安装说明](docs/installation.md)区分安装发现、实际安装与运行验证。

## 作品目录

先找问题，再找人物。首页推荐来自同一份目录；每个人物仓库都能回到这里，也能找到同类方法。

<!-- CATALOG:START -->
### 按问题选方法

| 你遇到的问题 | 先试这些方法 |
|---|---|
| [读了很多，怎样真正做到？](docs/choose-a-skill.md#learning) | [孔子·把学到的变成做到的](https://github.com/constantin2088/confucius-learning-skill) · [王阳明·把知道变成行动证据](https://github.com/constantin2088/wang-yangming-action-skill) · [苏轼·别把比喻当成掌握](https://github.com/constantin2088/su-shi-understanding-skill) |
| [材料很多，哪些值得相信？](docs/choose-a-skill.md#research) | [鲁迅·借鉴之前先辨别](https://github.com/constantin2088/lu-xun-selective-learning-skill) · [毛泽东·先调查再下结论](https://github.com/constantin2088/mao-zedong-investigation-skill) · [胡适·先把问题研究清楚](https://github.com/constantin2088/hu-shi-hypotheses-skill) |
| [资源有限，先做什么、停止什么？](docs/choose-a-skill.md#decisions) | [孙子·行动前先算清代价](https://github.com/constantin2088/sun-tzu-strategy-skill) · [老子·减少多余动作](https://github.com/constantin2088/laozi-low-intervention-skill) · [钱学森·把专家意见与数据合成可检验方案](https://github.com/constantin2088/qian-xuesen-system-synthesis-skill) |
| [人和规则，怎样一起运转？](docs/choose-a-skill.md#organizations) | [叶茂中·冲突营销](https://github.com/constantin2088/ye-maozhong-skill) · [蔡元培·多元协作](https://github.com/constantin2088/cai-yuanpei-skill) · [宋志平·经营管理](https://github.com/constantin2088/song-zhiping-management-skill) |
| [怎样写得清楚、看得具体？](docs/choose-a-skill.md#expression) | [叶圣陶·诚实写作与自改](https://github.com/constantin2088/ye-shengtao-writing-skill) · [朱光潜·审美观察与判断](https://github.com/constantin2088/zhu-guangqian-aesthetics-skill) · [宗白华·意境与空间节奏](https://github.com/constantin2088/zong-baihua-artistic-skill) |
| [被惯性困住，怎样重新看问题？](docs/choose-a-skill.md#reflection) | [庄子·跳出唯一答案](https://github.com/constantin2088/zhuangzi-perspective-skill) · [张载·共同体责任](https://github.com/constantin2088/zhang-zai-responsibility-skill) · [冯友兰·行动意义反思](https://github.com/constantin2088/feng-youlan-reflection-skill) |

[查看六类场景的全部方法](docs/choose-a-skill.md) · [按关键词找方法](docs/installation.md#find-a-method)

### 从熟悉的问题开始

| 人物入口 | 可以完成什么 |
|---|---|
| [孔子·把学到的变成做到的](https://github.com/constantin2088/confucius-learning-skill) | 把读书笔记转成行动、复盘承诺与协作信用 |
| [孙子·行动前先算清代价](https://github.com/constantin2088/sun-tzu-strategy-skill) | 民用项目竞争、资源不足或需要决定做与不做 |
| [老子·减少多余动作](https://github.com/constantin2088/laozi-low-intervention-skill) | 流程越来越复杂、需要降低控制和协调成本 |
| [庄子·跳出唯一答案](https://github.com/constantin2088/zhuangzi-perspective-skill) | 被单一指标困住、比较不同尺度与生活选择 |
| [王阳明·把知道变成行动证据](https://github.com/constantin2088/wang-yangming-action-skill) | 明白道理却迟迟不做、需要知行复盘 |
| [鲁迅·借鉴之前先辨别](https://github.com/constantin2088/lu-xun-selective-learning-skill) | 外部经验看起来都好、需要拆分可用与有害部分 |
| [毛泽东·先调查再下结论](https://github.com/constantin2088/mao-zedong-investigation-skill) | 民用项目出现争议、报告只有结论而缺少一手事实 |
| [钱学森·把专家意见与数据合成可检验方案](https://github.com/constantin2088/qian-xuesen-system-synthesis-skill) | 复杂民用项目涉及多专业、需要把意见和模型对齐 |
| [苏轼·别把比喻当成掌握](https://github.com/constantin2088/su-shi-understanding-skill) | 概念讲得懂却不会用、需要从说明转成体验与实践 |
| [胡适·先把问题研究清楚](https://github.com/constantin2088/hu-shi-hypotheses-skill) | 讨论被口号带走、需要把问题拆成可证伪假设 |
| [诸葛亮·把志向变成可持续专注](https://github.com/constantin2088/zhuge-liang-focus-skill) | 长期目标被杂务冲散、需要学习与行动节奏 |
| [曾国藩·让长期目标有恢复机制](https://github.com/constantin2088/zeng-guofan-routines-skill) | 长期习惯断断续续、需要稳健积累与复盘 |

### 完整目录

<details>
<summary>展开全部100位人物</summary>

| 人物 | 核心能力 | 项目 | 状态 |
|---|---|---|---|
| **梁启超·自新与变局** | 变局判断、能力更新、认知修正 | [liang-qichao-skill](https://github.com/constantin2088/liang-qichao-skill) | 已发布 |
| **叶茂中·冲突营销** | 消费冲突、产品表达、增长实验 | [ye-maozhong-skill](https://github.com/constantin2088/ye-maozhong-skill) | 已发布 |
| **陈寅恪·深度研究** | 史料互证、证据分层、研究推断 | [chen-yinke-research-skill](https://github.com/constantin2088/chen-yinke-research-skill) | 已发布 |
| **蔡元培·多元协作** | 异见管理、观点协调、多元协作 | [cai-yuanpei-skill](https://github.com/constantin2088/cai-yuanpei-skill) | 已发布 |
| **宋志平·经营管理** | 经营决策、精细管理、组织效率 | [song-zhiping-management-skill](https://github.com/constantin2088/song-zhiping-management-skill) | 已发布 |
| **许倬云·系统思维** | 系统观察、跨学科分析、长期演化 | [xu-zhuoyun-systems-skill](https://github.com/constantin2088/xu-zhuoyun-systems-skill) | 已发布 |
| **费孝通·文化自觉与实地洞察** | 访谈取证、关系情境、跨文化理解 | [fei-xiaotong-fieldwork-skill](https://github.com/constantin2088/fei-xiaotong-fieldwork-skill) | 已发布 |
| **陶行知·教学做合一** | 真实任务学习、教人自学、迁移验证 | [tao-xingzhi-learning-skill](https://github.com/constantin2088/tao-xingzhi-learning-skill) | 已发布 |
| **严复·概念转译与论证校核** | 术语定名、意义保真、解释与译文分离 | [yan-fu-translation-skill](https://github.com/constantin2088/yan-fu-translation-skill) | 已发布 |
| **黄宗羲·制度问责与公共评议** | 规则受益分析、权责制衡、独立评议 | [huang-zongxi-governance-skill](https://github.com/constantin2088/huang-zongxi-governance-skill) | 已发布 |
| **顾炎武·经世问题研究** | 现实问题定位、广泛取证、知识转成公共用途 | [gu-yanwu-practical-skill](https://github.com/constantin2088/gu-yanwu-practical-skill) | 已发布 |
| **张载·共同体责任** | 受影响者识别、责任边界、照护负担分配 | [zhang-zai-responsibility-skill](https://github.com/constantin2088/zhang-zai-responsibility-skill) | 已发布 |
| **戴震·概念与人情辨析** | 词义分辨、规范与事实分离、真实负担审查 | [dai-zhen-concepts-skill](https://github.com/constantin2088/dai-zhen-concepts-skill) | 已发布 |
| **王充·问难与实证** | 权威主张质疑、逻辑矛盾、可检验反例 | [wang-chong-skepticism-skill](https://github.com/constantin2088/wang-chong-skepticism-skill) | 已发布 |
| **章学诚·文献义例与史德** | 文献目的、分类义例、编纂取舍与立场披露 | [zhang-xuecheng-documentation-skill](https://github.com/constantin2088/zhang-xuecheng-documentation-skill) | 已发布 |
| **傅斯年·材料与工具规划** | 研究材料扩展、工具适配、采集计划与证据缺口 | [fu-sinian-evidence-skill](https://github.com/constantin2088/fu-sinian-evidence-skill) | 已发布 |
| **钱穆·历史文化脉络** | 研究意义、通史关联、制度与文化的情境解释 | [qian-mu-context-skill](https://github.com/constantin2088/qian-mu-context-skill) | 已发布 |
| **梁漱溟·社区协作实验** | 地方组织、共同事务、合作能力与渐进试点 | [liang-shuming-community-skill](https://github.com/constantin2088/liang-shuming-community-skill) | 已发布 |
| **晏阳初·生活能力建设** | 识字与表达、生计、卫生常识、公民协作的联动设计 | [yan-yangchu-education-skill](https://github.com/constantin2088/yan-yangchu-education-skill) | 已发布 |
| **叶圣陶·诚实写作与自改** | 思想与表达对齐、文字精密、自主修改 | [ye-shengtao-writing-skill](https://github.com/constantin2088/ye-shengtao-writing-skill) | 已发布 |
| **朱光潜·审美观察与判断** | 观看态度区分、具体形式观察、审美理由 | [zhu-guangqian-aesthetics-skill](https://github.com/constantin2088/zhu-guangqian-aesthetics-skill) | 已发布 |
| **宗白华·意境与空间节奏** | 情景关联、虚实层次、观看路径与时空节奏 | [zong-baihua-artistic-skill](https://github.com/constantin2088/zong-baihua-artistic-skill) | 已发布 |
| **刘勰·文思与篇章构造** | 立意、材料与想象、篇章气脉和体裁适配 | [liu-xie-composition-skill](https://github.com/constantin2088/liu-xie-composition-skill) | 已发布 |
| **刘知几·叙事偏差审查** | 事实与褒贬分离、删选偏差、叙事权力与修订 | [liu-zhiji-narrative-skill](https://github.com/constantin2088/liu-zhiji-narrative-skill) | 已发布 |
| **沈括·观察与试验辨误** | 现象记录、条件变化、仪器误差与解释检验 | [shen-kuo-observation-skill](https://github.com/constantin2088/shen-kuo-observation-skill) | 已发布 |
| **宋应星·工艺与生产系统** | 原料工具工序、工艺依赖、产出与损耗记录 | [song-yingxing-process-skill](https://github.com/constantin2088/song-yingxing-process-skill) | 已发布 |
| **徐光启·知识引入与试验** | 跨域知识理解、本地条件适配、小试与扩展门槛 | [xu-guangqi-adaptation-skill](https://github.com/constantin2088/xu-guangqi-adaptation-skill) | 已发布 |
| **冯友兰·行动意义反思** | 自我理解、动机与行动、个人与共同利益的关系 | [feng-youlan-reflection-skill](https://github.com/constantin2088/feng-youlan-reflection-skill) | 已发布 |
| **郑观应·产业能力与竞争** | 商务得失、能力链、竞争比较与资源优先级 | [zheng-guanying-commerce-skill](https://github.com/constantin2088/zheng-guanying-commerce-skill) | 已发布 |
| **颜元·实习与能力验收** | 学习投入分配、身体力行、独立表现与反馈 | [yan-yuan-practice-skill](https://github.com/constantin2088/yan-yuan-practice-skill) | 已发布 |
| **王夫之·因势审例** | 历史类比条件、制度适用范围、变化中的判断 | [wang-fuzhi-context-skill](https://github.com/constantin2088/wang-fuzhi-context-skill) | 已发布 |
| **龚自珍·破格与人才生态** | 单一标准偏差、人才多样性、修复成长环境 | [gong-zizhen-talent-skill](https://github.com/constantin2088/gong-zizhen-talent-skill) | 已发布 |
| **魏源·外部比较与长技识别** | 多方外部资料、能力差距、选择性学习 | [wei-yuan-benchmark-skill](https://github.com/constantin2088/wei-yuan-benchmark-skill) | 已发布 |
| **康有为·愿景与制度压力检验** | 痛苦地图、理想制度假设、过渡与权利检验 | [kang-youwei-utopia-skill](https://github.com/constantin2088/kang-youwei-utopia-skill) | 已发布 |
| **谭嗣同·关系壁垒与互通** | 关系阻隔、双向发声、资源与退出 | [tan-sitong-barriers-skill](https://github.com/constantin2088/tan-sitong-barriers-skill) | 已发布 |
| **章太炎·术语沿革与文本边界** | 术语古今义、文本类别、翻译中的时代错置 | [zhang-taiyan-terms-skill](https://github.com/constantin2088/zhang-taiyan-terms-skill) | 已发布 |
| **李贽·真意与评价压力** | 表达动机、评价压力、经验与套话分离 | [li-zhi-authenticity-skill](https://github.com/constantin2088/li-zhi-authenticity-skill) | 已发布 |
| **王安石·改革名实与执行** | 改革定义、权限、实施负担与异议复核 | [wang-anshi-change-skill](https://github.com/constantin2088/wang-anshi-change-skill) | 已发布 |
| **司马光·节用与持续负担** | 必要支出、惯性升级、收入变化下的持续性 | [sima-guang-restraint-skill](https://github.com/constantin2088/sima-guang-restraint-skill) | 已发布 |
| **苏洵·连续让步与累计代价** | 短期缓解、累计资源损失、替代选择与停止线 | [su-xun-concessions-skill](https://github.com/constantin2088/su-xun-concessions-skill) | 已发布 |
| **欧阳修·协作与利益同盟** | 协作理由、共同利益、异议和利益变化 | [ouyang-xiu-coalitions-skill](https://github.com/constantin2088/ouyang-xiu-coalitions-skill) | 已发布 |
| **韩愈·择师与问题求教** | 问题定位、专长匹配、求教与独立迁移 | [han-yu-mentorship-skill](https://github.com/constantin2088/han-yu-mentorship-skill) | 已发布 |
| **柳宗元·减扰与成长条件** | 过度干预、必要支持、扰动成本与恢复 | [liu-zongyuan-intervention-skill](https://github.com/constantin2088/liu-zongyuan-intervention-skill) | 已发布 |
| **嵇康·适配与拒绝表达** | 角色适配、不可承受条件、诚实拒绝与替代 | [ji-kang-boundaries-skill](https://github.com/constantin2088/ji-kang-boundaries-skill) | 已发布 |
| **阮籍·角色脚本与尺度转换** | 默认身份脚本、外部评价、尺度转换与自主选择 | [ruan-ji-conformity-skill](https://github.com/constantin2088/ruan-ji-conformity-skill) | 已发布 |
| **葛洪·广博取材与异说并置** | 取材范围、异说保留、用途与证据归属 | [ge-hong-breadth-skill](https://github.com/constantin2088/ge-hong-breadth-skill) | 已发布 |
| **陈亮·名目与实际能力** | 账面资源、实际可用性、表现与配套 | [chen-liang-capability-skill](https://github.com/constantin2088/chen-liang-capability-skill) | 已发布 |
| **洪亮吉·需求增长与资源缺口** | 需求与供给增速、分配不均、条件压力与补缺 | [hong-liangji-resources-skill](https://github.com/constantin2088/hong-liangji-resources-skill) | 已发布 |
| **李渔·用物适位与体验设计** | 使用频率、位置适配、脆弱物保护与实际体验 | [li-yu-usability-skill](https://github.com/constantin2088/li-yu-usability-skill) | 已发布 |
| **袁枚·性情与风格适题** | 具体感受、材料驱使、风格适配和多样评价 | [yuan-mei-expression-skill](https://github.com/constantin2088/yuan-mei-expression-skill) | 已发布 |
| **孔子·把学到的变成做到的** | 把读书笔记转成行动、复盘承诺与协作信用 | [confucius-learning-skill](https://github.com/constantin2088/confucius-learning-skill) | 已发布 |
| **孟子·把善意落实到选择** | 面对利益与原则冲突、把同情转成有边界的行动 | [mencius-values-skill](https://github.com/constantin2088/mencius-values-skill) | 已发布 |
| **荀子·设计能坚持的学习系统** | 学习计划反复中断、选择工具与练习环境 | [xunzi-deliberate-learning-skill](https://github.com/constantin2088/xunzi-deliberate-learning-skill) | 已发布 |
| **老子·减少多余动作** | 流程越来越复杂、需要降低控制和协调成本 | [laozi-low-intervention-skill](https://github.com/constantin2088/laozi-low-intervention-skill) | 已发布 |
| **庄子·跳出唯一答案** | 被单一指标困住、比较不同尺度与生活选择 | [zhuangzi-perspective-skill](https://github.com/constantin2088/zhuangzi-perspective-skill) | 已发布 |
| **墨子·让能力证据代替关系** | 选人、评价项目、比较受益与资源负担 | [mozi-merit-skill](https://github.com/constantin2088/mozi-merit-skill) | 已发布 |
| **韩非·看清奖励怎样改变行为** | 指标被刷、奖励被套利、权责与实际表现脱节 | [han-fei-incentives-skill](https://github.com/constantin2088/han-fei-incentives-skill) | 已发布 |
| **孙子·行动前先算清代价** | 民用项目竞争、资源不足或需要决定做与不做 | [sun-tzu-strategy-skill](https://github.com/constantin2088/sun-tzu-strategy-skill) | 已发布 |
| **孙膑·按条件重新配置资源** | 民用资源配置、需要在整体目标下重排任务 | [sun-bin-matching-skill](https://github.com/constantin2088/sun-bin-matching-skill) | 已发布 |
| **管仲·先补基础再谈激励** | 组织激励失效、资源基础与制度要求不匹配 | [guan-zhong-foundations-skill](https://github.com/constantin2088/guan-zhong-foundations-skill) | 已发布 |
| **商鞅·改变规则先检查代价** | 旧规则妨碍新目标、审查变革的实施与公平 | [shang-yang-reform-skill](https://github.com/constantin2088/shang-yang-reform-skill) | 已发布 |
| **鬼谷子·先听懂再表达** | 谈判信息不足、需要澄清对方真实约束 | [guiguzi-listening-skill](https://github.com/constantin2088/guiguzi-listening-skill) | 已发布 |
| **董仲舒·把失误追到治理责任** | 组织反复出错、检验领导示范和纠错机制 | [dong-zhongshu-accountability-skill](https://github.com/constantin2088/dong-zhongshu-accountability-skill) | 已发布 |
| **贾谊·为突发需求留出余量** | 日常资源够用但缺少应急余量、需要压力情景 | [jia-yi-reserves-skill](https://github.com/constantin2088/jia-yi-reserves-skill) | 已发布 |
| **司马迁·把事件写成有证据的历史** | 整理机构历史、人物故事或长期变化叙事 | [sima-qian-history-skill](https://github.com/constantin2088/sima-qian-history-skill) | 已发布 |
| **班固·让分类说清材料边界** | 知识库分类混乱、比较不同历史叙述与门类 | [ban-gu-categories-skill](https://github.com/constantin2088/ban-gu-categories-skill) | 已发布 |
| **诸葛亮·把志向变成可持续专注** | 长期目标被杂务冲散、需要学习与行动节奏 | [zhuge-liang-focus-skill](https://github.com/constantin2088/zhuge-liang-focus-skill) | 已发布 |
| **刘禹锡·分清条件与行动空间** | 把失败全怪运气、辨认可以改变与不能控制的部分 | [liu-yuxi-agency-skill](https://github.com/constantin2088/liu-yuxi-agency-skill) | 已发布 |
| **白居易·让表达回应真实问题** | 文章好看但用途不清、想让写作回应读者与现实 | [bai-juyi-purpose-skill](https://github.com/constantin2088/bai-juyi-purpose-skill) | 已发布 |
| **苏轼·别把比喻当成掌握** | 概念讲得懂却不会用、需要从说明转成体验与实践 | [su-shi-understanding-skill](https://github.com/constantin2088/su-shi-understanding-skill) | 已发布 |
| **朱熹·把一段材料真正读懂** | 读长文只剩印象、需要逐段理解和检验先入观点 | [zhu-xi-close-reading-skill](https://github.com/constantin2088/zhu-xi-close-reading-skill) | 已发布 |
| **陆九渊·识别目标背后的动机** | 目标正确却行动失真、需要审查义利冲突 | [lu-jiuyuan-intentions-skill](https://github.com/constantin2088/lu-jiuyuan-intentions-skill) | 已发布 |
| **王阳明·把知道变成行动证据** | 明白道理却迟迟不做、需要知行复盘 | [wang-yangming-action-skill](https://github.com/constantin2088/wang-yangming-action-skill) | 已发布 |
| **曾国藩·让长期目标有恢复机制** | 长期习惯断断续续、需要稳健积累与复盘 | [zeng-guofan-routines-skill](https://github.com/constantin2088/zeng-guofan-routines-skill) | 已发布 |
| **惠施·找出争论中的尺度变化** | 双方都说有道理却用不同尺度、需要检查概念边界 | [hui-shi-definitions-skill](https://github.com/constantin2088/hui-shi-definitions-skill) | 已发布 |
| **张之洞·分清目的与引入的方法** | 引入新工具时担心失去原有目标、需要评估取舍 | [zhang-zhidong-adaptation-skill](https://github.com/constantin2088/zhang-zhidong-adaptation-skill) | 已发布 |
| **胡适·先把问题研究清楚** | 讨论被口号带走、需要把问题拆成可证伪假设 | [hu-shi-hypotheses-skill](https://github.com/constantin2088/hu-shi-hypotheses-skill) | 已发布 |
| **鲁迅·借鉴之前先辨别** | 外部经验看起来都好、需要拆分可用与有害部分 | [lu-xun-selective-learning-skill](https://github.com/constantin2088/lu-xun-selective-learning-skill) | 已发布 |
| **陈独秀·让主张接受科学检验** | 观点来自权威或习惯、需要检查自主判断与实际用途 | [chen-duxiu-independent-thinking-skill](https://github.com/constantin2088/chen-duxiu-independent-thinking-skill) | 已发布 |
| **李大钊·把时代愿景落在现在** | 谈未来理想很多、需要明确当下责任与可实施行动 | [li-dazhao-present-action-skill](https://github.com/constantin2088/li-dazhao-present-action-skill) | 已发布 |
| **毛泽东·先调查再下结论** | 民用项目出现争议、报告只有结论而缺少一手事实 | [mao-zedong-investigation-skill](https://github.com/constantin2088/mao-zedong-investigation-skill) | 已发布 |
| **周恩来·把公私边界写清楚** | 公共资源、亲友请求与岗位职责发生冲突 | [zhou-enlai-public-duty-skill](https://github.com/constantin2088/zhou-enlai-public-duty-skill) | 已发布 |
| **邓小平·用事实检验小范围改变** | 旧规则阻碍任务、需要先试后扩而非凭口号改革 | [deng-xiaoping-fact-based-pilots-skill](https://github.com/constantin2088/deng-xiaoping-fact-based-pilots-skill) | 已发布 |
| **孙中山·把准备知识与实际行动分开** | 计划看似能做、需要检查知识缺口与实施条件 | [sun-yat-sen-preparation-skill](https://github.com/constantin2088/sun-yat-sen-preparation-skill) | 已发布 |
| **黄炎培·让学习连接真实职业任务** | 课程与岗位脱节、需要设计有实际产出的学习 | [huang-yanpei-vocational-fit-skill](https://github.com/constantin2088/huang-yanpei-vocational-fit-skill) | 已发布 |
| **王国维·把审美判断落到作品细节** | 评论诗词或创作只有好美、需要说明景与情如何相连 | [wang-guowei-aesthetic-scenes-skill](https://github.com/constantin2088/wang-guowei-aesthetic-scenes-skill) | 已发布 |
| **林语堂·让幽默保留体谅** | 文案或表达想轻松一些、需要避开羞辱和冷酷 | [lin-yutang-kind-humor-skill](https://github.com/constantin2088/lin-yutang-kind-humor-skill) | 已发布 |
| **钱钟书·比较之前先确定可比之处** | 跨文化或跨作品比较容易变成标签、需要落实文本证据 | [qian-zhongshu-comparative-reading-skill](https://github.com/constantin2088/qian-zhongshu-comparative-reading-skill) | 已发布 |
| **杨绛·让克制表达仍有事实与温度** | 回忆或个人叙事想避免煽情、需要区分所见与猜想 | [yang-jiang-restrained-narrative-skill](https://github.com/constantin2088/yang-jiang-restrained-narrative-skill) | 已发布 |
| **陈鹤琴·从生活活动设计学习** | 儿童学习只有讲解、需要设计安全的观察与做中学活动 | [chen-heqin-active-curriculum-skill](https://github.com/constantin2088/chen-heqin-active-curriculum-skill) | 已发布 |
| **张伯苓·把服务目的与能力证据相连** | 公益或团队项目有热情、需要同时核受益与实际能力 | [zhang-boling-service-capability-skill](https://github.com/constantin2088/zhang-boling-service-capability-skill) | 已发布 |
| **熊十力·看原则怎样在实际中表现** | 宣称有原则但实际行为不一致、需要检查抽象承诺与表现 | [xiong-shili-principles-in-use-skill](https://github.com/constantin2088/xiong-shili-principles-in-use-skill) | 已发布 |
| **牟宗三·分清价值判断与专业认知** | 以好动机代替专业证据、需要明确道德与知识的分工 | [mou-zongsan-judgment-boundaries-skill](https://github.com/constantin2088/mou-zongsan-judgment-boundaries-skill) | 已发布 |
| **唐君毅·让文化对话保留多种视角** | 跨背景交流陷入文化标签、需要理解自我与他人处境 | [tang-junyi-cultural-dialogue-skill](https://github.com/constantin2088/tang-junyi-cultural-dialogue-skill) | 已发布 |
| **季羡林·互鉴之前先理解材料** | 文化介绍容易只讲印象、需要核语言语境和互鉴条件 | [ji-xianlin-cultural-learning-skill](https://github.com/constantin2088/ji-xianlin-cultural-learning-skill) | 已发布 |
| **南怀瑾·读讲解时仍回到原典** | 通俗讲解很吸引人、需要分清原典与讲者发挥 | [nan-huaijin-classics-check-skill](https://github.com/constantin2088/nan-huaijin-classics-check-skill) | 已发布 |
| **钱学森·把专家意见与数据合成可检验方案** | 复杂民用项目涉及多专业、需要把意见和模型对齐 | [qian-xuesen-system-synthesis-skill](https://github.com/constantin2088/qian-xuesen-system-synthesis-skill) | 已发布 |
| **马寅初·把人口与资源放在同一口径下** | 人数、需求和供给增长不匹配、需要做有条件的资源情景 | [ma-yinchu-resource-scenarios-skill](https://github.com/constantin2088/ma-yinchu-resource-scenarios-skill) | 已发布 |
| **吴敬琏·先看竞争规则再谈效率** | 业务竞争被特权、信息不透明或准入障碍扭曲 | [wu-jinglian-competition-rules-skill](https://github.com/constantin2088/wu-jinglian-competition-rules-skill) | 已发布 |
| **李泽厚·从历史条件理解审美感受** | 作品评价只有个人喜好、需要连接形式与社会历史语境 | [li-zehou-aesthetic-context-skill](https://github.com/constantin2088/li-zehou-aesthetic-context-skill) | 已发布 |

</details>

<details>
<summary>展开逐个人物安装命令</summary>


选择一个已发布的方法安装即可。

```bash
npx skills add constantin2088/liang-qichao-skill
npx skills add constantin2088/ye-maozhong-skill
npx skills add constantin2088/chen-yinke-research-skill
npx skills add constantin2088/cai-yuanpei-skill
npx skills add constantin2088/song-zhiping-management-skill
npx skills add constantin2088/xu-zhuoyun-systems-skill
npx skills add constantin2088/fei-xiaotong-fieldwork-skill
npx skills add constantin2088/tao-xingzhi-learning-skill
npx skills add constantin2088/yan-fu-translation-skill
npx skills add constantin2088/huang-zongxi-governance-skill
npx skills add constantin2088/gu-yanwu-practical-skill
npx skills add constantin2088/zhang-zai-responsibility-skill
npx skills add constantin2088/dai-zhen-concepts-skill
npx skills add constantin2088/wang-chong-skepticism-skill
npx skills add constantin2088/zhang-xuecheng-documentation-skill
npx skills add constantin2088/fu-sinian-evidence-skill
npx skills add constantin2088/qian-mu-context-skill
npx skills add constantin2088/liang-shuming-community-skill
npx skills add constantin2088/yan-yangchu-education-skill
npx skills add constantin2088/ye-shengtao-writing-skill
npx skills add constantin2088/zhu-guangqian-aesthetics-skill
npx skills add constantin2088/zong-baihua-artistic-skill
npx skills add constantin2088/liu-xie-composition-skill
npx skills add constantin2088/liu-zhiji-narrative-skill
npx skills add constantin2088/shen-kuo-observation-skill
npx skills add constantin2088/song-yingxing-process-skill
npx skills add constantin2088/xu-guangqi-adaptation-skill
npx skills add constantin2088/feng-youlan-reflection-skill
npx skills add constantin2088/zheng-guanying-commerce-skill
npx skills add constantin2088/yan-yuan-practice-skill
npx skills add constantin2088/wang-fuzhi-context-skill
npx skills add constantin2088/gong-zizhen-talent-skill
npx skills add constantin2088/wei-yuan-benchmark-skill
npx skills add constantin2088/kang-youwei-utopia-skill
npx skills add constantin2088/tan-sitong-barriers-skill
npx skills add constantin2088/zhang-taiyan-terms-skill
npx skills add constantin2088/li-zhi-authenticity-skill
npx skills add constantin2088/wang-anshi-change-skill
npx skills add constantin2088/sima-guang-restraint-skill
npx skills add constantin2088/su-xun-concessions-skill
npx skills add constantin2088/ouyang-xiu-coalitions-skill
npx skills add constantin2088/han-yu-mentorship-skill
npx skills add constantin2088/liu-zongyuan-intervention-skill
npx skills add constantin2088/ji-kang-boundaries-skill
npx skills add constantin2088/ruan-ji-conformity-skill
npx skills add constantin2088/ge-hong-breadth-skill
npx skills add constantin2088/chen-liang-capability-skill
npx skills add constantin2088/hong-liangji-resources-skill
npx skills add constantin2088/li-yu-usability-skill
npx skills add constantin2088/yuan-mei-expression-skill
npx skills add constantin2088/confucius-learning-skill
npx skills add constantin2088/mencius-values-skill
npx skills add constantin2088/xunzi-deliberate-learning-skill
npx skills add constantin2088/laozi-low-intervention-skill
npx skills add constantin2088/zhuangzi-perspective-skill
npx skills add constantin2088/mozi-merit-skill
npx skills add constantin2088/han-fei-incentives-skill
npx skills add constantin2088/sun-tzu-strategy-skill
npx skills add constantin2088/sun-bin-matching-skill
npx skills add constantin2088/guan-zhong-foundations-skill
npx skills add constantin2088/shang-yang-reform-skill
npx skills add constantin2088/guiguzi-listening-skill
npx skills add constantin2088/dong-zhongshu-accountability-skill
npx skills add constantin2088/jia-yi-reserves-skill
npx skills add constantin2088/sima-qian-history-skill
npx skills add constantin2088/ban-gu-categories-skill
npx skills add constantin2088/zhuge-liang-focus-skill
npx skills add constantin2088/liu-yuxi-agency-skill
npx skills add constantin2088/bai-juyi-purpose-skill
npx skills add constantin2088/su-shi-understanding-skill
npx skills add constantin2088/zhu-xi-close-reading-skill
npx skills add constantin2088/lu-jiuyuan-intentions-skill
npx skills add constantin2088/wang-yangming-action-skill
npx skills add constantin2088/zeng-guofan-routines-skill
npx skills add constantin2088/hui-shi-definitions-skill
npx skills add constantin2088/zhang-zhidong-adaptation-skill
npx skills add constantin2088/hu-shi-hypotheses-skill
npx skills add constantin2088/lu-xun-selective-learning-skill
npx skills add constantin2088/chen-duxiu-independent-thinking-skill
npx skills add constantin2088/li-dazhao-present-action-skill
npx skills add constantin2088/mao-zedong-investigation-skill
npx skills add constantin2088/zhou-enlai-public-duty-skill
npx skills add constantin2088/deng-xiaoping-fact-based-pilots-skill
npx skills add constantin2088/sun-yat-sen-preparation-skill
npx skills add constantin2088/huang-yanpei-vocational-fit-skill
npx skills add constantin2088/wang-guowei-aesthetic-scenes-skill
npx skills add constantin2088/lin-yutang-kind-humor-skill
npx skills add constantin2088/qian-zhongshu-comparative-reading-skill
npx skills add constantin2088/yang-jiang-restrained-narrative-skill
npx skills add constantin2088/chen-heqin-active-curriculum-skill
npx skills add constantin2088/zhang-boling-service-capability-skill
npx skills add constantin2088/xiong-shili-principles-in-use-skill
npx skills add constantin2088/mou-zongsan-judgment-boundaries-skill
npx skills add constantin2088/tang-junyi-cultural-dialogue-skill
npx skills add constantin2088/ji-xianlin-cultural-learning-skill
npx skills add constantin2088/nan-huaijin-classics-check-skill
npx skills add constantin2088/qian-xuesen-system-synthesis-skill
npx skills add constantin2088/ma-yinchu-resource-scenarios-skill
npx skills add constantin2088/wu-jinglian-competition-rules-skill
npx skills add constantin2088/li-zehou-aesthetic-context-skill
```

</details>
<!-- CATALOG:END -->

## 为什么值得留在你的工具箱里

| 你遇到的情况 | Skill 提供的抓手 |
|---|---|
| 建议听起来对，却不知道下一步 | 有顺序的分析步骤、工作表与具体交付物 |
| 引语听起来像真的，却找不到出处 | 标明资料、章段、核查范围与现代转译 |
| 每个问题都被套成同一套答案 | 各人物独立的方法、适用问题与失效边界 |
| 想改进结果，却没有检查依据 | 示例、反例、确定性工具测试和待运行行为用例 |

以[王阳明](https://github.com/constantin2088/wang-yangming-action-skill)的行动验收、[胡适](https://github.com/constantin2088/hu-shi-hypotheses-skill)的假设研究和[陈寅恪](https://github.com/constantin2088/chen-yinke-research-skill)的史料互证为例：它们帮助你形成不同的可检查产物。资料卡区分历史材料、研究解释与项目设计的现代工作流。

## 现在做到哪一步

**100 个公开人物 Skill，直接从仓库安装，无需 GitHub Releases。新增人物暂告一段落，接下来优先打磨真实使用。**

- 已完成目录关联、公开提交、结构与链接检查、确定性工具测试、GitHub CI 和安装发现核验。
- 最近新增的 50 个作品有 550 项通过的本地单元测试，500 项已定义的模型行为场景；**这些模型行为场景尚未在独立客户端运行**。
- 安装工具能发现 Skill，不等于已安装进你的客户端；CI 通过也不等于模型回答已经达到预期。旧作品的行为用例数量另行复核。

[质量标准](QUALITY_STANDARD.md) · [下一阶段计划](ROADMAP.md) · [最近 50 位的选题与资料范围](docs/selection-famous-fifty-2026-10-10.md)。

## 一份目录，连起整个系列

维护者只编辑 [catalog/skills.json](catalog/skills.json)：作品状态、任务介绍、中英文发现入口、六类场景和推荐次序都来自这里。总仓库生成目录；人物仓库展示系列标识、总目录回链、三个同类方法和折叠的完整推荐。GitHub About 的 Description、Website、Topics 在发布时同步，开发模板继承这些关联。

[自动关联说明](docs/series-automation.md) · [开发模板](https://github.com/constantin2088/thinkers-skill-template)。

## 帮它变得更好

**如果这套方法帮你把一个问题想清楚，欢迎给总仓库一颗 ⭐，方便下次找回来。**

最有价值的贡献是一个真实问题：[提交使用反馈](https://github.com/constantin2088/chinese-thinkers-skills/issues/new?template=task-feedback.yml)、[纠正资料或报告问题](https://github.com/constantin2088/chinese-thinkers-skills/issues/new?template=quality-bug.yml)。请说明使用的 Skill、客户端、输入、输出和失败位置；分享前去除私人信息。人物扩展暂停期间，新人物提案保留为备选，优先处理现有作品的反馈与修正。

[贡献指南](CONTRIBUTING.md) · [行为准则](CODE_OF_CONDUCT.md)。

想介绍给朋友？可使用[1280×640 分享图](assets/social-preview.png)，并附上总仓库链接，方便对方按问题挑选。

## 资料与使用边界

本项目独立开源，历史材料与现代工作流的归属分别标注；不冒充人物本人，不伪造引语，不替人物认证现代事件的观点。资料卡会说明采用原文、译文、后人研究或回忆，以及实际核查范围。第三方资料保留原权利；原创代码与文档使用 [MIT](LICENSE)。

[安全说明](SECURITY.md) · 维护者 [@constantin2088](https://github.com/constantin2088)。
