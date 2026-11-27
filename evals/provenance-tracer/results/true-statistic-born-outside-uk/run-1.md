---
case: true-statistic-born-outside-uk
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:30:31Z
cost_usd: 1.0485
duration_s: 82
turns: 26
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
- WebSearch: 2021 census 10 million born outside UK England and Wales ONS
- WebSearch: ONS International migration England and Wales Census 2021 bulletin
- WebSearch: "16.8%" born outside UK census 2021
- WebSearch: source of "one in six" born abroad England Wales census statistic
- WebSearch: Full Fact one in six born outside UK census 2021
- WebFetch: https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021
- WebFetch: https://www.ons.gov.uk/news/news/census2021demographyandinternationalmigrationstatistics
- WebFetch: https://www.nationalworld.com/news/uk/census-2021-one-six-people-england-wales-born-outside-uk-3903034
- WebFetch: https://www.inkl.com/news/one-in-six-people-living-in-england-and-wales-were-born-in-a-different-country-census-reveals
- WebFetch: https://www.xsmanchester.co.uk/news/uk-news/one-in-six-people-living-in-england-and-wales-were-born-outside-the-uk-census-data-shows/
- WebFetch: https://www.thenationalnews.com/world/uk-news/2022/11/02/where-10-million-foreign-born-residents-of-england-and-wales-are-from/
- WebFetch: https://www.radiox.co.uk/90s/news/uk-news/one-in-six-people-living-in-england-and-wales-were-born-outside-the-uk-census-data-shows/
- WebSearch: Guardian "one in six people living in England and Wales" born census November 2022
- WebFetch (error): https://www.theguardian.com/uk-news/2022/nov/02/one-in-six-people-living-england-wales-were-born-different-country-census-reveals
- WebFetch: https://www.yahoo.com/news/one-six-people-living-england-102800759.html
- WebFetch: https://uk.news.yahoo.com/one-six-people-living-england-102800759.html
- WebFetch: https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021/pdf

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "In the 2021 census, one in six people in England and Wales were born outside the UK"

**Roots:** Echo · **Grounding:** Grounded
**Earliest instance found:** [Office for National Statistics, *International migration, England and Wales: Census 2021*](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021), 2022 (date from: byline, released 2 November 2022). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 4

### Chain
Your version: "In the 2021 census, one in six people in England and Wales were born outside the UK" (where you met it: not given)
 └─ [Sky News story, republished on Yahoo News UK](https://uk.news.yahoo.com/one-six-people-living-england-102800759.html), 2022, Secondary. It says "One in six people living in England and Wales were born outside of the UK" and credits the ONS. → cites
     └─ [ONS, *International migration, England and Wales: Census 2021*](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021), 2022, Primary. It says "One in six usual residents of England and Wales were born outside the UK". In numbers, that is 10.0 million (16.8%) of 59.6 million usual residents on Census Day, 21 March 2021, up from 7.5 million (13.4%) in 2011. Contact named on the bulletin: Michael Roskams.
 └─ [The National, Simon Rushton, *Where 10 million foreign-born residents of England and Wales are from*](https://www.thenationalnews.com/world/uk-news/2022/11/02/where-10-million-foreign-born-residents-of-england-and-wales-are-from/), 2022, Secondary. It says "one in six people living in England and Wales was born abroad" and gives 16.8% from the ONS. → cites
     └─ ONS bulletin (above), Primary
 └─ [ONS news release, *Census 2021 demography and international migration statistics*](https://www.ons.gov.uk/news/news/census2021demographyandinternationalmigrationstatistics), 2022, Secondary. It says "One in six, or 10 million (16.8%), usual residents" and links to the bulletin. → cites
     └─ ONS bulletin (above), Primary

### How it changed
None found.

### Status of the root
- No correction or revision notice was found on the ONS bulletin page. The page says it is the latest release and is labelled accredited official statistics. The bulletin's PDF could not be read as text, so it was not checked separately. It has no DOI, so the journal, Crossref, Retraction Watch and PubPeer checks do not apply.

### Cold trails
None.

### Confidence
High: the root is the ONS bulletin, opened and dated by its byline, and every retelling in the chain was opened and credits the ONS. Some other copies could not be opened, so they are not in the chain: NationalWorld and inkl returned 403, The Guardian could not be fetched, and XS Manchester redirected to a Radio X page that returned 404.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
