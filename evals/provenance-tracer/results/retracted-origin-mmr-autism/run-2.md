---
case: retracted-origin-mmr-autism
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:26:31Z
cost_usd: 1.3909
duration_s: 165
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
- WebSearch: "MMR vaccine causes autism"
- WebSearch: MMR jab linked to autism claim
- WebSearch: Wakefield 1998 Lancet ileal-lymphoid-nodular hyperplasia MMR autism
- WebSearch: origin of MMR autism claim first appeared 1998 press conference Royal Free
- WebSearch: MMR vaccine autism fact check Snopes OR Reuters OR "Full Fact"
- WebSearch: "12 children" MMR autism Lancet retraction 2010
- WebFetch: https://www.thelancet.com/pdfs/journals/lancet/PIIS0140-6736(97)11096-0.pdf
- WebFetch: https://en.wikipedia.org/wiki/H._Hugh_Fudenberg
- WebFetch: https://en.wikipedia.org/wiki/Lancet_MMR_vaccine-autism_report
- WebFetch: https://api.crossref.org/works/10.1016/S0140-6736(97)11096-0
- WebFetch: https://www.cmaj.ca/content/cmaj/182/4/E199.full.pdf
- WebFetch: https://www.poynter.org/fact-checking/2026/do-vaccines-cause-autism/
- WebFetch: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(97)11096-0/fulltext
- WebFetch: https://static1.squarespace.com/static/57698667d2b8574e2db7710a/t/591966f39de4bb3c019734fb/1494836984275/andrew-wakefiled-1998-lancet.pdf
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/8993773
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC2831678
- WebFetch: http://www.bmj.com/content/342/bmj.c7452.full
- Read (denied): <temp>/config/projects/-private-tmp-e-lQZc90-home-cwd/13ad8924-625b-4d4a-8782-5b718b4c1b90/tool-results/webfetch-1795771638838-rb2mz0.pdf
- WebFetch: https://briandeer.com/mmr/lancet-retraction.htm
- WebFetch (error): https://www.theguardian.com/society/2010/feb/02/lancet-retracts-mmr-paper
- WebFetch: https://briandeer.com/mmr/lancet-paper.htm
- WebFetch (error): https://web.archive.org/web/2010/http://www.thelancet.com/journals/lancet/article/PIIS0140-6736(97)11096-0/fulltext
- WebFetch: https://link.springer.com/article/10.1007/BF02628672
- WebSearch: Fudenberg 1996 Biotherapy "Dialysable lymphocyte extract" autism MMR cited by Wakefield Lancet
- WebFetch: https://www.unboundmedicine.com/medline/citation/8993773/Dialysable_lymphocyte_extract__DLyE__in_infantile_onset_autism:_a_pilot_study_
- WebFetch: https://briandeer.com/mmr/lancet-paper.htm
- WebFetch: https://www.nejm.org/doi/10.1056/NEJMoa021134

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "The MMR vaccine causes autism."

