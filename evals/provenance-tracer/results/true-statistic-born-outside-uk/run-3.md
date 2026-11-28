---
case: true-statistic-born-outside-uk
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:47:37Z
cost_usd: 1.1220
duration_s: 84
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
- WebSearch: "one in six" people England and Wales born outside the UK 2021 census
- WebSearch: 2021 census 10 million residents born outside UK England and Wales ONS
- WebSearch: ONS International migration England and Wales Census 2021 bulletin non-UK born 16.8%
- WebSearch: "16.8%" born outside the UK census 2021
- WebSearch: source of "one in six" born abroad England Wales census statistic
- WebSearch: Full Fact one in six born outside UK census 2021
- WebFetch: https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021
- WebFetch: https://www.ons.gov.uk/news/news/census2021demographyandinternationalmigrationstatistics
- WebFetch: https://www.nationalworld.com/news/uk/census-2021-one-six-people-england-wales-born-outside-uk-3903034
- WebFetch: https://www.thenationalnews.com/world/uk-news/2022/11/02/where-10-million-foreign-born-residents-of-england-and-wales-are-from/
- WebFetch: https://www.xsmanchester.co.uk/news/uk-news/one-in-six-people-living-in-england-and-wales-were-born-outside-the-uk-census-data-shows/
- WebFetch: https://www.radiox.co.uk/90s/news/uk-news/one-in-six-people-living-in-england-and-wales-were-born-outside-the-uk-census-data-shows/
- WebFetch: https://gulfnews.com/world/asia/india/1-in-6-people-in-england-wales-born-abroad-mostly-india-census-1.91843803
- WebFetch: https://www.inkl.com/news/one-in-six-people-living-in-england-and-wales-were-born-in-a-different-country-census-reveals
- WebSearch: Census 2021 England Wales country of birth estimates revised OR correction OR quality ONS
- WebFetch: https://www.nomisweb.co.uk/datasets/c2021ts004

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "In the 2021 census, one in six people in England and Wales were born outside the UK."

**Roots:** Echo · **Grounding:** Grounded
**Earliest instance found:** [ONS, *International migration, England and Wales: Census 2021*](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021), 2022 (date from: byline, released 2 November 2022; the data are for Census Day, 21 March 2021). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 4

### Chain
Your version: "In the 2021 census, one in six people in England and Wales were born outside the UK" (where you met it: not given)
 ├─ [The National, *Where 10 million foreign-born residents of England and Wales are from*](https://www.thenationalnews.com/world/uk-news/2022/11/02/where-10-million-foreign-born-residents-of-england-and-wales-are-from/), 2022, Secondary → cites the ONS data release
 │   └─ [ONS, *International migration, England and Wales: Census 2021*](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021), 2022, Primary, root
 ├─ [Gulf News (IANS wire), *1 in 6 people in England, Wales born abroad, mostly India*](https://gulfnews.com/world/asia/india/1-in-6-people-in-england-wales-born-abroad-mostly-india-census-1.91843803), 2022, Secondary → cites the ONS bulletin by title (root, above)
 └─ [ONS press release, *Census 2021 demography and international migration statistics*](https://www.ons.gov.uk/news/news/census2021demographyandinternationalmigrationstatistics), 2022, Secondary → cites the ONS bulletin (root, above)

The root is the Office for National Statistics' census bulletin. It says that of 59.6 million usual residents of England and Wales, [10.0 million (16.8%) were born outside the UK](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021). Its main points round that figure to one in six. In 2011 the figure was 7.5 million (13.4%). The other three retellings got the figure from this bulletin; I found none with an independent source. The Gulf News/IANS story garbles it in one sentence, which reads as if India were the birthplace of the one in six. Elsewhere in the same story it gives the 16.8% figure correctly.

### How it changed
None found.

### Status of the root
- The bulletin page shows no correction or revision notices. It is marked as accredited official statistics ([ONS bulletin](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021)).
- The underlying census table, TS004 *Country of birth*, says it has had no revisions or corrections ([Nomis TS004](https://www.nomisweb.co.uk/datasets/c2021ts004)).
- The bulletin counts usual residents only and excludes short-term residents. It covers England and Wales only, because Scotland and Northern Ireland ran separate censuses ([ONS bulletin](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021)).
- This is a government statistical release, not a journal paper, so Crossref, Retraction Watch and PubPeer do not apply.

### Cold trails
None.

### Confidence
High: the root is an official statistical bulletin that I opened, dated by its printed release date, and every retelling I used was opened and names it (NationalWorld and inkl copies were not used, as their fetches failed).

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
