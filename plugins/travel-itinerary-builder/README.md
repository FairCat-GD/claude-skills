# travel-itinerary-builder

Helps you effortlessly craft the perfect travel experience for the city of your choice: a
day-by-day plan tailored to what you actually want to see, do, and eat.

## What it does

- **Asks about your trip, one question at a time:** the city, how many days, your dates, where
  you are staying, who is travelling, the pace you like, famous sights or hidden gems, how you
  get around, your interests, shopping, food picks, your home currency, and anything else that
  should shape the plan.
- **Reads your answers back** and waits for your yes before it starts.
- **Researches the city on the web:** the sights, where to eat, the weather for your dates, the
  local scams and traps, and the emergency numbers.
- **Builds the plan day by day,** morning to dinner, routed around where you stay, with
  appendices for food picks, shopping, weather, things to watch out for, emergency contacts and
  the city's specialties.
- **Delivers a trip-themed A4 PDF** that reads well on a laptop and on paper, and on a phone
  once you zoom into its single column. You get the plan in chat instead if you ask for it, or
  if the PDF can't be built where the skill runs.

## Using it

Ask for what you want, for example "I'm going to Lisbon for three days, help me plan" or "make
me an itinerary for Porto". The skill starts on requests like these. In Claude Code you can also
start it with `/travel-itinerary-builder:travel-itinerary-builder`.

## What it needs

- **Web search.** The research is the heart of the plan; without search there is nothing to
  build it from.
- **For the PDF: Python, WeasyPrint and the Pango library.** The skill installs WeasyPrint in a
  separate environment when it can, and asks you before installing Pango on your system
  (`brew install pango` on a Mac, `apt install libpango-1.0-0 libpangoft2-1.0-0` on Debian or
  Ubuntu). Where none of this can run, you get the plan in chat.
- **The network, for the PDF's fonts.** Offline the PDF still builds, with your system's fonts.
- **A question tool is optional.** Without one, the interview asks in chat with numbered
  options.

Where it runs:

- **Claude Code:** web search is built in; the PDF needs Python and Pango on your machine.
- **Codex:** turn on web search (`web_search = "live"` in `~/.codex/config.toml`, or `--search`
  for one run); the PDF needs Python and Pango, as above.
- **claude.ai:** skills need *Code execution and file creation* turned on (Settings →
  Capabilities), and the chat needs web search on. Without network access from the sandbox the
  PDF can't install WeasyPrint or load its fonts.
- **Other agents:** web search, and a way to run Python for the PDF.

## Installing

### Claude Code

```
/plugin marketplace add FairCat-GD/claude-skills
/plugin install travel-itinerary-builder@faircat-skills
```

A new version reaches you when the plugin's version number moves.

### Codex, claude.ai and other agents

These take the skill folder itself, `plugins/travel-itinerary-builder/skills/travel-itinerary-builder/`
in a clone of this repository:

```bash
git clone https://github.com/FairCat-GD/claude-skills.git
```

- **Codex:** copy the folder to `~/.agents/skills/` (for you) or `.agents/skills/` (for one
  repository). Start it as `$travel-itinerary-builder` or by asking, as above.
- **claude.ai:** zip the folder, so the zip holds the folder at its root, and upload the zip as a
  custom skill.

  ```bash
  cd claude-skills/plugins/travel-itinerary-builder/skills
  zip -r travel-itinerary-builder.zip travel-itinerary-builder
  ```

- **Other agents:** copy the folder into the agent's skills directory.

## Version

1.1.0. What changed in each version is in [CHANGELOG.md](./CHANGELOG.md).

## License

[MIT](../../LICENSE)
