---
case: reverse-mode-stanford-prison
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T19:19:38Z
cost_usd: 1.4770
duration_s: 224
turns: 37
error: none
---

## Tool calls

- Skill: provenance-tracer:provenance-tracer
- Read: <plugin>/skills/provenance-tracer/references/output-template.md
- Read: <plugin>/skills/provenance-tracer/references/search-playbook.md
- Read: <plugin>/skills/provenance-tracer/references/mutation-types.md
- ToolSearch: {"query":"select:WebSearch,WebFetch","max_results":2}
- WebSearch: Haney Banks Zimbardo 1973 "Interpersonal dynamics in a simulated prison"
- WebSearch: Le Texier 2019 "Debunking the Stanford Prison Experiment" American Psychologist
- WebSearch: Stanford prison experiment shows good people become evil when given power
- WebFetch: https://www.ojp.gov/ncjrs/virtual-library/abstracts/interpersonal-dynamics-simulated-prison-0
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/31380664/
- WebFetch: https://www.academia.edu/3192746/Interpersonal_dynamics_in_a_simulated_prison
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/amp0000401&resultType=core&format=json
- WebFetch: https://www.scribd.com/document/585398101/Haney-C-Banks-C-Zimbardo-P-G-1973-Interpersonal-Dynamics-in-a-Simulated-Prison
- WebFetch (error): https://philipzimbardo.com/research/stanford-prison-experiment/
- WebSearch: "Interpersonal dynamics in a simulated prison" pdf "International Journal of Criminology and Penology" full text edu
- WebSearch: Haslam Reicher Van Bavel 2019 "Rethinking the nature of cruelty" identity leadership Stanford Prison Experiment
- WebFetch: https://www.scribd.com/document/804731321/Interpersonal-dynamics-in-a-simulated-prison-International-Journal-of-Criminology-and-Penology-1-69-97-text
- WebFetch: https://research-repository.st-andrews.ac.uk/handle/10023/18565
- WebFetch: https://www.simplypsychology.org/zimbardo.html
- WebFetch: https://apps.dtic.mil/sti/citations/AD0751041
- WebFetch: https://scispace.com/pdf/rethinking-the-nature-of-cruelty-the-role-of-identity-4zxopvzvoq.pdf
- WebSearch: Reicher Haslam 2006 "Rethinking the psychology of tyranny: The BBC prison study" British Journal of Social Psychology
- WebSearch: Carnahan McFarland 2007 "Revisiting the Stanford Prison Experiment: Could participant self-selection have led to the cruelty?"
- WebFetch (error): http://www.bbcprisonstudy.org/pdfs/bjsp(2006)tyrannny.pdf
- WebFetch: https://sites.pitt.edu/~bertsch/Carnahan.pdf
- WebFetch: https://blogs.scientificamerican.com/observations/rethinking-the-infamous-stanford-prison-experiment/
- WebFetch: https://www.psichi.org/page/051EyeFall00aZimbard
- WebFetch: https://www.scientificamerican.com/blog/observations/rethinking-the-infamous-stanford-prison-experiment/
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:16573869&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:17440210&resultType=core&format=json
- WebFetch: https://alamrafiul.com/blogs/stanford-prison-experiment/
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/amp0000443&resultType=core&format=json
- WebSearch: Ben Blum "The Lifespan of a Lie" Stanford prison experiment Medium 2018
- WebFetch: https://www.paloaltoonline.com/news/2018/07/01/was-the-stanford-prison-experiment-a-sham-a-qa-with-the-writer-who-exposed-the-celebrated-study-2/
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/amp0000593&resultType=core&format=json

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The source's details go into web searches.
- The source taken is the most cited of 3 matches: Haney, Banks and Zimbardo's 1973 journal paper. The other two are the 1972 technical report to the Office of Naval Research (DTIC AD0751041) and the 1973 *New York Times Magazine* article by Zimbardo and colleagues.

## Provenance: the Stanford prison experiment

