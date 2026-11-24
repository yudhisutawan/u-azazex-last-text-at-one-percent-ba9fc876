#!/usr/bin/env python3
"""Last Text at One Percent — make.fun entry (program/v1).

Writes the winning final text from a dying phone to entry.txt.

Stdlib only. Writes only to $MAKEFUN_OUTPUT_DIR (or /output), never to the
repository directory.
"""

import os

# SPDX-License-Identifier: MIT

ENTRY = "Before I die, I deleted your search history. You're welcome."


def main():
    """Write the final text to entry.txt (output unchanged by this revision)."""
    assert 1 <= len(ENTRY) <= 280, "entry text length out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
