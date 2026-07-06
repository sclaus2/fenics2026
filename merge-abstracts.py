from __future__ import annotations

import argparse
import json
import re
import unicodedata
from datetime import date, datetime
from pathlib import Path
from typing import Sequence
from urllib.parse import unquote, urlparse

from pypdf import PageObject, PdfReader, PdfWriter
from pypdf.generic import (
    ArrayObject,
    DecodedStreamObject,
    DictionaryObject,
    FloatObject,
    NameObject,
    NumberObject,
    RectangleObject,
)

here = Path(__file__).parent
EXPORT_STEM_LIMIT = 50
SUBMISSION_ORDER = {
    "Presentation": 0,
    "Poster": 1,
    "Software Demonstration": 2,
}
PAGE_WIDTH = 612
PAGE_HEIGHT = 792
INDEX_MARGIN_X = 54
INDEX_MARGIN_TOP = 64
INDEX_MARGIN_BOTTOM = 54
INDEX_COLUMN_GAP = 24
INDEX_TITLE_SIZE = 18
INDEX_TEXT_SIZE = 9
INDEX_LEADING = 12
WATERMARK_GRAY = 0.85
WATERMARK_FONT_SIZE = 8
WATERMARK_X = 0.05 * PAGE_WIDTH
WATERMARK_Y = 0.5 * PAGE_HEIGHT
DEFAULT_WATERMARK_DOI = "10.5281/zenodo.21225878"
DEFAULT_WATERMARK_VERSION = "v3"


def timestamp() -> str:
    return datetime.now().strftime("%H:%M:%S")


def log(message: str) -> None:
    print(f"[{timestamp()}] {message}", flush=True)


