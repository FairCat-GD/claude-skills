---
case: personal-chain-bilingual-speech
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T19:12:45Z
cost_usd: 1.5664
duration_s: 195
turns: 33
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
- WebSearch: bilingualism causes language delay children talk later
- WebSearch: origin of the myth that bilingualism delays speech history Saer 1923
- WebSearch: bilingual children first words age study monolingual comparison Petitto Pearson
- WebSearch: where did the idea bilingual children speak late come from earliest research
- WebSearch: fact check bilingual children speech delay
- WebFetch: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.01346/full
- WebFetch: https://lucianabrentano.com.br/wp-content/uploads/2019/12/Antoniou-2018.pdf
- WebFetch: https://littlewords.ai/blog/bilingual-children-speech-delay-myth
- WebSearch: Madorah Smith 1939 bilingual preschool children Hawaii speech vocabulary retardation
- WebFetch: https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1986)%20-%20MIRROR%20OF%20LANGUAGE%20THE%20DEBATE%20ON%20BILINGUALISM.pdf
- WebFetch: https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22Lexical%20development%20in%20bilingual%20infants%20and%20toddlers%22&resultType=core&format=json
- WebFetch: https://api.crossref.org/works?query.bibliographic=Lexical+development+in+bilingual+infants+and+toddlers+comparison+to+monolingual+norms+Pearson&rows=2
- WebFetch: https://web.stanford.edu/~hakuta/www/research/publications/(1987)%20-%20BILINGUALISM%20AND%20COGNITIVE%20DEVELOPMENT%20THREE%20PERSPE.pdf
- WebFetch: https://www.cambridge.org/core/journals/journal-of-child-language/article/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers/0BFAB689DC70E5A2A5220976E1939948
- WebSearch: "Some light on the problem of bilingualism" Smith 1939 "retardation in speech" "two languages"
- WebFetch: https://api.crossref.org/works?query.bibliographic=Saer+1923+The+effect+of+bilingualism+on+intelligence&rows=2
- WebFetch: https://files.eric.ed.gov/fulltext/ED273152.pdf
- WebFetch: https://commons.und.edu/cgi/viewcontent.cgi?article=10630&context=theses
- WebFetch: https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/
- WebFetch: https://www.levyinstitute.org/pubs/wp/229.pdf
- WebFetch (error): https://web.archive.org/cdx/search/cdx?url=acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html&limit=1
- WebFetch: https://sites.google.com/view/multicsd/multilingualism-multiculturalism/working-with-cld-clients/pediatrics/myths-surrounding-language-development-treatment-in-bilingual-children

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- Personal chain as you gave it: your manager (Hearsay), who read it in a business magazine you didn't name. I didn't search for the magazine, and the year isn't given.

## Provenance: "Bilingual children start speaking later."

**Roots:** Independent · **Grounding:** Primary differs · Mutated
**Earliest instance found:** Madorah Smith's 1939 study of preschool children in Hawaii (not opened), 1939 (date from: cited by the [Duchan history page](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html)). Earlier instances may exist.
**Roots:** 2 · **Retellings found:** 7

