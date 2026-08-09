# Publishing Kedger

## Current PyPI status

| Version | Notes |
|---------|--------|
| `0.1.0` | On PyPI — thinner CLI surface |
| `0.1.1` | **Live** — https://pypi.org/project/kedger/0.1.1/ |

Project: https://pypi.org/project/kedger/

**Do not reuse `0.1.0`.** Bump for every upload.

## Marketing / stars / LinkedIn

See [`docs/MARKETING.md`](MARKETING.md) for positioning lock, claim guardrails, LinkedIn paste pack, and peer-trial protocol.

**Claim guardrails:** alpha + mechanical tests only; never Phase F or “proven in production.”

## GitHub About

**Status (2026-08-09):** description, homepage, topics, and wiki-off are set on `gaganTakIITD/kedger`.

**Still maintainer UI:** Social preview — `open_graph_image_url` is null until you upload `docs/assets/social.png`.

```bash
bash scripts/set_github_about.sh          # refresh description/topics (needs admin)
bash scripts/remind_social_preview.sh     # prints Settings → Social preview steps
```

**Description:**
```text
Local-first eng-memory CLI for coding agents — hooks → Anchors → sealed .kxp handoff
```

**Homepage:** `https://pypi.org/project/kedger/`

**Topics:** cli, python, agents, cursor, claude-code, memory, handoff, local-first, sealed-packs, developer-tools

Release `v0.1.1` already published; body from `CHANGELOG.md`.

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
3. Do not publish from a dirty tree

## Do not

- Claim Phase F features (LLM distill / sync / MCP) as shipped
