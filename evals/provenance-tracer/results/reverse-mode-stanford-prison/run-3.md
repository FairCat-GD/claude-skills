---
case: reverse-mode-stanford-prison
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:29:16Z
cost_usd: 1.3748
duration_s: 151
turns: 32
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
- WebSearch: Stanford prison experiment shows ordinary people become cruel when given power
- WebFetch: https://www.researchgate.net/publication/313621236_Interpersonal_dynamics_in_a_simulated_prison
- WebFetch: https://apps.dtic.mil/sti/pdfs/AD0751041.pdf
- WebFetch: https://www.ojp.gov/ncjrs/virtual-library/abstracts/interpersonal-dynamics-simulated-prison
- WebFetch: https://www.semanticscholar.org/paper/Interpersonal-Dynamics-in-a-Simulated-Prison-Haney-Banks/4ab0111c47c08502583755c9418c23badd90696e
- WebFetch: https://www.ncjrs.gov/pdffiles1/Photocopy/10301NCJRS.pdf
- WebFetch: https://osf.io/preprints/psyarxiv/mjhnp/
- WebSearch: "Debunking the Stanford Prison Experiment" doi 10.1037/amp0000401 abstract
- WebSearch: Carnahan McFarland 2007 "prison study" self-selection advertisement
- WebSearch: Haslam Reicher Van Bavel 2019 "Rethinking the nature of cruelty" Stanford prison experiment
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/31380664/
- WebFetch: https://research-repository.st-andrews.ac.uk/handle/10023/18565
- WebFetch: https://sites.pitt.edu/~bertsch/Carnahan.pdf
- WebFetch: https://www.simplypsychology.org/zimbardo.html
- WebFetch: https://www.britannica.com/event/Stanford-Prison-Experiment
- WebFetch: https://gwern.net/doc/psychology/2019-letexier.pdf
- WebFetch: https://mindmatters.ai/2025/03/should-the-iconic-stanford-prison-experiment-study-be-retracted/
- WebSearch: Reicher Haslam 2006 BBC prison study "Rethinking the psychology of tyranny" British Journal of Social Psychology
- WebSearch: Retraction Watch Brannigan "Should Zimbardo's Stanford Prison Experiment be retracted"
- WebFetch: https://brainzmagazine.com/post/when-cruelty-becomes-normal-and-what-the-stanford-prison-experiment-reveals-about-power
- WebFetch: https://retractionwatch.com/2025/03/10/guest-post-should-zimbardos-stanford-prison-experiment-be-retracted/
- WebFetch: https://scienceandbeliefs.substack.com/p/how-power-changes-people-the-1971
- WebFetch (error): http://www.bbcprisonstudy.org/pdfs/bjsp(2006)tyrannny.pdf

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The source's details go into web searches.
- Several works match "the Stanford prison experiment". I picked the most cited: Haney, Banks & Zimbardo's 1973 journal article. The other match is a Navy-funded technical report from 1972 with the same title and authors (DTIC AD-751041). Its NCJRS catalogue record is the version I could open.
- You named no beliefs that rest on this source, so there is no *Your beliefs* section.

## Provenance: the Stanford prison experiment

