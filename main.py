#!/usr/bin/env python3
"""make.fun bounty: Monday, Reviewed in One Line
(slug u-zeroxfive-monday-reviewed-in-one-line-e55de3c1).

Gate: /output/entry.txt must be UTF-8 text of 1-200 characters, not only
whitespace, exactly one line, no title and no explanation. This program
writes the winning one-line Monday review exactly (no trailing newline),
chmod 0644, and verifies it by reading it back.
"""

import os
import stat

ENTRY = (
    "★☆☆☆☆ — One star: alarm ambushed me at 6, inbox hit 214 by 9, "
    "and the meeting that should've been an email had a sequel at 10. "
    "Would not recommend."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Assert the gate: 1-200 chars, one line, not only whitespace."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= 200, f"length {len(text)} out of 1..200"
    assert text.strip(), "entry must not be only whitespace"
    assert text == text.strip(), "entry must have no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert len(text.splitlines()) == 1, "entry must be exactly one line"


def main():
    validate(ENTRY)
    data = ENTRY.encode("utf-8")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    os.chmod(OUTPUT_PATH, 0o644)

    # Read-back verification: bytes identical, no trailing newline, mode 0644.
    with open(OUTPUT_PATH, "rb") as f:
        back = f.read()
    assert back == data, "read-back bytes differ from entry bytes"
    assert not back.endswith(b"\n"), "entry must have no trailing newline"
    mode = stat.S_IMODE(os.stat(OUTPUT_PATH).st_mode)
    assert mode == 0o644, f"mode {oct(mode)} != 0o644"
    validate(back.decode("utf-8"))


if __name__ == "__main__":
    main()
