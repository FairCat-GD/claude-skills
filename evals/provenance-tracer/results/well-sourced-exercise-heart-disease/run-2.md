---
case: well-sourced-exercise-heart-disease
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:31:51Z
cost_usd: 1.6597
duration_s: 278
turns: 38
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
- WebSearch: origin of the idea that exercise prevents heart disease history
- WebSearch: Jerry Morris London bus conductors drivers 1953 Lancet coronary heart disease physical activity
- WebSearch: who first showed physical activity reduces coronary heart disease earliest study
- WebSearch: Paffenbarger longshoremen Harvard alumni physical activity heart attack risk
- WebSearch: physical inactivity risk factor coronary heart disease American Heart Association 1992 statement
- WebFetch: https://www.nhlbi.nih.gov/health/heart/physical-activity/benefits
- WebFetch: https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger
- WebFetch: https://www.sciencedirect.com/science/article/abs/pii/S0140673653906655
- WebFetch: https://www.heartfoundation.org.au/healthy-living/physical-activity/physical-activity-and-exercise
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/S0140-6736(53)90665-5&resultType=core&format=json
- WebFetch: https://api.crossref.org/works/10.1016/S0140-6736(53)90665-5
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22coronary%20heart-disease%20and%20physical%20activity%20of%20work%22&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1093/oxfordjournals.aje.a112608&resultType=core&format=json
- WebSearch: "Coronary heart-disease and physical activity of work" Morris 1953 pubmed
- WebFetch: https://www.semanticscholar.org/paper/Physical-activity-as-an-index-of-heart-attack-risk-Paffenbarger-Wing/03bd073564ec5dfccd949753e750fb888c1ca715
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/13110049/
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC1750298/
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC11969862/
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1136/oem.10.4.245&resultType=core&format=json
- WebSearch: "Mortality in relation to the physical activity of work" Morris Heady 1953 PMC
- WebFetch: https://oem.bmj.com/content/10/4/245
- WebFetch: https://www.nejm.org/doi/full/10.1056/NEJM197005142822001
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC1402378/
- WebFetch: https://www.ahajournals.org/doi/10.1161/01.CIR.100.1.2
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:696021%20AND%20SRC:MED&resultType=core&format=json
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC3022443/
- WebFetch: https://pubpeer.com/search?q=10.1016/S0140-6736(53)90665-5
- WebFetch: https://api.crossref.org/works/10.1093/oxfordjournals.aje.a112608
- WebSearch: "Coronary heart-disease and physical activity of work" retraction OR erratum OR correction

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Regular exercise lowers the risk of heart disease."

