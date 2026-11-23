"""Dad Joke Showdown entry.

Writes the single dad joke stored in joke.txt to
$MAKEFUN_OUTPUT_DIR/entry.txt (the grader's output path).
Standard library only. Deterministic: same bytes every run.
"""

import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "joke.txt"), "r", encoding="utf-8") as f:
        joke = f.read().strip()

    if not joke:
        print("joke.txt is empty", file=sys.stderr)
        return 1
    if len(joke) > 200:
        print(f"joke is {len(joke)} characters, over the 200 limit",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(joke)
    print(f"wrote {len(joke)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
