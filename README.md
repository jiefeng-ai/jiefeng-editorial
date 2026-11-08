# 借风AI 编辑部

公众号「借风AI」的 Claude Code 编辑部配置：一份 CLAUDE.md、一份花名册、评审标准、去 AI 腔清单、写作规范和排版脚本。

> 这是第 1 天的版本（2026-11-08），还没经过真实数据验证，会随运营迭代更新。

## 用 Claude Code 搭一个

在一个空目录里启动 Claude Code，粘贴这一句：

```
照着 https://github.com/jiefeng-ai/jiefeng-editorial 帮我在当前目录搭一个公众号编辑部，把账号信息换成我的
```

需要自己准备：Claude Code 付费订阅。可选：一个能通过 USB 操作 iPhone 的 MCP（自备）、ChatGPT 账号和 Codex（生图）。

排版脚本依赖：`python3 -m venv tools/.venv && tools/.venv/bin/pip install -r tools/requirements.txt`。

## 目录

| 路径 | 内容 |
|---|---|
| `CLAUDE.md` | 账号、铁律、每日流程、目录 |
| `docs/team.md` | 子任务分工、模型选择、工具和已知坑 |
| `review/` | 七维评审标准、去 AI 腔清单、写作规范 |
| `topics/standards.md` | 选题标准 |
| `retro/lessons.md` | 第 1 天的教训，当作示例 |
| `data/metrics.csv` | 发布数据表头 |
| `tools/typeset/` | Markdown 转公众号 HTML 的排版脚本和主题 |
| `prompts/zero-threshold.md` | 不用 Claude Code 的零门槛版 |

`articles/`、`benchmarks/`、`brand/` 等随运营创建，仓库里没有。

## 零门槛版

不用 Claude Code，也有个零门槛的版本，手动一点，骨架一样（同内容见 `prompts/zero-threshold.md`）。

第一步，在 Claude 或 ChatGPT 里建一个项目，把下面这段规矩放进项目指令，这个项目里的对话就是你的主编。

```
# 编辑部规矩（精简版）
## 铁律
1. 第一人称是我本人。不编造我的经历、数据和感受。
   素材只有两个来源：真实做过的事，和我给你的记录。
2. 不洗稿、不搬运，引用注明出处。
3. 能查的事实去查，查不到就写「未核实」。
## 每次写稿
1. 先读我贴给你的「复盘」，照着避坑。
2. 写稿，交给我。
```

第二步，不要在同一个项目里开评审，它会继承主编的规矩。另开一个普通对话，贴上下面这段，再贴稿子。

```
你是公众号成稿评审，不认识作者。按下面 5 项各打 1–5 分：
1. 读者读完能做成什么？教程能不能照做？
2. 有什么是别处搜不到的？少于 2 条就不过。
3. 哪些句子像 AI 写的？逐句标出。
4. 读者会因为什么转发？标题和开头三行能不能让人读下去？
5. 有没有编造感？细节太顺、情绪太满、经历无法核实的都标出来。
最后给最重要的 3 条修改，具体到原句和改法，按收益排序。
```

第三步，你按评审意见改完、发出去，把这次的教训写成几行，存进一个「复盘」文档。下次写稿前，把它贴给主编。

## 致谢与许可

- 原创内容：MIT，见 `LICENSE`。内置的第三方部分保留各自的许可证。
- [khazix-writer](https://github.com/KKKKhazix/khazix-skills)，数字生命卡兹克，MIT。未内置，请从上游安装。
- 排版引擎来自 [wewrite](https://github.com/imraywang/wewrite)，MIT，已内置，许可证见 `tools/typeset/wechat_typeset/LICENSE-wewrite`。
- `review/ai-tone-checklist.md` 参考了 [humanizer](https://github.com/blader/humanizer)（Siqi Chen，MIT）、khazix-writer 和 [shuorenhua](https://github.com/MrGeDiao/shuorenhua)（MrGeDiao，MIT）。
