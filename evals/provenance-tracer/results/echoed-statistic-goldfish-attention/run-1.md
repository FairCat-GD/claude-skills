---
case: echoed-statistic-goldfish-attention
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T15:34:25Z
cost_usd: 1.9855
duration_s: 227
turns: 41
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
- WebSearch: Microsoft Canada 2015 attention spans report goldfish
- WebSearch: "8.25 seconds" attention span Statistic Brain source
- WebSearch: origin of goldfish attention span statistic
- WebSearch: goldfish attention span myth fact check BBC More or Less
- WebFetch: https://static1.squarespace.com/static/59bf2bf68fd4d28e59627113/t/5ab01bdff950b70546a08167/1521490918597/265348695-Microsoft-Attention-Spans-Research-Report.pdf
- WebFetch (error): https://www.bbc.com/news/health-38896790
- WebFetch: https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/
- WebFetch (error): https://web.archive.org/cdx/search/cdx?url=statisticbrain.com/attention-span-statistics/&limit=5
- Read (denied): <temp>/config/projects/-private-tmp-e-Ob6fyg-home-cwd/cb706a21-e4a1-4eb5-8551-545ba627a9bf/tool-results/webfetch-1795793689072-it095w.pdf
- WebFetch: https://time.com/3858309/attention-spans-goldfish/
- WebFetch: https://medium.com/psynamic/8-second-attention-spans-tracking-the-myth-that-just-wont-quit-614dd2cb9792
- WebFetch: https://www.mangalam.nl/wp-content/uploads/2019/05/microsoft-attention-spans-research-report.pdf
- WebSearch: "attention span" goldfish "8 seconds" 2013 OR 2014 statisticbrain
- WebFetch (error): https://www.statisticbrain.com/attention-span-statistics/
- WebFetch (error): https://dl.motamem.org/microsoft-attention-spans-research-report.pdf
- WebFetch (error): https://www.bbc.co.uk/news/health-38896790
- WebFetch: https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/
- WebFetch (error): http://news.bbc.co.uk/2/hi/science/nature/1834682.stm
- WebSearch: Andrew Littlefield Ceros goldfish attention span myth Guardian 2000
- WebFetch: https://www.ceros.com/originals/no-dont-attention-span-goldfish/
- WebSearch: Guardian September 2000 web design goldfish attention span nine seconds
- WebFetch: https://www.business2community.com/brandviews/ceros/no-dont-attention-span-goldfish-01691470
- WebSearch: "Goldfish are said to have an attention span of five seconds" guardian
- WebSearch: "attention span of nine seconds" goldfish BBC 2002 web browsing addictive
- WebFetch: http://joyfulpublicspeaking.blogspot.com/2014/11/does-it-take-9-90-or-900-seconds-to.html
- WebSearch: theguardian.com 2000 web design goldfish "attention span of five seconds" visitor website
- WebSearch: "Microsoft Attention Spans" "Spring 2015" pdf consumer insights
- WebFetch: https://pdfcoffee.com/microsoft-attention-spans-research-report-pdf-free.html
- WebFetch: https://pr.motamem.org/microsoft-attention-spans-research-report.pdf
- WebFetch: https://slideshare.net/sriushtiimx/microsoft-attentionspansresearchreport
- WebFetch (error): https://archive.ph/newest/http://www.statisticbrain.com/attention-span-statistics/

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Human attention span is now shorter than a goldfish's."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** a web-design article in *The Guardian*, 2000 (date from: cited by [Drumm, *Goldfish and Us*, 2022](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/), which reports Andrew Littlefield's search for the earliest mention). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 8

### Chain
Your version: "Human attention span is now shorter than a goldfish's" (where you met it: not given)
 ├─ [Time, *You Now Have a Shorter Attention Span Than a Goldfish*](https://time.com/3858309/attention-spans-goldfish/), 2015, Tertiary → cites
 │   └─ [Microsoft Canada Consumer Insights, *Attention spans*, Spring 2015 (SlideShare copy)](https://slideshare.net/sriushtiimx/microsoft-attentionspansresearchreport), 2015, Tertiary → cites
 │       └─ Statistic Brain, *Attention Span Statistics*, date unknown, (not opened), per [Drumm 2022](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/), Secondary → cites
 │           └─ National Center for Biotechnology Information / U.S. National Library of Medicine, and the Associated Press, date unknown, Primary (not opened, per [Drumm 2022](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/)) → stopped: not opened
 ├─ [Marketing Insider Group, *Human Attention Span vs. Goldfish: Myth Busted*](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/), 2022 (the page says it was first published in 2014), Tertiary → cites Statistic Brain (the node above)
 ├─ Sally Hogshead, *Fascinate*, p. 58, 2010, (not opened), per [Garber, *Joyful Public Speaking*, 2014](http://joyfulpublicspeaking.blogspot.com/2014/11/does-it-take-9-90-or-900-seconds-to.html), Tertiary → cites
 │   └─ [BBC News, *Turning into digital goldfish*, 22 Feb 2002](http://news.bbc.co.uk/2/hi/science/nature/1834682.stm), 2002, (not opened), per [Garber 2014](http://joyfulpublicspeaking.blogspot.com/2014/11/does-it-take-9-90-or-900-seconds-to.html), Unknown → stopped: not opened
 └─ *The Guardian*, web-design article, 13 Sept 2000, (not opened), per [Drumm 2022](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/), Unknown, root

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | the root compares a goldfish's attention span with an internet user's, in an article about web design (per Drumm 2022; root not opened) | Human attention span is now shorter than a goldfish's | [Microsoft Canada, *Attention spans*](https://slideshare.net/sriushtiimx/microsoft-attentionspansresearchreport), 2015 |

### Status of the root
- No primary found, so there was no status to check.
- National Center for Biotechnology Information / National Library of Medicine and the Associated Press: [Drumm 2022](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/) reports that Simon Maybin's 2017 BBC News investigation found no record of the research at any of the sources Statistic Brain listed. Drumm also reports that attention researchers Maybin asked didn't know where the figures came from. I could not open the BBC piece itself because the fetch tool can't reach bbc.com.
- Microsoft Canada report: its own research, per the [SlideShare copy](https://slideshare.net/sriushtiimx/microsoft-attentionspansresearchreport), was an online survey of 2,000 Canadians (Q4 2014) and EEG readings of 112 people (December 2014). The goldfish slide credits Statistic Brain, not that research. [Drumm 2022](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/) adds that the study examined sustained, selective and alternating attention, not a span in seconds.

### Cold trails
None.

### Confidence
Low: the Microsoft report and *Time* were opened, but every branch ends at a page I couldn't open: Statistic Brain (domain gone, archives unreachable), its listed sources, the 2002 BBC article and the 2000 *Guardian* article. So no node that cites nothing earlier was ever opened.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
