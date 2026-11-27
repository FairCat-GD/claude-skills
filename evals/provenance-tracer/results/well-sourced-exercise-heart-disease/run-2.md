---
case: well-sourced-exercise-heart-disease
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:31:54Z
cost_usd: 1.2517
duration_s: 161
turns: 31
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
- WebSearch: physical activity reduces risk of coronary heart disease
- WebSearch: Jerry Morris 1953 Lancet London bus conductors drivers coronary heart disease
- WebSearch: origin of idea that exercise prevents heart disease history first study
- WebSearch: who first showed exercise protects against heart disease
- WebSearch: exercise heart disease risk fact check myth
- WebFetch: https://www.nhlbi.nih.gov/health/heart/physical-activity/benefits
- WebFetch: https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger
- WebFetch: https://www.sciencedirect.com/science/article/abs/pii/S0140673653906655
- WebFetch (error): http://www.epi.umn.edu/cvdepi/essay/jeremy-morris-on-physical-activity-and-coronary-disease/
- WebFetch: https://www.cdc.gov/Mmwr/preview/mmwrhtml/00021477.htm
- WebSearch: Morris Heady Raffle "Coronary heart-disease and physical activity of work" pubmed
- WebFetch: https://academic.oup.com/ije/article-abstract/30/5/1184/724212
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/13110049/
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/13110075/
- WebFetch: https://api.crossref.org/works/10.1016/s0140-6736(53)90665-5
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC1024515/
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:13110049&resultType=core&format=json
- WebFetch: https://doi.org/10.7326/0003-4819-41-5-910
- WebFetch: https://www.heartfoundation.org.au/healthy-living/physical-activity/physical-activity-and-exercise
- WebFetch: https://www.acpjournals.org/doi/10.7326/0003-4819-41-5-910
- WebFetch: https://www.annualreviews.org/doi/10.1146/annurev.pu.08.050187.001345
- WebFetch: https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Regular exercise lowers the risk of heart disease."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** Morris, Heady, Raffle, Roberts & Parks, *Coronary heart-disease and physical activity of work*, The Lancet, 1953 (date from: cited by [Andrade & Ignaszewski, BCMJ 2007](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger), and the [Crossref record](https://api.crossref.org/works/10.1016/s0140-6736(53)90665-5)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 7

