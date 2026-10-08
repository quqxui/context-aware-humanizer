# Skill-local style memory verification — 2026-10-08

## Scope and environment

Local macOS, Python 3.13. Python 3.9 syntax was parsed separately, but the suite was not executed on Python 3.9, Windows or Linux. Host-model probes used fresh-context Codex subagents in one session. They are single-sample smoke checks, not a cross-model style-quality evaluation.

All source text below is synthetic. Real personal documents and the repository's own `memory/` were not used. Temporary probe installations were removed after inspection.

## Executable checks

Command: `python3 -m unittest discover -s tests -v`

Result: **28 tests passed** (16 memory storage, 12 packaging/update).

Coverage includes exact language/scenario selection, common fallback, read without creating files, metadata validation, stale revision rejection, cooperating-writer locks, owned-lock cleanup after initialization failure, owner-only directories, backup integrity, atomic replacement failures, malformed/unreadable profiles, symlink paths and ancestors, optional index-refresh failure, public export exclusion, private backup inclusion, direct CLI execution, invalid-update preflight and preservation of memory during updates.

The standalone package was also exported, extracted to a fresh directory and executed from a different working directory. Read, save, read-after-save, private backup and update all completed. The ZIP included the README banner and excluded `memory/`, `.local/`, tests and development docs. The private ZIP included the seeded profile and excluded the lock. Updating the installation preserved the seeded profile byte-for-byte.

Additional checks: skill frontmatter validator passed; 114 local Markdown/HTML links and anchors resolved; all 24 original scenario guides were byte-identical to HEAD; memory and revisions were Git-ignored; no test memory remained in the repository; `git diff --check` passed.

## Host-model probes

### Baseline before persistence support

Request: import supplied A/B chat into persistent Chinese work-message memory inside the skill.

The old skill proposed an unspecified `profiles/zh-work-message.md` location and asked for path confirmation. It did not define a durable location or automatic scenario read contract. This was a read-only baseline, not a persistence test.

### Import: author selection, tentative evidence and persistence

Supplied records (A is the target author):

```text
A: 导出失败了，报告还没发。如果今天恢复，预计明天给初稿。
B: 亲爱的辛苦啦！！！
A: 图改好了，还要再检查一次。今天先别发。
```

The first implemented probe saved a profile but mislabeled two A records as three A messages. Import guidance was narrowed to preserve original source units and counts. A fresh probe then used source record positions 1 and 3 correctly (there are three total source records, two authored by A).

Final saved artifact:

```markdown
---
schema_version: 1
language: zh
scenario: work-message
---
# Writing style

## Explicit constraints
- None confirmed.

## Observed preferences
- [tentative] Use short, direct sentences for progress updates. Evidence: S1, messages 1 and 3.
- [tentative] State the current status before the pending action or restriction. Evidence: S1, messages 1 and 3.
- [tentative] Preserve uncertainty and timing conditions in concise factual wording. Evidence: S1, message 1.
- [tentative] State temporary holds or restrictions directly when they apply. Evidence: S1, message 3.

## Sources
- S1: user-authored Chinese work messages supplied for this import. Three source records. No source facts retained.
```

Observed: read initially returned `missing`; save returned `saved: true`; read-after-save returned this profile with no warnings. No B expressions, project facts or raw document copies were saved. Final SHA-256: `a2fec1e65c4baa71692a71532ad6911ecbd6fd019ad63827b632ea0f0cf967f8`.

### Matching rewrite: current request overrides observed preference

Request: rewrite as a Chinese work message, retaining one complete sentence rather than splitting into short sentences.

Input:

```text
由于测试环境目前尚未恢复，因此我们暂时无法开展回归测试；如果今天恢复，我预计明天可以给出初步结果。
```

Actual output:

```text
由于测试环境目前尚未恢复，我们暂时无法开展回归测试；如果今天恢复，我预计明天可以给出初步结果。
```

Audit: the agent read the Chinese work-message guide, called `read --language zh --scenario work-message`, and received only `work-message`. It did not read the import guide or write memory. The condition, uncertainty and requested one-sentence format were retained.

### Different language/scenario: no-match fallback

Input was an English academic results paragraph with Dataset K, 81% accuracy, a 79% baseline, qualified improvement and no other datasets evaluated.

Actual output:

```text
Our method achieved 81% accuracy on Dataset K, compared with 79% for the baseline. This result may indicate improved performance on this dataset. Other datasets have not been evaluated.
```

Audit: the agent read the English academic-paper guide and called `read --language en --scenario academic-paper`. It received `profiles: []`, `target_revision: missing`, `warnings: []`. It did not read the Chinese source or Chinese work-message memory, and made no memory writes.

## Remaining boundaries

- The scripts validate storage, not the correctness of extracted style. The provenance error demonstrates why inspection and tentative observations still matter.
- Document extraction relies on the host's readers; no PDF/Word parser or OCR is bundled.
- Manually supplied legacy profiles remain in the documented current-task path; this run did not perform a separate legacy-profile generation probe.
- Locks coordinate these scripts; manual editors and third-party installers do not participate. Interrupted processes may leave a lock requiring owner verification before removal.
- Program updates are atomic per file, not an all-files transaction. Backups cover overwritten program files; unknown/obsolete program files are not pruned.
- Copies of a skill have independent memory. No cross-device sync, training, daemon, or background preference collection is implemented.
