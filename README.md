# FEniCS Conference 2026 Book of Abstracts

This repository is based on Simula's scripts for FEniCS 2024. This repository contains the scripts and MyST template used to turn the FEniCS 2026 abstract submission export into:

- one Markdown file per abstract in [`book/abstracts`](book/abstracts)
- a generated landing page in [`book/README.md`](book/README.md)
- one PDF per abstract via MyST
- one merged PDF book of abstracts

## Installation

You need:

- Python 3
- Node.js
- LaTeX

Create and activate a virtual environment, then install the project dependencies:

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install .
```

If you are using a conda environment, activate it first and install into that same environment:

```bash
conda activate base
python -m pip install .
```

## Build The Full Book

From inside `fenics2026`, run:

```bash
python3 build_book.py <SOURCEFILE>
```

This does three things:

1. Regenerates `book/abstracts/*.md`, `book/abstracts/manifest.json`, `book/README.md`, and `book/all_abstracts.md`
2. Runs `myst build --pdf` inside `book`
3. Merges the generated PDFs into `book/_build/exports/fenics2026-book-of-abstracts.pdf`

If you are running from conda, prefer:

```bash
python build_book.py <SOURCEFILE>
```

## Run The Steps Manually

If you want to run the pipeline step by step:

```bash
python3 convert.py <SOURCEFILE>
cd book
myst build --pdf
cd ..
python3 merge-abstracts.py
```

## Notes

- `convert.py` clears the existing `book/abstracts/*.md` files by default before regenerating the 2026 set.
- Prefer the `.xlsx` export when you have it. It avoids CSV parsing entirely, although it cannot correct entries that were typed inconsistently in the original form.
- Placeholder submissions with title/text like `NA` are skipped automatically.
- `merge-abstracts.py` uses `book/abstracts/manifest.json` so the merged PDF follows the generated front-page order.
- If you want a different merged PDF filename, pass `--output` to `build_book.py`.
- `build_book.py` first tries the `myst` executable and then falls back to `python -m mystmd_py` in the current environment.

Example:

```bash
python3 build_book.py  <SOURCEFILE> --output book/_build/exports/book-of-abstracts-v1.pdf
```

## Fake Data

To generate a fake CSV in the 2026 schema:

```bash
python3 generate_fake_abstracts.py fake-abstracts.csv 10
```
