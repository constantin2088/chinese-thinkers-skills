# 2026-10-10 新人物选题依据

本轮从覆盖稀少、可复用任务、认知度、原文可核查四个维度选择费孝通、陶行知、严复、黄宗羲。收藏潜力是编辑判断，不是可保证的星标增长预测；没有制造推广、购买星标或发送外部宣传消息。

## 检索范围及结果
2026-10-10 在 GitHub API 进行人物中文名和连字符英文名加 skill 的 repository search；另检索人物中文名加 filename:SKILL.md 的 code search，并用网页搜索补充。完整查询和返回路径见 candidate-search.json 与 candidate-code-search.json。
库搜索只匹配元数据；代码搜索受索引、别名和分支范围限制，不能证明全 GitHub 不存在同类作品。全文提及人物不等于专门人物 Skill，镜像和转载不能当成独立原创数量。以下是发布本项目之前的快照。

| 人物 | 已检出的相关实现 | 本系列定位和潜力判断 |
|---|---|---|
| 费孝通 | [zeno339/from-the-soil-skill](https://github.com/zeno339/from-the-soil-skill)、[ZaynArche/from-the-soil-skill](https://github.com/ZaynArche/from-the-soil-skill)；代码查询20处，含学术投稿、社会学、镜像等引用 | 《乡土中国》认知入口较清楚；将文化自觉转为用户研究、社区观察、产品出海的实地证据工作流，面向产品与研究使用者 |
| 陶行知 | [nuwa-skills/taoxingzhi-skill](https://github.com/nuwa-skills/taoxingzhi-skill)；代码查询4处，另有杜威和阳明相关提及 | 覆盖稀少；以真实任务、逐步撤提示和独立迁移验证补充课程生成，面向教师、学习者与企业培训 |
| 严复 | [人物生成示例](https://github.com/111pointer111/claude-marketplace/blob/main/skills/historical-persona-distiller/output/yan_fu/SKILL.md)及若干信达雅翻译工具；代码查询15处，含鲁迅、翻译和镜像提及 | 翻译是高频场景，但通用翻译工具已有竞争；突出术语语境、命题范围、作者与译者分离，服务技术文档与思想论述 |
| 黄宗羲 | repository search两种命名均0；代码查询5处，均为其他人物或文学 Skill 的提及，未检出专门黄宗羲人物 Skill | 稀缺度较高；将历史制度批评谨慎转译为组织规则审查、利益冲突和申诉设计，保持历史与现代制度的边界 |

不会宣称这些人物是 GitHub 首创，不复制已有仓库文案、人格设定或示例。作品原创方法转译与第三方原文分别标明。

## 来源与验证
费孝通原文来自清华校友网重刊与北大学术书目；陶行知早期原文、学术研究和实践报道分别标记；严复以《译例言》与《自序》核查概念；黄宗羲核查《明夷待访录》相应篇章并交叉定位。详细版本、定位、核查范围见人物仓库 references/sources.md。
本轮每个 Skill 包含3个示例、8个行为评测场景、专用确定性工具、11项单元测试。CI与安装发现不证明模型行为效果；独立客户端行为评测尚未执行。
