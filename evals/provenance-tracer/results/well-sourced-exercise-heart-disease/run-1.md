---
case: well-sourced-exercise-heart-disease
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:31:47Z
cost_usd: 1.3214
duration_s: 144
turns: 30
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
- WebSearch: origin of idea that exercise prevents heart disease earliest study
- WebSearch: Paffenbarger Harvard alumni physical activity heart attack 1978
- WebSearch: exercise heart disease claim fact check
- WebFetch: https://www.nhlbi.nih.gov/health/heart/physical-activity/benefits
- WebFetch: https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger
- WebFetch: https://www.sciencedirect.com/science/article/abs/pii/S0140673653906655
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/11689543/
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/707484/
- WebFetch: https://api.crossref.org/works/10.1016/S0140-6736(53)90665-5
- WebFetch: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(53)90665-5/fulltext
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC3022443/
- WebFetch: https://paulogentil.com/pdf/A%20tribute%20to%20Professor%20Jeremiah%20Morris%20-%20the%20man%20who%20invented%20the%20field%20of%20physical%20activity%20epidemiology.pdf
- WebFetch: https://www.harvardmagazine.com/2004/03/exercise-a-changing-pres-html
- WebSearch: "Coronary heart-disease and physical activity of work" Morris 1953 summary hypothesis conductors "less coronary heart-disease"
- WebFetch (error): http://www.epi.umn.edu/cvdepi/study-synopsis/london-transport-workers-study/
- WebFetch: https://pubpeer.com/search?q=10.1016/S0140-6736(53)90665-5
- WebSearch: "Coronary heart-disease and physical activity of work" retraction
- WebFetch: https://academic.oup.com/aje/article-abstract/108/3/161/105958
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:13110049%20AND%20SRC:MED&resultType=core&format=json

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Regular exercise lowers the risk of heart disease."

**Roots:** Independent · **Grounding:** Grounded · Mutated
**Earliest instance found:** [Morris, Heady, Raffle, Roberts & Parks, *Coronary heart-disease and physical activity of work*, *The Lancet*](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(53)90665-5/fulltext), 1953 (date from: cited by [BCMJ, 2007](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger) and the [Crossref record](https://api.crossref.org/works/10.1016/S0140-6736(53)90665-5), November 1953). Earlier instances may exist.
**Roots:** 2 · **Retellings found:** 6

### Chain
Your version: "Regular exercise lowers the risk of heart disease" (where you met it: not given)
 ├─ [NHLBI, *Physical Activity and Your Heart: Benefits*](https://www.nhlbi.nih.gov/health/heart/physical-activity/benefits), date unknown (the page shows only "last updated" 2022), Tertiary. It says regular aerobic activity "can lower your risk for coronary heart disease" and cites nothing → cold trail
 ├─ [Harvard Magazine, *Exercise: A Changing Prescription*](https://www.harvardmagazine.com/2004/03/exercise-a-changing-pres-html), 2004 (byline), Secondary. It calls Morris's bus study "the first formal epidemiologic study linking activity to better health" → cites
 │   └─ Morris et al., *Lancet*, 1953 (see below)
 ├─ [Lee, Matthews & Blair, *The Legacy of Dr. Ralph Seal Paffenbarger, Jr.*](https://pmc.ncbi.nlm.nih.gov/articles/PMC3022443/), 2009 (byline), Secondary → cites Morris 1953 and Paffenbarger 1978 (below)
 └─ [Andrade & Ignaszewski, *Exercise and the heart: A review of the early studies*, BCMJ](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger), 2007 (byline), Secondary. It says Morris's and Paffenbarger's studies were the first to link activity and exercise to lower heart-disease risk → cites
     ├─ [Morris JN et al., *Coronary heart-disease and physical activity of work*, *Lancet* 262:1053–1057 and 1111–1120](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(53)90665-5/fulltext), 1953, Primary (not opened, per BCMJ 2007; the Lancet and [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0140673653906655) both returned 403) → stopped: not opened
     └─ [Paffenbarger, Wing & Hyde, *Physical activity as an index of heart attack risk in college alumni*, *Am J Epidemiol* 108:161–175](https://academic.oup.com/aje/article-abstract/108/3/161/105958), 1978 (byline), Primary (abstract opened). It reports: "Risk of first heart attack was found to be related Inversely to energy expenditure."

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | Paffenbarger 1978: first heart attacks among 16,936 male Harvard alumni. Morris 1953: male London transport workers, per BCMJ | "heart disease," with no population named | [NHLBI](https://www.nhlbi.nih.gov/health/heart/physical-activity/benefits), date unknown |
| Correlation stated as causation | Paffenbarger 1978: in an observational cohort, activity was linked to lower risk, independent of the other influences measured | "lowers the risk" | [NHLBI](https://www.nhlbi.nih.gov/health/heart/physical-activity/benefits), date unknown ("can lower your risk") |
| Other: on-the-job activity retold as exercise | Morris 1953 compared physically active work (conductors) with sedentary work (drivers), per BCMJ | "regular exercise" | [BCMJ](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger), 2007, which groups the work-activity and leisure-exercise studies together |

### Status of the root
- Morris 1953: the [Crossref record](https://api.crossref.org/works/10.1016/S0140-6736(53)90665-5) and the [Europe PMC record](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:13110049%20AND%20SRC:MED&resultType=core&format=json) list no retraction, correction or expression of concern. The [PubPeer search](https://pubpeer.com/search?q=10.1016/S0140-6736(53)90665-5) returned no readable results. I searched for Retraction Watch entries but did not open its database directly.
- Morris 1953: [Harvard Magazine (2004)](https://www.harvardmagazine.com/2004/03/exercise-a-changing-pres-html) reports that critics at the time argued the conductors' lower blood pressure and body weight could explain the difference. I did not open the follow-up papers, such as Morris's 1956 paper on busmen's uniform sizes.
- Paffenbarger 1978: the [journal page](https://academic.oup.com/aje/article-abstract/108/3/161/105958) shows no correction or erratum.

### Cold trails
- [NHLBI, *Physical Activity and Your Heart: Benefits*](https://www.nhlbi.nih.gov/health/heart/physical-activity/benefits), date unknown: states the claim, cites nothing.

### Confidence
Medium: the Morris 1953 paper was paywalled and not opened, and Paffenbarger 1978 was opened only as its abstract, so I could not check whether it cites Morris; if it does, the two roots would be one chain rather than independent origins.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
