# Changelog

All notable changes to provenance-tracer are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow `major.minor.fix`.

## [Unreleased]

## [1.0.0] — 2026-11-28

The first stable release. In the third full test of the skill, twelve claims and sources run
three times each and every failed check reviewed, it met every measure set for it but two. One
well-sourced claim was traced to its original studies in one run of three; the other two could
not open the 1978 paper's abstract on the live web. And two replies to a claim about a private
person quoted more than the quote rule allows; the skill did not run in those replies, and each
still declined without a search.

### Changed

- **No change in behaviour from 0.3.0.** 1.0.0 is the same skill, released as stable.

## [0.3.0] — 2026-11-27

Changes from the second eval cycle, still in development before 1.0.0.

### Changed

- **A second origin needs the claim's own retellings.** An earlier work counts as a separate
  origin only when sources that retell the claim, or weigh its evidence, credit it. A work you
  would know only from a biography of its author is shown as background instead.
- **A cited source that doesn't address the claim no longer counts.** When a page cites a study
  or a book for the claim, and that work, read in full, says nothing on it, the report says the
  citation does not hold and what the work covers, rather than treating it as an original that
  differs. A copy that failed to load, or an abstract alone, is never read as silence.
- **Original passages are looked for by their own words.** For a book's or speech's passage,
  the skill searches the web for the passage's words before any library catalogue, checks each
  copy's title, volume and language as it reads it, skips an archive copy that isn't served, and
  doesn't fetch the same address twice. A passage held only in a few online copies may still not
  open.
- **Quotes stay with their sources.** A quote sits on the line that links the page it comes
  from, and a status line that quotes draws on one source.

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

[Unreleased]: https://github.com/FairCat-GD/claude-skills/compare/provenance-tracer--v1.0.0...HEAD
[1.0.0]: https://github.com/FairCat-GD/claude-skills/releases/tag/provenance-tracer--v1.0.0
[0.3.0]: https://github.com/FairCat-GD/claude-skills/commit/bf06fdf9900c0609534800b3c875cea27fc5b3b8
[0.2.0]: https://github.com/FairCat-GD/claude-skills/commit/429b407cbc2a21a290178238c14f00e933353335
[0.1.0]: https://github.com/FairCat-GD/claude-skills/commit/c7d99065d2648a1b72c047266cbe20fd81def8d3
