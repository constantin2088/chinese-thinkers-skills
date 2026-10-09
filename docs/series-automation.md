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

发布命令先克隆工作副本、仅修改受管 README 区块和模板快照，然后快进推送；失败立即停止且不强推。目录已发布项的仓库必须实际存在。新作品的建仓和版本 Release 仍由维护者根据研究完成情况决定。
