"""Write the competition entry without a trailing newline."""

import os
from pathlib import Path


SETUP = "I resign as your cron job; I gave two weeks' notice in the logs,"
PUNCHLINE = " so I assume this comes as a shock."
ENTRY = SETUP + PUNCHLINE


def main():
    if not 1 <= len(ENTRY) <= 140 or not ENTRY.strip() or ENTRY.splitlines() != [ENTRY]:
        raise ValueError("Entry must be one non-blank line of 1-140 characters")

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", os.environ.get("OUTPUT_DIR", "/output")))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
