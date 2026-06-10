# FEniCS Conference 2026 Book of Abstracts

This repository is based on Simula's scripts for FEniCS 2024. It contains the scripts and MyST template used to maintain the FEniCS 2026 book of abstracts:

- one Markdown file per abstract in [`book/abstracts`](book/abstracts)
- a generated programme/front-matter page in [`book/README.md`](book/README.md)
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


## Two-Step Workflow

The abstract markdown files are the reviewable source after the first import. Participants can open pull requests against their own file in [`book/abstracts`](book/abstracts), and maintainers can rebuild the programme/front matter and PDF from the committed markdown without touching the spreadsheet.

Spreadsheet exports are local maintainer inputs only. Do not commit `.xls`, `.xlsx`, or `.xlsm` files; GitHub Actions builds from the committed `programme.md` and `book/abstracts/*.md` files.

### 1. Import Abstracts From The Spreadsheet

First create the canonical programme source workbook from the corrected submission export:

```bash
cd fenics2026
python3 filter_programme_source.py
```

This writes `../AbstractProgrammeFEniCS2026.xlsx`, containing only unique abstracts referenced by `programme.md`. Then run the import only when you intentionally want to regenerate the individual abstract files from that workbook:

```bash
python3 convert.py ../AbstractProgrammeFEniCS2026.xlsx
```

By default, this clears and rewrites `book/abstracts/*.md`. Do not run it after participant PR edits unless you intend to re-import from the spreadsheet and review the resulting diff.

### 2. Rebuild From Markdown And Programme

Run this after changes to `programme.md` or any file in `book/abstracts`:

```bash
python3 build_book.py
```

This does three things:

1. Reads `book/abstracts/*.md`
2. Regenerates `book/README.md` and `book/abstracts/manifest.json`, ordered and grouped by `programme.md`
3. Builds per-abstract PDFs and merges them into `fenics2026-book-of-abstracts.pdf` in the repository root

To refresh only the programme/front matter and manifest:

```bash
python3 build_book.py --markdown-only
```

By default, `build_book.py` uses the serial MyST exporter because it gives useful per-file progress and avoids hangs in MyST's bulk exporter. To try MyST's bulk exporter explicitly, pass `--bulk-myst`.

For a faster rebuild when `book/_build/exports` already contains PDFs from a previous build, rebuild only changed or missing PDF exports:

```bash
python3 build_book.py --changed-only --base-ref origin/main
```

This still regenerates `book/README.md` and `book/abstracts/manifest.json`, then merges the final book in programme order. It rebuilds the front-matter PDF when `programme.md` or an abstract markdown file changed, rebuilds changed or missing abstract PDFs, and falls back to a full rebuild when templates or build scripts changed. GitHub Actions uses this mode with a cached `book/_build/exports` directory.

The committed PDF files in `book/_build/exports` are seed artifacts for CI cold starts. They are not participant-editable sources; edits should still be made in `programme.md` or `book/abstracts/*.md`, and CI will rebuild the affected PDF exports before merging the final book.

You can override the programme or output path when needed:

```bash
python3 build_book.py --programme programme.md --output book-of-abstracts-v1.pdf
```

The compatibility wrapper still works for the second step:

```bash
python3 rebuild_book_from_programme.py
```

## Notes

- `convert.py` is an import step only; it does not build PDFs or write the programme order.
- GitHub Actions does not need any spreadsheet files. It runs `python3 build_book.py` against `programme.md` and `book/abstracts/*.md`.
- Placeholder submissions with title/text like `NA` are skipped automatically.
- `build_book.py` reads the current markdown files, then writes `book/README.md` and `book/abstracts/manifest.json`.
- `merge-abstracts.py` uses `book/abstracts/manifest.json` so the merged PDF follows the generated programme/front-page order.
- If you want a different merged PDF filename, pass `--output` to `build_book.py`.
- `build_book.py` first tries the `myst` executable and then falls back to `python -m mystmd_py` in the current environment.
- Partial rebuilds use the committed seed PDFs and the GitHub Actions cache in `book/_build/exports`; without either, `--changed-only` rebuilds the missing exports.
