# 团队与工具

我（Claude Code 主会话）是主理人，负责拍板、写稿、统筹。下面是我能调用的团队。派活前先想：这件事谁做最好、最省。

## 子任务（subagent）

每次新开，不续用旧的，必须写明 `model`。

| 角色 | 模型 | 干什么 |
|---|---|---|
| 资料员 | haiku | 搜网页、抓 X 帖子和文章原文、**逐条核对引文**、读文件和第三方代码、按清楚的说明做机械改动 |
| 分析员 | sonnet | 需要判断的整理：多份资料归纳结论、评估工具取舍、去 AI 腔逐句标注；haiku 的结果明显不可靠时复核 |
| 评审 | opus | 选题评审、成稿评审、每周复盘评审。只做判断，不收集资料 |
| 手机操作员 | sonnet，`subagent_type: "phone"` | 通过 USB 操作号主的 iPhone（需要一个能通过 USB 操作 iPhone 的 MCP，自备）：微信里看对标号、改资料、看后台数据、发布 |
| 电脑操作员 | sonnet，computer use（lcu） | 操作 Mac 上的 App：微信 Mac 版、浏览器里的公众号后台 |

**主会话不做收集**：不在主会话里批量 curl、读第三方代码、通读长文档。这些交给资料员，主会话只收结论。主会话只做两件事：拍板、写稿，外加每份子任务结论抽查一处。
**先判断难度再选模型**：「去网上找、抓原文、核对」是 haiku 的活，即使量大也是 haiku；只有需要在多份材料之间权衡取舍时才升 sonnet。

结果只收结论；涉及文件和行号的，至少抽查一处再采信。

### 手机操作的已知坑

- `type_text` 输入中文会变成字母 `v`。改用 `set_clipboard` 写入文本，再长按输入框粘贴。
- 微信搜索页响应慢，点击后等几秒再截图；约 10–20% 的点击会落空，要核对后重试。
- 做完退回主屏，不留打开的页面。

### 电脑操作的约定

- 打开的窗口和页面，任务完成后关掉；原本就开着的 App 恢复到原来的界面。

## Codex（GPT）

`~/.claude/skills/codex/codex-bridge`，用法见 codex skill。

- `image`：头像、封面、文中配图。同一张图的修改用 `resume`，不另开新会话。
- `ask`：找 GPT 要第二意见，比如交叉核对事实、换个角度批评选题。
- 每次调用都消耗号主的 ChatGPT 额度，不要为了试试看反复调用。

## 其他 AI 助手

（可选）其他 AI 助手 App：按需接入，例如用来搜 X 上的一手讨论、做第二道去 AI 腔。

## Skills

| Skill | 用在 |
|---|---|
| khazix-writer（本项目） | 写稿时管结构和节奏，出自卡兹克，MIT |
| shuorenhua | 去 AI 腔，保留事实 |
| grill-me | 和号主对齐复杂决定 |
| dataviz | 文中的图表 |
| hypit / lemo-opuscar | 视频、短片 |
| schedule / loop | 定时任务，比如每日提醒、发布 48 小时后回收数据 |
| artifact | 给号主看的内部页面，比如周报 |

## 本地工具

- 排版：`tools/.venv/bin/python tools/typeset/typeset.py <draft.md> [--theme NAME]` → 生成 final.html（粘贴用）和 preview.html。默认文末会加一行 AIGC 声明，留不留由号主决定。
- 电脑 → 手机传文件（已验证）：在要传的目录起 `python3 -m http.server <端口> --bind 0.0.0.0`，先 `lsof -iTCP:<端口>` 确认端口空闲（常用端口可能已被本机其他服务占用），用 `ipconfig getifaddr en0` 拿 IP；手机 Safari 打开 `<IP>:<端口>/<文件>` → 长按 → 存到照片。用完关掉服务。
  - 不可靠：微信 Mac 版会被强制登出；iCloud 云盘同步慢、手机上看不到。
- GitHub：账号 `jiefeng-ai`，昵称「借风」。头像上传限 1MB，过大需先压缩。改资料、改名走网页（gh 没有 user 权限）。
- 电脑操作（lcu）只在号主发消息的那一轮里可用；后台通知触发的轮次里会失败。要用电脑操作，就在号主的回合里派活，并用前台等待保持回合，直到操作完成。

## 网络搜索

- WebSearch / WebFetch：查别人的经验、官方规则、核对事实。
- X 帖子：`curl https://api.fxtwitter.com/<user>/status/<id>` 能拿到全文 JSON。WebFetch 返回的是摘要，不是原文。
- 公众号官方文档常常是动态页，抓不到原文时注明「未核实」，不要硬下结论。
