---
case: personal-chain-bilingual-speech
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:20:35Z
cost_usd: 1.7183
duration_s: 357
turns: 40
error: none
---

## Tool calls

- Skill: provenance-tracer:provenance-tracer
- Read: <plugin>/skills/provenance-tracer/references/output-template.md
- Read: <plugin>/skills/provenance-tracer/references/search-playbook.md
- ToolSearch: {"query":"select:WebSearch,WebFetch","max_results":2}
- Read: <plugin>/skills/provenance-tracer/references/labels.md
- Read: <plugin>/skills/provenance-tracer/references/mutation-types.md
- WebSearch: "bilingual children start speaking later"
- WebSearch: bilingualism causes language delay in children myth origin
- WebSearch: origin of belief bilingual children talk later early 20th century studies Saer 1923 bilingualism
- WebSearch: bilingual toddlers first words age same as monolingual study Petitto 2001 milestones
- WebSearch: bilingual children speech delay fact check
- WebSearch: bilingual babies talk later business magazine Harvard Business Review Forbes
- WebFetch (error): https://www.newsmax.com/Health/Health-News/bilingual-babies-talk-later-how-bilingual-babies-learn-bilingual-and-learning-bilingual-babies-and-speaking-proficiency/2012/02/21/id/481814/
- WebSearch: Hoff 2012 "Dual language exposure and early bilingual development" Journal of Child Language
- WebSearch: Erika Hoff AAAS 2012 bilingual children slower to talk vocabulary
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC4323282/
- WebFetch (error): https://www.newsmax.com/Health/Health-News/bilingual-babies-talk-later-how-bilingual-babies-learn-bilingual-and-learning-bilingual-babies-and-speaking-proficiency/2012/02/21/id/481814/
- WebFetch: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6562894/
- WebSearch: "bilingual" babies "slower to talk" 2012 Hoff Vancouver news
- WebFetch: https://www.abc.net.au/science/articles/2012/02/20/3435085.htm
- WebFetch: https://moodle.unifr.ch/file.php/377/dynamique/hoff_S0305000910000759a.pdf
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC6562894/
- WebFetch: https://www.expatica.com/be/general/new-approach-urged-for-late-talking-bilingual-babies-63549/
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4323282/fullTextXML
- WebFetch: https://api.crossref.org/works/10.1017/S0305000910000759
- WebFetch: https://www.frontiersin.org/articles/10.3389/fpsyg.2019.01328/full
- WebFetch (error): https://www.britishcouncil.org/voices-magazine/few-more-myths-about-speakers-multiple-languages
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/21418730/
- WebFetch: https://iol.co.za/lifestyle/family/baby/2012-02-27-new-approach-for-bilingual-babies/
- WebFetch: https://www.tomedes.com/translator-hub/why-are-bilingual-babies-slower-to-start-talking.php
- WebFetch: https://littlewords.ai/blog/bilingual-children-speech-delay-myth
- WebFetch: https://eric.ed.gov/?id=EJ971194
- WebFetch: https://www.cambridge.org/core/journals/journal-of-child-language/article/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers/0BFAB689DC70E5A2A5220976E1939948
- WebFetch: https://atdle.org/wp-content/uploads/2018/07/translaguaging-origins_g.lewis2012.pdf
- WebSearch: bilingual children "talk later" OR "speak later" Economist OR Fortune OR "Fast Company" OR Inc bilingualism
- WebFetch: https://skemman.is/bitstream/1946/32203/1/BA%20Essay%20-%20Amila%20Crnac%20pdf.pdf
- WebFetch: https://en.wikipedia.org/wiki/Cognitive_effects_of_bilingualism
- WebFetch: https://www.babbel.com/en/magazine/bilingual-parenting

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches. Your manager's name was not searched, and they aren't named here.
- Personal chain from your message: your manager told you, after reading it in a business magazine. The magazine wasn't named, and no business-magazine version turned up in the searches, so that step isn't linked to any node.

## Provenance: "Bilingual children start speaking later."

