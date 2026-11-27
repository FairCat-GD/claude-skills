---
case: reverse-mode-stanford-prison
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:29:16Z
cost_usd: 1.1127
duration_s: 145
turns: 29
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
- WebSearch: Stanford prison experiment shows ordinary people become cruel when given power
- WebFetch: https://apps.dtic.mil/sti/pdfs/AD0751041.pdf
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/31380664/
- WebFetch: https://www.simplypsychology.org/zimbardo.html
- WebSearch: Reicher Haslam 2006 "Rethinking the psychology of tyranny: The BBC prison study" British Journal of Social Psychology
- WebSearch: Zimbardo Haney 2020 "Continuing to acknowledge the power of dehumanizing environments"
- WebFetch: https://www.ojp.gov/ncjrs/virtual-library/abstracts/interpersonal-dynamics-simulated-prison
- WebFetch: https://www.researchgate.net/publication/313621236_Interpersonal_dynamics_in_a_simulated_prison
- WebFetch: https://osf.io/preprints/psyarxiv/mjhnp_v1
- WebFetch (error): http://www.bbcprisonstudy.org/pdfs/bjsp(2006)tyrannny.pdf
- WebFetch: https://www.ncjrs.gov/pdffiles1/Photocopy/10301NCJRS.pdf
- WebFetch: https://www.ovid.com/journals/ampsy/abstract/10.1037/amp0000401~debunking-the-stanford-prison-experiment?redirectionsource=fulltextview
- WebFetch: https://en.wikipedia.org/wiki/Stanford_prison_experiment
- WebFetch: https://www.scribd.com/document/804731321/Interpersonal-dynamics-in-a-simulated-prison-International-Journal-of-Criminology-and-Penology-1-69-97-text
- WebSearch: Ben Blum "The Lifespan of a Lie" Stanford prison experiment Medium 2018
- WebFetch: https://www.paloaltoonline.com/news/2018/07/01/was-the-stanford-prison-experiment-a-sham-a-qa-with-the-writer-who-exposed-the-celebrated-study-2/
- WebFetch: https://www.semanticscholar.org/paper/Debunking-the-Stanford-Prison-Experiment.-Texier/25aa53ca5a6599f7d7464761d4447ca331c48cd9
- WebFetch: https://www.prisonexp.org/
- WebFetch: https://api.crossref.org/works/10.1037/amp0000401
- WebFetch: https://stafforini.com/works/le-texier-2019-debunking-stanford-prison/

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The source's details go into web searches.
- Source chosen: the main write-up of the Stanford Prison Experiment (SPE), Haney, Banks & Zimbardo's *Interpersonal Dynamics in a Simulated Prison*. It is the most cited of 4 matches. The other 3 are the 1972 Navy-funded technical report of the same title, Haney, Banks & Zimbardo in *Naval Research Reviews* (1973), and Zimbardo's *The Mind Is a Formidable Jailer* in the *New York Times Magazine* (1973). Wikipedia lists all of them.

## Provenance: the Stanford prison experiment

