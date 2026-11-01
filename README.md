# jazzcommon — Canonical Jazz Standards Reference

**jazzcommon** is a small, zero-dependency Python CLI and dataset for canonical jazz standards. It provides a curated, offline-accessible collection of well-known jazz tunes, their lead-sheet meta-information, and a CLI for browsing, searching, and exporting the set.

## About

Jazz standards are the shared repertoire that musicians reach for when they sit down without a setlist. **jazzcommon** is a compact, structured reference of the tunes most often called "common practice" material: title, alternative titles, key, common tempos, form, and a short era tag.

It is not an exhaustive music database. It is a small offline companion for developers building practice tools, setlist helpers, educational projects, or any script that needs a clean canonical list of jazz standards without scraping a website.

## Features

- **Curated canonical list** — a stable bundled dataset of widely recognized jazz standards.
- **CLI browse** — `jazzcommon list` prints the full set in a readable table.
- **Search** — `jazzcommon search <term>` matches title, aliases, composer, and form fields.
- **Show one** — `jazzcommon show <title>` prints the full record for a standard.
- **Export** — `jazzcommon export --format json|csv` dumps the dataset for downstream use.
- **Tags / eras** — each tune includes a short era tag such as `early`, `swing`, `bop`, `hardbop`, `modal`, `postbop`, `standard`.
- **Zero runtime dependencies** — stdlib only; works on Python 3.11+.

## Installation

```bash
python -m pip install jazzcommon
```

Or run from a checkout:

```bash
git clone <repo-url>
cd jazzcommon
python -m pip install -e .
```

## Usage

```bash
jazzcommon [options] <command> [args]
```

### Commands

| Command               | Description                                                  |
|-----------------------|--------------------------------------------------------------|
| `list`                | Print the full canonical standards list.                     |
| `search <term>`       | Search title, aliases, composer, and form fields.           |
| `show <title>`        | Show one standard by title or well-known alias.              |
| `export --format <f>` | Export the dataset as `json` or `csv`.                      |
| `tags`                | List unique era tags in the dataset.                         |
| `--help`              | Show help and exit.                                          |

### Examples

```bash
# Browse everything
jazzcommon list

# Search by tune or composer
jazzcommon search gershwin
jazzcommon search "take the"

# Show one standard
jazzcommon show "Autumn Leaves"

# Export the dataset
jazzcommon export --format json > standards.json
jazzcommon export --format csv > standards.csv

# See era coverage
jazzcommon tags
```

### Record shape

Each standard record contains:

- `title` — canonical title
- `aliases` — common alternative titles
- `composer` — primary composer/contributor
- `key` — commonly referenced key when one dominates
- `form` — typical form, e.g. `AABA`, `ABAC`, `12-bar`, `32-bar`, `head-solos`
- `tempo` — common tempo feel, e.g. `ballad`, `medium`, `up`, `bright`
- `era` — short era tag

## Project Structure

```
jazzcommon.py     # CLI entrypoint and bundled standards dataset
pyproject.toml    # Package metadata, entrypoint, tool config
README.md         # This file
.gitignore        # Python build artifacts and common noise
```

- `jazzcommon.py` — flat single-module implementation: dataset, search, CLI
- `pyproject.toml` — packaging, console script, ruff config
- `README.md` — user-facing documentation
- `.gitignore` — keeps build metadata and editor noise out of the repo

## Tech Stack

- Python 3.11+
- Standard library only (`argparse`, `json`, `csv`, `io`, `sys`)
- `pyproject.toml` packaging with a `jazzcommon` console script entrypoint
- Flat single-module layout

## Tags / Keywords

`cli`, `jazz`, `music`, `standards`, `reference`, `dataset`, `terminal`, `zero-dependency`, `python`

## License

MIT
