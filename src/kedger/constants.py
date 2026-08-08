"""Cross-cutting locked constants (schemas + literature cheat sheet)."""

from __future__ import annotations

SCHEMA_VERSION = "kedger.memory.v1"
PACK_SCHEMA = "kedger.pack.v1"
SHARE_MODE = "explicit_only"

# Budgets
WORKING_MAX_BYTES = 4096
HANDOFF_MAX_BYTES = 32768
ANCHOR_STATEMENT_MAX = 240
ANCHOR_REASON_MAX = 480
EPISODE_SUMMARY_MAX = 1200
EVIDENCE_SNIPPET_MAX = 280
FILES_IN_FLIGHT_MAX = 40
FILES_IN_FLIGHT_SOFT = 12

# L0 retention (enforce both)
L0_MAX_AGE_HOURS = 72
L0_MAX_ROWS_PER_WORKSTREAM = 5000
L0_MAX_AGE_DAYS_SCHEMA = 7
L0_MAX_BYTES = 50 * 1024 * 1024
L0_WARN_RATIO = 0.70
L0_FLUSH_RATIO = 0.85

# Promotion / cognify
RECURRENCE_PROMOTE_THETA = 3
HEAT_TAU = 5
CORE_REWRITE_RATIO = 0.90
SEGMENT_THETA = 0.60
IDLE_BOUNDARY_MINUTES = 25
PROBATION_DAYS = 7
PPR_DAMPING = 0.5
ALIAS_TAU = 0.8
RECENCY_MU_SECONDS = 1.0e7

# Workstream resolver
WS_JOIN_THRESHOLD = 3.0
WS_CREATE_THRESHOLD = 2.0
WS_AMBIGUOUS_GAP = 0.7

SURVIVAL_RANK = {
    "constraint": 0,
    "rejection": 1,
    "decision": 2,
    "goal": 3,
    "next_step": 4,
    "open_question": 5,
    "gotcha": 6,
}

SHARE_KIND_ALLOWLIST = frozenset({"constraint", "rejection", "decision", "gotcha"})

# Inv-Scope
NOT_FOUND_CODE = 404
NOT_FOUND_MSG = "not found"
