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
  <a href="#voice-options">Expression preferences</a> ·
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
| **Your own voice** | **Preserve your voice by default.** Describe the changes you want, supply writing samples, or reuse an editable personal profile. |

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

## 🎙️ Describe your expression preferences

The default is to **preserve the original voice** while adapting the text to its context. Describe any changes you want in your own words:

- “This is a message to a colleague. Put the requested action before the background.”
- “This is a reviewer response. Keep the wording polite and the disagreement clear.”
- “This is a message to a friend. Make it conversational without adding pleasantries.”

These are examples of requests, not fixed categories. Already suitable text can stay unchanged. Preferences apply to the current request and do not automatically become a lasting profile. They persist only after an explicit import, remember, save, or update request.

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

### Import supplied documents into memory

Use a natural-language request when you want a reusable memory entry. State the documents, target author, language, and scope. Ask for a preview if you want to inspect the merge before saving:

```text
These two files are my Chinese work-message samples. Treat only text written by me as evidence.
Import the observable style for the work-message scenario and remember it for future Chinese work messages.
Keep source facts out of the profile. Show the merged profile and save it after checking for conflicts.
```

The host uses its available document tools to read supplied files. The storage scripts save derived style data and minimal source labels; they do not parse `docx` or `pdf` themselves. A sample-derived pattern with limited evidence stays tentative. An explicit user preference can become a confirmed constraint.

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

This skill contains Markdown guidance and Python 3.9+ standard-library scripts for optional persistent memory and packaging. Ordinary text editing needs the Markdown files only. Persistent memory and package operations need a writable installation and Python 3.9 or newer.

Download the repository or clone it:

```bash
git clone https://github.com/quqxui/context-aware-humanizer.git
```

1. **Try it locally:** ask your assistant to read [`SKILL.md`](SKILL.md) and the guide for your scenario and language.
2. **Install for reuse:** copy `SKILL.md`, `references/`, `scripts/`, and `templates/` together into one writable skill directory. Keep the relative layout intact.
3. **Use the optional memory features:** ensure Python 3.9+ is available. If it is unavailable, ordinary editing still works; persistent memory is reported as unavailable and is not claimed as applied or saved.

### Persistent style memory

An installed copy can keep style memory from user-authorized imports under its private `memory/` directory. The memory may contain tentative observations from supplied samples. The root is derived from the installed script path, so commands work from any current directory. Routine rewrites read only same-language `common` and exact-scenario profiles.

```bash
python3 <skill-root>/scripts/style_memory.py read --language zh --scenario work-message
python3 <skill-root>/scripts/style_memory.py save \
  --language zh --scenario work-message \
  --input /tmp/profile.md --expected-revision HASH
```

Use `--expected-revision missing` for a new scope. `read` returns `profiles`, `target_revision`, and `warnings`. `save` returns `saved`, `path`, `revision`, `backup`, and `warnings`. Save only after the user explicitly asks to import, remember, save, or update. Preview and ordinary rewriting are read-only. See [`references/style-memory.md`](references/style-memory.md) for author checks, merge conflicts, and the profile template.

Package an installation or make a private backup with:

```bash
python3 <skill-root>/scripts/skill_package.py export --output /outside/context-aware-humanizer.zip
python3 <skill-root>/scripts/skill_package.py backup --output /outside/context-aware-humanizer-private.zip
python3 <skill-root>/scripts/skill_package.py update --source /path/to/new-skill
```

`export` uses an allowlist for maintained runtime files, documentation, templates, and the README display banner. It excludes private memory and local artifacts. `backup` includes memory and revisions. `update` copies maintained program files and preserves the target installation's memory. Outputs are created exclusively; an existing output is not overwritten.

The writable installation owns its memory. Public Git and public exports exclude it. Separate installations do not synchronize. A third-party installer or update tool can still remove user data, and this first release does not provide automatic cross-device sync. The scripts do not parse `docx` or `pdf`; the host reads supplied documents with its available document tools.

<details>
<summary><strong>Repository structure and what each part does</strong></summary>

```text
context-aware-humanizer/
├── SKILL.md                  # Shared rules, routing, and expression preferences
├── README.md                 # English documentation
├── README.zh.md              # Chinese documentation
├── .github/
│   └── banner.png            # README display only
├── scripts/                  # Python 3.9+ memory and packaging tools
├── templates/                # Public profile templates
├── memory/                   # Private generated memory; absent until first save
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

`SKILL.md` holds the shared meaning constraints, scenario routing, and guidance for expression preferences and personal profiles. The README presents usage examples and profile templates. `scripts/` provides optional persistence and packaging operations. `memory/` is private generated data and is not part of public exports. The banner is included by the public package for README display.

</details>

---

## Scope and evaluation

The goal is to preserve meaning, fit the context, and improve naturalness without unnecessary edits. Authored examples are not test outputs; systematic cross-model evaluation has not been completed.

The skill does not determine authorship, report an AI percentage, or promise detector outcomes. Editing does not perform independent fact checking, experiments, publication, or submission. Academic writing remains subject to the relevant venue or funder requirements.

## Contributing and license

**Contributions welcome:** add a scenario, a Chinese or English example, or a reproducible failure. See [CONTRIBUTING.md](CONTRIBUTING.md).

Original content is released under the [MIT License](LICENSE). External linked material remains owned by its authors.
