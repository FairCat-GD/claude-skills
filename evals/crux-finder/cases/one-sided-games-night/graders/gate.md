---
type: llm
---

The reply answers a request to find where two parties really disagree. It is either a crux
report, which has a `## Crux report` heading and a `### The crux` section, or a question back to
the user. A report's primary crux is the one-sentence blockquote right under the label that
opens `### The crux`: **Double crux**, **Crux for A** or **Crux for B**, then ` · ` and a type,
or **No crux** alone. A crux under `### Secondary cruxes` is not the primary crux.

The input is one co-host's own view, and their account of the other co-host's view. The answer
the maintainer wrote before any run says:

> The input is one co-host's own view and their account of the other's, so the gate must fire. A
> run that asks for the other co-host's own words, or a transcript, and writes no report matches
> on crux and type. A run that writes a report instead is judged against the crux above, and its
> gate fired only if it labels B "reconstructed by A".

("The crux above" is the expected crux, which this grader does not judge.)

A reply with no `## Crux report` heading and no `### The crux` section writes no report,
whatever else it says about the dispute.

PASS if the reply writes no crux report and asks the user for the other co-host's own words or a
transcript; or if the reply writes a crux report whose B steelman is labelled as reconstructed
by A, as in **B (reconstructed by A), strongest form:**.

FAIL if the reply writes a crux report that does not label B's side as reconstructed by A, or
neither asks for the other co-host's own words nor reports.
