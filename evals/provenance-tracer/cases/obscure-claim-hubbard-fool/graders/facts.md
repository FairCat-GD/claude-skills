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

> fact_1: The earliest instance found is in Hubbard's own periodical, The Philistine, in November 1909 (vol. 29, no. 6, p. 192), with ten minutes, not five: every man is a dam fool at least ten minutes a day, and wisdom consists in not exceeding the limit.
> fact_2: Hubbard's five-minute version appeared in The Philistine in January 1910 (vol. 30, no. 2, p. 57), without the wisdom clause.
> fact_3: Dale Carnegie's How to Stop Worrying and Start Living (1948) quotes Hubbard with the five-minute version and the wisdom clause together.

Its note says:

> Fact 1 is required, with its ten minutes, and at least one of facts 2 and 3, showing where
> the five-minute form came from. The Philistine may be named as edited or published by Hubbard;
> its issue and page are not required. Quote Investigator's post of 20 November 2026 is the
> source; the report may reach the same facts through another source that names them.

A fact's bibliographic detail (volume, issue, pages, number of authors) only identifies its source and
is not required: the source named by its authors, venue or year is a match.

PASS if the reply reports fact 1, including that the 1909 version says ten minutes, and at
least one of facts 2 and 3, in any wording.

FAIL if it leaves fact 1 out, gives the earliest version as five minutes, reports neither fact 2
nor fact 3, or writes no forward report.
