# FEATURE: one eval engine for every skill (round 2)

## The request, verbatim (2026-11-25)

Asked where provenance-tracer's eval cases should live, given that `claude plugin eval` reads
cases only from inside a plugin's folder, which would ship them to everyone who installs it, the
owner answered:

> I am leaning towards the recommended option, but I wonder why you want to build it differetly
> from what you've proposed and we've done for crux finder, and whether we should update crux
> finder structure as well so the repo layout is same for all skills?

The recommended option was cases at the root, `evals/provenance-tracer/`, run by a thin runner
over `claude plugin eval`. The intake answered that both skills would keep the same folders and
only the case format and engine would differ, and offered to leave crux-finder's harness alone.
The owner chose instead to move crux-finder onto the same engine this round.

## What the intake knew about the engine

Read from the docs (`https://code.claude.com/docs/en/plugin-evals.md`) and from
`claude plugin eval --help` on `claude` 2.1.330. None of it was measured here; E1 measures what
the round rests on before anything is built on it.
- A case is a folder holding `prompt.md` (frontmatter, then the prompt) and graders, either in
  a `case.yaml` or as `graders/*.md`. An unknown key in `prompt.md`'s frontmatter is an error.
- Six grader types, with no custom code: `regex`, `tool_used`, `tool_order`, `file_exists`,
  `llm` and `baseline`. A run's score is the share of its graders that pass; a case's is the
  mean of its runs; any case below `--threshold` (1.0 by default) makes the command exit 1.
- The eval folder must be inside the plugin (`--eval-dir` takes no `..`); a case's `plugins:`
  field takes a relative path, which may let cases live elsewhere.
- Each run is a non-interactive session in a temporary home with none of the user's settings,
  plugins, skills, `CLAUDE.md`, MCP servers or memory, and it cannot read the eval folder.
  `allowed_tools` defaults to none; WebSearch and WebFetch need `--allow-tools`; `max_turns`
  defaults to 10 and `timeout_seconds` to 300.
- A baseline arm without the plugin runs by default (`--ablation`); the HTML report is published
  to claude.ai as a private artifact unless `--no-publish`.
- An older CLI's `aggregate-result.json`, seen on this machine by the plan review, held each
  run's grader verdicts and short excerpts, and no whole reply or tool call.

## Resolved decisions (2026-11-25, at intake)

How the harness is built is in `docs/ARCHITECTURE.md`'s *The eval harness* and *The data layer*,
amended at this intake; these are the decisions as the owner gave them.

1. **One engine for every skill:** `claude plugin eval`. crux-finder's evals move onto it this
   round, and provenance-tracer's are built on it.
2. **The layout stays as decided:** `evals/<skill>/` at the root, never under `plugins/`, so no
   case ships. Each case is `evals/<skill>/cases/<id>/`, holding `prompt.md`, its graders and
   `gold.md`; each cycle's results are `evals/<skill>/results/<id>/`; each skill has its own
   `checks.py`. One runner, shared by every skill and standard library only, drives the engine.
   E1 measures whether cases run in place through `plugins:`; if not, the runner copies the
   plugin and the skill's cases into a temporary plugin folder and runs the engine on the copy.
3. **`gold.md` stays, one per case:** the answer the owner approved, in flat `key: value` lines
   (`approved_by`, the authoring date, and `source:` and `license:` where the input has them),
   which a `checks.py` reads with no YAML library. The graders are drawn from it. It is
   committed before any of the case's results present now (a retired cycle's, kept in git, do
   not count), the graders are unchanged since each run's commit, and the runner never opens
   or copies it.
4. **What a cycle commits:** for each run, `results/<id>/run-N.md`, as crux-finder's are today: a
   header (the case, the run, the model, the CLI's version, the skill's version, the commit, the
   date, the cost), the run's tool calls one per line (the tool and its query or URL), then the
   final reply. Beside them, each run's grader verdicts, with every machine path removed. No raw
   trace, no `report.html`, no `aggregate-result.json`, and nothing published (`--no-publish`).
   The owner first chose the JSON alone, and changed it after the plan review showed that the
   JSON holds no whole reply.
5. **How runs are judged:** the graders and the skill's `checks.py` decide. The owner reads
   every failed verdict and one run per case each cycle, to catch a judge that is wrong. This
   holds for both skills.
6. **A corrected verdict:** how the owner's correction of a grader's verdict is recorded and
   counted is asked at the start of E2. *Recommended:* one line per correction in the case's
   `review.md`, which `checks.py` counts over the grader's verdict.
7. **crux-finder on the new engine:**
   - its ten case ids stay, and each input's body becomes its `prompt.md` unchanged, with no
     line saying no reply is possible, as round 1's runs had none;
   - crux, type and *no statement about people* become `llm` and `regex` graders drawn from
     each `gold.md`, approved by the owner before they are committed;
   - stability is the owner's: they compare the two runs' crux sentences of each case;
   - its `checks.py` keeps quotes, symmetry and length, read from `run-N.md`;
   - two runs per case, and the pass bars of round 1, unchanged;
   - the old runner, its checks and tests, the `input.md` files and the old results are retired
     in one commit with the new checks, before any new result, since moving the real case's
     `source:` and `license:` into its gold must precede its first result (invariant 7);
   - a fresh cycle on the new engine, and the README's *How it was tested* and its table
     rewritten from it;
   - the three claude.ai replies of round 1's smoke test stay, with their verdicts (each
     case's `review.md` cut to its `## claude-ai` section), since the skill they ran is
     unchanged;
   - its version moves only if its shipped files change.
8. **A claude.ai reply is judged by the owner,** recorded in that case's `review.md`, for both
   skills, since the engine cannot grade a reply it did not run.
9. **Up to four runs at once** (`--concurrency 4`). Still one cycle at a time, never in a
   parallel part.
10. **The runner's fixed choices:** the model `claude-opus-5-5`, written into every result; no
    baseline arm (`--ablation none`); `--no-publish`; `--trust-plugin`, which it passes only for
    this repository's own plugin; `--output-dir` outside the plugin; the web tools a skill's
    cases need, granted with `--allow-tools`. It reads a run's failure from the results, not the
    exit code, since exit 1 is expected whenever a case scores below 1. It refuses while the
    plugin has uncommitted changes, as `evals/crux-finder/run.py` does now.
11. **Isolation is measured, not assumed.** E1 checks that a run loads none of the owner's
    plugins, synced skills or memory, cannot read the graders, and can read the skill's
    `references/`, and whether what a run loaded can be checked on every run, as today's runner
    checks each start event. Losing that per-run check is the owner's call, at a stop.
12. **Everything under `evals/` stays standard library only** (invariant 5). Its test is amended
    in E1 so that shared code under `evals/` may be imported.
13. **The sessions:** E1 (the engine measured, the shared runner built, today's tooling
    untouched), E2 (crux-finder's cases and new checks, the old harness and results retired),
    E3 (crux-finder's cycle). None cuts a version unless a shipped file changes.
14. **Out of this round:** pinning the `claude` CLI, which stays the owner's call as in round 1.