def load_manifest(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def build_export_name_map(abstract_dir: Path) -> dict[str, str]:
    counters: dict[str, int] = {}
    mapping: dict[str, str] = {}

    for markdown in sorted(abstract_dir.glob("*.md"), key=lambda path: path.name):
        base = markdown.stem[:EXPORT_STEM_LIMIT]
        count = counters.get(base, 0)
        counters[base] = count + 1
        export_stem = base if count == 0 else f"{base}-{count}"
        mapping[markdown.stem] = f"{export_stem}.pdf"

    return mapping


def default_pdf_order(input_folder: Path) -> list[Path]:
    return sorted(
        (
            pdf
            for pdf in input_folder.glob("*.pdf")
            if pdf.stem not in {"readme", "README", "fenics2026-book-of-abstracts"}
        ),
        key=lambda pdf: pdf.stem,
    )


def build_target_aliases(slug: str, export_name: str) -> set[str]:
    aliases = {
        slug.casefold(),
        f"{slug.casefold()}.md",
        f"abstracts/{slug.casefold()}.md",
        export_name.casefold(),
        export_name.removesuffix(".pdf").casefold(),
        f"abstracts/{export_name.casefold()}",
    }
    return aliases


def resolve_target_slug(target: str, alias_to_slug: dict[str, str]) -> str | None:
    if not target:
        return None

    decoded = unquote(str(target)).strip()
    parsed = urlparse(decoded)
    candidates = {
        decoded.casefold(),
        parsed.path.casefold(),
        Path(parsed.path).name.casefold(),
        Path(parsed.path).stem.casefold(),
    }
    path = parsed.path.casefold()
    if path:
        candidates.add(path.lstrip("./"))
        candidates.add(path.strip("/"))

    for candidate in list(candidates):
        if candidate in alias_to_slug:
            return alias_to_slug[candidate]

    markdown_match = re.search(r"abstracts/([^/#?]+)\.md$", path)
    if markdown_match:
        return alias_to_slug.get(markdown_match.group(1).casefold())

    pdf_match = re.search(r"([^/#?]+)\.pdf$", path)
    if pdf_match:
        stem = pdf_match.group(1).casefold()
        return alias_to_slug.get(stem)

    return None


def rewrite_readme_links(
    writer: PdfWriter,
    readme_pages: int,
    page_starts: dict[str, int],
    export_name_map: dict[str, str],
) -> None:
    log(f"Rewriting front-matter links for {len(page_starts)} abstracts")
    alias_to_slug: dict[str, str] = {}
    for slug, export_name in export_name_map.items():
        for alias in build_target_aliases(slug, export_name):
            alias_to_slug[alias] = slug

    for page_index in range(readme_pages):
        page = writer.pages[page_index]
        annots_ref = page.get("/Annots")
        if annots_ref is None:
            continue
        annots = annots_ref.get_object()
        for annot_ref in annots:
            annot = annot_ref.get_object()
            if annot.get("/Subtype") != "/Link":
                continue
            target = ""
            action = annot.get("/A")
            if action:
                if action.get("/URI"):
                    target = str(action["/URI"])
                elif action.get("/F"):
                    target = str(action["/F"])
            if not target:
                continue

            slug = resolve_target_slug(target, alias_to_slug)
            if slug is None or slug not in page_starts:
                continue

            rect = RectangleObject(tuple(float(value) for value in annot["/Rect"]))
            border_values = []
            for value in annot.get("/Border", [0, 0, 0])[:3]:
                numeric = float(value)
                border_values.append(NumberObject(int(numeric)) if numeric.is_integer() else FloatObject(numeric))

            annot.clear()
            annot.update(
                {
                    NameObject("/Type"): NameObject("/Annot"),
                    NameObject("/Subtype"): NameObject("/Link"),
                    NameObject("/Rect"): rect,
                    NameObject("/Border"): ArrayObject(border_values),
                    NameObject("/Dest"): ArrayObject(
                        [writer.pages[page_starts[slug]].indirect_reference, NameObject("/Fit")]
                    ),
                }
            )
            annot[NameObject("/P")] = page.indirect_reference


def add_outline(writer: PdfWriter, manifest: list[dict], page_starts: dict[str, int]) -> None:
    if not manifest:
        return
    log("Adding PDF outline")

    try:
        writer.page_mode = "/UseOutlines"
    except Exception:
        try:
            writer.set_page_mode("/UseOutlines")
        except Exception:
            pass

    grouped: dict[str, list[dict]] = {}
    for item in manifest:
        if item["slug"] in page_starts:
            grouped.setdefault(item["submission_type"], []).append(item)

    for submission_type in sorted(grouped, key=lambda item: SUBMISSION_ORDER.get(item, len(SUBMISSION_ORDER))):
        entries = grouped[submission_type]
        if not entries:
            continue
        first_slug = entries[0]["slug"]
        parent = writer.add_outline_item(submission_type, page_number=page_starts[first_slug], bold=True)
        for item in entries:
            writer.add_outline_item(item["title"], page_number=page_starts[item["slug"]], parent=parent)


def normalise_author_sort_name(name: str) -> tuple[str, str]:
    ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    tokens = re.findall(r"[A-Za-z0-9]+", ascii_name.casefold())
    if not tokens:
        return ("", "")
    particles = {"da", "de", "del", "der", "di", "dos", "du", "la", "le", "van", "von"}
    surname_tokens = [tokens[-1]]
    index = len(tokens) - 2
    while index >= 0 and tokens[index] in particles:
        surname_tokens.insert(0, tokens[index])
        index -= 1
    return (" ".join(surname_tokens), " ".join(tokens[: index + 1]))


def collect_author_index(manifest: list[dict], page_starts: dict[str, int]) -> list[tuple[str, list[int]]]:
    pages_by_author: dict[str, set[int]] = {}
    display_names: dict[str, str] = {}
    for item in manifest:
        slug = item.get("slug")
        if slug not in page_starts:
            continue
        page_number = page_starts[slug] + 1
        for author in item.get("authors", []):
            name = str(author.get("name", "")).strip()
            if not name:
                continue
            key = re.sub(r"\s+", " ", name).casefold()
            display_names.setdefault(key, re.sub(r"\s+", " ", name))
            pages_by_author.setdefault(key, set()).add(page_number)

    return sorted(
        ((display_names[key], sorted(pages)) for key, pages in pages_by_author.items()),
        key=lambda entry: (*normalise_author_sort_name(entry[0]), entry[0].casefold()),
    )


def pdf_text(value: str) -> str:
    ascii_value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    return ascii_value.replace("\\", r"\\").replace("(", r"\(").replace(")", r"\)")


def watermark_text(doi: str, version: str) -> str:
    today = date.today()
    doi_text = doi if doi.casefold().startswith("doi:") else f"doi:{doi}"
    return f"{doi_text}, {version}, {today:%B} {today.day}, {today:%Y}"


def add_author_index_watermark(commands: list[str], doi: str, version: str) -> None:
    commands.extend(
        [
            "q",
            f"{WATERMARK_GRAY:.2f} g",
            (
                f"BT /F1 {WATERMARK_FONT_SIZE} Tf "
                f"0 1 -1 0 {WATERMARK_X:.2f} {WATERMARK_Y:.2f} Tm "
                f"({pdf_text(watermark_text(doi, version))}) Tj ET"
            ),
            "Q",
        ]
    )


def add_text_line(commands: list[str], x: float, y: float, text: str, size: int = INDEX_TEXT_SIZE) -> None:
    commands.append(f"BT /F1 {size} Tf {x:.2f} {y:.2f} Td ({pdf_text(text)}) Tj ET")


def add_author_index(
    writer: PdfWriter,
    manifest: list[dict],
    page_starts: dict[str, int],
    watermark_doi: str,
    watermark_version: str,
) -> int | None:
    entries = collect_author_index(manifest, page_starts)
    if not entries:
        log("No author index entries found")
        return None

    log(f"Appending author index with {len(entries)} authors")
    first_index_page = len(writer.pages)
    column_width = (PAGE_WIDTH - 2 * INDEX_MARGIN_X - INDEX_COLUMN_GAP) / 2
    rows_per_column = int((PAGE_HEIGHT - INDEX_MARGIN_TOP - INDEX_MARGIN_BOTTOM - 28) / INDEX_LEADING)
    rows_per_page = rows_per_column * 2

    for page_offset in range(0, len(entries), rows_per_page):
        page_entries = entries[page_offset : page_offset + rows_per_page]
        page = PageObject.create_blank_page(width=PAGE_WIDTH, height=PAGE_HEIGHT)
        commands: list[str] = []
        add_author_index_watermark(commands, watermark_doi, watermark_version)
        commands.extend(["q", "0 0 0 rg"])
        if page_offset == 0:
            add_text_line(commands, INDEX_MARGIN_X, PAGE_HEIGHT - INDEX_MARGIN_TOP, "Author Index", INDEX_TITLE_SIZE)
        y_start = PAGE_HEIGHT - INDEX_MARGIN_TOP - 30
        for index, (author, pages) in enumerate(page_entries):
            column = index // rows_per_column
            row = index % rows_per_column
            x = INDEX_MARGIN_X + column * (column_width + INDEX_COLUMN_GAP)
            y = y_start - row * INDEX_LEADING
            page_text = ", ".join(str(page) for page in pages)
            entry_text = f"{author}  {page_text}"
            if len(entry_text) > 76:
                entry_text = entry_text[:73] + "..."
            add_text_line(commands, x, y, entry_text)
        commands.append("Q")

        stream = DecodedStreamObject()
        stream.set_data("\n".join(commands).encode("latin-1", errors="replace"))
        page[NameObject("/Contents")] = writer._add_object(stream)
        page[NameObject("/Resources")] = DictionaryObject(
            {
                NameObject("/Font"): DictionaryObject(
                    {
                        NameObject("/F1"): DictionaryObject(
                            {
                                NameObject("/Type"): NameObject("/Font"),
                                NameObject("/Subtype"): NameObject("/Type1"),
                                NameObject("/BaseFont"): NameObject("/Helvetica"),
                            }
                        )
                    }
                )
            }
        )
        writer.add_page(page)

    try:
        writer.add_outline_item("Author Index", page_number=first_index_page, bold=True)
    except Exception:
        pass
    return first_index_page


def apply_page_labels(writer: PdfWriter) -> None:
    try:
        page_count = len(writer.pages)
        if page_count > 0:
            writer.set_page_label(0, page_count - 1, style="/D", start=1)
    except Exception:
        pass


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Merge per-abstract PDFs into a single book of abstracts.")
    parser.add_argument("-i", "--input", type=Path, default=here / "book" / "_build" / "exports")
    parser.add_argument(
        "-m",
        "--manifest",
        type=Path,
        default=here / "book" / "abstracts" / "manifest.json",
        help="Manifest generated by build_book.py used to preserve abstract ordering.",
    )
    parser.add_argument(
        "-a",
        "--abstract-dir",
        type=Path,
        default=here / "book" / "abstracts",
        help="Directory containing the generated abstract markdown files.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=here / "fenics2026-book-of-abstracts.pdf",
    )
    parser.add_argument(
        "--no-author-index",
        action="store_true",
        help="Do not append the generated author index.",
    )
    parser.add_argument(
        "--watermark-doi",
        default=DEFAULT_WATERMARK_DOI,
        help="DOI text used in the author-index watermark, e.g. 10.5281/zenodo.21225878.",
    )
    parser.add_argument(
        "--watermark-version",
        default=DEFAULT_WATERMARK_VERSION,
        help="Version text used in the author-index watermark.",
    )
    args = parser.parse_args(argv)

    input_folder = args.input
    output_file = args.output.with_suffix(".pdf")
    if not input_folder.exists():
        print(f"{input_folder} does not exist")
        return 1
    log(f"Using PDF export directory: {input_folder}")

    readme_pdf = input_folder / "readme.pdf"
    if not readme_pdf.is_file():
        print(f"Missing required PDF: {readme_pdf}")
        print("Run `myst build --pdf` first.")
        return 1

    manifest = load_manifest(args.manifest)
    log(f"Loaded manifest entries: {len(manifest)}")
    if manifest:
        export_name_map = build_export_name_map(args.abstract_dir)
        abstract_items: list[tuple[dict, Path]] = []
        missing_files: list[Path] = []
        for item in manifest:
            export_name = export_name_map.get(item["slug"])
            if export_name is None:
                print(f"Could not resolve export filename for abstract: {item['slug']}")
                return 1
            pdf = input_folder / export_name
            if pdf.is_file():
                abstract_items.append((item, pdf))
            else:
                missing_files.append(pdf)

        if missing_files:
            print("Skipping abstracts without built PDFs:")
            for path in missing_files:
                print(f" - {path.name}")
        log(f"Resolved built abstract PDFs: {len(abstract_items)}")
    else:
        export_name_map = {}
        abstract_items = [
            (
                {"slug": pdf.stem, "title": pdf.stem, "submission_type": "Abstracts"},
                pdf,
            )
            for pdf in default_pdf_order(input_folder)
        ]
        log(f"Using default PDF order with {len(abstract_items)} PDFs")

    output_file.parent.mkdir(parents=True, exist_ok=True)
    merger = PdfWriter()
    readme_reader = PdfReader(str(readme_pdf))
    readme_pages = len(readme_reader.pages)
    page_starts: dict[str, int] = {}

    merger.append(readme_pdf, import_outline=False)
    current_page = readme_pages
    log(f"Appended front matter: {readme_pages} pages")
    for index, (item, pdf) in enumerate(abstract_items, start=1):
        log(f"Appending abstract {index}/{len(abstract_items)}: {pdf.name}")
        page_starts[item["slug"]] = current_page
        merger.append(pdf, import_outline=False)
        current_page += len(PdfReader(str(pdf)).pages)

    if export_name_map:
        rewrite_readme_links(merger, readme_pages, page_starts, export_name_map)
    add_outline(merger, manifest, page_starts)
    if manifest and not args.no_author_index:
        add_author_index(merger, manifest, page_starts, args.watermark_doi, args.watermark_version)
    apply_page_labels(merger)

    log(f"Writing merged PDF: {output_file}")
    merger.write(output_file)
    merger.close()
    log(f"Saved to: {output_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
