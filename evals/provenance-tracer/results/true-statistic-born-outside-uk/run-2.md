---
case: true-statistic-born-outside-uk
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:47:29Z
cost_usd: 1.1512
duration_s: 99
turns: 28
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
- WebSearch: ONS International migration England and Wales Census 2021 10.0 million born outside UK
- WebSearch: "16.8%" born outside the UK census 2021
- WebSearch: source of "one in six" residents England Wales born abroad statistic census
- WebSearch: Full Fact census 2021 born outside UK one in six
- WebSearch: census 2021 a sixth of population England and Wales born abroad news November 2022
- WebFetch: https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021
- WebFetch: https://www.ons.gov.uk/news/news/census2021demographyandinternationalmigrationstatistics
- WebFetch: https://www.nationalworld.com/news/uk/census-2021-one-six-people-england-wales-born-outside-uk-3903034
- WebFetch: https://www.thenationalnews.com/world/uk-news/2022/11/02/where-10-million-foreign-born-residents-of-england-and-wales-are-from/
- WebFetch: https://www.yahoo.com/news/one-six-people-living-england-102800759.html
- WebFetch: https://www.inkl.com/news/one-in-six-people-living-in-england-and-wales-were-born-in-a-different-country-census-reveals
- WebFetch: https://uk.news.yahoo.com/one-six-people-living-england-102800759.html
- WebFetch: https://www.lokmattimes.com/international/1-in-6-people-in-england-wales-born-abroad-mostly-india-census/
- WebFetch: https://themuslimtimes.info/2022/11/02/one-in-six-people-living-in-england-and-wales-were-born-in-a-different-country-census-reveals/
- WebFetch: https://www.breitbart.com/europe/2022/11/02/one-in-six-people-in-britain-were-born-in-foreign-countries-census/
- WebFetch (error): https://www.theguardian.com/uk-news/2022/nov/02/one-in-six-people-living-england-wales-were-born-different-country-census-reveals
- WebSearch: ONS census 2021 country of birth TS004 correction OR revision OR error notice
- WebFetch: https://www.nomisweb.co.uk/datasets/c2021ts004
- WebFetch: https://www.ons.gov.uk/news/statementsandletters/statementoninaccurateclaimsaboutcountryofbirthstatisticsandthecensus

## Reply

**Assumptions** (no reply was possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "In the 2021 census, one in six people in England and Wales were born outside the UK."

**Roots:** Echo · **Grounding:** Grounded
**Earliest instance found:** [ONS, *International migration, England and Wales: Census 2021*](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021), 2022 (date from: byline, released 2 November 2022). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 7

### Chain
Your version: "In the 2021 census, one in six people in England and Wales were born outside the UK" (where you met it: not given)
 ├─ [The Muslim Times](https://themuslimtimes.info/2022/11/02/one-in-six-people-living-in-england-and-wales-were-born-in-a-different-country-census-reveals/), 2022, Tertiary (reposts a Guardian article) → cites
 │   └─ [The Guardian, Aguilar García, Goodier & Duncan](https://www.theguardian.com/uk-news/2022/nov/02/one-in-six-people-living-england-wales-were-born-different-country-census-reveals), 2022, (not opened), per The Muslim Times → stopped: not opened
 ├─ [Yahoo News UK, republishing Sky News](https://uk.news.yahoo.com/one-six-people-living-england-102800759.html), 2022 (the page's update stamp; no first date given), Secondary → cites
 │   └─ [ONS, *International migration, England and Wales: Census 2021*](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021), 2022, Primary, root
 ├─ [The National, Simon Rushton](https://www.thenationalnews.com/world/uk-news/2022/11/02/where-10-million-foreign-born-residents-of-england-and-wales-are-from/), 2022, Secondary → cites the ONS bulletin (root, above)
 ├─ [Breitbart, Kurt Zindulka](https://www.breitbart.com/europe/2022/11/02/one-in-six-people-in-britain-were-born-in-foreign-countries-census/), 2022, Secondary → cites the ONS bulletin (root, above)
 └─ [ONS news release](https://www.ons.gov.uk/news/news/census2021demographyandinternationalmigrationstatistics), 2022, Secondary → cites the ONS bulletin (root, above)

### How it changed
None found.

### Status of the root
- ONS bulletin: gives the count as "10.0 million (16.8%) were born outside the UK" out of 59.6 million usual residents on Census Day, 21 March 2021, up from 7.5 million (13.4%) in 2011. The page shows no correction or revision notice. It covers England and Wales only, because Scotland's census was moved to 2022.
- Census table TS004 (Country of birth), the dataset behind the bulletin, on [Nomis](https://www.nomisweb.co.uk/datasets/c2021ts004): "There have been no revisions or corrections."
- [ONS statement on inaccurate claims about country of birth statistics](https://www.ons.gov.uk/news/statementsandletters/statementoninaccurateclaimsaboutcountryofbirthstatisticsandthecensus), November 2022: it rejects claims that the ONS planned to stop asking about country of birth. The corrections it describes apply to the Annual Population Survey series, not to the Census 2021 figure.

### Cold trails
None.

### Confidence
High: the root is the ONS bulletin, opened and dated by its byline, and the opened retellings name the ONS directly. Only the Guardian branch could not be opened.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
