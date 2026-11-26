#!/usr/bin/env python3
"""Worst Pizza Topping — make.fun bounty entry.

Writes one funny line pitching the worst imaginable pizza topping
to /output/entry.txt. Deterministic: no randomness, no network, no input.
"""

import os

ENTRY = (
    "Try our new topping: expired yogurt poured over raw oysters. "
    "It gurgles when you chew it, and by midnight, it eats you back."
)


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
