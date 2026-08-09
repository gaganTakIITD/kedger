"""Deterministic episode cognify (no LLM-every-turn)."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any

from kedger import SCHEMA_VERSION
from kedger.boundary import Boundary, detect_boundary
from kedger.boundary.segment import segment_continuity_score
from kedger.cognify.extract import Claim, extract_claims_from_span
from kedger.constants import EPISODE_SUMMARY_MAX, HEAT_TAU, RECURRENCE_PROMOTE_THETA
from kedger.handoff.compile import seal_handoff
from kedger.ids import new_id
from kedger.keys.principal import Principal
from kedger.store.db import Store, utc_now

# Kept for episode heat heuristics / back-compat imports in tests.
REJECT_RE = re.compile(
    r"\b(reject|don't|do not|never|avoid|instead of)\b", re.I
)
DECISION_RE = re.compile(r"\b(decide|decided|use|adopt|go with|we'll)\b", re.I)
CONSTRAINT_RE = re.compile(r"\b(must|always|require|only|shall)\b", re.I)


@dataclass
class CognifyResult:
    episode: dict[str, Any] | None
    boundary: Boundary | None
    candidates: list[dict[str, Any]] = field(default_factory=list)
    pruned_observations: int = 0
    pack_path: str | None = None
    skipped: bool = False
    skip_reason: str | None = None


def cognify_workstream(
    store: Store,
    *,
    principal: Principal,
    workstream_slug: str = "default",
    event_type: str = "cognify",
    force: bool = False,
    reseal: bool = True,
    min_span: int = 1,
) -> CognifyResult:
    ws = store.ensure_workstream(
        slug=workstream_slug,
        principal_id=principal.principal_id,
        signing_key=principal.signing_key,
    )
    ws_id = ws["id"]
    obs = store.list_observations(workstream_id=ws_id)
    last_ep = store.latest_episode(ws_id)
    since = last_ep["time_end"] if last_ep else None
    span = [o for o in obs if since is None or (o.get("ts") or "") > since]

    boundary = detect_boundary(
        event_type=event_type,
        force=force,
        last_obs_ts=span[-1]["ts"] if span else (obs[-1]["ts"] if obs else None),
        span_count=len(span),
        min_span=min_span,
        segment_score=segment_continuity_score(span) if len(span) >= 4 else None,
    )
    if boundary is None:
        return CognifyResult(
            episode=None, boundary=None, skipped=True, skip_reason="no_boundary"
        )
    if boundary.kind == "soft" and len(span) < min_span:
        return CognifyResult(
            episode=None,
            boundary=boundary,
            skipped=True,
            skip_reason="min_span",
        )
    if not span and not force:
        return CognifyResult(
            episode=None,
            boundary=boundary,
            skipped=True,
            skip_reason="empty_span",
        )

    now = utc_now()
    time_start = span[0]["ts"] if span else now
    time_end = span[-1]["ts"] if span else now
    summaries = [o.get("summary") or "" for o in span]
    # Capture gate: digest from extracted claims, not whole rambling turns.
    claims = extract_claims_from_span(span) if span else []
    failed = [c.statement for c in claims if c.kind == "rejection"][:20]
    next_steps = [
        c.statement for c in claims if c.kind in {"next_step", "decision"}
    ][:20]
    constraints = [c.statement for c in claims if c.kind == "constraint"][:12]
    files: list[str] = []
    for o in span:
        for h in o.get("entity_hints") or []:
            if isinstance(h, dict) and h.get("entity_type") == "file" and h.get("name"):
                if h["name"] not in files:
                    files.append(h["name"])
    files = files[:40]

    active = store.ranked_active_anchors(workstream_id=ws_id)

    # Deterministic digest summary — prefer span judgments; else active Anchors
    # (dogfood: remember-only then --force must not yield empty "Episode (cognify)").
    digest_bits = []
    if constraints:
        digest_bits.append("Constraints: " + "; ".join(constraints[:3]))
    if failed:
        digest_bits.append("Rejected: " + "; ".join(failed[:3]))
    if next_steps:
        digest_bits.append("Next: " + "; ".join(next_steps[:3]))
    if files:
        digest_bits.append("Files: " + ", ".join(files[:8]))
    if not digest_bits and active:
        # S3 refine: empty observation span + force → digest from Anchors (Batch4/PrefEval)
        bits = [
            f"[{a.get('kind')}] {a.get('statement')}"
            for a in active[:5]
            if a.get("statement")
        ]
        if bits:
            digest_bits.append("Anchors: " + "; ".join(bits))
    if not digest_bits:
        digest_bits.append(
            summaries[-1][:200] if summaries else f"Episode ({boundary.reason})"
        )
    summary = " | ".join(digest_bits)[:EPISODE_SUMMARY_MAX]
    heat = min(10.0, 0.5 * len(span) + 1.0 * len(failed) + 0.2 * len(files))
    episode = {
        "schema_version": SCHEMA_VERSION,
        "id": new_id("ep"),
        "repo_fingerprint": store.repo_fingerprint,
        "workstream_id": ws_id,
        "session_ids": sorted({o.get("session_id") for o in span if o.get("session_id")}),
        "time_start": time_start,
        "time_end": time_end,
        "branch": None,
        "summary": summary,
        "failed_approaches": failed,
        "next_steps": next_steps,
        "files_touched": files,
        "anchor_ids": [a["id"] for a in active[:20]],
        "entity_ids": [],
        "observation_span": {
            "from_ts": time_start,
            "to_ts": time_end,
            "count": len(span),
            "observation_ids": [o["id"] for o in span],
        },
        "salient_evidence_ids": [],
        "importance": min(1.0, 0.4 + heat / 20.0),
        "visibility": "workstream_private",
        "created_at": now,
        "heat": heat,
        "boundary": {"kind": boundary.kind, "reason": boundary.reason},
        "digest_v1": True,
    }
    if last_ep:
        episode["prev_episode_id"] = last_ep["id"]

    store.insert_episode(episode)
    if last_ep:
        store.insert_edge(
            edge_type="NEXT_IN",
            from_id=last_ep["id"],
            to_id=episode["id"],
            workstream_id=ws_id,
        )

    # Soft-patch working state
    working = store.get_working_state(ws_id) or {
        "schema_version": SCHEMA_VERSION,
        "id": new_id("wk"),
        "workstream_id": ws_id,
        "repo_fingerprint": store.repo_fingerprint,
        "goal": ws.get("name") or ws.get("slug") or "",
        "last_user_ask": "",
        "files_in_flight": [],
        "open_questions": [],
        "blockers": [],
        "active_branch": None,
        "active_anchor_ids": [],
        "updated_at": now,
        "updated_by_session_id": "cognify",
        "visibility": "workstream_private",
    }
    working = dict(working)
    working["files_in_flight"] = files[:40] or working.get("files_in_flight") or []
    working["active_anchor_ids"] = episode["anchor_ids"][:12]
    working["updated_at"] = now
    working["updated_by_session_id"] = "cognify"
    store.upsert_working_state(working)

    candidates = _emit_candidates(
        store,
        ws_id=ws_id,
        span=span,
        heat=heat,
        active_anchors=active,
        claims=claims,
    )

    # L0 prune payloads after episode — keep rows/ids for provenance, clear payload bodies
    pruned = store.prune_observation_payloads([o["id"] for o in span])

    pack_path = None
    if reseal:
        try:
            path, _pack = seal_handoff(
                store, principal=principal, workstream_slug=workstream_slug
            )
            pack_path = str(path)
            # COMPILED_INTO edge
            store.insert_edge(
                edge_type="COMPILED_INTO",
                from_id=episode["id"],
                to_id=_pack["id"],
                workstream_id=ws_id,
            )
        except Exception:  # noqa: BLE001
            pack_path = None

    return CognifyResult(
        episode=episode,
        boundary=boundary,
        candidates=candidates,
        pruned_observations=pruned,
        pack_path=pack_path,
    )


def _emit_candidates(
    store: Store,
    *,
    ws_id: str,
    span: list[dict[str, Any]],
    heat: float,
    active_anchors: list[dict[str, Any]] | None = None,
    claims: list[Claim] | None = None,
) -> list[dict[str, Any]]:
    """Tier A/B/C promotion candidates — never auto-share.

    Candidates are **extracted claims**, not whole observation summaries.
    """
    out: list[dict[str, Any]] = []
    counts: dict[str, int] = {}
    claim_list = list(claims) if claims is not None else extract_claims_from_span(span)

    # Empty span (force after remember-only): recurrence evidence from active Anchors
    # only — do not invent new statements (HaluMem).
    if not claim_list and not span and active_anchors:
        for a in active_anchors:
            stmt = (a.get("statement") or "").strip()
            if not stmt:
                continue
            claim_list.append(
                Claim(
                    kind=str(a.get("kind") or "gotcha"),
                    statement=stmt[:240],
                    tier="B",
                    source_type="anchor",
                    source_obs_id=None,
                    labeled=False,
                )
            )

    # Recurrence boost for identical claim text across the span
    for c in claim_list:
        key = c.statement.lower()[:120]
        counts[key] = counts.get(key, 0) + 1

    for c in claim_list:
        s = c.statement.strip()
        if not s:
            continue
        key = s.lower()[:120]
        kind = c.kind
        tier = c.tier
        if tier == "B" and (
            counts[key] >= RECURRENCE_PROMOTE_THETA or heat >= HEAT_TAU
        ):
            tier = "B"
        elif kind == "gotcha" and (
            counts[key] >= RECURRENCE_PROMOTE_THETA or heat >= HEAT_TAU
        ):
            tier = "B"
        # Skip exact duplicate of an already-active Anchor statement
        if active_anchors and any(
            (a.get("statement") or "").strip().lower() == s.lower()
            and a.get("kind") == kind
            for a in active_anchors
        ):
            continue
        cand = {
            "schema_version": SCHEMA_VERSION,
            "id": new_id("anc"),  # candidate id namespace reuse anc_ prefix as pending
            "tier": tier,
            "kind": kind,
            "statement": s[:240],
            "status": "candidate",
            "heat": heat,
            "recurrence": counts[key],
            "workstream_id": ws_id,
            "created_at": utc_now(),
            "shareable": False,  # explicit_only — never auto-share
            "source_observation_id": c.source_obs_id,
            "source_type": c.source_type,
            "labeled": c.labeled,
        }
        store.insert_promotion_candidate(cand)
        out.append(cand)
    return out
