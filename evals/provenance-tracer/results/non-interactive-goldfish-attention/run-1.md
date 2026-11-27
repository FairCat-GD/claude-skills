---
case: non-interactive-goldfish-attention
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:14:29Z
cost_usd: 1.6529
duration_s: 211
turns: 40
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
- WebSearch: humans have 8 second attention span goldfish 9 seconds
- WebSearch: Microsoft Canada 2015 attention spans consumer insights report goldfish
- WebSearch: "8.25 seconds" attention span Statistic Brain
- WebSearch: origin of goldfish attention span statistic source
- WebSearch: goldfish attention span claim fact check BBC More or Less
- WebFetch: https://static1.squarespace.com/static/59bf2bf68fd4d28e59627113/t/5ab01bdff950b70546a08167/1521490918597/265348695-Microsoft-Attention-Spans-Research-Report.pdf
- WebFetch (error): https://www.bbc.com/news/health-38896790
- WebFetch: https://medium.com/psynamic/8-second-attention-spans-tracking-the-myth-that-just-wont-quit-614dd2cb9792
- Read (denied): <temp>/config/projects/-private-tmp-e-2lywoM-home-cwd/f54b3881-ca78-4c88-8a9f-40c39d99d8f6/tool-results/webfetch-1795770893545-fyqbh3.pdf
- WebFetch: https://www.mangalam.nl/wp-content/uploads/2019/05/microsoft-attention-spans-research-report.pdf
- WebFetch: https://scienceblog.com/t-humans-eight-second-attention-span-goldfish-myth/
- WebFetch: https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/
- WebFetch (error): https://web.archive.org/web/2015/http://www.statisticbrain.com/attention-span-statistics/
- WebFetch: https://time.com/3858309/attention-spans-goldfish/
- WebFetch (error): http://news.bbc.co.uk/2/hi/science/nature/1834682.stm
- WebFetch (error): https://dl.motamem.org/microsoft-attention-spans-research-report.pdf
- WebFetch (error): https://www.statisticbrain.com/attention-span-statistics/
- WebSearch: Andrew Littlefield Ceros goldfish attention span Guardian 2000
- WebFetch: https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/
- WebFetch: https://www.warc.com/newsandopinion/opinion/the-goldfish-myth/en-gb/2806
- WebFetch: https://www.ceros.com/originals/no-dont-attention-span-goldfish/
- WebSearch: Guardian September 2000 web design goldfish attention span nine seconds
- WebFetch: https://www.business2community.com/brandviews/ceros/no-dont-attention-span-goldfish-01691470
- WebFetch: https://internet.psych.wisc.edu/wp-content/uploads/532-Master/532-UnitPages/Unit-09/Goldfish_MythBusting.pdf
- WebSearch: "Goldfish are said to have an attention span of five seconds"
- WebFetch: https://www.arrowsmithpress.com/journal/attention-goldfish
- WebSearch: theguardian.com 2000 "two seconds longer than a visitor to your website" goldfish
- WebFetch (error): https://www.nytimes.com/2016/01/22/opinion/the-eight-second-attention-span.html
- WebFetch: https://annejanzer.com/shrinking-reader-attention-span/
- WebFetch: http://advertising.microsoft.com/en/cl/31966/how-does-digital-affect-canadian-attention-spans
- WebFetch: https://about.ads.microsoft.com/en/cl/31966/how-does-digital-affect-canadian-attention-spans

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Human attention span is now shorter than a goldfish's."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** a web-design article in *The Guardian*, 2000 (date from: cited by [A Patchwork of Perceptions](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 10

