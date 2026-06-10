from __future__ import annotations

import argparse
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Sequence

here = Path(__file__).parent
default_programme_path = here / "programme.md" if (here / "programme.md").is_file() else here.parent / "programme.md"


def timestamp() -> str:
    return datetime.now().strftime("%H:%M:%S")


def log(message: str) -> None:
    print(f"[{timestamp()}] {message}", flush=True)


def run(command: list[str], cwd: Path, label: str) -> None:
    log(f"START {label}")
    log("+ " + " ".join(str(part) for part in command))
    start = time.monotonic()
    subprocess.run(command, cwd=cwd, check=True)
    log(f"DONE {label} after {time.monotonic() - start:.1f}s")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate the FEniCS 2026 book of abstracts from current markdown using the programme order."
    )
    parser.add_argument(
        "--programme",
        type=Path,
        default=default_programme_path,
        help="Programme markdown file used to order and group abstracts.",
    )
    parser.add_argument(
        "--book-dir",
        type=Path,
        default=here / "book",
        help="Book directory to regenerate.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=here / "book" / "_build" / "exports" / "fenics2026-book-of-abstracts-programme-indexed.pdf",
        help="Output PDF path when building the full PDF.",
    )
    parser.add_argument(
        "--markdown-only",
        action="store_true",
        help="Only regenerate README.md and abstracts/manifest.json from current abstract markdown.",
    )
    parser.add_argument(
        "--bulk-myst",
        action="store_true",
        help="Use MyST's bulk PDF exporter instead of the default serial exporter.",
    )
    args = parser.parse_args(argv)

    if not args.programme.is_file():
        print(f"Missing programme file: {args.programme}")
        return 1

    command = [
        sys.executable,
        str(here / "build_book.py"),
        "--book-dir",
        str(args.book_dir),
        "--programme",
        str(args.programme),
        "--output",
        str(args.output),
    ]
    if args.markdown_only:
        command.append("--markdown-only")
    if args.bulk_myst:
        command.append("--bulk-myst")
    run(
        command,
        cwd=here,
        label="build programme-ordered book from markdown",
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
