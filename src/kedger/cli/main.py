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
from kedger.handoff.transcript import (
    decompress_transcript,
    resolve_transcript_archive,
)
from kedger.consolidate import consolidate_workstream
from kedger.doctor import diagnose_cli_path, diagnose_ide_hooks, diagnose_l0_health
from kedger.hooks.install_packs import install_hook_packs
from kedger.hooks.runner import format_ide_stdout, run_hook
from kedger.hydrate import project_hydrate
from kedger.ingest import ingest_from_hook
from kedger.mcp.registry import TOOL_SPECS, call_tool
from kedger.mcp.server import serve
from kedger.keys import KeysError, init_principal, load_principal
from kedger.keys.principal import export_recipient
from kedger.policy import ensure_repo_policy
from kedger.promote import promote_candidates
from kedger.remember import forget_anchor, remember_anchor
from kedger.share import share_anchor, unshare_anchor
from kedger.store import (
    Store,
    StoreEncryptionError,
    StoreKeySource,
    encryption_state,
    kedger_home,
    repo_fingerprint,
    repo_material,
    resolve_store_key,
    store_path,
)
from kedger.store.encryption import (
    ENCRYPTION_SQLCIPHER,
    RAW_PAYLOADS_XCHACHA,
    read_store_meta,
    write_store_meta,
)
from kedger.store.raw_payloads import migrate_plaintext_to_encrypted, raw_encryption_label
from kedger.store.transcript_sidecars import (
    export_plaintext_sidecar,
    migrate_plaintext_to_encrypted as migrate_transcript_sidecars,
    transcript_sidecar_encryption_label,
)
from kedger.store.db import KIND_ALIASES
from kedger.store.paths import keys_dir, project_dir
from kedger.why import explain_anchor
from kedger.sync.bundle import (
    BUNDLE_SUFFIX,
    SyncBundleError,
    export_bundle,
    import_bundle,
    keys_guidance_lines,
)
from kedger.workstream import resolve_workstream


def _die(msg: str, code: int = 1) -> None:
    click.echo(f"error: {msg}", err=True)
    raise SystemExit(code)


def _require_principal():
    try:
        return load_principal()
    except KeysError as e:
        _die(str(e))


def _open_store(*, encrypt: bool = False, prefer_keyring: bool = True) -> Store:
    fp = repo_fingerprint()
    try:
        return Store.open(fp, encrypt=encrypt, prefer_keyring=prefer_keyring)
    except StoreEncryptionError as e:
        _die(str(e))


def _store_key_hint(resolution) -> str:
    if resolution.source == StoreKeySource.KEYRING:
        return f"key: keyring ({resolution.detail})"
    if resolution.source == StoreKeySource.FILE:
        return f"key: file ({resolution.detail})"
    if resolution.source == StoreKeySource.ENV:
        return f"key: env (KEDGER_STORE_KEY)"
    return "key: missing"


@click.group()
@click.version_option(__version__, prog_name="kedger")
def main() -> None:
    """Kedger — local-first engineering memory CLI.

    Product locks: ~/.kedger/, .kxp, kedger.memory.v1.
    """


@main.command("init")
@click.option("--name", default="default", show_default=True, help="Principal display name")
@click.option(
    "--hooks",
    "install_hooks",
    type=click.Choice(["cursor", "claude", "both", "none"]),
    default="both",
    show_default=True,
    help="Install IDE hook packs into this repo (none to skip)",
)
@click.option(
    "--mcp/--no-mcp",
    "install_mcp",
    default=True,
    show_default=True,
    help="When installing hooks, also merge Kedger MCP config snippets (fail-soft)",
)
@click.option("--force-keys", is_flag=True, help="Rotate existing principal keys")
@click.option(
    "--encrypt-store",
    is_flag=True,
    help="Create SQLCipher-encrypted store.sqlite (opt-in; requires kedger[encrypted])",
)
@click.option(
    "--key-file",
    is_flag=True,
    help="With --encrypt-store, store key in ~/.kedger/keys/store.key instead of OS keyring",
)
def init_cmd(
    name: str,
    install_hooks: str,
    install_mcp: bool,
    force_keys: bool,
    encrypt_store: bool,
    key_file: bool,
) -> None:
    """First-run onboard: keys + repo policy + optional IDE hooks."""
    try:
        if force_keys:
            principal = init_principal(name=name, force=True)
            click.echo(f"principal:    {principal.principal_id} (rotated)")
        else:
            try:
                principal = load_principal()
                click.echo(f"principal:    {principal.principal_id} (existing)")
            except KeysError:
                principal = init_principal(name=name, force=False)
                click.echo(f"principal:    {principal.principal_id} (created)")
    except KeysError as e:
        _die(str(e))

    fp = repo_fingerprint()
    ensure_repo_policy(repo_fingerprint=fp)
    store = _open_store(encrypt=encrypt_store, prefer_keyring=not key_file)
    store.ensure_workstream(
        slug="default",
        principal_id=principal.principal_id,
        signing_key=principal.signing_key,
    )
    enc = encryption_state(fp, store_path(fp))
    click.echo(f"store:        {store_path(fp)} ({enc.label})")
    click.echo(f"policy:       .kedger/ (repo)")
    if install_hooks != "none":
        try:
            result = install_hook_packs(
                target=install_hooks,  # type: ignore[arg-type]
                install_mcp=install_mcp,
            )
        except FileNotFoundError as e:
            _die(str(e))
        click.echo(f"hooks:        {result['target']} → {result['repo_root']}")
        for note in result.get("notes") or []:
            click.echo(f"note:         {note}")
    else:
        click.echo("hooks:        skipped (--hooks none)")
    if encrypt_store:
        key_res = resolve_store_key()
        click.echo("encryption:   SQLCipher + encrypted raw/ payloads (opt-in)")
        click.echo(_store_key_hint(key_res))
    else:
        click.echo(
            "encryption:   off (plaintext SQLite + raw/ — run `kedger store encrypt` to enable)"
        )
    click.echo("next:")
    click.echo("  # solo — capture + continue")
    click.echo("  kedger remember reject \"Do not use cookie sessions\" --reason CSRF")
    click.echo("  kedger cognify --force --promote")
    click.echo("  kedger hydrate --live && kedger doctor")
    click.echo("  # two people — share your card, then send a pack")
    click.echo("  kedger peer card --out me.kedger.json")
    click.echo("  kedger peer send --to their.kedger.json --out-dir ./xfer")


