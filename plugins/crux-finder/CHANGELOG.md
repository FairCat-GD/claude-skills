# Changelog

All notable changes to crux-finder are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow `major.minor.fix`.

## [Unreleased]

## [0.3.0] — 2026-11-22

Still in development: the change below comes from the second full test of the skill, ten
disagreements run twice each and every report read. Every other measure was met; 16 of the 18
reports kept within 400 words, and the two on a long debate excerpt ran to 463 and 488.

### Changed

- **A report stays within 400 words however long the input.** Each part of the report now has a
  limit in words, and the limits add up to under 400: a long input gets the same limits as a
  short one, so the report says less about each point rather than running long. A secondary
  crux is a single short line.
- **Each side's strongest form keeps to its main reasons.** It gives the conclusion and the
  reasons it most rests on, in at most 45 words, rather than every reason a long argument
  offers, so the two sides stay the same length.

## [0.2.0] — 2026-11-22

Still in development: the changes below come from the first full test of the skill, ten
disagreements run twice each and every report read.

### Changed

- **Shorter reports.** Each part of the report has a word budget, aiming at about 350 words so
  the report keeps inside the 400 it promises; in the test, most ran to between 416 and 591.
- **The crux is something both sides actually argue.** A point only one side raises is no longer
  reported as the crux or as a secondary crux, and a crux both sides state comes before one that
  rests on an unstated premise. Common ground lists only what both accept.
- **Clearer crux types.** A dispute over what has happened is a question of fact, even when both
  sides draw forecasts from it or word it in the future tense.

### Fixed

- **Quotation marks only around words copied exactly from what you shared:** never around the
  report's own wording, a question it poses or one of its labels.
- **"No crux" when nothing would change.** Two sides answering different questions are reported
  as such only where taking up the other's question would change a conclusion; otherwise the
  report says the positions do not conflict.
- **Nothing after the report.** It no longer adds a short answer or a summary after Confidence.

## [0.1.0] — 2026-11-20

The first release, in development: it works end to end, and its behaviour may still change
before 1.0.0.

### Added

- **Find where an argument really turns.** Share two positions, a debate or a transcript, and
  ask where the two sides really disagree. You get a short report: each side at its strongest,
  what both already accept, and the one claim the rest of the argument hinges on.
- **What kind of disagreement it is, and what would move it.** Each crux is named as a question
  of fact, a forecast, a word used two ways, a difference in values, or two sides answering
  different questions, with what would settle it: the evidence to look at, a forecast with a
  date, two clearer words, the trade-off named, or the two questions set apart.
- **No verdict, and nothing about the people.** The report never says who is right, and never
  comments on anyone's motives or character. Both sides get the same care and the same length.
- **It asks when one side is missing.** If you give your own view and your account of the other
  person's, it asks once for their own words. Go ahead without them and the report marks their
  side as your reconstruction, with low confidence.
- **It says so when there is nothing to find.** Positions that don't conflict are reported as
  such, rather than with a crux made up to fill the page.
- **The full breakdown on request.** Ask for the claim map to see every claim each side makes,
  and how they depend on each other.

[0.2.0]: https://github.com/FairCat-GD/claude-skills/commit/c52b303881d3ad90dd4c6167644af1cccba61a07
[0.1.0]: https://github.com/FairCat-GD/claude-skills/commit/352a3835dca5f9bf0527cfc74a6d92403756ab2a
