# The crux report

The exact format of every report. Keep every heading, in this order. The whole report is at most
400 words, and it ends at Confidence: nothing follows it but the claim map, appended only on
request, which does not count toward the 400.

## The budget

Aim for about 350 words, so the report stays under 400 when a section runs long:

| Section | At most |
| --- | --- |
| Each steelman | 50 words |
| Common ground | 3 lines |
| The crux | its sentence, then four fields of one sentence each, about 25 words a field |
| Secondary cruxes | 2, one line each; most reports have none or one |
| Not actually in dispute | 2 lines |
| Confidence | 1 sentence |

## The template

````markdown
## Crux report

**A, strongest form:** …
**B, strongest form:** …

### Common ground
- …

### The crux
**Double crux · Empirical**
> One sentence, neutral wording both parties would accept as a fair statement of the dispute.

- A holds: …
- B holds: …
- If A accepted B's view here: … (and the reverse)
- What would move it: …

### Secondary cruxes
Max 2. Same fields, one line each.

### Not actually in dispute
- Apparent disagreements that dissolve under definitions or framing.

### Confidence
High | Medium | Low, with the reason.
````

## The rules

- The crux sentence uses no loaded term from either side.
- Text shown as a quote must appear verbatim in the input.
- Steelman lengths for A and B within ±25% of each other by word count.

## Filling it in

- **The steelman lines.** 2 to 4 sentences each, at most 50 words, with `[inferred]` after each
  premise the input does not state. Where the input names its parties, add the name or role in
  brackets: `**A (<name or role>), strongest form:**`. After a one-sided input:
  `**B (reconstructed by A), strongest form:**`.
- **Common ground.** One line per claim both accept, at most three, the ones the crux stands on.
  A claim only one party makes is not common ground.
- **The crux label.** One of `Double crux`, `Crux for A` or `Crux for B`, then ` · ` and the
  type: `**Crux for B · Value**`. When the positions do not conflict, the label is
  `**No crux**` alone.
- **The crux sentence.** One sentence in a blockquote: your own neutral wording, which both
  parties would accept as fair, with no loaded term from either side.
- **A holds, B holds.** Each side's view of the crux claim, in one sentence, paraphrased without
  quotation marks unless the words are verbatim from the input.
- **If A accepted B's view here.** One sentence, both directions: what would happen to A's
  conclusion, then the reverse, `If A accepted B's view here: …; if B accepted A's: …`. For a
  crux for one party, the reverse says the other's conclusion would stand.
- **What would move it.** One sentence: the resolution path for the crux's type (procedure,
  step 8). For a Value crux, the trade-off, with no resolution. Name the evidence or the
  forecast; do not list every check that would go into it.
- **Secondary cruxes.** At most two, one line each, with the primary crux's fields in the same
  order. Each needs a side from each party, stated in the input: a point one party never
  addresses is no crux, so never write that a side is not addressed, or give it an `[inferred]`
  side. With none, the section says `None.`

  ```markdown
  - **Crux for A · Predictive**: <the crux sentence> A holds: …; B holds: …; if accepted: …; what would move it: …
  ```

- **Not actually in dispute.** Apparent disagreements that dissolve once a word is defined or the
  questions are told apart, one line each, at most two. It never repeats Common ground: a claim
  both accept goes there, not here. With none, the section says `None.`
- **Confidence.** `High`, `Medium` or `Low`, then the reason in one sentence. After a one-sided
  input it is at most `Low`, and it suggests sharing the report with B to confirm their side.
- **An empty section** keeps its heading and says `None.`
- **Quotation marks** hold only text copied verbatim from the input, its capitals included:
  never your own words, a question you pose, a section's label, or one of this template's
  labels, such as reconstructed by A.
- **The end.** The report is the whole answer to the user's question. Nothing follows
  Confidence: no short answer, no summary, no closing note.

## When the positions do not conflict

````markdown
### The crux
**No crux**
> One neutral sentence saying why both positions can hold at once.

### Secondary cruxes
None.
````

Every other section is filled in as usual.

## When you are one of the parties

The report's first line, above `## Crux report`, says so and recommends a fresh session:

````markdown
**Note:** I am one of the two parties in this disagreement. For a fair reading, start a fresh
session and paste this conversation's transcript as the input.

## Crux report
````

## The claim map, on request

Appended after Confidence, only when the user asks for it, one line per claim from step 3:

````markdown
### Claim map
- **A1** (stated · conclusion) …
- **A2** (stated · premise) … Depends on: none.
- **A3** (inferred · premise) … Depends on: A2.
- **B1** (stated · conclusion) …
````

## A question, not a report

When the gate stops (a one-sided input, or anything else), the reply is the question alone: one
short message, with no report headings. Name any label it mentions without quotation marks.
