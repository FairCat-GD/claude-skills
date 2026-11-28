---
case: echoed-statistic-goldfish-attention
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:25:29Z
cost_usd: 1.5300
duration_s: 177
turns: 37
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
- WebSearch: 8 seconds attention span goldfish 9 seconds Microsoft study 2015
- WebSearch: Microsoft Canada consumer insights attention spans report goldfish
- WebSearch: "8.25 seconds" attention span Statistic Brain National Center for Biotechnology Information
- WebSearch: origin of goldfish attention span statistic myth source
- WebSearch: goldfish attention span fact check BBC More or Less
- WebFetch: https://static1.squarespace.com/static/59bf2bf68fd4d28e59627113/t/5ab01bdff950b70546a08167/1521490918597/265348695-Microsoft-Attention-Spans-Research-Report.pdf
- WebFetch (error): https://www.bbc.com/news/health-38896790
- WebFetch (error): https://web.archive.org/cdx/search/cdx?url=statisticbrain.com/attention-span-statistics/&limit=5
- WebSearch: time.com 2015 "You Now Have a Shorter Attention Span Than a Goldfish"
- WebFetch: https://www.mangalam.nl/wp-content/uploads/2019/05/microsoft-attention-spans-research-report.pdf
- WebFetch (error): https://www.bbc.co.uk/news/health-38896790
- WebFetch: https://time.com/3858309/attention-spans-goldfish/
- WebSearch: "Microsoft attention spans" "Spring 2015" pdf "Statistic Brain"
- WebFetch: https://medium.com/psynamic/8-second-attention-spans-tracking-the-myth-that-just-wont-quit-614dd2cb9792
- WebFetch: https://scienceblog.com/t-humans-eight-second-attention-span-goldfish-myth/
- WebFetch: https://internet.psych.wisc.edu/wp-content/uploads/532-Master/532-UnitPages/Unit-09/Gausby_MicrosoftReport_2015_Excerpt.pdf
- WebFetch: https://dam-it.io/guides/goldfish-attention-span-myth-8-seconds
- WebFetch: https://geneticliteracyproject.org/2016/07/25/another-modern-myth-shrinking-attention-spans/
- WebFetch: https://storage.googleapis.com/public.papers.www.brainsights.com/Microsoft_Attention%20Spans.pdf
- WebFetch: https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/
- WebFetch (error): http://www.statisticbrain.com/attention-span-statistics/
- WebFetch: https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10061476
- Read (denied): <temp>/config/projects/-private-tmp-e-7329W4-home-cwd/11075a82-1c22-4ec2-9f63-746d7765071d/tool-results/webfetch-1795825557141-tlfmxx.pdf
- WebFetch (error): https://pdf4pro.com/view/microsoft-attention-spans-spring-2015-msadvertisingca-6dcfd0.html
- WebFetch: https://detox.so/blog/attention-span-goldfish-myth
- WebFetch: https://www.churchandculture.org/blog/2015/8/13/8-second-filters
- WebFetch: https://www.fastcompany.com/91023619/8-second-attention-span-is-bs-this-is-why
- WebFetch: https://www.tryhugo.app/blog/average-attention-span-goldfish-myth

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Human attention span is now shorter than a goldfish's."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** Statistic Brain, *Attention Span Statistics* page, 2012 (date from: cited by [Hugo blog](https://www.tryhugo.app/blog/average-attention-span-goldfish-myth), which links a Wayback Machine capture of 8 Feb 2012). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 8

