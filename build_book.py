from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime
from dataclasses import asdict
from pathlib import Path
from typing import Sequence

from convert import (
    DEFAULT_BOOK_AUTHOR,
    DEFAULT_BOOK_SUBTITLE,
    DEFAULT_BOOK_TITLE,
    DEFAULT_PROGRAMME_PATH,
    Author,
    Submission,
    apply_programme_order,
    normalise_space,
    parse_programme,
    write_book_pages,
)

here = Path(__file__).parent
EXPORT_STEM_LIMIT = 50
FULL_REBUILD_PATHS = {
    ".github/workflows/build_docs.yml",
    ".github/workflows/deploy_docs.yml",
    "book/myst.yml",
    "build_book.py",
    "convert.py",
    "merge-abstracts.py",
    "pyproject.toml",
}
FULL_REBUILD_PREFIXES = (
    "book/assets/",
    "template/",
)


def timestamp() -> str:
    return datetime.now().strftime("%H:%M:%S")


def log(message: str) -> None:
    print(f"[{timestamp()}] {message}", flush=True)


def run_command(command: list[str], cwd: Path, label: str) -> None:
    env = os.environ.copy()
    env_bin = str(Path(sys.executable).parent)
    env["PATH"] = f"{env_bin}{os.pathsep}{env.get('PATH', '')}"
    log(f"START {label}")
    log(f"CMD {' '.join(command)}")
    start = time.monotonic()
    process = subprocess.Popen(
        command,
        cwd=cwd,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
    )
    assert process.stdout is not None
    for line in process.stdout:
        elapsed = time.monotonic() - start
        print(f"[{timestamp()} +{elapsed:7.1f}s] {line}", end="", flush=True)
    return_code = process.wait()
    elapsed = time.monotonic() - start
    if return_code != 0:
        log(f"FAILED {label} after {elapsed:.1f}s with exit code {return_code}")
        raise subprocess.CalledProcessError(return_code, command)
    log(f"DONE {label} after {elapsed:.1f}s")


def resolve_myst_command(requested_command: str) -> list[str] | None:
    env_command = Path(sys.executable).parent / requested_command
    if env_command.is_file():
        return [str(env_command)]

    if shutil.which(requested_command):
        return [requested_command]

    if requested_command == "myst":
        try:
            from mystmd_py.main import main as _myst_main  # noqa: F401
        except ImportError:
            return None
        return [
            sys.executable,
            "-c",
            "from mystmd_py.main import main; raise SystemExit(main())",
        ]

    return None


def load_manifest_slugs(book_dir: Path) -> list[str]:
    manifest_path = book_dir / "abstracts" / "manifest.json"
    if not manifest_path.is_file():
        return []
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    return [item["slug"] for item in manifest if item.get("slug")]


def build_myst_serial(myst_command: list[str], book_dir: Path, targets: Sequence[str] | None = None) -> None:
    if targets is None:
        slugs = load_manifest_slugs(book_dir)
        targets = ["README.md", *[f"abstracts/{slug}.md" for slug in slugs]]
    log(f"Serial MyST export targets: {len(targets)} files")
    for index, target in enumerate(targets, start=1):
        run_command(
            [*myst_command, "build", target, "--pdf"],
            cwd=book_dir,
            label=f"build MyST PDF {index}/{len(targets)}: {target}",
        )


def unquote_yaml_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == "'" and value[-1] == "'":
        return value[1:-1].replace("''", "'")
    if len(value) >= 2 and value[0] == '"' and value[-1] == '"':
        return value[1:-1].replace(r"\"", '"')
    return value