### Chain
Your version: "Bilingual children start speaking later." (you heard it: from your manager (Hearsay), who read it in a business magazine; year not given; matches no node found)
 ├─ [Bright & Filippi, *Editorial: Perspectives on the 'Bilingual Advantage'*, Frontiers in Psychology](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.01346/full), 2019, Secondary → cites
 │   └─ Saer, *The effect of bilingualism on intelligence*, British Journal of Psychology 14, 1923, Primary (not opened, per Frontiers editorial), root 2
 ├─ [Duchan, *A History of Speech-Language Pathology*, page on Madorah Smith](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html), date unknown, Secondary → cites
 │   └─ Smith, *Some light on the problem of bilingualism…*, Genetic Psychology Monographs 21, 1939, Primary (not opened, per Duchan page), root 1
 └─ [Little Words, *The bilingual speech delay myth*](https://littlewords.ai/blog/bilingual-children-speech-delay-myth), date unknown, Secondary → credits Pearson, Fernández & Oller 1993
     └─ [Pearson, Fernández & Oller, *Lexical Development in Bilingual Infants and Toddlers*, Language Learning 43(1)](https://api.crossref.org/works?query.bibliographic=Lexical+development+in+bilingual+infants+and+toddlers+comparison+to+monolingual+norms+Pearson&rows=2), 1993, Primary (credited, differs)

How the branches got there:
- **Saer (1923)** compared Welsh–English bilingual children with English monolinguals on IQ tests. The Frontiers editorial says today's worry about language delay comes partly from evidence like this.
- **Smith (1939)** is the earliest source found that ties two languages to *speech* specifically.
- **Little Words** says the modern belief comes from misreading vocabulary counts that look at one language at a time. It points to Pearson et al. (1993), which itself reports no slower vocabulary growth.

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | Smith studied preschool children of immigrant ancestry in 1930s Hawaii (root 1) | Bilingual children start speaking later. | [Frontiers editorial](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.01346/full), 2019 |
| Context removed (comparison group dropped) | Smith measured the Hawaii children against norms she had built from Iowa monolinguals (root 1) | Bilingual children start speaking later. | [Frontiers editorial](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.01346/full), 2019 |
| Hedge dropped | ["simultaneous use of two languages contributed to a lag in speech development"](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html) (root 1, one contributing factor) | Bilingual children start speaking later. | [MultiCSD myths page](https://sites.google.com/view/multicsd/multilingualism-multiceulturalism/working-with-cld-clients/pediatrics/myths-surrounding-language-development-treatment-in-bilingual-children), date unknown |
| Other: outcome changed | Saer reported lower scores on intelligence and reasoning tests, not later speech (root 2) | Bilingual children start speaking later. | [Frontiers editorial](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.01346/full), 2019 |

### Status of the root
- Smith 1939: the [Duchan page](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html) says her studies were later found to be methodologically flawed. She compared poor immigrant children with middle-class native-born children, and she didn't separate fluent bilinguals from children who spoke one language poorly. The page doesn't say who made this critique. I found no retraction notice for a 1939 monograph, and Retraction Watch and PubPeer were not checked.
- Saer 1923: its [Crossref record](https://api.crossref.org/works?query.bibliographic=Saer+1923+The+effect+of+bilingualism+on+intelligence&rows=2) lists no retraction or correction. The journal page, Retraction Watch and PubPeer were not checked.
- Major later study: [Muszyńska et al., *Journal of Child Language*](https://www.cambridge.org/core/journals/journal-of-child-language/article/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers/0BFAB689DC70E5A2A5220976E1939948), published online 2025, compared 302 Polish bilingual children with 302 matched monolinguals. It found no significant difference in the age of first words and concluded that ["typical bilingual development follows a trajectory similar to monolingual development."](https://www.cambridge.org/core/journals/journal-of-child-language/article/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers/0BFAB689DC70E5A2A5220976E1939948)
- Pearson, Fernández & Oller 1993 (the credited text): the abstract compares 25 bilingual and 35 monolingual children aged 8 to 30 months. It found ["no statistical basis for concluding that the bilingual children were slower"](https://api.crossref.org/works?query.bibliographic=Lexical+development+in+bilingual+infants+and+toddlers+comparison+to+monolingual+norms+Pearson&rows=2) at building early vocabulary. Crossref lists no updates to it.

### Cold trails
- [Amma, *Do Bilingual Children Start Speaking Later?*](https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later), 2024: raises the claim as a question and cites no source for it (its sources are for its own answer, which is no).
- [MultiCSD, *Myths Surrounding Language Development & Treatment in Bilingual Children*](https://sites.google.com/view/multicsd/multilingualism-multiculturalism/working-with-cld-clients/pediatrics/myths-surrounding-language-development-treatment-in-bilingual-children), date unknown: says the belief comes from past research that judged bilinguals by monolingual standards, but names none of those studies.

### Confidence
Medium. Neither root (Saer 1923, Smith 1939) could be opened, so both are known only from the pages that cite them, and Smith's date rests on *cited by*.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