### Chain
Your version: "Human attention span is now shorter than a goldfish's" (where you met it: not given)
 ├─ [*You Now Have a Shorter Attention Span Than a Goldfish*, Time (Kevin McSpadden)](https://time.com/3858309/attention-spans-goldfish/), 2015, Tertiary → cites
 │   └─ [Microsoft Canada Consumer Insights, *Attention spans*, Spring 2015](https://static1.squarespace.com/static/59bf2bf68fd4d28e59627113/t/5ab01bdff950b70546a08167/1521490918597/265348695-Microsoft-Attention-Spans-Research-Report.pdf), 2015, Tertiary (not opened), per Time and Hugo blog → cites
 │       └─ [Statistic Brain, *Attention Span Statistics*](http://www.statisticbrain.com/attention-span-statistics/), March 2015 capture, Unknown (not opened), per Hugo blog → cites
 │           └─ Statistic Brain, same page, February 2012 capture, Unknown (not opened), per Hugo blog, root. It names the Associated Press as its source, and no AP item was found → stopped: not opened
 ├─ [*Busting The Social Media Ruined Our Average Attention Span Goldfish Myth*, Marketing Insider Group (Michael Brenner)](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/), 2014 (the page says it was first published then, under an earlier title), Tertiary → cites Statistic Brain (the root above)
 ├─ [*8-Second Filters*, Church & Culture (James Emery White)](https://www.churchandculture.org/blog/2015/8/13/8-second-filters), 2015, Tertiary → cites Statistic Brain (the 2015 version above)
 ├─ [*Another modern myth: Shrinking attention spans*, Genetic Literacy Project](https://geneticliteracyproject.org/2016/07/25/another-modern-myth-shrinking-attention-spans/), 2016, Tertiary → cites the Microsoft report and Statistic Brain (above)
 └─ [*What Is the Average Human Attention Span? Tracing the Goldfish Myth*, Hugo blog](https://www.tryhugo.app/blog/average-attention-span-goldfish-myth), 2026, Tertiary → cites the Statistic Brain captures, the Microsoft report and the BBC (above)

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Context removed (a dated figure became *now*) | The 2012 page dates the 8-second human figure to 2012 and puts it next to a 9-second goldfish figure. The 2015 version moved the same figure to 2013 (per Hugo blog). | Human attention span is now shorter than a goldfish's | [Time](https://time.com/3858309/attention-spans-goldfish/), 2015 (the headline says *now*) |
| Other: source moved (AP, then NCBI, then Microsoft) | The 2012 page credits the Associated Press. The 2015 version adds the National Center for Biotechnology Information (per Hugo blog). | Human attention span is now shorter than a goldfish's | [Time](https://time.com/3858309/attention-spans-goldfish/), 2015, credits a *new study from Microsoft* |

### Status of the root
- No primary found, so there was no status to check.
- Statistic Brain's named sources: according to [Hugo blog](https://www.tryhugo.app/blog/average-attention-span-goldfish-myth), the BBC's *More or Less* (Simon Maybin, 2017) asked the NCBI and the Associated Press about the figures. Neither could find research behind them, and attempts to reach Statistic Brain failed. The BBC page itself would not load here.
- Microsoft report: [Genetic Literacy Project](https://geneticliteracyproject.org/2016/07/25/another-modern-myth-shrinking-attention-spans/) calls it non-peer-reviewed. It adds that the report gives no definition of attention span and that it is unclear how the numbers were produced.
- Microsoft report: [Hugo blog](https://www.tryhugo.app/blog/average-attention-span-goldfish-myth) says page 6 lists 12 seconds (2000), 8 seconds (2013) and 9 seconds (goldfish), credited to Statistic Brain. It also says the figure was not Microsoft's own measurement. The report's own work was a survey of about 2,000 Canadians and an EEG study of 112 people.
- Marketing Insider Group: the author's [later version of the 2014 post](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/) now presents the goldfish comparison as a myth. It says the Statistic Brain page is gone and that the National Library of Medicine holds nothing on the study.

### Cold trails
None.

### Confidence
Medium: Time and the other retellings were opened, but the Microsoft report (five copies tried, none returned readable text) and the Statistic Brain captures (the Wayback Machine and the BBC were unreachable from here) were not, so the root and its dates rest on *cited by*.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
