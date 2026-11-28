---
case: echoed-statistic-goldfish-attention
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:25:29Z
cost_usd: 1.6501
duration_s: 174
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
- WebSearch: "attention span" "shorter than a goldfish"
- WebSearch: humans 8 second attention span goldfish 9 seconds
- WebSearch: Microsoft Canada 2015 attention spans report goldfish
- WebSearch: "8.25 seconds" attention span Statistic Brain
- WebSearch: origin of goldfish attention span statistic source
- WebSearch: goldfish attention span myth fact check BBC
- WebFetch: https://static1.squarespace.com/static/59bf2bf68fd4d28e59627113/t/5ab01bdff950b70546a08167/1521490918597/265348695-Microsoft-Attention-Spans-Research-Report.pdf
- WebFetch (error): https://www.bbc.com/news/health-38896790
- WebFetch: https://medium.com/psynamic/8-second-attention-spans-tracking-the-myth-that-just-wont-quit-614dd2cb9792
- WebFetch: https://time.com/3858309/attention-spans-goldfish/
- WebFetch: https://www.mangalam.nl/wp-content/uploads/2019/05/microsoft-attention-spans-research-report.pdf
- WebFetch (error): https://www.bbc.co.uk/news/health-38896790
- WebFetch (error): https://web.archive.org/web/2013/http://www.statisticbrain.com/attention-span-statistics/
- WebSearch: "Microsoft Attention Spans Research Report" pdf "Statistic brain" goldfish 2000 2013
- WebFetch: https://scienceblog.com/t-humans-eight-second-attention-span-goldfish-myth/
- WebFetch: https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/
- WebFetch (error): http://news.bbc.co.uk/2/hi/science/nature/1834682.stm
- WebFetch: https://www.usecarly.com/blog/attention-span-statistics/
- WebSearch: Andrew Littlefield attention span goldfish myth Guardian 2000 earliest
- WebFetch: https://www.ceros.com/originals/no-dont-attention-span-goldfish/
- WebSearch: theguardian.com 2000 web design goldfish attention span nine seconds
- WebSearch: "microsoft-attention-spans-research-report.pdf"
- WebFetch: https://www.csoonline.com/article/551475/microsoft-goldfish-have-higher-attention-spans-than-we-do-thanks-to-digital-lifestyles.html
- WebFetch: https://pr.motamem.org/microsoft-attention-spans-research-report.pdf
- Read (denied): <temp>/config/projects/-private-tmp-e-Qkph2a-home-cwd/3f23d406-5526-4dfd-ad69-eeb91214ad17/tool-results/webfetch-1795825630180-0wqbk9.pdf
- WebFetch: https://www.slideshare.net/slideshow/microsoft-attentionspansresearchreport/76370927
- WebFetch (error): https://www.statisticbrain.com/attention-span-statistics/

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Human attention span is now shorter than a goldfish's"

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** [BBC News](http://news.bbc.co.uk/2/hi/science/nature/1834682.stm), 2002 (date from: cited by [A Patchwork of Perceptions](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 7

### Chain
Your version: "Human attention span is now shorter than a goldfish's" (where you met it: not given)
 ├─ [Time, *You Now Have a Shorter Attention Span Than a Goldfish*](https://time.com/3858309/attention-spans-goldfish/), 2015, Tertiary: "people now generally lose concentration after eight seconds" → cites
 │   └─ [Microsoft Canada, *Attention spans*](https://www.slideshare.net/slideshow/microsoft-attentionspansresearchreport/76370927), 2015, Tertiary: slide 6 gives 12 s (2000), 8 s (2013), goldfish 9 s, "Source: Statistic brain" → cites
 │       └─ Statistic Brain, *Attention Span Statistics*, 2012 (date from: archive capture, per [usecarly](https://www.usecarly.com/blog/attention-span-statistics/)), (not opened), per usecarly → cites
 │           └─ The Associated Press; National Center for Biotechnology Information / U.S. National Library of Medicine, date unknown, (not opened), per usecarly → stopped: not opened
 ├─ [CSO Online, *Microsoft: Goldfish have higher attention spans than we do…*](https://www.csoonline.com/article/551475/microsoft-goldfish-have-higher-attention-spans-than-we-do-thanks-to-digital-lifestyles.html), 2015, Tertiary: "1 second shorter than a goldfish!" → cites the Microsoft Canada report (above)
 └─ [A Patchwork of Perceptions, *Goldfish and Us*](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/), 2022, Tertiary: quotes the 2002 BBC wording, "an attention span of nine seconds – the same as a goldfish" → cites
     └─ [BBC News](http://news.bbc.co.uk/2/hi/science/nature/1834682.stm), 2002, (not opened), per A Patchwork of Perceptions, Tertiary, root

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Number changed | web browsing can leave a person with a nine-second span, *the same as* a goldfish | Human attention span is now shorter than a goldfish's | [Microsoft Canada, *Attention spans*](https://www.slideshare.net/slideshow/microsoft-attentionspansresearchreport/76370927), 2015 |
| Context removed | ties the short span to the addictive nature of web browsing | Human attention span is now shorter than a goldfish's | [Microsoft Canada, *Attention spans*](https://www.slideshare.net/slideshow/microsoft-attentionspansresearchreport/76370927), 2015 |

### Status of the root
- No primary found, so there was no status to check.
- Microsoft Canada report: its own research was an online survey of 2,000 Canadians and EEG recordings of 112 people, both run in late 2014. It does not present the 8-second figure as one of its own results, and its foreword argues that digital media is not killing attention spans ([slideshare copy](https://www.slideshare.net/slideshow/microsoft-attentionspansresearchreport/76370927)).
- Statistic Brain: a February 2012 archive capture gave 8 seconds for 2012 and cited only The Associated Press. A March 2015 capture moved the figure to 2013 and added NCBI and the U.S. National Library of Medicine as sources ([usecarly](https://www.usecarly.com/blog/attention-span-statistics/), describing the archive captures).
- Statistic Brain's listed sources: according to [A Patchwork of Perceptions](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/), BBC journalist Simon Maybin found in 2017 that none of them had any record of the research. I could not open the BBC's own 2017 article.

### Cold trails
None.

### Confidence
Low: the fetch tool could not open the 2002 BBC root, the Statistic Brain page or its archive captures, or the BBC's 2017 investigation, so the earliest links rest on what later retellings say about them. A September 2000 *Guardian* web-design article, named second-hand as an even earlier goldfish comparison, was never found.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
