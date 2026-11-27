---
case: personal-chain-bilingual-speech
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:22:38Z
cost_usd: 1.3835
duration_s: 165
turns: 34
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
- WebSearch: bilingualism causes speech delay in children myth
- WebSearch: origin of belief bilingualism delays language development history research 1920s
- WebSearch: bilingual children first words age milestones study monolingual comparison
- WebSearch: "bilingual" "language delay" myth first appeared Saer 1923 Smith 1939
- WebSearch: fact check bilingual children talk later speech delay
- WebFetch: https://frontiersin.org/articles/10.3389/fpsyg.2019.01346/full
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC5214932/
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1986)%20-%20MIRROR%20OF%20LANGUAGE%20THE%20DEBATE%20ON%20BILINGUALISM.pdf
- WebFetch: https://www.cambridge.org/core/journals/journal-of-child-language/article/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers/0BFAB689DC70E5A2A5220976E1939948
- WebFetch: https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later
- WebFetch: https://www.semanticscholar.org/paper/THE-EFFECT-OF-BILINGUALISM-ON-INTELLIGENCE-Saer/fb24b3489d581ebb152c97fa93d2c747795d5d51
- WebFetch: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6168212/
- WebFetch: https://www.healthychildren.org/English/ages-stages/gradeschool/school/Pages/7-Myths-Facts-Bilingual-Children-Learning-Language.aspx
- WebFetch: https://ir.library.illinoisstate.edu/cgi/viewcontent.cgi?article=2291&context=etd
- WebFetch: https://files.eric.ed.gov/fulltext/ED226575.pdf
- WebFetch: https://www.speechtherapycentres.com/bilingual-children-and-speech-delays/
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/
- WebFetch: https://speechtherapycentres.com/bilingual-children-and-speech-delays/
- WebFetch (error): https://www.mindbrained.org/2021/08/bilingualism-benefits-early-late-or-never/
- WebFetch: https://api.crossref.org/works?query.bibliographic=Saer+1923+effect+of+bilingualism+on+intelligence&rows=2
- WebFetch: https://bpspsychub.onlinelibrary.wiley.com/doi/10.1111/j.2044-8295.1923.tb00110.x
- WebSearch: Madorah Smith 1939 "Some light on the problem of bilingualism" preschool Hawaii speech
- WebSearch: Pearson Fernández Oller 1993 "Lexical development in bilingual infants and toddlers" comparison to monolingual norms
- WebFetch: https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/
- WebFetch: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-1770.1993.tb00174.x

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches. Your manager's name and the magazine are not searched.
- Personal chain as you gave it: a manager told you, and they read it in a business magazine. The magazine's title and the year were not given, so I traced the claim from the web alone.

## Provenance: "Bilingual children start speaking later."

**Roots:** Independent · **Grounding:** No primary found · Mutated
**Earliest instance found:** [D. J. Saer, *The Effect of Bilingualism on Intelligence*, British Journal of Psychology](https://bpspsychub.onlinelibrary.wiley.com/doi/10.1111/j.2044-8295.1923.tb00110.x), 1923 (date from: [Crossref record](https://api.crossref.org/works?query.bibliographic=Saer+1923+effect+of+bilingualism+on+intelligence&rows=2), cited by Bright & Filippi 2019). Earlier instances may exist.
**Roots:** 2 · **Retellings found:** 7

### Chain
Your version: "Bilingual children start speaking later." (you heard it: from a manager (Hearsay), who read it in a business magazine, title and year not given; it matches no node because the magazine was not identified)
 ├─ [*Do Bilingual Children Start Speaking Later?*, amma.family](https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later), 2024, Tertiary. It calls the idea "one of the myths surrounding bilingualism" → cites
 │   └─ [Byers-Heinlein & Lew-Williams, *Bilingualism in the Early Years: What the Science Says*, Learning Landscapes](https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/), 2013, Secondary. Parents "feel that their child is behind due to their bilingualism" → cites
 │       └─ [Pearson, Fernández & Oller, *Lexical Development in Bilingual Infants and Toddlers*, Language Learning](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-1770.1993.tb00174.x), 1993, Primary (not opened, per Byers-Heinlein & Lew-Williams) → stopped: not opened
 ├─ [Bright & Filippi, *Editorial: Perspectives on the "Bilingual Advantage"*, Frontiers in Psychology](https://frontiersin.org/articles/10.3389/fpsyg.2019.01346/full), 2019, Secondary. It says the concern about delay "almost certainly derives in part from early evidence" → cites
 │   └─ [Saer, *The Effect of Bilingualism on Intelligence*](https://bpspsychub.onlinelibrary.wiley.com/doi/10.1111/j.2044-8295.1923.tb00110.x), 1923, root, Primary (not opened, per Bright & Filippi). It reported lower IQ-test scores for bilingual children in Wales. → stopped: not opened (403)
 └─ [*Madorah Elizabeth Smith 1884–*, A History of Speech-Language Pathology, University at Buffalo](https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/), date unknown, Secondary. Smith found two languages "contributed to a lag in speech development" → cites
     └─ M. E. Smith, *Some light on the problem of bilingualism…among preschool children of non-American ancestry in Hawaii*, Genetic Psychology Monographs 21(2), 1939, root, Primary (not opened, per the Buffalo page)

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Other: the outcome changed | Saer 1923: bilingual children scored lower on intelligence (IQ) tests, per Bright & Filippi | bilingual children start speaking later | [Bright & Filippi](https://frontiersin.org/articles/10.3389/fpsyg.2019.01346/full), 2019, which links a fear of delayed language learning to Saer's IQ study |
| Scope widened | Smith 1939: preschool children of non-American ancestry in Hawaii | bilingual children | your version |
| Context removed | Smith measured progress in English only, comparing poor immigrant children with middle-class native-born children (per the Buffalo page) | start speaking later, in general | your version |
| Other: what was measured changed | Smith: a lag in mastering English speech | the age at which children start speaking | your version |

### Status of the root
- Saer 1923: the [Crossref record](https://api.crossref.org/works?query.bibliographic=Saer+1923+effect+of+bilingualism+on+intelligence&rows=2) has no update, retraction or correction entries. The publisher's page could not be opened (403), and Retraction Watch and PubPeer were not checked.
- Smith 1939: no DOI or publisher page was found, so its status was not checked. The [Buffalo page](https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/) says her studies "were later found to be methodologically flawed".
- Major later study: [Muszyńska et al., *Bilingual children reach early language milestones at the same age as monolingual peers*, Journal of Child Language](https://www.cambridge.org/core/journals/journal-of-child-language/article/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers/0BFAB689DC70E5A2A5220976E1939948), published online January 2025. It drew on parent-app data for 2,357 children aged 0–24 months, 302 of them bilingual. It found no significant difference in the age of babbling, the first word, the 10th word or the first multiword utterance. It concludes that "typical bilingual development follows a trajectory similar to monolingual development."
- Major later study: Pearson, Fernández & Oller 1993 (not opened). [Byers-Heinlein & Lew-Williams](https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/) cite it for the finding that a bilingual child's lag disappears once words are counted across both languages.
- Professional bodies: the [AAP/ASHA page on HealthyChildren.org](https://www.healthychildren.org/English/ages-stages/gradeschool/school/Pages/7-Myths-Facts-Bilingual-Children-Learning-Language.aspx) says "Speech or language problems are not caused by learning multiple languages."

### Cold trails
None.

### Confidence
Medium: neither root study could be opened (the 1923 and 1939 studies are known only through later pages), and the business magazine was never identified, so the last link to your version is missing.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
