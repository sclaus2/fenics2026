from __future__ import annotations

import argparse
import csv
import json
import re
import unicodedata
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from textwrap import dedent
from typing import Sequence

here = Path(__file__).parent

DEFAULT_BOOK_TITLE = "FEniCS Conference 2026 Book of Abstracts"
DEFAULT_BOOK_SUBTITLE = "Generated from conference abstract submissions"
DEFAULT_BOOK_AUTHOR = "FEniCS Conference 2026 Organizing Committee"
PLACEHOLDER_VALUES = {"na", "n/a", "none", "null", "nan", "-"}
NON_NAME_HINTS = (
    "analysis",
    "university",
    "department",
    "laboratory",
    "lab",
    "college",
    "research",
    "centre",
    "center",
    "institute",
    "institut",
    "school",
    "faculty",
    "hospital",
    "scientific",
    "computing",
    "phd",
    "postdoctoral",
    "student",
    "scientist",
    "professor",
    "meudon",
    "france",
    "norway",
    "oslo",
    "onera",
    "simula",
    "polytechnique",
)
SUBMISSION_TYPE_FIELD = (
    "Is the submission relating to a poster, a software demonstration or a presentation?\n\n"
    "Participants can demonstrate their FEniCS-based software to small groups using their laptops. "
    "These “software demonstrations” take place at the same time as the poster session. One "
    "participant can choose to submit a presentation or a poster and a software demonstration - "
    "please submit the form twice."
)
SUBMISSION_ORDER = {
    "Presentation": 0,
    "Poster": 1,
    "Software Demonstration": 2,
}

FIELD_ALIASES = {
    "email": ("Email address", "Username"),
    "presenter_name": ("Name of presenter",),
    "presenter_affiliation": ("Affiliation of presenter",),
    "submission_type": (SUBMISSION_TYPE_FIELD,),
    "title": ("Abstract title",),
    "text": ("Abstract text",),
    "authors": ("Name of authors (including presenter, comma-separated list)",),
    "affiliations": ("Affiliation of co-authors (including presenter, comma-separated list)",),
    "references": ("Reference list",),
}

ABSTRACT_TEMPLATE = dedent(
    """\
    ---
    title: {title}
    {authors}
    license: CC-BY-4.0
    exports:
      - format: pdf
        template: ../../template

    ---

    {metadata}

    {text}
    {references}

    """
)

README_TEMPLATE = dedent(
    """\
    ---
    title: {book_title_yaml}
    authors:
      - name: {book_author}
    license: CC-BY-4.0
    exports:
      - format: pdf
        template: ../template
    ---

    # {book_title}

    {book_subtitle}

    Total abstracts: **{num_abstracts}**

    {sections}
    """
)

ALL_ABSTRACTS_TEMPLATE = dedent(
    """\
    ---
    title: 'All abstracts'
    authors:
      - name: {book_author}
    license: CC-BY-4.0
    exports:
      - format: pdf
        template: ../template
    ---

    This page is a placeholder for the merged PDF build.
    Run `python3 merge-abstracts.py` after `myst build --pdf` to create the combined file.
    """
)


