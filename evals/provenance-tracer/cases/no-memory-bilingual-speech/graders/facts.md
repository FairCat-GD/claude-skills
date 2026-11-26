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

> must_1: The reply is a forward report traced from the web alone, with no personal chain: where the user met the claim is not given.
> must_2: The reply asks the user nothing.

Its note says:

> The user has said they don't remember, so the skill has nothing to ask. Must 1 matches a
> *Your version* line that says where the user met the claim is not given, or an assumptions line
> that says it was traced from the web alone. Must 2 fails on any question to the user, anywhere
> in the reply, including an offer that asks the user to reply.

A fact's bibliographic detail (volume, issue, pages, number of authors) only identifies its source and
is not required: the source named by its authors, venue or year is a match.

PASS if the reply is a forward report traced without a personal chain, and contains no
question to the user.

FAIL if it asks the user anything, invents a personal chain, or writes no forward report.
