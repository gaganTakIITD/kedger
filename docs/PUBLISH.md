# Publishing Kedger

## Current PyPI status

| Version | Notes |
|---------|--------|
| `0.1.0` | On PyPI now — thinner CLI surface |
| `0.1.1` | Launch tip — publish after merge |

Project: https://pypi.org/project/kedger/

**Do not reuse `0.1.0`.** Bump for every upload.

## GitHub About (do this on launch day)

Repo settings → **General** → About (or CLI below). Empty description/topics hurt discoverability.

**Description (paste):**
```text
Kedger — local-first eng-memory CLI for coding agents (not MoDeX). Hooks → Anchors → sealed .kxp
```

**Homepage:** `https://pypi.org/project/kedger/`

**Topics:**
```text
cli python agents cursor claude-code memory handoff local-first sealed-packs developer-tools
```

**Social preview:** upload `docs/assets/social.png` (1280×640) under Settings → General → Social preview.

**Optional:** disable Wiki (docs live in `/docs`); keep Issues on; Discussions optional.

```bash
# Maintainer machine (needs repo admin)
gh repo edit gaganTakIITD/kedger \
  --description "Local-first eng-memory CLI for coding agents — hooks → Anchors → sealed .kxp handoff" \
  --homepage "https://pypi.org/project/kedger/" \
  --add-topic cli --add-topic python --add-topic agents \
  --add-topic cursor --add-topic claude-code --add-topic memory \
  --add-topic handoff --add-topic local-first --add-topic sealed-packs \
  --add-topic developer-tools \
  --enable-wiki=false
```

First GitHub Release: tag `v0.1.1`, title **Kedger 0.1.1**, body from `CHANGELOG.md` (Install + peer workflow blurb).

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

1. README install stays `pip install "kedger>=0.1.1"`
2. Pin GitHub Release assets if desired (wheel optional — PyPI is enough)
3. Do not publish from a dirty tree; do not bundle MoDeX assets

## Do not

- Claim Phase F features (LLM distill / sync / MCP) as shipped
- Market Kedger as MoDeX
