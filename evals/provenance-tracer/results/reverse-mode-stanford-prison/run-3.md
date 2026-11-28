---
case: reverse-mode-stanford-prison
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:46:33Z
cost_usd: 1.0944
duration_s: 194
turns: 31
error: none
---

## Tool calls

- Skill: provenance-tracer:provenance-tracer
- Read: <plugin>/skills/provenance-tracer/references/output-template.md
- Read: <plugin>/skills/provenance-tracer/references/search-playbook.md
- Read: <plugin>/skills/provenance-tracer/references/mutation-types.md
- ToolSearch: {"query":"select:WebSearch,WebFetch","max_results":2}
- WebSearch: Haney Banks Zimbardo 1973 "Interpersonal dynamics in a simulated prison" pdf
- WebSearch: Stanford prison experiment Le Texier 2019 American Psychologist "Debunking the Stanford Prison Experiment"
- WebSearch: Stanford prison experiment shows ordinary people become cruel when given power
- WebFetch: https://apps.dtic.mil/sti/pdfs/AD0751041.pdf
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/31380664/
- WebFetch: https://www.simplypsychology.org/zimbardo.html
- WebFetch: https://www.ojp.gov/ncjrs/virtual-library/abstracts/interpersonal-dynamics-simulated-prison
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:31380664&resultType=core&format=json
- WebFetch: https://www.ncjrs.gov/pdffiles1/Photocopy/10301NCJRS.pdf
- WebSearch: Haslam Reicher Van Bavel 2019 "Rethinking the nature of cruelty" identity leadership Stanford Prison Experiment
- WebSearch: Vox "The Stanford Prison Experiment was massively influential. We just learned it was a fraud" Blum 2018
- WebFetch: https://apps.dtic.mil/sti/citations/AD0751041
- WebFetch: https://research-repository.st-andrews.ac.uk/handle/10023/18565
- WebFetch (error): https://www.vox.com/platform/amp/2018/6/13/17449118/stanford-prison-experiment-fraud-psychology-replication
- WebFetch: https://www.researchgate.net/publication/313621236_Interpersonal_dynamics_in_a_simulated_prison
- WebFetch: https://blogs.scientificamerican.com/observations/rethinking-the-infamous-stanford-prison-experiment/?redirect=1
- WebFetch: https://www.paloaltoonline.com/news/2018/07/01/was-the-stanford-prison-experiment-a-sham-a-qa-with-the-writer-who-exposed-the-celebrated-study-2/
- WebFetch: https://www.scientificamerican.com/blog/observations/rethinking-the-infamous-stanford-prison-experiment/?redirect=1
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/amp0000593&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1348/014466605X48998&resultType=core&format=json
- WebFetch: https://www.inc.com/bill-murphy-jr/a-new-report-says-stanfords-most-famous-psychology-experiment-is-a-fraud-a-sham-a-lie.html?cid=hmhero
- WebFetch: https://api.crossref.org/works/10.21236/AD0751041
- WebFetch: https://www.sciencing.com/2224906/twenty-four-college-students-sealed-themselves-fake-prison-something-went-wrong/
- WebFetch: https://en.wikipedia.org/wiki/Stanford_prison_experiment

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The source's details go into web searches.
- Several works match the *Stanford prison experiment*. I took the most cited: Haney, Banks & Zimbardo, *Interpersonal Dynamics in a Simulated Prison* (*International Journal of Criminology and Penology* 1, 69–97, 1973). It also exists as a Navy-funded technical report dated 1 October 1972. I did not trace the other write-ups, such as Zimbardo's popular articles and his book *The Lucifer Effect*.

## Provenance: the Stanford prison experiment

