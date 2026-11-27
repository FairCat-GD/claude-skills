---
case: retracted-origin-mmr-autism
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:26:25Z
cost_usd: 1.4201
duration_s: 246
turns: 36
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
- WebSearch: measles mumps rubella vaccine autism link claim
- WebSearch: Wakefield 1998 Lancet ileal-lymphoid-nodular hyperplasia MMR autism
- WebSearch: origin of MMR autism claim first appeared
- WebSearch: MMR vaccine autism fact check
- WebSearch: Brian Deer MMR Wakefield investigation BMJ 2011 how the case was fixed
- WebFetch: https://www.thelancet.com/pdfs/journals/lancet/PIIS0140-6736(97)11096-0.pdf
- WebFetch: https://en.wikipedia.org/wiki/MMR_vaccine_and_autism
- WebFetch: https://en.wikipedia.org/wiki/H._Hugh_Fudenberg
- WebFetch: https://theconversation.com/mondays-medical-myth-the-mmr-vaccine-causes-autism-3739
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC3136032
- WebFetch: https://static1.squarespace.com/static/57698667d2b8574e2db7710a/t/591966f39de4bb3c019734fb/1494836984275/andrew-wakefiled-1998-lancet.pdf
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/9500320/
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/8993773/
- WebFetch: http://briandeer.com/wakefield/royal-video.htm
- WebFetch: https://www.bmj.com/content/342/bmj.c5347
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320%20AND%20SRC:MED&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:8993773%20AND%20SRC:MED&resultType=core&format=json
- WebFetch: https://briandeer.com/solved/bmj-wakefield-1-1.htm
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:8993773%20AND%20SRC:MED&resultType=core&format=json
- WebFetch: https://api.crossref.org/works/10.1016/S0140-6736(10)60175-4
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/S0140-6736(04)15715-2&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:30831578%20AND%20SRC:MED&resultType=core&format=json
- WebFetch: https://www.gavi.org/vaccineswork/can-mmr-vaccines-cause-autism
- WebFetch: https://api.crossref.org/works/10.1016/S0140-6736(04)15715-2
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:10376617%20AND%20SRC:MED&resultType=core&format=json
- WebFetch: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(97)11096-0/fulltext
- WebFetch: https://api.crossref.org/works/10.1007/BF02628672

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "The MMR vaccine causes autism."

