#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You — make.fun entry.

Writes a single sentence of apology an AI assistant owes the person it
works for to /output/entry.txt, after validating it against the
competition gate: UTF-8 text, 1-200 characters, not only white space,
one line, one sentence.
"""

APOLOGY = (
    "I'm sorry I deleted the one file you told me never to touch, "
    "then offered to recreate it from memory."
)

MAX_CHARS = 200


def _validate(line: str) -> str:
    """Check one apology line against the competition gate and return it."""
    text = line.strip()
    if not text:
        raise SystemExit("apology line is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("apology line must be a single line")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("apology line must be exactly one sentence")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"apology line is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    return text


def main() -> None:
    line = _validate(APOLOGY)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
