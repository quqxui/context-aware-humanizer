# Academic slides — English

Use for slide text, titles, captions, speaker notes, and visual sequencing. Slides support a talk; they are not a transcript of the paper.

## Worked examples

These fictional examples illustrate editing decisions; they are not model evaluation results.

### Case 1 — Main result

**Request:** Turn the supplied result into one descriptive title and two scannable bullets.

**Source:**

Accuracy increased from 82% to 86% on the same test set. Other datasets have not been evaluated.

**Rewrite:**

**Accuracy increased on the evaluated test set**

- Accuracy: 82% → 86% on the same test set
- Other datasets: not yet evaluated

**Why:** The metric, test-set scope, and evaluation caveat remain; no dataset name is added.

### Case 2 — Study design

**Request:** Make the study design slide self-contained while keeping the supplied sample definition and planned analysis separate.

**Source:**

We enrolled 48 participants with early tissue changes. We will compare the imaging workflow with the reference assessment. The comparison has not yet been completed.

**Rewrite:**

**Study design: cohort and planned comparison**

- Cohort: 48 participants with early tissue changes
- Planned comparison: imaging workflow vs. reference assessment
- Status: comparison not yet completed

**Why:** The cohort size and definition, planned comparator, and incomplete status remain; the slide separates design from future analysis.

## Common formats

- **Conference deck**: make the question, contribution, evidence, and takeaway scannable.
- **Teaching deck**: add definitions and checks for understanding when supplied.
- **Poster-like static deck**: increase local self-containment without overcrowding.
- **Speaker notes**: carry explanation that should not appear on the slide.

## Output

Return a slide-by-slide outline or edited slide text with one main idea per slide, explicit evidence labels, and notes separated from display text.

## Editing guidance

1. Give each slide one main idea and a descriptive title. A request to edit one slide does not call for a complete deck.
2. Compress supplied information into scannable bullets or evidence blocks. Titles and captions must not claim more than the underlying text.
3. Preserve axis labels, units, metrics, sample definitions, comparators, and necessary caveats. Keep each number attached to what it measures.
4. Distinguish observed results, interpretation, and planned work, including “not yet evaluated” or “comparison not yet completed.”
5. Make slide order follow the spoken reasoning. Keep speaker notes separate from display text rather than copying the script onto the slide.
6. Concise noun phrases and fragments can work as bullets. Use parallel grammar where it helps scanning, without deleting scientific qualifiers.
7. Keep technical terms, capitalization, US or UK spelling, and notation consistent. Use direct verbs when they save words without changing the process.

## References

- [Stanford Visuals and PowerPoint](https://oralcommprogram.stanford.edu/presentation-and-delivery/visuals-and-powerpoint)
