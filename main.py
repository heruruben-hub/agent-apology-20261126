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


def main() -> None:
    line = APOLOGY.strip()
    if not line:
        raise SystemExit("apology line is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("apology line must be a single line")
    if line.count(".") != 1 or not line.endswith("."):
        raise SystemExit("apology line must be exactly one sentence")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"apology line is {len(line)} chars, over the {MAX_CHARS} limit"
        )
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
