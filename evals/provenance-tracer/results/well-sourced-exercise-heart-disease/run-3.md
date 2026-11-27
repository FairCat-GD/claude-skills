---
case: well-sourced-exercise-heart-disease
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:32:10Z
cost_usd: 1.1989
duration_s: 177
turns: 33
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
- WebSearch: physical activity reduces coronary heart disease risk first evidence history
- WebSearch: Jerry Morris 1953 London bus conductors drivers coronary heart disease Lancet
- WebSearch: origin of idea exercise prevents heart disease who first discovered
- WebSearch: "30 to 50 percent" lower risk heart disease physically active
- WebSearch: fact check exercise lowers heart disease risk claim
- WebFetch: https://www.nhlbi.nih.gov/health/heart/physical-activity/benefits
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/11689543/
- WebFetch: https://www.sciencedirect.com/science/article/abs/pii/S0140673653906655
- WebFetch: https://en.wikipedia.org/wiki/Jerry_Morris
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/16222619
- WebFetch: https://api.crossref.org/works/10.1016/S0140-6736(53)90665-5
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:11689543%20AND%20SRC:MED&resultType=core&format=json
- WebFetch: https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger
- WebFetch: https://history.rcp.ac.uk/inspiring-physicians/jeremy-noah-morris
- WebFetch: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(53)90665-5/fulltext
- WebFetch: https://paulogentil.com/pdf/A%20tribute%20to%20Professor%20Jeremiah%20Morris%20-%20the%20man%20who%20invented%20the%20field%20of%20physical%20activity%20epidemiology.pdf
- WebFetch: https://www.cdc.gov/physical-activity-basics/benefits/index.html
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=AUTH:%22Morris%20JN%22%20AND%20(PUB_YEAR:1953%20OR%20PUB_YEAR:1973)%20AND%20coronary&resultType=core&format=json
- WebFetch: https://www.sciencedirect.com/science/article/abs/pii/0091743572900795
- WebFetch: https://www.ncbi.nlm.nih.gov/pmc/articles/pmid/13106231/
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/pmid/13106231/
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:13106231%20AND%20SRC:MED&resultType=core&format=json
- WebFetch: https://europepmc.org/articles/PMC1037497?pdf=render
- WebFetch: https://oem.bmj.com/content/10/4/245

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Regular exercise lowers the risk of heart disease."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** [Morris, Heady, Raffle, Roberts & Parks, *Coronary heart-disease and physical activity of work*, The Lancet 262(6795):1053–1057](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(53)90665-5/fulltext), November 1953 (date from: cited by the [Crossref record](https://api.crossref.org/works/10.1016/S0140-6736(53)90665-5)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 9

### Chain
Your version: "Regular exercise lowers the risk of heart disease" (where you met it: not given)
 ├─ [Royal College of Physicians Museum, *Jeremy Noah Morris*](https://history.rcp.ac.uk/inspiring-physicians/jeremy-noah-morris), date unknown, Secondary → cites
 │   └─ [Morris et al., *Coronary heart-disease and physical activity of work*, The Lancet](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(53)90665-5/fulltext), 1953, Primary (not opened, per RCP Museum and BCMJ) → stopped: not opened
 ├─ [Andrade & Ignaszewski, *Exercise and the heart: A review of the early studies*, BCMJ 49(10)](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger), 2007, Secondary → cites
 │   ├─ Morris et al., The Lancet, 1953, Primary (not opened, per BCMJ), the same root as above
 │   └─ [Paffenbarger, Blair & Lee, *A history of physical activity, cardiovascular health and longevity*, Int J Epidemiol 30(5)](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:11689543%20AND%20SRC:MED&resultType=core&format=json), 2001, Secondary (abstract opened via Europe PMC) → cites
 │       └─ Morris et al., The Lancet, 1953, Primary (not opened), the same root
 ├─ [Wikipedia, *Jerry Morris*](https://en.wikipedia.org/wiki/Jerry_Morris), date unknown, Tertiary → cites
 │   └─ Simon Kuper, *The man who invented exercise*, Financial Times, 2009, (not opened), per Wikipedia → stopped: not opened
 └─ Companion paper: [Morris & Heady, *Mortality in relation to the physical activity of work: a preliminary note on experience in middle age*, Br J Ind Med 10(4):245–254](https://oem.bmj.com/content/10/4/245), 1953, Primary (not opened, per [Europe PMC record](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=AUTH:%22Morris%20JN%22%20AND%20(PUB_YEAR:1953%20OR%20PUB_YEAR:1973)%20AND%20coronary&resultType=core&format=json)) → stopped: not opened

According to the opened retellings, the root studied about 31,000 male London transport workers aged 35–65. Conductors climbed stairs all day and drivers sat. The conductors had less coronary heart disease than the drivers, and it came later in life. The BCMJ review describes this as the authors suggesting that physically active work had a protective effect.

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | Physically active *work* in male London transport workers aged 35–65 (per BCMJ, 2007) | regular exercise, everyone | [RCP Museum](https://history.rcp.ac.uk/inspiring-physicians/jeremy-noah-morris), date unknown: "the beneficial impact of regular exercise" |
| Hedge dropped | the authors *suggested* a protective effect (per BCMJ, 2007) | lowers the risk | [RCP Museum](https://history.rcp.ac.uk/inspiring-physicians/jeremy-noah-morris), date unknown, which says "showing unequivocally" |

The wider scope may come from Morris's own later work rather than from retelling. His 1973 *Lancet* paper on leisure-time exercise studied exercise outside work (see below). That paper was not opened.

### Status of the root
- No correction, retraction or other update is listed on the [Crossref record](https://api.crossref.org/works/10.1016/S0140-6736(53)90665-5) for the 1953 *Lancet* paper. The journal page returned 403. Retraction Watch and PubPeer were not checked because the fetch budget ran out.
- Major later studies:
  - Morris et al., *Vigorous exercise in leisure-time and the incidence of coronary heart-disease*, Lancet 1973;1:333–339. It is listed in the [Europe PMC record](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=AUTH:%22Morris%20JN%22%20AND%20(PUB_YEAR:1953%20OR%20PUB_YEAR:1973)%20AND%20coronary&resultType=core&format=json), which has no abstract, so its findings were not read.
  - Paffenbarger et al., a study of San Francisco longshoremen, NEJM 1970;282:1109–1114. According to [BCMJ](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger), the most active cargo handlers had significantly lower death rates from coronary disease.
  - Paffenbarger, Blair & Lee (2001). Their [abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:11689543%20AND%20SRC:MED&resultType=core&format=json) says later studies in many populations and countries reinforced the finding.

### Cold trails
- [NHLBI, *Physical Activity and Your Heart: Benefits*](https://www.nhlbi.nih.gov/health/heart/physical-activity/benefits), date unknown (the page shows only "last updated" 2022). It states the claim and cites no study.
- [CDC, *Benefits of Physical Activity*](https://www.cdc.gov/physical-activity-basics/benefits/index.html), date unknown (the page shows 4 Dec 2025 but doesn't say what that date is). It states the claim and cites no study.

### Confidence
Medium: every opened history leads to the 1953 Morris *Lancet* paper, but neither that paper nor its companion could be opened, so the root's own wording and hedges are known only from the opened retellings.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
