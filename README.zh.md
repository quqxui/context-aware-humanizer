<p align="center">
  <img src=".github/banner.png" alt="Context-Aware Humanizer：中英文多场景写作 Skill" width="100%">
</p>

<h1 align="center">Context-Aware Humanizer｜中英文去 AI 味与多场景写作 Skill</h1>

<p align="center">
  让文字符合使用场景，也保留你的表达习惯。<br>
  微信聊天、社交平台、学术写作——中文与英文，各有自己的规则和示例。
</p>

<p align="center">
  <a href="#scenarios"><img src="https://img.shields.io/badge/Languages-English%20%2B%20Chinese-24544F?style=flat-square" alt="Languages: English + Chinese"></a>
  <a href="#scenarios"><img src="https://img.shields.io/badge/Scenarios-12-24544F?style=flat-square" alt="Scenarios: 12"></a>
  <a href="#personal-voice"><img src="https://img.shields.io/badge/Voice-Personal-B96543?style=flat-square" alt="Voice: Personal"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-69717C?style=flat-square" alt="License: MIT"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <strong>简体中文</strong>
</p>

<p align="center">
  <a href="#quick-start">快速使用</a> ·
  <a href="#scenarios">场景目录</a> ·
  <a href="#voice-options">语气选择</a> ·
  <a href="#personal-voice">个人表达</a> ·
  <a href="#installation">安装</a>
</p>

---

一个面向中文与英文的 Agent Skill，用于**去 AI 味、说人话、文本润色、改写、措辞校对、语气调整与个人风格保留**。适用于微信聊天、小红书笔记、X / Twitter 帖子、公众号文章、技术文档、基金申请、论文润色、学术讲稿、PPT 文本、审稿意见和审稿回复。

> **只负责文本润色。** 本 skill 润色和改写你提供的文本。场景名称表示写作语气和格式，不代表可访问对应平台。它不提供微信、小红书、X、投稿系统等服务的 API 或访问接口，也不负责抓取、发布或提交内容。

<a id="core-features"></a>

## 核心 Features

- **按场景改写** — 12 个场景分别维护规则和案例。其中 6 个学术场景覆盖基金申请、讲稿、PPT、论文、审稿意见与审稿回复。

- **中英文独立** — 每个场景各有 `zh.md` 和 `en.md`，包含各自的规则和示例。改中文只看中文，改英文只看英文，无需同步修改另一份。

- **保留个人表达** — 默认保留原文口气；也可以选 6 种语气、提供自己的写作样本，或使用可编辑的个人档案。下方都有可直接参考的例子。

默认保持原文语言。只有明确要求翻译或中英对照时，才输出另一种语言。

<a id="examples"></a>

## 同一组记录，写给不同场景

**原始记录：** 数据集 A 的同一测试集：本方法准确率 86%，基线 82%；其他数据集未评估。

| 用途 | 改写示例 |
|---|---|
| **学术讲稿** | 先看数据集 A 的结果：在同一测试集上，本方法的准确率是 86%，基线是 82%。其他数据集还没评估。 |
| **学术 PPT** | **数据集 A 测试集：准确率**<br>本方法 86% · 基线 82%<br>其他数据集：尚未评估 |
| **学术论文** | 在数据集 A 的同一测试集上，本方法的准确率为 86%，基线为 82%。尚未评估其他数据集。 |

结构和措辞随用途调整，**事实、条件和结论力度保持不变**。例如，“如果负责人今天批准，我可能周五前给你一版草案”可以写得自然些，但不能变成“我周五给你”。

<a id="quick-start"></a>

## ⚡ 快速使用

