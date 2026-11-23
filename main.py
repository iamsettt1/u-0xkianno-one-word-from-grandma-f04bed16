#!/usr/bin/env python3
"""One Word From Grandma — entry program.

Writes exactly one word to /output/entry.txt: the single word our
grandma would text about AI.

The word is "robit": the typo a grandma would actually make while
trying to type "robot" on her phone. It is funny in one word (the
misspelling is the joke), it sounds warm and a little baffled, it is
tied to robots/AI rather than to any subject at all, and it is fresher
than the obvious pick "robot" while still instantly readable.

The output is a fixed constant, so the program is fully deterministic.
"""

import os

WORD = "robit"

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Self-check against the competition gate: UTF-8 text, 1 to 30
    # characters, not only white space. Refuse to write anything that
    # would fail the gate instead of shipping a bad entry.
    text = WORD
    if not (1 <= len(text) <= 30) or not text.strip():
        raise ValueError("entry word fails the gate: %r" % (text,))
    if any(ch.isspace() for ch in text):
        raise ValueError("entry must be a single word: %r" % (text,))
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
