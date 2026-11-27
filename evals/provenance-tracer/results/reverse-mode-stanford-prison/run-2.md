---
case: reverse-mode-stanford-prison
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T19:19:31Z
cost_usd: 1.0130
duration_s: 142
turns: 28
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
- WebSearch: Stanford prison experiment shows ordinary people become evil when given power
- WebFetch: https://apps.dtic.mil/sti/pdfs/AD0751041.pdf
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/31380664/
- WebFetch: https://www.ojp.gov/ncjrs/virtual-library/abstracts/interpersonal-dynamics-simulated-prison
- WebFetch: https://osf.io/preprints/psyarxiv/mjhnp/
- WebFetch: https://api.crossref.org/works/10.1037/amp0000401
- WebSearch: Reicher Haslam 2006 "Rethinking the psychology of tyranny" BBC prison study British Journal of Social Psychology
- WebFetch: https://www.prisonexp.org/conclusion
- WebFetch (error): http://www.bbcprisonstudy.org/pdfs/bjsp(2006)tyrannny.pdf
- WebFetch: https://www.semanticscholar.org/paper/Debunking-the-Stanford-Prison-Experiment.-Texier/25aa53ca5a6599f7d7464761d4447ca331c48cd9
- WebFetch: https://www.simplypsychology.org/zimbardo.html
- WebFetch: https://greatergood.berkeley.edu/article/item/does_power_corrupt_everyone_equally
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/amp0000401&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:16573869&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/amp0000593&resultType=core&format=json
- WebFetch: https://api.crossref.org/works?query.bibliographic=Interpersonal+dynamics+in+a+simulated+prison+Haney+Banks+Zimbardo&rows=5
- WebSearch: "Interpersonal dynamics in a simulated prison" retraction OR "expression of concern"
- WebFetch: https://retractionwatch.com/category/by-subject/psychology-by-subject
- WebFetch: https://retractionwatch.com/2025/03/10/guest-post-should-zimbardos-stanford-prison-experiment-be-retracted/

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The source's details go into web searches.
- Several write-ups of the study exist. This report traces the most cited one, Haney, Banks & Zimbardo, *Interpersonal Dynamics in a Simulated Prison* (*International Journal of Criminology and Penology* 1, 69–97, 1973). The other matches are the October 1972 Office of Naval Research technical report with the same title, Zimbardo's website prisonexp.org, and his later book *The Lucifer Effect*.
- The journal version did not open. The DTIC copy of the 1972 report returned HTTP 403. What it found below comes from the NCJRS abstract record of that report (51 pages, funded by the US Navy), which describes the same study.

## Provenance: the Stanford prison experiment

**Source:** [Haney, C., Banks, C. & Zimbardo, P. G., *Interpersonal Dynamics in a Simulated Prison*, Stanford University report for the US Navy (NCJ 10301), 1972; journal version 1973](https://www.ojp.gov/ncjrs/virtual-library/abstracts/interpersonal-dynamics-simulated-prison)

### Status
- No retraction or correction found. The [Crossref record of the 1972 report](https://api.crossref.org/works?query.bibliographic=Interpersonal+dynamics+in+a+simulated+prison+Haney+Banks+Zimbardo&rows=5) has no update entries, and the journal version has no Crossref record. A Retraction Watch search found no notice. PubPeer was not checked.
- [Brannigan, Retraction Watch guest post, March 2025](https://retractionwatch.com/2025/03/10/guest-post-should-zimbardos-stanford-prison-experiment-be-retracted/) asks whether the study should be retracted, building on Le Texier's work. He does not recommend it, and notes that the original journal stopped publishing in 1978. His conclusion: "the best outcome we can expect is more responsible reporting in contemporary textbooks."
- [Le Texier, *Debunking the Stanford Prison Experiment*, *American Psychologist* 74(7), 2019](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/amp0000401&resultType=core&format=json) is a reanalysis based on the SPE archives and interviews with 15 participants. It reports:
  - biased and incomplete data collection;
  - guards who were given precise instructions on how to treat prisoners;
  - a design borrowed from a student project run months earlier;
  - participants who were rarely fully immersed in the situation.

  It also says textbooks have largely ignored these criticisms. [Crossref](https://api.crossref.org/works/10.1037/amp0000401) lists no corrections to the paper.
- [Zimbardo & Haney, *American Psychologist* 75(3), 2020](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/amp0000593&resultType=core&format=json) is the authors' reply. They describe the study as showing the destructive dynamics that can arise when one group holds near-total power over a derogated group in a dehumanizing setting. They reject criticisms they call ad hominem, misleading or inaccurate.
- [Reicher & Haslam, *Rethinking the psychology of tyranny: the BBC prison study*, *British Journal of Social Psychology* 45, 2006](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:16573869&resultType=core&format=json) ran a later study with a similar design: men randomly assigned as guards or prisoners for 8 days. The guards did not identify with their role, were reluctant to use their authority, and were eventually overcome by the prisoners. The authors propose that tyranny becomes acceptable through powerlessness and the failure of groups, not through the roles themselves.

### What it found
The study placed male college volunteers, screened as having normal personalities, in a simulated prison. They were randomly assigned to be guards or prisoners, and neither group got role-specific training. The authors report that the simulation became psychologically compelling. Prisoners lost their sense of personal identity and became passive, dependent, depressed and helpless, and about half had to be released early with acute emotional disturbance. At least a third of the guards were judged to have become far more aggressive and dehumanizing than expected, and the authors traced few of these reactions to pre-existing personality.

### Popular versions
| Version | Where it appears | How it differs |
| --- | --- | --- |
| The study showed how "ordinary people could be readily transformed" from good to evil | [Zimbardo, prisonexp.org, *Conclusion*](https://www.prisonexp.org/conclusion), date unknown (site © 1999–) | Scope widened: the report's *at least a third of the guards* becomes ordinary people in general. Context removed: the guards' instructions, reported by Le Texier 2019, are not mentioned |
| The study revealed that "people conform to social roles readily" | [McLeod, *Simply Psychology*](https://www.simplypsychology.org/zimbardo.html), 2022 | Scope widened: from some guards in one simulation to people in general. Hedge dropped: individual differences go unmentioned, though the page does note later archival and replication challenges |
| Everyday people given too much power become sadistic tyrants (the standard account, as summarised there) | [Kaufman, *Greater Good*, UC Berkeley](https://greatergood.berkeley.edu/article/item/does_power_corrupt_everyone_equally), 2015 | Scope widened and hedge dropped: the report's share of guards becomes everyone in power. The article itself calls this message far too simplistic |
