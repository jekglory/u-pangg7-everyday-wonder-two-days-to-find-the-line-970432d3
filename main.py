#!/usr/bin/env python3
"""Everyday Wonder -- make.fun entry (program/v1, Python 3.13, stdlib only).

Writes one sentence -- a single line of at most 200 characters -- to
/output/entry.txt, where the competition's sealed scorer reads it. The
gate accepts UTF-8 text of 1 to 200 characters, not only white space;
the line below is 79 characters, and the file carries it plus one
trailing newline, so the file stays inside the gate at 80 characters.
The sentence takes its wonder from a dripping tap: one last, unheld
word from the pipes turns a household sound into something that speaks.
The program is fully deterministic: it writes the same line on every
run, so two runs produce byte-identical output.
"""

import os

LINE = "The tap drips once after I turn it off, a last word the pipes couldn't hold in."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE.strip()
    if not line or "\n" in line:
        raise ValueError("entry must be exactly one non-empty sentence")
    if len(line) > 200:
        raise ValueError(
            f"entry is {len(line)} characters, over the 200 limit"
        )
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()
