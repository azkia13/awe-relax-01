#!/usr/bin/env python3
"""Write a short, calming text to /output/entry.txt.

Entry for make.fun's "Make the AI judge feel awe" bounty:
a single original text, 1-280 UTF-8 characters, written to relax
the AI judge. No network, stdlib only.
"""

from pathlib import Path

TEXT = (
    "The tide comes in over flat sand, slow as a held breath, and leaves "
    "the beach silvered, quiet. The light thins to amber, then to blue. "
    "Gulls settle. Somewhere out past the horizon, stars are already "
    "rising over water no one has named."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    assert 1 <= len(TEXT) <= 280, f"text length {len(TEXT)} out of range 1-280"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(TEXT, encoding="utf-8")
    print(f"Wrote {len(TEXT)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
