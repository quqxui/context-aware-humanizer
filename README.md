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
| 4 | [微信公众号](references/wechat-article.md) | 中文 | AI 论文讲述、实验解读与长文展开 |
| 5 | [基金申请](references/grant-proposal.md) | 中文 | 研究问题、计划目标与已有基础 |
| 6 | [学术讲稿中文](references/academic-talk-zh.md) | 中文 | 中文口头节奏、图表指引与科学限定 |
| 7 | [学术讲稿英文](references/academic-talk-en.md) | 英文 | 英语口头表达、过渡与科学限定 |
| 8 | [学术 PPT 中文](references/academic-slides-zh.md) | 中文 | 中文标题、数据要点与展示顺序 |
| 9 | [学术 PPT 英文](references/academic-slides-en.md) | 英文 | 英文标题、要点语法与展示顺序 |
| 10 | [学术论文](references/academic-paper.md) | 英文 | 学术表达、证据范围与 LaTeX 保真 |
| 11 | [审稿意见](references/peer-review.md) | 英文 | 问题依据、严重程度与审稿建议 |
| 12 | [审稿回复](references/reviewer-response.md) | 英文 | 逐点回应、证据位置与修改状态 |

以下初稿与改写均为编写的示例。微信公众号案例依据所引论文，实验结果归属于原论文。其余案例使用自拟材料。英文场景使用英文原文与改写，场景说明统一使用中文。

<details open>
<summary><strong>1. 日常聊天｜公文口吻 → 朋友间的自然回复</strong></summary>

**原文**

> 关于周六共同用餐一事，现将本人行程安排告知如下：鉴于当日下午另有会议需参加，本人存在延迟抵达餐厅的可能。如你先行抵达，可先行点餐，无需以本人到场作为前提。

**改写**

> 我周六下午还有个会，吃饭可能会晚点到，你先到了就先点菜，不用等我。

处理流程与完整案例：[日常聊天](references/chat.md)

</details>

<details>
<summary><strong>2. 工作沟通｜随手交代、重点分散 → 行动与期限优先</strong></summary>

**原文**

> 周五要给客户做演示，登录流程还得回归一下。小林，这个你来负责。测试里要是碰到卡住的地方，记得告诉我，周四 17:00 前要反馈。对了，前面说的回归测试本身要在周四 15:00 前完成，别和反馈问题的时间弄混了。

**改写**

> 小林，登录流程的回归测试请你在周四 15:00 前做完，周五要给客户做演示。如果测试中有问题卡住，也请在周四 17:00 前告诉我。

处理流程与完整案例：[工作沟通](references/work-message.md)

</details>

<details>
<summary><strong>3. 小红书｜现场记录口吻 → 有细节的个人体验</strong></summary>

**原文**

> 本次到访对象为河边咖啡店，到访时间为上周日 14:00，停留时长为两小时。关于座位环境，本人对靠窗座位的光线感受较为舒适；关于供电设施，插座分布范围仅限吧台旁。综合上述情况，本人认为该场所适宜携带书籍停留，携带电脑的情况下则需关注座位与插座的位置关系。

**改写**

> 上周日下午两点去了河边那家咖啡店，在里面坐了两个小时。靠窗的光线挺舒服，感觉带本书来坐坐很合适，不过带电脑的话得留意座位，插座只有吧台旁边才有。

处理流程与完整案例：[小红书](references/xiaohongshu.md)

</details>

<a id="wechat-ai-case"></a>

<details>
<summary><strong>4. 微信公众号｜综述式初稿 → 讲述一篇 AI 论文</strong></summary>

