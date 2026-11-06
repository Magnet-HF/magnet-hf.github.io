<p align="center"><img src="assets/magnet-logo.png" alt="MagNet — Mutual Assistance Group Network" width="180"></p>

# MagNet Tools & Guides

The public technical library for MagNet software, operational guidance, radio configurations, and supporting resources.

**Planned public address:** https://magnet-hf.github.io/

- [Software directory source](content/software/index.md)
- [Operational guidance source](content/operational-guidance/index.md)
- [Radio setup source](content/radio-configurations/index.md)
- [Contribution instructions](content/contribute/index.md)
- [Maintainer setup](MAINTAINERS.md)

Website cards should link to stable paths such as `/software/fldigi/` and `/software/spotterx/`. Tool pages link to official download pages; technical guidance records suggested versions separately.

## Local preview

Requires Python 3.11 or newer.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install --require-hashes -r requirements.txt
.venv/bin/python scripts/build.py
.venv/bin/python -m http.server 8000 --directory dist
```

Open http://localhost:8000/. Markdown pages live under `content/`. The initial JSON block supplies the title, description, section, and editorial date. Category indexes list child guides automatically. Files under `documents/` are copied without modification. Build output is ignored by Git.

The build verifies local page, asset, document, and anchor links. External links require periodic human review. GitHub Actions builds pull requests and publishes only changes on `main` after merge.

## Attribution and publication

Existing documents retain their authors' rights. No blanket license is asserted over contributed material. Contributors must identify author/source and permission to publish. Maintainers should choose an explicit license for original website code and prose before encouraging reuse outside MagNet.
