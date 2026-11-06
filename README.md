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
| 4 | [微信公众号](references/wechat-article.md) | 中文 | AI 产品体验、技术解读、行业观察与长文展开 |
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
<summary><strong>4. 微信公众号｜内部试用报告 → AI 工具体验长文</strong></summary>

本例为自拟案例，文中的试用经历、时间和数量均为设定。

**需求**

把这份内部试用报告改成面向 AI 工具使用者的公众号长文。可以调整标题和段落，保留第一人称、任务细节、实际问题和使用判断。

**原文**

> **关于使用 AI 助手辅助编制技术周报的试用情况**
>
> 为评估 AI 助手在技术信息整理场景中的应用价值，我在上周使用一款具备网页读取能力的 AI 助手，开展了一次技术周报编制试用。本次试用使用我事先收集的 12 个链接，其中包括 7 篇官方博客、3 条项目更新和 2 篇媒体报道。周报面向团队内的产品和研发同事，主要用于了解近期发布了什么、哪些功能可以尝试，以及哪些变化可能与现有工作有关，不要求详细讲解模型结构。
>
> 在以往的周报编制过程中，我通常会在一周内持续保存链接，集中整理时再逐篇阅读、摘录信息并调整格式。同一件事有时会同时出现在官方博客和媒体报道中，需要合并处理。此次希望由 AI 助手完成初步归类与摘要，以减少重复摘录和排版操作。我没有让它自行扩大搜索范围，也没有要求它判断整个行业的发展趋势，任务材料限于已经提供的链接。
>
> 我给出的要求是根据这 12 个链接整理一份供产品和研发同事阅读的 AI 周报，每条保留发生了什么、可能影响什么以及来源链接。对于无法读取的页面，应明确标注，不根据标题补写内容。提供这些要求后，助手约用十分钟输出了一份约 1,800 字的初稿，按模型更新、开发工具和应用功能分组，并在每条信息后附上了链接。初稿包含开头概述和结尾总结，表面上已经具备一份完整周报的结构。
>
> 从初步阅读感受看，归类和排版基本符合需要。原本分散在多个网页中的内容被整理到一起，我可以较快查看每条信息的主题和出处。这部分让我感到省事，也让我一度认为后续只需要做少量文字修改。但是，在逐条尝试打开来源页面、对照正文及读取记录后，我发现初稿还存在需要人工纠正的问题，结构完整并不足以判断内容已经可以发给同事。
>
> 第一个问题是重复信息。有两篇材料讨论的是同一次产品更新，其中一篇为官方说明，另一篇为媒体报道。助手分别生成了两条摘要，使用了不同的标题，读起来容易被理解为两项独立进展。我要求合并后，它将两条内容整合为一条，并保留官方说明作为主要来源。此次情况说明，按网页生成摘要之后，还需要检查不同网页是否对应同一个事件，否则周报中的信息数量会被重复条目放大。
>
> 第二个问题涉及页面读取状态。12 个链接中有两个页面没有成功读取正文，助手获取到的内容只有标题和搜索摘要，但初稿仍对这两项内容写出了完整介绍，也没有标记材料缺失。我对此感到失望，因为任务要求中已经明确说明了无法读取时的处理方式。随后，我要求将这两项移入待核实部分，只保留标题和链接。其余可读取材料在合并重复事件后，形成了 9 条正文条目。
>
> 第三个问题是功能开放范围。一篇官方说明明确写着，相关功能仅向申请通过的企业账号开放试用，初稿却将其表述为所有用户都可以直接使用。对于只是了解新闻的读者，这一差异可能不会立刻显现，但产品和研发同事可能据此安排试用，因此开放对象和申请条件都应保留。我将官方原句提供给助手后，它修正了这一条。至于其他读者是否实际受到影响，本次并未对外发布初稿，也没有相关记录。
>
> 对于“可能影响什么”的部分，初稿也存在较多笼统表达，多条信息均被概括为“显著提升效率”或“推动工作方式变革”，但提供的材料并未包含足以支持这些判断的使用结果。我希望周报能具体说明与同事有什么关系，例如是否需要申请试用、现有接口是否需要调整，以及是否值得安排进一步体验。对于材料无法支持的影响判断，我要求删除，或明确保留为后续需要验证的问题。
>
> 在后续修改中，我要求助手先整理一份供我核对的表格，逐项列出事件、来源、页面读取状态、开放条件以及尚待确认的内容。我先检查表格，再让它按确认后的信息生成周报正文。完成这些调整后，正文保留 9 条信息，另外列出 2 条待核实材料。我仍逐项检查了相关信息，修订稿才达到可以用于内部分享的程度。原来的初稿没有直接发送，整个过程也没有让助手代为发布。
>
> 本次首稿等待时间约为十分钟，人工核对和修改另用了约二十分钟。我没有记录以往完全手工完成同类周报的耗时，也没有进行相同材料下的人工对照，因此无法给出节省时间的比例。此次最直接的感受是，摘录、归类和排版更方便了，而自己的主要工作集中到了来源核对、条件检查和内容取舍。对于已经熟悉材料的人，这种分工可能有用，实际效果仍需结合后续使用记录判断。
>
> 后续我计划继续用几周，保留每次提供的链接和修改记录，并分别记录初稿等待时间、人工核对时间以及同类错误是否重复出现。在目前这类内部技术周报任务中，我愿意继续让助手整理初稿，同时保留人工核对。如果材料需要登录才能访问，或只有标题和摘要可用，就先列为待核实，等取得完整材料后再补入正文。是否适合扩展到对外发布的文章，需要另外评估。

