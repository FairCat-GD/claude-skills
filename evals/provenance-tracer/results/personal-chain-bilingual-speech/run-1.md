---
case: personal-chain-bilingual-speech
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T19:12:45Z
cost_usd: 1.6830
duration_s: 187
turns: 35
error: none
---

## Tool calls

- Skill: provenance-tracer:provenance-tracer
- Read: <plugin>/skills/provenance-tracer/references/output-template.md
- Read: <plugin>/skills/provenance-tracer/references/search-playbook.md
- Read: <plugin>/skills/provenance-tracer/references/labels.md
- Read: <plugin>/skills/provenance-tracer/references/mutation-types.md
- ToolSearch: {"query":"select:WebSearch,WebFetch","max_results":2}
- WebSearch: "bilingual children start speaking later"
- WebSearch: bilingualism causes language delay in children myth
- WebSearch: bilingual first words milestones study Petitto Holowka 2001 same timing
- WebSearch: origin of belief bilingualism delays speech history Saer 1923 Smith 1931
- WebSearch: bilingual babies talk later fact check
- WebSearch: bilingual children speak later business magazine raising bilingual kids
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1986)%20-%20MIRROR%20OF%20LANGUAGE%20THE%20DEBATE%20ON%20BILINGUALISM.pdf
- WebFetch: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.01346/full
- WebFetch: https://www.habilnet.org/bilingual-children-do-not-start-speaking-later-than-monolingual-ones/
- WebFetch: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0BFAB689DC70E5A2A5220976E1939948/S0305000924000655a.pdf/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers.pdf
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1017/S0305000924000655&resultType=core&format=json
- WebSearch: Madorah Smith 1939 "Some light on the problem of bilingualism" Hawaii preschool Genetic Psychology Monographs
- WebSearch: Madorah Smith 1931 "A study of five bilingual children from the same family" Child Development
- WebFetch: https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html
- WebFetch: https://www.jstor.org/stable/1125374
- WebFetch: https://api.crossref.org/works/10.2307/1125374
- WebFetch: https://archive.org/advancedsearch.php?q=%22problem+of+bilingualism%22+Smith+Hawaii&fl[]=identifier&fl[]=title&fl[]=year&rows=20&output=json
- WebFetch: https://www.fcd-us.org/wp-content/uploads/2016/04/Han_Bilingualism_and_Academic_and_Social_Development.pdf
- WebSearch: "Smith (1939)" bilingual Hawaii preschool speech "retardation" vocabulary 1000 children criticism Hakuta
- WebFetch: https://web.stanford.edu/~hakuta/www/research/publications/(1987)%20-%20BILINGUALISM%20AND%20COGNITIVE%20DEVELOPMENT%20THREE%20PERSPE.pdf
- WebFetch: https://files.eric.ed.gov/fulltext/ED273152.pdf
- Read (denied): <temp>/config/projects/-private-tmp-e-Yy2mK0-home-cwd/3ab2bbea-26e8-408b-8c65-2e9561000c9a/tool-results/webfetch-1795806856461-79bzkc.pdf
- WebFetch: https://commons.und.edu/cgi/viewcontent.cgi?article=10630&context=theses
- WebFetch: https://www.babbel.com/en/magazine/bilingual-parenting
- WebFetch: https://laura-ann-petitto.com/images/assets/publications/Publications/2001_PetittoKaterelosEtAl_ChildLanguage.pdf
- WebFetch: https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22Bilingual%20signed%20and%20spoken%20language%20acquisition%20from%20birth%22&resultType=core&format=json

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- Personal chain as given: your manager, who read it in a business magazine. The manager's name was not searched, and no year was given.

## Provenance: "Bilingual children start speaking later."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** Madorah E. Smith, *Some light on the problem of bilingualism as found from a study of the progress in mastery of English among preschool children of non-American ancestry in Hawaii*, *Genetic Psychology Monographs* 21, 1939 (date from: cited by [Duchan, *A History of Speech-Language Pathology*](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 7