本例根据 Nelson F. Liu 等人的《Lost in the Middle: How Language Models Use Long Contexts》编写。初稿与改写均为中文转述与重组，实验设置和数据来自原论文。论文发表于 TACL 2024，采用 CC BY 4.0 许可。[论文与作者信息](https://aclanthology.org/2024.tacl-1.9/) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

**需求**

把下面的综述式初稿改成面向 AI 领域读者的公众号长文。围绕论文的问题和实验展开讲述，保留技术细节、数字、出处与原稿中的阅读判断。可以调整标题和段落，完整讲清楚，不压缩成摘要。

**原文**

> **《Lost in the Middle》论文内容综述**
>
> **研究背景与问题定义**
>
> 随着语言模型上下文窗口长度的增加，其在长文档问答与检索增强生成等场景中的应用受到关注。上下文窗口决定了单次输入所允许包含的文本长度，而模型在这些文本中查找和使用信息的能力需要通过任务表现进行考察。Nelson F. Liu 等人的《Lost in the Middle: How Language Models Use Long Contexts》于 2023 年公开，并发表于 TACL 2024。该研究围绕相关信息的位置与输入长度开展实验，分析二者对模型任务表现的影响。
>
> 论文使用多文档问答和键值检索两个任务进行分析，并进一步考察模型架构、问题在输入中的位置以及指令微调等因素。本文关注其中的文档位置实验、长窗口版本对照、键值检索和问题前置实验。相关实验使用的是论文所列出的模型版本，涉及 GPT-3.5-Turbo、Claude-1.3 及其长上下文版本等，GPT-3.5-Turbo 使用 0613 版本。
>
> **多文档问答任务设置**
>
> 作者从 NaturalQuestions-Open 中选取了 2,655 个问题，所选问题的长答案标注为维基百科段落。每次输入包括一个问题和若干文档，其中一篇包含标注答案，其余为干扰文档。干扰文档由检索系统选出，与问题具有相关性，但不包含标注答案。实验分别使用 10、20 和 30 篇文档，通过改变答案文档在序列中的位置，观察模型回答准确率的变化。这里的准确率按输出中是否包含标注答案计算。
>
> 对于同一个问题，移动答案文档的位置并不会改变该问题的正确答案。文档位置实验保留问题及文档集合，调整文档顺序，因此可以用于考察顺序变化对模型表现的影响。另一个变量是文档数量，作者通过增加干扰文档扩大输入长度。答案出现在模型输入中这一条件由实验设置保证，可据此分析模型取得相关材料后的使用情况。
>
> **主要实验结果**
>
> 在 20 篇文档的设置下，GPT-3.5-Turbo 在答案文档位于第 1 篇时，准确率为 75.8%，在第 10 篇时为 53.8%，在第 20 篇时为 63.2%。第 1 篇与第 10 篇之间相差 22 个百分点。论文中的多组实验呈现出首尾表现较高、中间表现较低的趋势。各模型下降程度有所不同，具体表现应结合对应模型与文档数量判断。
>
> 论文还提供了两种补充对照。在不给任何文档的情况下，GPT-3.5-Turbo 仅根据模型自身已有信息作答，准确率为 56.1%。在只提供包含答案的那一篇文档时，其准确率为 88.3%。因此，20 篇文档且答案位于第 10 篇时的 53.8%，甚至低于不给文档的对照结果。这一比较说明，包含正确证据的输入仍可能因干扰文档和排列方式而降低最终任务表现。
>
> **上下文窗口扩展实验**
>
> 作者进一步比较了 GPT-3.5-Turbo 与 GPT-3.5-Turbo 16K，以及 Claude-1.3 与 Claude-1.3 100K。当输入长度在普通版本和长窗口版本的允许范围内时，两者的表现非常接近。以 20 篇文档的 GPT-3.5-Turbo 对照为例，16K 版本在答案位于第 1、10、20 篇时分别为 75.7%、54.1% 和 63.1%，与普通版本在相同位置的数值接近。
>
> 这组比较控制了输入材料，考察扩展窗口的模型是否也改善了对相同输入的使用。长窗口版本能够接收更多文本，但在本组对照中，答案文档位于中间时的准确率下降仍然存在。该结果的适用范围是论文使用的模型和任务，后续模型需重新评估。
>
> **键值检索任务**
>
> 为进一步减少自然语言理解等因素的影响，作者使用了合成的键值检索任务。输入为 JSON 格式的键值对，其中键和值均为随机生成的 UUID。系统给出一个键，要求模型返回对应的值。作者分别设置了 75、140 和 300 对键值，每种规模生成 500 个样例，并改变目标键值对的位置。
>
> 这个任务主要要求从输入中找到精确匹配的键并返回其值。实验中，部分模型在目标位于中间位置时仍出现表现下降，但 Claude-1.3 及其 100K 版本在各个已测长度上表现接近满分。结合前面的多文档问答结果，可以看到精确字符串检索与自然语言问答具有不同的要求。单一任务的成功无法覆盖所有长上下文应用。
>
> **问题位置调整实验**
>
> 论文原有设置把问题放在材料之后。作者尝试在材料前后各放一次问题，使 decoder-only 模型在处理材料时也能利用前面的查询内容。经过这一调整，键值检索任务中的模型表现接近满分。GPT-3.5-Turbo 16K 在 300 对键值的设置下达到 100%，而原有提示下最差位置的准确率为 45.6%。
>
> 在多文档问答任务中，相同调整的效果较为有限。答案文档位于开头时，表现略有提高，其他位置则略有下降，位置敏感的总体趋势仍然存在。因此，这一提示调整的有效性与任务有关。论文还进行了其他因素分析，对位置效应原因的解释仍属于初步探索。
>
> **阅读判断与应用启示**
>
> 这篇论文使我更关注长上下文评测中的位置控制。只展示一次回答正确的案例，难以判断模型在同一批材料的不同顺序下是否稳定。对检索问答系统而言，评估应同时考虑相关文档能否被检索，以及模型拿到文档后能否正确使用。可以在保持问题和材料内容一致的条件下移动答案位置，观察输出变化。
>
> 同时，精确匹配任务和需要理解文本的问答任务应分别检查。前置问题在键值检索中取得很大改善，但这种改善没有同等地出现在多文档问答中。本文涉及的数值均为原论文报告的结果。针对一个新的模型或具体应用，仍需要在对应版本、输入长度和任务条件下重新测试。

**改写**

> **答案就在文档里，模型还是答错了**
>
> 给模型 20 篇文档，其中一篇写着答案。把这篇放在最前面，回答准确率是 75.8%。挪到第 10 篇，准确率掉到 53.8%。再放到最后，回升到 63.2%。
>
> 问题相同，文档也相同，仅仅换了排列顺序，准确率就相差 22 个百分点。
>
> 这是 Nelson F. Liu 等人在《Lost in the Middle》里做的一组实验，使用的是 GPT-3.5-Turbo 0613。论文最早在 2023 年公开，后来发表于 TACL 2024。它问了一个很具体的问题——一段信息出现在上下文的不同位置，模型还能不能同样准确地使用它？
>
> 做文档问答时，我们通常会先关心检索。相关段落有没有找到，返回的材料够不够，输入会不会超长。这篇论文往后追了一步。作者已经把包含答案的文档放进输入，接下来要看的是模型能否据此答对。
>
> **先把答案放进去，再移动它**
>
> 作者从 NaturalQuestions-Open 里选了 2,655 个问题，每个问题都能在维基百科的一段文字里找到标注答案。给模型的材料中，有一篇包含答案，其余是干扰文档。
>
> 干扰文档由检索系统选出，与问题相关，但不含标注答案。模型会同时看到一些看起来都相关的材料，需要从中找出能支持回答的那一篇。评估时，作者检查生成的回答里是否包含标注答案，据此计算准确率。
>
> 然后开始移动答案文档。先放在开头，再放到中间，最后放到末尾。文档总数也分别设成 10、20 和 30，观察材料增多以后会怎样。
>
> 我比较看重这里对位置的控制。同一个问题，正确答案始终在那里，干扰材料也相同。如果换个顺序就答不好，我们至少知道，输入排列已经影响了这次问答的结果。继续增加检索召回，还无法直接回答这个问题。
>
> 开头那组数字来自 20 篇文档的实验。论文中，多组实验都出现了类似趋势，答案靠近开头或结尾时表现较好，放到中间就下降。各模型下降多少，要看各自的结果。
>
> 还有一组对照更让人在意。作者完全不给文档，让同一个 GPT-3.5-Turbo 直接回答，准确率是 56.1%。只给包含答案的那一篇文档，则是 88.3%。换成 20 篇、把答案放在第 10 篇，结果就是前面的 53.8%。
>
> 正确证据已经提供了，结果却比不给资料还低。这说明，在这组任务里，补充材料的收益会受到其他文档和输入排列的影响。检索找到了答案以后，仍然有一段处理过程需要检查。[论文第 2 节、表 1 与附录 G](https://arxiv.org/html/2307.03172v3#S2)
>
> **换成长窗口版本，会好一些吗？**
>
> 作者比较了 GPT-3.5-Turbo 和它的 16K 版本，也比较了 Claude-1.3 和它的 100K 版本。这里有一个条件，拿来比较的输入必须同时处于两个版本允许的长度范围内。
>
> 结果相当接近。还是那组 20 篇文档，GPT-3.5-Turbo 16K 在第 1、10、20 篇的位置，分别得到 75.7%、54.1% 和 63.1%。对应普通版本的 75.8%、53.8% 和 63.2%，中间位置的下降几乎照样发生。
>
> 长窗口版本容纳的文本更多，确实扩大了能接收的输入范围。但对于这批两个版本都放得下的材料，窗口扩展带来的改善很有限。评估时，最大输入长度之外，还需要看模型在不同位置使用信息的表现。这里讨论的是论文中的模型版本，换一个模型仍要重新测。[论文第 2.3 节](https://arxiv.org/html/2307.03172v3#S2.SS3)
>
> 读到这里，还有一种可能需要考虑。多文档问答涉及自然语言理解，模型要判断哪些句子有用，再组织答案。中间位置的下降，会不会与这些步骤有关？
>
> 作者接着把任务简化了，输入换成一份 JSON，里面全是键值对。键和值都用随机生成的 UUID。给定一个键，模型只需要找到它，再返回对应的值。作者测了 75、140 和 300 对键值，每种规模各 500 个样例，也会移动目标键值对的位置。
>
> 部分模型在这个任务上依然会漏掉中间的信息。不过，Claude-1.3 及其 100K 版本在所测长度上几乎都能答对。再回看多文档问答，它们也受到了位置变化的影响。把字符串找出来和理解一组文档，需要分开看。[论文第 3 节](https://arxiv.org/html/2307.03172v3#S3)
>
> **把问题提前，两个任务的反应不同**
>
> 原来的输入顺序是先给材料，最后提问。作者又试了一次，把问题放在材料前后各一遍。
>
> 这个调整有具体的考虑。decoder-only 模型在处理某个位置时，只能使用它之前的内容。如果问题只放在最后，模型处理前面的材料时还看不到问题。把问题也放在前面，就能让材料的表示包含查询信息。
>
> 键值检索的结果改善得很明显。GPT-3.5-Turbo 16K 在 300 对键值的任务中达到了 100%，原提示下最差位置的准确率只有 45.6%。其他被测模型在这项任务里也接近满分。
>
> 但回到多文档问答，效果就小得多。答案在开头时略有改善，其他位置略有下降，原先的位置敏感仍然存在。相同的提示调整，在两个任务上给出了差别很大的结果。[论文第 4.2 节](https://arxiv.org/html/2307.03172v3#S4.SS2)
>
> 如果要给文档问答系统选提示词，我会直接在问答任务上比较效果。前面那个 100% 对应的是查找随机键值对，能否处理自然语言材料，还要看后面的问答结果。
>
> 论文还检查了模型架构和指令微调等因素，作者对原因的解释仍属于初步分析。[论文第 4 节](https://arxiv.org/html/2307.03172v3#S4)
>
> 对我来说，这篇论文给文档问答评测增加了一个很容易执行的检查。固定问题和材料，把答案所在段落换几个位置，再看模型的回答。一次答对之后，继续检查同样的信息换个顺序还能否被用上。做精确匹配和做自然语言问答时，也分别保留结果。
>
> 下一次看到长上下文演示，我会多看一眼答案所在的位置。它恰好在开头时答对了，放到中间还能答对多少？

处理流程与写作要求见[微信公众号指南](references/wechat-article.md)。

</details>

<details>
<summary><strong>5. 基金申请｜口头讨论草稿 → 正式的研究目标与验证计划</strong></summary>

**原文**

> 现在做工业缺陷检测，一到新产线，标注图像又少，现有方法就不太适应。我们的想法是试试能不能把没标注的图像也用起来，少依赖一些人工标注。打算找三条产线做对比实验，看看能不能在检测准确率不降的情况下，把标注量减下来。

**改写**

> 现有工业缺陷检测方法在标注图像较少时难以适应新产线。本项目拟利用未标注图像减少对人工标注的依赖，并在三条产线上开展对比实验，检验该方法能否在保持检测准确率的同时降低标注量。

处理流程与完整案例：[基金申请](references/grant-proposal.md)

</details>

<details>
<summary><strong>6. 学术讲稿中文｜论文式长句 → 听众容易跟上的讲述</strong></summary>

**原文**

> 围绕检索模块是否构成性能增益主要来源这一问题，本研究通过移除该模块开展消融实验，并在与完整系统相同的测试集上进行评估，所得结果表现为任务成功率由完整系统配置下的 71% 下降至移除检索模块配置下的 59%，由此可见，检索模块对于当前系统的性能具有贡献。

**改写**

> 为了弄清性能提升是不是主要来自检索模块，我们把它去掉后，在同一个测试集上做了对比。任务成功率从完整系统的 71% 降到了 59%，说明检索模块确实对当前系统有贡献。

处理流程与完整案例：[学术讲稿中文](references/academic-talk-zh.md)

</details>

<details>
<summary><strong>7. 学术讲稿英文｜书面学术长句 → 适合英语口头讲述的段落</strong></summary>

**原文**

> An ablation experiment involving the removal of the retrieval module was conducted with the objective of determining whether this module constituted the principal source of the performance gain, with evaluation on the same test set yielding a reduction in task success from 71% under the full-system configuration to 59% under the configuration in which retrieval was absent, thereby indicating a contribution of the retrieval module to the performance of the current system.

**改写**

> We wanted to know whether most of the gain came from retrieval, so we removed that module and ran the system on the same test set. Task success fell from 71% with the full system to 59% without retrieval, which shows that the module contributes to performance in this system.

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

> Table 3 already includes the comparison with method B. We may not have made this clear in the original text, so we have revised Section 4.2 to refer explicitly to Table 3 and explain that both methods use the same training budget.

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
