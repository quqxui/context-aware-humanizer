<p align="center">
  <img src=".github/banner.png" alt="Context-Aware Humanizer — Chinese and English writing skill" width="100%">
</p>

<h1 align="center">Context-Aware Humanizer</h1>

<p align="center"><strong>Write for the context. Keep your voice.</strong></p>

<p align="center">
  <a href="#scenarios"><img src="https://img.shields.io/badge/Languages-English%20%2B%20Chinese-24544F?style=flat-square" alt="Languages: English and Chinese"></a>
  <a href="#scenarios"><img src="https://img.shields.io/badge/Scenarios-12-24544F?style=flat-square" alt="12 writing scenarios"></a>
  <a href="#personal-voice"><img src="https://img.shields.io/badge/Voice-Personal-B96543?style=flat-square" alt="Personal voice"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-69717C?style=flat-square" alt="MIT License"></a>
</p>

<p align="center">
  <strong>English</strong> · <a href="README.zh.md">简体中文</a>
</p>

<p align="center">
  <a href="#quick-start">Quick start</a> ·
  <a href="#examples">Scenarios &amp; examples</a> ·
  <a href="#personal-voice">Personal voice</a> ·
  <a href="#installation">Installation</a>
</p>

A bilingual Agent Skill for **AI text humanization, text polishing, and tone adjustment**. Adapt Chinese and English drafts to their readers and purpose, from everyday messages to academic papers.

<a id="core-features"></a>

- **12 writing scenarios**: dedicated guidance for chat, social posts, work messages, documentation, and six academic uses.
- **Separate Chinese and English rules**: each scenario has language-specific guides and worked examples, maintained independently.
- **Your own voice**: preserve the draft's tone, use writing samples, or apply a reusable style profile.

<a id="quick-start"></a>

## 🚀 Quick start