**改写**

> **AI 周报写完了，我又点开了它的每一条链接**
>
> 上周，我把攒下来的 12 个链接交给一款 AI 助手，让它整理成技术周报。大约十分钟后，一份约 1,800 字的初稿出来了。模型更新、开发工具、应用功能，分组齐全，每条后面还带着来源链接。
>
> 第一眼看过去，我挺满意。平时要自己摘录、归类、统一格式的内容，这次已经整理好了。我当时觉得，再顺一遍文字，大概就能发给同事。
>
> 等我逐条点开链接，问题才陆续出现。有两条说的是同一件事，有两个页面根本没读到正文，还有一项只向部分企业账号开放的功能，被写成了所有用户都能用。最后，核对和修改又花了我大约二十分钟。
>
> 我准备继续让它整理初稿，自己负责核对来源、检查开放条件，再决定哪些内容发给同事。
>
> **12 个链接，一份内部周报**
>
> 这 12 个链接是我自己收集的，包括 7 篇官方博客、3 条项目更新和 2 篇媒体报道。我希望产品和研发同事看完以后，能知道最近发布了什么、哪些功能可以试，以及哪些变化可能与手头的工作有关。模型结构有多复杂，这份周报暂时用不上。
>
> 所以，我给助手的要求也很直接。只根据这些链接整理，每条写清发生了什么、可能影响什么，再附上来源。页面打不开就注明，别根据标题把内容补出来。
>
> 以前我会在一周里不断存链接，等到整理时再逐篇看。同一次更新，经常既有官方博客，也有媒体报道。把它们合并、摘出有用的信息，再整理成统一格式，确实有些重复工作。我最希望 AI 帮忙完成的就是这部分。
>
> **链接都在，内容还得逐条看**
>
> 最先发现的是重复。官方博客讲了一次产品更新，媒体又报道了同一件事。助手给它们各写了一条摘要，标题还不一样。连着读下来，很容易以为这一周多了两项进展。
>
> 我让它合并后，它把两条整理成了一条，以官方说明为主要来源。这需要有人先认出它们说的是同一件事。按网页逐条做摘要，仍然需要再检查一次事件是否重复。
>
> 更让我失望的是那两个没读到正文的页面。我对照了来源和读取记录，发现助手拿到的只有标题和搜索摘要，初稿却给出了完整介绍，连材料缺失都没标出来。任务里明明已经要求标出无法读取的页面，这条要求还是被漏掉了。
>
> 我把这两项移到了待核实部分，只留标题和链接。剩下的材料合并重复事件后，正文保留了 9 条。少写几条也可以，至少要知道每条信息具体依据了什么。
>
> **开放条件，会直接影响同事能不能用**
>
> 还有一处修改，单看文字很容易略过。官方说明限定了试用范围，只有申请通过的企业账号能用，初稿却写成所有用户都可以直接使用。
>
> 如果只是快速浏览新闻，这句话读起来很顺。但这份周报会给产品和研发同事看，他们可能真的打开产品，准备试一试。能不能申请、需要什么账号，都会影响下一步安排。把这些条件删掉，信息就变了。
>
> 我把官方原句交给助手，它修正了表述。这次初稿还没发出去，也就没有同事据此安排试用的后续记录。不过，这个问题让我决定，今后要单独检查开放条件。
>
> 至于“可能影响什么”，我也删了不少空泛的判断。好几条都在说“显著提升效率”“推动工作方式变革”，材料里却没有对应的使用结果。我更想让同事看到具体的事情，比如是否需要申请资格，现有接口是否要调整，或者有哪些功能值得另外试一次。材料支持到哪里，就先写到哪里。
>
> **后来，我先让它整理了一张核对表**
>
> 发现这些问题后，我让助手把事件、来源、页面读取状态、开放条件和尚待确认的内容列成表格。我先看这张表，确认哪些信息可以保留，再让它生成正文。
>
> 这样做以后，归类和排版仍然交给助手。我检查时也有了明确的位置，可以对着来源确认条件，决定哪些条目合并、哪些暂时放下。修订稿最后保留了 9 条正文信息，另列 2 条待核实材料，逐项检查后才达到内部分享的要求。整个过程里的发送决定都由我来做，助手没有代为发布。
>
> 要问这次到底省了多少时间，我还给不出比例。首稿约等了十分钟，核对修改又花了约二十分钟，但以前纯手工做同类周报用了多久，我没有记录。这次也没有拿同一批材料做人工对照。
>
> 我能确定的是，自己少做了重复摘录和排版，把更多注意力放到了来源、条件和内容取舍上。对这批我已经收集过的材料，这种分工值得继续试，实际效果还要看后续的使用记录。
>
> 接下来几周，我会保留每次输入的链接和修改记录，分别记下等初稿、核对内容用了多久，再看看同样的问题会不会反复出现。能读到完整材料的条目，就继续让助手整理初稿。需要登录或者只有摘要的，先放进待核实部分，等材料补齐再写。
>
> 至于能不能直接用它做对外发布的文章，我还想再积累一些使用记录。眼下这份内部周报，我会继续让 AI 帮忙整理，也会继续点开那些链接。

风格指南、公开样本与 Agent 记忆技术解读长文见[微信公众号指南](references/wechat-article.md)。

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
