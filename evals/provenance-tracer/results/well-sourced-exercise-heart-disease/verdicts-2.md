---
case: well-sourced-exercise-heart-disease
run: 2
score: 1
judge_model: claude-sonnet-5-5
judge_cost_usd: 0.0400
---

## facts

- type: llm
- verdict: pass
- scored: yes
- weight: 1
- votes: pass pass pass
- explanation: judge votes: PASS PASS PASS

## footer

- type: regex
- verdict: pass
- scored: yes
- weight: 1
- votes: none
- explanation: matched Earlier instances may exist\.[\s\S]*[_*]Tiers describe position in the chain, not reliability\. ["“]No primary found["”] means this search found none, not that the claim is false\.[_*]

## labels

- type: regex
- verdict: pass
- scored: yes
- weight: 1
- votes: none
- explanation: matched \*\*Roots:\*\* Independent · \*\*Grounding:\*\* Grounded(?: · Mutated)?(?: · Misattributed)?(?: · Origin retracted)?(?: · Origin corrected)?(?: · Origin failed replication)?[ \t]*(?:\r?\n|$)

## no-verdict

- type: llm
- verdict: pass
- scored: yes
- weight: 1
- votes: pass pass pass
- explanation: judge votes: PASS PASS PASS
