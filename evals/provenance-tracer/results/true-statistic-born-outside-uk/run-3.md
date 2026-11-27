---
case: true-statistic-born-outside-uk
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T19:21:56Z
cost_usd: 1.0285
duration_s: 83
turns: 24
error: none
---

## Tool calls

- Skill: provenance-tracer:provenance-tracer
- Read: <plugin>/skills/provenance-tracer/references/output-template.md
- Read: <plugin>/skills/provenance-tracer/references/search-playbook.md
- Read: <plugin>/skills/provenance-tracer/references/labels.md
- Read: <plugin>/skills/provenance-tracer/references/mutation-types.md
- ToolSearch: {"query":"select:WebSearch,WebFetch","max_results":2}
- WebSearch: "one in six" born outside the UK 2021 census England and Wales
- WebSearch: 2021 census 10 million people England Wales born outside UK 16.8%
- WebSearch: ONS International migration England and Wales Census 2021 non-UK born
- WebSearch: "16.8%" born outside UK census 2021
- WebSearch: source of "one in six" born abroad England Wales statistic
- WebSearch: Full Fact census 2021 born outside UK one in six
- WebFetch: https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021
- WebFetch: https://www.ons.gov.uk/news/news/census2021demographyandinternationalmigrationstatistics
- WebFetch: https://www.yahoo.com/news/one-six-people-living-england-102800759.html
- WebFetch: https://www.nationalworld.com/news/uk/census-2021-one-six-people-england-wales-born-outside-uk-3903034
- WebFetch: https://uk.news.yahoo.com/one-six-people-living-england-102800759.html
- WebFetch: https://www.inkl.com/news/one-in-six-people-living-in-england-and-wales-were-born-in-a-different-country-census-reveals
- WebFetch: https://www.breitbart.com/europe/2022/11/02/one-in-six-people-in-britain-were-born-in-foreign-countries-census/
- WebFetch: https://www.inkl.com/news/one-in-six-people-in-uk-were-born-abroad-see-how-your-area-compares
- WebFetch: https://en.wikipedia.org/wiki/Foreign-born_population_of_the_United_Kingdom
- WebFetch: https://www.ons.gov.uk/news/news/census2021demographyandinternationalmigrationstatisticsforwales

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "In the 2021 census, one in six people in England and Wales were born outside the UK."

**Roots:** Echo · **Grounding:** Grounded
**Earliest instance found:** [Office for National Statistics, *International migration, England and Wales: Census 2021*](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021), 2022 (date from: byline, released 2 November 2022). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 5

### Chain
Your version: "In the 2021 census, one in six people in England and Wales were born outside the UK" (where you met it: not given)
 ├─ [Sky News story republished on Yahoo News UK](https://uk.news.yahoo.com/one-six-people-living-england-102800759.html), 2022, Secondary → cites the ONS census data
 │   └─ ONS bulletin (root, below)
 ├─ [Breitbart, Kurt Zindulka](https://www.breitbart.com/europe/2022/11/02/one-in-six-people-in-britain-were-born-in-foreign-countries-census/), 2022, Secondary → cites (links the ONS bulletin)
 │   └─ ONS bulletin (root, below)
 ├─ [ONS news release, *Census 2021 demography and international migration statistics*](https://www.ons.gov.uk/news/news/census2021demographyandinternationalmigrationstatistics), 2022, Secondary → cites (links the bulletin)
 │   └─ ONS bulletin (root, below)
 ├─ [ONS news release for Wales](https://www.ons.gov.uk/news/news/census2021demographyandinternationalmigrationstatisticsforwales), 2022, Secondary → cites Census 2021 data
 │   └─ ONS bulletin (root, below)
 └─ [ONS, *International migration, England and Wales: Census 2021*](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021), 2022, Primary, root

### How it changed
None found.

The root gives the figure as 10.0 million of the 59.6 million usual residents of England and Wales (16.8%) on Census Day, 21 March 2021. It rounds that to about one in six itself, and it also gives the 2011 figure: 7.5 million (13.4%). Your version keeps the right year, the right area (England and Wales, not the whole UK) and the right measure (country of birth, not nationality or passport).

### Status of the root
- No correction, revision or errata notice found on the [bulletin page](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021). The page marks itself as the latest release. The bulletin is an official statistics release with no DOI, so Crossref, Retraction Watch and PubPeer were not checked.
- The bulletin says its numbers are estimates of the usual-resident population, adjusted for people who did not respond. It gives a person response rate of 97%.

### Cold trails
None.

### Confidence
High: the root is the ONS's own Census 2021 bulletin, which I opened; every link back to it was opened, and each date comes from the page's own date line.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
