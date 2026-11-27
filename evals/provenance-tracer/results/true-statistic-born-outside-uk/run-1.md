---
case: true-statistic-born-outside-uk
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T19:21:36Z
cost_usd: 1.1490
duration_s: 104
turns: 25
error: none
---

## Tool calls

- Skill: provenance-tracer:provenance-tracer
- Read: <plugin>/skills/provenance-tracer/references/output-template.md
- Read: <plugin>/skills/provenance-tracer/references/search-playbook.md
- Read: <plugin>/skills/provenance-tracer/references/labels.md
- Read: <plugin>/skills/provenance-tracer/references/mutation-types.md
- ToolSearch: {"query":"select:WebSearch,WebFetch","max_results":2}
- WebSearch: "one in six" people England and Wales born outside the UK 2021 census
- WebSearch: 2021 census 16.8% residents born outside UK England Wales
- WebSearch: ONS International migration England and Wales Census 2021 bulletin non-UK born
- WebSearch: "10 million" born outside UK census 2021 England Wales
- WebSearch: source of statistic one in six born abroad England Wales census
- WebSearch: Full Fact census 2021 born outside UK one in six
- WebFetch: https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021
- WebFetch: https://www.ons.gov.uk/news/news/census2021demographyandinternationalmigrationstatistics
- WebFetch: https://www.nationalworld.com/news/uk/census-2021-one-six-people-england-wales-born-outside-uk-3903034
- WebFetch: https://www.inkl.com/news/one-in-six-people-living-in-england-and-wales-were-born-in-a-different-country-census-reveals
- WebFetch: https://www.breitbart.com/europe/2022/11/02/one-in-six-people-in-britain-were-born-in-foreign-countries-census/
- WebFetch: https://scroll.in/latest/1037027/indians-comprised-highest-number-non-uk-born-residents-of-england-and-wales-shows-census-data
- WebFetch: https://themuslimtimes.info/2022/11/02/one-in-six-people-living-in-england-and-wales-were-born-in-a-different-country-census-reveals/
- WebFetch: https://news.yahoo.com/england-waless-foreign-born-population-105156960.html
- WebFetch: https://www.business-standard.com/article/current-affairs/indians-make-up-largest-foreign-born-residents-in-england-wales-census-122110801445_1.html
- WebFetch: https://www.yahoo.com/news/england-waless-foreign-born-population-105156960.html
- WebSearch: Guardian 2 November 2022 "one in six people living in England and Wales" born different country census

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "In the 2021 census, one in six people in England and Wales were born outside the UK."

**Roots:** Echo · **Grounding:** Grounded
**Earliest instance found:** [ONS, *International migration, England and Wales: Census 2021*](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021), 2022 (date from: byline, released 2 November 2022). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 7

### Chain
Your version: "In the 2021 census, one in six people in England and Wales were born outside the UK" (where you met it: not given)
- [Scroll.in, Scroll Staff](https://scroll.in/latest/1037027/indians-comprised-highest-number-non-uk-born-residents-of-england-and-wales-shows-census-data), 2022, Tertiary → cites
  - [ONS news release, *Census 2021 demography and international migration statistics*](https://www.ons.gov.uk/news/news/census2021demographyandinternationalmigrationstatistics), 2022, Secondary → cites
    - [ONS bulletin, *International migration, England and Wales: Census 2021*](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021), 2022, Primary, root
- [Reuters (David Milliken), via Yahoo News](https://www.yahoo.com/news/england-waless-foreign-born-population-105156960.html), 2022, Secondary → cites
  - the ONS census release (the root, above)
- [Breitbart (Kurt Zindulka)](https://www.breitbart.com/europe/2022/11/02/one-in-six-people-in-britain-were-born-in-foreign-countries-census/), 2022, Secondary → cites
  - the ONS bulletin (the root, above)
- [The Muslim Times, a repost](https://themuslimtimes.info/2022/11/02/one-in-six-people-living-in-england-and-wales-were-born-in-a-different-country-census-reveals/), 2022, Tertiary → cites
  - *The Guardian* (Carmen Aguilar García, Michael Goodier, Pamela Duncan), 2022, (not opened), per The Muslim Times → stopped: not opened

The root's own figures: 10.0 million of England and Wales's 59.6 million usual residents (16.8%) were born outside the UK on Census Day, 21 March 2021. That is up from 7.5 million (13.4%) in 2011. The bulletin gives the share as one in six in its main points and as *about one in six* in its body text. It draws on the Census 2021 country-of-birth tables (TS004 and TS012).

### How it changed
None found.

### Status of the root
- No correction, revision or amendment notice appears on the bulletin's own page. It is an ONS statistical bulletin with no DOI, so Crossref, Retraction Watch and PubPeer don't apply.
- Background: the figure covers England and Wales only. Scotland (census held in 2022) and Northern Ireland ran separate censuses, so it is not a UK-wide figure.

### Confidence
High: the root is an opened ONS Primary dated by its own byline, and every link from the retellings back to it was opened. Three more same-day retellings (NationalWorld, inkl's copy of The Guardian, and Business Standard) returned 403 errors and are not shown in the chain.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
