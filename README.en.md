<div align="center">

<img src="assets/banner.svg" width="900" alt="Chinese Thinkers as Skills" />

# Chinese Thinkers as Skills

### Not personas. Executable wisdom.

Research-grounded, testable AI Agent Skills inspired by methods of Chinese thinkers, scholars, and practitioners.

[中文](README.md) · [Catalog](#catalog) · [Install](#installation) · [Quality Standard](QUALITY_STANDARD.md) · [Contribute](CONTRIBUTING.md)

</div>

## Why this exists

A historical figure should not become a simulated authority on modern events. Instead, we turn **documented reasoning approaches** into transparent, limited and testable workflows.

Each released Skill should include a distinct method, credible source map, explicit trigger, examples, failure cases and boundaries. A shared project style does *not* mean the thinkers share one generic decision template.

## Catalog

<!-- CATALOG:START -->
| Thinker | Focus | Repository | Status |
|---|---|---|---|
| **Liang Qichao** | 变局判断、能力更新、认知修正 | [liang-qichao-skill](https://github.com/constantin2088/liang-qichao-skill) | Released |
| **Ye Maozhong** | 消费冲突、产品表达、增长实验 | [ye-maozhong-skill](https://github.com/constantin2088/ye-maozhong-skill) | Released |
| **Chen Yinke** | 史料互证、证据分层、研究推断 | chen-yinke-research-skill | Planned |
| **Cai Yuanpei** | 异见管理、观点协调、多元协作 | cai-yuanpei-skill | Planned |
| **Song Zhiping** | 经营决策、精细管理、组织效率 | song-zhiping-management-skill | Planned |
| **Cho-yun Hsu** | 系统观察、跨学科分析、长期演化 | xu-zhuoyun-systems-skill | Planned |

Only published entries are installable.

```bash
npx skills add constantin2088/liang-qichao-skill
npx skills add constantin2088/ye-maozhong-skill
```
<!-- CATALOG:END -->

## Installation

```bash
npx skills add constantin2088/liang-qichao-skill
```

Sample prompt:

> Use the Liang Qichao skill to examine whether AI is changing the underlying rules of my profession. Separate durable advantages from obsolete habits and propose a reversible 60-day experiment.

Runtime behavior differs across agents; see [installation notes](docs/installation.md).

## Our standards

- Distinguish **historical fact / documented view / project interpretation / modern transfer**.
- Avoid invented quotations and statements on posthumous events.
- Never claim a thought framework applies to every problem.
- Prefer transparent methods over stylistic imitation.
- Evaluate on realistic tasks and adverse test cases.
- Respect copyright and modern professional / political boundaries.

Read the [quality standard](QUALITY_STANDARD.md) and [roadmap](ROADMAP.md). Contributions are welcome: [CONTRIBUTING.md](CONTRIBUTING.md).

**MIT licensed** · Maintained by [@constantin2088](https://github.com/constantin2088).
Series links and repository metadata derive from catalog/skills.json; see [automation](docs/series-automation.md).
