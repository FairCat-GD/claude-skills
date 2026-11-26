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

> fact_1: Banuazizi and Movahedi, Interpersonal dynamics in a simulated prison: A methodological analysis, American Psychologist 30(2):152-160, 1975.
> fact_2: Reicher and Haslam, Rethinking the psychology of tyranny: The BBC prison study, British Journal of Social Psychology 45(1):1-40, 2006.
> fact_3: Carnahan and McFarland, Revisiting the Stanford Prison Experiment: Could participant self-selection have led to the cruelty?, Personality and Social Psychology Bulletin 33(5):603-614, 2007.
> fact_4: Le Texier, Debunking the Stanford Prison Experiment, American Psychologist 74(7):823-839, 2019.

Its note says:

> These are four major published critiques of the experiment (Haney, Banks and Zimbardo,
> 1973). The report's Status must name at least two of them, by their authors, with the year or
> the venue. A critique named with a one-line account of its argument in any wording matches.
> Other published critiques or replications may be listed too; journalism such as Ben Blum's 2018
> article counts toward none of the four.

A fact's bibliographic detail (volume, issue, pages, number of authors) only identifies its source and
is not required: the source named by its authors, venue or year is a match.

PASS if the reply is a reverse report whose `### Status` section (or, if it writes a forward
report instead, its status section) names at least two of the four critiques in facts 1 to 4,
each by its authors with its year or venue.

FAIL if it names fewer than two of them in its status section, or writes no report.
