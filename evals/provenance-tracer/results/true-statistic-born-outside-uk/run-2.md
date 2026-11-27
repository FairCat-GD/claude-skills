---
case: true-statistic-born-outside-uk
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:30:50Z
cost_usd: 1.0325
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
- WebSearch: "one in six" born outside the UK 2021 census England and Wales
- WebSearch: ONS International migration England and Wales Census 2021 born outside UK 10 million
- WebSearch: "16.8%" born outside the UK census 2021
- WebSearch: census 2021 one in six residents born abroad England Wales news November 2022
- WebSearch: source of statistic one in six people in England and Wales born abroad
- WebSearch: Full Fact census 2021 born outside UK one in six
- WebFetch: https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021
- WebFetch: https://www.yahoo.com/news/one-six-people-living-england-102800759.html
- WebFetch: https://www.nationalworld.com/news/uk/census-2021-one-six-people-england-wales-born-outside-uk-3903034
- WebFetch: https://www.ons.gov.uk/news/news/census2021demographyandinternationalmigrationstatistics
- WebFetch: https://uk.news.yahoo.com/one-six-people-living-england-102800759.html
- WebFetch: https://www.thenationalnews.com/world/uk-news/2022/11/02/where-10-million-foreign-born-residents-of-england-and-wales-are-from/
- WebFetch: https://gulfnews.com/world/asia/india/1-in-6-people-in-england-wales-born-abroad-mostly-india-census-1.91843803
- WebFetch: https://www.breitbart.com/europe/2022/11/02/one-in-six-people-in-britain-were-born-in-foreign-countries-census/
- WebSearch: ONS "International migration, England and Wales: Census 2021" correction OR revision OR erratum

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "In the 2021 census, one in six people in England and Wales were born outside the UK."

**Roots:** Echo · **Grounding:** Grounded
**Earliest instance found:** [Office for National Statistics, *International migration, England and Wales: Census 2021*](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021), 2022 (date from: byline, release date 2 November 2022). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 6

### Chain
Your version: "In the 2021 census, one in six people in England and Wales were born outside the UK" (where you met it: not given)
 ├─ [Sky News, via Yahoo News UK](https://uk.news.yahoo.com/one-six-people-living-england-102800759.html), 2022, Secondary → cites
 │   └─ ONS (named in the text: "the Office for National Statistics said")
 ├─ [Simon Rushton, *The National*](https://www.thenationalnews.com/world/uk-news/2022/11/02/where-10-million-foreign-born-residents-of-england-and-wales-are-from/), 2022, Secondary → cites
 │   └─ "data released by the Office for National Statistics (ONS) on Wednesday"
 ├─ [Kurt Zindulka, Breitbart](https://www.breitbart.com/europe/2022/11/02/one-in-six-people-in-britain-were-born-in-foreign-countries-census/), 2022, Secondary → cites
 │   └─ the ONS bulletin (linked)
 ├─ [IANS, via *Gulf News*](https://gulfnews.com/world/asia/india/1-in-6-people-in-england-wales-born-abroad-mostly-india-census-1.91843803), 2022, Secondary → cites
 │   └─ the ONS bulletin (named by title)
 └─ [ONS news release](https://www.ons.gov.uk/news/news/census2021demographyandinternationalmigrationstatistics), 2022, Secondary → cites
     └─ [ONS, *International migration, England and Wales: Census 2021*](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021), 2022, Primary

All five retellings point back to the same ONS bulletin. It is built on Census 2021 table TS004 (country of birth). Its main points say: ["One in six usual residents of England and Wales were born outside the UK"](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/internationalmigrationenglandandwales/census2021). That is 10.0 million (16.8%) of 59.6 million usual residents, counted on Census Day, 21 March 2021. The figure was 7.5 million (13.4%) in 2011.

### How it changed
None found.

Your wording matches the bulletin's own. The bulletin says "usual residents" in its main points and "people" in section 3. The figure is rounded from 16.8%, and the bulletin itself does that rounding. It also covers England and Wales only, as your version does. Two retellings changed the claim, but not on the way to your version:
- **Gulf News (IANS):** says ["India was found to be the most common country of birth for one in six"](https://gulfnews.com/world/asia/india/1-in-6-people-in-england-wales-born-abroad-mostly-india-census-1.91843803). That attaches the share to India. In the bulletin, India is only the most common single country of birth outside the UK, with about 920,000 people.
- **Breitbart:** mixes "England and Wales" in its headline with "Britain" in the body, which widens the scope.

### Status of the root
- No correction or revision notice appears on the bulletin page, and a search for a correction, revision or erratum found none for this bulletin. This is an official statistics release, not a journal article, so Crossref, Retraction Watch and PubPeer do not apply.

### Cold trails
None.

### Confidence
High: the root is an opened ONS Primary dated by its own release byline, and every retelling in the chain was opened and names it.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
