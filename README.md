# Claude Skills

Ready-to-use Agent Skills that give Claude new superpowers. Browse the collection, pick whatever fits, and drop it into your setup. Each one is self-contained, so there's nothing to configure and nothing you're locked into. Take them for a spin.

## Skills

**Travel**

- [travel-itinerary-builder](./plugins/travel-itinerary-builder/README.md) — Helps you effortlessly craft the perfect travel experience for the city of your choice: a day-by-day plan tailored to what you actually want to see, do, and eat.

**Reasoning**

- [crux-finder](./plugins/crux-finder/README.md) *(in development)* — Untangles an argument that keeps going in circles: finds the one claim both sides hinge on, and what would settle it, without taking sides.

*More coming as I build them.*

## Installing

This repository is a Claude Code plugin marketplace, `faircat-skills`, with one plugin per skill,
so you install only the skills you want. In Claude Code, add the marketplace once, then install
a skill by its name:

```
/plugin marketplace add FairCat-GD/claude-skills
/plugin install travel-itinerary-builder@faircat-skills
```

Each skill also works on its own as a plain skill folder in Codex, claude.ai and other agents.
Its README says how to install it there.

## Developing

You need [uv](https://docs.astral.sh/uv/), which provides Python 3.10 and the pinned tools, and
Claude Code's `claude` command. The gate, run before every commit:

```bash
uv run scripts/verify.py
```

It runs the stages `skills`, `plugins`, `format`, `lint`, `tests` and `hygiene`, then a summary;
name a stage to run it alone. `skills` runs the Agent Skills validator through `uvx`, which
needs the network the first time, while uv's cache is empty. `plugins` runs
`claude plugin validate`. The hygiene stage reads a list of private words from
`~/.config/hygiene/terms.txt`, one per line. If nothing is private to you, create the file empty.

How the repository is built is in [docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md), the way work is
done in [docs/DEVELOPMENT-WORKFLOW.md](./docs/DEVELOPMENT-WORKFLOW.md), the standing rules in
[CLAUDE.md](./CLAUDE.md), and the round in progress in [docs/spec/](./docs/spec/).

## License

[MIT](./LICENSE)
