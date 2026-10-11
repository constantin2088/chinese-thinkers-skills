# 安装与第一次使用 / Installation

每个人物仓库提供一个独立 Skill。总仓库提供目录和维护工具，先选一个当前有用的方法即可。

## 1. 先查看，再安装

```bash
# 只列出，不安装
npx skills add constantin2088/wang-yangming-action-skill --list

# 安装一个方法，按提示选择客户端
npx skills add constantin2088/wang-yangming-action-skill
```

需要 Node.js 与 npm/npx。CLI 支持的客户端与参数以 [vercel-labs/skills](https://github.com/vercel-labs/skills) 当前说明为准。常规安装使用项目范围；需要全局安装或指定客户端时，先核对其参数和实际目录。不要把一百个人物一次全部装入当前项目作为必需步骤。

也可按客户端文档，把人物仓库放入 Skill 目录：保留匹配名称的文件夹、根目录 `SKILL.md`、资料和脚本。复制文件并不保证客户端已经加载。

## 2. 给它一个具体任务

说明背景、已有证据、约束和希望交付的成果。[四个可复制的任务](try-it.md)帮助起步；每个人物仓库还有自己的示例和边界。若没有自动加载，可按客户端支持的方式明确调用对应 Skill。

## 3. 分清三个状态

| 状态 | 能证明什么 |
|---|---|
| `--list` 找到正确名称 | 安装工具可以发现此 Skill |
| 安装结束，文件出现在目标目录 | 该客户端目录已有文件，仍须检查加载 |
| 客户端调用、输出符合验收与资料边界 | 这一次实际任务的行为可以被检查 |

系列已经核验安装发现。独立客户端的模型行为评测尚未执行，不能把发现、单元测试或 CI 写成真实模型任务已经通过。模型与客户端版本会影响行为，按实际结果反馈。

<a id="find-a-method"></a>

## 按关键词找方法

直接使用[六类场景指南](choose-a-skill.md)。已经下载总仓库的使用者也可离线查询同一目录：

```bash
python scripts/find_skill.py "王阳明"
python scripts/find_skill.py "备份 行动"
python scripts/find_skill.py "hypothesis"
```

工具显示人物、用途、仓库和安装命令，不联网、不自动安装；只返回已发布作品，使用名称与任务字段的关键词匹配。

## English

Run `npx skills add owner/repository --list` to discover a skill without installing it. Run the command without `--list` to select a client and install it. The [official CLI README](https://github.com/vercel-labs/skills) documents scope and client options. Each thinker repository contains its own root `SKILL.md`; this index is not a combined skill. Most instructions and examples are Chinese. Installation discovery and actual client execution are distinct; independent-client model behavior has not been evaluated.
