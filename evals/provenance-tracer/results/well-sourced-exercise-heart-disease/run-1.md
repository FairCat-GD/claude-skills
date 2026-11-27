---
case: well-sourced-exercise-heart-disease
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T19:23:18Z
cost_usd: 1.2356
duration_s: 156
turns: 32
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
- WebSearch: origin of the idea that exercise prevents heart disease history first study
- WebSearch: Jerry Morris 1953 Lancet London bus conductors drivers coronary heart disease physical activity
- WebSearch: who first discovered physical activity reduces coronary heart disease risk
- WebSearch: Paffenbarger Harvard alumni physical activity heart attack risk 1978 study
- WebSearch: physical activity reduces risk of heart disease CDC American Heart Association evidence
- WebFetch: https://www.sciencedirect.com/science/article/abs/pii/S0140673653906655
- WebFetch: https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger
- WebFetch: https://www.cdc.gov/physical-activity-basics/benefits/index.html
- WebFetch: https://www.cdc.gov/mmwr/preview/mmwrhtml/00021477.htm
- WebFetch: https://www.ahajournals.org/doi/10.1161/CIRCRESAHA.123.322121
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/S0140-6736(53)90665-5&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:707484&resultType=core&format=json
- WebFetch: https://en.wikipedia.org/wiki/Jerry_Morris
- WebFetch (error): https://web.archive.org/cdx/search/cdx?url=cdc.gov/mmwr/preview/mmwrhtml/00021477.htm&limit=1
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:"coronary heart-disease and physical activity of work" AND AUTH:"Morris JN"&resultType=core&format=json
- WebFetch: https://paulogentil.com/pdf/A%20tribute%20to%20Professor%20Jeremiah%20Morris%20-%20the%20man%20who%20invented%20the%20field%20of%20physical%20activity%20epidemiology.pdf
- WebFetch: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(53)90665-5/fulltext
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC2027542/
- WebFetch: https://europepmc.org/articles/PMC2027542/pdf
- WebFetch (error): http://www.epi.umn.edu/cvdepi/study-synopsis/london-transport-workers-study/
- WebFetch: https://api.crossref.org/works/10.1016/s0140-6736(53)90665-5
- WebFetch: https://api.crossref.org/works/10.1093/oxfordjournals.aje.a112608
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:"work activity of longshoremen" AND AUTH:"Paffenbarger"&resultType=core&format=json

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Regular exercise lowers the risk of heart disease."

**Roots:** Independent · **Grounding:** Grounded · Mutated
**Earliest instance found:** [Morris, Heady, Raffle, Roberts and Parks, *Coronary heart-disease and physical activity of work*, The Lancet](https://www.sciencedirect.com/science/article/abs/pii/S0140673653906655), 1953 (date from: cited by [BCMJ, 2007](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger); issue month November 1953 per its [Crossref record](https://api.crossref.org/works/10.1016/s0140-6736(53)90665-5)). Earlier instances may exist.
**Roots:** 2 · **Retellings found:** 9

### Chain
Your version: "Regular exercise lowers the risk of heart disease" (where you met it: not given)
 └─ [Benefits of Physical Activity, CDC](https://www.cdc.gov/physical-activity-basics/benefits/index.html), 2025, Tertiary (see *Cold trails*)
 └─ [Andrade and Ignaszewski, *Exercise and the heart: A review of the early studies*, BCMJ](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger), 2007, Secondary → cites
     ├─ [Morris et al., *Coronary heart-disease and physical activity of work*, Lancet](https://www.sciencedirect.com/science/article/abs/pii/S0140673653906655), 1953, Primary (not opened, per BCMJ 2007), root 1 (London bus drivers compared with bus conductors; publisher page returned 403, and no abstract was found in Europe PMC)
     └─ Paffenbarger et al., *Work activity of longshoremen…*, N Engl J Med 282:1109–1114, 1970, Primary (not opened, per BCMJ 2007), same team as ↓
         └─ [Paffenbarger, Wing and Hyde, *Physical activity as an index of heart attack risk in college alumni*, Am J Epidemiol](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:707484&resultType=core&format=json), 1978, Primary, root 2 (abstract opened; BCMJ credits Paffenbarger's college-alumni studies)
 └─ [Jerry Morris, Wikipedia](https://en.wikipedia.org/wiki/Jerry_Morris), date unknown, Tertiary → cites
     ├─ Morris et al., Lancet, 1953 → see root 1
     └─ [Morris and Crawford, *Coronary heart disease and physical activity of work*, BMJ](https://pmc.ncbi.nlm.nih.gov/articles/PMC2027542/), 1958, Primary (not opened, per Wikipedia; the PMC page returned only references), same team as root 1
 └─ [*Physical Activity and the Prevention of Coronary Heart Disease*, MMWR, CDC](https://www.cdc.gov/mmwr/preview/mmwrhtml/00021477.htm), date unknown (the page cites a 1993 paper), Secondary → cites
     └─ Powell, Thompson, Caspersen and Kendrick, *Physical activity and the incidence of coronary heart disease*, Annu Rev Public Health, 1987, (not opened), per MMWR → stopped: not opened

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Context removed | Root 1 compared [physically active work with sedentary work and coronary mortality in middle-aged men](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger) (it measured activity on the job, not exercise) | Regular exercise lowers the risk of heart disease | [BCMJ](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger), 2007 |
| Scope widened | Root 2 studied male Harvard alumni aged 35–74, and its outcome was a first heart attack | Regular exercise lowers the risk of heart disease | [MMWR, CDC](https://www.cdc.gov/mmwr/preview/mmwrhtml/00021477.htm), date unknown |
| Hedge dropped | In root 2's abstract, as Europe PMC returned it, adult activity *appeared* to lower risk, in a cohort that reported its own activity | Regular exercise lowers the risk of heart disease | [MMWR, CDC](https://www.cdc.gov/mmwr/preview/mmwrhtml/00021477.htm), date unknown |

### Status of the root
- Root 1 (Morris et al., 1953): the [Crossref record](https://api.crossref.org/works/10.1016/s0140-6736(53)90665-5) lists no retraction, correction or erratum. I could not open the journal page (403), and I did not check Retraction Watch or PubPeer.
- Root 2 (Paffenbarger et al., 1978): the [Crossref record](https://api.crossref.org/works/10.1093/oxfordjournals.aje.a112608) lists no retraction, correction or erratum. I did not check Retraction Watch or PubPeer.
- Later review: according to [MMWR](https://www.cdc.gov/mmwr/preview/mmwrhtml/00021477.htm), a 1987 review of 43 studies (Powell et al.) found an inverse relation between physical activity and CHD risk in about two-thirds of them. MMWR also cites a 1990 meta-analysis by Berlin and Colditz. I did not open either.

### Cold trails
- [Benefits of Physical Activity, CDC](https://www.cdc.gov/physical-activity-basics/benefits/index.html), 2025: states the claim (150 minutes a week of moderate activity) and cites no study, only a link to another CDC prevention page, which I did not follow.

### Confidence
Medium: root 2's abstract was opened and dated through Europe PMC and Crossref, but root 1, the 1953 Lancet paper that most sources credit as the origin, could not be opened, so what it says rests on the BCMJ review that cites it.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
