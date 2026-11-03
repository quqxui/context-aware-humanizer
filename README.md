# Context-Aware Humanizer｜多场景写作润色

让文字符合使用场景，也保留作者的表达习惯。

用于去 AI 味、文本润色和语气调整。提供 12 个独立场景，每个场景有明确的输出语言、处理流程和改写示例。中文场景面向日常沟通、内容写作和基金申请；英文场景面向论文、审稿意见和审稿回复。学术讲稿与学术 PPT 各有独立的中文场景和英文场景。

[快速使用](#quick-start) · [场景与示例](#scenarios) · [个人表达](#personal-voice) · [安装](#installation)

<a id="quick-start"></a>

## 快速使用

[加载 skill](#installation) 后，说明场景和要求，再提供原稿：

```text
用 context-aware-humanizer 的“工作沟通”场景润色这条中文消息。
先说需要对方做什么，保留原来的负责人、期限和不确定性。
```

也可以直接指定独立的学术场景：

```text
用“学术讲稿中文”场景润色下面这段组会讲稿，保留图号和实验范围。
```

```text
用“学术讲稿英文”场景润色下面这段英文报告讲稿，适合口头表达，保留结论的限定条件。
```

默认只返回所选场景的一份正文，不附另一种语言版本。原稿已合适时可以保留。需要翻译时，明确说明目标语言；中文原稿不会因主题是论文而自动翻成英文。未列出的语言或用途只使用共同润色规则。

<a id="scenarios"></a>
<a id="examples"></a>

## 场景与示例

| 编号 | 场景 | 输出语言 | 处理重点 |
|---|---|---|---|
| 1 | [日常聊天](references/chat.md) | 中文 | 关系、答复、安排与边界 |
| 2 | [工作沟通](references/work-message.md) | 中文 | 动作、负责人、期限与依赖 |
| 3 | [小红书](references/xiaohongshu.md) | 中文 | 具体经历、资料来源与使用限制 |
| 4 | [微信公众号](references/wechat-article.md) | 中文 | 主旨、段落展开与结论范围 |
| 5 | [基金申请](references/grant-proposal.md) | 中文 | 研究问题、计划目标与已有基础 |
| 6 | [学术讲稿中文](references/academic-talk-zh.md) | 中文 | 中文口头节奏、图表指引与科学限定 |
| 7 | [学术讲稿英文](references/academic-talk-en.md) | 英文 | 英语口头表达、过渡与科学限定 |
| 8 | [学术 PPT 中文](references/academic-slides-zh.md) | 中文 | 中文标题、数据要点与展示顺序 |
| 9 | [学术 PPT 英文](references/academic-slides-en.md) | 英文 | 英文标题、要点语法与展示顺序 |
| 10 | [学术论文](references/academic-paper.md) | 英文 | 学术表达、证据范围与 LaTeX 保真 |
| 11 | [审稿意见](references/peer-review.md) | 英文 | 问题依据、严重程度与审稿建议 |
| 12 | [审稿回复](references/reviewer-response.md) | 英文 | 逐点回应、证据位置与修改状态 |

以下为自拟示例，不代表实际研究结果或模型效果评测。英文场景使用英文原文与改写；场景说明统一使用中文。

<details open>
<summary><strong>1. 日常聊天｜公文口吻 → 朋友间的自然回复</strong></summary>

**原文**

> 关于周六共同用餐一事，现将本人行程安排告知如下：鉴于当日下午另有会议需参加，本人存在延迟抵达餐厅的可能。如你先行抵达，可先行点餐，无需以本人到场作为前提。

**改写**

> 周六吃饭我可能会晚点到，下午还有个会。你要是先到了，就先点菜，不用等我。

处理流程与完整案例：[日常聊天](references/chat.md)

</details>

<details>
<summary><strong>2. 工作沟通｜随手交代、重点分散 → 行动与期限优先</strong></summary>

**原文**

> 周五要给客户做演示，登录流程还得回归一下。小林，这个你来负责。测试里要是碰到卡住的地方，记得告诉我，周四 17:00 前要反馈。对了，前面说的回归测试本身要在周四 15:00 前完成，别和反馈问题的时间弄混了。

**改写**

> 小林，请在周四 15:00 前完成登录流程的回归测试，支持周五的客户演示。如有阻塞问题，请在周四 17:00 前告诉我。

处理流程与完整案例：[工作沟通](references/work-message.md)

</details>

<details>
<summary><strong>3. 小红书｜现场记录口吻 → 有细节的个人体验</strong></summary>

**原文**

> 本次到访对象为河边咖啡店，到访时间为上周日 14:00，停留时长为两小时。关于座位环境，本人对靠窗座位的光线感受较为舒适；关于供电设施，插座分布范围仅限吧台旁。综合上述情况，本人认为该场所适宜携带书籍停留，携带电脑的情况下则需关注座位与插座的位置关系。

**改写**

> **河边咖啡店：窗边舒服，插座在吧台旁**
>
> 上周日下午两点去，坐了两小时。靠窗光线挺舒服，带本书来坐坐很合适。
>
> 带电脑的话留意一下座位：插座只在吧台旁边。

处理流程与完整案例：[小红书](references/xiaohongshu.md)

</details>

<details>
<summary><strong>4. 微信公众号｜内部汇报口吻 → 重点清楚的公众号短文</strong></summary>

**原文**

> 经对团队过去一个月周会开展复盘，现就有关情况及后续安排汇报如下：单次周会平均耗时约 50 分钟，其中轮流汇报进度环节占用约 30 分钟。基于上述情况，决定自下周起对周会组织形式作出调整，将进度更新环节前置至会前文档，将会中时间用于阻塞问题讨论。有关安排先行试行两周，届时再就是否继续采用作出决定。

**改写**

> 过去一个月，我们的周会平均每次约 50 分钟，其中约 30 分钟在报进度。
>
> 下周起，我们会试行两周：进度提前写进文档，会上讨论阻塞问题。试行结束后，再决定是否继续。

处理流程与完整案例：[微信公众号](references/wechat-article.md)

</details>

<details>
<summary><strong>5. 基金申请｜口头讨论草稿 → 正式的研究目标与验证计划</strong></summary>

**原文**

> 现在做工业缺陷检测，一到新产线，标注图像又少，现有方法就不太适应。我们的想法是试试能不能把没标注的图像也用起来，少依赖一些人工标注。打算找三条产线做对比实验，看看能不能在检测准确率不降的情况下，把标注量减下来。

**改写**

> 针对工业缺陷检测在少量标注下难以适应新产线的问题，本项目拟利用未标注图像，降低对人工标注的依赖。计划在三条产线上开展对比实验，检验该方法能否在保持检测准确率的同时减少标注量。

处理流程与完整案例：[基金申请](references/grant-proposal.md)

</details>

<details>
<summary><strong>6. 学术讲稿中文｜论文式长句 → 听众容易跟上的讲述</strong></summary>

**原文**

> 围绕检索模块是否构成性能增益主要来源这一问题，本研究通过移除该模块开展消融实验，并在与完整系统相同的测试集上进行评估，所得结果表现为任务成功率由完整系统配置下的 71% 下降至移除检索模块配置下的 59%，由此可见，检索模块对于当前系统的性能具有贡献。

**改写**

> 接下来，我们看检索模块是不是性能提升的主要来源。我们把它去掉，在同一测试集上做了对比。任务成功率从 71% 降到了 59%，说明检索模块对当前系统有贡献。

处理流程与完整案例：[学术讲稿中文](references/academic-talk-zh.md)

</details>

<details>
<summary><strong>7. 学术讲稿英文｜书面学术长句 → 适合英语口头讲述的段落</strong></summary>

**原文**

> An ablation experiment involving the removal of the retrieval module was conducted with the objective of determining whether this module constituted the principal source of the performance gain, with evaluation on the same test set yielding a reduction in task success from 71% under the full-system configuration to 59% under the configuration in which retrieval was absent, thereby indicating a contribution of the retrieval module to the performance of the current system.

**改写**

> Next, let's look at whether retrieval accounts for most of the gain. We removed the retrieval module and tested again on the same test set. Task success dropped from 71% to 59%, so retrieval does contribute to the current system's performance.

处理流程与完整案例：[学术讲稿英文](references/academic-talk-en.md)

</details>

<details>
<summary><strong>8. 学术 PPT 中文｜整段实验报告 → 中文标题与数据要点</strong></summary>

**原文**

> 本次测试是在 batch size 设置为 1、输入长度设置为 2,048 tokens 的条件下开展的。从测试结果来看，在单次请求的平均延迟这一指标上，使用缓存后对应的数值由 1.8 秒降低到了 1.1 秒；而在峰值显存占用这一指标上，使用缓存后对应的数值则由 8.2 GB 上升到了 9.0 GB。也就是说，在上述测试条件下，缓存的使用伴随着平均延迟的下降和峰值显存占用的增加。

**改写**

> **缓存降低延迟，但增加显存占用**
>
> - 单次请求平均延迟：1.8 → 1.1 秒
> - 峰值显存：8.2 → 9.0 GB
>
> 测试条件：batch size = 1；输入长度 = 2,048 tokens。

处理流程与完整案例：[学术 PPT 中文](references/academic-slides-zh.md)

</details>

<details>
<summary><strong>9. 学术 PPT 英文｜整段实验报告 → 英文标题与数据要点</strong></summary>

**原文**

> The tests were conducted with the batch size set to 1 and the input length set to 2,048 tokens. In terms of the mean latency per request, the use of caching was associated with a reduction in the measured value from 1.8 seconds to 1.1 seconds. In terms of peak GPU memory use, however, the measured value increased from 8.2 GB to 9.0 GB. Thus, under the stated test conditions, caching reduced mean latency per request while also increasing peak GPU memory use.

**改写**

> **Caching lowers latency but uses more GPU memory**
>
> - Mean latency per request: 1.8 → 1.1 seconds
> - Peak GPU memory: 8.2 → 9.0 GB
>
> Test conditions: batch size = 1; input length = 2,048 tokens.

处理流程与完整案例：[学术 PPT 英文](references/academic-slides-en.md)

</details>

<details>
<summary><strong>10. 学术论文｜随手实验笔记 → 准确的英文结果分析</strong></summary>

**原文**

> So, we ran our method on Dataset A and got 86% accuracy. The baseline got 82%, and yes, both were evaluated with the same setup. That's 4 percentage points in our favor. Basically, ours came out ahead on accuracy in this test.

**改写**

> Under the same evaluation setup on Dataset A, our method achieved 86% accuracy, exceeding the baseline's 82% by 4 percentage points.

处理流程与完整案例：[学术论文](references/academic-paper.md)

</details>

<details>
<summary><strong>11. 审稿意见｜生硬质问 → 有依据的专业审稿意见</strong></summary>

**原文**

> Table 2 gives us one run. Just one. Where is the variation across random seeds? Without that, I don't see how we're supposed to judge whether the improvement is stable. The authors need to report the mean and standard deviation across multiple random seeds.

**改写**

> Table 2 reports only a single run, leaving the stability of the improvement across random seeds unclear. Please report means and standard deviations across multiple random seeds.

处理流程与完整案例：[审稿意见](references/peer-review.md)

</details>

<details>
<summary><strong>12. 审稿回复｜防御性争辩 → 专业澄清与修改定位</strong></summary>

**原文**

> The reviewer says the comparison with method B is missing. But it is already in Table 3! We did include it, and both methods use the same training budget. Maybe our original wording did not make that clear enough. We have now added text in Section 4.2 explicitly pointing to Table 3 and stating that the training budget is the same for both methods.

**改写**

> Table 3 includes the comparison with method B under the same training budget. We may not have made this clear in the original text. We have revised Section 4.2 to point explicitly to Table 3 and clarify the matched training budget.

处理流程与完整案例：[审稿回复](references/reviewer-response.md)

</details>

<a id="voice-options"></a>
<a id="personal-voice"></a>

## 保留你的表达习惯

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

## 安装

```bash
git clone https://github.com/quqxui/context-aware-humanizer.git
```

1. **本地试用**：让助手读取 [`SKILL.md`](SKILL.md)，再读取所选独立场景的指南。
2. **安装复用**：将 `SKILL.md`、`references/`、`scripts/` 和 `templates/` 一起复制到助手的 skill 目录，保留相对结构。
3. **启用可选记忆**：需要可写安装目录和 Python 3.9+。普通文本改写只依赖 Markdown 指南。

表达记忆保存在该安装目录的私有 `memory/` 中；普通改写只读取所选场景的档案和同语言的通用档案。不同安装之间不会自动同步。

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

从旧版覆盖升级时，更新命令不会清理旧文件。先备份安装目录，再用新版完整替换 `references/`，移除旧版 `README.zh.md` 或 `README.en.md`；保留原有 `memory/`。已移除场景的旧记忆不会自动应用。

公共 Git 不包含个人记忆。第三方安装器仍可能移除数据；更新前可先备份。文档读取由宿主助手完成，存储脚本只保存提取出的风格。

</details>
