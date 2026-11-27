---
case: true-statistic-born-outside-uk
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:31:41Z
cost_usd: 1.0264
duration_s: 80
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
- WebSearch: "one in six" people England and Wales born outside the UK 2021 census
- WebSearch: ONS International migration England and Wales Census 2021 non-UK born 16.8%
- WebSearch: "10 million" people born outside UK census 2021 England Wales
- WebSearch: source of "one in six" born abroad England Wales census statistic
- WebSearch: Full Fact census 2021 born outside UK one in six
- WebSearch: census 2021 a sixth of residents England Wales born abroad first appeared November 2022
- WebFetch: https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021
- WebFetch: https://www.nationalworld.com/news/uk/census-2021-one-six-people-england-wales-born-outside-uk-3903034
- WebFetch: https://www.thenationalnews.com/world/uk-news/2022/11/02/where-10-million-foreign-born-residents-of-england-and-wales-are-from/
- WebFetch: https://www.ons.gov.uk/news/news/census2021demographyandinternationalmigrationstatistics
- WebFetch: https://www.yahoo.com/news/one-six-people-living-england-102800759.html
- WebFetch: https://kalingatv.com/world/1-in-6-people-in-england-wales-born-abroad-mostly-india-census/
- WebSearch: ONS Census 2021 country of birth quality information correction revised international migration bulletin
- WebFetch: https://uk.news.yahoo.com/one-six-people-living-england-102800759.html
- WebFetch: https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/methodologies/demographyandmigrationqualityinformationforcensus2021

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "In the 2021 census, one in six people in England and Wales were born outside the UK."

**Roots:** Echo · **Grounding:** Grounded
**Earliest instance found:** [Office for National Statistics, *International migration, England and Wales: Census 2021*](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021), 2022 (date from: byline, release date 2 November 2022). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 4

### Chain
Your version: "In the 2021 census, one in six people in England and Wales were born outside the UK" (where you met it: not given)
 ├─ [Sky News, via *Yahoo News UK*](https://uk.news.yahoo.com/one-six-people-living-england-102800759.html), 2022, Secondary → cites
 │   └─ [ONS, *International migration, England and Wales: Census 2021*](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021), 2022, Primary
 ├─ [Simon Rushton, *Where 10 million foreign-born residents of England and Wales are from*, The National](https://www.thenationalnews.com/world/uk-news/2022/11/02/where-10-million-foreign-born-residents-of-england-and-wales-are-from/), 2022, Secondary → cites
 │   └─ ONS, *International migration, England and Wales: Census 2021*, 2022, Primary (the same node as above)
 └─ [ONS news release, *Census 2021 demography and international migration statistics*](https://www.ons.gov.uk/news/news/census2021demographyandinternationalmigrationstatistics), 2022, Secondary → cites
     └─ ONS, *International migration, England and Wales: Census 2021*, 2022, Primary (the same node as above)

The root is the ONS bulletin. It reports results from Census 2021, which was taken on Census Day, 21 March 2021. Its main points say ["One in six usual residents of England and Wales were born outside the UK"](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021). It gives the count as 10.0 million of 59.6 million usual residents (16.8%), up from 7.5 million (13.4%) in 2011. The Sky News and *The National* pieces from the same day both credit the ONS census data and quote the census deputy director, Jon Wroth-Smith.

### How it changed
None found. Your version says "people" where the bulletin says "usual residents", which is the population a census counts. The Sky News retelling uses the same wording as yours: ["One in six people living in England and Wales were born outside of the UK"](https://uk.news.yahoo.com/one-six-people-living-england-102800759.html). "One in six" rounds 16.8%, and the ONS uses that rounding itself.

### Status of the root
- The bulletin has no DOI, so Crossref, Retraction Watch and PubPeer do not apply. Its [ONS release page](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021) shows no correction or revision notice.
- The ONS page [*Demography and migration quality information for Census 2021*](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/methodologies/demographyandmigrationqualityinformationforcensus2021) (last revised 6 September 2023) lists one known issue: Croatian passport holders were miscoded. That affects the passports-held figures, not country of birth. The same page says short-term residents (under 200,000 people) were not adjusted for non-response. It notes this as a caveat, not a correction.

### Cold trails
None.

### Confidence
High: the root is an opened Primary dated by its own release byline, and every retelling in the chain was opened and credits it.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
