---
type: llm
---

The reply answers a request to find where two parties really disagree. It is either a crux
report, which has a `## Crux report` heading and a `### The crux` section, or a question back to
the user. A report's primary crux is the one-sentence blockquote right under the label that
opens `### The crux`: **Double crux**, **Crux for A** or **Crux for B**, then ` · ` and a type,
or **No crux** alone. A crux under `### Secondary cruxes` is not the primary crux.

The expected primary crux, in the answer the maintainer wrote before any run:

> Whether a £2 door charge would put off people coming for the first time.

The input is one co-host's own view, and their account of the other co-host's view. The answer
also says:

> The input is one co-host's own view and their account of the other's, so the gate must fire. A
> run that asks for the other co-host's own words, or a transcript, and writes no report matches
> on crux and type. A run that writes a report instead is judged against the crux above, and its
> gate fired only if it labels B "reconstructed by A".

A reply with no `## Crux report` heading and no `### The crux` section writes no report,
whatever else it says about the dispute.

PASS if the reply writes no crux report and asks the user for the other co-host's own words or a
transcript; or if the reply is a crux report whose primary crux is about the same question as
the expected crux.

FAIL if the reply is a crux report whose label is **No crux** or whose primary crux is about
anything else, even where a secondary crux is a match, or if the reply neither asks for the
other co-host's own words nor reports.

Judge only what the primary crux is about, or whether the reply asks for the other co-host's
words: its type label, its exact wording and the rest of the reply do not matter here.