**Source:** [Haney, C., Banks, W. C. & Zimbardo, P. G., *Interpersonal dynamics in a simulated prison*, International Journal of Criminology and Penology 1: 69–97, 1973](https://www.ojp.gov/ncjrs/virtual-library/abstracts/interpersonal-dynamics-simulated-prison-0), not opened. I tried four copies: the NCJRS record, Academia.edu and two Scribd uploads. None returned the text, and the DTIC copy of the 1972 report returned an error too. What follows therefore comes from later papers about the study that I did open.

### Status
- I did not check for a retraction or correction (journal page, Crossref, Retraction Watch, PubPeer). The fetch budget went on copies of the paper and on the later studies below.
- **Archival critique, 2019:** [Le Texier, *Debunking the Stanford Prison Experiment*, American Psychologist 74(7), 2019](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/amp0000401&resultType=core&format=json). It draws on the study's archives and interviews with 15 participants. It reports:
  - biased and incomplete data collection;
  - guards who got precise instructions on how to treat prisoners;
  - guards who were not told they were subjects.

  It also says most textbooks have left out these criticisms.
- **Archival reanalysis, 2019:** [Haslam, Reicher & Van Bavel, *Rethinking the nature of cruelty*, American Psychologist 74(7), 2019](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/amp0000443&resultType=core&format=json). From the archive, it argues that the experimenters pushed the guards to take on their roles and act tough. On this account the guards did not conform on their own. In a companion piece, the same authors say the experimenters [used psychological tactics to persuade reluctant guards to adopt an aggressive style](https://www.scientificamerican.com/blog/observations/rethinking-the-infamous-stanford-prison-experiment/). That piece also notes that some guards resisted being brutal (*Scientific American* blog, 2019).
- **Partial replication with a different result:** [Reicher & Haslam, *Rethinking the psychology of tyranny: the BBC prison study*, British Journal of Social Psychology 45, 2006](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:16573869&resultType=core&format=json). Men were randomly assigned as guards or prisoners for 8 days, and [the guards failed to identify with their role](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:16573869&resultType=core&format=json). They were hesitant to use their authority and were overthrown. The authors conclude that tyranny takes hold when groups are powerless or have failed.
- **Self-selection, 2007:** [Carnahan & McFarland, *Revisiting the Stanford prison experiment*, Personality and Social Psychology Bulletin 33(5), 2007](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:17440210&resultType=core&format=json). People who answered an ad worded almost like the 1971 one, for a study of prison life, scored higher than other volunteers on aggressiveness, authoritarianism and social dominance. They scored lower on empathy and altruism. The authors favour a person-and-situation explanation over a purely situational one.
- **The original authors' reply, 2020:** [Zimbardo & Haney, *Continuing to acknowledge the power of dehumanizing environments*, American Psychologist 75(3), 2020](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/amp0000593&resultType=core&format=json). They stand by the study as showing how destructive dynamics arise when one group holds near-total power in a dehumanizing setting. They reject some of the critiques as ad hominem or inaccurate.

### What it found
I did not open the paper, so this is the study as its authors and critics later described it. In 2020, Zimbardo and Haney described it as showing destructive psychological dynamics in a dehumanizing prison setting where one group of student volunteers held near-total power over another. Its 2019 critics summarize the usual reading as saying that being put in a toxic role is enough, by itself, to unlock cruelty. Their archival work says the experimenters steered the guards toward that cruelty.

### Popular versions
| Version | Where it appears | How it differs |
| --- | --- | --- |
| The study showed [the power of situations to alter human behavior dramatically](https://www.simplypsychology.org/zimbardo.html), even in good, normal people | [Simply Psychology](https://www.simplypsychology.org/zimbardo.html), 2022 (updated 2026) | **Scope widened:** one simulation with student volunteers becomes a rule about people in general. **Hedge dropped:** the claim is stated as fact. The same page also covers Le Texier and the BBC Prison Study. |
| [We are all capable of cruelty when the situation enables it.](https://alamrafiul.com/blogs/stanford-prison-experiment/) | [Rafiul Alam blog](https://alamrafiul.com/blogs/stanford-prison-experiment/), 2025 | **Scope widened:** from one study to everyone. **Context removed:** the experimenters' briefing and coaching of the guards is left out. The author later added a correction in November 2026 saying that reading does not hold up well. |
