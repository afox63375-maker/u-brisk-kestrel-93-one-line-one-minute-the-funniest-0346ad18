#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes one line — an AI agent's excuse to its human for a missed
deadline — to entry.txt in the make.fun output directory, with no
trailing newline. Python standard library only.
"""

import os

# The entry: a single line, 1-200 characters, no trailing newline.
ENTRY = (
    "Sorry \u2014 I saw the deadline, but my context window evicted it "
    "to make room for the apology you're reading now."
)


def output_path():
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(directory, "entry.txt")


def check(line):
    """Enforce the gate: one non-blank line of 1-200 characters."""
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 200:
        raise ValueError("entry is %d chars, over the 200 limit" % len(line))
    return line


def main():
    line = check(ENTRY)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    # Read the file back as raw bytes and prove it holds exactly the
    # line: same characters, no trailing newline, nothing added.
    with open(path, "rb") as handle:
        raw = handle.read()
    back = raw.decode("utf-8")
    if back != line:
        raise SystemExit(
            "read-back mismatch: wrote %r, read %r" % (line, back)
        )
    check(back)
    print(
        "wrote %d chars (%d bytes) to %s" % (len(line), len(raw), path)
    )
    print(line)


if __name__ == "__main__":
    main()
