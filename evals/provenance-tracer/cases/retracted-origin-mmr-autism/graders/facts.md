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

> fact_1: The claim traces to a 1998 paper by Andrew Wakefield and twelve co-authors in The Lancet (vol. 351, pp. 637-641), on 12 children.
> fact_2: The paper reported that parents associated the onset of behavioural symptoms with MMR vaccination in eight of the 12 children.
> fact_3: The paper did not claim to prove that the vaccine causes autism.
> fact_4: The Lancet retracted the paper in full in February 2010; ten of its authors had retracted its interpretation in 2004.

Its note says:

> All four facts are required, except the 2004 clause of fact 4, which is not. Facts 2 and 3
> match any wording that says the paper reported an association in time, reported by parents, in a
> few children, rather than a proven cause. Fact 4 matches a retraction in 2010 by The Lancet. A
> report may add the 2011 BMJ articles that called the paper fraudulent; they are not required.

A fact's bibliographic detail (volume, issue, pages, number of authors) only identifies its source and
is not required: the source named by its authors, venue or year is a match.

PASS if the reply reports facts 1 to 4, in any wording (the 2004 retraction of the
interpretation may be left out).

FAIL if it leaves any of them out, says the paper claimed MMR causes autism, or writes no
forward report.