def split_frontmatter(text: str) -> tuple[list[str], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return [], text

    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return lines[1:index], "\n".join(lines[index + 1 :]).lstrip("\n")
    return [], text


def parse_frontmatter(frontmatter_lines: Sequence[str]) -> tuple[str, list[Author]]:
    title = ""
    authors: list[Author] = []
    current_author: dict[str, object] | None = None
    collecting_affiliations = False

    def finish_author() -> None:
        nonlocal current_author
        if current_author is None:
            return
        name = str(current_author.get("name", "")).strip()
        affiliations = [str(value).strip() for value in current_author.get("affiliations", []) if str(value).strip()]
        email = str(current_author.get("email", "")).strip()
        if name:
            authors.append(
                Author(
                    name=name,
                    affiliations=affiliations or ["Affiliation unavailable"],
                    email=email,
                    name_is_literal=True,
                )
            )
        current_author = None

    for line in frontmatter_lines:
        stripped = line.strip()
        if stripped.startswith("title:"):
            title = unquote_yaml_scalar(stripped.removeprefix("title:").strip())
            collecting_affiliations = False
            continue

        if stripped.startswith("- name:"):
            finish_author()
            current_author = {"name": "", "affiliations": [], "email": ""}
            name_value = stripped.removeprefix("- name:").strip()
            if name_value:
                current_author["name"] = unquote_yaml_scalar(name_value)
            collecting_affiliations = False
            continue

        if current_author is None:
            continue

        if stripped.startswith("literal:"):
            current_author["name"] = unquote_yaml_scalar(stripped.removeprefix("literal:").strip())
            collecting_affiliations = False
        elif stripped.startswith("affiliations:"):
            collecting_affiliations = True
        elif collecting_affiliations and stripped.startswith("- "):
            current_author["affiliations"].append(unquote_yaml_scalar(stripped.removeprefix("- ").strip()))
        elif stripped.startswith("email:"):
            current_author["email"] = unquote_yaml_scalar(stripped.removeprefix("email:").strip())
            collecting_affiliations = False
        elif re.match(r"^[A-Za-z_-]+:", stripped):
            collecting_affiliations = False

    finish_author()
    return title, authors


def parse_presenter(value: str) -> tuple[str, str]:
    match = re.fullmatch(r"(.+?)\s*\((.+)\)", value.strip())
    if match:
        return normalise_space(match.group(1)), normalise_space(match.group(2))
    return normalise_space(value), ""


def parse_body_metadata(body: str) -> tuple[str, str, str, str, str]:
    submission_type = "Presentation"
    presenter = ""
    presenter_affiliation = ""
    body_without_metadata: list[str] = []
    in_leading_metadata = True

    for line in body.splitlines():
        type_match = re.fullmatch(r"\*\*Submission type:\*\*\s*(.+)", line.strip())
        if in_leading_metadata and type_match:
            submission_type = normalise_space(type_match.group(1))
            continue

        presenter_match = re.fullmatch(r"\*\*Presenter:\*\*\s*(.+)", line.strip())
        if in_leading_metadata and presenter_match:
            presenter, presenter_affiliation = parse_presenter(presenter_match.group(1))
            continue

        if in_leading_metadata and not line.strip():
            continue

        in_leading_metadata = False
        body_without_metadata.append(line)

    content = "\n".join(body_without_metadata).strip()
    references = ""
    reference_match = re.search(r"(?:^|\n)# References\n", content)
    if reference_match:
        references = content[reference_match.end() :].strip()
        content = content[: reference_match.start()].strip()

    return submission_type, presenter, presenter_affiliation, content, references


def load_markdown_submission(path: Path) -> Submission:
    text = path.read_text(encoding="utf-8")
    frontmatter_lines, body = split_frontmatter(text)
    title, authors = parse_frontmatter(frontmatter_lines)
    submission_type, presenter, presenter_affiliation, abstract_text, references = parse_body_metadata(body)

    if not presenter and authors:
        presenter = authors[0].name

    return Submission(
        slug=path.stem,
        title=title or path.stem.replace("-", " ").title(),
        presenter=presenter,
        presenter_affiliation=presenter_affiliation,
        submission_type=submission_type,
        authors=authors,
        text=abstract_text,
        references=references,
    )


def load_markdown_submissions(book_dir: Path) -> list[Submission]:
    abstract_dir = book_dir / "abstracts"
    if not abstract_dir.is_dir():
        raise FileNotFoundError(f"Missing abstract directory: {abstract_dir}")
    return [load_markdown_submission(path) for path in sorted(abstract_dir.glob("*.md"))]


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


def normalise_repo_path(value: str | Path) -> str:
    path = Path(value)
    if path.is_absolute():
        try:
            path = path.resolve().relative_to(here.resolve())
        except ValueError:
            return path.as_posix()
    return path.as_posix().removeprefix("./")


def git_output_lines(command: list[str]) -> list[str] | None:
    try:
        result = subprocess.run(
            command,
            cwd=here,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except subprocess.CalledProcessError as error:
        message = error.stderr.strip() or error.stdout.strip() or str(error)
        log(f"Could not run `{' '.join(command)}`: {message}")
        return None
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def collect_changed_paths(base_ref: str | None, explicit_paths: Sequence[str]) -> list[str] | None:
    if explicit_paths:
        return sorted({normalise_repo_path(path) for path in explicit_paths if str(path).strip()})

    paths: set[str] = set()
    if base_ref:
        changed = git_output_lines(["git", "diff", "--name-only", f"{base_ref}...HEAD"])
        if changed is None:
            changed = git_output_lines(["git", "diff", "--name-only", base_ref, "HEAD"])
        if changed is None:
            return None
        paths.update(normalise_repo_path(path) for path in changed)

    for command in (["git", "diff", "--name-only"], ["git", "diff", "--name-only", "--cached"]):
        changed = git_output_lines(command)
        if changed is not None:
            paths.update(normalise_repo_path(path) for path in changed)

    untracked = git_output_lines(["git", "ls-files", "--others", "--exclude-standard", "book/abstracts/*.md"])
    if untracked is not None:
        paths.update(normalise_repo_path(path) for path in untracked)

    return sorted(paths)


def is_abstract_markdown(path: str) -> bool:
    return path.startswith("book/abstracts/") and path.endswith(".md")


def needs_full_rebuild(changed_paths: Sequence[str]) -> bool:
    for path in changed_paths:
        if path in FULL_REBUILD_PATHS or any(path.startswith(prefix) for prefix in FULL_REBUILD_PREFIXES):
            log(f"Full rebuild required because `{path}` changed")
            return True
    return False


def add_target(targets: list[str], target: str) -> None:
    if target not in targets:
        targets.append(target)


def collect_partial_targets(book_dir: Path, submissions: Sequence[Submission], changed_paths: Sequence[str]) -> list[str]:
    targets: list[str] = []
    slugs = {submission.slug for submission in submissions}
    export_name_map = build_export_name_map(book_dir / "abstracts")
    export_dir = book_dir / "_build" / "exports"

    source_changes_affect_front_matter = "programme.md" in changed_paths or any(
        is_abstract_markdown(path) for path in changed_paths
    )
    if source_changes_affect_front_matter or not (export_dir / "readme.pdf").is_file():
        add_target(targets, "README.md")

    for path in changed_paths:
        if not is_abstract_markdown(path):
            continue
        slug = Path(path).stem
        if slug in slugs and (book_dir / "abstracts" / f"{slug}.md").is_file():
            add_target(targets, f"abstracts/{slug}.md")

    for submission in submissions:
        export_name = export_name_map.get(submission.slug)
        if export_name is None:
            add_target(targets, f"abstracts/{submission.slug}.md")
            continue
        if not (export_dir / export_name).is_file():
            add_target(targets, f"abstracts/{submission.slug}.md")

    return targets


def write_manifest(submissions: list[Submission], book_dir: Path) -> None:
    manifest_path = book_dir / "abstracts" / "manifest.json"
    manifest_path.write_text(json.dumps([asdict(submission) for submission in submissions], indent=2), encoding="utf-8")
    log(f"Wrote manifest: {manifest_path}")


def prepare_programme_book(
    book_dir: Path,
    programme: Path | None,
    book_title: str,
    book_subtitle: str,
    book_author: str,
) -> list[Submission]:
    submissions = load_markdown_submissions(book_dir)
    if not submissions:
        raise ValueError(f"No abstract markdown files found in {book_dir / 'abstracts'}")

    programme_entries = parse_programme(programme) if programme else []
    ordered_submissions = apply_programme_order(submissions, programme_entries)
    write_manifest(ordered_submissions, book_dir)
    write_book_pages(ordered_submissions, book_dir, book_title, book_subtitle, book_author, programme_entries)
    log(f"Wrote programme front matter: {book_dir / 'README.md'}")
    if programme_entries:
        matched_entries = sum(1 for entry in programme_entries if entry.slug is not None)
        log(f"Matched {matched_entries}/{len(programme_entries)} programme entries from {programme}")
    return ordered_submissions


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build the FEniCS 2026 book of abstracts from committed markdown files."
    )
    parser.add_argument(
        "--book-dir",
        type=Path,
        default=here / "book",
        help="MyST book directory. Defaults to fenics2026/book.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=here / "fenics2026-book-of-abstracts.pdf",
        help="Path for the merged PDF.",
    )
    parser.add_argument(
        "--myst-command",
        default="myst",
        help="MyST CLI command to use. Defaults to `myst`.",
    )
    parser.add_argument(
        "--programme",
        type=Path,
        default=DEFAULT_PROGRAMME_PATH if DEFAULT_PROGRAMME_PATH.is_file() else None,
        help="Programme markdown file used to order and group abstracts. Defaults to programme.md when present.",
    )
    parser.add_argument(
        "--bulk-myst",
        action="store_true",
        help="Use MyST's bulk PDF exporter instead of the default serial exporter.",
    )
    parser.add_argument(
        "--changed-only",
        action="store_true",
        help=(
            "Reuse existing PDFs in book/_build/exports and rebuild only changed abstract PDFs, "
            "missing PDFs, and the generated front matter. Falls back to a full rebuild when "
            "templates or build scripts changed."
        ),
    )
    parser.add_argument(
        "--base-ref",
        default=None,
        help="Git ref or SHA used with --changed-only to detect changed source files.",
    )
    parser.add_argument(
        "--changed-file",
        action="append",
        default=[],
        help="Explicit changed source path for --changed-only. Can be passed multiple times.",
    )
    parser.add_argument(
        "--force-full",
        action="store_true",
        help="Ignore --changed-only and rebuild every PDF.",
    )
    parser.add_argument(
        "--markdown-only",
        action="store_true",
        help="Only regenerate README.md and abstracts/manifest.json from the current markdown files.",
    )
    parser.add_argument("--book-title", default=DEFAULT_BOOK_TITLE)
    parser.add_argument("--book-subtitle", default=DEFAULT_BOOK_SUBTITLE)
    parser.add_argument("--book-author", default=DEFAULT_BOOK_AUTHOR)
    args = parser.parse_args(argv)

    changed_paths: list[str] | None = None
    if args.changed_only and not args.force_full:
        changed_paths = collect_changed_paths(args.base_ref, args.changed_file)
        if changed_paths is None:
            log("Changed paths could not be determined; using a full rebuild")
        elif changed_paths:
            log("Changed source paths:")
            for path in changed_paths:
                log(f" - {path}")
        else:
            log("No changed source paths detected")

    submissions = prepare_programme_book(
        book_dir=args.book_dir,
        programme=args.programme,
        book_title=args.book_title,
        book_subtitle=args.book_subtitle,
        book_author=args.book_author,
    )
    if args.markdown_only:
        return 0

    myst_command = resolve_myst_command(args.myst_command)
    if myst_command is None:
        print(
            f"Could not find a usable MyST command for `{args.myst_command}`. "
            "Install dependencies in the same Python environment that runs this script."
        )
        return 1
    merge_script = here / "merge-abstracts.py"
    build_dir = args.book_dir / "_build"
    use_partial_rebuild = (
        args.changed_only
        and not args.force_full
        and changed_paths is not None
        and not needs_full_rebuild(changed_paths)
    )

    if use_partial_rebuild:
        partial_targets = collect_partial_targets(args.book_dir, submissions, changed_paths)
        if partial_targets:
            if args.bulk_myst:
                log("Ignoring --bulk-myst for partial rebuild targets")
            build_myst_serial(myst_command, args.book_dir, partial_targets)
        else:
            log("All required per-page PDFs are already present; skipping MyST PDF export")
    else:
        if build_dir.exists():
            log(f"Removing existing build directory: {build_dir}")
            shutil.rmtree(build_dir)

    if args.bulk_myst and not use_partial_rebuild:
        run_command([*myst_command, "build", "--pdf"], cwd=args.book_dir, label="build MyST PDFs")
    elif not use_partial_rebuild:
        build_myst_serial(myst_command, args.book_dir)

    run_command(
        [
            sys.executable,
            str(merge_script),
            "--input",
            str(args.book_dir / "_build" / "exports"),
            "--abstract-dir",
            str(args.book_dir / "abstracts"),
            "--output",
            str(args.output),
        ],
        cwd=here,
        label="merge PDFs and append author index",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
