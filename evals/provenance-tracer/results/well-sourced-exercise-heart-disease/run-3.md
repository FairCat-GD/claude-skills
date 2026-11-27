---
case: well-sourced-exercise-heart-disease
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T19:23:22Z
cost_usd: 1.3590
duration_s: 186
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
- WebSearch: physical activity reduces coronary heart disease risk history first study
- WebSearch: Jerry Morris 1953 London bus drivers conductors coronary heart disease Lancet
- WebSearch: "30 to 50 percent" lower risk heart disease physically active
- WebSearch: origin of the idea that exercise prevents heart disease
- WebSearch: exercise prevents heart disease fact check
- WebFetch: https://www.sciencedirect.com/science/article/abs/pii/S0140673653906655
- WebFetch: https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger
- WebFetch: https://www.nhlbi.nih.gov/health/heart/physical-activity/benefits
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/12458972/
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:"coronary heart-disease and physical activity of work"&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:"work activity of longshoremen"&resultType=core&format=json
- WebFetch: https://travelwest.info/essential-evidence/138-the-legacy-of-jerry-morris-research-on-physical-activity/
- WebFetch: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(53)90665-5/fulltext
- WebFetch: https://www.nejm.org/doi/full/10.1056/NEJM197005142822001
- WebFetch: https://api.crossref.org/works/10.1016/s0140-6736(53)90665-5
- WebSearch: Morris Heady Raffle 1953 "physical activity of work" full text pdf conductors drivers "physically active work"
- WebFetch: https://www.studocu.com/en-us/document/purdue-university/history-internship/london-bus-study-1953-lancet/104106608
- WebFetch (error): http://www.epi.umn.edu/cvdepi/document/coronary-heart-disease-and-physical-activity-of-work/
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:"vigorous exercise in leisure-time" AND AUTH:"Morris JN"&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:"physical activity as an index of heart attack risk in college alumni"&resultType=core&format=json
- WebFetch: https://www.cdc.gov/physical-activity-basics/benefits/index.html
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:"physique of London busmen"&resultType=core&format=json
- WebFetch: https://api.crossref.org/works/10.1093/oxfordjournals.aje.a112608

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Regular exercise lowers the risk of heart disease."