@main.group("hooks")
def hooks_group() -> None:
    """Install IDE hook packs into a repository."""


@hooks_group.command("install")
@click.option(
    "--target",
    type=click.Choice(["cursor", "claude", "both"]),
    default="both",
    show_default=True,
)
@click.option(
    "--repo",
    "repo_root",
    type=click.Path(path_type=Path, exists=True, file_okay=False),
    default=None,
    help="Repo root (default: git toplevel or cwd)",
)
@click.option(
    "--mcp/--no-mcp",
    "install_mcp",
    default=True,
    show_default=True,
    help="Merge Kedger MCP config snippets into the repo (fail-soft)",
)
def hooks_install_cmd(target: str, repo_root: Path | None, install_mcp: bool) -> None:
    """Copy Cursor/Claude hook scripts + configs into a repo."""
    try:
        result = install_hook_packs(
            target=target,
            repo_root=repo_root,
            install_mcp=install_mcp,
        )  # type: ignore[arg-type]
    except FileNotFoundError as e:
        _die(str(e))
    click.echo(f"repo:         {result['repo_root']}")
    click.echo(f"packs:        {result['packs_root']}")
    click.echo(f"target:       {result['target']}")
    click.echo(f"files:        {len(result['written'])}")
    for note in result.get("notes") or []:
        click.echo(f"note:         {note}")
    for warn in result.get("warnings") or []:
        click.echo(f"warning:      {warn}", err=True)


@main.group("peer")
def peer_group() -> None:
    """Least-friction two-person handoff (Alice's agent ↔ Bob's agent)."""


def _load_recipient_card(path: Path) -> dict:
    try:
        recip = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        _die(f"invalid peer card: {e}")
    if not recip.get("principal_id") or not recip.get("public_key_b64") or not recip.get(
        "x25519_public_b64"
    ):
        _die("peer card missing principal_id / public_key_b64 / x25519_public_b64")
    return recip


@peer_group.command("card")
@click.option(
    "--out",
    "out_path",
    type=click.Path(path_type=Path),
    default=None,
    help="Write card JSON (default: <name>.kedger.json in cwd)",
)
def peer_card_cmd(out_path: Path | None) -> None:
    """Export your public peer card (safe to send — no private keys)."""
    principal = _require_principal()
    payload = export_recipient(principal)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if out_path is None:
        safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in principal.name) or "me"
        out_path = Path(f"{safe}.kedger.json")
    Path(out_path).write_text(text, encoding="utf-8")
    click.echo(f"wrote:        {out_path.resolve()}")
    click.echo(f"principal:    {principal.principal_id}")
    click.echo("contains:     public keys only (safe to Slack/email)")
    click.echo("give_to:      your teammate → they run: kedger peer add " + str(out_path.name))


@peer_group.command("add")
@click.argument("card", type=click.Path(path_type=Path, exists=True))
def peer_add_cmd(card: Path) -> None:
    """TOFU: register a teammate's peer card (no pack access yet)."""
    principal = _require_principal()
    store = _open_store()
    recip = _load_recipient_card(card)
    pid = recip["principal_id"]
    store.upsert_known_principal(
        principal_id=pid,
        display_name=recip.get("name") or "peer",
        public_key_b64=recip["public_key_b64"],
        x25519_public_b64=recip["x25519_public_b64"],
    )
    store.upsert_known_principal(
        principal_id=principal.principal_id,
        display_name=principal.name,
        public_key_b64=principal.public_key_b64,
        x25519_public_b64=principal.x25519_public_b64,
    )
    click.echo(f"added:        {pid} ({recip.get('name') or 'peer'})")
    click.echo("next:         they need a sealed pack — ask them to:")
    click.echo(f"              kedger peer send --to {card.name} --out-dir ./xfer")


@peer_group.command("send")
@click.option(
    "--to",
    "card",
    type=click.Path(path_type=Path, exists=True),
    required=True,
    help="Teammate peer card (*.kedger.json)",
)
@click.option(
    "--out-dir",
    type=click.Path(path_type=Path),
    required=True,
    help="Folder to write the .kxp (+ sidecar) for transfer",
)
@click.option("--workstream", default="default", show_default=True)
@click.option(
    "--promote/--no-promote",
    default=True,
    show_default=True,
    help="Run cognify --force --promote before sealing",
)
def peer_send_cmd(
    card: Path, out_dir: Path, workstream: str, promote: bool
) -> None:
    """Grant teammate + seal + export a pack they can open (one command)."""
    import shutil

    principal = _require_principal()
    store = _open_store()
    recip = _load_recipient_card(card)
    to_principal = recip["principal_id"]
    ws = store.ensure_workstream(
        slug=workstream,
        principal_id=principal.principal_id,
        signing_key=principal.signing_key,
    )
    store.upsert_known_principal(
        principal_id=to_principal,
        display_name=recip.get("name") or "peer",
        public_key_b64=recip["public_key_b64"],
        x25519_public_b64=recip["x25519_public_b64"],
    )
    store.upsert_known_principal(
        principal_id=principal.principal_id,
        display_name=principal.name,
        public_key_b64=principal.public_key_b64,
        x25519_public_b64=principal.x25519_public_b64,
    )
    try:
        cap = store.grant(
            workstream_id=ws["id"],
            grantee_principal_id=to_principal,
            issuer_principal_id=principal.principal_id,
            permissions=["read_hydrate"],
            grantee_public_key_b64=recip["public_key_b64"],
            grantee_x25519_public_b64=recip["x25519_public_b64"],
            grantee_name=recip.get("name", "peer"),
            signing_key=principal.signing_key,
        )
    except KeyError:
        _die("not found", code=404)
    click.echo(f"granted:      {to_principal} ({cap['id']})")

    if promote:
        try:
            cog = cognify_workstream(
                store,
                principal=principal,
                workstream_slug=workstream,
                force=True,
                event_type="cognify",
                reseal=False,
            )
            click.echo(
                f"cognify:      episode={cog.episode['id'] if cog.episode else 'none'} "
                f"candidates={len(cog.candidates)}"
            )
            promoted = promote_candidates(
                store,
                principal=principal,
                workstream_id=ws["id"],
                mode="conservative",
            )
            click.echo(f"promoted:     {len(promoted)}")
        except Exception as e:  # noqa: BLE001
            click.echo(f"cognify_note: {e}", err=True)

    try:
        path, pack = seal_handoff(
            store, principal=principal, workstream_slug=workstream
        )
    except KeyError:
        _die("not found", code=404)
    except Exception as e:  # noqa: BLE001
        _die(str(e))

    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / path.name
    shutil.copy2(path, dst)
    copied = [dst]
    tmeta = pack.get("transcript_meta") or {}
    if tmeta.get("sidecar"):
        from kedger.store.transcript_sidecars import sidecar_candidates

        candidates = sidecar_candidates(path.parent, tmeta["sidecar"])
        side = next((p for p in candidates if p.exists()), None)
        if side is not None:
            side_dst = out_dir / f"{pack['id']}.transcript.json"
            _copy_transcript_sidecar_for_transfer(
                side, side_dst, store_key=store._store_key
            )
            copied.append(side_dst)
    click.echo(f"pack:         {dst}")
    for extra in copied[1:]:
        click.echo(f"sidecar:      {extra}")
    click.echo("give_to:      teammate (Slack/Drive/USB) → they run:")
    click.echo(f"              kedger peer open {dst.name}")
    click.echo("              kedger hydrate --live")