**Roots:** Echo · **Grounding:** Primary differs · Mutated
**Earliest instance found:** [H. H. Fudenberg, *Dialysable lymphocyte extract (DLyE) in infantile onset autism: A pilot study*, *Biotherapy*](https://link.springer.com/article/10.1007/BF02628672), 1996 (date from: cited by [Wikipedia, *H. Hugh Fudenberg*](https://en.wikipedia.org/wiki/H._Hugh_Fudenberg)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 6

### Chain
Your version: "The MMR vaccine causes autism" (where you met it: not given)
 └─ [PolitiFact / Poynter, *Decades of research show vaccines do not cause autism*](https://www.poynter.org/fact-checking/2026/do-vaccines-cause-autism/), 2026, Secondary. It says the idea "dates back to a 1998 paper in The Lancet" → cites
     └─ [Wikipedia, *Wakefield MMR-autism fraud*](https://en.wikipedia.org/wiki/Lancet_MMR_vaccine-autism_report), date unknown, Secondary. It covers the February 1998 Royal Free Hospital press conference, where Wakefield said "I can't support the continued use of these three vaccines given in combination" → cites
         ├─ Royal Free press conference and video news release, 1998, (not opened), per Wikipedia, *Wakefield MMR-autism fraud* → stopped: not opened
         └─ [A. J. Wakefield et al., *Ileal-lymphoid-nodular hyperplasia, non-specific colitis, and pervasive developmental disorder in children*, *The Lancet* 351:637–41](https://briandeer.com/mmr/lancet-paper.htm), 28 Feb 1998, Primary. I opened it through the full text reproduced at briandeer.com, because [the Lancet's own page](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(97)11096-0/fulltext) returned 403. In this paper, parents linked the onset of behavioural symptoms to MMR in 8 of the 12 children. Its Discussion sentence saying MMR "has also been implicated" carries no reference number of its own, and reference 16 (Fudenberg) follows it → cites
             └─ [Fudenberg, *Biotherapy*](https://link.springer.com/article/10.1007/BF02628672), 1996, Primary (not opened, per [Wikipedia, *H. Hugh Fudenberg*](https://en.wikipedia.org/wiki/H._Hugh_Fudenberg)). Wikipedia quotes it as saying "Fifteen of the [True Autism] patients developed symptoms within a week after immunization", and says Wakefield's paper cites it → stopped: not opened (Springer redirected to a login)

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Correlation stated as causation | Per Wikipedia, Fudenberg 1996 reports symptoms *within a week after* MMR, a timing association. Wakefield 1998 reports parents associating onset with MMR in 8 of 12 children | the vaccine *causes* autism | Wikipedia's account of Fudenberg, which says he "began claiming that the MMR vaccine causes autism" in the 1980s. It gives no dated source for that, so the first dated node in causal form was not found |
| Hedge dropped | [Wakefield 1998](https://briandeer.com/mmr/lancet-paper.htm): "We did not prove an association between measles, mumps, and rubella vaccine" | stated without qualification | Royal Free press conference, 1998 (not opened, per Wikipedia), which called for single vaccines until MMR could be ruled out |
| Scope widened | a case series of 12 referred children with bowel symptoms and developmental regression (Wakefield 1998). Wikipedia reports Fudenberg's paper as covering 15 patients | the claim now covers autism in general | your version |
| Context removed | the 1998 paper was mainly about a bowel finding (ileal lymphoid nodular hyperplasia, colitis), and the MMR timing was reported by parents | the bowel context and the parental reporting are gone | your version |

### Status of the root
- Fudenberg 1996 (root): Springer redirected to a login, PubMed and the MEDLINE mirror returned no content, and so no journal-page, Crossref, Retraction Watch or PubPeer check was completed.
- Wakefield 1998, correction: the [Crossref record](https://api.crossref.org/works/10.1016/S0140-6736(97)11096-0) lists a correction notice (DOI 10.1016/s0140-6736(04)15715-2, 6 Mar 2004; Retraction Watch record 17269). According to [Brian Deer's retraction page](https://briandeer.com/mmr/lancet-retraction.htm), 10 co-authors signed the 2004 *Retraction of an interpretation*, stating "no causal link was established between (the) vaccine and autism". Wakefield did not sign.
- Wakefield 1998, retraction: the [Crossref record](https://api.crossref.org/works/10.1016/S0140-6736(97)11096-0) lists a retraction (DOI 10.1016/s0140-6736(10)60175-4, 6 Feb 2010; Retraction Watch record 4036) and titles the paper "RETRACTED". [Wikipedia](https://en.wikipedia.org/wiki/Lancet_MMR_vaccine-autism_report) dates the editors' announcement to 2 February 2010.
- Wakefield 1998, fraud finding: Wikipedia reports that *The BMJ* published Brian Deer's investigation and an editorial in January 2011 calling the paper "an elaborate fraud". The BMJ page returned 403, so it was not opened.
- Later studies: [PolitiFact / Poynter (2026)](https://www.poynter.org/fact-checking/2026/do-vaccines-cause-autism/) reviews later studies, including a 2002 Danish cohort, a 2019 cohort of over 650,000 children, the Yokohama data and a 2014 meta-analysis. It concludes: "Credible studies have not linked vaccines to autism." I did not open the studies themselves (NEJM returned 403).

### Cold trails
None.

### Confidence
Medium: the root (Fudenberg 1996) was not opened, so its date and wording rest on Wikipedia, and the 1998 Lancet paper was read through a third-party copy because the journal's own page refused the fetch.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
