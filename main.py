#!/usr/bin/env python3
"""One Line, Big Laugh.

Writes one line -- a single hilarious line that lands entirely on its
own -- to /output/entry.txt.
"""

import os

LINE = "My therapist says I deflect with humor, so now my childhood trauma comes with a laugh track and a subscription I can't cancel."


def main() -> None:
    # Gate: the bounty only accepts a single line of 1-200 chars.
    assert 1 <= len(LINE) <= 200, f"entry line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE, "entry line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
