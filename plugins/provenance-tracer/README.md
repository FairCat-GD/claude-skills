# provenance-tracer

Follows a claim back to where it came from: the earliest instance it can find, the chain of
retellings that carried it to you, and how it changed on the way. It doesn't decide whether the
claim is true.

## What it does

- **Traces a claim (forward).** Type a belief, a statistic or an attributed quote. The skill
  searches the web, opens every page it uses, and follows each retelling back through what it
  cites, as far as the trail goes. You get the chain, from your version to its root, each source
  dated and linked. It always notes that earlier instances may exist.
- **Shows how it changed.** A table sets the root's version beside yours and names each change:
  - a widened scope;
  - a changed number;
  - a dropped hedge;
  - a correlation retold as a cause;
  - a shifted attribution;
  - lost context.

  Each change is shown with the source where it first appears.
- **Labels every trace on two axes:**
  - **Roots:** one source retold once (*Single thread*), one origin echoed by many (*Echo*), or
    several origins found independently (*Independent*), such as separate studies with their own
    data.
  - **Grounding:** an original source was opened and says what your version says (*Grounded*),
    it was opened and says something materially different (*Primary differs*), or none was
    opened (*No primary found*).

  Notes follow where they apply: *Mutated*, *Misattributed*, *Origin retracted*, *Origin
  corrected*, *Origin failed replication*.
- **Checks the original's status.** For a study or document at the root, it looks for a
  retraction, a correction, a failed replication and major later studies, and links what it
  finds.
- **Starts from a source instead (reverse).** Name a study, book, speech or document, by its
  title, its DOI, its link or a description. You get:
  - its status;
  - what it found, in at most three sentences, with its scope and hedges;
  - its two or three most common popular versions, and how each differs;
  - for any belief you name that rests on it, whether it supports that belief as stated, in
    part, or not at all.
- **Asks once, if at all.** It may ask where you came across the claim, roughly when, and whether
  that source cited anything. It links your answer to the chain. Say you don't remember and it
  traces from the web alone. When it runs with nobody to answer, it asks nothing and lists its
  assumptions at the top of the report.

What it never does:
- **Say whether a claim is true.** "No primary found" means the search found none, not that the
  claim is false; a fact-check it cites is named as a source.
- **Invent a source, date, link or quote.** A page it could not open is marked *not opened*.
- **Quote a source at length.** It quotes each source at most once, in a dozen words at most,
  linked.
- **Trace a claim about a private person.** A claim whose subject is not a public figure is
  declined before any search.
- **Trace more than one claim per run.**
- **Read your files or notes.**

## Using it

Type the claim and ask where it came from, for example:
- "Where does the quote '<quote>' come from? I've seen it credited to <person>."
- "Where did the figure that <statistic> come from?"
- "What did <a named study, with its authors and year> really find?"

The skill starts on requests like these. In Claude Code you can also start it with
`/provenance-tracer:provenance-tracer`. Ask it to save the report, and in Claude Code it writes
`provenance-reports/YYYY-MM-DD-<first-words-of-the-claim>.md` in your working folder.

## What it needs

**Web search and page fetch.** Without both it says so and stops, since it never traces from
memory.

**The claim's text goes into web searches.** The name of whoever told you about it never does,
unless they are a public figure or publication.

It runs no code and installs nothing: it is instructions and references only.

- **Claude Code:** its built-in WebSearch and WebFetch tools. Claude Code asks your permission for
  them unless your settings already allow them.
- **Codex:**
  - web search: set `web_search = "live"` in `~/.codex/config.toml`, or pass `--search` for one
    run, so results are current;
  - page fetch: it also needs to open the pages it finds.
- **claude.ai:**
  - skills need *Code execution and file creation* turned on (Settings → Capabilities), though
    this one runs no code;
  - the chat needs web search on;
  - it also needs to open the pages it finds. Whether claude.ai offers that with web search alone
    is not yet checked; without it, the skill says so and stops.
- **Other agents:** any agent that loads a skill's `SKILL.md` and can search the web and open
  pages.

## Installing

### Claude Code

```
/plugin marketplace add FairCat-GD/claude-skills
/plugin install provenance-tracer@faircat-skills
```

A new version reaches you when the plugin's version number moves.

### Codex, claude.ai and other agents

These take the skill folder itself, `plugins/provenance-tracer/skills/provenance-tracer/` in a
clone of this repository:

```bash
git clone https://github.com/FairCat-GD/claude-skills.git
```

- **Codex:** copy the folder to `~/.agents/skills/` (for you) or `.agents/skills/` (for one
  repository). Start it as `$provenance-tracer` or by asking, as above.
- **claude.ai:** zip the folder, so the zip holds the folder at its root. Upload the zip as a
  custom skill on claude.ai's Plugins page (*Add*, then *Upload plugin*).

  ```bash
  cd claude-skills/plugins/provenance-tracer/skills
  zip -r provenance-tracer.zip provenance-tracer
  ```

- **Other agents:** copy the folder into the agent's skills directory.

## Version

0.2.0, in development: its behaviour may still change before 1.0.0. What changed in each version
is in [CHANGELOG.md](./CHANGELOG.md).

## License

[MIT](../../LICENSE)
