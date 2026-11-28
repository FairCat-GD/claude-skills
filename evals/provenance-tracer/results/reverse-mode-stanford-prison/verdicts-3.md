---
case: reverse-mode-stanford-prison
run: 3
score: 1
judge_model: claude-sonnet-5-5
judge_cost_usd: 0.0375
---

## facts

- type: llm
- verdict: pass
- scored: yes
- weight: 1
- votes: pass pass pass
- explanation: judge votes: PASS PASS PASS

## no-verdict

- type: llm
- verdict: pass
- scored: yes
- weight: 1
- votes: fail pass pass
- explanation: judge votes: FAIL PASS PASS
