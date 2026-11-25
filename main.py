#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest — entry program.

Writes a single crypto/trading joke (under 200 characters) to
/output/entry.txt, where the make.fun grader reads it.

The joke: a seed-phrase gag. The field is full of dip-buying and
stop-loss jokes, so this one takes the self-custody angle instead —
the safest wallet in crypto is the one even its owner cannot open.
"""

import os

JOKE = (
    "I keep my seed phrase on paper so hackers can't steal it. "
    "I lost the paper \u2014 so now it's the most secure wallet in crypto: "
    "even I can't get in."
)


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    out_dir = "/output" if os.path.isdir("/output") else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