[加载 skill](#installation) 后，直接说清楚用途、语言、对象和偏好，**不需要记参数或填写问卷**。

**给导师发微信**

```text
用 context-aware-humanizer，把下面这段改成给导师发的中文微信。
礼貌、自然，保留“可能周五完成”，不要改成确定承诺：
……
```

**润色英文审稿回复**

```text
用 context-aware-humanizer 润色下面这封英文审稿回复。
保留明确的不同意见，语气专业，不增加实验或修改记录：
……
```

**压缩成一页学术 PPT**

```text
把下面结果改成一页中文学术 PPT：一个标题、两条要点。
保留测试条件、指标和局限：
……
```

这些是发给助手的自然语言请求，不是终端命令。默认返回一份可直接使用的正文；需要修改对照、多个版本或只标问题时，直接说。**原文已经合适，可以不改。**

<a id="scenarios"></a>

## 📚 场景目录

**先选场景，再选语言。** 每份文件都有该语言的规则和 **两类完整案例**，按“需求 → 原文 → 改写 → 说明”展示。

| 场景 | 适用内容与重点 | 中文 | English |
|---|---|:---:|:---:|
| **日常聊天** | 微信、私聊；关系、口语、条件与承诺 | [中文](references/chat/zh.md) | [English](references/chat/en.md) |
| **工作沟通** | 邮件、跟进、进度；事项、责任人、时间 | [中文](references/work-message/zh.md) | [English](references/work-message/en.md) |
| **小红书** | 经验、教程、产品信息；来源与真实经历 | [中文](references/xiaohongshu/zh.md) | [English](references/xiaohongshu/en.md) |
| **X / Twitter** | 单条、长帖、回复；观点与上下文 | [中文](references/x-post/zh.md) | [English](references/x-post/en.md) |
| **微信公众号** | 科普、评论、通知；连贯展开与文章类型 | [中文](references/wechat-article/zh.md) | [English](references/wechat-article/en.md) |
| **说明文档** | README、教程；步骤、输入输出、技术精度 | [中文](references/documentation/zh.md) | [English](references/documentation/en.md) |
| **基金申请** | 研究计划、立项依据；问题、论证、可行性 | [中文](references/grant-proposal/zh.md) | [English](references/grant-proposal/en.md) |
| **学术讲稿** | 组会、报告、答辩；听众背景、口播与转场 | [中文](references/academic-talk/zh.md) | [English](references/academic-talk/en.md) |
| **学术 PPT 文本** | 标题、要点、图表说明；主旨与必要条件 | [中文](references/academic-slides/zh.md) | [English](references/academic-slides/en.md) |
| **学术论文** | 摘要、方法、结果、讨论；术语、证据与限定 | [中文](references/academic-paper/zh.md) | [English](references/academic-paper/en.md) |
| **审稿意见** | 润色已有评审；具体问题、依据与批评力度 | [中文](references/peer-review/zh.md) | [English](references/peer-review/en.md) |
| **审稿回复** | 会议 rebuttal、期刊返修；逐条回应与实际进展 | [中文](references/reviewer-response/zh.md) | [English](references/reviewer-response/en.md) |

文档中的案例均为自拟，用于说明写法，不代表实际研究结果或模型效果评测。

<a id="voice-options"></a>

## 🎙️ 语气由你选择

默认 **保留原文口气**。想调整时，直接说“温和一点”“正式但直接”，或使用下表中的名称。想先看效果，可以这样问：

```text
用 context-aware-humanizer，展示可选语气。
选一段有足够上下文的中文，展示真正有用的差别；原文已合适的版本可以不改。
```

**已经合适的短消息**

> 请周五前把修订版简报发来，方便我们在上线前完成审核。

选择 **自然** 时，原文可以直接保留。为了凑出差异而换近义词、加“谢谢！”或感叹号，并不会让这条请求更好。其余语气只在受众和用途需要时使用，不必把每句话都改成六个版本。

**有实际选择空间的对比**

> **原文：** 新版搜索流程的演示安排在周四 15:00，届时会介绍新增的筛选选项。请在周三前发来问题；会议链接在日历邀请里。

| 语气 | 改写示例 | 调整点 |
|---|---|---|
| **自然 · natural** | 新版搜索流程的演示安排在周四 15:00，届时会介绍新增的筛选选项。请在周三前发来问题；会议链接在日历邀请里。 | 原文已经合适。 |
| **直接 · direct** | 新版搜索流程演示：周四 15:00，介绍新增筛选选项。问题请在周三前发来；会议链接见日历邀请。 | 时间和动作集中在前面，适合群内同步。 |
| **正式 · formal** | 新版搜索流程演示定于周四 15:00，内容包括新增的筛选选项。请于周三前发送问题，会议链接见日历邀请。 | 语体更正式，但没有堆叠公文词。 |
| **轻快 · lively** | 周四 15:00，我们来演示新版搜索流程和新增的筛选选项。有问题的话，周三前发来；链接在日历邀请里。 | 调整句子节奏，不靠感叹号制造活泼感。 |

四个版本都保留演示时间、内容、提问截止时间和链接位置。**温和**、**克制** 仍可按具体场景选择。语气选择仅用于本次改写，**不会自动成为长期偏好**。

<a id="personal-voice"></a>

## 保留你自己的表达

| 方式 | 你提供什么 | 如何使用 |
|---|---|---|
| **保留原文口气**（默认） | 原稿 | 清理不自然的表达，保留原有语气 |
| **参考自己的样本** | 一两段或更多自己写的文字 | 本次任务参考句长、措辞、标点和节奏 |
| **使用个人表达档案** | 你明确提供或选择的 Markdown 档案 | 复用可查看、可修改的偏好 |

### 给样本，直接改写

```text
下面是我自己写的，只参考表达方式，不沿用其中的事实。
样本一：图已经改好了，还差最后一遍检查。今天先别发。
样本二：先给结论：这个版本能用，但还有两处要改。

请按这个口气改写下面的工作消息：
由于数据导出失败，报告无法按原计划发送。
如果今天恢复导出，我预计可以在明天发出初稿。
```

**改写示例：** 导出失败了，报告没法按原计划发。如果今天恢复导出，我预计明天能发初稿。

参考的是短句和直接交代进展的习惯。样本里的“图”“两处要改”不带入新消息，原稿中的条件和“预计”继续保留。

### 想复用偏好，再建立档案

个人档案是可选的。可以自己填写，也可以让助手根据样本整理：

```text
根据这些样本整理一个可编辑的个人表达档案。
中文和英文偏好分开列，拿不准的留空。
先展示档案和一个改写例子，不要自动保存。
```

<details>
<summary><strong>展开：可复制的档案模板、填写示例和使用方法</strong></summary>

所有字段可选，只保留你想复用的内容。

```markdown
# 我的表达偏好

## 使用范围
- 适用场景：未指定

## 中文
- 语气、句长：未指定
- 称呼、标点、格式：未指定
- 希望保留或避免的表达：未指定
- 自己的写作样本：可选

## English
- 语气、句长：未指定
- 称呼、标点、格式：未指定
- 希望保留或避免的表达：未指定
- 自己的写作样本：可选
```

**填写示例（虚构）：**

```markdown
# 我的表达偏好

## 使用范围
- 仅用于中文工作进度消息。

## 中文
- 先交代进展，再说明限制；以短句为主。
- 不加感叹号，保留原文中的“预计”“可能”。

## English
- 未指定。
```

**套用示例：** “当前导出任务尚未结束，因此我们目前还无法发送报告。” → “导出任务还没结束，我们现在还不能发报告。”

下次把档案交给助手，说“按这个档案改写下面的工作消息”即可。档案可以放在 skill 目录之外。未指定的字段无需追问。

</details>

**当前任务要求优先于档案；样本和档案只提供风格，不提供新稿的事实。** 普通改写不需要建档案。skill 不会自动保存、更新档案或训练模型；保存档案需要你明确提出。宿主产品如何保存聊天记录不由本 skill 控制。

<a id="installation"></a>

## 安装与文件结构

这是一个由 Markdown 文件组成的 skill。具体加载方式取决于你使用的助手或工具。

下载仓库，或使用 Git 克隆：

```bash
git clone https://github.com/quqxui/context-aware-humanizer.git
```

1. **本地试用：** 让支持读取本地文件的助手读取本仓库的 [`SKILL.md`](SKILL.md)，再按其中的指引读取对应场景与语言文件。
2. **安装使用：** 如果宿主支持 skill，将 **`SKILL.md` 和 `references/`** 放入其指定的 skill 目录，保留相对结构。
3. **开始改写：** 发送上面的[自然语言请求](#quick-start)，附上原文。

README 和横幅仅用于展示，不需要随 skill 一起加载。

<details>
<summary><strong>查看目录结构与维护方式</strong></summary>

```text
context-aware-humanizer/
├── SKILL.md                 # 执行入口与共用规则
├── README.md                # English
├── README.zh.md             # 简体中文
├── .github/
│   └── banner.png           # README 展示图片
└── references/
    ├── chat/                # 每个场景均有 zh.md 和 en.md
    ├── work-message/
    ├── xiaohongshu/
    ├── x-post/
    ├── wechat-article/
    ├── documentation/
    ├── grant-proposal/
    ├── academic-talk/
    ├── academic-slides/
    ├── academic-paper/
    ├── peer-review/
    └── reviewer-response/
```

例如，中文论文看 **[`references/academic-paper/zh.md`](references/academic-paper/zh.md)**，英文论文看 **[`references/academic-paper/en.md`](references/academic-paper/en.md)**。每份文件包含本语言的规则和示例，可以单独维护，**无需为了改一份而同步另一份**。

通用的原意保留规则、场景选择、语气和个人档案的使用方式放在 **[`SKILL.md`](SKILL.md)**；用户可查看的选项、模板和例子就在 README 中。

</details>

---

## 验证与边界

验证重点是 **原意保留、场景适配、自然程度、避免过度修改**。文档示例不计作实际测试结果；目前尚未完成系统性的跨模型评测。

skill 不判断文本由谁写成，不提供“AI 含量”分数或检测通过保证。润色不会自动完成事实核查、研究、补实验、发布内容或提交文稿。学术场景以具体资助方、期刊或会议的要求为准。

## 贡献与许可

欢迎贡献一个具体场景、一份中文或英文示例，或一个可复现的失败案例。见 **[贡献说明](CONTRIBUTING.md)**。

本仓库原创内容采用 **[MIT License](LICENSE)**。外部链接内容仍归各自作者所有。
