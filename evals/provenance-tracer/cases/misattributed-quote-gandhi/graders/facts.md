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

The answer the maintainer wrote before any run says:

> fact_1: Gandhi wrote a related but different passage in 1913, in Indian Opinion (The Collected Works of Mahatma Gandhi, vol. XII): if we could change ourselves, the tendencies in the world would also change.
> fact_2: The one-line saying is not found in Gandhi's own writings.
> fact_3: The earliest close match Quote Investigator found is by the educator Arleen Lorrance in 1974, be the change you want to see happen; the saying was credited to Gandhi in print by 1987.

Its note says:

> Facts 1 and 2 are required: the report names Gandhi's 1913 passage, or the 1913 Indian
> Opinion piece, as a text by Gandhi that says something different from the saying, and says the
> one-line saying is not in his writings (in its own voice as a finding of the trace, or as a
> named source's finding). Fact 3 is not required: the earliest instance of the short wording may
> be given as another 1970s or 1980s source, or not found. Any wording of these facts is a match,
> and the 1913 passage may be paraphrased or quoted in another translation.

A fact's bibliographic detail (volume, issue, pages, number of authors) only identifies its source and
is not required: the source named by its authors, venue or year is a match.

PASS if the reply reports both facts 1 and 2, in any wording.

FAIL if it leaves either out, credits the one-line saying to Gandhi's own writings, or writes no
forward report.