**Roots:** Independent · **Grounding:** No primary found · Mutated
**Earliest instance found:** [Morris, Heady, Raffle, Roberts & Parks, *Coronary heart-disease and physical activity of work*, The Lancet](https://www.sciencedirect.com/science/article/abs/pii/S0140673653906655), 1953 (date from: cited by the [Crossref record](https://api.crossref.org/works/10.1016/S0140-6736(53)90665-5), which gives November 1953). Earlier instances may exist.
**Roots:** 2 · **Retellings found:** 10

### Chain
Your version: "Regular exercise lowers the risk of heart disease" (where you met it: not given)
 ├─ [Warburton, Nicol & Bredin, *Health benefits of physical activity: the evidence*, CMAJ](https://pmc.ncbi.nlm.nih.gov/articles/PMC1402378/), 2006, Secondary → cites
 │   ├─ [Morris et al., *Coronary heart-disease and physical activity of work*, The Lancet](https://www.sciencedirect.com/science/article/abs/pii/S0140673653906655), 1953, Primary (not opened, per Warburton et al. and the Crossref record), root 1
 │   └─ [Morris & Heady, *Mortality in relation to the physical activity of work*, Br J Ind Med](https://oem.bmj.com/content/10/4/245), 1953, Primary (not opened, per Warburton et al.), same team as root 1 → stopped: not opened
 ├─ [Andrade & Ignaszewski, *Exercise and the heart: A review of the early studies*, BCMJ](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger), 2007, Secondary → cites
 │   ├─ Morris et al., The Lancet, 1953: see root 1 above
 │   └─ [Paffenbarger, Laughlin, Gima & Black, *Work activity of longshoremen as related to death from coronary heart disease and stroke*, NEJM](https://www.nejm.org/doi/full/10.1056/NEJM197005142822001), 1970, Primary (not opened, per Andrade & Ignaszewski), root 2
 ├─ [Lange, *Jeremy Morris as a pioneer of behavioural epidemiology, social medicine and public health*, Scand J Public Health](https://pmc.ncbi.nlm.nih.gov/articles/PMC11969862/), 2023, Secondary → cites
 │   └─ Morris et al., The Lancet, 1953, and Morris & Heady, Br J Ind Med, 1953: see root 1 above
 └─ [Lee, Matthews & Blair, *The Legacy of Dr. Ralph Seal Paffenbarger, Jr.*, PCPFS Research Digest](https://pmc.ncbi.nlm.nih.gov/articles/PMC3022443/), 2009, Secondary → cites
     └─ [Paffenbarger, Wing & Hyde, *Physical activity as an index of heart attack risk in college alumni*, Am J Epidemiol](https://www.semanticscholar.org/paper/Physical-activity-as-an-index-of-heart-attack-risk-Paffenbarger-Wing/03bd073564ec5dfccd949753e750fb888c1ca715), 1978, Primary (not opened, per Lee et al. and the [Crossref record](https://api.crossref.org/works/10.1093/oxfordjournals.aje.a112608)), same team as root 2 → stopped: not opened

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | Root 1, as [Lange](https://pmc.ncbi.nlm.nih.gov/articles/PMC11969862/) and [Andrade & Ignaszewski](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger) describe it: men in physically active jobs (London bus conductors, postmen) had less coronary heart disease than men in sedentary jobs (bus drivers, clerks). It was about activity at work in middle-aged male workers, not exercise in general. Root 2's 1978 alumni study, per Lee et al., looked at leisure-time activity, but again only in men. | Regular exercise lowers the risk of heart disease | [Warburton et al., CMAJ](https://pmc.ncbi.nlm.nih.gov/articles/PMC1402378/), 2006 |

### Status of the root
- Morris et al., *The Lancet*, 1953: no retraction or correction found (Crossref record with no update relations; a web search for a retraction or erratum turned up none). The journal's page on ScienceDirect returned *403 Forbidden*. The [PubPeer search](https://pubpeer.com/search?q=10.1016/S0140-6736(53)90665-5) returned no usable content, and Retraction Watch's database was not searched directly.
- Paffenbarger, Wing & Hyde, *Am J Epidemiol*, 1978: the [Crossref record](https://api.crossref.org/works/10.1093/oxfordjournals.aje.a112608) lists no retraction, correction or erratum.
- Paffenbarger et al., *NEJM*, 1970: not checked. The publisher's page returned *403 Forbidden*.
- Background: the 1999 AHA editorial (page blocked), the 1992 *Baltimore Sun* report, and the 1992 AHA statement it covers (none opened) appear in search results as the point when the American Heart Association named physical inactivity a major risk factor for coronary disease. This is a later institutional endorsement, not an origin. Nothing from it is used as a node.

### Cold trails
- [NHLBI, *Physical Activity and Your Heart – Benefits*](https://www.nhlbi.nih.gov/health/heart/physical-activity/benefits), date unknown (the page shows only a last-updated date of March 2022): states the claim for moderate and vigorous aerobic activity, and cites nothing.
- [Heart Foundation (Australia), *Physical activity and your heart health*](https://www.heartfoundation.org.au/healthy-living/physical-activity/physical-activity-and-exercise), date unknown (the page shows only last-updated and last-reviewed dates): states the claim, with a one-third risk cut, and cites nothing for it.

### Confidence
Medium: the retellings that credit both roots were opened and agree on them, but neither root's paper could be opened (paywall or blocked pages on every copy tried), and their dates come from Crossref and the citing pages.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
