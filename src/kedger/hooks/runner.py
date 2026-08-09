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
            # Skip empty/sessionStart JSON previews — they pollute zlib transcript tape
            summary = (obs.get("summary") or "").strip()
            otype = obs.get("type") or ""
            if otype == "session_start" and (
                not summary
                or summary.startswith("{")
                or summary.lower() in {"sessionstart", "session_start"}
            ):
                results["side_effects"].append(
                    {"effect": "ingest", "status": "skipped_empty_session_start"}
                )
                continue
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
            # If live store has no Anchors yet, try HEAD pack auto-import (cross-session)
            if not proj.anchors:
                try:
                    from kedger.handoff.compile import hydrate_pack
                    from kedger.store.paths import project_dir

                    packs_dir = (
                        project_dir(store.repo_fingerprint)
                        / "packs"
                        / resolved.workstream["id"]
                    )
                    head = packs_dir / "HEAD"
                    if head.exists():
                        hid = head.read_text(encoding="utf-8").strip()
                        kxp = packs_dir / f"{hid}.kxp"
                        if kxp.exists():
                            hydrate_pack(
                                store,
                                principal=principal,
                                pack_path=kxp,
                                import_memory=True,
                                workstream_slug=workstream_slug,
                            )
                            proj = project_hydrate(
                                store,
                                principal_id=principal.principal_id,
                                workstream_id=resolved.workstream["id"],
                            )
                except Exception:  # noqa: BLE001 — best-effort continuity
                    pass
            activity = (proj.working or {}).get("activity") or {}
            tmeta = (proj.working or {}).get("transcript_meta")
            has_memory = bool(proj.anchors) or bool(activity.get("files")) or bool(
                tmeta and tmeta.get("turn_count")
            )
            if not has_memory:
                # Don't burn model context on empty boots
                results["additionalContext"] = None
                results["side_effects"].append(
                    {
                        "effect": "hydrate_inject",
                        "anchors": 0,
                        "status": "empty",
                    }
                )
                continue
            lines = ["# Kedger hydrate", ""]
            lines.append("## Base memory (Anchors)")
            if proj.working and proj.working.get("goal"):
                lines.append(f"Goal: {proj.working['goal']}")
            if proj.working and proj.working.get("last_agent_action"):
                lines.append(f"Last agent: {proj.working['last_agent_action'][:160]}")
            for a in proj.anchors[:20]:
                lines.append(f"- [{a['kind']}] {a['statement']}")
            # Advanced ops layer — what the agent did (survives compact)
            from kedger.cognify.activity import activity_inject_lines
            from kedger.handoff.transcript import transcript_inject_lines

            lines.extend(activity_inject_lines(activity))
            # Transfer layer — zlib archive pointer + short recent-turn preview
            preview_turns = None
            try:
                from kedger.handoff.transcript import (
                    decompress_transcript,
                    resolve_transcript_archive,
                )
                from kedger.store.paths import project_dir

                ep = store.latest_episode(resolved.workstream["id"])
                packs_root = (
                    project_dir(store.repo_fingerprint)
                    / "packs"
                    / resolved.workstream["id"]
                )
                archive = None
                if ep:
                    archive = resolve_transcript_archive(ep, sidecar_root=packs_root)
                if archive is None and tmeta and tmeta.get("sidecar"):
                    archive = resolve_transcript_archive(
                        {"transcript_meta": tmeta}, sidecar_root=packs_root
                    )
                if archive and archive.get("blob_b64"):
                    preview_turns = decompress_transcript(archive)
            except Exception:  # noqa: BLE001
                preview_turns = None
            lines.extend(
                transcript_inject_lines(tmeta, turns=preview_turns, tail=4)
            )
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
                reseal=False,  # reseal after promote so pack includes Anchors
            )
            promoted = 0
            seal_err = None
            if not cog.skipped and cog.episode is not None:
                from kedger.promote import promote_candidates

                out = promote_candidates(
                    store,
                    principal=principal,
                    workstream_id=resolved.workstream["id"],
                    mode="conservative",
                )
                promoted = len(out)
                try:
                    from kedger.handoff.compile import seal_handoff

                    path, _pack = seal_handoff(
                        store,
                        principal=principal,
                        workstream_slug=workstream_slug,
                    )
                    cog.pack_path = str(path)
                except Exception as e:  # noqa: BLE001
                    seal_err = str(e)[:160]
            results["side_effects"].append(
                {
                    "effect": "cognify_hard",
                    "episode": None if cog.skipped else (cog.episode or {}).get("id"),
                    "skipped": cog.skipped,
                    "promoted": promoted,
                    "pack": cog.pack_path,
                    **({"seal_error": seal_err} if seal_err else {}),
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


def format_ide_stdout(
    result: dict[str, Any],
    *,
    source: str = "generic",
    event_name: str | None = None,
) -> str:
    """JSON line for IDE hook stdout (shape differs by adapter)."""
    ctx = result.get("additionalContext")
    if source == "cursor":
        # Cursor sessionStart consumes additional_context (snake_case).
        out: dict[str, Any] = {"ok": bool(result.get("ok", True))}
        if ctx:
            out["additional_context"] = ctx
            out["additionalContext"] = ctx  # compat for tests / older callers
        if result.get("side_effects") is not None:
            out["side_effects"] = result["side_effects"]
        if result.get("observation_id") is not None:
            out["observation_id"] = result["observation_id"]
        return json.dumps(out, sort_keys=True)
    if source == "claude_code":
        # Claude Code SessionStart: hookSpecificOutput.additionalContext
        out = {"ok": bool(result.get("ok", True))}
        if ctx:
            out["hookSpecificOutput"] = {
                "hookEventName": event_name or "SessionStart",
                "additionalContext": ctx,
            }
            out["additionalContext"] = ctx  # compat
        if result.get("side_effects") is not None:
            out["side_effects"] = result["side_effects"]
        if result.get("observation_id") is not None:
            out["observation_id"] = result["observation_id"]
        return json.dumps(out, sort_keys=True)
    return json.dumps(result, sort_keys=True)