**Roots:** Independent · **Grounding:** Primary differs · Mutated
**Earliest instance found:** Arsenian, *Bilingualism and Mental Development*, 1937 (date from: cited by [Wikipedia, *Cognitive effects of bilingualism*](https://en.wikipedia.org/wiki/Cognitive_effects_of_bilingualism)). Earlier instances may exist.
**Roots:** 2 · **Retellings found:** 9

### Chain
Your version: "Bilingual children start speaking later." (you heard it from your manager (Hearsay), who read it in an unnamed business magazine; year not given; matches no node found)
 └─ [Tomedes, *Why Are Bilingual Babies Slower to Start Talking?*](https://www.tomedes.com/translator-hub/why-are-bilingual-babies-slower-to-start-talking.php), 2015, Tertiary: children in bilingual homes "can also seem to experience a delay when it comes to learning to talk" → cites
     └─ Patti Hamaguchi, *Childhood Speech, Language, and Listening Problems*, date unknown, (not opened), per Tomedes → stopped: not opened

 Branch 2, the 2012 news cycle:
 └─ [Newsmax, *Bilingual Babies Talk Later*](https://www.newsmax.com/Health/Health-News/bilingual-babies-talk-later-how-bilingual-babies-learn-bilingual-and-learning-bilingual-babies-and-speaking-proficiency/2012/02/21/id/481814/), 2012, (not opened, timed out twice), per search listing of the AFP story → stopped: not opened
 └─ [ABC Science / AFP (Kerry Sheridan), *Sum of bilingual baby's ability equal to others*](https://www.abc.net.au/science/articles/2012/02/20/3435085.htm), 2012 (date from: byline), Secondary: bilingual babies "may appear to talk later" → cites
     └─ Erika Hoff, talk at the AAAS meeting, Vancouver, 2012, (not opened), per ABC Science → the same researcher's published study on Spanish–English toddlers in south Florida:
         └─ [Hoff, Core, Place, Rumiche, Señor & Parra, *Dual language exposure and early bilingual development*, *Journal of Child Language* 39(1)](https://eric.ed.gov/?id=EJ971194), 2012 (online 2011; date from: byline), Primary (abstract opened via ERIC)

 Branch 3, the older research literature:
 └─ [Wikipedia, *Cognitive effects of bilingualism*](https://en.wikipedia.org/wiki/Cognitive_effects_of_bilingualism), date unknown, Tertiary: early researchers "believed that bilinguals would have smaller vocabularies and stunted cognitive abilities" → cites
     ├─ Hakuta & Diaz, 1985, (not opened), per Wikipedia: later studies reported bilinguals did worse on IQ tests and in language development → stopped: not opened
     └─ Arsenian, *Bilingualism and Mental Development*, 1937, Primary (not opened, per Wikipedia)

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Other: a different measure | Hoff et al. measured vocabulary and grammar size at 22–30 months. They did not measure when children first start speaking. | start speaking later | [ABC Science / AFP](https://www.abc.net.au/science/articles/2012/02/20/3435085.htm), 2012 |
| Context removed | Bilingual children were behind only when each language was tested on its own. On total vocabulary across both languages, the two groups were comparable. | Bilingual children start speaking later. | [Tomedes](https://www.tomedes.com/translator-hub/why-are-bilingual-babies-slower-to-start-talking.php), 2015 |
| Scope widened | 47 Spanish–English bilingual toddlers from high-SES families, compared with 56 monolingual toddlers | Bilingual children | [ABC Science / AFP](https://www.abc.net.au/science/articles/2012/02/20/3435085.htm), 2012 |
| Hedge dropped | ABC: bilingual babies "may appear" to talk later; Tomedes: they "can seem" to | start speaking later | your version |

### Status of the root
- Hoff et al. 2012: the [Crossref record](https://api.crossref.org/works/10.1017/S0305000910000759) shows no retraction, correction or erratum. It has 750 citing works. Retraction Watch and PubPeer were not checked because the fetch budget ran out.
- Major later study: [Muszyńska et al., *Bilingual children reach early language milestones at the same age as monolingual peers*, *Journal of Child Language*](https://www.cambridge.org/core/journals/journal-of-child-language/article/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers/0BFAB689DC70E5A2A5220976E1939948), 2025. It compared 302 Polish bilingual children with 302 matched monolingual children from birth to 24 months. It reports that "typical bilingual development follows a trajectory similar to monolingual development". The authors say the evidence was strongest for the first word, and that they cannot draw strong conclusions about later milestones.
- Arsenian 1937: not opened, so its status was not checked.

### Cold trails
None.

### Confidence
Medium. The Hoff study was opened only as an abstract. The step from the AFP story to the paper is an inference: the story cites Hoff's talk, not the paper. The Newsmax headline and the whole pre-1962 branch were not opened. Early IQ studies from the 1920s, often named as the start of this belief, came up only in search snippets, so they are not in the chain.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