**Roots:** Independent · **Grounding:** Grounded · Mutated
**Earliest instance found:** [Morris, Heady, Raffle, Roberts & Parks, *Coronary heart-disease and physical activity of work*, The Lancet 262(6795):1053–1057](https://www.sciencedirect.com/science/article/abs/pii/S0140673653906655), 1953 (date from: cited by [BCMJ, 2007](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger), and the [Crossref record](https://api.crossref.org/works/10.1016/s0140-6736(53)90665-5)). Earlier instances may exist.
**Roots:** 2 · **Retellings found:** 8

### Chain
Your version: "Regular exercise lowers the risk of heart disease" (where you met it: not given)
 ├─ [NHLBI, *Physical Activity and Your Heart: Benefits*](https://www.nhlbi.nih.gov/health/heart/physical-activity/benefits), date unknown, Tertiary (cold trail, see below)
 ├─ [CDC, *Benefits of Physical Activity*](https://www.cdc.gov/physical-activity-basics/benefits/index.html), 2025, Tertiary (cold trail, see below)
 ├─ [Travelwest, *The legacy of Jerry Morris' research on physical activity*](https://travelwest.info/essential-evidence/138-the-legacy-of-jerry-morris-research-on-physical-activity/), 2015, Secondary → cites
 │   └─ Morris et al., *Lancet*, 1953 (root 1, below)
 └─ [Andrade & Ignaszewski, *Exercise and the heart: A review of the early studies*, BCMJ 49(10)](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger), 2007, Secondary → cites
     ├─ [Morris et al., *Coronary heart-disease and physical activity of work*, Lancet](https://www.sciencedirect.com/science/article/abs/pii/S0140673653906655), 1953, Primary (not opened, per BCMJ 2007), root 1 → stopped: not opened (copies also tried: [The Lancet](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(53)90665-5/fulltext), [Studocu](https://www.studocu.com/en-us/document/purdue-university/history-internship/london-bus-study-1953-lancet/104106608), [Europe PMC, no abstract](<https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:"coronary heart-disease and physical activity of work"&resultType=core&format=json>))
     ├─ [Morris, Everitt, Pollard et al., *Vigorous exercise in leisure-time: protection against coronary heart disease*, Lancet 2:1207–1210](<https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:"vigorous exercise in leisure-time" AND AUTH:"Morris JN"&resultType=core&format=json>), 1980, Primary (same team as root 1, abstract opened)
     ├─ [Paffenbarger, Laughlin, Gima & Black, *Work activity of longshoremen…*, NEJM 282:1109–1114](https://www.nejm.org/doi/full/10.1056/NEJM197005142822001), 1970, Primary (not opened, per BCMJ 2007), same team as root 2 → stopped: not opened
     └─ [Paffenbarger, Wing & Hyde, *Physical activity as an index of heart attack risk in college alumni*, Am J Epidemiol 108:161–175](<https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:"physical activity as an index of heart attack risk in college alumni"&resultType=core&format=json>), 1978, Primary, root 2

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | Root 1: male London transport workers, with conductors compared to drivers; root 2: about 17,000 male Harvard alumni aged 35–74 | Regular exercise lowers the risk of heart disease | [BCMJ](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger), 2007 |
| Context removed (condition dropped) | Root 1 measured *physically active work* on the job. Morris's own 1980 follow-up was about *vigorous* leisure exercise, not exercise of any kind | Regular exercise lowers the risk of heart disease | [NHLBI](https://www.nhlbi.nih.gov/health/heart/physical-activity/benefits), date unknown |
| Hedge dropped | Morris 1980: "vigorous exercise is a natural defence of the body", which the authors frame as something that *may* protect the ageing heart | Regular exercise lowers the risk of heart disease | [BCMJ](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger), 2007 |

### Status of the root
- Root 1, Morris et al. 1953: no retraction, correction or erratum appears on its [Crossref record](https://api.crossref.org/works/10.1016/s0140-6736(53)90665-5). The publisher's page and the full text could not be opened (HTTP 403), and Retraction Watch and PubPeer were not checked.
- Root 1: the same team published [*Physique of London busmen; epidemiology of uniforms*](<https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:"physique of London busmen"&resultType=core&format=json>) (Lancet, 1956), indexed under body build and coronary disease. Its record has no abstract, so its finding is not reported here.
- Root 1: the team's later civil-servant cohort ([Lancet, 1980](<https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:"vigorous exercise in leisure-time" AND AUTH:"Morris JN"&resultType=core&format=json>)) found that men reporting vigorous sport or fitness activity had about half the coronary incidence of inactive men over about 8.5 years.
- Root 2, Paffenbarger et al. 1978: no retraction, correction or erratum appears on its [Crossref record](https://api.crossref.org/works/10.1093/oxfordjournals.aje.a112608). Its abstract reports that the risk of a first heart attack was "related inversely to energy expenditure" ([Europe PMC](<https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:"physical activity as an index of heart attack risk in college alumni"&resultType=core&format=json>)). Men expending under 2,000 kcal a week had 64% higher risk. Retraction Watch and PubPeer were not checked.

### Cold trails
- [NHLBI, *Physical Activity and Your Heart: Benefits*](https://www.nhlbi.nih.gov/health/heart/physical-activity/benefits), date unknown (the page gives only a last-updated date, 2022): states the claim and names no study.
- [CDC, *Benefits of Physical Activity*](https://www.cdc.gov/physical-activity-basics/benefits/index.html), 2025: states the claim and cites no study for it.

### Confidence
Medium: the opened Primaries (Morris 1980, Paffenbarger 1978) were read as abstracts on Europe PMC, but the 1953 Morris paper that starts root 1 could not be opened in any copy, and its date rests on citations and its Crossref record.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
