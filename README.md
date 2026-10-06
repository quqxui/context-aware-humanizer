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
  <a href="#examples">Examples</a> ·
  <a href="#scenarios">Scenarios</a> ·
  <a href="#voice-options">Tone choices</a> ·
  <a href="#installation">Installation</a>
</p>

A bilingual Agent Skill for **AI text humanization, text polishing, rewriting, paraphrasing, copyediting, and proofreading** in Chinese and English. Adapt tone and preserve your personal voice across chat, social media, documentation, grant proposals, academic papers, talks, slides, peer reviews, and rebuttals.

> **Text editing only.** This skill polishes and rewrites text you provide. Scenarios describe writing styles and formats. It provides no APIs or connectors for WeChat, Xiaohongshu, X, journal submission systems, or other services, and does not fetch, publish, or submit content.

<a id="core-features"></a>

## ✨ Core features

| Core feature | What you get |
|---|---|
| **The right context** | **12 dedicated scenarios**, including six academic uses: grants, talks, slides, papers, peer reviews, and reviewer responses. |
| **Independent Chinese and English** | Each scenario has **separate rules and examples for each language**. Maintain either version independently. |
| **Your own voice** | **Preserve your voice by default.** Choose a tone, supply writing samples, or reuse an editable personal profile. |

The skill reads the guide for the requested **scenario and language**. Chinese rewrites use Chinese examples; English rewrites use English examples. Conference rebuttals and journal revision letters are handled with their different constraints.

<a id="examples"></a>

## One set of notes, three contexts

> **Source notes:** Dataset A test set (the same for both): our method 86% accuracy; baseline 82%; other datasets not evaluated.

| You are writing… | A rewrite for that context |
|---|---|
| **A talk** | On the same test set from Dataset A, our method reached 86% accuracy and the baseline reached 82%. We haven't evaluated other datasets yet. |
| **A slide** | **Dataset A test set: accuracy**<br>Our method 86% · baseline 82%<br>Other datasets: not evaluated |
| **A paper** | Using the same test set from Dataset A, our method achieved 86% accuracy, compared with 82% for the baseline. We did not evaluate other datasets. |

The wording and structure change. The numbers, evaluation conditions, and limitations stay intact.

<details>
<summary><strong>Another example: a plan must remain a plan</strong></summary>

**Before**

> We plan to run three additional seeds, subject to compute availability. We have not run them yet.

**After**

> We plan to run three additional seeds if compute is available. We have not run them yet.

Smoother wording does not turn a planned experiment into a completed one.

</details>

<a id="quick-start"></a>

## 🚀 Quick start

Once the skill is available to your assistant, describe the context and paste your text. These are **natural-language requests**, not shell commands.

```text
Use context-aware-humanizer to rewrite this as a friendly work message in English.
Keep the deadline and the conditional promise. Return only the message:
[paste your draft]
```

<details>
<summary><strong>Try an academic response or a slide</strong></summary>

```text
Use context-aware-humanizer to polish this reviewer response in English.
Keep the disagreement explicit and professional. Do not add experiments or revisions:
[paste your response]
```

```text
Turn these results into one academic slide in English: one title and two bullets.
Keep the evaluation conditions and limitations:
[paste your results]
```

</details>

Add an audience, tone, or writing sample when useful. The default output is **one usable rewrite**. Ask for alternatives or comments if you want them. Text that already fits can remain unchanged; the original language is kept unless translation or bilingual output is requested.

