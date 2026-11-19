# Changelog

All notable changes to travel-itinerary-builder are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow `major.minor.fix`.

## [Unreleased]

## [1.1.0] — 2026-11-19

Fixes from a read of the whole skill, and plain answers to what it does where an app lacks
something it uses.

### Added

- **It works without question buttons.** Where the app can't show multiple-choice options, the
  skill asks the same questions in chat, one at a time, as numbered options.
- **It tells you what it couldn't do.** If the PDF can't be built where it runs, you get the plan
  in chat, with the reason and what would make the PDF possible. If it couldn't look at the
  pages, or the fonts fell back because it was offline, it says so.
- **A pointer to your embassy.** The emergency appendix tells you to look up your own country's
  embassy or consulate, since the interview doesn't ask your nationality.

### Changed

- **Saying No to food picks keeps the restaurant list.** No meals are planned into your days,
  and the food appendix still lists 10 to 15 places across every budget, each labelled.
- **Appendix letters stay put.** When one is left out (no shopping, or no dates), the others keep
  their letters.
- **It installs its PDF tool more carefully.** It uses a separate environment, asks before
  installing anything on your system, and never overrides your system Python's protection.
- **An honest promise on reading.** The A4 PDF reads well on a laptop and on paper; on a phone,
  you zoom into its single column.
- **You're told where the PDF is,** by its path or the link your app gives.

### Fixed

- **The PDF's own fonts now load.** Its headings and text were silently falling back to the
  system's default fonts.
- **Snack stops show your destination's currency** with your home-currency conversion, instead
  of one city's currency in every plan.
- **Weekdays are checked in a way that works on any computer,** a Mac included.
- **Small inconsistencies:** the Wikipedia link always sits on the place's name; the example
  restaurant links to its own site; one spelling of "(verify)"; six appendices counted as six; a
  walk-in restaurant keeps its booking line; no doubled "Other" option; no emoji in the PDF.

## [1.0.1] — 2026-11-18

The skill becomes a plugin of its own in the `faircat-skills` marketplace. What it does for your
trip is unchanged.

### Added

- **Install it from the `faircat-skills` marketplace.** In Claude Code, add the marketplace once
  and install the plugin; a new version reaches you when its version number moves.
- **The licence travels with the skill.** It states MIT itself, so a copy in Codex or an upload
  to claude.ai carries its terms.

### Changed

- **The worked examples use Lisbon.** The examples behind the snack stops, coffee houses,
  ceramics and curiosities now come from one city, the one the skill's other examples already
  use. Plans for any city follow the same rules as before.

### Fixed

- **The skill meets the Agent Skills specification.** Its version moved to the place the
  specification allows for it, so a tool that checks skills strictly accepts it, and a copied or
  zipped folder still shows which version it is.

## [1.0.0] — 2026-07-22

As first published.

### Added

- **A day-by-day itinerary for one city,** from a guided interview, deep web research, and a
  trip-themed PDF made to read on a phone.

[1.0.1]: https://github.com/FairCat-GD/claude-skills/commit/b41611a260c8a501744d3e934b068bd44a0303fb
[1.0.0]: https://github.com/FairCat-GD/claude-skills/commit/b0b5b5157c81de61b4d8f89d4ebee319811b21a5