### Chain
Your version: "Bilingual children start speaking later." (you heard it: from your manager (Hearsay), who read it in a business magazine; year not given; that magazine was not found, so it matches no node)
 └─ [Judy Duchan, *A History of Speech-Language Pathology*: Madorah Elizabeth Smith](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html), date unknown, Tertiary → cites
     └─ Smith, *Some light on the problem of bilingualism…*, *Genetic Psychology Monographs* 21, 1939, Primary (not opened, per Duchan), root
 └─ [University at Buffalo, *History of CDS*: Madorah Elizabeth Smith](https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/), date unknown, Tertiary → cites Smith 1939 (root, above)
 └─ [Bright & Filippi, *Editorial: Perspectives on the 'Bilingual Advantage'*, *Frontiers in Psychology*](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.01346/full), 2019, Secondary → cites
     └─ Saer, *The effect of bilingualism on intelligence*, *British Journal of Psychology* 14, 1923, Primary (not opened, per Bright & Filippi) → stopped: not opened

The Duchan page describes Smith's Hawaii work as concluding that using two languages at once *contributed to a lag in speech development*. The Frontiers editorial traces today's advice to raise children with one language partly to Saer's 1923 evidence of a *mental delay*. That claim is about intelligence and confusion, not about when children begin to speak. Kenji Hakuta's 1986 book *Mirror of Language*, which search results describe as the main history of this debate and which names Smith as its most influential proponent, is a scanned PDF. Its text could not be opened.

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | preschool children of non-American ancestry in Hawaii, measured on their progress in English (per Duchan) | Bilingual children start speaking later. | [habilnet, De Houwer & Pascall](https://www.habilnet.org/bilingual-children-do-not-start-speaking-later-than-monolingual-ones/), 2021 |
| Hedge dropped | using two languages *contributed to* a lag, as one factor among others (per Duchan) | Bilingual children start speaking later. | [habilnet, De Houwer & Pascall](https://www.habilnet.org/bilingual-children-do-not-start-speaking-later-than-monolingual-ones/), 2021 |
| Context removed | a comparison of poor immigrant children with middle-class native-born children (per Duchan) | Bilingual children start speaking later. | [habilnet, De Houwer & Pascall](https://www.habilnet.org/bilingual-children-do-not-start-speaking-later-than-monolingual-ones/), 2021 |
| Other: a lag in level became a later start | a *lag in speech development* at preschool age, not the age of first words (per Duchan) | Bilingual children start speaking later. | [habilnet, De Houwer & Pascall](https://www.habilnet.org/bilingual-children-do-not-start-speaking-later-than-monolingual-ones/), 2021 |

### Status of the root
- The [Duchan page](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html) says Smith's widely cited studies were "later found to be methodologically flawed". It names two problems: she paired poor immigrant children with middle-class native-born children, and she did not separate fluent bilinguals from limited ones. It gives no source for this critique.
- Smith 1939 has no DOI or publisher page that could be found and opened. No retraction, correction or failed replication notice was checked for it (journal page, Crossref, Retraction Watch and PubPeer were not reached). Her related 1931 paper, *A study of five bilingual children from the same family* (*Child Development* 2(3)), shows no update, correction or retraction in its [Crossref record](https://api.crossref.org/works/10.2307/1125374).
- Major later study: [Petitto et al. 2001, *Journal of Child Language*](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22Bilingual%20signed%20and%20spoken%20language%20acquisition%20from%20birth%22&resultType=core&format=json) followed six bilingual children (French-English, and French with Quebec Sign Language). It reports that both groups "achieved their early linguistic milestones" in each language at the same time, at a pace similar to monolingual children. The abstract was opened.
- Major later study: [Muszyńska et al. 2025, *Journal of Child Language*](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1017/S0305000924000655&resultType=core&format=json) compared 302 Polish bilingual children living abroad with 302 matched monolingual children. Parents reported milestones through an app. It found a similar trajectory, including for babbling, first words and first word combinations. The abstract was opened.
- Saer 1923 (the editorial's branch): the [Frontiers editorial](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.01346/full) cites it as early evidence of a mental delay in bilingual children compared with monolingual peers. The paper was not opened, so its status was not checked.

### Cold trails
- [habilnet, De Houwer & Pascall](https://www.habilnet.org/bilingual-children-do-not-start-speaking-later-than-monolingual-ones/), 2021 (date from: byline of the German original, April 2021): describes many professionals as convinced that bilingual children start speaking later. It names no origin for the belief and argues against it.
- [Babbel Magazine, Katrin Sperling](https://www.babbel.com/en/magazine/bilingual-parenting), 2022: gives the belief as "so they will start speaking later" and lists it as myth #1. It cites no origin for it and lists Oller 1997, Genesee 2003, Pearson 2004 and Petitto 2001 against it.

### Confidence
Medium: the root's Primary (Smith 1939) could not be opened and its date rests on *cited by*, and the business-magazine article your manager read could not be found, so its link to this chain is not established.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
