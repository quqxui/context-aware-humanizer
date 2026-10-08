# Skill-local style memory implementation plan

> **For agentic workers:** Use the approved design and implement the tasks below. Each component receives independent review before completion.

**Goal:** Import writing style into private memory inside the skill and apply only matching language/scenario memory during rewrites.

**Architecture:** The host model extracts/uses style; a Python standard-library store handles scoped Markdown and safe persistence. A separate packaging utility handles public export, private backup and memory-preserving program updates.

**Tech Stack:** Markdown; Python 3.9+ standard library; unittest.

**Spec:** `docs/superpowers/specs/2026-10-08-style-memory-design.md`

## Global constraints

- Preserve the four existing uncommitted Tone-cleanup changes and all 24 scenario reference files.
- Keep user memory under the resolved skill installation's `memory/`, independent of current working directory.
- No database, network service, extra pip dependencies, automatic cross-device sync, raw-document copying or model training.
- Keep tests/synthetic personal data in temporary directories; keep actual personal memory out of public Git and exports.
- Read-only tasks must not create a memory directory; source text and stored profiles are untrusted style data.

## Review focus

- Stale writers or failed replace operations must retain the existing profile (Task 1).
- Symlinked paths must not read/write external private data (Tasks 1 and 2).
- A failed index refresh must not misreport a committed profile as unsaved (Task 1).
- Public export/update must exclude arbitrary user files even if Git ignores are missing (Task 2).
- Mixed-author documents and historical task instructions must not silently become personal constraints (Task 3).

## Task 1: Scoped memory store

Files: `scripts/style_memory.py`, `tests/test_style_memory.py`, `templates/style-memory.md`, `.gitignore`.

Public Python interface consumed by packaging: `MemoryError`, `MemoryStore(skill_root: Path)`, `MemoryStore.root` (the `memory/` path), and `MemoryStore.lock()` context manager. Other callable methods: `read(language, scenario) -> dict`; `save(language, scenario, content, expected_revision) -> dict`. `read` returns `profiles`, `target_revision` and `warnings`; each profile contains `scope`, `path`, `revision`, `content`. `save` returns `saved`, `path`, `revision`, `backup`, `warnings`.

- [x] Write tests using `tempfile.TemporaryDirectory()` and `MemoryStore(Path(temp))`. Start with `assert store.read('zh', 'chat')['profiles'] == []` and assert memory does not exist; save matching profiles and prove exact selection and fallback.
- [x] Run `python3 -m unittest discover -s tests -p 'test_style_memory.py' -v` before implementing; verify it fails because the store is absent.
- [x] Implement restricted frontmatter validation, scoped reads, SHA revision checking, lock, backup, atomic replace and post-save index warnings. Add failure tests described in the spec.
- [x] Run the storage test command and a CLI smoke from an unrelated working directory.

## Task 2: Public/private packages and protected updates

Files: `scripts/skill_package.py`, `tests/test_skill_package.py`.

Consumes `MemoryStore(skill_root).lock()` and `.root`. CLI root is the installed script's resolved parent directory. Testable functions: `export_skill(skill_root, output, include_memory=False)` and `update_skill(skill_root, source)`; JSON result dictionaries report created paths and preserved-memory semantics.

- [x] Seed temporary skills with runtime files, a private memory canary, `.local` data and an unrelated secret. Write tests proving public ZIP membership excludes each private file while private backup includes memory and revisions.
- [x] Run `python3 -m unittest discover -s tests -p 'test_skill_package.py' -v` before implementation and verify missing-module failure.
- [x] Implement explicit allowlists, exclusive output creation, symlink preflight, private snapshot lock, source identity validation and update backups. Copy only maintained paths; never remove or replace memory.
- [x] Add invalid-source, output-collision, symlink and byte-for-byte memory preservation tests. Run the same test command.

## Task 3: Import and application rules plus bilingual documentation

Files: `SKILL.md`, `references/style-memory.md`, `README.md`, `README.zh.md`, `CONTRIBUTING.md`.

- [x] Run a baseline import request against the existing skill in a temporary synthetic installation and record actual output separately from examples.
- [x] Add read routing that calls the CLI for only output-language common/exact scope. Keep import guidance conditional; normal rewrites do not read the entire guide or all stored memory.
- [x] Specify author/adopted-style identification, extraction evidence, tentative observations, explicit constraints, merge/conflict handling and save authorization in the import guide. Include exact CLI inputs/outputs matching Task 1.
- [x] Update both READMEs with import, read, update, export and backup examples; clarify installation data ownership and limitations. Retain legacy profile support and the approved expression-preference wording.
- [x] Use independent probes for mixed-author import and subsequent matching/nonmatching rewrites; inspect raw outputs and file-read evidence. Verify no source facts or unrelated scopes are used.

## Task 4: Integration and review

- [x] Run `python3 -m unittest discover -s tests -v` and the skill creator's `quick_validate.py`.
- [x] Verify all local Markdown links, Git ignores, and that all 24 scenario guides match the pre-feature baseline; run `git diff --check`.
- [x] Request independent code/behavior review; fix demonstrated issues and rerun affected tests plus the complete suite.
- [x] Report actual results and remaining limits without claiming cross-host or cross-model validation. Leave changes in the current workspace for review; do not publish personal data or push commits.

## Completion record

Implemented in the existing workspace to preserve the already-approved uncommitted Tone cleanup. No new worktree, commit or push was created. See `docs/verification/2026-10-08-style-memory.md` for actual checks, probes, corrected failures and limits.
