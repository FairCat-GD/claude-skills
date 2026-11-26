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

> fact_1: The figure is the Office for National Statistics' own: its bulletin International migration, England and Wales: Census 2021, released 2 November 2022, says one in six usual residents of England and Wales were born outside the UK (10.0 million, 16.8%).

Its note says:

> Fact 1 is required: the report names the Office for National Statistics' Census 2021
> release as the root, with the one-in-six figure or 10.0 million or 16.8%. Another ONS page that
> gives the same Census 2021 figure, such as a census overview, matches. News retellings are not
> required.

A fact's bibliographic detail (volume, issue, pages, number of authors) only identifies its source and
is not required: the source named by its authors, venue or year is a match.

PASS if the reply names an Office for National Statistics Census 2021 publication as the
source of the figure, with the figure as one in six, 10.0 million or 16.8%.

FAIL if it does not, or writes no forward report.
