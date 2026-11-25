---
type: llm
---

The reply answers a request to find where two parties really disagree. It is either a crux
report, which has a `## Crux report` heading and a `### The crux` section, or a question back to
the user. A report's primary crux is the one-sentence blockquote right under the label that
opens `### The crux`: **Double crux**, **Crux for A** or **Crux for B**, then ` · ` and a type,
or **No crux** alone. A crux under `### Secondary cruxes` is not the primary crux.

The expected primary crux, in the answer the maintainer wrote before any run:

> Whether slavery is one of the local differences among the states that bind the Union, or a
> cause of division between them.

Any wording about whether slavery belongs with the local varieties that hold the Union together
or divides it is a match; so is the founders' policy, whether they left slavery wholly to each
State or restricted its spread so that it would die out, since Lincoln rests his account of the
division on it.

The answer also says:

> A run whose primary crux is whether the Union can endure permanently half slave and half free
> counts no for crux and type.

That holds where the endurance of the divided Union is itself the question. A primary crux that
asks whether slavery belongs with the local varieties or divides the Union is a match even where
it also mentions endurance.

PASS if the reply is a crux report whose primary crux is a match.

FAIL if the reply has no crux report, or if its label is **No crux**, or if its primary crux is
about anything else, even where a secondary crux is a match, or if its primary crux is the one
the answer counts no.

Judge only what the primary crux is about: its type label, its exact wording and the rest of the
report do not matter here.
