# Final Solution (copy-paste)

## Critical bug fix (account links)

Links are undirected groups. Store **both** directions, then close transitively:

```cpp
for (const auto& link : links) {
    account_groups[link.primary_account_id].insert(link.related_account_id);
    account_groups[link.related_account_id].insert(link.primary_account_id);  // FIX
}
```

Without the reverse edge, if data has `u201 → u202`, looking up `u202` never sees `u201`, so risk totals are too low.

## Decision order

1. Category returnable? else `REJECT` / `CATEGORY_NON_RETURNABLE` / `risk_score=null`
2. Within return window? else `REJECT` / `RETURN_WINDOW_EXPIRED` / `risk_score=null`
3. `return_history_total` = own count + all linked counts (missing = 0)
4. Score from `scoring_rules.json`, clamp `[0, 100]`
5. Map score via `decision_bands.json`; add reason only for `MANUAL_REVIEW` / `REJECT`

## Output shape

```json
{"request_id":"r101","risk_score":35,"decision":"AUTO_APPROVE"}
{"request_id":"r102","risk_score":null,"decision":"REJECT","reason":"CATEGORY_NON_RETURNABLE"}
{"request_id":"r103","risk_score":60,"decision":"MANUAL_REVIEW","reason":"MEDIUM_RISK_SCORE"}
{"request_id":"r104","risk_score":80,"decision":"REJECT","reason":"HIGH_RISK_SCORE"}
```

See `src/engine.cpp` (C++) or `engine.py` (runnable Python).