@peer_group.command("open")
@click.argument("pack", type=click.Path(path_type=Path, exists=True))
@click.option("--workstream", default="default", show_default=True)
def peer_open_cmd(pack: Path, workstream: str) -> None:
    """Import a teammate's sealed .kxp into your local store (durable)."""
    principal = _require_principal()
    store = _open_store()
    ensure_repo_policy(repo_fingerprint=store.repo_fingerprint)
    try:
        opened = hydrate_pack(
            store,
            principal=principal,
            pack_path=Path(pack),
            import_memory=True,
            workstream_slug=workstream,
        )
    except KxpError:
        _die("not found", code=404)
    except KeyError:
        _die("not found", code=404)
    except Exception as e:  # noqa: BLE001
        _die(str(e))

    payload = opened["payload"]
    imp = opened.get("import") or {}
    click.echo(f"opened:       {payload.get('id')}")
    click.echo(f"from:         {payload.get('from_principal_id')}")
    click.echo(f"anchors:      {len(payload.get('anchors') or [])}")
    if imp:
        click.echo(
            f"imported:     anchors={imp.get('anchors_imported')} "
            f"skipped={imp.get('anchors_skipped')} "
            f"activity={imp.get('activity')} transcript={imp.get('transcript')}"
        )
    for a in (payload.get("anchors") or [])[:8]:
        click.echo(f"  [{a['kind']}] {a['statement']}")
    click.echo("next:")
    click.echo("  kedger hydrate --live     # see what your agent will get")
    click.echo("  kedger doctor")
    click.echo("  # start a new IDE chat — sessionStart injects this memory")


@main.group("store")
def store_group() -> None:
    """At-rest SQLCipher encryption for ~/.kedger store.sqlite (opt-in)."""


def _ensure_raw_payload_encryption(store: Store, fp: str) -> int:
    meta = read_store_meta(fp) or {}
    if meta.get("raw_payloads") == RAW_PAYLOADS_XCHACHA:
        return 0
    if store._store_key is None:
        return 0
    migrated = migrate_plaintext_to_encrypted(fp, store_key=store._store_key)
    write_store_meta(
        fp,
        {
            **meta,
            "encryption": meta.get("encryption") or ENCRYPTION_SQLCIPHER,
            "raw_payloads": RAW_PAYLOADS_XCHACHA,
            "raw_payloads_migrated": migrated,
        },
    )
    return migrated


def _ensure_transcript_sidecar_encryption(store: Store, fp: str) -> int:
    meta = read_store_meta(fp) or {}
    if meta.get("transcript_sidecars") == RAW_PAYLOADS_XCHACHA:
        return 0
    if store._store_key is None:
        return 0
    migrated = migrate_transcript_sidecars(fp, store_key=store._store_key)
    write_store_meta(
        fp,
        {
            **meta,
            "encryption": meta.get("encryption") or ENCRYPTION_SQLCIPHER,
            "transcript_sidecars": RAW_PAYLOADS_XCHACHA,
            "transcript_sidecars_migrated": migrated,
        },
    )
    return migrated


def _copy_transcript_sidecar_for_transfer(
    src: Path,
    dst: Path,
    *,
    store_key: bytes | None,
) -> None:
    """Peer send / pack-export: always write plaintext sidecars for transfer."""
    export_plaintext_sidecar(src, dst, store_key=store_key)


@store_group.command("status")
def store_status_cmd() -> None:
    """Show whether the current repo store is encrypted at rest."""
    fp = repo_fingerprint()
    path = store_path(fp)
    state = encryption_state(fp, path)
    click.echo(f"store:      {path}")
    click.echo(f"encryption: {state.label}")
    if state.enabled or state.raw_payloads:
        key_res = resolve_store_key()
        click.echo(_store_key_hint(key_res))
        if key_res.source == StoreKeySource.MISSING:
            click.echo(
                "hint:       set KEDGER_STORE_KEY, run `kedger store encrypt`, "
                "or install keyring for OS credential storage"
            )
    elif path.exists():
        click.echo("hint:       run `kedger store encrypt` to migrate to SQLCipher")
    try:
        store = Store.open(fp)
        click.echo(f"raw/:       {raw_encryption_label(store._store_key)}")
        click.echo(
            f"transcripts: {transcript_sidecar_encryption_label(store._store_key)}"
        )
    except StoreEncryptionError:
        click.echo(f"raw/:       {raw_encryption_label(None)}")
        click.echo(f"transcripts: {transcript_sidecar_encryption_label(None)}")


