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
- **Delivers a trip-themed PDF** made to read on your phone, or the plan in chat if you ask for
  it.

## Using it

Ask for what you want, for example "I'm going to Lisbon for three days, help me plan" or "make
me an itinerary for Porto". The skill starts on requests like these. In Claude Code you can also
start it with `/travel-itinerary-builder:travel-itinerary-builder`.

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

1.0.1. What changed in each version is in [CHANGELOG.md](./CHANGELOG.md).

## License

[MIT](../../LICENSE)
