---
case: true-statistic-born-outside-uk
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T19:21:52Z
cost_usd: 1.1666
duration_s: 117
turns: 27
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
- WebSearch: 2021 census 16.8% residents England Wales born outside UK
- WebSearch: ONS International migration England and Wales Census 2021 bulletin non-UK born 10 million
- WebSearch: "10 million" born outside UK census 2021 England Wales
- WebSearch: source of statistic one in six born abroad England Wales census
- WebSearch: Full Fact census 2021 born outside UK one in six
- WebFetch: https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021
- WebFetch: https://www.ons.gov.uk/news/news/census2021demographyandinternationalmigrationstatistics
- WebFetch: https://www.nationalworld.com/news/uk/census-2021-one-six-people-england-wales-born-outside-uk-3903034
- WebFetch: https://www.inkl.com/news/one-in-six-people-living-in-england-and-wales-were-born-in-a-different-country-census-reveals
- WebFetch: https://news.yahoo.com/england-waless-foreign-born-population-105156960.html
- WebFetch: https://www.breitbart.com/europe/2022/11/02/one-in-six-people-in-britain-were-born-in-foreign-countries-census/
- WebFetch: https://www.yahoo.com/news/england-waless-foreign-born-population-105156960.html
- WebFetch: https://scroll.in/latest/1037027/indians-comprised-highest-number-non-uk-born-residents-of-england-and-wales-shows-census-data
- WebFetch: https://www.truescoopnews.com/newsdetail/1-in-6-people-in-england-wales-born-abroad-mostly-india-census
- WebFetch: https://themuslimtimes.info/2022/11/02/one-in-six-people-living-in-england-and-wales-were-born-in-a-different-country-census-reveals/
- WebFetch (error): https://www.theguardian.com/uk-news/2022/nov/02/one-in-six-people-living-england-wales-were-born-different-country-census-reveals
- WebSearch: ONS demography and migration quality information Census 2021 country of birth
- WebFetch: https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/articles/thechangingpictureoflongterminternationalmigrationenglandandwales/census2021

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "In the 2021 census, one in six people in England and Wales were born outside the UK"

**Roots:** Echo · **Grounding:** Grounded
**Earliest instance found:** [Office for National Statistics, *International migration, England and Wales: Census 2021*](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021), 2022 (date from: byline, release date 2 November 2022; Census Day was 21 March 2021). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 9

### Chain
Your version: "In the 2021 census, one in six people in England and Wales were born outside the UK" (where you met it: not given)
- └─ [Scroll.in](https://scroll.in/latest/1037027/indians-comprised-highest-number-non-uk-born-residents-of-england-and-wales-shows-census-data), 2022, Tertiary → cites
  - └─ [ONS news release, *Census 2021: demography and international migration statistics*](https://www.ons.gov.uk/news/news/census2021demographyandinternationalmigrationstatistics), 2022, Secondary → cites
    - └─ [ONS bulletin, *International migration, England and Wales: Census 2021*](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021), 2022, Primary, root
- └─ [Breitbart, Kurt Zindulka](https://www.breitbart.com/europe/2022/11/02/one-in-six-people-in-britain-were-born-in-foreign-countries-census/), 2022, Secondary → cites the ONS bulletin (root, above)
- └─ [Reuters via Yahoo News, David Milliken](https://www.yahoo.com/news/england-waless-foreign-born-population-105156960.html), 2022, Secondary → cites the ONS census figures (root, above)
- └─ [TrueScoop News](https://www.truescoopnews.com/newsdetail/1-in-6-people-in-england-wales-born-abroad-mostly-india-census), 2022, Secondary → cites the ONS bulletin by title, via the IANS news agency (root, above)
- └─ [ONS article, *The changing picture of long-term international migration, England and Wales: Census 2021*](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/articles/thechangingpictureoflongterminternationalmigrationenglandandwales/census2021), 2023, Secondary → cites the ONS bulletin (root, above)
- └─ [The Muslim Times](https://themuslimtimes.info/2022/11/02/one-in-six-people-living-in-england-and-wales-were-born-in-a-different-country-census-reveals/), 2022, Tertiary → cites
  - └─ [The Guardian, Aguilar García, Goodier and Duncan](https://www.theguardian.com/uk-news/2022/nov/02/one-in-six-people-living-england-wales-were-born-different-country-census-reveals), 2022, (not opened), per The Muslim Times → stopped: not opened

### How it changed
None found.

The bulletin gives 10.0 million of 59.6 million usual residents (16.8%), up from 7.5 million (13.4%) in 2011. The bulletin itself sums this up as about one in six. Your version keeps its scope (England and Wales, 2021 census) and its figure. Off your version's path, the TrueScoop retelling reworded the figure so that it reads as though India were the country of birth for one in six residents. The bulletin names India as the most common non-UK country of birth, at 1.5% of residents.

### Status of the root
- No correction or revision notice on the [ONS bulletin page](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021). It gives a 97% person response rate and points to separate ONS quality information for Census 2021. Crossref, Retraction Watch and PubPeer were not checked: this is an official statistical bulletin with no DOI, not a journal paper.
- The [ONS article of 27 January 2023](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/articles/thechangingpictureoflongterminternationalmigrationenglandandwales/census2021) gives the same 10.0 million (16.8%) figure, and its page shows no revision or correction notice.

### Cold trails
None.

### Confidence
Medium: the root is an opened ONS Primary dated by its byline, and every branch but one was opened back to it. The Guardian article cited by The Muslim Times could not be fetched, and the NationalWorld and inkl retellings returned 403 errors, so they stay out of the chain.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
