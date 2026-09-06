# Multi-device sync (0.2.5 slice)

Kedger stays **local-first** and **explicit-only** for sharing with others. Multi-device sync is an **operator-controlled file transfer** — no cloud bus, no ambient team sync.

## When to use what

| Goal | Command |
|------|---------|
| Same person, new laptop (full store) | `kedger sync export` → transfer `.kxs` → `kedger sync import` |
| Same person, session slice only | `kedger pack-export` → `kedger hydrate --pack` |
| Two people, sealed handoff | `kedger peer send` / `kedger peer open` (`.kxp`) |

`.kxs` bundles the project store under `~/.kedger/projects/<repo_fp>/` (SQLite, `raw/`, `packs/`, `acl/`).  
`.kxp` remains recipient-sealed handoff — unchanged by sync.

## Export (source device)

```bash
# optional but recommended before export:
kedger store encrypt    # SQLCipher + encrypted raw/ payloads

kedger sync export --out ./myproject.kxs
# default: ./<repo_fp>.kxs in cwd
```

Copy the `.kxs` via USB, rsync, Drive, etc.

**Keys are not in the bundle.** Transfer separately:

| Secret | Where |
|--------|--------|
| Principal (sign/open `.kxp`, ACL) | `~/.kedger/keys/principal.{json,ed25519,x25519}` |
| Store encryption (if enabled) | `KEDGER_STORE_KEY`, OS keyring, or `~/.kedger/keys/store.key` |

On the new device you can either copy principal keys or run `kedger keys init` and re-grant peers — but copied keys preserve pack open/grant continuity.

## Import (target device)

```bash
cd /path/to/same-git-repo    # same origin → same repo_fingerprint
kedger keys init             # or copy principal keys from source
# if source used store encrypt:
export KEDGER_STORE_KEY=…    # or copy store.key / keyring entry

kedger sync import ./myproject.kxs
kedger doctor
kedger hydrate --live
```

Import backs up an existing project store to `~/.kedger/projects/<fp>.sync-backup-<timestamp>/`.

If the bundle `repo_fingerprint` differs (wrong repo checkout), import fails unless you pass `--force`.

## Honest gaps (still true at 0.2.5)

- **No live sync protocol** — no MQTT, no hosted ciphertext bus, no merge/conflict engine
- **No automatic key escrow** — you move keys out of band
- **No cross-repo import guard beyond fingerprint** — `--force` is sharp
- **Peer share unchanged** — `share_mode=explicit_only`; teammates still use sealed `.kxp`

Future Phase F may add a ciphertext sync service; this slice is the smallest honest operator path without SaaS.
