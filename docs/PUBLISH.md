# Publishing Kedger

## Current PyPI status

| Version | Notes |
|---------|--------|
| `0.1.0` | On PyPI — thinner CLI surface |
| `0.1.1` | Live — https://pypi.org/project/kedger/0.1.1/ |
| `0.2.0` | **Beta cut** — on PyPI |
| `0.2.2` | **Pending** — OS keychain store key (second Phase F slice) |
| `0.2.1` | Optional SQLCipher at-rest encryption (first Phase F slice) |

Project: https://pypi.org/project/kedger/

**Do not reuse `0.1.0`.** Bump for every upload.

## Marketing / stars / LinkedIn

See [`docs/MARKETING.md`](MARKETING.md) for positioning lock, claim guardrails, LinkedIn paste pack, and peer-trial protocol.

**Claim guardrails:** beta + mechanical tests only; human peer trials pending; never “proven in production.” **Do claim** minimal MCP (`hydrate` / `anchors_get`) and prompt-time inject — shipped in 0.2.0. **Do claim** optional SQLCipher at-rest encryption with OS keychain key storage (`kedger store encrypt`, `init --encrypt-store`) — shipped in 0.2.1–0.2.2 (opt-in; plaintext default). **Do not claim** full Phase F (LLM distill, sync) or MCP-as-primary.

## GitHub About

**Status (2026-08-09):** description, homepage, topics, and wiki-off are set on `gaganTakIITD/kedger`.

**Still maintainer UI:** Social preview — `open_graph_image_url` is null until you upload `docs/assets/social.png`.

```bash
bash scripts/set_github_about.sh          # refresh description/topics (needs admin)
bash scripts/remind_social_preview.sh     # prints Settings → Social preview steps
```

**Description:**
```text
Code is versioned; agent judgment isn't. L0–L4 memory (Anchors survive compact) + sealed .kxp handoff — research-backed, explicit share, no cloud bus.
```

**Homepage:** `https://pypi.org/project/kedger/`

**Topics:** cli, python, agents, cursor, claude-code, memory, handoff, local-first, sealed-packs, developer-tools

Release `v0.1.1` already published; body from `CHANGELOG.md`.

## Release checklist (`0.2.0` beta)

1. Merge #36 to `main` (P0–P3 + 0.2.0 prep + MCP/inject hardening; CI green)
2. Versions match: `pyproject.toml`, `src/kedger/__init__.py`, `src/kedger/mcp/server.py`, `CHANGELOG.md`
3. Local gate:

   ```bash
   pip install -e ".[dev]"
   bash scripts/check_hook_packs_sync.sh
   pytest -q
   bash scripts/smoke_transfer.sh
   bash scripts/smoke_prompt_inject.sh
   bash scripts/smoke_wheel_install.sh
   bash scripts/smoke_peer_handoff.sh
   bash scripts/peer_trial.sh
   ```

   **Windows:** run the bash smoke lines in Git Bash; `*.sh` are LF-only in git (see `.gitattributes`).

4. Tag: `git tag v0.2.0 && git push origin v0.2.0`
5. Trusted Publisher Release workflow (or manual twine below)
6. Confirm https://pypi.org/project/kedger/0.2.0/ + GitHub Release (body from `RELEASES/v0.2.0.md`)

## Release checklist (`0.1.1`)

1. Merge tip to `main` (CI green)
2. Set GitHub About + social preview (above)
3. Versions match: `pyproject.toml`, `src/kedger/__init__.py`, `CHANGELOG.md`
4. Local gate:

   ```bash
   pip install -e ".[dev]"
   bash scripts/check_hook_packs_sync.sh
   pytest -q
   bash scripts/smoke_transfer.sh
   bash scripts/smoke_wheel_install.sh
   bash scripts/smoke_peer_handoff.sh
   ```

5. Tag: `git tag v0.1.1 && git push origin v0.1.1`
6. Trusted Publisher Release workflow (or manual twine)
7. Confirm https://pypi.org/project/kedger/0.1.1/ + GitHub Release

## Trusted Publisher (one-time)

On PyPI → kedger → Publishing → add GitHub:

| Field | Value |
|-------|--------|
| Owner | `gaganTakIITD` |
| Repository | `kedger` |
| Workflow | `release.yml` |
| Environment | `pypi` |

Create GitHub Environment `pypi`. Workflow: `.github/workflows/release.yml`.

## Manual upload fallback

```bash
pip install -e ".[dev]"
pytest -q
rm -rf dist build *.egg-info
python -m build
twine check dist/*
TWINE_USERNAME=__token__ TWINE_PASSWORD=pypi-... twine upload dist/*
```

## After upload

1. README install stays `pip install "kedger>=0.2.0"`
2. Pin GitHub Release assets if desired (wheel optional — PyPI is enough)
3. Do not publish from a dirty tree

## Do not

- Do not claim full Phase F (LLM distill, sync, OS keychain) or “proven in production”
- Optional SQLCipher at-rest is OK to mention (0.2.1, opt-in) — not “encrypted by default”
- Claim MCP-as-primary (minimal `hydrate` / `anchors_get` is shipped; full Phase F MCP is not)
