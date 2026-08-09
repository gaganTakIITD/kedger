# Return Routing Engine — Fixed Solution

Standalone fix for the broken return routing engine (Question 2).

## The Bug

Links were stored **one-way only**:

```cpp
// BUG: only primary -> related
account_groups[link.primary_account_id].insert(link.related_account_id);
```

If the data says `u201 -> u202`, then `u201` could see `u202`, but `u202` could **not** see `u201`.  
Risk lookup starts from the request's own `account_id`, so linked accounts on the "other side" got **too-low** `total_return_history` totals.

## The Fix

Store links **bidirectionally**, then run transitive closure:

```cpp
account_groups[link.primary_account_id].insert(link.related_account_id);
account_groups[link.related_account_id].insert(link.primary_account_id);
```

## Routing Logic (correct order)

1. **Category checks** (before scoring)
   - Unknown / non-returnable category → `REJECT`, `risk_score: null`, reason `CATEGORY_NON_RETURNABLE`
   - `days_since_purchase` > window → `REJECT`, `risk_score: null`, reason `RETURN_WINDOW_EXPIRED`

2. **Risk score**
   - `total_return_history` = own count + all transitively linked accounts (missing profiles = 0)
   - Sum points from `scoring_rules.json`, clamp 0–100

3. **Decision**
   - 0–49 → `AUTO_APPROVE` (no reason)
   - 50–74 → `MANUAL_REVIEW`, reason `MEDIUM_RISK_SCORE`
   - 75–100 → `REJECT`, reason `HIGH_RISK_SCORE`

## Build & Run

```bash
cd return-routing-engine
mkdir -p build && cd build
cmake ..
cmake --build .
./return_engine
cat ../data/results.jsonl
ctest
```

## Key Files

| File | Purpose |
|------|---------|
| `src/engine.cpp` | Core fix + routing logic |
| `src/engine.h` | Engine interface |
| `src/types.h` | Data structures |
| `src/json_io.h` | JSON load/write |
| `data/*.json(l)` | Config + sample input |

## Expected Sample Output

```
{"decision":"MANUAL_REVIEW","reason":"MEDIUM_RISK_SCORE","request_id":"r101","risk_score":50}
{"decision":"AUTO_APPROVE","request_id":"r102","risk_score":25}
{"decision":"MANUAL_REVIEW","reason":"MEDIUM_RISK_SCORE","request_id":"r103","risk_score":55}
{"decision":"REJECT","reason":"CATEGORY_NON_RETURNABLE","request_id":"r104","risk_score":null}
{"decision":"REJECT","reason":"RETURN_WINDOW_EXPIRED","request_id":"r105","risk_score":null}
```

Note: `r103` is the critical bidirectional-link case — `u202` must include `u201`'s history (1+6=7). Without the fix, `u202` would only count its own 6 returns and score lower.
