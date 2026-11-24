"""One-line office joke for make.fun's "Make the AI Judge Laugh: Office Jokes".

The program writes a single joke about office life to /output/entry.txt.
The joke is a fixed string: no randomness, no timestamps, no input of any
kind, so every run produces byte-identical output.
"""

import os
import sys

JOKE = (
    "My out-of-office reply starts with 'per my last email,' "
    "so even my absence sounds passive-aggressive."
)

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")

MIN_CHARS = 1
MAX_CHARS = 199


def check_joke(text):
    """The gate wants 1 to 199 UTF-8 characters, not only white space."""
    if not isinstance(text, str):
        raise TypeError("the joke must be text")
    if not text.strip():
        raise ValueError("the joke must not be only white space")
    if len(text) < MIN_CHARS or len(text) > MAX_CHARS:
        raise ValueError(
            "the joke is %d characters, the gate allows %d to %d"
            % (len(text), MIN_CHARS, MAX_CHARS)
        )
    text.encode("utf-8")
    return text


def write_entry(text):
    """Write the joke to the output path, then read it back to prove it."""
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    with open(OUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise ValueError("what was written does not match the joke")
    return written


def main():
    joke = check_joke(JOKE)
    written = write_entry(joke)
    print("wrote %s (%d characters)" % (OUT_PATH, len(written)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
