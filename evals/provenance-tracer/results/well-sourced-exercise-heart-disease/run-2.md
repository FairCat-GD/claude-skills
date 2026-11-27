---
case: well-sourced-exercise-heart-disease
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T19:23:20Z
cost_usd: 1.1760
duration_s: 147
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
- WebSearch: "regular exercise lowers the risk of heart disease"
- WebSearch: physical activity reduces coronary heart disease risk origin of idea first study
- WebSearch: Jerry Morris 1953 London bus conductors drivers coronary heart disease Lancet
- WebSearch: who first discovered exercise prevents heart disease history
- WebSearch: Paffenbarger longshoremen Harvard alumni physical activity heart attack study
- WebSearch: exercise heart disease risk fact check 30 percent lower
- WebFetch: https://www.nhlbi.nih.gov/health/heart/physical-activity/benefits
- WebFetch: https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger
- WebFetch: https://www.sciencedirect.com/science/article/abs/pii/S0140673653906655
- WebFetch: https://academic.oup.com/ije/article/30/5/1184/724212
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/S0140-6736(53)90665-5&resultType=core&format=json
- WebFetch: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(53)90665-5/fulltext
- WebFetch: https://www.cdc.gov/physical-activity-basics/benefits/index.html
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22coronary%20heart-disease%20and%20physical%20activity%20of%20work%22&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22physical%20activity%20as%20an%20index%20of%20heart%20attack%20risk%20in%20college%20alumni%22&resultType=core&format=json
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/13110049/
- WebFetch: https://api.crossref.org/works/10.1093/oxfordjournals.aje.a112608
- WebFetch: https://api.crossref.org/works/10.1016/s0140-6736(53)90665-5
- WebFetch (error): http://www.epi.umn.edu/cvdepi/study-synopsis/london-transport-workers-study/

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Regular exercise lowers the risk of heart disease."

**Roots:** Independent · **Grounding:** Grounded · Mutated
**Earliest instance found:** [Morris, Heady, Raffle, Roberts & Parks, *Coronary heart-disease and physical activity of work*, The Lancet](https://www.sciencedirect.com/science/article/abs/pii/S0140673653906655), 1953 (date from: cited by the [BCMJ review](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger) and the [Europe PMC record](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22coronary%20heart-disease%20and%20physical%20activity%20of%20work%22&resultType=core&format=json)). Earlier instances may exist.
**Roots:** 2 · **Retellings found:** 7

### Chain
Your version: "Regular exercise lowers the risk of heart disease" (where you met it: not given)
 ├─ [Andrade & Ignaszewski, *Exercise and the heart: A review of the early studies*, BCMJ](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger), 2007, Secondary → cites
 │   ├─ [Morris et al., *Coronary heart-disease and physical activity of work*, The Lancet](https://www.sciencedirect.com/science/article/abs/pii/S0140673653906655), 1953, Primary (not opened, per BCMJ), root 1
 │   ├─ Paffenbarger, Laughlin, Gima & Black, *Work activity of longshoremen as related to death from coronary heart disease and stroke*, NEJM, 1970, (not opened), per BCMJ (by the same team as the 1978 study, so part of root 2)
 │   └─ [Paffenbarger, Wing & Hyde, *Physical activity as an index of heart attack risk in college alumni*, Am J Epidemiol](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22physical%20activity%20as%20an%20index%20of%20heart%20attack%20risk%20in%20college%20alumni%22&resultType=core&format=json), 1978, Primary, root 2
 └─ [Paffenbarger, Blair & Lee, *A history of physical activity, cardiovascular health and longevity*, Int J Epidemiol](https://academic.oup.com/ije/article/30/5/1184/724212), 2001, Secondary → cites
     └─ Morris et al., 1953 (root 1, above)

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | Among 16,936 male Harvard alumni aged 35–74, the risk of a first heart attack fell as weekly energy spent on activity rose. The 1953 root, as BCMJ describes it, was about physically active work among London transport workers, not about exercise in general. | Regular exercise lowers the risk of heart disease | [BCMJ](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger), 2007 |

### Status of the root
- Morris et al. 1953: the [Crossref record](https://api.crossref.org/works/10.1016/s0140-6736(53)90665-5) shows no retraction, correction or expression of concern. The Lancet and ScienceDirect pages returned 403 errors. Retraction Watch and PubPeer were not checked.
- Morris et al. 1953: the [BCMJ review](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger) reports two follow-ups by the same team. A 1956 study of uniform sizes found that drivers were already larger than conductors, even among the youngest men, which suggests the difference existed before the job. A 1966 follow-up found that the effect of work activity held among men with the same blood pressure. The review also reports that the 1953 idea first met considerable skepticism from medical scientists.
- Paffenbarger et al. 1978: the [Crossref record](https://api.crossref.org/works/10.1093/oxfordjournals.aje.a112608) shows no retraction, correction or expression of concern. Retraction Watch and PubPeer were not checked.
- Paffenbarger et al. 1978: according to the [Europe PMC record](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22physical%20activity%20as%20an%20index%20of%20heart%20attack%20risk%20in%20college%20alumni%22&resultType=core&format=json), the *American Journal of Epidemiology* reprinted the paper in 1995, with an accompanying discussion.

### Cold trails
- [NHLBI, *Physical Activity and Your Heart: Benefits*](https://www.nhlbi.nih.gov/health/heart/physical-activity/benefits), date unknown (the page gives only a last-updated date, 2022). It states the claim and cites no source.
- [CDC, *Benefits of Physical Activity*](https://www.cdc.gov/physical-activity-basics/benefits/index.html), date unknown (the page gives only a last-reviewed date, 2025). It states the claim and cites no specific study.

### Confidence
Medium: I opened the Paffenbarger 1978 abstract, but no copy of Morris's 1953 paper would open (403 errors, and no abstract in the Europe PMC or PubMed records), so that root rests on how later pages describe it.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
