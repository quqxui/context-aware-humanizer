<p align="center">
  <img src=".github/banner.png" alt="Context-Aware Humanizer：中英文多场景写作 Skill" width="100%">
</p>

<h1 align="center">Context-Aware Humanizer｜中英文去 AI 味与多场景写作 Skill</h1>

<p align="center"><strong>让文字符合使用场景，也保留你的表达习惯。</strong></p>

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
  <a href="#examples">场景与示例</a> ·
  <a href="#personal-voice">个人表达</a> ·
  <a href="#installation">安装</a>
</p>

一个面向中文与英文的 Agent Skill，用于**去 AI 味、文本润色和语气调整**。从日常消息到学术论文，让表达更适合读者和用途。

<a id="core-features"></a>

- **12 个写作场景**：分别处理聊天、社交内容、工作沟通、文档和六类学术写作。
- **中英文独立规则**：每个场景各有语言指南和完整案例，可分别维护。
- **保留个人表达**：默认保留原文口气，也支持写作样本和可复用的表达档案。

<a id="quick-start"></a>

## ⚡ 快速使用

[加载 skill](#installation) 后，告诉助手用途和偏好，再贴上原文：

```text
用 context-aware-humanizer，把下面这段改成给导师发的中文微信。
礼貌、自然，保留“可能周五完成”，不要改成确定承诺：
[粘贴原文]
```

默认保留原文语言，返回一份可直接使用的正文；原文已经合适时可以不改。需要翻译、修改对照或多个版本，直接说明。

<a id="scenarios"></a>
<a id="examples"></a>

## ✍️ 12 个场景，12 组改写示例

每个场景选用不同原稿，展示措辞、语气或结构的变化。以下均为自拟示例，不代表实际研究结果或模型效果评测。展开可看前后对照与对应指南。

<details open>
<summary><strong>1. 日常聊天｜书面通知 → 朋友间的自然回复</strong></summary>

**原文**

> 关于周六一起吃饭的安排，我这边可能需要晚一点才能到达，因为下午还有一场会议需要参加。如果你先到了餐厅，可以先点菜，不必等待我到场。

**改写**

> 周六吃饭我可能会晚点到，下午还有个会。你要是先到了，就先点菜，不用等我。

指南：[中文](references/chat/zh.md) · [English](references/chat/en.md)

</details>

<details>
<summary><strong>2. 工作沟通｜背景铺陈 → 行动与期限优先</strong></summary>

**原文**

> 客户演示已安排在周五，因此还需要推进登录流程的回归测试工作，该项工作由小林负责，完成时间为周四 15:00 前。如在测试中遇到阻塞问题，也请在周四 17:00 前向我进行反馈。

**改写**

> 小林，请在周四 15:00 前完成登录流程的回归测试，支持周五的客户演示。如有阻塞问题，请在周四 17:00 前告诉我。

指南：[中文](references/work-message/zh.md) · [English](references/work-message/en.md)

</details>

<details>
<summary><strong>3. 小红书｜平铺记录 → 有细节、有重点的体验分享</strong></summary>

**原文**

> 上周日我下午两点去了河边那家咖啡店，在店内待了两小时。靠窗座位的光线让我觉得比较舒服，但插座只有吧台旁边有。我觉得这里适合带一本书坐坐，带电脑的话需要留意座位位置。

**改写**

> **河边咖啡店：窗边舒服，插座在吧台旁**
>
> 上周日下午两点去，坐了两小时。靠窗光线挺舒服，带本书来坐坐很合适。
>
> 带电脑的话留意一下座位：插座只在吧台旁边。

指南：[中文](references/xiaohongshu/zh.md) · [English](references/xiaohongshu/en.md)

</details>

<details>
<summary><strong>4. X / Twitter｜完整铺垫 → 简短鲜明的个人观点</strong></summary>

**原文**

> 在试用了三个笔记应用之后，我发现对我而言，影响使用体验的关键并不是功能数量的多少，而是在需要时能否快速找到此前记录的内容。因此，我现在选笔记应用时会先关注搜索功能。

**改写**

> 试了三个笔记应用，我现在先看搜索。对我来说，能快速找到旧笔记，比多几个功能更重要。

指南：[中文](references/x-post/zh.md) · [English](references/x-post/en.md)

</details>

<details>
<summary><strong>5. 微信公众号｜过程汇报 → 重点清楚、自然展开的短文</strong></summary>

**原文**

> 我们对团队过去一个月的周会进行了回顾，发现平均每次会议耗时约 50 分钟，其中有约 30 分钟被用于轮流汇报进度。因此，我们决定从下周开始尝试将进度更新放在会前文档中完成，并将会议时间用于讨论阻塞问题。这一安排将先试行两周，然后再决定是否继续采用。

**改写**

> 过去一个月，我们的周会平均每次约 50 分钟，其中约 30 分钟在报进度。
>
> 下周起，我们会试行两周：进度提前写进文档，会上讨论阻塞问题。试行结束后，再决定是否继续。

指南：[中文](references/wechat-article/zh.md) · [English](references/wechat-article/en.md)

</details>

<details>
<summary><strong>6. 说明文档｜操作描述 → 可直接执行的步骤</strong></summary>

**原文**

> 在开始执行数据校验任务之前，需要确保输入文件 `data.csv` 已经放置于当前目录中。在此前提下，通过执行 `sampletool validate data.csv --output report.json` 命令，即可对输入文件开展校验，并在校验成功后将报告输出至 `report.json` 文件。

**改写**

> 1. 将 `data.csv` 放到当前目录。
> 2. 运行 `sampletool validate data.csv --output report.json`。
>
> 校验成功后，报告写入 `report.json`。

指南：[中文](references/documentation/zh.md) · [English](references/documentation/en.md)

</details>

<details>
<summary><strong>7. 基金申请｜冗长目标陈述 → 问题、方法与验证计划</strong></summary>

**原文**

> 本项目计划围绕现有工业缺陷检测方法在少量标注条件下适应新产线能力不足的问题开展研究，拟通过引入未标注图像来减少对人工标注的依赖，并计划在三条产线上开展对比实验，以评估在保持检测准确率的条件下是否能够降低标注量。

**改写**

> 针对工业缺陷检测在少量标注下难以适应新产线的问题，本项目拟利用未标注图像，降低对人工标注的依赖。计划在三条产线上开展对比实验，检验该方法能否在保持检测准确率的同时减少标注量。

指南：[中文](references/grant-proposal/zh.md) · [English](references/grant-proposal/en.md)

</details>

<details>
<summary><strong>8. 学术讲稿｜书面实验描述 → 听众容易跟上的口头讲述</strong></summary>

**原文**

> 为明确检索模块是否是性能增益的主要来源，我们进行了移除该模块的消融实验。在相同测试集上，完整系统的任务成功率为 71%，移除检索模块后降至 59%，这一结果表明检索模块对当前系统有贡献。

**改写**

> 接下来，我们看检索模块是不是性能提升的主要来源。我们把它去掉，在同一测试集上做了对比。任务成功率从 71% 降到了 59%，说明检索模块对当前系统有贡献。

指南：[中文](references/academic-talk/zh.md) · [English](references/academic-talk/en.md)

</details>

<details>
<summary><strong>9. 学术 PPT｜结果段落 → 结论标题与数据要点</strong></summary>

**原文**

> 在 batch size 为 1、输入长度为 2,048 tokens 的测试中，缓存使单次请求的平均延迟从 1.8 秒降至 1.1 秒，峰值显存占用从 8.2 GB 增至 9.0 GB。

**改写**

> **缓存降低延迟，但增加显存占用**
>
> - 单次请求平均延迟：1.8 → 1.1 秒
> - 峰值显存：8.2 → 9.0 GB
>
> 测试条件：batch size = 1；输入长度 = 2,048 tokens。

指南：[中文](references/academic-slides/zh.md) · [English](references/academic-slides/en.md)

</details>

<details>
<summary><strong>10. 学术论文｜重复解说 → 紧凑、准确的结果分析</strong></summary>

**原文**

> 我们对所提出的方法进行评估后发现，在数据集 A 上，相同评估设置下的方法准确率为 86%，而基线的准确率为 82%。从这一对比可以看出，我们的方法在准确率上比基线高出 4 个百分点。

**改写**

> 在相同评估设置下，本方法在数据集 A 上的准确率为 86%，较基线的 82% 提高了 4 个百分点。

指南：[中文](references/academic-paper/zh.md) · [English](references/academic-paper/en.md)

</details>

<details>
<summary><strong>11. 审稿意见｜笼统批评 → 具体依据与修改要求</strong></summary>

**原文**

> 论文在实验报告方面还有比较明显的不足。表 2 只给出了单次运行的结果，没有报告不同随机种子下的波动情况，因此目前难以判断方法的提升是否稳定。我认为作者需要补充多个随机种子下的均值和标准差。

**改写**

> 表 2 只报告单次运行结果，尚不足以判断不同随机种子下的提升是否稳定。请补充多个随机种子下的均值和标准差。

指南：[中文](references/peer-review/zh.md) · [English](references/peer-review/en.md)

</details>

<details>
<summary><strong>12. 审稿回复｜辩解口吻 → 专业澄清与修改定位</strong></summary>

**原文**

> 审稿人认为我们遗漏了与方法 B 的对比，但实际上我们已经在表 3 中提供了该结果。可能是原文的表述不够清楚，导致这一点未被注意到。我们已在第 4.2 节补充文字，明确指向表 3，并说明两个方法采用相同训练预算。

**改写**

> 表 3 已包含与方法 B 的对比，两种方法使用相同训练预算。原文可能未充分说明这一点；我们已在第 4.2 节明确引用表 3，并说明训练预算设置。

指南：[中文](references/reviewer-response/zh.md) · [English](references/reviewer-response/en.md)

</details>

<a id="voice-options"></a>
<a id="personal-voice"></a>

## 🎙️ 保留你的表达习惯

可以直接说“先说需要对方做什么”“保留不同意见，措辞礼貌”或“口语一点，不加客套话”。也可以提供自己的样本：

```text
下面是我自己写的两段话，只参考表达方式，不沿用其中的事实：
[写作样本]

请按这个口气改写下面的工作消息：
[原稿]
```

**当前任务要求优先；样本只提供风格，不提供新稿的事实。** 普通改写不会保存偏好。需要长期复用时，可以提供已有档案，或明确要求：

```text
把这些样本中的表达习惯保存为“中文工作消息”记忆，供以后使用。
只提取我写的段落；不要保存来源事实，证据不足的偏好标为暂定。
```

想先检查时，把“保存”改为“只预览，不保存”。详见[记忆指南](references/style-memory.md)与[档案模板](templates/style-memory.md)。

<a id="installation"></a>

## 🛠️ 安装

```bash
git clone https://github.com/quqxui/context-aware-humanizer.git
```

1. **本地试用**：让助手读取 [`SKILL.md`](SKILL.md)，再按指引读取对应场景和语言的指南。
2. **安装复用**：将 `SKILL.md`、`references/`、`scripts/` 和 `templates/` 一起复制到助手的 skill 目录，保留相对结构。
3. **启用可选记忆**：需要可写安装目录和 Python 3.9+。普通文本改写只依赖 Markdown 指南。

表达记忆保存在该安装目录的私有 `memory/` 中；普通改写只读取同语言的通用及对应场景档案。不同安装之间不会自动同步。

<details>
<summary><strong>导出、备份与更新</strong></summary>

以下命令中的 `<skill-root>` 为安装目录；输出路径须指向安装目录外的新文件。

```bash
python3 <skill-root>/scripts/skill_package.py export --output /outside/context-aware-humanizer.zip
python3 <skill-root>/scripts/skill_package.py backup --output /outside/context-aware-humanizer-private.zip
python3 <skill-root>/scripts/skill_package.py update --source /path/to/new-skill
```

- `export`：导出公共安装包，排除个人记忆和本地文件。
- `backup`：生成包含记忆及历史版本的私有备份。
- `update`：更新受维护的程序文件，保留目标安装中的记忆。

公共 Git 不包含个人记忆。第三方安装器仍可能移除数据；更新前可先备份。文档读取由宿主助手完成，存储脚本只保存提取出的风格。

</details>

## 范围与许可

本 skill 只改写用户提供的文本，不连接平台、抓取、发布或提交内容。它不核查事实，不提供“AI 含量”分数或检测通过保证；目前尚未完成系统性的跨模型效果评测。

欢迎贡献场景、示例或可复现的失败案例，见[贡献说明](CONTRIBUTING.md)。原创内容采用 [MIT License](LICENSE)，外部材料归各自作者所有。
