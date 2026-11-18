# Claude Skills

Ready-to-use Agent Skills that give Claude new superpowers. Browse the collection, pick whatever fits, and drop it into your setup. Each one is self-contained, so there's nothing to configure and nothing you're locked into. Take them for a spin.

## Skills

**Travel**

- [travel-itinerary-builder](./travel-itinerary-builder) — Helps you effortlessly craft the perfect travel experience for the city of your choice: a day-by-day plan tailored to what you actually want to see, do, and eat.

*More coming as I build them.*

## Developing

You need [uv](https://docs.astral.sh/uv/); it provides Python 3.10 and the pinned tools. The
gate, run before every commit:

```bash
uv run scripts/verify.py
```

It runs the stages `format`, `lint`, `tests` and `hygiene`, then a summary; name a stage to run it
alone. The hygiene stage reads a list of private words from `~/.config/hygiene/terms.txt`, one
per line. If nothing is private to you, create the file empty.

How the repository is built is in [docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md), the way work is
done in [docs/DEVELOPMENT-WORKFLOW.md](./docs/DEVELOPMENT-WORKFLOW.md), the standing rules in
[CLAUDE.md](./CLAUDE.md), and the round in progress in [docs/spec/](./docs/spec/).

## License

[MIT](./LICENSE)
