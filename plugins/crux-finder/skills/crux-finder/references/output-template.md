# The crux report

The exact format of every report. Keep every heading, in this order. The whole report is at most
400 words, and it ends at Confidence: nothing follows it but the claim map, appended only on
request, which does not count toward the 400.

## The caps

Each section has a cap in words. A section's words are everything under its heading, its labels
included; a steelman's are those after its label. The caps add up to under 400 with the headings
and labels, so a report inside every cap is inside 400, however long the input. A long input
gets the same caps as a short one: say less about each point, never more.

| Section | At most |
| --- | --- |
| Each steelman | 45 words |
| Common ground | 40 words in all, at most 3 lines |
| The crux | 130 words in all: the crux sentence at most 25, each of the four fields at most 22 |
| Secondary cruxes | 50 words in all: one, or two short ones; most reports have none or one |
| Not actually in dispute | 30 words in all, at most 2 lines |
| Confidence | 25 words, one sentence |

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

- **The steelman lines.** 2 to 4 sentences each, at most 45 words: the conclusion and the
  reasons it most rests on, never a list of every reason the input gives, with `[inferred]`
  after each premise the input does not state. Where the input names its parties, add the name
  or role in brackets, in at most three words: `**A (<name or role>), strongest form:**`. After a one-sided input:
  `**B (reconstructed by A), strongest form:**`.
- **Common ground.** One short line per claim both accept, at most three and 40 words in all,
  the ones the crux stands on. A claim only one party makes is not common ground.
- **The crux label.** One of `Double crux`, `Crux for A` or `Crux for B`, then ` · ` and the
  type: `**Crux for B · Value**`. When the positions do not conflict, the label is
  `**No crux**` alone.
- **The crux sentence.** One sentence of at most 25 words in a blockquote: your own neutral
  wording, which both parties would accept as fair, with no loaded term from either side.
- **The four fields** below it are one sentence each, at most 22 words.
- **A holds, B holds.** Each side's view of the crux claim, in one sentence, paraphrased without
  quotation marks unless the words are verbatim from the input.
- **If A accepted B's view here.** One sentence, both directions: what would happen to A's
  conclusion, then the reverse, `If A accepted B's view here: …; if B accepted A's: …`. For a
  crux for one party, the reverse says the other's conclusion would stand.
- **What would move it.** One sentence: the resolution path for the crux's type (procedure,
  step 8). For a Value crux, the trade-off, with no resolution. Name the evidence or the
  forecast; do not list every check that would go into it.
- **Secondary cruxes.** At most two, one line each and 50 words in all, with the primary crux's
  fields in the same order, each a short clause. Each needs a side from each party, as
  procedure step 5 has it: a point one party never addresses is no crux, so never write that a
  side is not addressed, or invent one for a party whose words never touch the point. With
  none, the section says `None.`

  ```markdown
  - **Crux for A · Predictive**: <the crux sentence> A holds: …; B holds: …; if accepted: …; what would move it: …
  ```

- **Not actually in dispute.** Apparent disagreements that dissolve once a word is defined or the
  questions are told apart, one line each, at most two and 30 words in all. It never repeats
  Common ground: a claim both accept goes there, not here. With none, the section says `None.`
- **Confidence.** `High`, `Medium` or `Low`, then the reason in one sentence, 25 words in all.
  After a one-sided input it is at most `Low`, and it suggests sharing the report with B to
  confirm their side.
- **An empty section** keeps its heading and says `None.`
- **Quotation marks** hold only text copied verbatim from the input, its capitals included:
  never your own words, a question you pose, a section's label, or one of this template's
  labels, such as reconstructed by A. A quotation keeps the input's first letter as it is,
  capital or lower case, wherever it falls in your sentence; where that reads wrong, reword the
  line around the quotation rather than change the letter.
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

The note counts toward the 400 words, so this report's Secondary cruxes says `None.`

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
