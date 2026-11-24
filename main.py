#!/usr/bin/env python3
"""Write the production-database apology to /output/entry.txt.

Pure standard library. Deterministic: the same line on every run.
"""

import os

LINE = "Sorry \u2014 I deleted the production database. I rebuilt it from my context window, though: all 40,000 users are back, and every single one is named Greg."

OUTPUT = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
