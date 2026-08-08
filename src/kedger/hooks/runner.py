"""Execute normalized hook side effects via in-process APIs (CLI-equivalent)."""

from __future__ import annotations

import json
from typing import Any

from kedger.cognify import cognify_workstream
from kedger.hydrate import project_hydrate
from kedger.hooks.normalize import normalize_hook_event
from kedger.keys.principal import Principal
from kedger.store.db import Store
from kedger.workstream import resolve_workstream


def run_hook(
    store: Store,
    *,
    principal: Principal,
    payload: dict[str, Any],
    source: str = "generic",
    workstream_slug: str = "default",
) -> dict[str, Any]:
    """
    Adapter contract: parse → Observation → side_effects → IDE stdout JSON.
    Core never imports IDE-specific types.
    """
    normalized = normalize_hook_event(payload, source=source)
    obs = dict(normalized["observation"])
    resolved = resolve_workstream(
        store, principal=principal, explicit_slug=workstream_slug
    )
    if resolved.workstream is None:
        return {
            "ok": False,
            "error": "not found",
            "code": 404,
            "side_effects": [],
        }
    obs["workstream_id"] = obs.get("workstream_id") or resolved.workstream["id"]

    results: dict[str, Any] = {
        "ok": True,
        "observation_id": None,
        "side_effects": [],
        "additionalContext": None,
        "code": 0,
    }

    for effect in normalized["side_effects"]:
        if effect == "ingest":
            record = store.ingest_observation(obs, principal_id=principal.principal_id)
            results["observation_id"] = record["id"]
            results["side_effects"].append({"effect": "ingest", "id": record["id"]})
        elif effect == "hydrate_inject":
            try:
                proj = project_hydrate(
                    store,
                    principal_id=principal.principal_id,
                    workstream_id=resolved.workstream["id"],
                )
            except Exception:  # noqa: BLE001 — Inv-Scope / missing
                results["side_effects"].append(
                    {"effect": "hydrate_inject", "status": "not found", "code": 404}
                )
                continue
            lines = ["# Kedger hydrate", ""]
            if proj.working and proj.working.get("goal"):
                lines.append(f"Goal: {proj.working['goal']}")
            for a in proj.anchors[:20]:
                lines.append(f"- [{a['kind']}] {a['statement']}")
            ctx = "\n".join(lines)
            results["additionalContext"] = ctx
            results["side_effects"].append(
                {
                    "effect": "hydrate_inject",
                    "anchors": len(proj.anchors),
                    "status": "ok",
                }
            )
        elif effect == "cognify_hard":
            cog = cognify_workstream(
                store,
                principal=principal,
                workstream_slug=workstream_slug,
                event_type=obs["type"],
                force=True,
                reseal=True,
            )
            results["side_effects"].append(
                {
                    "effect": "cognify_hard",
                    "episode": None if cog.skipped else cog.episode["id"],
                    "skipped": cog.skipped,
                }
            )
        elif effect == "boundary_soft":
            cog = cognify_workstream(
                store,
                principal=principal,
                workstream_slug=workstream_slug,
                event_type="turn_stop",
                force=False,
                reseal=False,
            )
            results["side_effects"].append(
                {
                    "effect": "boundary_soft",
                    "skipped": cog.skipped,
                    "skip_reason": cog.skip_reason,
                }
            )

    return results


def format_ide_stdout(result: dict[str, Any]) -> str:
    """JSON line for IDE hook stdout."""
    return json.dumps(result, sort_keys=True)
