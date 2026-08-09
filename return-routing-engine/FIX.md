# One-Line Fix for `engine.cpp`

## Problem
Account links were stored only one way (`primary → related`).  
Lookup starts from the request's `account_id`, so the other side of a link could not see the full linked group.

## Change (lines ~37–39)

**Before (buggy):**
```cpp
for (const auto& link : links) {
    account_groups[link.primary_account_id].insert(link.related_account_id);
}
```

**After (fixed):**
```cpp
for (const auto& link : links) {
    account_groups[link.primary_account_id].insert(link.related_account_id);
    account_groups[link.related_account_id].insert(link.primary_account_id);
}
```

Keep the existing transitive-closure `while (changed)` loop unchanged — it already works once links are bidirectional.

## Full routing checklist

1. Reject non-returnable / unknown categories → `CATEGORY_NON_RETURNABLE`, `risk_score = null`
2. Reject expired window → `RETURN_WINDOW_EXPIRED`, `risk_score = null`
3. Compute `total_return_history` = own + all linked (transitive) accounts
4. Score from `scoring_rules.json`, clamp 0–100
5. Decision: 0–49 `AUTO_APPROVE`, 50–74 `MANUAL_REVIEW`, 75–100 `REJECT`
6. Reason only for review/reject: `MEDIUM_RISK_SCORE` / `HIGH_RISK_SCORE`