@store_group.command("encrypt")
@click.option(
    "--force",
    is_flag=True,
    help="Re-encrypt even if store.meta.json already marks SQLCipher",
)
@click.option(
    "--key-file",
    is_flag=True,
    help="Store key in ~/.kedger/keys/store.key instead of OS keyring",
)
def store_encrypt_cmd(force: bool, key_file: bool) -> None:
    """Migrate plaintext store.sqlite to SQLCipher (creates store key if missing)."""
    fp = repo_fingerprint()
    path = store_path(fp)
    state = encryption_state(fp, path)
    if state.enabled and not force:
        click.echo(f"store already encrypted ({path})")
        key_res = resolve_store_key()
        click.echo(_store_key_hint(key_res))
        try:
            store = _open_store()
            migrated_raw = _ensure_raw_payload_encryption(store, fp)
            migrated_transcripts = _ensure_transcript_sidecar_encryption(store, fp)
            if migrated_raw:
                click.echo(f"raw/:       migrated {migrated_raw} plaintext payload(s) to encrypted")
            if migrated_transcripts:
                click.echo(
                    f"transcripts: migrated {migrated_transcripts} plaintext sidecar(s) to encrypted"
                )
        except StoreEncryptionError:
            pass
        return
    if not path.exists():
        _die(f"no store at {path}; run `kedger init` first")
    store = _open_store(encrypt=True, prefer_keyring=not key_file)
    migrated_raw = _ensure_raw_payload_encryption(store, fp)
    migrated_transcripts = _ensure_transcript_sidecar_encryption(store, fp)
    counts = store.counts()
    key_res = resolve_store_key()
    click.echo(f"encrypted:  {path}")
    click.echo(_store_key_hint(key_res))
    if migrated_raw:
        click.echo(f"raw/:       migrated {migrated_raw} plaintext payload(s) to encrypted")
    if migrated_transcripts:
        click.echo(
            f"transcripts: migrated {migrated_transcripts} plaintext sidecar(s) to encrypted"
        )
    click.echo(
        f"backup:     {path}.plaintext.bak (remove after verifying `kedger doctor`)"
    )
    click.echo(
        f"anchors:    active={counts['anchors_active']} total={counts['anchors_total']}"
    )


@main.group("sync")
def sync_group() -> None:
    """Export/import full project store bundles for same-person device transfer."""


@sync_group.command("export")
@click.option(
    "--out",
    "out_path",
    type=click.Path(path_type=Path),
    default=None,
    help=f"Output bundle path (default: ./{'{repo_fp}'}{BUNDLE_SUFFIX} in cwd)",
)
def sync_export_cmd(out_path: Path | None) -> None:
    """Write a `.kxs` tarball of ~/.kedger/projects/<fp>/ for offline transfer.

    Keys are NOT bundled — copy principal + store keys separately (see hints below).
    For teammate handoff slices, use `kedger pack-export` / sealed `.kxp` instead.
    """
    fp = repo_fingerprint()
    if out_path is None:
        out_path = Path.cwd() / f"{fp}{BUNDLE_SUFFIX}"
    try:
        result = export_bundle(out_path=out_path, repo_fp=fp)
    except SyncBundleError as e:
        _die(str(e))
    click.echo(f"bundle:       {result.path}")
    click.echo(f"repo_fp:      {result.repo_fingerprint}")
    click.echo(f"files:        {result.file_count}")
    click.echo(
        f"encryption:   {'on (SQLCipher in bundle)' if result.encrypted else 'off (plaintext in bundle)'}"
    )
    for line in keys_guidance_lines(encrypted=result.encrypted):
        click.echo(line)
    click.echo("next:         scp/rsync/USB the .kxs to new device → `kedger sync import`")


@sync_group.command("import")
@click.argument(
    "bundle_path",
    type=click.Path(path_type=Path, exists=True, dir_okay=False),
)
@click.option(
    "--force",
    is_flag=True,
    help="Import even when bundle repo_fingerprint differs from current repo",
)
def sync_import_cmd(bundle_path: Path, force: bool) -> None:
    """Restore a `.kxs` bundle into ~/.kedger/projects/<fp>/ (backs up existing store)."""
    try:
        result = import_bundle(bundle_path, force=force)
    except SyncBundleError as e:
        _die(str(e))
    click.echo(f"imported:     {result.file_count} file(s) → {project_dir(result.repo_fingerprint)}")
    if result.backup_path:
        click.echo(f"backup:       {result.backup_path}")
    click.echo(
        f"encryption:   {'on (needs store key)' if result.encrypted else 'off (plaintext store)'}"
    )
    for line in keys_guidance_lines(encrypted=result.encrypted):
        click.echo(line)
    click.echo("next:         `kedger doctor` && `kedger hydrate --live`")


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
    payload = export_recipient(principal)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if out_path:
        Path(out_path).write_text(text, encoding="utf-8")
        click.echo(f"wrote: {out_path}")
    else:
        click.echo(text, nl=False)