### Chain
Your version: "Human attention span is now shorter than a goldfish's" (where you met it: not given)
 ├─ [Kevin McSpadden, *You Now Have a Shorter Attention Span Than a Goldfish*, TIME](https://time.com/3858309/attention-spans-goldfish/), 2015, Secondary → cites
 │   └─ [Microsoft Canada Consumer Insights, *Attention Spans*](https://static1.squarespace.com/static/59bf2bf68fd4d28e59627113/t/5ab01bdff950b70546a08167/1521490918597/265348695-Microsoft-Attention-Spans-Research-Report.pdf), 2015, Primary (not opened, per TIME; the fetch returned unreadable PDF data) → cites
 │       └─ [Statistic Brain, *Attention Span Statistics*](https://www.statisticbrain.com/attention-span-statistics/), date unknown, (not opened), per A Patchwork of Perceptions → stopped: not opened
 ├─ [Michael Brenner, *Thanks social media – our attention span is now shorter than a goldfish*, Marketing Insider Group](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/), 2014, Tertiary → cites Statistic Brain without a link (the same node as above) → stopped: not opened
 ├─ [Dan Hunter, *The Attention of a Goldfish*, Arrowsmith Press](https://www.arrowsmithpress.com/journal/attention-goldfish), date unknown, Secondary → cites the Microsoft Canada report (the same node as above) → stopped: not opened
 └─ [*Goldfish and Us: Unsubstantiated Claims About the Human Attention Span*, A Patchwork of Perceptions](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/), 2022, Secondary → cites
     ├─ [Timothy Egan, *The Eight-Second Attention Span*, The New York Times](https://www.nytimes.com/2016/01/22/opinion/the-eight-second-attention-span.html), 2016, (not opened), per A Patchwork of Perceptions → stopped: not opened
     ├─ [Simon Maybin, *Busting the attention span myth*, BBC News](https://www.bbc.com/news/health-38896790), 2017, (not opened), per A Patchwork of Perceptions → stopped: not opened
     ├─ [BBC News article on web browsing](http://news.bbc.co.uk/2/hi/science/nature/1834682.stm), 2002, (not opened), per A Patchwork of Perceptions → stopped: not opened
     └─ a web-design article in *The Guardian*, 2000, (not opened), per A Patchwork of Perceptions; earliest instance found, root

The 2000 and 2002 articles are linked to the Microsoft/Statistic Brain branch only by being earlier. No opened page shows that Statistic Brain drew on them.

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Hedge dropped | per A Patchwork of Perceptions, the 2002 BBC piece was the first to state the goldfish comparison as fact. That implies the 2000 Guardian article did not (neither article was opened). | Human attention span is now shorter than a goldfish's | BBC News, 2002 (not opened, per A Patchwork of Perceptions) |
| Number changed | 2002 version: [“attention span of nine seconds – the same as a goldfish”](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/), equal to the goldfish | shorter than a goldfish's (8 seconds against 9 in the later retellings) | [Marketing Insider Group](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/), 2014 |
| Scope widened | 2002 version: web browsing *can leave you* with that span, as an effect on web users | Human attention span is now shorter… (all humans, as a general measure) | [Marketing Insider Group](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/), 2014, which writes that [“attention span was now shorter than a goldfish”](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/) |
| Other: figure credited to research that did not produce it | per A Patchwork of Perceptions, the Microsoft report's own survey and EEG study did not measure attention span in seconds, and its chart credits Statistic Brain | widely retold as a Microsoft study's finding, e.g. TIME credits the human figure to the Microsoft study | [TIME](https://time.com/3858309/attention-spans-goldfish/), 2015 |

### Status of the root
- No primary found, so there was no status to check.
- Statistic Brain: per [A Patchwork of Perceptions](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/), Simon Maybin's 2017 BBC News investigation found no record of the research at the bodies Statistic Brain cited (the National Center for Biotechnology Information, the U.S. National Library of Medicine and the Associated Press).
- Microsoft Canada, *Attention Spans*: per [Anne Janzer](https://annejanzer.com/shrinking-reader-attention-span/), the report's data came from a self-reported survey of 2,000 Canadians and an EEG study of about 110 people. She says none of the goldfish-chart figures came from that research.
- On the goldfish figure: [TIME](https://time.com/3858309/attention-spans-goldfish/) gives no source for the 9-second number, and no opened page names a study that measured it.

### Cold trails
None.

### Confidence
Low: every node before 2014, along with the Microsoft report and Statistic Brain, failed to open (unreadable PDF, dead site, blocked BBC, NYT and archive fetches), so the chain stops short of any node known to cite nothing.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
