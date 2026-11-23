"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch-note line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
The line is a single-line software release note for a bug in human biology,
in the terse register of a real changelog. Stdlib only, no network, no input
files: everything the entry runs ships in this repository.

The joke is written to land on a first read: a version number, the stock
"fixed a bug where" phrasing, and one specific, instantly recognisable bug
of daily life — the brain choosing 3 a.m. to replay an old embarrassment
instead of sleeping. No setup the punchline does not need.
"""

import os
import sys

ENTRY = (
    "v2.4.1: fixed a bug where the brain replayed an embarrassing "
    "moment from 2014 at 3 a.m. instead of sleeping."
)

MAX_CHARS = 160


def main() -> int:
    text = ENTRY
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"error: entry is {len(text)} chars, must be 1..{MAX_CHARS}",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("error: entry is blank", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