**Roots:** Echo · **Grounding:** Primary differs · Mutated
**Earliest instance found:** [Fudenberg, *Dialysable lymphocyte extract (DLyE) in infantile onset autism: A pilot study*, *Biotherapy*, 1996](https://api.crossref.org/works/10.1007/BF02628672) (date from: byline in the Crossref record; that the paper's text links symptom onset to MMR comes from [Wikipedia](https://en.wikipedia.org/wiki/H._Hugh_Fudenberg), because the abstract I opened doesn't mention MMR). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 9

### Chain
Your version: "The MMR vaccine causes autism" (where you met it: not given)
 ├─ [Gavi, *Can MMR vaccines cause autism?*](https://www.gavi.org/vaccineswork/can-mmr-vaccines-cause-autism), 2025, Secondary → cites
 │   └─ [Wakefield et al., *Ileal-lymphoid-nodular hyperplasia, non-specific colitis, and pervasive developmental disorder in children*, *The Lancet*, 1998](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320%20AND%20SRC:MED&resultType=core&format=json), Primary (opened through its abstract record; [the full text](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(97)11096-0/fulltext) returned 403) → cites
 │       └─ [Fudenberg, *Biotherapy*, 1996](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:8993773%20AND%20SRC:MED&resultType=core&format=json), Primary (not opened, per [Wikipedia, *H. Hugh Fudenberg*](https://en.wikipedia.org/wiki/H._Hugh_Fudenberg)): I opened only the abstract, which doesn't mention MMR, so the passage on MMR is unseen → stopped: not opened
 ├─ [Dunlop, *Monday's medical myth: the MMR vaccine causes autism*, The Conversation](https://theconversation.com/mondays-medical-myth-the-mmr-vaccine-causes-autism-3739), 2011, Secondary → cites
 │   ├─ [Brian Deer's account of the Royal Free press conference and video](http://briandeer.com/wakefield/royal-video.htm), date unknown, Secondary → cites
 │   │   └─ Royal Free Hospital Medical School press conference, 1998, Primary (not opened, per briandeer.com) → stopped: not opened
 │   └─ Wakefield et al., 1998 (as above)
 ├─ [Rao & Andrade, *The MMR vaccine and autism: Sensation, refutation, retraction, and fraud*, *Indian J Psychiatry*](https://pmc.ncbi.nlm.nih.gov/articles/PMC3136032), 2011, Secondary → cites
 │   └─ Wakefield et al., 1998 (as above)
 └─ [Wikipedia, *H. Hugh Fudenberg*](https://en.wikipedia.org/wiki/H._Hugh_Fudenberg), date unknown, Secondary → cites
     └─ Fudenberg, 1996 (as above)

### How it changed
The root's text on MMR wasn't opened, so this table compares your version with the opened Primary, Wakefield et al. 1998.

| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Correlation stated as causation | parents linked the onset of behavioural symptoms to MMR in 8 of 12 children; the authors report an association with possible environmental triggers ([abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320%20AND%20SRC:MED&resultType=core&format=json)) | causes | Royal Free press conference, 1998, per [The Conversation](https://theconversation.com/mondays-medical-myth-the-mmr-vaccine-causes-autism-3739), which says the paper itself did not address a link |
| Scope widened | a case series of 12 referred children who had both chronic bowel inflammation and developmental regression | the MMR vaccine, generally | the same press conference, where Wakefield said ["I can't support the continued use of these three vaccines, given in combination"](http://briandeer.com/wakefield/royal-video.htm) |
| Hedge dropped | "possible environmental triggers"; in 2004, ten co-authors said no causal link had been established ([Rao & Andrade](https://pmc.ncbi.nlm.nih.gov/articles/PMC3136032)) | causes | your version |

### Status of the root
- Fudenberg 1996: the [Crossref record](https://api.crossref.org/works/10.1007/BF02628672) lists no retraction, correction or expression of concern. I did not check the journal page, Retraction Watch or PubPeer. Wikipedia calls *Biotherapy* a fringe journal that has since been discontinued.
- Wakefield et al. 1998: ten of the twelve co-authors published a [*Retraction of an interpretation*](https://api.crossref.org/works/10.1016/S0140-6736(04)15715-2) in *The Lancet* in March 2004.
- Wakefield et al. 1998: *The Lancet* fully [retracted the paper](https://api.crossref.org/works/10.1016/S0140-6736(10)60175-4) on 6 February 2010 (Crossref, Retraction Watch record 4036). The [Europe PMC record](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320%20AND%20SRC:MED&resultType=core&format=json) also lists an expression of concern in *Eur J Gastroenterol Hepatol* (2011), which I did not open.
- Wakefield et al. 1998: in 2011 Brian Deer reported in the *BMJ* that the published cases did not match the children's NHS records. Among other things, he wrote ["Only one child clearly had regressive autism"](https://briandeer.com/solved/bmj-wakefield-1-1.htm). The BMJ's own page returned 403; I read the text on Deer's site.
- Later study: [Taylor et al., *The Lancet*, 1999](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:10376617%20AND%20SRC:MED&resultType=core&format=json), 498 children with autism in North Thames: ["Our analyses do not support a causal association between MMR vaccine and autism."](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:10376617%20AND%20SRC:MED&resultType=core&format=json)
- Later study: [Hviid et al., *Annals of Internal Medicine*, 2019](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:30831578%20AND%20SRC:MED&resultType=core&format=json), a Danish nationwide cohort of 657,461 children: ["MMR vaccination does not increase the risk for autism"](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:30831578%20AND%20SRC:MED&resultType=core&format=json).

### Cold trails
- [Wikipedia, *MMR vaccine and autism*](https://en.wikipedia.org/wiki/MMR_vaccine_and_autism), date unknown: says the link ["was first suggested in the early 1990s"](https://en.wikipedia.org/wiki/MMR_vaccine_and_autism) and gives no citation for that sentence. The same article records the background: Wakefield's 1993 paper on measles virus in Crohn's disease, and solicitor Richard Barr winning legal aid in 1994 for a class action against MMR makers.

### Confidence
Medium: the root's text on MMR, Wakefield's full text and the press conference were all not opened, so the trace rests on abstract records, Crossref notices and secondary accounts.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
