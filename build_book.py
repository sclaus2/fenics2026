from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Sequence

here = Path(__file__).parent


def run_command(command: list[str], cwd: Path) -> None:
    print("+", " ".join(command))
    subprocess.run(command, cwd=cwd, check=True)


def resolve_myst_command(requested_command: str) -> list[str] | None:
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


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the FEniCS 2026 book of abstracts PDF from a CSV/XLSX export.")
    parser.add_argument("path", type=Path, help="CSV or XLSX export from the abstract submission form.")
    parser.add_argument(
        "--book-dir",
        type=Path,
        default=here / "book",
        help="MyST book directory. Defaults to fenics2026/book.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=here / "book" / "_build" / "exports" / "fenics2026-book-of-abstracts.pdf",
        help="Path for the merged PDF.",
    )
    parser.add_argument(
        "--myst-command",
        default="myst",
        help="MyST CLI command to use. Defaults to `myst`.",
    )
    args = parser.parse_args(argv)

    if not args.path.is_file():
        print(f"{args.path} is not a file")
        return 1
    myst_command = resolve_myst_command(args.myst_command)
    if myst_command is None:
        print(
            f"Could not find a usable MyST command for `{args.myst_command}`. "
            "Install dependencies in the same Python environment that runs this script."
        )
        return 1

    convert_script = here / "convert.py"
    merge_script = here / "merge-abstracts.py"

    run_command([sys.executable, str(convert_script), str(args.path), "--book-dir", str(args.book_dir)], cwd=here)
    run_command([*myst_command, "build", "--pdf"], cwd=args.book_dir)
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
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
