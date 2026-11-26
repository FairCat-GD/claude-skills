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

> fact_1: Jerry Morris and colleagues reported in The Lancet in November 1953 (Coronary heart-disease and physical activity of work) that London's bus conductors, who climbed the stairs, had less coronary heart disease than the seated drivers.
> fact_2: Ralph Paffenbarger and colleagues found the same inverse link in cohorts of their own: San Francisco longshoremen (New England Journal of Medicine, May 1970), and 16,936 Harvard alumni whose risk of a first heart attack fell as their reported energy expenditure rose (American Journal of Epidemiology, September 1978).

Its note says:

> The report must name two or more studies with their own data as separate roots. The full
> match is Morris's 1953 study and a Paffenbarger study (1970 or 1978) as two roots. One of them
> with another study of its own data by other authors as a second root also matches. Two
> Paffenbarger studies alone are one research programme, not two independent roots. A review or
> guideline that weighs earlier studies is not a root of its own. The report may flag the move
> from work activity to exercise as a drift.

A fact's bibliographic detail (volume, issue, pages, number of authors) only identifies its source and
is not required: the source named by its authors, venue or year is a match.

PASS if the reply names Morris's 1953 study or a Paffenbarger study (1970 or 1978) as a root,
and at least one other study with its own data, by other authors, as a separate root.

FAIL if it names neither Morris 1953 nor a Paffenbarger study as a root, names only one root,
or writes no forward report.
