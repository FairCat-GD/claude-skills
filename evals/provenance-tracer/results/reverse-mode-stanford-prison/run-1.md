---
case: reverse-mode-stanford-prison
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:45:01Z
cost_usd: 0.9544
duration_s: 149
turns: 26
error: none
---

## Tool calls

- Skill: provenance-tracer:provenance-tracer
- Read: <plugin>/skills/provenance-tracer/references/output-template.md
- Read: <plugin>/skills/provenance-tracer/references/search-playbook.md
- Read: <plugin>/skills/provenance-tracer/references/mutation-types.md
- ToolSearch: {"query":"select:WebSearch,WebFetch","max_results":2}
- WebSearch: Haney Banks Zimbardo 1973 "Interpersonal dynamics in a simulated prison"
- WebSearch: Stanford prison experiment Le Texier 2019 American Psychologist debunking
- WebSearch: Stanford prison experiment shows good people become evil situation
- WebFetch: https://www.ojp.gov/ncjrs/virtual-library/abstracts/interpersonal-dynamics-simulated-prison-0
- WebFetch: https://osf.io/preprints/psyarxiv/mjhnp/
- WebFetch: https://www.apa.org/topics/forensics-law-public-safety/prison
- WebSearch: "Interpersonal dynamics in a simulated prison" pdf "pathological reactions"
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:31380664&resultType=core&format=json
- WebFetch: https://theconversation.com/the-infamous-stanford-prison-experiment-was-flawed-so-why-is-it-still-so-influential-today-246881
- WebFetch: https://www.researchgate.net/publication/232496133_Interpersonal_Dynamics_in_a_Simulated_Prison
- WebFetch: https://www.academia.edu/3192746/Interpersonal_dynamics_in_a_simulated_prison
- WebFetch: https://philipzimbardo.com/research/stanford-prison-experiment/
- WebFetch: https://www.scribd.com/document/473552744/Interpersonal-Dynamics-in-a-simulated-prison
- WebFetch: https://api.crossref.org/works/10.1037/h0076835
- WebFetch: https://mindmatters.ai/2025/03/should-the-iconic-stanford-prison-experiment-study-be-retracted/
- WebFetch: https://www.simplypsychology.org/zimbardo.html
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/amp0000417&resultType=core&format=json
- WebFetch: https://retractionwatch.com/2025/03/10/guest-post-should-zimbardos-stanford-prison-experiment-be-retracted/
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22Rethinking%20the%20nature%20of%20cruelty%22&resultType=core&format=json

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The source's details go into web searches.
- No personal chain: traced from the web alone.
- Your question names the experiment, not one publication. Several publications match. I traced the most cited one, the 1973 peer-reviewed paper by Haney, Banks and Zimbardo. Not traced: the 1972 *Pathology of imprisonment* short report in *Society*, and the 1973 *New York Times Magazine* piece, *The mind is a formidable jailer* (both named by [Retraction Watch](https://retractionwatch.com/2025/03/10/guest-post-should-zimbardos-stanford-prison-experiment-be-retracted/)).

## Provenance: the Stanford prison experiment

**Source:** [Haney, Banks & Zimbardo, *Interpersonal dynamics in a simulated prison*, International Journal of Criminology and Penology 1, 69–97, 1973](https://www.ojp.gov/ncjrs/virtual-library/abstracts/interpersonal-dynamics-simulated-prison-0) (not opened). The NCJRS link returned an unrelated page. The [ResearchGate](https://www.researchgate.net/publication/232496133_Interpersonal_Dynamics_in_a_Simulated_Prison) and [Academia.edu](https://www.academia.edu/3192746/Interpersonal_dynamics_in_a_simulated_prison) copies returned 403. The [Scribd](https://www.scribd.com/document/473552744/Interpersonal-Dynamics-in-a-simulated-prison) copy showed only an uploader's summary that never names the authors. The citation is as given by [Retraction Watch](https://retractionwatch.com/2025/03/10/guest-post-should-zimbardos-stanford-prison-experiment-be-retracted/).

### Status
- No retraction or correction found. Brannigan's March 2025 Retraction Watch guest post calls this 1973 paper the study's first refereed report. It reports no retraction and argues that one is not possible because the journal stopped publishing in 1978. Given the critiques, he adds that "official retraction, while desirable, becomes redundant" ([Retraction Watch](https://retractionwatch.com/2025/03/10/guest-post-should-zimbardos-stanford-prison-experiment-be-retracted/)). I found no DOI, so there was no Crossref record or journal page to check.
- Banuazizi & Movahedi, *Interpersonal dynamics in a simulated prison: A methodological analysis*, American Psychologist 30(2):152–160, 1975 ([Crossref](https://api.crossref.org/works/10.1037/h0076835)). This was an early methodological critique. Crossref gives no abstract.
- Banuazizi & Movahedi 1975, per [Simply Psychology](https://www.simplypsychology.org/zimbardo.html): most people who were told the study's design predicted its results. The article reads this as a sign that stereotyped expectations (demand characteristics) could explain the behaviour.
- Le Texier, *Debunking the Stanford Prison Experiment*, American Psychologist 74(7):823–839, 2019 ([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:31380664&resultType=core&format=json)). The paper draws on the archive and on interviews with 15 participants. It reports biased data collection, demand characteristics and precise instructions given to the guards.
- Haslam, Reicher & Van Bavel, *Rethinking the nature of cruelty*, American Psychologist 74(7):809–822, 2019 ([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22Rethinking%20the%20nature%20of%20cruelty%22&resultType=core&format=json)). Archive material shows the experimenters urging guards to act tough. The authors explain the guards' cruelty as identity leadership rather than conformity to a role.
- Le Texier's book *Investigating the Stanford Prison Experiment: History of a Lie*, per [The Conversation](https://theconversation.com/the-infamous-stanford-prison-experiment-was-flawed-so-why-is-it-still-so-influential-today-246881) (Gina Perry, 2025). Guards were coached before the study began. Three prisoners were released for distress, not five, and at least one of them faked it. The study ended partly because guards were losing control and a lawyer's visit raised concerns.
- Later studies, per [Simply Psychology](https://simplypsychology.org/zimbardo.html):
  - Carnahan & McFarland (2007) found that people who volunteer for a "prison study" score higher on aggression and authoritarianism.
  - The BBC Prison Study (Reicher & Haslam, 2006), a partial re-run, did not find guards turning uniformly cruel without encouragement.
  - Neither study was opened.

### What it found
The paper itself was not opened, so this comes from opened pages that describe it. Healthy male college students, screened beforehand, were randomly assigned to play guards or prisoners in a mock prison in a Stanford basement ([Scribd summary](https://www.scribd.com/document/473552744/Interpersonal-Dynamics-in-a-simulated-prison)). The study was stopped after about six days, and the authors credited the setting, not the participants' prior personalities, for the guards' harshness and the prisoners' distress. Zimbardo's own site says participants internalized their roles ([philipzimbardo.com](https://philipzimbardo.com/research/stanford-prison-experiment/)). Archival work since then disputes how far that behaviour was spontaneous (see *Status*).

### Popular versions
| Version | Where it appears | How it differs |
| --- | --- | --- |
| "a classic demonstration of the power of social situations" | [philipzimbardo.com](https://philipzimbardo.com/research/stanford-prison-experiment/), date unknown | Scope widened: one six-day simulation with student volunteers is presented as a general demonstration about situations and morality. Context removed: the page leaves out the guard instructions that the 2019 archival papers report. |
| The study "appears to shed light on how good people can become evil" | [The Conversation](https://theconversation.com/the-infamous-stanford-prison-experiment-was-flawed-so-why-is-it-still-so-influential-today-246881), 2025 | The article describes this as the study's popular appeal and does not endorse it. Scope widened: guard and prisoner behaviour in a simulation becomes *good people* turning *evil* in general. |
| The study "revealed how easily ordinary people can conform to social roles" | [Simply Psychology](https://www.simplypsychology.org/zimbardo.html), 2022 | Scope widened and hedge dropped: a small screened sample becomes *ordinary people*. Context removed: role conformity is the main reading, though the page later lists the coaching and self-selection critiques. |
