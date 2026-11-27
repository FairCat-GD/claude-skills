---
case: reverse-mode-stanford-prison
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:28:17Z
cost_usd: 0.9495
duration_s: 153
turns: 30
error: none
---

## Tool calls

- Skill: provenance-tracer:provenance-tracer
- Read: <plugin>/skills/provenance-tracer/references/output-template.md
- Read: <plugin>/skills/provenance-tracer/references/search-playbook.md
- Read: <plugin>/skills/provenance-tracer/references/mutation-types.md
- ToolSearch: {"query":"select:WebSearch,WebFetch","max_results":2}
- WebSearch: Haney Banks Zimbardo 1973 "Interpersonal dynamics in a simulated prison" pdf
- WebSearch: Stanford prison experiment Le Texier 2019 American Psychologist debunking
- WebSearch: Stanford prison experiment showed ordinary people become cruel when given power
- WebFetch: https://apps.dtic.mil/sti/pdfs/AD0751041.pdf
- WebFetch: https://osf.io/preprints/psyarxiv/mjhnp/
- WebFetch: https://en.wikipedia.org/wiki/Stanford_prison_experiment
- WebFetch: https://www.simplypsychology.org/zimbardo.html
- WebFetch: https://www.ojp.gov/ncjrs/virtual-library/abstracts/interpersonal-dynamics-simulated-prison
- WebFetch: https://psyarxiv.com/mjhnp/
- WebFetch: https://www.britannica.com/event/Stanford-Prison-Experiment
- WebFetch: https://www.ncjrs.gov/pdffiles1/Photocopy/10301NCJRS.pdf
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/31380664/
- WebSearch: Reicher Haslam 2006 "Rethinking the psychology of tyranny" BBC prison study British Journal of Social Psychology
- WebFetch: https://api.crossref.org/works/10.1037/amp0000401
- WebFetch: https://api.crossref.org/works/10.21236/AD0751041
- WebFetch (error): http://www.bbcprisonstudy.org/pdfs/bjsp(2006)tyrannny.pdf
- WebFetch: https://www.scribd.com/document/804731321/Interpersonal-dynamics-in-a-simulated-prison-International-Journal-of-Criminology-and-Penology-1-69-97-text
- WebFetch: https://www.semanticscholar.org/paper/Debunking-the-Stanford-Prison-Experiment.-Texier/25aa53ca5a6599f7d7464761d4447ca331c48cd9
- WebFetch: https://mindmatters.ai/2025/03/should-the-iconic-stanford-prison-experiment-study-be-retracted/
- WebFetch: https://findanexpert.unimelb.edu.au/news/98029-the-infamous-stanford-prison-experiment-was-flawed-%E2%80%93-so-why-is-it-still-so-influential-today%3F
- WebFetch: https://retractionwatch.com/2025/03/10/guest-post-should-zimbardos-stanford-prison-experiment-be-retracted/
- WebFetch: https://news.stanford.edu/stories/2024/10/philip-zimbardo-the-psychologist-behind-stanford-prison-experiment-dies-at-age-91
- WebFetch: https://www.bps.org.uk/psychologist/tyranny-revisited-groups-psychological-well-being-and-health-societies

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The source's details go into web searches.
- Several documents report the study. This report takes the most cited: Haney, Banks and Zimbardo's paper, *Interpersonal dynamics in a simulated prison*. It exists as a 1972 Office of Naval Research technical report and as the 1973 article in the *International Journal of Criminology and Penology* 1:69–97. Not chosen: the 1973 *Naval Research Reviews* write-up and Zimbardo's later books.

## Provenance: the Stanford prison experiment

