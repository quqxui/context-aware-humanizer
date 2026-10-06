# English work messages

Use for workplace chat, email, status updates, handoffs, follow-ups, requests, and escalations. Make the subject, action, owner, timing, and blockers easy to find.

## Worked examples

These fictional examples illustrate editing decisions; they are not model evaluation results.

### Example 1: staging status and handoff

**Request:** Turn this status note into a handoff while keeping the owner, deadline, and deployment boundary.

**Before:** The payment API timeout fix is now in staging, while production is still on the previous version. Qiao is handling regression checks, and those checks need to be completed by 16:00 tomorrow.

**After:** The payment API timeout fix is in staging; production is still on the previous version. Qiao, please complete regression checks by 16:00 tomorrow.

**Why:** The note becomes a request Qiao can act on. Staging and production remain distinct, and the deadline is unchanged; no production deployment is promised.

### Example 2: an unresolved dependency

**Request:** Clarify the status and blocker without adding a deadline or a commitment.

**Before:** The design review was uploaded yesterday, but the mobile team has not yet provided confirmation of the API field. I need that confirmation before I can proceed with updating the integration branch.

**After:** The design review was uploaded yesterday. The mobile team has not confirmed the API field. I need that confirmation before updating the integration branch.

**Why:** Completed work and the unresolved dependency are separate. The branch update still depends on confirmation; no new owner, deadline, or escalation appears.

## Organizing the message

| Purpose | Prioritize |
|---|---|
| Status update | Current state, supporting evidence, and material impact |
| Request | The action, owner, and necessary context |
| Follow-up | The earlier item, current blocker, and response needed |
| Escalation | Known impact, attempted resolution, and decision needed |

Use only information supplied in the draft. These are useful fields, not requirements to invent missing details.

## Writing clear English at work

- Put the subject and action early. One acknowledgement can remain one line; several independent handoff items may benefit from bullets.
- Use familiar verbs instead of unnecessary noun phrases. Keep project terminology and named procedures stable.
- Distinguish completed, pending, and proposed work. Preserve tense and environment qualifiers such as “in staging.”
- Retain exact owners, identifiers, commands, dates, times, and dependencies. Do not resolve a relative date without the required context.
- Keep “can,” “expect,” “plan,” “must,” and conditional phrases at their original strength. Friendliness must not make a requirement optional.
- Contractions are appropriate when the audience and author's style support them. Preserve US or UK spelling; do not make every message sound like a formal letter.
- Use active voice when the actor is supplied and useful. Keep passive wording when the actor is unknown or irrelevant.
- Do not append generic thanks, “let me know,” pressure, or blame that the message does not need.

## Delivery

Return the sendable text by default. Preserve suitable email, paragraph, or list formatting; do not expand a short update into a report. Leave a clear, appropriate draft unchanged.

## Reference

[GOV.UK's clear-language guidance](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-language/) supports direct phrasing; it does not supply missing project facts or commitments.
