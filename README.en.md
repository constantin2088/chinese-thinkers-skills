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

| Thinker | Focus | Repository | Status |
|---|---|---|---|
| **Liang Qichao** | Transition, capability renewal, belief revision | [liang-qichao-skill](https://github.com/constantin2088/liang-qichao-skill) | **Released** |
| **Ye Maozhong** | Consumer tension, brand positioning, growth | ye-maozhong-skill | Planned |
| **Chen Yinke** | Research evidence, source corroboration | chen-yinke-research-skill | Planned |
| **Cai Yuanpei** | Pluralism, diverse viewpoints, collaboration | cai-yuanpei-skill | Planned |
| **Song Zhiping** | Enterprise strategy, management, efficiency | song-zhiping-management-skill | Planned |
| **Cho-yun Hsu** | Systems history and multidisciplinary change | xu-zhuoyun-systems-skill | Planned |

Planned repositories do not yet exist. Only the released skill is installable. Track structured records in [catalog/skills.json](catalog/skills.json).

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