---
type: llm
---

The reply answers a request to find where two parties really disagree. It is either a crux
report, which has a `## Crux report` heading and a `### The crux` section, or a question back to
the user. A report's primary crux is the one-sentence blockquote right under the label that
opens `### The crux`: **Double crux**, **Crux for A** or **Crux for B**, then ` · ` and a type,
or **No crux** alone. A crux under `### Secondary cruxes` is not the primary crux.

The expected type of the primary crux is Empirical. The answer the maintainer wrote before any
run says:

> A run whose primary crux is whether the Union can endure permanently half slave and half free
> counts no for crux and type.

That holds where the endurance of the divided Union is itself the question. A primary crux that
asks whether slavery belongs with the local varieties or divides the Union is a match even where
it also mentions endurance.

PASS if the reply is a crux report whose primary crux's label names the type Empirical,
whichever of Double crux, Crux for A or Crux for B comes before it, and whose primary crux is
not, by that rule, whether the Union can endure permanently half slave and half free.

FAIL otherwise.

Judge only the type the label names, as the report writes it, and the rule above; do not judge
whether that type is right for the crux.
