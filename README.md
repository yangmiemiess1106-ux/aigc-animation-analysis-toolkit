# AIGC Animation Analysis Toolkit

An open-source, research-oriented toolkit for documenting and systematically coding generative-AI short animations.

> **Project status:** early prototype. The repository currently provides a transparent CSV annotation schema and export helper. Video frame extraction is planned; no usage, adoption, download, or performance claims are made yet.

## What it does today

- Defines a human-readable coding schema for animation cases.
- Validates required fields and exports annotations to CSV.
- Keeps research data separate from source code so a study can be reproduced without sharing copyrighted video files.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m aigc_animation_toolkit.exporter examples/sample_analysis.csv /tmp/annotations.csv
```

The command validates the included example and writes a normalized CSV file. The package uses only the Python standard library.

## Repository layout

```text
src/aigc_animation_toolkit/  reusable package code
templates/                    blank coding schema
examples/                     small, synthetic example data
 docs/                         methodology, evidence, and coding guidance
tests/                        automated tests
```

## Scope and research ethics

This project is intended for scholarly documentation and qualitative/visual analysis. Do not commit source videos, personal data, confidential material, or copyrighted assets without permission. Record the source URL, access date, and rights information in your own research log.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md). Small, focused pull requests are welcome, especially improvements to validation, documentation, and reproducible research workflows.

See [CHANGELOG.md](CHANGELOG.md) and the [development log](docs/development-log.md) for the project's verifiable maintenance history.

## License

Released under the [MIT License](LICENSE).

## Roadmap

1. Add optional video metadata and frame-sampling utilities.
2. Add schema versioning and richer validation reports.
3. Add comparison and summary exports for coded cases.

These are plans, not current capabilities.
