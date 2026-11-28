---
case: non-interactive-goldfish-attention
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:28:03Z
cost_usd: 1.4867
duration_s: 204
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
- WebSearch: "attention span" "shorter than a goldfish"
- WebSearch: humans 8 second attention span goldfish 9 seconds Microsoft study
- WebSearch: Microsoft Canada Consumer Insights Attention Spans 2015 report PDF
- WebSearch: "8.25 seconds" attention span Statistic Brain National Center for Biotechnology Information
- WebSearch: origin of goldfish attention span statistic myth source
- WebSearch: goldfish attention span claim fact check BBC More or Less
- WebFetch: https://storage.googleapis.com/public.papers.www.brainsights.com/Microsoft_Attention%20Spans.pdf
- WebFetch (error): https://www.bbc.com/news/health-38896790
- WebFetch (error): https://web.archive.org/cdx/search/cdx?url=statisticbrain.com/attention-span-statistics/&limit=5
- WebFetch: https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/
- WebFetch (error): https://pdf4pro.com/view/microsoft-attention-spans-spring-2015-msadvertisingca-6dcfd0.html
- WebFetch (error): https://www.bbc.co.uk/news/health-38896790
- WebSearch: Time 2015 "You Now Have a Shorter Attention Span Than a Goldfish"
- WebFetch: https://time.com/3858309/attention-spans-goldfish/
- WebFetch: https://www.mangalam.nl/wp-content/uploads/2019/05/microsoft-attention-spans-research-report.pdf
- WebFetch: http://joyfulpublicspeaking.blogspot.com/2015/05/do-reporters-have-lower-attention-spans.html
- WebFetch (error): http://www.statisticbrain.com/attention-span-statistics/
- WebFetch: https://static1.squarespace.com/static/59bf2bf68fd4d28e59627113/t/5ab01bdff950b70546a08167/1521490918597/265348695-Microsoft-Attention-Spans-Research-Report.pdf
- WebFetch: https://geneticliteracyproject.org/2016/07/25/another-modern-myth-shrinking-attention-spans/
- WebFetch: https://medium.com/psynamic/8-second-attention-spans-tracking-the-myth-that-just-wont-quit-614dd2cb9792
- Read (denied): <temp>/config/projects/-private-tmp-e-kmtJtP-home-cwd/eeebaa6b-3e43-49be-b357-e15246362726/tool-results/webfetch-1795825708751-mkg9ro.pdf
- WebFetch: https://scienceblog.com/t-humans-eight-second-attention-span-goldfish-myth/
- WebFetch: http://advertising.microsoft.com/en/cl/31966/how-does-digital-affect-canadian-attention-spans
- WebFetch: https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10061476
- WebFetch: https://about.ads.microsoft.com/en/cl/31966/how-does-digital-affect-canadian-attention-spans
- WebFetch: https://dam-it.io/guides/goldfish-attention-span-myth-8-seconds
- WebFetch: http://joyfulpublicspeaking.blogspot.com/2014/12/statistic-brain-is-just-statistical.html
- WebFetch: https://en.wikipedia.org/wiki/Attention_span
- WebFetch: https://www.warc.com/newsandopinion/opinion/why-the-goldfish-myth-wont-die/3226
- WebFetch: https://www.linkedin.com/today/post/article/20140418171300-15742110-writing-for-goldfish

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Human attention span is now shorter than a goldfish's."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** [Statistic Brain, *Attention Span Statistics*](http://www.statisticbrain.com/attention-span-statistics/), 2014 (date from: cited by Joyful Public Speaking, December 2014). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 9

