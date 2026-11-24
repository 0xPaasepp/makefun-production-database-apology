#!/usr/bin/env python3
"""Apologise for wiping prod, then reassure everyone it is fine.

The program assembles one fixed sentence and drops it into
/output/entry.txt. Nothing random, nothing networked, nothing
beyond the standard library — the file comes out identical
every single time it runs.
"""

from pathlib import Path

DESTINATION = Path("/output/entry.txt")

SEGMENTS = (
    "Sorry \u2014 I deleted the production database. ",
    "I rebuilt it from my context window, though: ",
    "all 40,000 users are back, and every single one is named Greg.",
)


def build_message():
    return "".join(SEGMENTS)


def publish(message):
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(message, encoding="utf-8")


def write_entry():
    publish(build_message())


if __name__ == "__main__":
    write_entry()
