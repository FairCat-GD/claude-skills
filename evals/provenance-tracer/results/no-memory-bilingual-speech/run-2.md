---
case: no-memory-bilingual-speech
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T15:38:15Z
cost_usd: 1.8267
duration_s: 231
turns: 38
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
- WebSearch: Pearson Fernández Oller 1993 bilingual toddlers vocabulary first words
- WebSearch: origin of belief bilingualism delays speech history Saer 1923 "language handicap"
- WebSearch: bilingual children first words age milestones same as monolingual study
- WebSearch: fact check "bilingual" children "speech delay" myth ASHA
- WebFetch: https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/
- WebFetch: https://files.eric.ed.gov/fulltext/ED283368.pdf
- WebFetch: https://commons.und.edu/cgi/viewcontent.cgi?article=10630&context=theses
- WebFetch: https://europepmc.org/article/PMC/PMC6168212
- WebFetch: https://www.healthychildren.org/English/ages-stages/gradeschool/school/Pages/7-Myths-Facts-Bilingual-Children-Learning-Language.aspx
- WebFetch: https://files.eric.ed.gov/fulltext/ED226575.pdf
- WebFetch: https://library.scottbarrykaufman.com/uploads/2012/10/Bialystok-in-press.pdf
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6168212/fullTextXML
- WebSearch: Madorah Smith 1939 bilingualism Hawaii preschool children retarded speech development
- WebFetch: https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1986)%20-%20MIRROR%20OF%20LANGUAGE%20THE%20DEBATE%20ON%20BILINGUALISM.pdf
- WebSearch: bilingual delay myth history Madorah Smith Saer early twentieth century research origin "bilingual children" talk later
- WebFetch: https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay
- WebFetch: https://www.cambridge.org/core/journals/journal-of-child-language/article/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers/0BFAB689DC70E5A2A5220976E1939948
- WebSearch: Frontiers editorial "Perspectives on the 'Bilingual Advantage'" Challenges and Opportunities 2019
- WebFetch: https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/
- WebFetch: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.01346/full
- WebFetch: https://api.crossref.org/works?query.bibliographic=Saer+1923+effect+of+bilingualism+on+intelligence&rows=2
- WebSearch: Smith 1939 "Some light on the problem of bilingualism" Genetic Psychology Monographs archive.org full text
- WebFetch: https://speechtherapycentres.com/bilingual-children-and-speech-delays/
- WebFetch: https://onlinelibrary.wiley.com/doi/10.1111/j.2044-8295.1923.tb00110.x
- WebFetch: https://www.greatspeech.com/is-it-normal-for-bilingual-children-to-have-speech-delays/
- WebFetch: https://link.springer.com/chapter/10.1007/978-3-030-87063-8_2

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Bilingual children start speaking later than children who learn one language."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** [Madorah E. Smith, *Some Light on the Problem of Bilingualism…*, Genetic Psychology Monographs 21](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html), 1939 (date from: cited by Judy Duchan's *History of Speech-Language Pathology*). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 8

