# crux-finder

Untangles an argument that keeps going in circles: finds the one claim both sides hinge on, and
what would settle it, without taking sides.

**In development.** Version 0.3.0 works end to end; its behaviour may still change before 1.0.0.

## What it does

- **Takes two positions:** two people's views in their own words, labelled A and B, or a
  transcript of the two (a chat log, a thread, an email chain).
- **Restates each side at its strongest,** in a few sentences, using only what the input says,
  and with the same care and length for both.
- **Lists what both sides already accept,** then finds the crux: the smallest claim that, seen
  the other way, would change a side's conclusion.
- **Names the kind of disagreement** (a fact, a forecast, a word used two ways, a difference in
  values, or two sides answering different questions) and **what would move it:** the evidence
  to look at, a forecast with a date, two clearer words, the trade-off named, or the two
  questions set apart.
- **Gives a short report,** of at most 400 words, with up to two secondary cruxes, the
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
  custom skill.

  ```bash
  cd claude-skills/plugins/crux-finder/skills
  zip -r crux-finder.zip crux-finder
  ```

- **Other agents:** copy the folder into the agent's skills directory.

## Version

0.1.0, in development. What changed in each version is in [CHANGELOG.md](./CHANGELOG.md).

## License

[MIT](../../LICENSE)