def quote_yaml(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def normalise_text(value: str) -> str:
    return value.replace("\r\n", "\n").strip()


def is_placeholder(value: str) -> bool:
    return normalise_space(value).casefold().strip(".") in PLACEHOLDER_VALUES


def normalise_space(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip(" ,;")


def split_outside_brackets(value: str, delimiter: str = ",") -> list[str]:
    parts: list[str] = []
    current: list[str] = []
    round_depth = 0
    square_depth = 0
    curly_depth = 0
    for char in value:
        if char == "(":
            round_depth += 1
        elif char == ")" and round_depth > 0:
            round_depth -= 1
        elif char == "[":
            square_depth += 1
        elif char == "]" and square_depth > 0:
            square_depth -= 1
        elif char == "{":
            curly_depth += 1
        elif char == "}" and curly_depth > 0:
            curly_depth -= 1

        if char == delimiter and round_depth == 0 and square_depth == 0 and curly_depth == 0:
            part = "".join(current).strip()
            if part:
                parts.append(part)
            current = []
            continue
        current.append(char)

    part = "".join(current).strip()
    if part:
        parts.append(part)
    return parts


def split_name_chunks(value: str) -> list[str]:
    if not value:
        return []

    chunks: list[str] = []
    for part in split_outside_brackets(value.replace("\n", " "), ","):
        for subpart in re.split(r"\s+(?:and|&)\s+", part):
            cleaned = normalise_space(subpart)
            if cleaned:
                chunks.append(cleaned)
    return chunks


def slugify(value: str) -> str:
    normalised = unicodedata.normalize("NFKD", value)
    ascii_value = normalised.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_value.lower()).strip("-")
    return slug or "abstract"


def escape_table(value: str) -> str:
    return value.replace("|", "\\|")


def find_value(row: dict[str, str], field: str, default: str = "") -> str:
    for alias in FIELD_ALIASES[field]:
        if alias in row and row[alias].strip():
            value = normalise_text(row[alias])
            if is_placeholder(value):
                return default
            return value
    return default


def extract_affiliation_markers(value: str) -> list[str]:
    markers: list[str] = []
    marker_groups = []
    for pattern in (
        r"\^\{([^}]*)\}",
        r"\^\(([^)]*)\)",
        r"\(([0-9,\s]+)\)\)?$",
    ):
        marker_groups.extend(re.findall(pattern, value))
    for group in marker_groups:
        markers.extend(re.findall(r"\d+", group))
    return list(dict.fromkeys(markers))


def clean_author_name(value: str) -> str:
    cleaned = re.sub(r"\^\{[^}]*\}", "", value)
    cleaned = re.sub(r"\^\([^)]*\)", "", cleaned)
    cleaned = re.sub(r"\(([0-9,\s]+)\)\)?$", "", cleaned)
    cleaned = re.sub(r"\[[0-9,\s]+\]$", "", cleaned)
    return normalise_space(cleaned).strip("()")


def looks_like_person_name(value: str) -> bool:
    lower = value.casefold()
    if not value or any(hint in lower for hint in NON_NAME_HINTS):
        return False
    if any(char.isdigit() for char in value):
        return False

    tokens = re.findall(r"[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ.'’-]*", value)
    return 2 <= len(tokens) <= 6


def parse_author_entries(value: str) -> list[tuple[str, list[str]]]:
    entries: list[tuple[str, list[str]]] = []
    for chunk in split_name_chunks(value):
        cleaned = clean_author_name(chunk)
        if looks_like_person_name(cleaned):
            entries.append((cleaned, extract_affiliation_markers(chunk)))
    return entries


def clean_affiliation_text(value: str) -> str:
    return normalise_space(value.replace("\n", " "))


def parse_numbered_affiliations(value: str) -> dict[str, str]:
    if not value:
        return {}
    matches = list(re.finditer(r"(?:(?<=^)|(?<=\n)|(?<=,)\s*)(\d+)[.)]\s*", value))
    if not matches:
        return {}

    affiliations: dict[str, str] = {}
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(value)
        affiliation = clean_affiliation_text(value[start:end]).strip(",")
        if affiliation:
            affiliations[match.group(1)] = affiliation
    return affiliations


def strip_leading_author_list(value: str) -> str:
    parts = split_outside_brackets(value, ",")
    if not parts:
        return value

    first = parts[0]
    entries = parse_author_entries(first)
    if entries:
        return value[len(first) :].lstrip(" ,")
    return value


def parse_extra_author_entries_from_affiliations(value: str) -> list[tuple[str, list[str]]]:
    parts = split_outside_brackets(value, ",")
    if not parts:
        return []
    return parse_author_entries(parts[0])


def build_authors(
    presenter_name: str,
    presenter_affiliation: str,
    email: str,
    raw_authors: str,
    raw_affiliations: str,
) -> list["Author"]:
    presenter_name = clean_author_name(presenter_name)
    author_entries = parse_author_entries(raw_authors)
    extra_entries = parse_extra_author_entries_from_affiliations(raw_affiliations)

    ordered_entries: list[tuple[str, list[str]]] = []
    seen_names: set[str] = set()

    if presenter_name:
        ordered_entries.append((presenter_name, []))
        seen_names.add(presenter_name.casefold())

    for name, markers in [*author_entries, *extra_entries]:
        key = name.casefold()
        if presenter_name and len(presenter_name.split()) == 1 and key.startswith(f"{presenter_name.casefold()} "):
            ordered_entries[0] = (name, markers)
            seen_names.discard(presenter_name.casefold())
            seen_names.add(key)
            presenter_name = name
            continue
        if key not in seen_names:
            ordered_entries.append((name, markers))
            seen_names.add(key)

    if not ordered_entries and presenter_name:
        ordered_entries.append((presenter_name, []))

    numbered_affiliations = parse_numbered_affiliations(raw_affiliations)
    cleaned_affiliation_field = clean_affiliation_text(strip_leading_author_list(raw_affiliations))
    simple_affiliations = [
        clean_affiliation_text(part)
        for part in split_outside_brackets(cleaned_affiliation_field, ",")
        if clean_affiliation_text(part)
    ]

    authors: list[Author] = []
    for index, (name, markers) in enumerate(ordered_entries):
        affiliation = ""
        if markers and numbered_affiliations:
            affiliation = "; ".join(
                dict.fromkeys(numbered_affiliations[marker] for marker in markers if marker in numbered_affiliations)
            )
        elif simple_affiliations and len(simple_affiliations) == len(ordered_entries):
            affiliation = simple_affiliations[index]
        elif name.casefold() == presenter_name.casefold() and presenter_affiliation:
            affiliation = presenter_affiliation
        elif cleaned_affiliation_field:
            affiliation = cleaned_affiliation_field
        else:
            affiliation = presenter_affiliation or "Affiliation unavailable"

        authors.append(
            Author(
                name=name,
                affiliation=affiliation or "Affiliation unavailable",
                email=email if index == 0 else "",
            )
        )

    return authors


@dataclass
class Author:
    name: str
    affiliation: str
    email: str = ""

    def to_myst(self) -> str:
        lines = [
            f"- name: {quote_yaml(self.name)}",
            "  affiliations:",
            f"    - {quote_yaml(self.affiliation)}",
        ]
        if self.email:
            lines.append(f"  email: {quote_yaml(self.email)}")
        return "\n".join(lines)


@dataclass
class Submission:
    slug: str
    title: str
    presenter: str
    presenter_affiliation: str
    submission_type: str
    authors: list[Author]
    text: str
    references: str

    def to_markdown(self) -> str:
        authors_block = "authors:\n" + "\n".join(f"  {line}" for author in self.authors for line in author.to_myst().splitlines())

        metadata_lines = []
        if self.submission_type:
            metadata_lines.append(f"**Submission type:** {self.submission_type}")
        presenter_line = self.presenter
        if self.presenter_affiliation:
            presenter_line = f"{presenter_line} ({self.presenter_affiliation})"
        if presenter_line.strip():
            metadata_lines.append(f"**Presenter:** {presenter_line}")
        metadata = "\n\n".join(metadata_lines)

        references = ""
        if self.references:
            ref_text = "\n\n".join(part for part in self.references.split("\n") if part.strip())
            references = f"\n# References\n{ref_text}\n"

        return ABSTRACT_TEMPLATE.format(
            title=quote_yaml(self.title),
            authors=authors_block,
            metadata=metadata,
            text=self.text,
            references=references,
        )


def build_submission(row: dict[str, str], used_slugs: set[str]) -> Submission:
    title = find_value(row, "title")
    presenter = find_value(row, "presenter_name")
    presenter_affiliation = find_value(row, "presenter_affiliation")
    submission_type = find_value(row, "submission_type", default="Presentation")
    email = find_value(row, "email")
    text = find_value(row, "text")
    references = find_value(row, "references")
    authors = build_authors(
        presenter_name=presenter,
        presenter_affiliation=presenter_affiliation,
        email=email,
        raw_authors=find_value(row, "authors"),
        raw_affiliations=find_value(row, "affiliations"),
    )
    presenter_name = presenter or (authors[0].name if authors else "")
    if authors and presenter_name:
        short_presenter = clean_author_name(presenter_name)
        lead_author = clean_author_name(authors[0].name)
        if len(short_presenter.split()) < len(lead_author.split()) and lead_author.casefold().startswith(
            short_presenter.casefold()
        ):
            presenter_name = authors[0].name
    presenter_affiliation = presenter_affiliation or (authors[0].affiliation if authors else "")

    slug_base = slugify(title)
    slug = slug_base
    suffix = 2
    while slug in used_slugs:
        slug = f"{slug_base}-{suffix}"
        suffix += 1
    used_slugs.add(slug)

    return Submission(
        slug=slug,
        title=title,
        presenter=presenter_name,
        presenter_affiliation=presenter_affiliation,
        submission_type=submission_type,
        authors=authors,
        text=text,
        references=references,
    )


def sort_key(submission: Submission) -> tuple[int, str, str]:
    return (
        SUBMISSION_ORDER.get(submission.submission_type, len(SUBMISSION_ORDER)),
        submission.title.casefold(),
        submission.presenter.casefold(),
    )


def render_sections(submissions: list[Submission]) -> str:
    grouped: defaultdict[str, list[Submission]] = defaultdict(list)
    for submission in submissions:
        grouped[submission.submission_type].append(submission)

    sections = []
    ordered_types = sorted(grouped, key=lambda item: SUBMISSION_ORDER.get(item, len(SUBMISSION_ORDER)))
    for submission_type in ordered_types:
        items = sorted(grouped[submission_type], key=lambda item: (item.title.casefold(), item.presenter.casefold()))
        section_title = f"{submission_type}s"
        if submission_type == "Software Demonstration":
            section_title = "Software Demonstration Session"
        lines = [f"## {section_title} ({len(items)})"]
        if submission_type == "Software Demonstration":
            lines.extend(
                [
                    "",
                    "These abstracts belong to the live software demonstration session.",
                ]
            )
        lines.extend(["", "| Title | Presenter |", "| :--- | :--- |"])
        for item in items:
            lines.append(
                f"| [{escape_table(item.title)}](abstracts/{item.slug}.md) | {escape_table(item.presenter)} |"
            )
        sections.append("\n".join(lines))
    return "\n\n".join(sections)


def write_book_pages(
    submissions: list[Submission],
    book_dir: Path,
    book_title: str,
    book_subtitle: str,
    book_author: str,
) -> None:
    book_dir.mkdir(parents=True, exist_ok=True)
    sections = render_sections(submissions)
    (book_dir / "README.md").write_text(
        README_TEMPLATE.format(
            book_title_yaml=quote_yaml(book_title),
            book_title=book_title,
            book_subtitle=book_subtitle,
            book_author=quote_yaml(book_author),
            num_abstracts=len(submissions),
            sections=sections,
        ),
        encoding="utf-8",
    )
    (book_dir / "all_abstracts.md").write_text(
        ALL_ABSTRACTS_TEMPLATE.format(book_author=quote_yaml(book_author)),
        encoding="utf-8",
    )


def load_rows(path: Path) -> list[dict[str, str]]:
    suffix = path.suffix.casefold()
    if suffix == ".csv":
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            return list(csv.DictReader(handle))

    if suffix == ".xlsx":
        try:
            from openpyxl import load_workbook
        except ImportError:
            print("Reading .xlsx files requires `openpyxl`. Install dependencies with `python3 -m pip install .`.")
            raise SystemExit(1)

        workbook = load_workbook(path, read_only=True, data_only=True)
        worksheet = workbook[workbook.sheetnames[0]]
        rows = list(worksheet.iter_rows(values_only=True))
        if not rows:
            return []
        headers = [str(value).strip() if value is not None else "" for value in rows[0]]
        data: list[dict[str, str]] = []
        for values in rows[1:]:
            row = {
                header: "" if value is None else str(value).strip()
                for header, value in zip(headers, values)
                if header
            }
            data.append(row)
        return data

    print(f"Unsupported input format: {path.suffix}. Use .csv or .xlsx.")
    raise SystemExit(1)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Convert conference abstract CSV/XLSX exports into MyST markdown.")
    parser.add_argument("path", type=Path, help="CSV or XLSX export from the conference abstract submission form.")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Directory for individual abstract markdown files. Defaults to book/abstracts.",
    )
    parser.add_argument(
        "--book-dir",
        type=Path,
        default=here / "book",
        help="Book directory where README.md and all_abstracts.md will be generated.",
    )
    parser.add_argument(
        "--keep-existing",
        action="store_true",
        help="Keep existing markdown files in the abstract output directory instead of clearing it first.",
    )
    parser.add_argument("--book-title", default=DEFAULT_BOOK_TITLE)
    parser.add_argument("--book-subtitle", default=DEFAULT_BOOK_SUBTITLE)
    parser.add_argument("--book-author", default=DEFAULT_BOOK_AUTHOR)
    args = parser.parse_args(argv)

    csv_path = args.path
    if not csv_path.is_file():
        print(f"{csv_path} is not a file")
        return 1

    output_dir = args.output or args.book_dir / "abstracts"
    output_dir.mkdir(parents=True, exist_ok=True)

    if not args.keep_existing:
        for markdown_file in output_dir.glob("*.md"):
            markdown_file.unlink()
        manifest_path = output_dir / "manifest.json"
        if manifest_path.exists():
            manifest_path.unlink()

    used_slugs: set[str] = set()
    submissions: list[Submission] = []
    for row in load_rows(csv_path):
        title = find_value(row, "title")
        text = find_value(row, "text")
        if not title or not text or is_placeholder(title) or is_placeholder(text):
            continue
        submissions.append(build_submission(row, used_slugs))

    submissions.sort(key=sort_key)

    for submission in submissions:
        (output_dir / f"{submission.slug}.md").write_text(submission.to_markdown(), encoding="utf-8")

    manifest = [asdict(submission) for submission in submissions]
    (output_dir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    write_book_pages(submissions, args.book_dir, args.book_title, args.book_subtitle, args.book_author)

    print(f"Wrote {len(submissions)} abstracts to {output_dir}")
    print(f"Wrote generated book pages to {args.book_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