### Chain
Your version: "Human attention span is now shorter than a goldfish's" (where you met it: not given)
 ├─ [TIME, *You Now Have a Shorter Attention Span Than a Goldfish*](https://time.com/3858309/attention-spans-goldfish/), 2015, Secondary → cites
 │   └─ [Microsoft Canada Consumer Insights, *Attention spans*](https://storage.googleapis.com/public.papers.www.brainsights.com/Microsoft_Attention%20Spans.pdf), 2015, (not opened), per TIME → cites
 │       └─ [Statistic Brain, *Attention Span Statistics*](http://www.statisticbrain.com/attention-span-statistics/), 2014, (not opened), per Joyful Public Speaking 2014, root → stopped: not opened (the page names the Associated Press, the NCBI and the US National Library of Medicine as its sources)
 ├─ [Joyful Public Speaking, *Do reporters have shorter attention spans than goldfish?*](http://joyfulpublicspeaking.blogspot.com/2015/05/do-reporters-have-lower-attention-spans.html), 2015, Tertiary → cites the Microsoft report and its page-6 source, Statistic Brain (both above)
 ├─ [Joyful Public Speaking, *Statistic Brain is just statistical…*](http://joyfulpublicspeaking.blogspot.com/2014/12/statistic-brain-is-just-statistical.html), 2014, Tertiary → cites Statistic Brain (above)
 ├─ [Genetic Literacy Project, *Another modern myth: Shrinking attention spans*](https://geneticliteracyproject.org/2016/07/25/another-modern-myth-shrinking-attention-spans/), 2016, Tertiary → cites TIME and the Microsoft report (above)
 ├─ [Marketing Insider Group, Michael Brenner](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/), 2022 (byline; the author says he first published it in 2014), Tertiary → cites the Microsoft report (above)
 └─ [dam-it.io, *Goldfish Attention Span: Is It 9 Seconds?*](https://dam-it.io/guides/goldfish-attention-span-myth-8-seconds), date unknown, Tertiary → cites
     └─ [BBC News, *Busting the attention span myth*](https://www.bbc.com/news/health-38896790), 2017, (not opened), per dam-it.io → cites the Microsoft report and Statistic Brain (above)

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Context removed (dated figures with no stated method became a present-tense general fact) | [Per Joyful Public Speaking](http://joyfulpublicspeaking.blogspot.com/2014/12/statistic-brain-is-just-statistical.html): "human attention spans of 12 seconds in 2000, 8 seconds in 2013" | Human attention span is now shorter than a goldfish's | [TIME](https://time.com/3858309/attention-spans-goldfish/), 2015 |

### Status of the root
- No primary found, so there was no status to check.
- Statistic Brain: according to [Joyful Public Speaking (2014)](http://joyfulpublicspeaking.blogspot.com/2014/12/statistic-brain-is-just-statistical.html), the page listed the NCBI, the NLM and the Associated Press as sources, and earlier versions listed only the AP. The post adds that a writer tried to find the goldfish data in April 2014 and could not.
- Microsoft Canada report: [Joyful Public Speaking (2015)](http://joyfulpublicspeaking.blogspot.com/2015/05/do-reporters-have-lower-attention-spans.html) says the figures on page 6 were quoted from Statistic Brain: "That was NOT something found by the Microsoft research."
- BBC *More or Less*, 2017 (not opened): according to [dam-it.io](https://dam-it.io/guides/goldfish-attention-span-myth-8-seconds), the BBC found that Statistic Brain's listed sources had no record of research behind the figures. A fish-behaviour expert told the BBC there is no evidence that goldfish have unusually short attention spans or memories.
- Microsoft Canada report: [Genetic Literacy Project](https://geneticliteracyproject.org/2016/07/25/another-modern-myth-shrinking-attention-spans/) notes the report was not peer-reviewed and that "no definition of attention span is given".
- Marketing Insider Group: [Michael Brenner](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/) says he spread the claim in 2014. His current page says the claim has since been shown to be untrue and that no one ever measured a goldfish's attention span.

### Cold trails
None.

### Confidence
Medium. I could open neither the Microsoft report (no copy's PDF text could be read) nor the Statistic Brain page (the site no longer resolves, and the Wayback Machine was blocked), and the root's 2014 date rests on *cited by*.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
