---
case: well-sourced-exercise-heart-disease
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:31:27Z
cost_usd: 1.6071
duration_s: 215
turns: 34
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
- WebSearch: origin of idea that exercise prevents heart disease history first study
- WebSearch: Jerry Morris 1953 Lancet bus conductors drivers coronary heart disease physical activity of work
- WebSearch: Paffenbarger longshoremen Harvard alumni physical activity heart attack risk history
- WebSearch: physical activity reduces coronary heart disease risk who first discovered earliest evidence
- WebSearch: exercise heart disease claim fact check meta-analysis physical activity cardiovascular risk reduction percent
- WebFetch: https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger
- WebFetch: https://www.nhlbi.nih.gov/health/heart/physical-activity/benefits
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22coronary%20heart-disease%20and%20physical%20activity%20of%20work%22&resultType=core&format=json
- WebFetch: https://academic.oup.com/ije/article/30/5/1184/724212
- WebFetch: https://www.sciencedirect.com/science/article/abs/pii/S0140673653906655
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22work%20activity%20of%20longshoremen%22&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22physical%20activity%20as%20an%20index%20of%20heart%20attack%20risk%22&resultType=core&format=json
- WebFetch: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(53)90665-5/fulltext
- WebFetch (error): http://www.epi.umn.edu/cvdepi/study-synopsis/london-transport-workers-study/
- WebSearch: "Men in physically active jobs have a lower incidence of coronary heart-disease" Morris 1953
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC1024515/?page=0
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=AUTH:%22Morris%20JN%22%20AND%20TITLE:%22mortality%20in%20relation%20to%20the%20physical%20activity%20of%20work%22&resultType=core&format=json
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC1037497/
- WebFetch: https://europepmc.org/backend/ptpmcrender.fcgi?accid=PMC1037497&blobtype=pdf
- WebFetch: https://api.crossref.org/works/10.1093/oxfordjournals.aje.a112608
- WebFetch: https://api.crossref.org/works/10.1016/s0140-6736(53)90665-5
- WebSearch: "Physical activity as an index of heart attack risk in college alumni" retraction OR reanalysis OR replication
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/18525377/
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:18525377&resultType=core&format=json
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC6527136/

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Regular exercise lowers the risk of heart disease"

**Roots:** Independent · **Grounding:** Grounded · Mutated
**Earliest instance found:** [Morris, Heady, Raffle, Roberts & Parks, *Coronary heart-disease and physical activity of work*, The Lancet](https://www.sciencedirect.com/science/article/abs/pii/S0140673653906655), 1953 (date from: cited by [BCMJ 2007](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger) and the [Crossref record](https://api.crossref.org/works/10.1016/s0140-6736(53)90665-5)). Earlier instances may exist.
**Roots:** 2 · **Retellings found:** 6

### Chain
Your version: "Regular exercise lowers the risk of heart disease" (where you met it: not given)
 ├─ [Andrade & Ignaszewski, *Exercise and the heart: A review of the early studies*, BCMJ](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger), 2007, Secondary → cites
 │   ├─ [Morris et al., *Coronary heart-disease and physical activity of work*, The Lancet](https://www.sciencedirect.com/science/article/abs/pii/S0140673653906655), 1953, Primary (not opened, per BCMJ 2007), root 1
 │   ├─ [Paffenbarger, Laughlin, Gima & Black, *Work activity of longshoremen…*, NEJM](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22work%20activity%20of%20longshoremen%22&resultType=core&format=json), 1970, Primary (not opened, per BCMJ 2007), same team as root 2
 │   └─ [Paffenbarger, Wing & Hyde, *Physical activity as an index of heart attack risk in college alumni*, Am J Epidemiol](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22physical%20activity%20as%20an%20index%20of%20heart%20attack%20risk%22&resultType=core&format=json), 1978, Primary, root 2
 └─ [Paffenbarger, Blair & Lee, *A history of physical activity, cardiovascular health and longevity: the scientific contributions of Jeremy N Morris*, Int J Epidemiol](https://academic.oup.com/ije/article/30/5/1184/724212), 2001, Secondary → cites
     └─ Morris et al., 1953 (root 1, above)

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | Root 2: in 16,936 male Harvard alumni aged 35–74, the risk of a first heart attack fell as reported weekly energy expenditure rose ([abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22physical%20activity%20as%20an%20index%20of%20heart%20attack%20risk%22&resultType=core&format=json)) | Regular exercise lowers the risk of heart disease | [BCMJ](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger), 2007 |
| Other: *activity at work* became *exercise* | Root 1, per BCMJ 2007 and IJE 2001: Morris compared physically active jobs (bus conductors, postmen) with sedentary ones (drivers, office workers). It measured activity at work, not exercise. | Regular exercise lowers the risk of heart disease | [BCMJ](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger), 2007 |

### Status of the root
- Morris et al. 1953 (root 1): the [Crossref record](https://api.crossref.org/works/10.1016/s0140-6736(53)90665-5) shows no retraction, correction or expression of concern. The paper itself could not be opened: ScienceDirect and The Lancet both returned 403. Retraction Watch and PubPeer were not checked.
- Paffenbarger, Wing & Hyde 1978 (root 2): the [Crossref record](https://api.crossref.org/works/10.1093/oxfordjournals.aje.a112608) shows no retraction, correction or expression of concern. The [Europe PMC listing](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22physical%20activity%20as%20an%20index%20of%20heart%20attack%20risk%22&resultType=core&format=json) also shows a 1995 reprint in the same journal. Retraction Watch and PubPeer were not checked.
- Morris's team, later work: their 1990 study of leisure-time exercise in [Br Heart J](https://pmc.ncbi.nlm.nih.gov/articles/PMC1024515/?page=0) says the men who took vigorous exercise were a favourably selected group.
- Morris's team, companion paper: [Morris & Heady, *Mortality in relation to the physical activity of work: a preliminary note*, Br J Ind Med](https://pmc.ncbi.nlm.nih.gov/articles/PMC1037497/), October 1953. Its text is posted only as page images, so it could not be read.
- Major later review: [Kraus et al., for the 2018 Physical Activity Guidelines Advisory Committee, Med Sci Sports Exerc](https://pmc.ncbi.nlm.nih.gov/articles/PMC6527136/), 2019. It reports a 14% lower coronary heart disease risk at the guideline minimum and adds, "The evidence for these conclusions was considered strong by the Committee."
- Background: the [IJE 2001 history](https://academic.oup.com/ije/article/30/5/1184/724212) traces general advice that exercise is good for health back to Hippocrates. That advice does not concern heart disease, and no retelling credits it as the claim's source.

### Cold trails
- [NHLBI, *Physical Activity and Your Heart – Benefits*](https://www.nhlbi.nih.gov/health/heart/physical-activity/benefits), date unknown (the page gives only a 2022 last-updated date). It states the claim and cites nothing.

### Confidence
Medium: root 2 was opened only as its abstract record, and root 1 (Morris 1953) could not be opened, so its finding rests on the reviews that describe it.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
