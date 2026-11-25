# Changelog

All notable changes to provenance-tracer are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow `major.minor.fix`.

## [Unreleased]

## [0.1.0] — 2026-11-25

The first release, in development: it works end to end, and its behaviour may still change
before 1.0.0.

### Added

- **Trace where a claim came from.** Type a belief, a statistic or a quote and ask where it came
  from. The skill searches the web and follows each retelling back through what it cites to the
  earliest instance it can find, opening every page it uses. It shows you the chain, from your
  version down to its root, with a date for each source and where that date came from.
- **See how it changed.** A table sets the root's version beside yours and names each change, such
  as a widened scope, a changed number, a dropped hedge, a correlation retold as a cause, a shifted
  attribution or lost context, with the source where it first appears.
- **Two labels on every trace.** *Roots* says whether the claim has one origin or several
  independent ones. *Grounding* says whether an original source was found and opened, and whether
  it says what your version says. Notes such as *Misattributed* or *Origin retracted* follow.
- **The status of the original.** For a study or document at the root, the report lists any
  retraction, correction, failed replication or major later study, each linked.
- **Start from a source instead.** Name a study, book, speech or document and ask what it really
  found. You get its status, what it found in at most three sentences, how its popular versions
  differ, and, if you name beliefs that rest on it, how far it supports each.
- **Where you met it, if you remember.** The skill asks once where you came across the claim, and
  links your answer to the matching source. It never searches the name of whoever told you.
- **No verdicts, no invented sources.** The report never rules on whether a claim is true. It
  never invents a source, date, link or quote. It quotes each source at most once, briefly.
- **Not for claims about private people.** A claim about someone who is not a public figure is
  declined before any search.
- **Saved on request.** In Claude Code, ask and the report is saved under `provenance-reports/`.
