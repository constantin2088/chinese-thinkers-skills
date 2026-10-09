<div align="center">

<img src="assets/banner.svg" alt="Chinese Thinkers as Skills — Not personas. Executable wisdom." width="900" />

# Chinese Thinkers as Skills

### 让中国思想，成为 AI 的可执行能力。

**Not personas. Executable wisdom.**

把中国思想家、学者与实践者的研究方法与决策框架，转译为可验证、可调用、可复用的 **Agent Skills**。

[📚 作品目录](#作品目录) · [🚀 快速安装](#快速安装) · [🔍 质量标准](QUALITY_STANDARD.md) · [🌍 English](README.en.md) · [🤝 参与贡献](CONTRIBUTING.md)

</div>

---

## 为什么做这个系列？

多数“名人 AI”关注人物语气；我们关注**可用的思考程序**。

一个好 Skill 应当回答：在什么问题上使用？如何分析？依据是什么？什么时候不适用？怎样判断结果是否有效？

因此每一个人物 Skill 均应具备独特的 **方法论 → 操作步骤 → 真实 Demo → 证据来源 → 失效边界 → 评测用例**。

> **方法论可以借鉴，历史人物不能被当作现代事件的代言人。**

## 作品目录

<!-- CATALOG:START -->
| 人物 | 核心能力 | 项目 | 状态 |
|---|---|---|---|
| **梁启超·自新与变局** | 变局判断、能力更新、认知修正 | [liang-qichao-skill](https://github.com/constantin2088/liang-qichao-skill) | 已发布 |
| **叶茂中·冲突营销** | 消费冲突、产品表达、增长实验 | [ye-maozhong-skill](https://github.com/constantin2088/ye-maozhong-skill) | 已发布 |
| **陈寅恪·深度研究** | 史料互证、证据分层、研究推断 | chen-yinke-research-skill | 规划中 |
| **蔡元培·多元协作** | 异见管理、观点协调、多元协作 | cai-yuanpei-skill | 规划中 |
| **宋志平·经营管理** | 经营决策、精细管理、组织效率 | song-zhiping-management-skill | 规划中 |
| **许倬云·系统思维** | 系统观察、跨学科分析、长期演化 | xu-zhuoyun-systems-skill | 规划中 |

只有“已发布”项目可安装；规划项目尚不可用。

```bash
npx skills add constantin2088/liang-qichao-skill
npx skills add constantin2088/ye-maozhong-skill
```
<!-- CATALOG:END -->

## 快速安装

安装命令见上方作品目录，选择标为“已发布”的项目。叶茂中目前为 v0.1.0 初始研究版本，独立目标客户端行为评测待执行。

```bash
npx skills add constantin2088/liang-qichao-skill
```

随后在你使用的 Agent 中提问：

> 用梁启超的方法分析我的职业转型。先判断是不是结构性变局，再盘点旧优势和新能力缺口，并给出可验证的 60 天方案。

安装和运行时兼容性取决于客户端；请参阅 [安装说明](docs/installation.md) 与各项目的 README。

## 统一标准，各有自己的方法

**不是**把同一个七步法复制六次，只替换人名。统一的是工程质量；不同人物必须提供独立的分析路径和历史依据。

| 方法类别 | 应当呈现的独特能力 | 典型用户 |
|---|---|---|
| 变革与自新 | 旧经验何时失效，哪些需要保留或更新 | 职场与组织管理 |
| 营销与增长 | 消费冲突如何形成更好的产品表达与测试 | 创业者、品牌经理 |
| 证据研究 | 不一致的材料如何被核查与互证 | 分析师、研究者 |
| 多元协作 | 不同观点如何充分争辩并转成共同决策 | 团队、Multi-Agent |
| 企业经营 | 经营、管理、组织的效率如何具体改善 | 企业管理者 |
| 复杂系统 | 如何识别历史及产业系统的结构变化 | 产业与政策研究 |

## 为什么可信？

我们要求每个正式发布的 Skill：

- **有史料 / 访谈 / 原著依据**：不把网上流传的名言当作证据；
- **四层严格区分**：历史事实、作者原意、项目解释、现代转译；
- **明确适用和不适用**：不把某个人物的思维当作万能工具；
- **可检查工作流**：不是华丽口号，而是能在案例中执行；
- **有针对性评测**：既验证能力，也记录会失败的场景。

详细标准：[QUALITY_STANDARD.md](QUALITY_STANDARD.md)。

## 路线图

- **Phase 1 / Foundation** — 系列总仓库、公开目录、统一模板与 CI；梁启超作为首个参考项目。
- **Phase 2 / Evidence** — 通过真实问题、反例和历史资料修订梁启超 Skill。
- **Phase 3 / Marketing** — 叶茂中初版已发布，继续完成目标客户端行为评测和真实任务反馈。
- **Phase 4 / Research** — 开发陈寅恪 Skill，重点做材料互证与反证机制。
- **Phase 5 / Scale** — 多个 Skill 稳定后再考虑组合安装、路由与独立社区组织。

详见 [ROADMAP.md](ROADMAP.md)。

## 系列发布与自动关联

只维护 [catalog/skills.json](catalog/skills.json)，由工具生成中英文作品目录、人物系列标识与相关推荐。发布时统一同步 GitHub About。详见 [自动关联说明](docs/series-automation.md)。

## 参与贡献

欢迎提交真实任务、失败案例、史料修正和新人物提案。请先阅读 [贡献指南](CONTRIBUTING.md)，或通过 [GitHub Issue](https://github.com/constantin2088/chinese-thinkers-skills/issues) 提案。

我们不以关注数量、立场一致或文风相似度作为接受贡献的标准。

## 安全、版权与免责声明

- 独立开源项目，未获相关历史人物、家属或机构的授权或背书；不宣称代表人物本人。
- 不伪造引语，不替已故人物对其身后事件表达“真实观点”。
- 一手文本与现代版著作的版权可能不同；仓库不应未经许可复制受保护的整书材料。
- 不把历史概念当作现代政治宣传、歧视、恐吓、操纵或高风险专业建议的理由。

阅读 [SECURITY.md](SECURITY.md) 与 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。

---

**English:** This is an independent open-source series of research-grounded Agent Skills inspired by Chinese thinkers and practitioners. Each skill aims for a concrete and testable reasoning workflow, not historical impersonation. See the [English README](README.en.md).

**MIT License** · Maintainer: [@constantin2088](https://github.com/constantin2088)