@keys_group.command("import-recipient")
@click.option(
    "--file",
    "recip_file",
    type=click.Path(path_type=Path, exists=True),
    required=True,
    help="JSON from peer `kedger keys export-recipient`",
)
def keys_import_recipient(recip_file: Path) -> None:
    """TOFU: register a peer's public keys in the local store (no grant yet)."""
    principal = _require_principal()
    store = _open_store()
    try:
        recip = json.loads(Path(recip_file).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        _die(f"invalid recipient file: {e}")
    pid = recip.get("principal_id")
    if not pid or not recip.get("public_key_b64") or not recip.get("x25519_public_b64"):
        _die("recipient file missing principal_id / public_key_b64 / x25519_public_b64")
    store.upsert_known_principal(
        principal_id=pid,
        display_name=recip.get("name") or "peer",
        public_key_b64=recip["public_key_b64"],
        x25519_public_b64=recip["x25519_public_b64"],
    )
    # Ensure local principal is also registered for seal paths
    store.upsert_known_principal(
        principal_id=principal.principal_id,
        display_name=principal.name,
        public_key_b64=principal.public_key_b64,
        x25519_public_b64=principal.x25519_public_b64,
    )
    click.echo(f"imported:     {pid}")
    click.echo(f"name:         {recip.get('name') or 'peer'}")
    click.echo("note:         run `kedger grant` to add pack recipient capability")


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
@click.option("--workstream", default="default", show_default=True)
def status_cmd(list_anchors: bool, workstream: str) -> None:
    """Show fingerprint, store path, counts, and handoff layers."""
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
    ws = store.get_workstream_by_slug(workstream)
    if ws is not None:
        working = store.get_working_state(ws["id"]) or {}
        act = working.get("activity") or {}
        totals = act.get("totals") or {}
        click.echo(
            "activity:           "
            f"files={totals.get('files', 0)} edits={totals.get('edits', 0)} "
            f"+{totals.get('lines_added', 0)}/-{totals.get('lines_removed', 0)}"
        )
        tmeta = working.get("transcript_meta") or {}
        ep = store.latest_episode(ws["id"])
        if not tmeta and ep:
            tmeta = ep.get("transcript_meta") or {}
        if tmeta:
            click.echo(
                "transcript:         "
                f"turns={tmeta.get('turn_count')} "
                f"zlib={tmeta.get('compressed_bytes')}B "
                f"ratio={tmeta.get('ratio')}"
            )
        else:
            click.echo("transcript:         (none)")
        click.echo("layers:             base=anchors activity=ops transcript=zlib")
    if list_anchors:
        anchors = (
            store.ranked_active_anchors(workstream_id=ws["id"])
            if ws is not None
            else store.list_anchors(active_only=True)
        )
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
    warnings: list[tuple[str, str]] = []

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
    enc_state = encryption_state(fp, path)
    if path.exists():
        try:
            store = Store.open(fp)
            meta = store.meta()
            ok = meta.get("schema_version") == SCHEMA_VERSION
            checks.append(
                (
                    "store",
                    ok,
                    f"{path} schema={meta.get('schema_version')} encryption={enc_state.label}",
                )
            )
            counts = store.counts()
            checks.append(
                (
                    "anchors",
                    True,
                    f"active={counts['anchors_active']} total={counts['anchors_total']}",
                )
            )
            # Dual-layer + zlib transfer health on default workstream
            ws = store.get_workstream_by_slug("default")
            if ws is not None:
                working = store.get_working_state(ws["id"]) or {}
                act = working.get("activity") or {}
                totals = act.get("totals") or {}
                checks.append(
                    (
                        "activity_layer",
                        True,
                        (
                            f"files={totals.get('files', 0)} "
                            f"edits={totals.get('edits', 0)} "
                            f"+{totals.get('lines_added', 0)}/-{totals.get('lines_removed', 0)}"
                        ),
                    )
                )
                tmeta = working.get("transcript_meta") or {}
                ep = store.latest_episode(ws["id"])
                if not tmeta and ep:
                    tmeta = ep.get("transcript_meta") or {}
                if tmeta:
                    checks.append(
                        (
                            "transcript_archive",
                            True,
                            (
                                f"turns={tmeta.get('turn_count')} "
                                f"zlib={tmeta.get('compressed_bytes')}B "
                                f"ratio={tmeta.get('ratio')} "
                                f"codec={tmeta.get('codec') or 'zlib'}"
                            ),
                        )
                    )
                else:
                    checks.append(
                        (
                            "transcript_archive",
                            True,
                            "none yet (run cognify after turns)",
                        )
                    )
                checks.append(
                    (
                        "handoff_layers",
                        True,
                        "base=anchors activity=agent_ops transcript=zlib",
                    )
                )
                # Pending candidates + HEAD pack continuity hints
                with store.connection() as conn:
                    row = conn.execute(
                        "SELECT COUNT(*) AS c FROM promotion_candidates "
                        "WHERE workstream_id = ? AND status = 'candidate'",
                        (ws["id"],),
                    ).fetchone()
                pending = int(row["c"]) if row else 0
                checks.append(
                    (
                        "promotion_queue",
                        True,
                        (
                            f"pending={pending}"
                            + (
                                " (run kedger promote or cognify --promote)"
                                if pending
                                else ""
                            )
                        ),
                    )
                )
                packs_dir = project_dir(fp) / "packs" / ws["id"]
                head = packs_dir / "HEAD"
                if head.exists():
                    hid = head.read_text(encoding="utf-8").strip()
                    kxp_ok = (packs_dir / f"{hid}.kxp").exists()
                    checks.append(
                        (
                            "handoff_head",
                            kxp_ok,
                            f"{hid}.kxp" if kxp_ok else f"HEAD={hid} missing .kxp",
                        )
                    )
                else:
                    checks.append(
                        (
                            "handoff_head",
                            True,
                            "none yet (run cognify --promote / handoff)",
                        )
                    )
                obs_n = len(store.list_observations(workstream_id=ws["id"]))
                checks.append(("l0_observations", True, f"count={obs_n}"))
                for w in diagnose_l0_health(store, workstream_id=ws["id"]):
                    warnings.append(("l0_health", w))
            if enc_state.enabled:
                checks.append(("store_encryption", True, enc_state.label))
                key_res = resolve_store_key()
                key_ok = key_res.source != StoreKeySource.MISSING
                checks.append(("store_key", key_ok, key_res.label))
                checks.append(
                    (
                        "raw_payloads",
                        enc_state.raw_payloads == RAW_PAYLOADS_XCHACHA,
                        raw_encryption_label(store._store_key),
                    )
                )
                meta = read_store_meta(fp) or {}
                checks.append(
                    (
                        "transcript_sidecars",
                        meta.get("transcript_sidecars") == RAW_PAYLOADS_XCHACHA,
                        transcript_sidecar_encryption_label(store._store_key),
                    )
                )
            else:
                warnings.append(
                    (
                        "store_encryption",
                        "plaintext SQLite at rest — run `kedger store encrypt` for SQLCipher",
                    )
                )
                warnings.append(
                    (
                        "raw_payloads",
                        "plaintext JSON in raw/ — enabled with `kedger store encrypt`",
                    )
                )
                warnings.append(
                    (
                        "transcript_sidecars",
                        "plaintext JSON in packs/ — enabled with `kedger store encrypt`",
                    )
                )
            checks.append(
                (
                    "kxp_at_rest",
                    True,
                    "recipient-sealed (KXP1 X25519/XChaCha) — no extra store-key wrap (peer open)",
                )
            )
        except StoreEncryptionError as e:
            checks.append(("store", False, str(e)))
            if enc_state.enabled:
                key_res = resolve_store_key()
                checks.append(
                    (
                        "store_key",
                        False,
                        key_res.label if key_res.source != StoreKeySource.MISSING else str(e),
                    )
                )
        except Exception as e:  # noqa: BLE001
            checks.append(("store", False, str(e)))
    else:
        checks.append(("store", True, f"not created yet ({path})"))
        checks.append(
            (
                "store_encryption",
                True,
                "off (plaintext default; use `kedger init --encrypt-store` or `kedger store encrypt`)",
            )
        )

    kinds = ", ".join(sorted(set(KIND_ALIASES.values())))
    checks.append(("anchor_kinds", True, kinds))
    checks.append(
        (
            "identity_lock",
            True,
            "CLI=kedger; store=~/.kedger/; packs=.kxp; schema=kedger.memory.v1",
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

    for w in diagnose_ide_hooks():
        warnings.append(("ide_hooks", w))
    for w in diagnose_cli_path():
        warnings.append(("cli_path", w))

    failed = 0
    for name, ok, detail in checks:
        mark = "ok" if ok else "FAIL"
        if not ok:
            failed += 1
        click.echo(f"[{mark}] {name}: {detail}")
    for name, detail in warnings:
        click.echo(f"[warn] {name}: {detail}")
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
    act = pack.get("activity") or {}
    totals = act.get("totals") or {}
    if totals:
        click.echo(
            f"activity:     files={totals.get('files', 0)} "
            f"edits={totals.get('edits', 0)} "
            f"+{totals.get('lines_added', 0)}/-{totals.get('lines_removed', 0)}"
        )
    tmeta = pack.get("transcript_meta") or {}
    if tmeta:
        click.echo(
            f"transcript:   turns={tmeta.get('turn_count')} "
            f"raw={tmeta.get('raw_bytes')}B "
            f"zlib={tmeta.get('compressed_bytes')}B "
            f"via={pack.get('layers', {}).get('transcript')}"
        )
        if tmeta.get("sidecar"):
            click.echo(f"sidecar:      {path.parent / tmeta['sidecar']}")
    click.echo(f"pack:         {path}")


@main.command("pack-export")
@click.option("--workstream", default="default", show_default=True)
@click.option(
    "--out-dir",
    type=click.Path(path_type=Path),
    required=True,
    help="Directory to write .kxp (+ transcript sidecar if any)",
)
def pack_export_cmd(workstream: str, out_dir: Path) -> None:
    """Copy the latest sealed pack (+ zlib sidecar) into a folder for transfer."""
    import shutil

    principal = _require_principal()
    store = _open_store()
    try:
        path, pack = seal_handoff(
            store, principal=principal, workstream_slug=workstream
        )
    except KeyError:
        _die("not found", code=404)
    except Exception as e:  # noqa: BLE001
        _die(str(e))
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / path.name
    shutil.copy2(path, dst)
    copied = [str(dst)]
    tmeta = pack.get("transcript_meta") or {}
    if tmeta.get("sidecar"):
        from kedger.store.transcript_sidecars import sidecar_candidates

        candidates = sidecar_candidates(path.parent, tmeta["sidecar"])
        side = next((p for p in candidates if p.exists()), None)
        if side is not None:
            side_dst = out_dir / f"{pack['id']}.transcript.json"
            _copy_transcript_sidecar_for_transfer(
                side, side_dst, store_key=store._store_key
            )
            copied.append(str(side_dst))
    click.echo(f"handoff_id:   {pack['id']}")
    click.echo(f"exported:     {len(copied)} file(s)")
    for c in copied:
        click.echo(f"  {c}")
    click.echo("next:         kedger hydrate --pack <exported.kxp>")


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
@click.option(
    "--purpose",
    default=None,
    type=click.Choice(["engineering", "internal", "third_party", "export"]),
    help="AirGap field minimization purpose (third_party/export strip reason/provenance)",
)
@click.option(
    "--notebook-calls",
    default=10,
    show_default=True,
    type=int,
    help="GraphReader notebook walk call budget (separate from node walk-budget)",
)
@click.option(
    "--surface-k",
    default=None,
    type=int,
    help="Visible-surface seed size (default: VISIBLE_SURFACE_K=5)",
)
@click.option(
    "--no-import",
    is_flag=True,
    help="Open pack without merging Anchors/activity/transcript into the local store",
)
def hydrate_cmd(
    pack_path: Path | None,
    live: bool,
    workstream: str,
    topic: str | None,
    walk_budget: int,
    purpose: str | None,
    notebook_calls: int,
    surface_k: int | None,
    no_import: bool,
) -> None:
    """Authorized hydrate of a sealed `.kxp` pack or live ranked projection.

    Pack hydrate imports durable memory by default (Anchors + activity + zlib
    transcript) so the next agent session can use `--live` / IDE hooks.
    """
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
                purpose=purpose,
                notebook_max_calls=notebook_calls,
                surface_k=surface_k,
            )
        except InvScopeError:
            _die("not found", code=404)
        click.echo(f"workstream:   {resolved.workstream['id']}")
        click.echo(f"anchors:      {len(proj.anchors)}")
        click.echo(f"evidence:     {len(proj.evidence)}")
        click.echo(f"used_bytes:   {proj.used_bytes}")
        click.echo(
            f"surface_k:    {proj.surface_k} (seeds={len(proj.seed_ids)})"
        )
        click.echo(f"walk_budget:  {proj.walk_budget} (expanded={len(proj.walk_ids)})")
        if purpose:
            click.echo(f"purpose:      {purpose}")
        if proj.notebook_calls:
            click.echo(
                f"notebook:     calls={proj.notebook_calls} "
                f"entries={len(proj.notebook)} terminated={proj.notebook_terminated}"
            )
        working = proj.working or {}
        act = working.get("activity") or {}
        totals = act.get("totals") or {}
        if totals:
            click.echo(
                f"activity:     files={totals.get('files', 0)} "
                f"edits={totals.get('edits', 0)} "
                f"+{totals.get('lines_added', 0)}/-{totals.get('lines_removed', 0)}"
            )
        tmeta = working.get("transcript_meta") or {}
        if tmeta:
            click.echo(
                f"transcript:   turns={tmeta.get('turn_count')} "
                f"zlib={tmeta.get('compressed_bytes')}B "
                f"ratio={tmeta.get('ratio')}"
            )
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
        opened = hydrate_pack(
            store,
            principal=principal,
            pack_path=Path(pack_path),
            import_memory=not no_import,
            workstream_slug=workstream,
        )
    except KxpError:
        _die("not found", code=404)
    except KeyError:
        _die("not found", code=404)
    payload = opened["payload"]
    click.echo(f"handoff_id:   {payload['id']}")
    click.echo(f"workstream:   {payload.get('workstream_id')}")
    click.echo(f"anchors:      {len(payload.get('anchors') or [])}")
    click.echo(f"from:         {payload.get('from_principal_id')}")
    imp = opened.get("import") or {}
    if imp:
        click.echo(
            f"imported:     anchors={imp.get('anchors_imported')} "
            f"skipped={imp.get('anchors_skipped')} "
            f"activity={imp.get('activity')} transcript={imp.get('transcript')} "
            f"into={imp.get('workstream_slug')}"
        )
    act = payload.get("activity") or {}
    totals = act.get("totals") or {}
    if totals:
        click.echo(
            f"activity:     files={totals.get('files', 0)} "
            f"+{totals.get('lines_added', 0)}/-{totals.get('lines_removed', 0)}"
        )
    tmeta = payload.get("transcript_meta") or imp.get("transcript_meta") or {}
    if tmeta:
        click.echo(
            f"transcript:   turns={tmeta.get('turn_count')} "
            f"raw={tmeta.get('raw_bytes')}B zlib={tmeta.get('compressed_bytes')}B"
        )
    for a in payload.get("anchors") or []:
        click.echo(f"  [{a['kind']}] {a['statement']}")


@main.group("transcript")
def transcript_group() -> None:
    """Lossless zlib transcript archive — zip-style transfer across sessions."""


def _load_archive_from_pack(pack_path: Path, store: Store, principal) -> dict:
    opened = hydrate_pack(
        store,
        principal=principal,
        pack_path=pack_path,
        import_memory=False,
    )
    payload = opened["payload"]
    archive = resolve_transcript_archive(
        payload,
        sidecar_root=pack_path.parent,
        store_key=None,
    )
    if archive is None:
        _die("no transcript archive in pack (inline or sidecar)")
    return archive


def _load_archive_live(store: Store, workstream: str, principal) -> dict:
    ws = store.get_workstream_by_slug(workstream) or store.ensure_workstream(
        slug=workstream,
        principal_id=principal.principal_id,
        signing_key=principal.signing_key,
    )
    ep = store.latest_episode(ws["id"])
    working = store.get_working_state(ws["id"]) or {}
    packs_root = project_dir(store.repo_fingerprint) / "packs" / ws["id"]
    archive = None
    if ep:
        archive = resolve_transcript_archive(
            ep,
            sidecar_root=packs_root,
            store_key=store._store_key,
        )
    if archive is None and working.get("transcript_meta", {}).get("sidecar"):
        from kedger.handoff.transcript import read_transcript_sidecar
        from kedger.store.transcript_sidecars import sidecar_candidates

        side_name = working["transcript_meta"]["sidecar"]
        for side in sidecar_candidates(packs_root, side_name):
            if side.exists():
                archive = read_transcript_sidecar(side, store_key=store._store_key)
                break
    if archive is None:
        _die("no transcript archive in live store")
    return archive


@transcript_group.command("stats")
@click.option("--pack", "pack_path", type=click.Path(path_type=Path), default=None)
@click.option("--live", is_flag=True, help="Read from latest episode / working meta")
@click.option("--workstream", default="default", show_default=True)
def transcript_stats(pack_path: Path | None, live: bool, workstream: str) -> None:
    """Show zlib compression stats for a pack or live archive."""
    principal = _require_principal()
    store = _open_store()
    if pack_path:
        try:
            archive = _load_archive_from_pack(Path(pack_path), store, principal)
        except KxpError:
            _die("not found", code=404)
    elif live:
        archive = _load_archive_live(store, workstream, principal)
    else:
        _die("pass --pack PATH or --live")
    click.echo(f"schema:       {archive.get('schema')}")
    click.echo(f"codec:        {archive.get('codec')}")
    click.echo(f"turn_count:   {archive.get('turn_count')}")
    click.echo(f"raw_bytes:    {archive.get('raw_bytes')}")
    click.echo(f"compressed:   {archive.get('compressed_bytes')}")
    click.echo(f"ratio:        {archive.get('ratio')}")


@transcript_group.command("decompress")
@click.option("--pack", "pack_path", type=click.Path(path_type=Path), default=None)
@click.option("--live", is_flag=True)
@click.option("--workstream", default="default", show_default=True)
@click.option(
    "--out",
    "out_path",
    type=click.Path(path_type=Path),
    default=None,
    help="Write turn JSON (default: stdout)",
)
def transcript_decompress(
    pack_path: Path | None, live: bool, workstream: str, out_path: Path | None
) -> None:
    """Restore the full redacted turn tape (lossless inverse of zlib compress)."""
    principal = _require_principal()
    store = _open_store()
    if pack_path:
        try:
            archive = _load_archive_from_pack(Path(pack_path), store, principal)
        except KxpError:
            _die("not found", code=404)
    elif live:
        archive = _load_archive_live(store, workstream, principal)
    else:
        _die("pass --pack PATH or --live")
    turns = decompress_transcript(archive)
    text = json.dumps(turns, indent=2, sort_keys=True)
    if out_path:
        Path(out_path).write_text(text + "\n", encoding="utf-8")
        click.echo(f"turns:        {len(turns)}")
        click.echo(f"wrote:        {out_path}")
    else:
        click.echo(text)


@transcript_group.command("show")
@click.option("--pack", "pack_path", type=click.Path(path_type=Path), default=None)
@click.option("--live", is_flag=True)
@click.option("--workstream", default="default", show_default=True)
@click.option("--limit", default=20, show_default=True, type=int)
def transcript_show(
    pack_path: Path | None, live: bool, workstream: str, limit: int
) -> None:
    """Print a human preview of decompressed turns."""
    principal = _require_principal()
    store = _open_store()
    if pack_path:
        try:
            archive = _load_archive_from_pack(Path(pack_path), store, principal)
        except KxpError:
            _die("not found", code=404)
    elif live:
        archive = _load_archive_live(store, workstream, principal)
    else:
        _die("pass --pack PATH or --live")
    turns = decompress_transcript(archive)
    click.echo(f"turns:        {len(turns)}")
    click.echo(
        f"compressed:   {archive.get('compressed_bytes')}B / "
        f"{archive.get('raw_bytes')}B (ratio={archive.get('ratio')})"
    )
    for t in turns[-limit:]:
        summary = (t.get("summary") or "")[:160]
        click.echo(f"  [{t.get('type')}] {summary}")


@main.command("grant")
@click.option("--workstream", default="default", show_default=True, help="Workstream slug")
@click.option(
    "--to",
    "to_principal",
    default=None,
    help="Grantee principal id (pr_…). Optional if --recipient-file has principal_id.",
)
@click.option(
    "--recipient-file",
    type=click.Path(path_type=Path, exists=True),
    required=True,
    help="JSON from `kedger peer card` / `kedger keys export-recipient`",
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
    to_principal: str | None,
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
    file_pid = recip.get("principal_id")
    if to_principal is None:
        if not file_pid:
            _die("pass --to or use a recipient file with principal_id")
        to_principal = file_pid
    elif file_pid and file_pid != to_principal:
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
    click.echo("next:         kedger pack-export --out-dir ./xfer   # or: kedger peer send")


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
    """Promote Tier A/B candidates into Anchors (never auto-share).

    ``normal`` mode also commits Tier B when recurrence ≥ θ or heat ≥ τ.
    """
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


@main.command("consolidate")
@click.option("--workstream", default="default", show_default=True)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Print merge plan without forgetting losers",
)
def consolidate_cmd(workstream: str, dry_run: bool) -> None:
    """Sleep-time near-dup Anchor merge via SUPERSEDES (offline; never SessionStart)."""
    principal = _require_principal()
    store = _open_store()
    ws = store.ensure_workstream(
        slug=workstream,
        principal_id=principal.principal_id,
        signing_key=principal.signing_key,
    )
    result = consolidate_workstream(
        store,
        principal=principal,
        workstream_id=ws["id"],
        dry_run=dry_run,
    )
    click.echo(f"scanned:    {result.scanned}")
    click.echo(f"clusters:   {result.clusters}")
    click.echo(f"merged:     {result.merged}")
    click.echo(f"escalate:   {result.skipped_escalate} (pairs left alone)")
    if dry_run:
        click.echo("dry_run:    true (no writes)")
    for act in result.actions[:40]:
        click.echo(
            f"  keep {act.keep_id} ← drop {act.drop_id} ({act.reason})"
        )


@main.command("cognify")
@click.option("--workstream", default="default", show_default=True)
@click.option("--force", is_flag=True, help="Force HARD boundary")
@click.option("--event", default="cognify", show_default=True, help="Boundary event type")
@click.option("--no-reseal", is_flag=True, help="Skip auto handoff reseal")
@click.option(
    "--promote",
    "do_promote",
    is_flag=True,
    help="Promote conservative candidates before reseal (durable Anchors for next session)",
)
@click.option(
    "--consolidate/--no-consolidate",
    "do_consolidate",
    default=False,
    show_default=True,
    help="After promote, run sleep-time near-dup consolidate (default off)",
)
@click.option(
    "--llm-distill",
    is_flag=True,
    help=(
        "Optional LLM episode summary (needs KEDGER_LLM_API_KEY; "
        "falls back to heuristics on missing config or error)"
    ),
)
def cognify_cmd(
    workstream: str,
    force: bool,
    event: str,
    no_reseal: bool,
    do_promote: bool,
    do_consolidate: bool,
    llm_distill: bool,
) -> None:
    """Deterministic episode cognify on a boundary (PRE_COMPACT/SESSION_END/…)."""
    principal = _require_principal()
    store = _open_store()
    # When promoting, defer reseal so the pack includes newly promoted Anchors
    reseal = not no_reseal and not do_promote
    result = cognify_workstream(
        store,
        principal=principal,
        workstream_slug=workstream,
        event_type=event,
        force=force,
        reseal=reseal,
        llm_distill=llm_distill,
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
    dmeta = (result.episode or {}).get("distill_v1") or {}
    if dmeta.get("mode") == "llm":
        click.echo(f"distill:    llm ({dmeta.get('model')})")
    elif llm_distill:
        click.echo("distill:    heuristic (llm unavailable or failed)")
    tmeta = (result.episode or {}).get("transcript_meta") or {}
    if tmeta:
        click.echo(
            f"transcript: turns={tmeta.get('turn_count')} "
            f"zlib={tmeta.get('compressed_bytes')}B ratio={tmeta.get('ratio')}"
        )
    promoted = 0
    if do_promote:
        resolved = resolve_workstream(
            store, principal=principal, explicit_slug=workstream
        )
        ws_id = resolved.workstream["id"] if resolved.workstream else None
        out = promote_candidates(
            store,
            principal=principal,
            workstream_id=ws_id,
            mode="conservative",
        )
        promoted = len(out)
        click.echo(f"promoted:   {promoted}")
        if do_consolidate and ws_id:
            cres = consolidate_workstream(
                store, principal=principal, workstream_id=ws_id, dry_run=False
            )
            click.echo(f"consolidated: {cres.merged} (clusters={cres.clusters})")
        if not no_reseal:
            try:
                path, pack = seal_handoff(
                    store, principal=principal, workstream_slug=workstream
                )
                result.pack_path = str(path)
                click.echo(f"anchors:    {len(pack.get('anchors') or [])}")
            except Exception:  # noqa: BLE001
                pass
    elif do_consolidate:
        resolved = resolve_workstream(
            store, principal=principal, explicit_slug=workstream
        )
        if resolved.workstream:
            cres = consolidate_workstream(
                store,
                principal=principal,
                workstream_id=resolved.workstream["id"],
                dry_run=False,
            )
            click.echo(f"consolidated: {cres.merged} (clusters={cres.clusters})")
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


@main.group("mcp")
def mcp_group() -> None:
    """Minimal MCP read tools (hydrate, anchors_get) for agent pull fallback."""


@mcp_group.command("tools-list")
def mcp_tools_list_cmd() -> None:
    """List registered MCP tools (JSON)."""
    click.echo(json.dumps(TOOL_SPECS, indent=2, sort_keys=True))


@mcp_group.command("call")
@click.argument("tool_name")
@click.option("--args-json", default="{}", show_default=True, help="Tool arguments JSON")
def mcp_call_cmd(tool_name: str, args_json: str) -> None:
    """Invoke one MCP tool in-process (smoke / CI without stdio server)."""
    principal = _require_principal()
    store = _open_store()
    try:
        args = json.loads(args_json)
    except json.JSONDecodeError as e:
        _die(f"invalid --args-json: {e}")
    if not isinstance(args, dict):
        _die("--args-json must be an object")
    result = call_tool(tool_name, args, store=store, principal=principal)
    click.echo(json.dumps(result, indent=2, sort_keys=True))
    if result.get("code") == 404:
        raise SystemExit(404)


@mcp_group.command("serve")
def mcp_serve_cmd() -> None:
    """Run MCP stdio server (Content-Length JSON-RPC framing)."""
    serve()


if __name__ == "__main__":
    main()