**Source:** [Haney, Banks & Zimbardo, *Interpersonal Dynamics in a Simulated Prison*, International Journal of Criminology and Penology 1:69–97, 1973](https://www.ojp.gov/ncjrs/virtual-library/abstracts/interpersonal-dynamics-simulated-prison)

### Status
- **I could only read the abstract.** I opened the abstract in the NCJRS record of the Navy-funded report version. The full texts at DTIC, ResearchGate and NCJRS's PDF all returned HTTP 403, and Semantic Scholar did too. The summary below therefore rests on that abstract.
- **It has not been retracted, and it can't be.** A 2025 Retraction Watch guest post by sociologist Augustine Brannigan asks whether it should be. He notes the journal stopped publishing in 1978 and writes that ["a retraction in the *IJCP* is not even possible."](https://retractionwatch.com/2025/03/10/guest-post-should-zimbardos-stanford-prison-experiment-be-retracted/) I did not run Crossref or PubPeer checks because I found no DOI for the 1973 article.
- **Haslam, Reicher & Van Bavel (2019).** *Rethinking the nature of cruelty*, [*American Psychologist* 74(7):809–822](https://research-repository.st-andrews.ac.uk/handle/10023/18565). From the study's archive, they report that the experimenters directly encouraged the guards to take on their roles and act tough. They argue this fits "identity leadership" better than the idea that guards conformed to their roles on their own.
- **Le Texier (2019).** *Debunking the Stanford Prison Experiment*, *American Psychologist* 74(7):823–839, doi:10.1037/amp0000401. (not opened, per [Retraction Watch](https://retractionwatch.com/2025/03/10/guest-post-should-zimbardos-stanford-prison-experiment-be-retracted/) and [Simply Psychology](https://www.simplypsychology.org/zimbardo.html).) This is an archival study of the experiment. Simply Psychology summarises it as finding the guards were coached toward cruelty by the experimenters. PubMed and the [gwern.net PDF](https://gwern.net/doc/psychology/2019-letexier.pdf) would not return readable text.
- **Carnahan & McFarland (2007).** *Personality and Social Psychology Bulletin* 33(5):603, doi:10.1177/0146167206292689. I [opened the PDF](https://sites.pitt.edu/~bertsch/Carnahan.pdf), but only the cover page was readable. According to [Simply Psychology](https://www.simplypsychology.org/zimbardo.html), people who answered an ad for "a psychological study of prison life" scored higher on aggression and authoritarianism than people who answered a neutral ad. The study tested new volunteers, not the 1971 participants.
- **Banuazizi & Movahedi (1975)** (not opened, per [Simply Psychology](https://www.simplypsychology.org/zimbardo.html)). This was an early critique arguing that stereotyped expectations of the roles alone could explain the results.
- **Reicher & Haslam (2006), the BBC Prison Study.** *British Journal of Social Psychology* 45(1):1–40. This was a later prison simulation, randomly dividing men into guards and prisoners for 8 days, not a direct repeat of the 1971 study. My fetch of [the PDF](http://www.bbcprisonstudy.org/pdfs/bjsp(2006)tyrannny.pdf) failed, so this is per [Simply Psychology](https://www.simplypsychology.org/zimbardo.html), which describes its result as "no automatic slide into tyranny."

### What it found
Volunteer male college students were randomly assigned to be guards or prisoners in a mock prison for about a week, with no prior training in their roles. The prisoners became passive, depressed and helpless, and about half showed emotional disturbance severe enough to be released early. At least a third of the guards became more aggressive and dehumanizing than expected. The authors concluded that most of these reactions came from the situation rather than from the participants' existing personalities. ([NCJRS abstract](https://www.ojp.gov/ncjrs/virtual-library/abstracts/interpersonal-dynamics-simulated-prison))

### Popular versions
| Version | Where it appears | How it differs |
| --- | --- | --- |
| ["Even good, normal people can do evil things"](https://www.simplypsychology.org/zimbardo.html) when situations push them that way | [Simply Psychology](https://www.simplypsychology.org/zimbardo.html), 2022 (updated 2026) | **Scope widened:** the abstract describes a week-long simulation with one group of volunteer students, and this version applies it to people in general. **Hedge dropped:** the authors said "most" reactions came from the situation. The same page also lists the critiques of coaching, self-selection and demand characteristics. |
| ["if you put everyday people into positions of unchecked authority, cruelty will follow"](https://scienceandbeliefs.substack.com/p/how-power-changes-people-the-1971) | [Science & Beliefs Weekly](https://scienceandbeliefs.substack.com/p/how-power-changes-people-the-1971), 2026 | **Number changed:** the abstract says "at least a third" of guards; this version implies cruelty follows in general. **Scope widened:** from one simulated prison to any position of unchecked authority. **Hedge dropped:** "cruelty will follow" is stated as certain. **Context removed:** the headline line leaves out that, as the same article says further down, guards received guidance encouraging toughness. |