**Source:** [Haney, C., Banks, C. & Zimbardo, P. G., *Interpersonal Dynamics in a Simulated Prison*, International Journal of Criminology and Penology, vol. 1, 1973 (abstract as held by the NCJRS library)](https://www.ojp.gov/ncjrs/virtual-library/abstracts/interpersonal-dynamics-simulated-prison)

### Status
- **Full text not opened.** I tried to fetch 4 copies of the full text: [DTIC](https://apps.dtic.mil/sti/pdfs/AD0751041.pdf) (403), [the NCJRS PDF](https://www.ncjrs.gov/pdffiles1/Photocopy/10301NCJRS.pdf) (403), [ResearchGate](https://www.researchgate.net/publication/313621236_Interpersonal_dynamics_in_a_simulated_prison) (403), and [Scribd](https://www.scribd.com/document/804731321/Interpersonal-dynamics-in-a-simulated-prison-International-Journal-of-Criminology-and-Penology-1-69-97-text), which loaded only a wrapper. *What it found* below rests on the abstract alone.
- **No retraction or correction checks.** I found no journal page or DOI for the 1973 article, so the publisher, Crossref, Retraction Watch and PubPeer checks could not be run on it. None of the opened pages mentions a retraction or correction.
- **Banuazizi & Movahedi, 1975, *American Psychologist*** (not opened, per [Wikipedia](https://en.wikipedia.org/wiki/Stanford_prison_experiment)). They argued the behaviour came from demand characteristics, with participants acting out the roles they were cast in, not from the prison setting. [Simply Psychology](https://www.simplypsychology.org/zimbardo.html) reports that most people they asked predicted the guards would become abusive and the prisoners passive.
- **Carnahan & McFarland, 2007, *Personality and Social Psychology Bulletin*** (not opened, per [Wikipedia](https://en.wikipedia.org/wiki/Stanford_prison_experiment)). People who answered an advert for a "prison life" study scored higher on aggressiveness, and lower on empathy and altruism, than people who answered a generic advert. This points to self-selection.
- **Reicher & Haslam's BBC Prison Study, run 2002, published 2006 in the *British Journal of Social Psychology*.** I tried to fetch [the PDF](http://www.bbcprisonstudy.org/pdfs/bjsp(2006)tyrannny.pdf) and the fetch failed. Per [Wikipedia](https://en.wikipedia.org/wiki/Stanford_prison_experiment), the guards were told only to run a prison, and the results challenged the idea that people slip mindlessly into roles. Per [Simply Psychology](https://www.simplypsychology.org/zimbardo.html), the guards did not uniformly turn cruel, and many prisoners organised and challenged them.
- **Blum, *The Lifespan of a Lie*, Medium, June 2018** (not opened, per [Palo Alto Online, 2018](https://www.paloaltoonline.com/news/2018/07/01/was-the-stanford-prison-experiment-a-sham-a-qa-with-the-writer-who-exposed-the-celebrated-study-2/)).
  - A prisoner told Blum his much-cited breakdown was acting.
  - Another participant said Zimbardo had encouraged the guards to act aggressively.
  - Guard Dave Eshelman "took it as a kind of an improv exercise."
  - Per [Wikipedia](https://en.wikipedia.org/wiki/Stanford_prison_experiment), in a 2017 interview prisoner Douglas Korpi said his breakdown had been fake.
  - Zimbardo replied with a 26-page defence.
- **Le Texier, *Debunking the Stanford Prison Experiment*, *American Psychologist* 74(7), 823–839, October 2019.** I opened its [Crossref record](https://api.crossref.org/works/10.1037/amp0000401), which lists no corrections or updates. The paper itself was not opened. Per [Wikipedia](https://en.wikipedia.org/wiki/Stanford_prison_experiment), it draws on the SPE archives and argues the guards were asked directly to behave in ways that would confirm Zimbardo's conclusions.
- **Haslam, Reicher & Van Bavel, *American Psychologist*, October 2019** (not opened, per [Wikipedia](https://en.wikipedia.org/wiki/Stanford_prison_experiment)). It argues that "identity leadership" by the experimenters drove the guards' cruelty, not role-taking alone.
- **Zimbardo & Haney, *American Psychologist* 75(3), 2020** (not opened). This is their comment on Le Texier and on Haslam et al. Per [Wikipedia](https://en.wikipedia.org/wiki/Stanford_prison_experiment), Zimbardo called Le Texier's paper mostly an ad hominem attack that ignored contrary data. Wikipedia also reports a 2018 joint statement by Zimbardo, Reicher and Haslam that both experiments were valid.

### What it found
Male college student volunteers, screened for pre-existing dispositions, were randomly assigned to be guards or prisoners in a simulated prison for nearly a week. The authors report that the setting became a ["psychologically compelling prison environment."](https://www.ojp.gov/ncjrs/virtual-library/abstracts/interpersonal-dynamics-simulated-prison) The prisoners became passive, depressed and helpless, and about half had acute emotional distress severe enough to be released early. The guards gained social power and status, and at least a third became more aggressive and dehumanizing than expected.

### Popular versions
| Version | Where it appears | How it differs |
| --- | --- | --- |
| "Even good, normal people can do evil things when situational forces push them in that direction." | [Simply Psychology](https://www.simplypsychology.org/zimbardo.html), 2022 | **Scope widened:** one week-long simulation with student volunteers becomes a rule about "good, normal people" in general. **Hedge dropped:** the abstract's "at least a third" of guards becomes an unqualified claim. **Context removed:** the same page reports that the guards' orientation encouraged cruelty, which this summary line leaves out. |
| "Our guards became sadistic and our prisoners became depressed" | [prisonexp.org](https://www.prisonexp.org/) (Zimbardo's own site), date unknown | **Scope widened and number changed:** "at least a third" of guards in the abstract becomes "our guards", with no fraction. No critique is mentioned. |
| "Normal people can take ghastly actions," likening the SPE to Arendt on Eichmann | 1996 Stanford News piece, as quoted by [Wikipedia](https://en.wikipedia.org/wiki/Stanford_prison_experiment) | **Scope widened:** the result in a lab simulation is extended to real-world atrocity. **Context removed:** the setting, the sample and the abstract's fractions are dropped. |
