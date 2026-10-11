# 系列关联：只维护一个作品目录

`catalog/skills.json` 是作品状态、仓库、统一 Topics、能力描述、推荐和系列入口的唯一编辑入口。README 的标记区由脚本生成；其他内容不覆盖。

## 新作品发布

1. 用 thinkers-skill-template 的 `scripts/new_skill.py` 生成草案。生成器附带系列标识、回链、推荐、同步工具和 README 同步工作流。
2. 完成研究、示例与测试，通过发布检查。此时生成文件仅是草案，不能把目录状态自动升级。
3. 用户授权后创建人物仓库。在总目录加入 repo、focus、topics，并把 status 改为 published。提交目录变更。
4. 总仓库 CI 检查目录；生成工作流自动更新中英文目录。人物仓库和模板每天读取总目录，更新 README 回链与相关推荐；也可手动运行 Actions。
5. 用已有 gh 管理登录执行 `python scripts/publish_series.py --apply`，一次同步已发布人物和模板的 Description、Website、Topics 与模板目录快照。该命令预览默认不写远端；合并现有 Topics，保留 README 标记外内容，并拒绝非本系列仓库。

GitHub 自动令牌只用于各仓库自己的 README 提交，不增加跨仓库长期密钥。About Topics 和 Website 需要管理权限，不能依靠普通 Actions GITHUB_TOKEN 自动完成；它们随上述发布命令一次完成。个人置顶和 Social Preview 仍是 GitHub UI 设置。不要将它们误称为全部无人值守。

## 手动刷新

```bash
python scripts/render_catalog.py
python scripts/publish_series.py
python scripts/publish_series.py --apply
```

发布命令先克隆工作副本、仅修改受管 README 区块和模板快照，然后快进推送；失败立即停止且不强推。目录已发布项的仓库必须实际存在。新作品按研究完成情况建仓，直接提供 SKILL.md，不需要 GitHub Releases。

## 首页发现入口

对希望优先展示的已发布作品，在唯一目录中添加可选 `discovery_rank` 正整数，数值越小越靠前，同一目录不得重复。省略该字段的作品仍显示在完整目录和安装列表；规划项目不能设置推荐排名。运行 `python scripts/render_catalog.py` 生成双语首页，不手改推荐名单。

人物仓库的相关推荐全部保留在折叠区，系列标识与总仓库回链保持可见，让具体用途、示例和安装命令更易发现。所有人物的共享同步脚本和模板中的同名脚本应保持一致，避免每日刷新恢复旧布局。修改共享脚本前核对是否存在仓库特有的改动，不覆盖未知修改。

发布状态不表示模型行为评测已经通过；新作品须提供至少10项行为用例，实际运行结果与未运行状态分别记录。

## 六类场景与同类推荐

同一份目录的 `discovery_paths` 定义场景，人物的 `discovery_path` 指向其中一个场景；`focus_en` 提供英文任务介绍。生成器据此更新中英文首页及 `docs/choose-a-skill.md`。人物页默认显示同场景中三个已发布方法，先按 `discovery_rank` 再按目录顺序，排除自己和规划项目；全部其他已发布人物仍保留在折叠区。

`python scripts/find_skill.py "研究"` 离线读取同一目录，列出匹配的人物、用途、仓库与安装命令，不执行安装。新增人物当前暂停；后续恢复时，先补齐实际资料、用例和发布验证，再登记元数据。

发布工具同时同步所有人物、模板及模板内的共享脚本。已知前版可以升级，仓库中特有的未知修改在任何文件写入前被拒绝，须检查后合并。原有正文不覆盖；日常工作流只改自己的 README 受管区块，About 仍由有管理权限的发布工具同步。
