# Peer review — English

Use when editing the user's own review report or assessment. Preserve the reviewer's actual observations, standards, and recommendation; do not generate criticism for an unread paper.

## Worked examples

These fictional examples illustrate editing decisions; they are not model evaluation results.

### Case 1 — Actionable major concern

**Request:** Make the concern and requested action more direct while keeping the reviewer's evidence.

**Source:**

My concern is that the reported results are based on only one random seed. I ask the authors to repeat the experiments with multiple seeds and provide the mean and standard deviation.

**Rewrite:**

I am concerned that the reported results use only one random seed. I ask the authors to repeat the experiments with multiple seeds and report the mean and standard deviation.

**Why:** The one-seed evidence and requested experiment remain; the wording becomes easier to act on without changing severity.

### Case 2 — Justified positive assessment

**Request:** State the supplied strength and recommendation clearly, while retaining the stated limitation.

**Source:**

One strength of this paper is that it provides an evaluation of the proposed method on two datasets, reporting consistent gains over the baseline. I find the analysis clear, although the paper does not discuss performance outside these datasets. My recommendation is acceptance.

**Rewrite:**

A strength of this paper is its evaluation on two datasets, with consistent gains over the baseline. I find the analysis clear, although performance outside these datasets is not discussed. I recommend acceptance.

**Why:** The two datasets, consistent gains, clear analysis, limitation, and recommendation all remain; no extra praise or criticism is added.

## Common formats

- **Summary**: state the paper's claimed question and contribution as represented in the manuscript.
- **Major concerns**: identify a concrete issue, its evidence, and its effect on validity or clarity.
- **Minor comments**: separate local corrections from decision-level concerns.
- **Confidential comments**: follow the venue's policy and do not move private information into public comments.

## Output

Return the edited review with sections for summary, strengths, major concerns, minor comments, and recommendation only when those sections exist in the input. Keep criticism actionable and traceable.

## Editing guidance

1. Tie each concern to a claim, section, figure, experiment, or omission supplied by the user. Do not invent criticism of material that has not been provided.
2. Separate evidence, interpretation, and requested action so authors can tell what they need to address.
3. Preserve severity and the reviewer’s actual judgment. Do not turn an established issue into a guess, or a concern into a definitive finding.
4. Acknowledge strengths only when supplied; do not invent courtesy praise or speculate about author intent.
5. Preserve the recommendation and any score. If they conflict with the discussion, flag the inconsistency outside the review rather than changing the decision.
6. Keep distinctions among “I suggest,” “I ask,” and “the authors must.” A polite edit must not weaken a requirement or intensify criticism.
7. Use clear, direct sentences and stable technical terms. Preserve suitable hedges, passive constructions, quotations, notation, and the reviewer’s degree of formality.
8. Keep confidential comments separate from public comments and follow supplied venue rules. Do not invent flaws, missing experiments, citations, conflicts, or policy violations.

## References

- [Paper Rebuttal Tips](https://github.com/MLNLP-World/Paper-Rebuttal-Tips/tree/4fe2b488c1ebc83eba9c91fbd2fc2eb51abeba4c)
