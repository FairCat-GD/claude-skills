---
case: reverse-mode-stanford-prison
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T19:19:18Z
cost_usd: 0.9747
duration_s: 137
turns: 26
error: none
---

## Tool calls

- Skill: provenance-tracer:provenance-tracer
- Read: <plugin>/skills/provenance-tracer/references/output-template.md
- Read: <plugin>/skills/provenance-tracer/references/search-playbook.md
- Read: <plugin>/skills/provenance-tracer/references/mutation-types.md
- ToolSearch: {"query":"select:WebSearch,WebFetch","max_results":2}
- WebSearch: Haney Banks Zimbardo 1973 "Interpersonal dynamics in a simulated prison" pdf
- WebSearch: Le Texier 2019 "Debunking the Stanford Prison Experiment" American Psychologist
- WebSearch: Stanford prison experiment shows good people turn evil when given power
- WebFetch: https://apps.dtic.mil/sti/pdfs/AD0751041.pdf
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/31380664/
- WebFetch: https://www.apa.org/topics/forensics-law-public-safety/prison
- WebFetch: https://www.simplypsychology.org/zimbardo.html
- WebFetch: https://www.ojp.gov/ncjrs/virtual-library/abstracts/interpersonal-dynamics-simulated-prison
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/amp0000401&resultType=core&format=json
- WebSearch: BBC Prison Study Reicher Haslam 2006 "Rethinking the psychology of tyranny" British Journal of Social Psychology
- WebFetch: https://www.ncjrs.gov/pdffiles1/Photocopy/10301NCJRS.pdf
- WebFetch (error): http://www.bbcprisonstudy.org/pdfs/bjsp(2006)tyrannny.pdf
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/amp0000593&resultType=core&format=json
- WebFetch: https://greatergood.berkeley.edu/article/item/does_power_corrupt_everyone_equally
- WebFetch: https://www.researchgate.net/publication/313621236_Interpersonal_dynamics_in_a_simulated_prison
- WebFetch: https://research-portal.st-andrews.ac.uk/en/publications/rethinking-the-psychology-of-tyranny-the-bbc-prison-study/
- WebFetch: https://api.semanticscholar.org/graph/v1/paper/4ab0111c47c08502583755c9418c23badd90696e?fields=title,authors,year,venue,abstract,externalIds
- WebSearch: "Stanford prison experiment" retraction Retraction Watch Haney Banks Zimbardo
- WebFetch: https://retractionwatch.com/2025/03/10/guest-post-should-zimbardos-stanford-prison-experiment-be-retracted/

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The source's details go into web searches.
- Several records match *the Stanford prison experiment*. This report uses the most cited one: Haney, Banks & Zimbardo, *Interpersonal Dynamics in a Simulated Prison*, the Navy-funded report that was published in 1973 in the *International Journal of Criminology and Penology*. Other matches: the 1972 DTIC technical report version (AD-751041), which would not open (HTTP 403), and later write-ups by Zimbardo.

## Provenance: the Stanford prison experiment

**Source:** [Haney, C., Banks, C. & Zimbardo, P. G., *Interpersonal Dynamics in a Simulated Prison*, NCJRS abstract record of the Navy-funded report (no date on the record; journal version in *International Journal of Criminology and Penology*, 1973)](https://www.ojp.gov/ncjrs/virtual-library/abstracts/interpersonal-dynamics-simulated-prison)

### Status
- No retraction found. A 2025 guest post on [Retraction Watch](https://retractionwatch.com/2025/03/10/guest-post-should-zimbardos-stanford-prison-experiment-be-retracted/) by Augustine Brannigan argues the paper should be retracted. It notes that the journal stopped publishing in 1978, so "a retraction in the IJCP is not even possible". The grounds it gives are no hypotheses or control group, coached guards, ethics problems and publicity before peer review.
- Le Texier (2019), [*Debunking the Stanford Prison Experiment*, *American Psychologist* 74(7):823–839](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/amp0000401&resultType=core&format=json), drew on the study's archives and interviews with 15 participants. It reports biased and incomplete data collection, precise instructions given to the guards, guards who were not told they were subjects, and a study that relied on an earlier prison experiment run by students in one of Zimbardo's classes.
- The authors replied in Zimbardo & Haney (2020), [*Continuing to acknowledge the power of dehumanizing environments*, *American Psychologist* 75(3):400–402](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/amp0000593&resultType=core&format=json). They stand by the study and reject criticisms they call "ad hominem, misleading, inaccurate, and unscientific".
- Later study: Reicher & Haslam (2006), [*Rethinking the psychology of tyranny: the BBC Prison Study*, *British Journal of Social Psychology* 45(1):1–40](https://research-portal.st-andrews.ac.uk/en/publications/rethinking-the-psychology-of-tyranny-the-bbc-prison-study/), randomly split men into guards and prisoners for eight days. Its guards did not identify with their role, were reluctant to use their authority, and were eventually overpowered by the prisoners. The authors propose that powerlessness and the failure of groups are what make tyranny psychologically acceptable.
- Not checked: the 1973 article has no DOI that I could find, so there is no Crossref record, and I did not search PubPeer. I could not open the full text: the DTIC and NCJRS PDFs and the ResearchGate copy all returned HTTP 403. The summary below rests on the NCJRS abstract.

### What it found
College students, screened to reduce differences in personality, were randomly assigned to play guards or prisoners in a mock prison, with guards working eight-hour shifts. Prisoners lost their sense of personal identity and became passive, depressed and helpless, and about half had acute emotional distress severe enough that they were released early. Guards gained social power and group identity, and at least a third were judged to have become far more aggressive and dehumanizing than expected; the authors put these reactions down to the situation rather than to traits the participants already had.

### Popular versions
| Version | Where it appears | How it differs |
| --- | --- | --- |
| "Even good, normal people can do evil things when situational forces push" | [Simply Psychology (McLeod)](https://www.simplypsychology.org/zimbardo.html), 2022 (updated 2026) | **Scope widened:** a small sample of screened, self-selected college students becomes *good, normal people* in general. **Number changed:** *at least a third* of the guards becomes people as a whole. **Context removed:** the instructions given to the guards (per Le Texier) are left out of this conclusion, though the page covers them later in its section on criticisms. |
| Everyday people, given too much power, become sadistic tyrants (given as the standard account) | [Greater Good (Kaufman)](https://greatergood.berkeley.edu/article/item/does_power_corrupt_everyone_equally), 2015 | **Scope widened** and **number changed** in the same way. **Context removed:** Zimbardo told the guards to gain control over the prisoners, which makes "given power" alone the cause. Kaufman gives this account in order to criticize it: he notes how much guards differed and calls the original message too simplistic. |
