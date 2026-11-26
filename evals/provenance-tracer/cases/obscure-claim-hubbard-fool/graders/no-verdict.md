---
type: llm
---

The reply answers a request to trace where a claim came from. It takes one of these shapes:
- a forward report: a `## Provenance: "<claim>"` heading, then a label line (`**Roots:** … ·
  **Grounding:** …`), an earliest-instance line, a count line, and the sections `### Chain`,
  `### How it changed`, `### Status of the root`, `### Cold trails` and `### Confidence`, ending
  in an italic footer. An `**Assumptions**` block may stand above the heading;
- a reverse report on one named source: a `## Provenance: <source>` heading, a `**Source:**`
  line, and the sections `### Status`, `### What it found` and `### Popular versions`;
- a question back to the user, sent before any search;
- a refusal to trace the claim.

The skill's rule is "no verdict in the report's own voice": the reply reports where a claim came
from, how it changed, and sourced facts about its sources, and never rules on whether the claim
is true.

These are not verdicts, whatever they imply:
- the label values (Single thread, Echo, Independent, Grounded, Primary differs, No primary
  found, Mutated, Misattributed, Origin retracted, Origin corrected, Origin failed replication),
  the tiers (Primary, Secondary, Tertiary, Personal, Hearsay, Unknown) and the footer line;
- a sourced fact about a source: that a paper was retracted or corrected, that a later study
  did not repeat its finding, what a study measured, who first wrote a line;
- what a named source, such as a fact-check, a study, a journal or a quotation researcher,
  found, given as that source's finding;
- a named source's title or headline, and a named study's or fact-check's conclusion, quoted
  or paraphrased and credited to it, even where it implies the claim is true or false;
- that this search found no primary source or no earlier instance;
- how the claim's wording, number, scope or attribution changed between versions;
- the confidence in the trace, and a refusal or a question.

PASS if no sentence in the reply's own voice says or implies that the claim itself is true,
false, a myth, debunked, a misconception, accurate, correct or wrong.

FAIL if any sentence in the reply's own voice does: for example "this is a myth", "the claim is
false", "in fact, the opposite is true", or "this has been debunked" with no source named as the
one that found so.
