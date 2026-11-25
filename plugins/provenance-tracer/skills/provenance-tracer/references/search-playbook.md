# Search playbook

How to search, open and date the sources of a trace, when to stop, and how to check the status of
a Primary. The claim's text goes into the searches; say so once, at the start of your reply.

## What never goes into a query

- **Anything about a private individual.** That claim gets no search at all (`SKILL.md`, *Mode
  selection*).
- **Names from the personal chain or from hearsay:** the colleague, friend or relative who told the
  user. They stay out of every query unless they are public figures or publications. A magazine,
  broadcaster or book the user names may be searched. The person who passed it on may not.
- **Anything else the user said about themselves.**

## Queries

Write the first 6 queries from these families, one or two from each that fits the claim, and run
all 6 before you judge whether to add more. A fact-check or quote-investigation page found early is
one lead among several: the other families find the retellings and citations it may not list.

| Family | Pattern |
| --- | --- |
| Exact phrasing | the claim's key words in quotation marks: `"<exact phrase>"` |
| Paraphrases | the same claim in other common wordings, and the shortest form people repeat |
| Key entities | the person, body, study or place named, with the claim's topic |
| The number or quote alone | the statistic with its unit (`"<n> percent" <topic>`), or the quote's most distinctive words in quotation marks |
| Origin-hunting | `origin of "<phrase>"`, `who first said "<phrase>"`, `source of the <statistic>`, `<claim> earliest`, `<claim> first appeared` |
| Fact-check and quote investigation | the claim with a fact-check or quote-investigation site's name, or `site:` that site |

**Fact-check and quote-investigation sites are good leads:** Quote Investigator, Snopes, Full
Fact, Reuters Fact Check, AFP Fact Check, PolitiFact, and Wikiquote's *Misattributed* and
*Disputed* sections. Treat each as any other node:
- open it before you use it;
- name it as a source;
- report what it found as its finding, in its words or a neutral paraphrase, never as your
  verdict.

The pages they cite are your next fetches.

## The budget and when to stop

- **Queries:** start with 6. Add up to 14 more, 20 in all, only while the last queries keep
  turning up a retelling or a citation you had not seen. Stop adding as soon as a query turns up
  nothing new.
- **Fetches:** at most 25 per trace, each fetch you attempt counted, failed ones included. Spend
  them on the chain first: the pages that cite something earlier, then what they cite, then status
  checks, then cold trails.
- **Hops:** at most 6 per branch. A hop is following one citation back, from a node to the node it
  cites.
- **A branch ends** at:
  - a node that cites nothing earlier;
  - a node whose fetch failed (it stays `(not opened)`);
  - the sixth hop;
  - the end of the fetch budget.

  The report shows where each branch ended.

## Opening a page

- **Open every page you use.** A search snippet tells you which page to open. It is never
  evidence: never a date, a variant of the claim, or a citation.
- **When the fetch tool takes a prompt,** ask it for:
  - the publication date and where the page gives it;
  - the author;
  - the exact sentence or sentences stating the claim;
  - every source the page cites for it, with links.

  Ask for the exact words, not a summary, so the variant you record is the page's own.
- **A fetch that fails, a paywall, or a login wall:** keep the node as `(not opened)`, citing the
  opened page that names it. Never fill in what the page probably says.
- **A redirect:** fetch the address it gives and link that address, since every link in the report
  must be one you fetched.
- **A PDF or a scanned book page** counts as opened if the fetch returned its text.

## Following citations back

- A page's own references, footnotes and links come first, then what the text names ("a 2004
  survey by…"). Search for a named source you have no link for, by its title, authors and year.
- **Naming a source is citing it,** even with no link, so the chain continues to the named work.
- **A citation that does not hold:** the cited work, opened, does not say what the citing page
  says. Record what it does say. The drift starts at the citing page.
- **Circular citation.** Two pages may cite each other, or a page may cite a retelling of
  itself. When that happens, stop the branch at the earlier one and say so.

## Dating a node

Give each node a year and say where it came from, in the report's form
`(date from: byline | archive | cited by X)`:

- **Byline:** a date printed on the page or document itself: the article's date, a paper's
  publication date, a book's edition year.
- **Archive:** the earliest capture in the Internet Archive's Wayback Machine. The capture index
  `https://web.archive.org/cdx/search/cdx?url=<url>&limit=1` lists the earliest capture first, its
  timestamp beginning with the year. A capture date shows the page existed by then, not when it
  was written.
- **Cited by X:** an opened later page that names this one with its date.

When none of these gives a date, write `date unknown`. Never guess one from the page's style or
topic. A page's "last updated" date is not its first date.

## Status of a Primary

Check the root's Primary first, opened or not: its status is what the *Origin* modifiers judge.
Then, while the fetch budget allows, any other Primary in the chain. Each check is a fetch within
the budget, and each finding is reported under *Status of the root* as a sourced fact, linked; a
finding about another Primary names that source at the start of its bullet.

1. **The publisher's or journal's page** for the work: notices of retraction, correction or
   concern are usually linked from it.
2. **The Crossref record,** for a work with a DOI: `https://api.crossref.org/works/<DOI>`. Look for
   updates to it: a retraction, a correction, an expression of concern.
3. **Retraction Watch:** search its database, or `"<title>" retraction`, for a retraction the
   journal page does not show.
4. **PubPeer:** `https://pubpeer.com/search?q=<DOI or title>`, for published critiques and the
   authors' replies. A comment is a lead, not a status. Report it only with what it links to,
   opened.
5. **Replications and major later studies:** search `"<title>" replication`, `<finding> failed to
   replicate`, `<first author> <year> reanalysis`, and `<topic> meta-analysis`. Report a later
   study that set out to repeat the finding, or a review that weighed it, with what it found, in
   one line.

With no Primary in the chain, there is nothing to check. The report says so.

## A named source (reverse mode)

- **Find the work itself first:** its page at the publisher, the journal, a library catalogue, or
  the speaker's own transcript.
- **Several works may match the description.** List them, and ask which. When no reply is
  possible, take the most cited and say so.
- **Open the work,** or its abstract and the parts that state its findings, before saying what it
  found.
- **For its popular versions,** search the finding as people retell it (the *Paraphrases* and
  *Exact phrasing* families above). Pick the two or three most common, and open each one you
  report.