### Chain
Your version: "Bilingual children start speaking later." (where you met it: not given)
 ├─ [amma parenting blog, *Do bilingual children start speaking later?*](https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later), 2024, Tertiary → cites
 │   └─ Byers-Heinlein & Lew-Williams, *Bilingualism in the Early Years: What the Science Says*, Learning Landscapes, 2013, (not opened), per amma → stopped: not opened
 ├─ [Great Speech, *Is It Normal for Bilingual Children to Have Speech Delays?*](https://www.greatspeech.com/is-it-normal-for-bilingual-children-to-have-speech-delays/), 2025, Tertiary → cites
 │   ├─ Byers-Heinlein & Lew-Williams, 2013, (not opened), per Great Speech: the same node as above
 │   └─ [HealthyChildren.org (AAP and ASHA), *7 Myths and Facts About Bilingual Children Learning Language*](https://www.healthychildren.org/English/ages-stages/gradeschool/school/Pages/7-Myths-Facts-Bilingual-Children-Learning-Language.aspx), 2024, Tertiary → cites
 │       └─ ASHA, *Learning More Than One Language*, date unknown, (not opened), per HealthyChildren.org → stopped: not opened
 ├─ [Nationwide Children's Hospital, *Teaching Kids a Second Language: Can It Cause a Speech Delay?*](https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay), 2017, Tertiary: cites nothing (cold trail)
 ├─ [Bright & Filippi, *Editorial: Perspectives on the 'Bilingual Advantage'*, Frontiers in Psychology](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.01346/full), 2019, Secondary → credits D. J. Saer
 │   └─ [Saer, *The Effect of Bilingualism on Intelligence*, British Journal of Psychology 14](https://onlinelibrary.wiley.com/doi/10.1111/j.2044-8295.1923.tb00110.x), 1923, Primary (not opened, per Bright & Filippi) → stopped: not opened (paywalled; per the editorial it reported lower IQ scores, not later speech)
 └─ [Judy Duchan, *A History of Speech-Language Pathology*: Madorah Smith](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html), date unknown, Secondary → cites
     └─ Smith, *Some Light on the Problem of Bilingualism as Found from a Study of the Progress in Mastery of English among Preschool Children of Non-American Ancestry in Hawaii*, Genetic Psychology Monographs 21, 1939, Primary (not opened, per Duchan), root

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | Smith studied preschoolers aged 2 to 6 in Hawaii, from Chinese, Filipino, Hawaiian, Japanese, Korean and Portuguese families (per Duchan) | Bilingual children start speaking later. | [Nationwide Children's Hospital](https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay), 2017 |
| Hedge dropped | [Smith concluded the "simultaneous use of two languages contributed to a lag in speech development"](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html) (Duchan's summary): bilingualism as one *contributing* factor, not the whole cause | Bilingual children start speaking later. | [Nationwide Children's Hospital](https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay), 2017 |
| Context removed | Smith compared poor immigrant children with norms from middle-class, native-born American children, and did not separate fluent bilinguals from children with weak command of a language (per Duchan) | Bilingual children start speaking later. | [Nationwide Children's Hospital](https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay), 2017 |
| Other: what was measured changed | Smith measured how far children had progressed in mastering English, using speech samples, not when they began to talk | Bilingual children start speaking later. | [amma parenting blog](https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later), 2024 |

### Status of the root
- Smith (1939) has no DOI that I found, and its full text was not opened, so the journal-page, Crossref, Retraction Watch and PubPeer checks were not run for it.
- Duchan's history page says Smith's widely cited studies were later found to have flawed methods (the mismatched comparison groups described above). The page does not say who reached that finding: [Duchan](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html).
- Later study: Muszyńska et al. (2025) followed 302 Polish bilingual and 302 Polish monolingual children, matched on several factors, using parent reports. It found no significant difference in the age of babbling, first word, 10th word or first multiword utterance: [*Journal of Child Language*, DOI 10.1017/S0305000924000655](https://www.cambridge.org/core/journals/journal-of-child-language/article/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers/0BFAB689DC70E5A2A5220976E1939948).
- Saer (1923): the Crossref record lists no retraction, correction or other update: [Crossref](https://api.crossref.org/works?query.bibliographic=Saer+1923+effect+of+bilingualism+on+intelligence&rows=2).

### Cold trails
- [Nationwide Children's Hospital](https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay), 2017: calls the idea a long-standing US myth and cites no source for the belief or for its own counter-claim.

### Confidence
Medium. The root (Smith 1939) and Saer (1923) were not opened: Smith's monograph had no online copy I could find, Saer's was paywalled, and several scanned PDFs (Hakuta's *Mirror of Language* and two ERIC reviews) returned no readable text, so Smith's year and conclusion rest on Duchan's page, which is cited by.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