**First time here?** Follow the short [installation guide](#installation) below.

<a id="scenarios"></a>

## 📚 Find your scenario

**Choose a scenario, then a language.** Every guide contains its own rules and **two worked cases**: request → source → rewrite → explanation.

| Scenario | What the guide focuses on | Chinese | English |
|---|---|:---:|:---:|
| **Chat** | Personal messages, relationships, spoken phrasing, commitments | [中文](references/chat/zh.md) | [English](references/chat/en.md) |
| **Work message** | Emails, requests, updates, actions, ownership, timing | [中文](references/work-message/zh.md) | [English](references/work-message/en.md) |
| **Xiaohongshu** | Experiences, guides, product notes, sources and personal experience | [中文](references/xiaohongshu/zh.md) | [English](references/xiaohongshu/en.md) |
| **X / Twitter** | Posts, threads, replies, a clear point and relevant context | [中文](references/x-post/zh.md) | [English](references/x-post/en.md) |
| **WeChat article** | Explainers, opinions, notices, coherent article structure | [中文](references/wechat-article/zh.md) | [English](references/wechat-article/en.md) |
| **Documentation** | READMEs, procedures, guides, usable and precise instructions | [中文](references/documentation/zh.md) | [English](references/documentation/en.md) |
| **Grant proposal** | Aims, rationale, plans, evidence and feasibility | [中文](references/grant-proposal/zh.md) | [English](references/grant-proposal/en.md) |
| **Academic talk** | Seminars, reports, defenses, spoken flow and audience | [中文](references/academic-talk/zh.md) | [English](references/academic-talk/en.md) |
| **Academic slides** | Titles, bullets, captions, key points and essential conditions | [中文](references/academic-slides/zh.md) | [English](references/academic-slides/en.md) |
| **Academic paper** | Abstracts, methods, results, discussion, evidence and limits | [中文](references/academic-paper/zh.md) | [English](references/academic-paper/en.md) |
| **Peer review** | Editing an existing review, supporting criticism with evidence | [中文](references/peer-review/zh.md) | [English](references/peer-review/en.md) |
| **Reviewer response** | Rebuttals, revision letters, direct answers and actual changes | [中文](references/reviewer-response/zh.md) | [English](references/reviewer-response/en.md) |

All examples are fictional illustrations, not research findings or performance measurements.

<a id="voice-options"></a>

## 🎙️ Choose a tone

The default is **preserve the original voice**. Say “make it warmer” or “formal but direct,” or choose **natural · warm · direct · measured · formal · lively**.

To see relevant options in use:

```text
Use context-aware-humanizer to show me the available tones.
Use a passage with enough context to show meaningful differences; leave an already suitable version unchanged.
```

**A short message that already works**

> Please send the revised brief by Friday so we can finish our review before launch.

For **natural**, keep it as written. A forced synonym, added “Thank you!”, or exclamation mark would not improve this request. The other tones are available when the audience and purpose call for them; they do not require six different rewrites of every sentence.

**A comparison with room for a real choice**

> **Source:** The new search flow demo is Thursday at 3 p.m. We'll show the new filtering options. Please send questions by Wednesday; the link is in the calendar invite.

| Tone | Rewrite | What changes |
|---|---|---|
| **natural** | The new search flow demo is Thursday at 3 p.m. We'll show the new filtering options. Please send questions by Wednesday; the link is in the calendar invite. | The original already fits. |
| **direct** | New search flow demo: Thursday, 3 p.m. We'll show the new filtering options. Send questions by Wednesday. Link in the calendar invite. | Puts the logistics first and uses a compact team-update format. |
| **formal** | The new search flow demo will take place on Thursday at 3 p.m. and cover the new filtering options. Please send any questions by Wednesday. The meeting link is in the calendar invitation. | Uses a professional register without padded phrases. |
| **lively** | On Thursday at 3 p.m., we'll show the new search flow and its filtering options. Questions? Send them by Wednesday. The link's in the calendar invite. | Uses shorter beats without adding facts or relying on an exclamation mark. |

These versions keep the demo time, topic, question deadline, and link location. **Warm** and **measured** remain options for contexts where those shifts serve the reader.

A tone choice applies to the current request; it does not automatically become a lasting preference. Ordinary rewriting does not require a questionnaire.

<a id="personal-voice"></a>

## Keep it sounding like you

| Start with… | What you provide | How it is used |
|---|---|---|
| **Your draft** | The text to rewrite | Improve awkward phrasing while preserving its voice |
| **Writing samples** | One or more passages you wrote | Refer to wording, rhythm, punctuation, and directness for this task |
| **A reusable profile** | A Markdown profile you explicitly supply or select | Reuse preferences you can inspect and edit |

### Supply writing samples and rewrite directly

```text
These are samples of my own writing. Use them for style only, not facts.
Sample 1: Quick update: the chart is ready. It still needs a final check.
Sample 2: The new version works, but two details need fixing.

Now rewrite this work message in my voice:
The report is delayed because the data export failed.
If the export succeeds today, I expect to be able to send a draft tomorrow.
```

**Example rewrite**

> Quick update: the report is delayed because the data export failed. If it succeeds today, I expect to be able to send a draft tomorrow.

The short update format carries over. The chart and the two fixes do not. Delivery remains expected and conditional.

<details>
<summary><strong>Optional: create a reusable profile</strong></summary>

Fill in a profile yourself, or ask the assistant to draft one from your samples:

```text
Create an editable voice profile from these samples.
Separate Chinese and English preferences. Leave uncertain fields unspecified.
Show the profile and a sample rewrite; do not save it automatically.
```

**Copyable template** — every field is optional. Keep only the preferences you want to reuse.

```markdown
# My writing preferences

## Scope
- Contexts: unspecified

## Chinese
- Tone and sentence length: unspecified
- Address, punctuation, and formatting: unspecified
- Expressions to keep or avoid: unspecified
- Own writing samples: optional

## English
- Tone and sentence length: unspecified
- Address, punctuation, and formatting: unspecified
- Expressions to keep or avoid: unspecified
- Own writing samples: optional
```

**Filled example (fictional)**

```markdown
# My writing preferences

## Scope
- English work updates only.

## Chinese
- Unspecified.

## English
- Use short sentences; state progress before limitations.
- Contractions are fine; avoid exclamation marks.
- Keep uncertainty and conditions from the draft.
```

**Application**

> **Before:** The export task has not finished, and as a result we cannot send the report yet.
>
> **After:** The export isn't finished, so we can't send the report yet.

Next time, supply the profile and ask the assistant to apply it to a work message. The file can live outside the skill directory. Unspecified fields do not trigger a questionnaire, and normal rewriting does not require a profile.

</details>

**Current instructions take priority.** Samples and profiles supply style, not facts for the new draft. The skill does not automatically save or update profiles, or train a model on samples. Saving requires an explicit request; the host product controls its own conversation retention.

<a id="installation"></a>

## Installation

This is a **Markdown skill** for a host model. The files provide instructions and examples; no build step is needed.

Download the repository or clone it:

```bash
git clone https://github.com/quqxui/context-aware-humanizer.git
```

1. **Try it locally:** ask your assistant to read [`SKILL.md`](SKILL.md) and the guide for your scenario and language.
2. **Install for reuse:** place `SKILL.md` and `references/` together in your host's skill directory, following that host's setup instructions.
3. **Keep the relative layout intact:** `SKILL.md` routes requests to the appropriate guide.

<details>
<summary><strong>Repository structure and what each part does</strong></summary>

```text
context-aware-humanizer/
├── SKILL.md                  # Shared rules, routing, tones, and personal voice
├── README.md                 # English documentation
├── README.zh.md              # Chinese documentation
├── .github/
│   └── banner.png            # README display only
└── references/
    ├── chat/                 # Every scenario has its own zh.md and en.md
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

For example, Chinese papers use [`references/academic-paper/zh.md`](references/academic-paper/zh.md), while English papers use [`references/academic-paper/en.md`](references/academic-paper/en.md). **Maintain either file independently without synchronizing edits to the other.**

`SKILL.md` holds the shared meaning constraints and instructions for choosing guides, tones, and personal profiles. The README presents user-facing choices, templates, and examples. The banner is for display and is not needed to run the skill.

</details>

---

## Scope and evaluation

The goal is to preserve meaning, fit the context, and improve naturalness without unnecessary edits. Authored examples are not test outputs; systematic cross-model evaluation has not been completed.

The skill does not determine authorship, report an AI percentage, or promise detector outcomes. Editing does not perform independent fact checking, experiments, publication, or submission. Academic writing remains subject to the relevant venue or funder requirements.

## Contributing and license

**Contributions welcome:** add a scenario, a Chinese or English example, or a reproducible failure. See [CONTRIBUTING.md](CONTRIBUTING.md).

Original content is released under the [MIT License](LICENSE). External linked material remains owned by its authors.
