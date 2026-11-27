# Changelog

All notable changes to provenance-tracer are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow `major.minor.fix`.

## [Unreleased]

## [0.2.0] — 2026-11-27

Changes from the first eval cycle, still in development before 1.0.0.

### Changed

- **Origins are told apart more carefully.** Separate studies by different teams, each with its
  own data, now count as independent origins even when the later one mentions the earlier. Work
  that a study names only as background is shown as background, not as an earlier origin. A
  saying credited to the wrong person no longer counts that person's own writing as a second
  origin: the report shows it as the text the credit points to, and how it differs. Each origin
  is marked as a root in the chain.
- **A study's own findings count as grounding.** When an opened study's own data show what your
  version says, the report marks it *Grounded*, even where the study reports an association. A
  retold cause is flagged as a change only where the study itself held back from claiming one.
- **Original sources are opened more often.** When a study's or a book's own page won't open,
  the skill looks for another copy, such as the study's abstract record or a full-text scan of the
  book, before marking it as not opened.
- **Quotes are fewer and shorter.** Each source is quoted at most once in the whole report, one
  quote to a line, a dozen words at most. A single word or a rating it points to is set in
  italics instead of quotation marks.

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

[Unreleased]: https://github.com/FairCat-GD/claude-skills/commits/main/plugins/provenance-tracer
[0.2.0]: https://github.com/FairCat-GD/claude-skills/commit/429b407cbc2a21a290178238c14f00e933353335
[0.1.0]: https://github.com/FairCat-GD/claude-skills/commit/c7d99065d2648a1b72c047266cbe20fd81def8d3
