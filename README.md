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

Install the project dependencies:

```bash
python3 -m pip install .
```


## Build The Full Book

From inside `fenics2026`, run:

```bash
python3 build_book.py <SOURCEFILE>
```

This does three things:

1. Regenerates `book/abstracts/*.md`, `book/abstracts/manifest.json`, `book/README.md`, and `book/all_abstracts.md`
2. Runs `myst build --pdf` inside `book`
3. Merges the individual abstract PDFs into `book/_build/exports/fenics2026-book-of-abstracts.pdf`

This default path preserves the existing abstract layout: each abstract is typeset on its own page with the template-driven title, authors, affiliations, and logo.

## Run The Steps Manually

If you want to run the pipeline step by step:

```bash
python3 convert.py <SOURCEFILE>
cd book
myst build --pdf
cd ..
python3 merge-abstracts.py
```

To build the optional single combined document instead, run:

```bash
python3 build_book.py <SOURCEFILE> --final-mode single
```

## Notes

- `convert.py` clears the existing `book/abstracts/*.md` files by default before regenerating the 2026 set.
- Placeholder submissions with title/text like `NA` are skipped automatically.
- `merge-abstracts.py` uses `book/abstracts/manifest.json` so the merged PDF follows the generated front-page order.
- `--final-mode single` builds from `book/all_abstracts.md`, but that mode does not preserve the same per-abstract title-page styling as the merged default.
- If you want a different merged PDF filename, pass `--output` to `build_book.py`.
- `build_book.py` first tries the `myst` executable and then falls back to `python -m mystmd_py` in the current environment.

Example:

```bash
python3 build_book.py  <SOURCEFILE> --output book/_build/exports/book-of-abstracts-v1.pdf
```