Once the skill is [available to your assistant](#installation), describe the context and paste your draft:

```text
Use context-aware-humanizer to rewrite this as a message to my supervisor in English.
Keep it polite and natural. Preserve "may finish by Friday" as a possibility, not a promise:
[paste your draft]
```

By default, the skill keeps the original language and returns one usable rewrite. Text that already fits can stay unchanged. Ask for translation, a before-and-after comparison, or alternatives when needed.

<a id="scenarios"></a>
<a id="examples"></a>

## ✍️ 12 scenarios, 12 before-and-after examples

Each scenario uses a different draft to show changes in wording, tone, or structure. These are fictional illustrations, not research findings or model evaluation results. Expand an example for the comparison and its guides.

<details open>
<summary><strong>1. Chat | Formal notice → A natural reply to a friend</strong></summary>

**Before**

> Regarding dinner on Saturday, it is possible that I will arrive a little late, as I have a meeting in the afternoon. If you arrive at the restaurant before I do, please go ahead and order without waiting for me.

**After**

> I might be a bit late for dinner on Saturday. I've got a meeting that afternoon. If you get there first, go ahead and order. No need to wait for me.

Guides: [English](references/chat/en.md) · [中文](references/chat/zh.md)

</details>

<details>
<summary><strong>2. Work message | Background first → Action and deadline first</strong></summary>

**Before**

> The client demo has been scheduled for Friday, so regression testing of the login flow needs to be carried out. Alex is responsible for this work, with completion required by 3 p.m. Thursday. Any blockers encountered during testing should also be reported to me by 5 p.m. Thursday.

**After**

> Alex, please finish regression testing of the login flow by 3 p.m. Thursday for Friday's client demo. Report any blockers to me by 5 p.m. Thursday.

Guides: [English](references/work-message/en.md) · [中文](references/work-message/zh.md)

</details>

<details>
<summary><strong>3. Xiaohongshu | Visit log → Personal notes with practical details</strong></summary>

**Before**

> I visited the riverside café at 2 p.m. last Sunday and stayed for two hours. I found the light at the window seats pleasant, although power outlets were available only next to the counter. I think it is a good place to sit with a book, but anyone bringing a laptop should pay attention to where they sit.

**After**

> **Riverside café: window light, outlets by the counter**
>
> I went at 2 p.m. last Sunday and stayed for two hours. The light by the windows was lovely. A good spot to sit with a book.
>
> If you're bringing a laptop, check your seat: the only outlets are next to the counter.

Guides: [English](references/xiaohongshu/en.md) · [中文](references/xiaohongshu/zh.md)

</details>

<details>
<summary><strong>4. X / Twitter | Long setup → A concise personal take</strong></summary>

**Before**

> After trying three note-taking apps, I found that, for me, the key factor in the experience was not the number of features available but whether I could quickly find something I had previously written down. As a result, search is now the first feature I consider when choosing a notes app.

**After**

> Three notes apps later, I check search first. For me, finding an old note quickly matters more than having more features.

Guides: [English](references/x-post/en.md) · [中文](references/x-post/zh.md)

</details>

<details>
<summary><strong>5. WeChat article | Process report → A focused, readable update</strong></summary>

**Before**

> We conducted a review of the team's weekly meetings over the past month and found that each meeting lasted about 50 minutes on average, with roughly 30 minutes devoted to taking turns reporting progress. We therefore decided to try moving progress updates into a document before each meeting and use meeting time to discuss blockers. This arrangement will begin next week and run for two weeks before we decide whether to continue.

**After**

> Over the past month, our weekly meetings averaged about 50 minutes. Roughly 30 of those minutes went to progress updates.
>
> Starting next week, we'll try a two-week change: write updates in a document beforehand and use the meeting to discuss blockers. Then we'll decide whether to keep it.

Guides: [English](references/wechat-article/en.md) · [中文](references/wechat-article/zh.md)

</details>

<details>
<summary><strong>6. Documentation | Dense instructions → Steps the reader can follow</strong></summary>

**Before**

> Before initiating the data validation task, it is necessary to ensure that the input file `data.csv` has been placed in the current directory. Once this prerequisite has been met, executing `sampletool validate data.csv --output report.json` performs validation of the input file and, on successful validation, writes the report to `report.json`.

**After**

> 1. Place `data.csv` in the current directory.
> 2. Run `sampletool validate data.csv --output report.json`.
>
> On successful validation, the report is written to `report.json`.

Guides: [English](references/documentation/en.md) · [中文](references/documentation/zh.md)

</details>

<details>
<summary><strong>7. Grant proposal | Dense aim statement → Problem, approach, and evaluation</strong></summary>

**Before**

> This project intends to conduct research into the difficulty that existing industrial defect detection methods have in adapting to new production lines when few labeled images are available, with the aim of using unlabeled images to reduce reliance on manual annotation, and plans to carry out comparative experiments on three production lines to assess whether annotation requirements can be reduced while maintaining detection accuracy.

**After**

> Industrial defect detection methods struggle to adapt to new production lines with few labeled images. This project aims to investigate whether unlabeled images can reduce reliance on manual annotation. We plan comparative experiments on three production lines to test whether the approach reduces annotation needs while maintaining detection accuracy.

Guides: [English](references/grant-proposal/en.md) · [中文](references/grant-proposal/zh.md)

</details>

<details>
<summary><strong>8. Academic talk | Written experiment description → An explanation listeners can follow</strong></summary>

**Before**

> To determine whether the retrieval module was the main source of the performance gain, we conducted an ablation experiment in which the module was removed. On the same test set, task success fell from 71% for the full system to 59% without retrieval, indicating that the module contributes to the current system's performance.

**After**

> Next, let's look at whether retrieval accounts for most of the gain. We removed the retrieval module and tested again on the same test set. Task success dropped from 71% to 59%, so retrieval does contribute to the current system's performance.

Guides: [English](references/academic-talk/en.md) · [中文](references/academic-talk/zh.md)

</details>

<details>
<summary><strong>9. Academic slides | Results paragraph → A takeaway title and key numbers</strong></summary>

**Before**

> In tests with a batch size of 1 and an input length of 2,048 tokens, caching reduced mean latency per request from 1.8 to 1.1 seconds, while peak GPU memory use increased from 8.2 to 9.0 GB.

**After**

> **Caching lowers latency but uses more GPU memory**
>
> - Mean latency per request: 1.8 → 1.1 seconds
> - Peak GPU memory: 8.2 → 9.0 GB
>
> Test conditions: batch size = 1; input length = 2,048 tokens.

Guides: [English](references/academic-slides/en.md) · [中文](references/academic-slides/zh.md)

</details>

<details>
<summary><strong>10. Academic paper | Repeated explanation → A concise, precise result</strong></summary>

**Before**

> Our evaluation of the proposed method showed that, on Dataset A under the same evaluation setup, it achieved an accuracy of 86%, while the baseline achieved an accuracy of 82%. From this comparison, it can be seen that our method's accuracy was 4 percentage points higher than the baseline's.

**After**

> Under the same evaluation setup on Dataset A, our method achieved 86% accuracy, exceeding the baseline's 82% by 4 percentage points.

Guides: [English](references/academic-paper/en.md) · [中文](references/academic-paper/zh.md)

</details>

<details>
<summary><strong>11. Peer review | General criticism → Evidence and a clear revision request</strong></summary>

**Before**

> The experimental reporting has an important gap. Table 2 gives results from only one run and does not report variation across random seeds, making it difficult to judge whether the improvement is stable. I think the authors need to report means and standard deviations across multiple random seeds.

**After**

> Table 2 reports only a single run, leaving the stability of the improvement across random seeds unclear. Please report means and standard deviations across multiple random seeds.

Guides: [English](references/peer-review/en.md) · [中文](references/peer-review/zh.md)

</details>

<details>
<summary><strong>12. Reviewer response | Defensive wording → Professional clarification and a revision location</strong></summary>

**Before**

> The reviewer says we omitted a comparison with method B, but we actually already included this result in Table 3. The original wording may not have been clear enough, causing this point to be overlooked. We have added text in Section 4.2 that explicitly points to Table 3 and states that both methods use the same training budget.

**After**

> Table 3 includes the comparison with method B under the same training budget. We may not have made this clear in the original text. We have revised Section 4.2 to point explicitly to Table 3 and clarify the matched training budget.

Guides: [English](references/reviewer-response/en.md) · [中文](references/reviewer-response/zh.md)

</details>

<a id="voice-options"></a>
<a id="personal-voice"></a>

## 🎙️ Keep your own voice

Describe what you want: "Put the request before the background," "Keep the disagreement clear and polite," or "Make it conversational without adding pleasantries." You can also supply your own writing:

```text
These are two samples of my writing. Use them for style only, not facts:
[writing samples]

Rewrite this work message in my voice:
[draft]
```

**Current instructions take priority; samples supply style, not facts for the new draft.** Ordinary rewrites do not save preferences. To reuse a style, supply an existing profile or explicitly request memory:

```text
Save the style from these samples for future English work messages.
Use only passages I wrote. Exclude source facts and mark uncertain observations as tentative.
```

To inspect it first, ask for a preview without saving. See the [memory guide](references/style-memory.md) and [profile template](templates/style-memory.md).

<a id="installation"></a>

## 🛠️ Installation

```bash
git clone https://github.com/quqxui/context-aware-humanizer.git
```

1. **Try locally:** ask your assistant to read [`SKILL.md`](SKILL.md) and follow its routing to the scenario and language guide.
2. **Install for reuse:** copy `SKILL.md`, `references/`, `scripts/`, and `templates/` into your assistant's skill directory. Keep the relative layout intact.
3. **Enable optional memory:** use a writable installation and Python 3.9+. Ordinary text editing needs only the Markdown guides.

Style memory lives in the installation's private `memory/` directory. Routine rewrites read only same-language common and matching scenario profiles. Separate installations do not synchronize automatically.

<details>
<summary><strong>Export, backup, and update</strong></summary>

Replace `<skill-root>` with the installation directory. Output paths must name new files outside that directory.

```bash
python3 <skill-root>/scripts/skill_package.py export --output /outside/context-aware-humanizer.zip
python3 <skill-root>/scripts/skill_package.py backup --output /outside/context-aware-humanizer-private.zip
python3 <skill-root>/scripts/skill_package.py update --source /path/to/new-skill
```

- `export`: create a public package without private memory or local artifacts.
- `backup`: create a private backup that includes memory and revisions.
- `update`: update maintained program files while preserving the target installation's memory.

Public Git excludes personal memory. Third-party installers may still remove data; back up before using them. The host assistant reads supplied documents; the storage scripts save only the extracted style.

</details>

## Scope and license

This skill edits supplied text. It does not connect to platforms, fetch, publish, or submit content. It does not fact-check text, report an "AI percentage," or guarantee detector outcomes. Systematic cross-model evaluation has not been completed.

Contributions of scenarios, examples, and reproducible failures are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md). Original content uses the [MIT License](LICENSE); external material belongs to its authors.
