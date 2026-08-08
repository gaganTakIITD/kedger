"""kedger CLI — store, keys, remember/forget, sealed handoff."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import click

from kedger import SCHEMA_VERSION, __version__
from kedger.acl import InvScopeError
from kedger.cognify import cognify_workstream
from kedger.crypto.kxp import KxpError
from kedger.handoff import hydrate_pack, seal_handoff
from kedger.hooks.runner import format_ide_stdout, run_hook
from kedger.hydrate import project_hydrate
from kedger.ingest import ingest_from_hook
from kedger.keys import KeysError, init_principal, load_principal
from kedger.keys.principal import export_recipient
from kedger.policy import ensure_repo_policy
from kedger.promote import promote_candidates
from kedger.remember import forget_anchor, remember_anchor
from kedger.share import share_anchor, unshare_anchor
from kedger.store import Store, kedger_home, repo_fingerprint, repo_material, store_path
from kedger.store.db import KIND_ALIASES
from kedger.store.paths import keys_dir
from kedger.why import explain_anchor
from kedger.workstream import resolve_workstream


def _die(msg: str, code: int = 1) -> None:
    click.echo(f"error: {msg}", err=True)
    raise SystemExit(code)


def _require_principal():
    try:
        return load_principal()
    except KeysError as e:
        _die(str(e))


def _open_store() -> Store:
    fp = repo_fingerprint()
    return Store.open(fp)


@click.group()
@click.version_option(__version__, prog_name="kedger")
def main() -> None:
    """Kedger — local-first engineering memory CLI.

    Kedger is not MoDeX. Product locks: ~/.kedger/, .kxp, kedger.memory.v1.
    """


@main.group("keys")
def keys_group() -> None:
    """Manage local Ed25519 + X25519 principal keys."""


@keys_group.command("init")
@click.option("--name", default="default", show_default=True, help="Principal display name")
@click.option("--force", is_flag=True, help="Rotate / overwrite existing principal")
def keys_init(name: str, force: bool) -> None:
    """Create a local Ed25519 identity + X25519 recipient under ~/.kedger/keys/."""
    try:
        principal = init_principal(name=name, force=force)
    except KeysError as e:
        _die(str(e))
    click.echo(f"principal_id: {principal.principal_id}")
    click.echo(f"name:         {principal.name}")
    click.echo(f"public_key:   {principal.public_key_b64}")
    click.echo(f"x25519_public:{principal.x25519_public_b64}")
    click.echo(f"keys_dir:     {keys_dir()}")


@keys_group.command("show")
def keys_show() -> None:
    """Show principal id + public keys."""
    principal = _require_principal()
    click.echo(f"principal_id: {principal.principal_id}")
    click.echo(f"name:         {principal.name}")
    click.echo(f"public_key:   {principal.public_key_b64}")
    click.echo(f"x25519_public:{principal.x25519_public_b64}")
    click.echo(f"created_at:   {principal.created_at}")
    click.echo(f"keys_dir:     {keys_dir()}")


@keys_group.command("export-recipient")
@click.option(
    "--out",
    "out_path",
    type=click.Path(path_type=Path),
    default=None,
    help="Write recipient JSON to file (default: stdout)",
)
def keys_export_recipient(out_path: Path | None) -> None:
    """Export recipient key material for `kedger grant --recipient-file`."""
    principal = _require_principal()
    payload = json.dumps(export_recipient(principal), indent=2) + "\n"
    if out_path is None:
        click.echo(payload, nl=False)
    else:
        out_path.write_text(payload, encoding="utf-8")
        click.echo(f"wrote: {out_path}")


@main.command("remember")
@click.argument("kind")
@click.argument("statement")
@click.option("--reason", default=None, help="Why this Anchor exists")
@click.option("--shareable", is_flag=True, help="Explicit share (share_mode=explicit_only)")
@click.option("--workstream", default=None, help="Optional workstream id (ws_…)")
def remember_cmd(
    kind: str,
    statement: str,
    reason: str | None,
    shareable: bool,
    workstream: str | None,
) -> None:
    """Create an Anchor (decision/reject/constraint/…)."""
    principal = _require_principal()
    store = _open_store()
    ensure_repo_policy(repo_fingerprint=store.repo_fingerprint)
    try:
        record = remember_anchor(
            store,
            principal=principal,
            kind=kind,
            statement=statement,
            reason=reason,
            shareable=shareable,
            workstream_id=workstream,
        )
    except ValueError as e:
        _die(str(e))
    click.echo(f"id:      {record['id']}")
    click.echo(f"kind:    {record['kind']}")
    click.echo(f"status:  {record['status']}")
    click.echo(f"statement: {record['statement']}")
    if record.get("reason"):
        click.echo(f"reason:  {record['reason']}")


@main.command("forget")
@click.argument("anchor_id")
def forget_cmd(anchor_id: str) -> None:
    """Invalidate an Anchor via SUPERSEDES — never hard-delete."""
    principal = _require_principal()
    store = _open_store()
    try:
        result = forget_anchor(store, principal=principal, anchor_id=anchor_id)
    except KeyError:
        _die("not found", code=404)
    except ValueError as e:
        _die(str(e))
    forgotten = result["forgotten"]
    tomb = result["tombstone"]
    edge = result["edge"]
    click.echo(f"forgotten:     {forgotten['id']} (status={forgotten['status']})")
    click.echo(f"superseded_by: {tomb['id']}")
    click.echo(f"edge:          {edge['id']} SUPERSEDES")


@main.command("status")
@click.option("--list", "list_anchors", is_flag=True, help="List active Anchors")
def status_cmd(list_anchors: bool) -> None:
    """Show fingerprint, store path, and counts."""
    fp = repo_fingerprint()
    material = repo_material()
    path = store_path(fp)
    home = kedger_home()
    click.echo(f"schema:            {SCHEMA_VERSION}")
    click.echo(f"kedger_home:       {home}")
    click.echo(f"repo_fingerprint:  {fp}")
    click.echo(f"repo_material:     {material}")
    click.echo(f"store:             {path}")
    if not path.exists():
        click.echo("counts:            (store not initialized)")
        return
    store = Store.open(fp)
    counts = store.counts()
    click.echo(
        "counts:            "
        f"active={counts['anchors_active']} "
        f"superseded={counts['anchors_superseded']} "
        f"total_anchors={counts['anchors_total']} "
        f"observations={counts['observations']} "
        f"supersedes_edges={counts['supersedes_edges']}"
    )
    if list_anchors:
        anchors = store.list_anchors(active_only=True)
        if not anchors:
            click.echo("anchors:           (none active)")
            return
        click.echo("anchors:")
        for a in anchors:
            reason = f" — {a['reason']}" if a.get("reason") else ""
            click.echo(f"  {a['id']}  [{a['kind']}] {a['statement']}{reason}")


@main.command("doctor")
def doctor_cmd() -> None:
    """Run health checks for the local Kedger install."""
    checks: list[tuple[str, bool, str]] = []

    home = kedger_home()
    home.mkdir(parents=True, exist_ok=True)
    checks.append(("kedger_home", home.is_dir(), str(home)))

    try:
        principal = load_principal()
        checks.append(
            ("principal", True, f"{principal.principal_id} ({principal.name})")
        )
        checks.append(("signing_key", principal.signing_key is not None, "present" if principal.signing_key else "missing"))
    except KeysError as e:
        checks.append(("principal", False, str(e)))
        principal = None

    fp = repo_fingerprint()
    path = store_path(fp)
    if path.exists():
        try:
            store = Store.open(fp)
            meta = store.meta()
            ok = meta.get("schema_version") == SCHEMA_VERSION
            checks.append(
                ("store", ok, f"{path} schema={meta.get('schema_version')}")
            )
            counts = store.counts()
            checks.append(
                (
                    "anchors",
                    True,
                    f"active={counts['anchors_active']} total={counts['anchors_total']}",
                )
            )
        except Exception as e:  # noqa: BLE001
            checks.append(("store", False, str(e)))
    else:
        checks.append(("store", True, f"not created yet ({path})"))

    kinds = ", ".join(sorted(set(KIND_ALIASES.values())))
    checks.append(("anchor_kinds", True, kinds))
    checks.append(
        (
            "identity_lock",
            True,
            "Kedger≠MoDeX; CLI=kedger; packs=.kxp; schema=kedger.memory.v1",
        )
    )
    checks.append(
        (
            "crypto_limits",
            True,
            "insider recipients can leak; metadata visible; revoke≠erase offline packs; TOFU on import",
        )
    )
    checks.append(("share_mode", True, "explicit_only"))

    failed = 0
    for name, ok, detail in checks:
        mark = "ok" if ok else "FAIL"
        if not ok:
            failed += 1
        click.echo(f"[{mark}] {name}: {detail}")
    if failed:
        raise SystemExit(1)
    click.echo("doctor: all checks passed")


@main.command("ingest")
@click.option("--from-hook", "from_hook", is_flag=True, required=True, help="Read observation JSON from stdin")
def ingest_cmd(from_hook: bool) -> None:
    """Ingest an L0 observation (typically from an IDE hook)."""
    if not from_hook:
        _die("--from-hook is required")
    principal = _require_principal()
    raw = sys.stdin.read()
    if not raw.strip():
        _die("empty stdin; expected JSON observation")
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as e:
        _die(f"invalid JSON: {e}")
    if not isinstance(payload, dict):
        _die("observation JSON must be an object")
    store = _open_store()
    ensure_repo_policy(repo_fingerprint=store.repo_fingerprint)
    record = ingest_from_hook(store, payload, principal=principal)
    click.echo(f"id:      {record['id']}")
    click.echo(f"type:    {record['type']}")
    click.echo(f"summary: {record['summary']}")
    if record.get("redacted"):
        click.echo("redacted: true")
    pressure = record.get("l0_pressure") or {}
    if pressure.get("warn"):
        click.echo(
            f"l0_pressure: warn count={pressure.get('count')} "
            f"flushed={pressure.get('flushed')}"
        )


@main.command("handoff")
@click.option("--workstream", default="default", show_default=True, help="Workstream slug")
@click.option(
    "--out",
    "out_path",
    type=click.Path(path_type=Path),
    default=None,
    help="Output .kxp path",
)
@click.option(
    "--include-shared",
    is_flag=True,
    help="Opt-in ranked shared-anchor facet (anti pack-deputy; off by default)",
)
def handoff_cmd(workstream: str, out_path: Path | None, include_shared: bool) -> None:
    """Compile active Anchors into a sealed `.kxp` handoff pack."""
    principal = _require_principal()
    store = _open_store()
    try:
        path, pack = seal_handoff(
            store,
            principal=principal,
            workstream_slug=workstream,
            output=out_path,
            include_shared=include_shared,
        )
    except KeyError:
        _die("not found", code=404)
    except Exception as e:  # noqa: BLE001
        _die(str(e))
    click.echo(f"handoff_id:   {pack['id']}")
    click.echo(f"workstream:   {pack['workstream_id']}")
    click.echo(f"anchors:      {len(pack['anchors'])}")
    click.echo(f"pack:         {path}")


@main.command("hydrate")
@click.option(
    "--pack",
    "pack_path",
    type=click.Path(path_type=Path, exists=False),
    default=None,
    help="Path to .kxp pack",
)
@click.option("--live", is_flag=True, help="Project from live store (ranked hydrate)")
@click.option("--workstream", default="default", show_default=True)
@click.option("--topic", default=None, help="Active retrieval topic hint")
@click.option(
    "--walk-budget",
    default=16,
    show_default=True,
    type=int,
    help="GraphReader-style associative expand node budget",
)
def hydrate_cmd(
    pack_path: Path | None,
    live: bool,
    workstream: str,
    topic: str | None,
    walk_budget: int,
) -> None:
    """Authorized hydrate of a sealed `.kxp` pack or live ranked projection."""
    principal = _require_principal()
    store = _open_store()
    if live or pack_path is None:
        resolved = resolve_workstream(
            store, principal=principal, explicit_slug=workstream
        )
        if resolved.workstream is None:
            _die("not found", code=404)
        try:
            proj = project_hydrate(
                store,
                principal_id=principal.principal_id,
                workstream_id=resolved.workstream["id"],
                topic=topic,
                walk_budget=walk_budget,
            )
        except InvScopeError:
            _die("not found", code=404)
        click.echo(f"workstream:   {resolved.workstream['id']}")
        click.echo(f"anchors:      {len(proj.anchors)}")
        click.echo(f"used_bytes:   {proj.used_bytes}")
        click.echo(f"walk_budget:  {proj.walk_budget} (expanded={len(proj.walk_ids)})")
        if proj.conflicts:
            # Knowledge Conflicts / Adaptive Chameleon: surface both views
            click.echo(f"conflicts:    {len(proj.conflicts)}")
            for c in proj.conflicts[:12]:
                click.echo(
                    "  ! {ctype} action={action} {left} vs {right}".format(
                        ctype=c.get("type") or "conflict",
                        action=c.get("action") or "?",
                        left=c.get("left_id") or "?",
                        right=c.get("right_id") or "?",
                    )
                )
        for a in proj.anchors:
            click.echo(f"  [{a['kind']}] {a['statement']}")
        return
    try:
        opened = hydrate_pack(store, principal=principal, pack_path=pack_path)
    except KxpError:
        _die("not found", code=404)
    except KeyError:
        _die("not found", code=404)
    payload = opened["payload"]
    click.echo(f"handoff_id:   {payload['id']}")
    click.echo(f"workstream:   {payload['workstream_id']}")
    click.echo(f"anchors:      {len(payload.get('anchors') or [])}")
    click.echo(f"from:         {payload.get('from_principal_id')}")
    for a in payload.get("anchors") or []:
        click.echo(f"  [{a['kind']}] {a['statement']}")


@main.command("grant")
@click.option("--workstream", default="default", show_default=True, help="Workstream slug")
@click.option("--to", "to_principal", required=True, help="Grantee principal id (pr_…)")
@click.option(
    "--recipient-file",
    type=click.Path(path_type=Path, exists=True),
    required=True,
    help="JSON from `kedger keys export-recipient`",
)
@click.option(
    "--permission",
    "permissions",
    multiple=True,
    default=["read_hydrate"],
    show_default=True,
    help="Capability permission (repeatable)",
)
def grant_cmd(
    workstream: str,
    to_principal: str,
    recipient_file: Path,
    permissions: tuple[str, ...],
) -> None:
    """Grant workstream capability and register recipient X25519 key."""
    principal = _require_principal()
    store = _open_store()
    try:
        recip = json.loads(recipient_file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        _die(f"invalid recipient file: {e}")
    if recip.get("principal_id") and recip["principal_id"] != to_principal:
        _die("recipient-file principal_id does not match --to")
    ws = store.ensure_workstream(
        slug=workstream,
        principal_id=principal.principal_id,
        signing_key=principal.signing_key,
    )
    try:
        cap = store.grant(
            workstream_id=ws["id"],
            grantee_principal_id=to_principal,
            issuer_principal_id=principal.principal_id,
            permissions=list(permissions),
            grantee_public_key_b64=recip["public_key_b64"],
            grantee_x25519_public_b64=recip["x25519_public_b64"],
            grantee_name=recip.get("name", "peer"),
            signing_key=principal.signing_key,
        )
    except KeyError:
        _die("not found", code=404)
    click.echo(f"capability:   {cap['id']}")
    click.echo(f"workstream:   {ws['id']}")
    click.echo(f"grantee:      {to_principal}")
    click.echo(f"permissions:  {', '.join(cap['permissions'])}")


@main.command("revoke")
@click.option("--workstream", default="default", show_default=True, help="Workstream slug")
@click.option("--from", "from_principal", required=True, help="Principal id to revoke")
@click.option(
    "--no-reseal",
    is_flag=True,
    help="Skip auto-reseal (not recommended — revoke without reseal is theater)",
)
def revoke_cmd(workstream: str, from_principal: str, no_reseal: bool) -> None:
    """Revoke workstream capability and auto-reseal live pack (epoch++)."""
    principal = _require_principal()
    store = _open_store()
    ws = store.get_workstream_by_slug(workstream)
    if ws is None:
        _die("not found", code=404)
    try:
        result = store.revoke(
            workstream_id=ws["id"],
            grantee_principal_id=from_principal,
            issuer_principal_id=principal.principal_id,
        )
    except KeyError:
        _die("not found", code=404)
    click.echo(f"revoked:      {result['revoked']}")
    click.echo(f"workstream:   {result['workstream_id']}")
    if not no_reseal:
        try:
            path, pack = seal_handoff(
                store, principal=principal, workstream_slug=workstream
            )
            click.echo(f"resealed:     {pack['id']} -> {path}")
            click.echo("note:         old .kxp files remain openable with old recipient keys")
        except Exception as e:  # noqa: BLE001
            click.echo(f"reseal_error: {e}", err=True)
            click.echo("note:         run `kedger handoff` to reseal")
    else:
        click.echo("note:         --no-reseal set; run `kedger handoff` for a new epoch")


@main.command("share")
@click.argument("anchor_id")
def share_cmd(anchor_id: str) -> None:
    """Explicit share Anchor to repo_shared_safe (share_mode=explicit_only)."""
    principal = _require_principal()
    store = _open_store()
    # Ensure actor has a workstream capability context
    store.ensure_workstream(
        slug="default",
        principal_id=principal.principal_id,
        signing_key=principal.signing_key,
    )
    try:
        anc = share_anchor(
            store, anchor_id=anchor_id, principal_id=principal.principal_id
        )
    except InvScopeError:
        _die("not found", code=404)
    except ValueError as e:
        _die(str(e))
    click.echo(f"id:         {anc['id']}")
    click.echo(f"shareable:  {anc['shareable']}")
    click.echo(f"visibility: {anc['visibility']}")


@main.command("unshare")
@click.argument("anchor_id")
def unshare_cmd(anchor_id: str) -> None:
    """Revoke shared projection; cascade stale packs."""
    principal = _require_principal()
    store = _open_store()
    try:
        anc = unshare_anchor(
            store, anchor_id=anchor_id, principal_id=principal.principal_id
        )
    except InvScopeError:
        _die("not found", code=404)
    click.echo(f"id:         {anc['id']}")
    click.echo(f"shareable:  {anc['shareable']}")
    click.echo(f"visibility: {anc['visibility']}")


@main.command("hook")
@click.option(
    "--source",
    type=click.Choice(["cursor", "claude_code", "generic"]),
    default="generic",
    show_default=True,
)
@click.option("--workstream", default="default", show_default=True)
def hook_cmd(source: str, workstream: str) -> None:
    """IDE hook entrypoint: stdin JSON → normalize → side effects → stdout JSON."""
    principal = _require_principal()
    store = _open_store()
    raw = sys.stdin.read()
    if not raw.strip():
        _die("empty stdin; expected hook JSON")
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as e:
        _die(f"invalid JSON: {e}")
    if not isinstance(payload, dict):
        _die("hook JSON must be an object")
    result = run_hook(
        store,
        principal=principal,
        payload=payload,
        source=source,
        workstream_slug=workstream,
    )
    event_name = (
        payload.get("hook_event_name")
        or payload.get("event")
        or payload.get("type")
        or payload.get("name")
    )
    click.echo(
        format_ide_stdout(
            result,
            source=source,
            event_name=str(event_name) if event_name else None,
        ),
        nl=True,
    )
    if not result.get("ok"):
        raise SystemExit(int(result.get("code") or 1))


@main.command("why")
@click.argument("anchor_id")
def why_cmd(anchor_id: str) -> None:
    """Explain an Anchor via provenance and SUPERSEDES chain."""
    principal = _require_principal()
    store = _open_store()
    try:
        explanation = explain_anchor(
            store, anchor_id=anchor_id, principal_id=principal.principal_id
        )
    except InvScopeError:
        _die("not found", code=404)
    click.echo(json.dumps(explanation, indent=2))


@main.command("promote")
@click.option("--workstream", default="default", show_default=True)
@click.option(
    "--mode",
    type=click.Choice(["conservative", "normal"]),
    default="conservative",
    show_default=True,
)
def promote_cmd(workstream: str, mode: str) -> None:
    """Promote Tier A/B candidates into Anchors (never auto-share)."""
    principal = _require_principal()
    store = _open_store()
    ws = store.ensure_workstream(
        slug=workstream,
        principal_id=principal.principal_id,
        signing_key=principal.signing_key,
    )
    promoted = promote_candidates(
        store, principal=principal, workstream_id=ws["id"], mode=mode
    )
    click.echo(f"promoted: {len(promoted)}")
    for a in promoted:
        click.echo(f"  {a['id']} [{a['kind']}] {a['statement']}")


@main.command("cognify")
@click.option("--workstream", default="default", show_default=True)
@click.option("--force", is_flag=True, help="Force HARD boundary")
@click.option("--event", default="cognify", show_default=True, help="Boundary event type")
@click.option("--no-reseal", is_flag=True, help="Skip auto handoff reseal")
def cognify_cmd(workstream: str, force: bool, event: str, no_reseal: bool) -> None:
    """Deterministic episode cognify on a boundary (PRE_COMPACT/SESSION_END/…)."""
    principal = _require_principal()
    store = _open_store()
    result = cognify_workstream(
        store,
        principal=principal,
        workstream_slug=workstream,
        event_type=event,
        force=force,
        reseal=not no_reseal,
    )
    if result.skipped:
        click.echo(f"skipped: {result.skip_reason}")
        raise SystemExit(0)
    assert result.episode is not None and result.boundary is not None
    click.echo(f"episode:    {result.episode['id']}")
    click.echo(f"boundary:   {result.boundary.kind}/{result.boundary.reason}")
    click.echo(f"summary:    {result.episode['summary'][:200]}")
    click.echo(f"candidates: {len(result.candidates)}")
    click.echo(f"pruned_l0:  {result.pruned_observations}")
    if result.pack_path:
        click.echo(f"pack:       {result.pack_path}")


@main.command("anchors")
@click.option("--shared", is_flag=True, help="List repo_shared_safe Anchors only")
@click.option("--get", "get_id", default=None, help="GET-by-id (Inv-Scope 404)")
def anchors_cmd(shared: bool, get_id: str | None) -> None:
    """List or get Anchors with Inv-Scope enforcement."""
    principal = _require_principal()
    store = _open_store()
    if get_id:
        try:
            anc = store.get_anchor_scoped(
                get_id, principal_id=principal.principal_id, require_shared=shared
            )
        except KeyError:
            _die("not found", code=404)
        click.echo(json.dumps(anc, indent=2))
        return
    if shared:
        items = store.list_shared_anchors()
    else:
        # Only list workstreams the principal can read
        items = []
        for a in store.list_anchors(active_only=True):
            try:
                items.append(
                    store.get_anchor_scoped(a["id"], principal_id=principal.principal_id)
                )
            except KeyError:
                continue
    if not items:
        click.echo("(none)")
        return
    for a in items:
        flag = " shared" if a.get("shareable") else ""
        click.echo(f"{a['id']}  [{a['kind']}]{flag}  {a['statement']}")


if __name__ == "__main__":
    main()
