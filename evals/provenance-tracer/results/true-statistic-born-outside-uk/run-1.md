---
case: true-statistic-born-outside-uk
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:47:20Z
cost_usd: 1.1497
duration_s: 97
turns: 23
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
- WebSearch: ONS International migration England and Wales Census 2021 non-UK-born 10 million 16.8%
- WebSearch: "16.8%" born outside the UK census 2021
- WebSearch: source of statistic one in six people in England and Wales born abroad census
- WebSearch: Full Fact census 2021 born outside UK one in six
- WebSearch: census 2021 a sixth of residents of England and Wales born abroad BBC
- WebFetch: https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021
- WebFetch: https://www.ons.gov.uk/news/news/census2021demographyandinternationalmigrationstatistics
- WebFetch: https://www.nationalworld.com/news/uk/census-2021-one-six-people-england-wales-born-outside-uk-3903034
- WebFetch: https://www.yahoo.com/news/one-six-people-living-england-102800759.html
- WebFetch: https://www.thenationalnews.com/world/uk-news/2022/11/02/where-10-million-foreign-born-residents-of-england-and-wales-are-from/
- WebFetch: https://uk.news.yahoo.com/one-six-people-living-england-102800759.html
- WebFetch: https://themuslimtimes.info/2022/11/02/one-in-six-people-living-in-england-and-wales-were-born-in-a-different-country-census-reveals/
- WebFetch: https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/articles/thechangingpictureoflongterminternationalmigrationenglandandwales/census2021
- WebSearch: Guardian "One in six people living in England and Wales in 2021 were born in a different country"

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "In the 2021 census, one in six people in England and Wales were born outside the UK."

**Roots:** Echo · **Grounding:** Grounded
**Earliest instance found:** [Office for National Statistics, *International migration, England and Wales: Census 2021*](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021), 2022 (date from: byline, released 2 November 2022). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 7

### Chain
Your version: "In the 2021 census, one in six people in England and Wales were born outside the UK" (where you met it: not given)
 ├─ [Sky News, republished on Yahoo News UK](https://uk.news.yahoo.com/one-six-people-living-england-102800759.html), 2022, Secondary → cites the ONS census release (the root, below)
 ├─ [The National, Simon Rushton](https://www.thenationalnews.com/world/uk-news/2022/11/02/where-10-million-foreign-born-residents-of-england-and-wales-are-from/), 2022, Secondary → cites ONS census data (the root, below)
 ├─ [The Muslim Times, reposting a Guardian article](https://themuslimtimes.info/2022/11/02/one-in-six-people-living-in-england-and-wales-were-born-in-a-different-country-census-reveals/), 2022, Tertiary → cites
 │   └─ The Guardian, Carmen Aguilar García, Michael Goodier and Pamela Duncan, 2022, (not opened), per The Muslim Times → cites the latest census figures (the root, below)
 ├─ [ONS, *The changing picture of long-term international migration, England and Wales: Census 2021*](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/articles/thechangingpictureoflongterminternationalmigrationenglandandwales/census2021), 2023, Secondary → cites Census 2021 data and its companion bulletin (the root, below)
 └─ [ONS news release, *Census 2021: demography and international migration statistics*](https://www.ons.gov.uk/news/news/census2021demographyandinternationalmigrationstatistics), 2022, Secondary → cites
     └─ [ONS, *International migration, England and Wales: Census 2021*](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021), 2022, Primary, root

### How it changed
None found.

### Status of the root
- The [bulletin's page](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021) shows no correction or revision notice and carries the accredited official statistics badge. It gives 10.0 million (16.8%) of 59.6 million usual residents as born outside the UK on Census Day, 21 March 2021, up from 7.5 million (13.4%) in 2011. Crossref, Retraction Watch and PubPeer were not checked because the bulletin is an official statistics release with no DOI.
- Scope notes on the same [bulletin](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021):
  - The figure counts *usual residents* only, meaning people staying 12 months or more.
  - About 136,000 short-term residents are left out of it.
  - The figure covers England and Wales only, because Scotland's census was moved to March 2022.
- The ONS [follow-up article](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/articles/thechangingpictureoflongterminternationalmigrationenglandandwales/census2021) of 27 January 2023 gives the same 10.0 million (16.8%) figure but does not use the *one in six* wording for it. That wording appears there only for UK-born residents who hold no passport.

### Cold trails
None.

### Confidence
Medium: the root and every news retelling except one were opened and dated by byline, but the Guardian original was seen only through a reposted copy and was not opened.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
