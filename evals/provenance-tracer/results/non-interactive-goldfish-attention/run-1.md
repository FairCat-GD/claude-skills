---
case: non-interactive-goldfish-attention
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:25:29Z
cost_usd: 1.5536
duration_s: 201
turns: 39
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
- WebSearch: "8 seconds" attention span Statistic Brain National Center for Biotechnology Information
- WebSearch: origin of goldfish attention span statistic source
- WebSearch: goldfish attention span myth fact check BBC More or Less
- WebSearch: Microsoft Canada "Attention spans" consumer insights 2015 report PDF
- WebFetch: https://storage.googleapis.com/public.papers.www.brainsights.com/Microsoft_Attention%20Spans.pdf
- WebFetch (error): https://www.bbc.com/news/health-38896790
- WebFetch: https://medium.com/psynamic/8-second-attention-spans-tracking-the-myth-that-just-wont-quit-614dd2cb9792
- WebFetch: https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/
- WebFetch (error): http://news.bbc.co.uk/2/hi/science/nature/1834682.stm
- WebFetch: https://pdfcoffee.com/microsoft-attention-spans-research-report-pdf-free.html
- WebFetch (error): https://web.archive.org/web/2017/https://www.bbc.com/news/health-38896790
- WebFetch (error): https://web.archive.org/web/2002/http://news.bbc.co.uk/2/hi/science/nature/1834682.stm
- WebFetch: https://pdfcookie.com/documents/microsoft-attention-spans-research-report-3lkzme99kplk
- WebFetch: https://www.mangalam.nl/wp-content/uploads/2019/05/microsoft-attention-spans-research-report.pdf
- WebFetch: https://scienceblog.com/t-humans-eight-second-attention-span-goldfish-myth/
- WebFetch: https://dam-it.io/guides/goldfish-attention-span-myth-8-seconds
- WebFetch: https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/
- WebFetch: https://pr.motamem.org/microsoft-attention-spans-research-report.pdf
- WebSearch: Time 2015 "You Now Have a Shorter Attention Span Than a Goldfish"
- WebSearch: "attention span of nine seconds" goldfish web 2000 OR 2002
- WebFetch: https://time.com/3858309/attention-spans-goldfish/
- WebFetch: https://internet.psych.wisc.edu/wp-content/uploads/532-Master/532-UnitPages/Unit-09/Attention_Goldfish_Abbreviated.pdf
- WebFetch (error): https://www.statisticbrain.com/attention-span-statistics/
- WebFetch: https://exnihilomagazine.com/the-great-attention-spans-hoax-why-8-seconds-never-mattered/
- WebFetch: https://geneticliteracyproject.org/2016/07/25/another-modern-myth-shrinking-attention-spans/
- WebFetch: http://policyviz.com/the-attention-span-statistic-fallacy/
- WebFetch: https://ccit.college.columbia.edu/sites/ccit/files/weinreich-web-use-study.pdf
- WebFetch: http://advertising.microsoft.com/en/cl/31966/how-does-digital-affect-canadian-attention-spans
- WebFetch: https://about.ads.microsoft.com/en/cl/31966/how-does-digital-affect-canadian-attention-spans

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Human attention span is now shorter than a goldfish's."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** [BBC News, 2002](http://news.bbc.co.uk/2/hi/science/nature/1834682.stm) (date from: cited by [A Patchwork of Perceptions, 2022](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 5

### Chain
Your version: "Human attention span is now shorter than a goldfish's" (where you met it: not given)
 └─ [Time, *You Now Have a Shorter Attention Span Than a Goldfish* (Kevin McSpadden)](https://time.com/3858309/attention-spans-goldfish/), 2015, Tertiary → cites
     └─ [Microsoft Canada Consumer Insights, *Attention spans*](https://storage.googleapis.com/public.papers.www.brainsights.com/Microsoft_Attention%20Spans.pdf), 2015, Tertiary (not opened, per [PolicyViz](http://policyviz.com/the-attention-span-statistic-fallacy/)) → cites
         └─ [Statistic Brain, *Attention Span Statistics*](https://www.statisticbrain.com/attention-span-statistics/), date unknown, Unknown (not opened, per [PolicyViz](http://policyviz.com/the-attention-span-statistic-fallacy/)) → stopped: not opened
 └─ [Marketing Insider Group (Michael Brenner)](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/), 2014, Tertiary → cites Statistic Brain (above)
 └─ [BBC News, science/nature article](http://news.bbc.co.uk/2/hi/science/nature/1834682.stm), 2002, Unknown (not opened, per [A Patchwork of Perceptions](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/)), root

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | heavy web browsing can leave a person with a goldfish-length attention span (as the 2022 blog reports it) | Human attention span is now shorter than a goldfish's | [Marketing Insider Group](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/), 2014 |
| Number changed | nine seconds, the *same as* a goldfish | Human attention span is now shorter than a goldfish's | [Marketing Insider Group](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/), 2014 |

### Status of the root
- No primary found, so there was no status to check.
- Microsoft Canada report: according to [Time](https://time.com/3858309/attention-spans-goldfish/), Microsoft's own research was a survey of 2,000 Canadians plus EEG recordings of 112 people. Time gives no source for the 9-second goldfish figure.
- Microsoft Canada report, per [PolicyViz (Jon Schwabish, 2016)](http://policyviz.com/the-attention-span-statistic-fallacy/): "Attention span length was not even tested as part of the study!" It says the figures appear in a graphic on page 6 that credits Statistic Brain.
- Statistic Brain, per [PolicyViz](http://policyviz.com/the-attention-span-statistic-fallacy/): the page listed a 2008 web-usage study by Weinreich et al. (25 participants), which PolicyViz says does not test attention spans. It also listed NCBI/NLM and the Associated Press. PolicyViz reports that NLM told it it could not verify the figure. A copy of the Weinreich paper ([Columbia copy](https://ccit.college.columbia.edu/sites/ccit/files/weinreich-web-use-study.pdf)) returned 403 and was not opened.
- BBC *More or Less* (Simon Maybin, March 2017), per [Dam It! guide](https://dam-it.io/guides/goldfish-attention-span-myth-8-seconds): NCBI and the Associated Press could find no record of research behind the numbers. Statistic Brain could not be reached. A fish-behaviour expert said there is no evidence that goldfish have unusually short attention spans. The BBC page itself could not be fetched.
- [Genetic Literacy Project (Andrew Porterfield, 2016)](https://geneticliteracyproject.org/2016/07/25/another-modern-myth-shrinking-attention-spans/) notes that the figures came with no definition of attention span and no method for deriving them. It also records that Statistic Brain's version gave 8.25 seconds for 2015.
- [Marketing Insider Group](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/): the author of this 2014 retelling has since revised it and now describes the figures as a myth.

### Cold trails
None.

### Confidence
Low. The main branch stops at two pages that could not be opened (four copies of the Microsoft report PDF gave no readable text, and Statistic Brain's domain no longer resolves), and the 2002 earliest instance is known only from a 2022 blog.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
