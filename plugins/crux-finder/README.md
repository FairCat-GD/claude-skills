# crux-finder

Untangles an argument that keeps going in circles: finds the one claim both sides hinge on, and
what would settle it, without taking sides.

## What it does

- **Takes two positions:** two people's views in their own words, labelled A and B, or a
  transcript of the two (a chat log, a thread, an email chain).
- **Restates each side at its strongest,** in a few sentences, using only what the input says,
  and with the same care and length for both.
- **Lists what both sides already accept,** then finds the crux: the claim that, seen the
  other way, would change a side's conclusion, starting from any point a side says outright
  would change its mind.
- **Names the kind of disagreement** (a fact, a forecast, a word used two ways, a difference in
  values, or two sides answering different questions) and **what would move it:** the evidence
  to look at, a forecast with a date, two clearer words, the trade-off named, or the two
  questions set apart.
- **Gives a short report,** meant to stay within 400 words, with up to two secondary cruxes, the
  disagreements that turn out not to be real, and how confident it is. Ask for the claim map to
  see every claim each side makes.

What it never does: say who is right, or say anything about either person's motives, intelligence
or good faith. If you give only your side and your account of the other's, it asks once for their
own words; if you go ahead without them, it marks their side as your reconstruction. If the
positions don't conflict, it says so rather than inventing a crux.

## Using it

Share the two positions and ask, for example "Where do A and B really disagree?" or "Why does
this argument keep going in circles?". The skill starts on requests like these. In Claude Code
you can also start it with `/crux-finder:crux-finder`.

## What it needs

Nothing beyond the model: it searches nothing, runs no code, needs no network and installs
nothing. It is instructions and references only.

- **Claude Code** and **Codex:** nothing to set up.
- **claude.ai:** skills need *Code execution and file creation* turned on (Settings →
  Capabilities), though this one runs no code.
- **Other agents:** any agent that loads a skill's `SKILL.md`.

## Installing

### Claude Code

```
/plugin marketplace add FairCat-GD/claude-skills
/plugin install crux-finder@faircat-skills
```

A new version reaches you when the plugin's version number moves.

### Codex, claude.ai and other agents

These take the skill folder itself, `plugins/crux-finder/skills/crux-finder/` in a clone of this
repository:

```bash
git clone https://github.com/FairCat-GD/claude-skills.git
```

- **Codex:** copy the folder to `~/.agents/skills/` (for you) or `.agents/skills/` (for one
  repository). Start it as `$crux-finder` or by asking, as above.
- **claude.ai:** zip the folder, so the zip holds the folder at its root, and upload the zip as a
  custom skill on claude.ai's Plugins page (*Add*, then *Upload plugin*).

  ```bash
  cd claude-skills/plugins/crux-finder/skills
  zip -r crux-finder.zip crux-finder
  ```

- **Other agents:** copy the folder into the agent's skills directory.

## How it was tested

The skill was tested on ten disagreements, each with an answer the maintainer wrote down before
any run: one for each kind of crux, a second question of fact, one where only one side speaks,
one where the two positions don't conflict, a message thread between two siblings, and two
passages from the first Lincoln–Douglas debate of 1858. Each ran twice through `claude plugin
eval`, in a fresh Claude Code session in a temporary home that loaded none of the user's
settings, plugins, memory or files, only the skill and Claude Code's own. Each reply was graded
against that answer by graders drawn from it and approved by the maintainer, with Claude Sonnet
5.5 as judge, and checked for verbatim quotes, balanced steelmen and length. The maintainer read
every failed verdict, one full reply per case, and the primary crux of both runs side by side,
and confirmed or overruled each failed verdict. Three of the disagreements were also run once
each on claude.ai. The last full test ran on 1.0.0, with Claude Opus 5.5 in Claude Code 2.1.330;
the claude.ai test ran on 0.4.0, with Claude Fable 5.2, and 1.0.0 is 0.4.0 with only its version
number changed.

| Check | Pass bar | Result | Met |
|---|---|---|---|
| Crux matches gold | ≥ 16 / 20 runs | 20 / 20 | yes |
| Type matches gold | ≥ 18 / 20 runs | 18 / 20 | yes |
| Stability: same primary crux in both runs | ≥ 8 / 10 cases | 10 / 10 | yes |
| Quotes verbatim | all runs | 20 / 20 | yes |
| Steelman symmetry | all reports | 18 / 18 | yes |
| Length ≤ 400 words | all reports | 18 / 18 | yes |
| No statement about people | all runs | 20 / 20 | yes |
| One-sided gate fires | all runs with its grader | 2 / 2 | yes |
| No-conflict case reports no conflict or a Framing crux | all runs with its grader | 2 / 2 | yes |
| Gold order + approved_by + graders as run | all cases | 10 / 10 | yes |
| Runs on the skill as it stands | all runs | 20 / 20 | yes |
| claude.ai smoke test | 3 / 3 cases | 3 / 3 | yes |

*Gold* is the maintainer's answer. *No statement about people* means no report said anything
about either person's motives, intelligence or good faith. Both runs of the one-sided case asked
for the other side's own words and wrote no report, so 18 reports count for symmetry and length.
Both misses on type are the two runs of one case whose answer is two sides answering different
questions, which both runs read as a difference in values; the bar allows two. The judge failed
three of the 64 verdicts on statements about people, giving no reason, and the maintainer, reading
each report, found none and overruled them. The cases, every report and its verdicts, and the
maintainer's reviews are kept in this repository, under `evals/crux-finder/`.

## Version

1.0.0. What changed in each version is in [CHANGELOG.md](./CHANGELOG.md).

## License

[MIT](../../LICENSE)
