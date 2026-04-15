from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Sequence
from urllib.parse import unquote, urlparse

from pypdf import PdfReader, PdfWriter
from pypdf.generic import ArrayObject, FloatObject, NameObject, NumberObject, RectangleObject

here = Path(__file__).parent
EXPORT_STEM_LIMIT = 50
SUBMISSION_ORDER = {
    "Presentation": 0,
    "Poster": 1,
    "Software Demonstration": 2,
}


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
            if pdf.stem
            not in {"readme", "README", "all-abstracts", "all_abstracts", "fenics2026-book-of-abstracts"}
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
        help="Manifest generated by convert.py used to preserve abstract ordering.",
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
        default=here / "book" / "_build" / "exports" / "fenics2026-book-of-abstracts.pdf",
    )
    args = parser.parse_args(argv)

    input_folder = args.input
    output_file = args.output.with_suffix(".pdf")
    if not input_folder.exists():
        print(f"{input_folder} does not exist")
        return 1

    readme_pdf = input_folder / "readme.pdf"
    if not readme_pdf.is_file():
        print(f"Missing required PDF: {readme_pdf}")
        print("Run `myst build --pdf` first.")
        return 1

    manifest = load_manifest(args.manifest)
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
    else:
        export_name_map = {}
        abstract_items = [({"slug": pdf.stem, "title": pdf.stem, "submission_type": "Abstracts"}, pdf) for pdf in default_pdf_order(input_folder)]

    output_file.parent.mkdir(parents=True, exist_ok=True)
    merger = PdfWriter()
    readme_reader = PdfReader(str(readme_pdf))
    readme_pages = len(readme_reader.pages)
    page_starts: dict[str, int] = {}

    merger.append(readme_pdf, import_outline=False)
    current_page = readme_pages
    for item, pdf in abstract_items:
        page_starts[item["slug"]] = current_page
        merger.append(pdf, import_outline=False)
        current_page += len(PdfReader(str(pdf)).pages)

    if export_name_map:
        rewrite_readme_links(merger, readme_pages, page_starts, export_name_map)
    add_outline(merger, manifest, page_starts)
    apply_page_labels(merger)

    merger.write(output_file)
    merger.close()
    print(f"Saved to: {output_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
