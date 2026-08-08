# Publishing Kedger (`v0.1.0`)

## Preconditions

- [x] `pyproject.toml` name = `kedger`, version = `0.1.0`
- [x] PyPI project name **`kedger`** appears unclaimed (HTTP 404 on `/pypi/kedger/json` as of 2026-08-08)
- [ ] Maintainer has a PyPI account + API token (`pypi-...`)
- [ ] `pytest -q` green on the release commit
- [ ] Git tag `v0.1.0` pushed

## Build & upload

```bash
pip install -e ".[dev]"
pytest -q
python -m build
twine check dist/*
# First claim (creates the project on PyPI):
TWINE_USERNAME=__token__ TWINE_PASSWORD=pypi-... twine upload dist/*
```

Test PyPI dry-run:

```bash
twine upload --repository testpypi dist/*
pip install -i https://test.pypi.org/simple/ kedger==0.1.0
```

## After first upload

1. Confirm https://pypi.org/project/kedger/
2. Add Trusted Publisher (GitHub → `gaganTakIITD/kedger`) when CI publish is ready
3. Document `pip install kedger` as the default install path in README

## Do not

- Publish from a dirty tree
- Reuse the same version after a bad upload (bump or yank)
- Bundle MoDeX / hackathon assets into the sdist