**Source:** [Haney, C., Banks, C. & Zimbardo, P. G., *Interpersonal Dynamics in a Simulated Prison*, Office of Naval Research technical report, 1972 (Crossref date 1 Oct 1972); journal version in *International Journal of Criminology and Penology*, 1973](https://www.ojp.gov/ncjrs/virtual-library/abstracts/interpersonal-dynamics-simulated-prison)

### Status
- Not opened in full: the full text would not open. The DTIC PDF and the NCJRS PDF both returned 403, and the Scribd copy came back cut off. *What it found* below rests on the NCJRS abstract.
- The [Crossref record](https://api.crossref.org/works/10.21236/AD0751041) for the technical report (DOI 10.21236/AD0751041) lists no retraction, correction or other update. PubPeer was not checked.
- Retraction: Augustine Brannigan's [guest post on Retraction Watch](https://retractionwatch.com/2025/03/10/guest-post-should-zimbardos-stanford-prison-experiment-be-retracted/) (10 March 2025) reports no retraction or correction of any SPE paper. It notes that the original journal stopped publishing in 1978, so a retraction there is not possible. It also says the results were publicised by press release before peer review, and that the guards' apparent spontaneity "was due in part to coaching".
- Le Texier, *Debunking the Stanford Prison Experiment*, *American Psychologist* 74(7):823–839, October 2019 ([Crossref](https://api.crossref.org/works/10.1037/amp0000401), no corrections listed). Per [Wikipedia](https://en.wikipedia.org/wiki/Stanford_prison_experiment) and [Retraction Watch](https://retractionwatch.com/2025/03/10/guest-post-should-zimbardos-stanford-prison-experiment-be-retracted/), it is an archival analysis. It argues that the guards' cruelty followed instructions from the experimenters and the guards' wish to please them, and that at least one prisoner's breakdown was faked. The article itself was not opened: the PsyArXiv and Semantic Scholar fetches failed.
- Zimbardo & Haney (2020), *American Psychologist* 75(3):400–402, a reply to Le Texier and to Haslam et al. Per [Wikipedia](https://en.wikipedia.org/wiki/Stanford_prison_experiment), it calls Le Texier's critique mostly ad hominem. Not opened.
- BBC Prison Study, Reicher & Haslam, *British Journal of Social Psychology*, 2006. This was a partial replication in which guards were given no instructions on how to behave. The authors' [summary in *The Psychologist*](https://www.bps.org.uk/psychologist/tyranny-revisited-groups-psychological-well-being-and-health-societies) (2006) says participants "showed no 'natural' tendencies to slip helplessly into role". It reports that the guards were ambivalent and never formed a cohesive group. The journal PDF would not open.
- Earlier critiques, per [Wikipedia](https://en.wikipedia.org/wiki/Stanford_prison_experiment), not opened:
  - Banuazizi & Movahedi (1975), *American Psychologist*: the participants may have been acting out their assigned roles in response to demand characteristics.
  - Carnahan & McFarland (2007), *Personality and Social Psychology Bulletin*: the recruitment ad's mention of "prison life" may have drawn applicants who were more aggressive and less empathic.
- Consensus statement, per [Wikipedia](https://en.wikipedia.org/wiki/Stanford_prison_experiment): in 2018 Haney, Haslam, Reicher and Zimbardo issued a joint statement. It called for more replication and allowed that behaviour in both studies may have had causes beyond the situation. Not opened.

### What it found
Male college students were randomly assigned to play guards or prisoners in a mock prison. According to the [abstract](https://www.ojp.gov/ncjrs/virtual-library/abstracts/interpersonal-dynamics-simulated-prison), the prisoners lost their sense of personal identity and became passive, dependent, depressed and helpless, and half were released early with acute emotional disturbance. Meanwhile, "at least a third of the guards were judged to have become far more aggressive and dehumanizing." The authors put these reactions down mainly to the prison situation, not to the participants' pre-existing personalities. The study did not use a statistical test across conditions to establish this: it rested on the authors' observations of one simulation.

### Popular versions
| Version | Where it appears | How it differs |
| --- | --- | --- |
| The study shows that "even good, normal people can do evil things" when situational forces push them | [Simply Psychology](https://www.simplypsychology.org/zimbardo.html) (McLeod), 2022, updated 2026 | **Scope widened:** the abstract's "at least a third of the guards" becomes people in general. **Hedge dropped:** "judged to have become" becomes a plain demonstration. The same page does say that later archival work and a replication have challenged how spontaneous the cruelty was. |
| The SPE explains corporate fraud, military torture, cult behaviour and genocide (Zimbardo's own extension by 2007) | Gina Perry, [*The Conversation*, republished by the University of Melbourne](https://findanexpert.unimelb.edu.au/news/98029-the-infamous-stanford-prison-experiment-was-flawed-%E2%80%93-so-why-is-it-still-so-influential-today%3F), 2025 | **Scope widened:** one week-long simulation with students becomes an explanation of atrocities. **Context removed:** the guard coaching and the experimenters' role, described in this same article from archival sources, drop out of the story. |
| Ordinary participants spontaneously became cruel guards or broken prisoners, which proves that situations override personality | [Wikipedia](https://en.wikipedia.org/wiki/Stanford_prison_experiment) (Zimbardo's interpretation, as reported) and [Perry](https://findanexpert.unimelb.edu.au/news/98029-the-infamous-stanford-prison-experiment-was-flawed-%E2%80%93-so-why-is-it-still-so-influential-today%3F), 2025 | **Context removed:** the researchers' instructions and the recruitment ad, per Le Texier and Carnahan & McFarland. **Number changed:** the abstract's "half" of the prisoners released early becomes three released for distress rather than five, per Perry, who says at least one may have faked it. |
