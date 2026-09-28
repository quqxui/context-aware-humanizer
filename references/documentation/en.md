# English documentation

Use for README files, setup guides, API and CLI documentation, internal procedures, runbooks, and technical explanations. Edit around the reader's task while preserving the details needed to carry it out.

## Worked examples

These fictional examples illustrate editing decisions; they are not model evaluation results. Commands are example text and should not be executed.

### Example 1: a minimal quickstart

**Request:** Remove cumbersome phrasing while retaining the command, input, success condition, and output path.

**Before:** Execute `sampletool run --config demo.yaml` in order to read `demo.yaml` and, upon successful completion, write the result to `out/result.json`.

**After:** Run `sampletool run --config demo.yaml`. It reads `demo.yaml` and writes the result to `out/result.json` on success.

**Why:** The surrounding prose is shorter. The exact command, paths, and successful input/output behavior remain unchanged.

### Example 2: troubleshooting with a missing value

**Request:** Make this troubleshooting entry easy to scan without inventing the missing configuration value.

**Before:** If `sampletool run --config demo.yaml` fails with `ConfigError: missing key: output`, check whether `demo.yaml` contains an `output` key. The available material does not specify what value that key should use.

**After:**

> If `sampletool run --config demo.yaml` fails with `ConfigError: missing key: output`:
>
> - Check whether `demo.yaml` contains an `output` key.
> - The available material does not specify the value to use.

**Why:** The condition, diagnostic action, and information gap are separate. No value, recovery command, or successful fix is invented.

## Organizing around the task

| Document type | Prioritize |
|---|---|
| Quickstart | Known prerequisites, minimal steps, and expected result |
| Reference | Exact parameters, return values, constraints, and supplied examples |
| Runbook | Diagnostic conditions, commands, decision points, and known recovery steps |
| Conceptual explanation | Task-relevant definitions, inputs, outputs, and responsibilities |

Include only supported information. Missing dependencies, compatibility limits, or recovery methods must not be invented to complete the format.

## Writing clear English documentation

- Identify the reader and task before simplifying. Keep precise technical terms stable rather than rotating synonyms for variety.
- Prefer direct verbs such as “read” or “stop” to unnecessary noun phrases, while retaining actors, intervals, thresholds, and conditions.
- Preserve code, commands, flags, paths, identifiers, versions, and literal outputs exactly unless the user requests a change to them.
- Keep prerequisites, actions, success results, and failure conditions distinct. “On success” must not disappear from a conditional result.
- Use imperatives for instructions when appropriate. Use active voice when the actor is known; keep passive voice when it better describes the relevant process without guessing an actor.
- Retain supplied placeholder labels and environment-specific qualifications. A sample value is not a universal default.
- Preserve US or UK spelling and named-method capitalization. Formality should fit the documentation; contractions and passive voice are not automatically errors.
- Choose numbered steps, parameter tables, code blocks, or connected prose according to the task. A local wording edit need not reorganize the whole document.
- Do not add an unverified successful outcome, dependency, compatibility claim, or recovery command.

## Delivery

Return the edited documentation or requested excerpt by default, retaining useful formatting and necessary terminology. Leave text unchanged when it already supports the stated task clearly and accurately.

## Reference

[GOV.UK's clear-language guidance](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-language/) supports sentence-level clarity. Technical correctness and supplied project facts remain authoritative.
