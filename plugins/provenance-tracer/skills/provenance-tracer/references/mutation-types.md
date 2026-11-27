# Mutation types

How a claim drifts between its root and the version the user met. Compare the user's version with
the root, the Primary if you opened one, and name every drift you find, each with the node where it
first appears. Each drift found is one row of the report's *How it changed* table, and any drift
at all adds the Mutated modifier.

Every example below is invented, to show the shape: the studies, bodies and numbers do not exist.
Never cite them. Their wordings are in italics, so as not to model quotation marks.

## Finding where a drift first appears

Walk the chain from the root towards the user's version. The first node whose variant of the claim
shows the drift is where it first appears; name that node, its source and its year, in the
*First appears in* column. If the drift is already in every node you opened, it first appears in
the earliest of them. If it shows only in the user's version, write `your version`.

## The six drifts

### Scope widened

The claim now covers more than the root did: more people, places, times or cases.

- Root: a survey of 200 night-shift nurses in one regional hospital.
- Later: *nurses*.
- Later still: *healthcare workers*.

Look for a narrowing word the root had that is gone, such as *in this sample*, *in adults over
60*, *in one county*, *in 2009*.

### Number changed

A figure is rounded, inflated, shrunk, converted, or attached to a different quantity.

- Root: *27% of respondents*.
- Later: *about a third*.
- Later still: *most people*.

A percentage read as an absolute number, a mean read as a typical case, or a figure moved to a
different year all count. Give both figures in the table, the root's first.

### Hedge dropped

The root's uncertainty is gone: *may*, *suggests*, *in this sample*, *preliminary*, *associated
with*, *requires further study*.

- Root: *a small pilot study suggests the coating may reduce corrosion*.
- Later: *the coating reduces corrosion*.

### Correlation stated as causation

The root reports two things that go together. A retelling says one causes the other.

- Root: households with more houseplants reported fewer colds.
- Later: *houseplants prevent colds*.

This is distinct from a dropped hedge. The root may be quite certain of the association and still
claim no cause. Record both drifts where both happened.

### Attribution shifted

The words or finding are credited to someone other than the source they came from. Three forms:

- **Another person.** Words written by a minor author are credited to a famous one.
- **Another source.** A blog's estimate is credited to *a university study*.
- **A paraphrase given as a direct quote.**

This drift always brings the Misattributed modifier too (see `labels.md`).

- Root: a 1971 trade newsletter's editorial on harbour dredging.
- Later: the same line, credited to a well-known engineer, in quotation marks.

### Context removed

What made the root's statement true where it stood is gone.

- Root: a figure from one year's drought: *river levels fell 40% in the dry summer of 2003*.
- Later: *river levels have fallen 40%*.

Other forms:

- a condition dropped;
- a comparison group dropped;
- a joke or a hypothetical read as a plain statement;
- a quote cut so that it says the opposite of the sentence around it.

## Other

Some drifts fit none of the six, such as:

- a date moved;
- a place swapped;
- a fictional work's line read as fact.

Name such a drift plainly in the *Change* column. Do not stretch one of the six to cover it.

## Writing the table

````markdown
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Hedge dropped | a pilot study suggests the coating may reduce corrosion | the coating reduces corrosion | [Coastal Works Weekly](<url as fetched>), 2015 |
````

- **Root says.** Paraphrase the root. Quote it only if the page has no quote anywhere else in the
  reply, linked to that page, in 12 words at most, and never two quotes in one row. A word that changed is
  shown in italics, as in *want* became *wish*, not in quotation marks.
- **Your version.** The user's own words exactly as typed, which are exempt from the quote rule.
- **One row per drift.** Write `None found.` under the heading when there is no drift.
- **No verdict.** The table reports what changed, never which version is true.
