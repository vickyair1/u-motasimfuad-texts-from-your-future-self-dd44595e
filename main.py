#!/usr/bin/env python3
"""Texts From Your Future Self — one funny text from your future self.

The entry is a single text message, under 200 characters, that reads exactly
as it would arrive on your phone: no setup, no context, just the message.
"""

import os
import sys

MAX_CHARS = 200
MIN_CHARS = 1

ENTRY = (
    "it's me, you, from 2031. do NOT throw away that box of cables. "
    "you'll need exactly one of them, and you will cry."
)


def main() -> int:
    text = ENTRY
    assert MIN_CHARS <= len(text) <= MAX_CHARS, (
        f"entry length {len(text)} outside {MIN_CHARS}..{MAX_CHARS}"
    )
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert text.isprintable(), "entry must be printable text"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)  # no trailing newline
    return 0


if __name__ == "__main__":
    sys.exit(main())
