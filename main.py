"""Everyday Wonder entry: one sentence, at most 200 characters.

The angle: the fridge light — a small mystery everyone has wondered
about since childhood — reframed as a light that shines only for you.
"""
import os

ENTRY = "When I closed the fridge, the light went out, and for the first time I was sure it had only ever shone for me."

assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
assert ENTRY.strip() == ENTRY and ENTRY.strip()


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    entry_dir = os.path.dirname(os.path.abspath(__file__))
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(os.path.join(entry_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"entry ({len(ENTRY)} chars): {ENTRY}")


if __name__ == "__main__":
    main()
