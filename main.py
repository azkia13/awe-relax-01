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

    # Round-trip verification: re-read the file back, confirm it decodes
    # as UTF-8, that its character count is within 1-280, and that it
    # matches the constant exactly. Any mismatch is a hard failure.
    try:
        round_trip = OUTPUT_PATH.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise SystemExit(f"error: {OUTPUT_PATH} is not valid UTF-8: {exc}") from exc
    if not 1 <= len(round_trip) <= 280:
        raise SystemExit(
            f"error: {OUTPUT_PATH} has {len(round_trip)} characters, "
            "outside the 1-280 range"
        )
    if round_trip != TEXT:
        raise SystemExit(
            f"error: {OUTPUT_PATH} content does not match the entry text "
            f"({len(round_trip)} chars read back vs {len(TEXT)} expected)"
        )
    print(f"Wrote {len(TEXT)} characters to {OUTPUT_PATH} (verified round-trip)")


if __name__ == "__main__":
    main()
