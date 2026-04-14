from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Sequence

from faker import Faker

SUBMISSION_TYPE_FIELD = (
    "Is the submission relating to a poster, a software demonstration or a presentation?\n\n"
    "Participants can demonstrate their FEniCS-based software to small groups using their laptops. "
    "These “software demonstrations” take place at the same time as the poster session. One "
    "participant can choose to submit a presentation or a poster and a software demonstration - "
    "please submit the form twice."
)


def authors(fake: Faker, n: int) -> str:
    return ", ".join(fake.name() for _ in range(n))


def affiliations(fake: Faker, n: int) -> str:
    return ", ".join(fake.company() for _ in range(n))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a fake 2026 abstract submission CSV.")
    parser.add_argument("path", type=Path)
    parser.add_argument("N", type=int, default=10)
    args = vars(parser.parse_args(argv))

    fake = Faker()
    fake.seed_instance(4321)

    path = Path(args["path"]).with_suffix(".csv")

    fieldnames = [
        "Timestamp",
        "Email address",
        "Name of presenter",
        "Affiliation of presenter",
        SUBMISSION_TYPE_FIELD,
        "Are you a PhD candidate or a Postdoctoral researcher?",
        "Do you need a signed letter of acceptance (for VISA or other purposes)?",
        "Name of authors (including presenter, comma-separated list)",
        "Affiliation of co-authors (including presenter, comma-separated list)",
        "Abstract title",
        "Abstract text",
        "Reference list",
        "Do you agree to your presentation being recorded and for the recording to be made available on a video hosting platform after the conference?",
        "Do you accept the terms and conditions?",
    ]
    submission_types = ["Presentation", "Poster", "Software Demonstration"]

    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(args["N"]):
            num_authors = fake.random_int(1, 5)
            presenter_name = fake.name()
            presenter_affiliation = fake.company()
            coauthor_names = [presenter_name]
            coauthor_names.extend(fake.name() for _ in range(num_authors - 1))
            coauthor_affiliations = [presenter_affiliation]
            coauthor_affiliations.extend(fake.company() for _ in range(num_authors - 1))

            writer.writerow(
                {
                    "Timestamp": fake.iso8601(),
                    "Email address": fake.email(),
                    "Name of presenter": presenter_name,
                    "Affiliation of presenter": presenter_affiliation,
                    SUBMISSION_TYPE_FIELD: fake.random_element(submission_types),
                    "Are you a PhD candidate or a Postdoctoral researcher?": fake.random_element(
                        ["PhD candidate", "Postdoctoral researcher", "No"]
                    ),
                    "Do you need a signed letter of acceptance (for VISA or other purposes)?": fake.random_element(
                        ["Yes", "No"]
                    ),
                    "Name of authors (including presenter, comma-separated list)": ", ".join(coauthor_names),
                    "Affiliation of co-authors (including presenter, comma-separated list)": ", ".join(
                        coauthor_affiliations
                    ),
                    "Abstract title": fake.sentence(nb_words=8).rstrip("."),
                    "Abstract text": fake.paragraph(nb_sentences=8),
                    "Reference list": fake.paragraph(nb_sentences=2) if fake.random_int(0, 1) else "",
                    "Do you agree to your presentation being recorded and for the recording to be made available on a video hosting platform after the conference?": fake.random_element(
                        ["Yes", "No"]
                    ),
                    "Do you accept the terms and conditions?": "Yes",
                }
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
