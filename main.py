"""Office Jokes entry: write one office joke to /output/entry.txt."""

import os

JOKE = "My out-of-office reply starts with 'per my last email,' so even my absence sounds passive-aggressive."

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Gate check, mirroring the scorer: one line, 1-199 chars, not blank."""
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 199:
        raise ValueError(f"entry must be 1-199 characters, got {len(text)}")


def main() -> None:
    validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(JOKE)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != JOKE:
        raise ValueError("read-back mismatch: output differs from the joke")
    print(f"wrote {len(written)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
