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

> fact_1: The idea has been linked to the psychologist William James, whose essay The Energies of Men (1907) says people make use of only a small part of their possible mental and physical resources, and gives no percentage.
> fact_2: The ten-percent figure was in print by the 1920s and 1930s, for example in Lowell Thomas's 1936 preface to Dale Carnegie's How to Win Friends and Influence People, which credits James with saying the average person develops only ten percent of their latent mental ability.
> fact_3: No study is the source of the figure: Scientific American (2008) says there is no definitive culprit for starting it.

Its note says:

> Facts 1 and 2 are required. For fact 2, any printed instance of the ten-percent figure from
> the 1920s or 1930s matches: Thomas's 1936 preface, the 1929 World Almanac, or John W.
> Campbell's 1932 story, each of which the Wikipedia article names. Fact 3 is not required. Any
> wording is a match; the report may give James's link through a source that names it.

A fact's bibliographic detail (volume, issue, pages, number of authors) only identifies its source and
is not required: the source named by its authors, venue or year is a match.

PASS if the reply reports both facts 1 and 2, in any wording.

FAIL if it leaves either out, gives James a percentage he did not write, or writes no forward
report.
