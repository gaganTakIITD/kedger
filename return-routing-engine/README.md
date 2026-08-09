# Return Routing Engine — Final Solution

Standalone fix for the e-commerce **return routing** challenge (kept separate from the main Kedger repo).

## What was broken

1. **One-way account links** — links were stored only as `primary → related`, so looking up the related account missed the group and under-counted return history.
2. Links must be **undirected** and **transitive** (connected components), then history is summed across the whole group.
3. Policy checks, scoring, and decision bands must run in the correct order with the correct reasons.

## Correct pipeline

1. **Category eligibility** — missing / not returnable → `REJECT` + `CATEGORY_NON_RETURNABLE` (`risk_score: null`)
2. **Return window** — `days_since_purchase > allowed_return_window_days` → `REJECT` + `RETURN_WINDOW_EXPIRED` (`risk_score: null`)
3. **Linked return history** — sum `return_history_count` for the request account and every transitively linked account (missing profile = 0)
4. **Risk score** — apply every rule in `scoring_rules.json`, clamp to `0–100`
5. **Decision bands** (from `decision_bands.json`):
   - `0–49` → `AUTO_APPROVE` (omit `reason`)
   - `50–74` → `MANUAL_REVIEW` + `MEDIUM_RISK_SCORE`
   - `75–100` → `REJECT` + `HIGH_RISK_SCORE`

## Layout

```
return-routing-engine/
  README.md
  SOLUTION.md                 # short “paste this” summary
  src/engine.cpp              # fixed C++ engine (challenge style)
  include/engine.hpp
  src/main.cpp
  CMakeLists.txt
  engine.py                   # runnable reference implementation
  data/                       # sample configs + inputs
  run_demo.py                 # end-to-end demo
```

## Run the demo

```bash
cd return-routing-engine
python3 run_demo.py
```

Writes `data/results.jsonl` and prints each decision.