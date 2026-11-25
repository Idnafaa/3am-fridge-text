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


def main() -> int:
    text = LINE.strip()
    if not 1 <= len(text) <= 140:
        print(f"entry must be 1-140 characters, got {len(text)}", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
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
