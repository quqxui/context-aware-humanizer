# Academic paper — English

Use for an abstract, introduction, methods, results, discussion, or full manuscript. Keep the target venue, genre, evidence, and LaTeX structure in scope.

## Worked examples

These fictional examples illustrate editing decisions; they are not model evaluation results.

### Case 1 — Results paragraph

**Request:** Remove a framing phrase from the results paragraph while preserving the metric, comparator, uncertainty, and scope.

**Source:**

It is worth noting that our method achieved an accuracy of 86% on Dataset A, compared with 82% for the baseline. These results may indicate improved performance on this dataset. Other datasets have not been evaluated.

**Rewrite:**

Our method achieved 86% accuracy on Dataset A, compared with 82% for the baseline. These results may indicate improved performance on this dataset. Other datasets have not been evaluated.

**Why:** The metric, comparator, hedge, and evaluation scope remain; only the framing phrase is removed.

### Case 2 — Limitations

**Request:** Make the limitations paragraph easier to read without softening its scope or adding a validation plan.

**Source:**

Our evaluation was carried out using retrospective records from a single hospital. As a consequence of not having assessed the model at other hospitals, its generalizability remains uncertain. Prospective validation has not been performed.

**Rewrite:**

Our evaluation used retrospective records from one hospital. We have not assessed the model at other hospitals, so its generalizability remains uncertain. Prospective validation has not been performed.

**Why:** The data source, uncertainty, and lack of prospective validation remain. No promise to validate later is added.

## Common formats

- **Abstract**: compress question, method, result, and implication without adding a conclusion.
- **Introduction**: establish the gap, research question, contribution, and paper map.
- **Methods/results**: prioritize reproducible detail and distinguish observation from interpretation.
- **Discussion**: connect findings to scope, limitations, and prior work without overclaiming.
- **LaTeX pass**: preserve commands, labels, math, citations, and environments exactly unless asked to edit them.

## Output

Return edited prose in place, preserving paragraph order and markup. If a claim needs evidence, flag the gap rather than inventing a citation or result.

## Editing guidance

1. Make each sentence’s role clear: method, observation, interpretation, limitation, or implication. Preserve paragraph order unless restructuring is requested.
2. Use precise nouns and verbs while retaining qualifiers such as “may,” “suggests,” and “under these conditions.” Correlation must not become causation.
3. Expand an abbreviation at first use only when its full form is supplied. Keep terminology, capitalization, US or UK spelling, and notation consistent.
4. Clarify “better” with the supplied metric, baseline, and setting. If these are missing, retain the intended comparison and flag a material gap rather than inventing experimental details.
5. Keep citations attached to the claims they support, and preserve citation commands, math, labels, and LaTeX environments.
6. Prefer direct verbs to unnecessary nominalizations. Retain passive voice when the actor is unknown, irrelevant, or less important than the procedure.
7. Match tense to completed methods, observed results, current interpretations, and future work; do not rewrite a whole paper into one tense.
8. Follow venue and author conventions for contractions and punctuation. Do not invent participants, datasets, analyses, numbers, statistical significance, or novelty claims.

## References

- [Paper Writing Tips](https://github.com/MLNLP-World/Paper-Writing-Tips/tree/50712564062249b28b8493ebdc35f8b3a3b88512)
