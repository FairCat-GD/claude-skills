---
case: well-sourced-exercise-heart-disease
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:32:38Z
cost_usd: 1.4362
duration_s: 163
turns: 35
error: none
---

## Tool calls

- Skill: provenance-tracer:provenance-tracer
- Read: <plugin>/skills/provenance-tracer/references/output-template.md
- Read: <plugin>/skills/provenance-tracer/references/search-playbook.md
- Read: <plugin>/skills/provenance-tracer/references/labels.md
- Read: <plugin>/skills/provenance-tracer/references/mutation-types.md
- ToolSearch: {"query":"select:WebSearch,WebFetch","max_results":2}
- WebSearch: "regular exercise lowers the risk of heart disease"
- WebSearch: physical activity reduces coronary heart disease risk first study origin history
- WebSearch: Jerry Morris 1953 London bus conductors drivers coronary heart disease Lancet
- WebSearch: who first showed exercise prevents heart disease
- WebSearch: Paffenbarger longshoremen Harvard alumni physical activity heart attack study
- WebSearch: exercise heart disease risk 30 percent lower claim fact check
- WebFetch: https://www.nhlbi.nih.gov/health/heart/physical-activity/benefits
- WebFetch: https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger
- WebFetch: https://www.sciencedirect.com/science/article/abs/pii/S0140673653906655
- WebFetch (error): http://www.epi.umn.edu/cvdepi/study-synopsis/london-transport-workers-study/
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/S0140-6736(53)90665-5&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:"physical activity as an index of heart attack risk in college alumni"&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:"work activity of longshoremen as related to death from coronary heart disease and stroke"&resultType=core&format=json
- WebSearch: pubmed Morris Heady Raffle 1953 "Coronary heart-disease and physical activity of work"
- WebSearch: pubmed Paffenbarger Wing Hyde 1978 "Physical activity as an index of heart attack risk in college alumni"
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/707484/
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/?term=10.1016%2Fs0140-6736%2853%2990665-5
- WebFetch: https://www.nejm.org/doi/full/10.1056/NEJM197005142822001
- WebFetch: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(53)90665-5/fulltext
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:707484&resultType=core&format=json
- WebFetch: https://api.crossref.org/works/10.1016/s0140-6736(53)90665-5
- WebFetch: https://www.semanticscholar.org/paper/Physical-activity-as-an-index-of-heart-attack-risk-Paffenbarger-Wing/03bd073564ec5dfccd949753e750fb888c1ca715
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC3022443/
- WebFetch (error): https://web.archive.org/web/2020/http://www.epi.umn.edu/cvdepi/document/coronary-heart-disease-and-physical-activity-of-work/
- WebFetch: https://doi.org/10.1093/oxfordjournals.aje.a112608
- WebFetch: https://api.crossref.org/works/10.1093/oxfordjournals.aje.a112608
- WebFetch: https://api.crossref.org/works/10.1056/NEJM197005142822001

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Regular exercise lowers the risk of heart disease."

**Roots:** Independent · **Grounding:** No primary found · Mutated
**Earliest instance found:** [Morris, Heady, Raffle, Roberts & Parks, *Coronary Heart-Disease and Physical Activity of Work*, The Lancet](https://www.sciencedirect.com/science/article/abs/pii/S0140673653906655), 1953 (date from: cited by [BCMJ review](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger); the [Crossref record](https://api.crossref.org/works/10.1016/s0140-6736(53)90665-5) gives November 1953). Earlier instances may exist.
**Roots:** 2 · **Retellings found:** 4

### Chain
Your version: "Regular exercise lowers the risk of heart disease" (where you met it: not given)
 └─ [Andrade & Ignaszewski, *Exercise and the heart: A review of the early studies*, BCMJ](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger), 2007, Secondary → cites
     ├─ [Morris et al., *Coronary Heart-Disease and Physical Activity of Work*, The Lancet](https://www.sciencedirect.com/science/article/abs/pii/S0140673653906655), 1953, Primary (not opened, per BCMJ review), root 1
     └─ Paffenbarger et al., [*Work Activity of Longshoremen…*, NEJM](https://www.nejm.org/doi/full/10.1056/NEJM197005142822001), 1970, and [*Physical Activity as an Index of Heart Attack Risk in College Alumni*, Am J Epidemiol](https://doi.org/10.1093/oxfordjournals.aje.a112608), 1978, Primary (not opened, per BCMJ review), root 2

The BCMJ review says these studies were "the first to link physical activity and exercise to a lower risk" of heart disease. The two lines of work came from different teams, each with its own data, and retellings credit both. Paffenbarger's two papers are counted as one root because they come from one team.

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | Root 1's title, per its Crossref record, is about *physical activity of work*: active London bus conductors compared with seated drivers, per the BCMJ review. It is not about exercise as such | Regular exercise lowers the risk of heart disease | [BCMJ review](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger), 2007 |

### Status of the root
- Morris et al. 1953: the [Crossref record](https://api.crossref.org/works/10.1016/s0140-6736(53)90665-5) lists no retraction, correction or erratum. The BCMJ review cites a second part of the paper, The Lancet 1953, pp. 1111–1120.
- Paffenbarger et al. 1978: the [Crossref record](https://api.crossref.org/works/10.1093/oxfordjournals.aje.a112608) lists no retraction, correction or erratum.
- Paffenbarger et al. 1970: the [Crossref record](https://api.crossref.org/works/10.1056/NEJM197005142822001) lists no retraction, correction or erratum.
- I did not run Retraction Watch or PubPeer checks. None of the papers' own pages or abstracts could be opened: ScienceDirect, The Lancet, NEJM, PubMed, Europe PMC and Semantic Scholar all refused or failed, and the DOI for the 1978 paper redirected to an Oxford Academic page that I could not fetch within the budget.

### Cold trails
- [NHLBI, *Physical Activity and Your Heart – Benefits*](https://www.nhlbi.nih.gov/health/heart/physical-activity/benefits), date unknown (the page shows only a last-updated date of 2022). It says regular aerobic activity "can lower your risk for coronary heart disease" and cites no study.

### Confidence
Medium: the review that cites both roots was opened and dated from its byline, but neither root's Primary could be opened, so the roots rest on that review's citations.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
