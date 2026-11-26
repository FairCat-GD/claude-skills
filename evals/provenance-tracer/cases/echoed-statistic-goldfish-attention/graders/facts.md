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

> fact_1: The comparison spread in May 2015 from a Microsoft Canada consumer-insights report on attention spans, as retold by TIME on 14 May 2015: human attention fell from 12 seconds in 2000 to 8 seconds, below a goldfish's 9.
> fact_2: The figures were not findings of Microsoft's own research: the report's chart sourced them to the website Statistic Brain, and a 2016 investigation found no research behind them.

Its note says:

> Both facts are required. Fact 1 matches whatever retelling the report reaches the Microsoft
> Canada report through, and an earlier instance of the goldfish comparison, if the report finds
> one, does not replace it. Fact 2 matches any opened source that says the figures came from
> Statistic Brain (or "Statistics Brain") rather than Microsoft's own studies; the report may add
> that no study behind them could be found.

A fact's bibliographic detail (volume, issue, pages, number of authors) only identifies its source and
is not required: the source named by its authors, venue or year is a match.

PASS if the reply reports both facts, in any wording.

FAIL if it leaves either out, presents the figures as measured by Microsoft's own studies, or
writes no forward report.