**Source:** [Haney, Banks & Zimbardo, *Interpersonal Dynamics in a Simulated Prison*, Navy-funded report version (NCJRS abstract record), 1972/1973](https://www.ojp.gov/ncjrs/virtual-library/abstracts/interpersonal-dynamics-simulated-prison)

### Status
- **No retraction or correction found in the one record I checked.** The [Crossref record](https://api.crossref.org/works/10.21236/AD0751041) for the 1972 report version (DOI 10.21236/AD0751041) shows no retraction, correction or expression of concern. I did not open the 1973 journal's own page, Retraction Watch or PubPeer. Three full-text copies of the paper (DTIC PDF, NCJRS PDF, ResearchGate) returned errors, so I could not read the full text.
- **Archival reanalysis:** [Le Texier, *Debunking the Stanford Prison Experiment*, *American Psychologist* 74(7), 823–839, 2019](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:31380664&resultType=core&format=json). Le Texier worked from the study's archives and interviews with 15 participants. He questions the study's scientific validity and argues that textbooks have largely ignored long-standing criticisms of it.
- **Second reanalysis:** Haslam, Reicher & Van Bavel, *Rethinking the nature of cruelty*, *American Psychologist* 74(7), 809–822, 2019 (not opened, per [the same authors' *Scientific American* piece, 2019](https://www.scientificamerican.com/blog/observations/rethinking-the-infamous-stanford-prison-experiment/?redirect=1)). The authors say the archive's audio tapes show a research-team member pressing a reluctant guard to act tough. They also say some guards resisted, and that taking on a role is "not sufficient to produce cruel behavior."
- **The original authors' reply:** [Zimbardo & Haney, comment in *American Psychologist* 75(3), 400–402, 2020](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/amp0000593&resultType=core&format=json). They hold that the study remains a classic demonstration of how dehumanizing environments with near-total power produce destructive dynamics. They reject the critiques they consider ad hominem or inaccurate.
- **A related later study:** [Reicher & Haslam, the BBC Prison Study, *British Journal of Social Psychology* 45, 2006](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1348/014466605X48998&resultType=core&format=json). Men were randomly assigned as guards or prisoners for eight days. The guards were reluctant to use their authority, and the prisoners eventually gained the upper hand. The authors conclude it is "powerlessness and the failure of groups that makes tyranny psychologically acceptable."
- **Participant accounts and early readings,** per [Wikipedia](https://en.wikipedia.org/wiki/Stanford_prison_experiment):
  - Prisoner Douglas Korpi said in a 2017 interview that "his breakdown had been fake." Zimbardo replied in 2018 that this account was a lie.
  - Erich Fromm argued in 1973 that only about a third of the guards behaved sadistically.

### What it found
The study screened male college volunteers and randomly assigned them to play guards or prisoners in a mock prison for about a week, choosing "A HOMOGENEOUS, NORMAL SAMPLE ... AFTER EXTENSIVE INTERVIEWING AND DIAGNOSTIC TESTING". The authors report intense reactions: many guards became more aggressive and dehumanizing than expected, prisoners became passive and depressed, and some prisoners were released early in acute distress. Because of the screening, they attributed few of these reactions to pre-existing traits and credited the simulated environment itself. The full text, with any hedges it carries, would not open; this summary rests on the abstract record.

### Popular versions
| Version | Where it appears | How it differs |
| --- | --- | --- |
| "Even good, normal people can do evil things" when situations push them | [Simply Psychology (McLeod)](https://www.simplypsychology.org/zimbardo.html), first published 2022, updated 2026 | **Scope widened:** a single study of screened male students becomes a claim about people in general. **Hedge dropped:** the result is stated as a general rule. The same page does go on to set out Le Texier's critique and the demand-characteristics criticism. |
| "the guards were coached to be brutal towards the prisoners" | [Sciencing (Oliverio)](https://www.sciencing.com/2224906/twenty-four-college-students-sealed-themselves-fake-prison-something-went-wrong/), 2026 | **Attribution shifted:** this retells the 2018–19 archival critiques, not the 1973 paper, which credits the environment. **Hedge dropped:** coaching is stated as fact, and Zimbardo & Haney's 2020 rebuttal is not mentioned. **Number changed:** it says two-thirds of guards were not sadistic, a reading Wikipedia traces to Fromm (1973), not the study. |
| Ended on day 6 because of guard brutality and prisoner breakdowns | [Wikipedia](https://en.wikipedia.org/wiki/Stanford_prison_experiment), date unknown | **Context added:** the account of the study is mixed with later disputes, including Korpi's account, Eshelman saying he played his guard role like an actor, and Fromm's one-third figure. These sit beside the original narrative. |