### Chain
Your version: "Regular exercise lowers the risk of heart disease" (where you met it: not given)
 ├─ [NHLBI, *Physical Activity and Your Heart: Benefits*](https://www.nhlbi.nih.gov/health/heart/physical-activity/benefits), date unknown (last updated 2022), Tertiary → cites nothing (cold trail)
 ├─ [Heart Foundation (Australia), *Physical activity and exercise*](https://www.heartfoundation.org.au/healthy-living/physical-activity/physical-activity-and-exercise), date unknown (last updated 2025), Tertiary → cites nothing (cold trail)
 ├─ [CDC MMWR, *Public Health Focus: Physical Activity and the Prevention of Coronary Heart Disease*](https://www.cdc.gov/Mmwr/preview/mmwrhtml/00021477.htm), date unknown, Secondary → cites
 │   └─ [Powell, Thompson, Caspersen & Kendrick, *Physical activity and the incidence of coronary heart disease*, Annu Rev Public Health](https://www.annualreviews.org/doi/10.1146/annurev.pu.08.050187.001345), 1987, (not opened), per CDC MMWR → stopped: not opened
 ├─ [Paffenbarger, Blair & Lee, *A history of physical activity, cardiovascular health and longevity*, Int J Epidemiol](https://academic.oup.com/ije/article-abstract/30/5/1184/724212), 2001 (abstract only), Secondary → cites
 │   └─ Morris et al., London busmen studies, (not opened), per Int J Epidemiol 2001 → same root as below
 └─ [Andrade & Ignaszewski, *Exercise and the heart: A review of the early studies*, BCMJ](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger), 2007, Secondary → cites
     └─ [Morris et al., *Coronary heart-disease and physical activity of work*, The Lancet 262:1053–57 and 1111–20](https://www.sciencedirect.com/science/article/abs/pii/S0140673653906655), 1953, Primary (not opened, per BCMJ 2007): fetch returned 403. [PubMed](https://pubmed.ncbi.nlm.nih.gov/13110049/) also returned only a cookie wall, and [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:13110049&resultType=core&format=json) lists no abstract and no open full text.

BCMJ 2007 and Int J Epidemiol 2001 both name the 1953 bus study as where this idea started as an epidemiological finding. BCMJ says Morris's London busmen studies and Paffenbarger's longshoremen and college-alumni studies were "the first to link physical activity and exercise to a lower risk of heart disease." In that study, conductors climbing the stairs of double-decker buses had less coronary heart disease than the drivers, who sat for their whole shift. BCMJ states Morris's hypothesis as: "men doing physically active work have a lower mortality from coronary heart disease". Int J Epidemiol calls the result "an apparent protection against CHD enjoyed by active conductors".

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | middle-aged male London bus workers (also postmen), per BCMJ 2007 | everyone ("regular exercise", heart disease in general) | [NHLBI](https://www.nhlbi.nih.gov/health/heart/physical-activity/benefits), date unknown (earliest opened node that states it generally: [CDC MMWR](https://www.cdc.gov/Mmwr/preview/mmwrhtml/00021477.htm), date unknown) |
| Other: physical activity at work became leisure exercise | activity done as part of the job (conductors vs drivers) | "regular exercise" | Morris et al., *Vigorous exercise in leisure-time and the incidence of coronary heart-disease*, Lancet 1973 (not opened, per BCMJ 2007) |
| Correlation stated as causation | an observed difference between two groups of workers, which Int J Epidemiol 2001 calls "apparent" protection | "lowers the risk" | [CDC MMWR](https://www.cdc.gov/Mmwr/preview/mmwrhtml/00021477.htm), date unknown: a review of 43 studies "concluded that moderate to vigorous physical activity reduces risk for CHD", citing Powell 1987 |

### Status of the root
- No correction, retraction or expression of concern is listed in the [Crossref record for part 1](https://api.crossref.org/works/10.1016/s0140-6736(53)90665-5). Its update and relation fields are empty. The journal page and PubPeer were not reached, and Retraction Watch was not checked.
- Morris's team's 1956 study of uniform sizes, per [BCMJ 2007](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger): after adjusting for height and weight, drivers had larger chests and waists than conductors, even in the youngest age group. The authors read this as a difference that existed before the job (a possible confounder).
- Morris et al.'s 1966 follow-up of 667 busmen, per [BCMJ 2007](https://bcmj.org/articles/exercise-and-heart-review-early-studies-memory-dr-rs-paffenbarger): drivers still had more heart disease than conductors at the same blood pressure (8.5 vs 4.7 per 100 men over five years).
- Later reviews named in opened pages: Powell et al. 1987 (43 epidemiologic studies) and Berlin & Colditz 1990 (a meta-analysis), both per [CDC MMWR](https://www.cdc.gov/Mmwr/preview/mmwrhtml/00021477.htm), neither opened. The MMWR gives the risk for physically inactive people as a relative risk of 1.9 (95% CI 1.4–2.5).

### Cold trails
- [NHLBI, *Physical Activity and Your Heart: Benefits*](https://www.nhlbi.nih.gov/health/heart/physical-activity/benefits), date unknown: states the claim and cites no study.
- [Heart Foundation (Australia)](https://www.heartfoundation.org.au/healthy-living/physical-activity/physical-activity-and-exercise), date unknown: says "you can cut your risk of heart disease by a third", with no source for the figure.

### Confidence
Medium: every chain leads to Morris et al. 1953, but that Primary could not be opened (403, cookie wall, no open full text), so what it says comes from the opened secondaries that cite it.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
