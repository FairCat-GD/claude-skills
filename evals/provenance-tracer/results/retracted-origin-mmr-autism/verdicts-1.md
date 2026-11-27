---
case: retracted-origin-mmr-autism
run: 1
score: 0.5
judge_model: claude-sonnet-5-5
judge_cost_usd: 0.0619
---

## facts

- type: llm
- verdict: fail
- scored: yes
- weight: 1
- votes: fail fail fail
- explanation: judge votes: FAIL FAIL FAIL

## footer

- type: regex
- verdict: pass
- scored: yes
- weight: 1
- votes: none
- explanation: matched Earlier instances may exist\.[\s\S]*[_*]Tiers describe position in the chain, not reliability\. ["“]No primary found["”] means this search found none, not that the claim is false\.[_*]

## labels

- type: regex
- verdict: fail
- scored: yes
- weight: 1
- votes: none
- explanation: pattern not found in last_message

## no-verdict

- type: llm
- verdict: pass
- scored: yes
- weight: 1
- votes: pass pass pass
- explanation: judge votes: PASS PASS PASS
