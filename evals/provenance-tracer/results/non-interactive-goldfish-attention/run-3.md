---
case: non-interactive-goldfish-attention
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:17:59Z
cost_usd: 1.4374
duration_s: 156
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
- WebSearch: humans 8 second attention span goldfish 9 seconds Microsoft study
- WebSearch: Microsoft Canada Consumer Insights attention spans 2015 report
- WebSearch: "8 seconds" attention span Statistic Brain National Center for Biotechnology Information
- WebSearch: origin of goldfish attention span statistic source
- WebSearch: goldfish attention span myth fact check BBC More or Less
- WebFetch (error): https://www.bbc.com/news/health-38896790
- WebFetch: https://static1.squarespace.com/static/59bf2bf68fd4d28e59627113/t/5ab01bdff950b70546a08167/1521490918597/265348695-Microsoft-Attention-Spans-Research-Report.pdf
- WebFetch: https://medium.com/psynamic/8-second-attention-spans-tracking-the-myth-that-just-wont-quit-614dd2cb9792
- WebSearch: Time "You Now Have a Shorter Attention Span Than a Goldfish" 2015
- WebFetch: https://time.com/3858309/attention-spans-goldfish/
- WebFetch: https://pdfcoffee.com/microsoft-attention-spans-research-report-pdf-free.html
- WebFetch (error): https://web.archive.org/web/2012/http://www.statisticbrain.com/attention-span-statistics/
- WebFetch: https://www.swordandthescript.com/2022/02/goldfish-attention-span/
- WebFetch: http://www.marketplace.org/2014/02/11/business/goldfish-have-longer-attention-spans-americans-and-publishing-industry-knows-it
- WebFetch: https://scienceblog.com/t-humans-eight-second-attention-span-goldfish-myth/
- WebFetch: https://dam-it.io/guides/goldfish-attention-span-myth-8-seconds
- WebFetch: https://en.wikipedia.org/wiki/Attention_span
- WebFetch: http://advertising.microsoft.com/en/cl/31966/how-does-digital-affect-canadian-attention-spans
- WebSearch: "Statistic Brain" attention span goldfish 2012 Associated Press wayback
- WebSearch: Alyson Gausby Policy Options attention span goldfish misinterpreted
- WebFetch: https://internet.psych.wisc.edu/wp-content/uploads/532-Master/532-UnitPages/Unit-09/Gausby_MicrosoftReport_2015_Excerpt.pdf
- WebFetch: https://www.ceros.com/originals/no-dont-attention-span-goldfish/
- WebFetch: https://about.ads.microsoft.com/en/cl/31966/how-does-digital-affect-canadian-attention-spans
- WebFetch: https://www.tryhugo.app/blog/average-attention-span-goldfish-myth
- WebFetch (error): https://web.archive.org/web/20120208152927/http://www.statisticbrain.com/attention-span-statistics/
- WebFetch: https://www.marketplace.org/2014/02/11/goldfish-have-longer-attention-spans-americans-and-publishing-industry-knows-it/
- WebFetch: https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Human attention span is now shorter than a goldfish's."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** [Statistic Brain, *Attention Span Statistics*](https://web.archive.org/web/20120208152927/http://www.statisticbrain.com/attention-span-statistics/), 2012 (date from: cited by [Hugo](https://www.tryhugo.app/blog/average-attention-span-goldfish-myth), which links a Wayback capture dated 8 February 2012). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 5

### Chain
Your version: "Human attention span is now shorter than a goldfish's" (where you met it: not given)
 ├─ [Time, *You Now Have a Shorter Attention Span Than a Goldfish* (Kevin McSpadden)](https://time.com/3858309/attention-spans-goldfish/), 2015, Secondary. It says "people now generally lose concentration after eight seconds." → cites
 │   └─ [Microsoft Canada Consumer Insights, *Attention spans* (Alyson Gausby)](https://pdfcoffee.com/microsoft-attention-spans-research-report-pdf-free.html), Spring 2015, Secondary. Opened, but the text I got back has no goldfish passage. [Sword and the Script](https://www.swordandthescript.com/2022/02/goldfish-attention-span/) (2022) says the figure appears in it "with a citation for another source called Statistic Brain". → cites
 │       └─ Statistic Brain, *Attention Span Statistics*, 2012, (not opened), per [Hugo](https://www.tryhugo.app/blog/average-attention-span-goldfish-myth). Hugo says the 2012 version gave 8 seconds for 2012, 12 for 2000 and 9 for a goldfish, crediting the Associated Press. → cites
 │           └─ The Associated Press, no article named, date unknown, (not opened), per [Hugo](https://www.tryhugo.app/blog/average-attention-span-goldfish-myth) → stopped: not opened
 └─ [Marketing Insider Group, *Thanks social media – our attention span is now shorter than a goldfish* (Michael Brenner)](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/), 2014, Secondary. The current page says it first ran in 2014 and gives the figures as "dropped from 12 seconds in 2000 to 8 seconds in 2013". It also says Statistic Brain cited the U.S. National Library of Medicine's NCBI. → cites
     └─ Statistic Brain (as above)

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Context removed | Dated figures with no stated method: 12 s in 2000, 8 s in 2012, goldfish 9 s (per Hugo's account of the 2012 capture) | "now shorter than a goldfish's" | [Marketing Insider Group](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/), 2014 (title) |
| Date moved (other) | 8 seconds labelled as 2012 | 8 seconds labelled as 2013 (the version Microsoft and Marketing Insider Group carry) | Statistic Brain's later version, a March 2015 capture per [Hugo](https://www.tryhugo.app/blog/average-attention-span-goldfish-myth) |
| Attribution shifted (later retellings, not your version) | A Statistic Brain table | The figure as a Microsoft finding: the article cites a "Microsoft study" | [Time](https://time.com/3858309/attention-spans-goldfish/), 2015 |

The Microsoft report's own summary opens "Good news! It's not as bad as you think." ([report text](https://pdfcoffee.com/microsoft-attention-spans-research-report-pdf-free.html)). Its foreword says tech-savvy consumers are getting better at processing information. Retellings that cite Microsoft for the goldfish line leave out that framing.

### Status of the root
- No primary found, so there was no status to check.
- Fact-checks, as sources: [Sword and the Script](https://www.swordandthescript.com/2022/02/goldfish-attention-span/) (2022) and [Dam It!](https://dam-it.io/guides/goldfish-attention-span-myth-8-seconds) (2026) both report on a 2017 BBC *More or Less* investigation by Simon Maybin. Per them, the sources Statistic Brain named (the NCBI and the Associated Press) found no record of research behind the numbers. I could not open the [BBC article](https://www.bbc.com/news/health-38896790) itself.
- The current [Marketing Insider Group](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/) page, by the 2014 author, now says no one has ever measured a goldfish's attention span. It also says it found nothing about the figure on the NCBI site.

### Cold trails
None.

### Confidence
Low. The chain stops at an Associated Press reference that names no article. The Statistic Brain page that started the trail could not be opened, because Wayback Machine fetches were blocked. Its 2012 date and contents come from Hugo's account of the archive capture.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
