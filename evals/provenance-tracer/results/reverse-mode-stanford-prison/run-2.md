---
case: reverse-mode-stanford-prison
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:45:18Z
cost_usd: 1.1135
duration_s: 139
turns: 27
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
- WebSearch: Stanford prison experiment shows good people become evil when given power
- WebFetch: https://apps.dtic.mil/sti/pdfs/AD0751041.pdf
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/31380664/
- WebFetch: https://www.apa.org/topics/forensics-law-public-safety/prison
- WebFetch: https://www.ojp.gov/ncjrs/virtual-library/abstracts/interpersonal-dynamics-simulated-prison
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/amp0000401&resultType=core&format=json
- WebFetch: https://www.simplypsychology.org/zimbardo.html
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/amp0000593&resultType=core&format=json
- WebSearch: Haslam Reicher Van Bavel 2019 "Rethinking the nature of cruelty" identity leadership Stanford Prison Experiment
- WebFetch: https://www.democracynow.org/2007/3/30/understanding_how_good_people_turn_evil/
- WebFetch: https://research-repository.st-andrews.ac.uk/handle/10023/18565
- WebSearch: Banuazizi Movahedi 1975 American Psychologist simulated prison demand characteristics questionnaire students guessed
- WebSearch: Reicher Haslam 2006 BBC prison study "Rethinking the psychology of tyranny" British Journal of Social Psychology
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/amp0000443&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:16573869&resultType=core&format=json
- WebFetch: https://www.ncjrs.gov/pdffiles1/Photocopy/10301NCJRS.pdf
- WebFetch: https://api.semanticscholar.org/graph/v1/paper/DOI:10.21236/AD0751041?fields=title,abstract,year,venue,authors
- WebFetch: https://api.crossref.org/works/10.1037/h0076835

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The source's details go into web searches.
- Source chosen: the original Haney, Banks & Zimbardo report, *Interpersonal Dynamics in a Simulated Prison*, the most cited of 3 matches. I opened its abstract record. The other matches are the 1973 journal version (*International Journal of Criminology and Penology* 1:69–97), whose copies would not open, and the 1973 *Naval Research Reviews* write-up, which I did not search.

## Provenance: the Stanford prison experiment

**Source:** [Haney, C., Banks, C. & Zimbardo, P. G., *Interpersonal Dynamics in a Simulated Prison*, US Navy–funded report, Stanford University, 1972 (NCJRS abstract record)](https://www.ojp.gov/ncjrs/virtual-library/abstracts/interpersonal-dynamics-simulated-prison). The year comes from the [Semantic Scholar record](https://api.semanticscholar.org/graph/v1/paper/DOI:10.21236/AD0751041?fields=title,abstract,year,venue,authors). The full text could not be opened: the [DTIC PDF](https://apps.dtic.mil/sti/pdfs/AD0751041.pdf) and the [NCJRS PDF](https://www.ncjrs.gov/pdffiles1/Photocopy/10301NCJRS.pdf) both returned 403.

### Status
- No retraction or correction notice appears in the records opened (NCJRS, Semantic Scholar). The 1972 report has a DOI, but its Crossref record was not checked, and the 1973 journal version has no DOI. Retraction Watch and PubPeer were not checked.
- [Banuazizi & Movahedi, *American Psychologist* 30(2):152–160, 1975](https://api.crossref.org/works/10.1037/h0076835): an early methodological critique of the study. Only its Crossref record was opened, which lists no abstract and no updates.
- [Reicher & Haslam, *Rethinking the psychology of tyranny: the BBC prison study*, *British Journal of Social Psychology*, 2006](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:16573869&resultType=core&format=json): a new study with a similar design (men randomly assigned to guards or prisoners for 8 days). The guards did not identify with their role and were reluctant to use their authority, and the prisoners overcame them. The authors conclude that tyranny becomes acceptable through "powerlessness and the failure of groups that makes tyranny psychologically acceptable."
- [Le Texier, *Debunking the Stanford Prison Experiment*, *American Psychologist* 74(7):823–839, 2019](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/amp0000401&resultType=core&format=json): drew on the study's archives and interviews with 15 participants. It reports:
  - demand characteristics;
  - biased and incomplete data collection;
  - reliance on a student-run prison exercise held 3 months earlier;
  - precise instructions given to the guards;
  - guards not told they were subjects;
  - participants rarely fully immersed.

  It also says most textbooks ignore these criticisms.
- [Haslam, Reicher & Van Bavel, *Rethinking the nature of cruelty*, *American Psychologist* 74(7):809–822, 2019](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/amp0000443&resultType=core&format=json): archive material shows the experimenters directly encouraged the guards to act tough. The authors argue this fits *identity leadership* better than the guards conforming to the role on their own.
- [Zimbardo & Haney, *Continuing to acknowledge the power of dehumanizing environments*, *American Psychologist* 75(3):400–402, 2020](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/amp0000593&resultType=core&format=json): the original authors' reply to both 2019 papers. They maintain that the study shows destructive dynamics arising when one group holds near-total power over a derogated group in a dehumanizing setting. They reject the critiques as ad hominem, inaccurate or unscientific.

### What it found
The researchers screened volunteer male college students to get a normal, homogeneous sample. They randomly assigned half to play guards and half to play prisoners in a simulated prison for nearly a week; it was planned to run longer. The report says the prisoners became passive, dependent, depressed and helpless, and about half had emotional disturbance severe enough to be released early. At least a third of the guards became more aggressive and dehumanizing than expected, and the authors attributed few of these reactions to pre-existing personality differences.

### Popular versions
| Version | Where it appears | How it differs |
| --- | --- | --- |
| The study shows "good, normal people can do evil things" under situational pressure | [Simply Psychology](https://www.simplypsychology.org/zimbardo.html), 2022 | Scope widened: the report described at least a third of the guards in one sample of male students, and this applies it to people in general. Context removed: it leaves out the experimenters' instructions to the guards, which the 2019 archive papers report. The same page also notes that the study's standing has been downgraded. |
| Zimbardo: "ordinary people, even good people, can be seduced or corrupted" | [Democracy Now!](https://www.democracynow.org/2007/3/30/understanding_how_good_people_turn_evil/), 2007 | Scope widened: the finding is applied to powerful social situations in general. Context removed: the finding is carried from a week-long student simulation to Abu Ghraib. It is the study's own author speaking, so the attribution is not shifted. |
