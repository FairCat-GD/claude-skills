---
case: non-interactive-goldfish-attention
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:17:09Z
cost_usd: 1.5175
duration_s: 159
turns: 36
error: none
---

## Tool calls

- Skill: provenance-tracer:provenance-tracer
- Read: <plugin>/skills/provenance-tracer/references/output-template.md
- Read: <plugin>/skills/provenance-tracer/references/search-playbook.md
- Read: <plugin>/skills/provenance-tracer/references/labels.md
- Read: <plugin>/skills/provenance-tracer/references/mutation-types.md
- ToolSearch: {"query":"select:WebSearch,WebFetch","max_results":2}
- WebSearch: "attention span" "shorter than a goldfish"
- WebSearch: humans 8 second attention span goldfish 9 seconds
- WebSearch: Microsoft Canada 2015 attention spans consumer insights report goldfish
- WebSearch: "8.25 seconds" attention span 2013 Statistic Brain
- WebSearch: origin of goldfish attention span statistic source
- WebSearch: goldfish attention span myth fact check BBC
- WebFetch: https://static1.squarespace.com/static/59bf2bf68fd4d28e59627113/t/5ab01bdff950b70546a08167/1521490918597/265348695-Microsoft-Attention-Spans-Research-Report.pdf
- WebFetch (error): https://www.bbc.com/news/health-38896790
- WebFetch: https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/
- WebFetch (error): http://news.bbc.co.uk/2/hi/science/nature/1834682.stm
- WebSearch: Ceros Inspire Littlefield goldfish attention span Guardian 2000
- WebFetch: https://time.com/3858309/attention-spans-goldfish/
- WebFetch: https://www.ceros.com/originals/no-dont-attention-span-goldfish/
- WebFetch: https://www.mangalam.nl/wp-content/uploads/2019/05/microsoft-attention-spans-research-report.pdf
- WebFetch (error): https://web.archive.org/web/2013/http://www.statisticbrain.com/attention-span-statistics/
- WebFetch: https://medium.com/psynamic/8-second-attention-spans-tracking-the-myth-that-just-wont-quit-614dd2cb9792
- WebFetch: https://scienceblog.com/t-humans-eight-second-attention-span-goldfish-myth/
- WebSearch: Guardian September 2000 web design goldfish attention span nine seconds
- WebFetch: https://www.business2community.com/brandviews/ceros/no-dont-attention-span-goldfish-01691470
- WebSearch: "goldfish are said to have an attention span of five seconds" Guardian
- WebSearch: BBC More or Less 2017 "Busting the attention span myth" Maybin
- Read (denied): <temp>/config/projects/-private-tmp-e-4vS5hz-home-cwd/345d1b7e-b425-43d2-a9fb-c37fba7c1095/tool-results/webfetch-1795771055153-86f63f.pdf
- WebFetch: https://www.swordandthescript.com/2022/02/goldfish-attention-span/
- WebFetch: https://www.marketplace.org/2014/02/11/business/goldfish-have-longer-attention-spans-americans-and-publishing-industry-knows-it
- WebFetch (error): https://www.statisticbrain.com/attention-span-statistics/
- WebFetch (error): https://news.nationalpost.com/news/canada/canadians-now-have-shorter-attention-span-than-goldfish-thanks-to-portable-devices-microsoft-study
- WebFetch: https://www.scribd.com/document/265348695/Microsoft-Attention-Spans-Research-Report
- WebFetch: https://www.linkedin.com/business/marketing/blog/content-marketing/the-great-goldfish-attention-span-myth-and-why-its-killing-cont

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Human attention span is now shorter than a goldfish's."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** *The Guardian*, article on web design, 13 September 2000 (not opened), 2000 (date from: cited by [*A Patchwork of Perceptions*, 2022](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 6

### Chain
Your version: "Human attention span is now shorter than a goldfish's" (where you met it: not given)
 └─ [TIME, *You Now Have a Shorter Attention Span Than a Goldfish*](https://time.com/3858309/attention-spans-goldfish/), 2015, Secondary → cites
     └─ [Microsoft Canada Consumer Insights, *Attention Spans*](https://www.scribd.com/document/265348695/Microsoft-Attention-Spans-Research-Report), 2015, Secondary. I opened only part of it; the pages with the figures did not come back. Per [Jason Miller, LinkedIn, 2016](https://www.linkedin.com/business/marketing/blog/content-marketing/the-great-goldfish-attention-span-myth-and-why-its-killing-cont), the infographic "wasn't actually based on findings from Microsoft's own research." → cites
         └─ [Statistic Brain, *Attention Span Statistics*](https://www.statisticbrain.com/attention-span-statistics/), date unknown, (not opened), per Jason Miller, LinkedIn, 2016 → cites
             └─ US National Center for Biotechnology Information and Associated Press, date unknown, (not opened), per [*Sword and the Script*, 2022](https://www.swordandthescript.com/2022/02/goldfish-attention-span/). That page quotes the BBC's 2017 investigation: "neither can find any record of research that backs up the stats." → stopped: not opened

 Side branch: a 2014 Marketplace radio segment with a Harvard academic citing the figures, (not opened: the fetch returned an empty page), per *Sword and the Script*, 2022 → stopped: not opened

 Earlier branch. No opened page links it to the 2015 chain:
 └─ [BBC News, 2002](http://news.bbc.co.uk/2/hi/science/nature/1834682.stm), 2002, (not opened), per *A Patchwork of Perceptions*, 2022. Its wording as that post quotes it: "an attention span of nine seconds – the same as a goldfish." It names an MIT researcher, and the post says following that name was a dead end. → stopped: not opened
 └─ *The Guardian*, web design article, 2000, (not opened), per *A Patchwork of Perceptions*, 2022. This is the root: the earliest instance found.

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | Visitors to websites and web browsing (2000 Guardian and 2002 BBC, as *A Patchwork of Perceptions* describes them) | "Human attention span" | [TIME](https://time.com/3858309/attention-spans-goldfish/), 2015: "people now generally lose concentration after eight seconds" |
| Comparison changed (equal → shorter) | Nine seconds, "the same as a goldfish" (2002 BBC, per *A Patchwork of Perceptions*) | "shorter than a goldfish's" | TIME, 2015: 8 seconds against the goldfish's 9 |
| Time trend added | No decline over time in either early version, as described | "is now shorter" | TIME, 2015: attention span "dropped from 12 seconds to eight seconds" since 2000 |

### Status of the root
- No primary found, so there was no status to check.
- Fact-check, as relayed by an opened source: BBC *More or Less* (Simon Maybin, 10 March 2017) contacted the sources Statistic Brain lists. Per *Sword and the Script*, neither the NCBI nor the Associated Press could find research behind the figures. The BBC page itself would not open.
- Jason Miller ([LinkedIn, 2016](https://www.linkedin.com/business/marketing/blog/content-marketing/the-great-goldfish-attention-span-myth-and-why-its-killing-cont)) says he searched Statistic Brain and found no mention of human or goldfish attention spans.

### Cold trails
None.

### Confidence
Low. Every node before TIME (2015) failed to open: the Guardian 2000 root, the BBC 2002 article, Statistic Brain, and the figure pages of the Microsoft report. The links and dates for those nodes rest on later pages that name them.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
