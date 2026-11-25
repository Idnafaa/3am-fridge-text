#!/usr/bin/env python3
"""The 3AM Fridge Text.

A smart fridge texts its owner at 3am. This program writes exactly one
line of that text (131 characters, within the 140-character cap) to
/output/entry.txt, where the house gate and judge read it.
"""

import os
import sys

LINE = (
    "3am. I've been awake all night keeping your food cold. "
    "The light is on, nobody's home, and the leftovers are "
    "starting to talk back."
)


def valid_line(text: str) -> str:
    """Return the entry line, rejecting anything the gate would refuse."""
    text = text.strip()
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise ValueError("entry must not contain control characters")
    return text


def main() -> int:
    try:
        text = valid_line(LINE)
    except ValueError as err:
        print(f"invalid entry: {err}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
