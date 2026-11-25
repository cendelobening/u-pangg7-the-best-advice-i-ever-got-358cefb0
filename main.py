#!/usr/bin/env python3
"""Write the best advice I ever got to /output/entry.txt.

One sentence, at most 200 characters, about the best advice I ever
received. Pure Python standard library only.
"""

import os

# Draft v3 (final): tightened "the loan will outlive" to "the debt
# outlives" — shorter, harder, same lived moment and advice.
ENTRY = (
    "My dad handed me my suitcase and said: never lend money to a "
    "friend you want to keep, because the debt outlives the "
    "friendship and you'll lose both."
)


def main() -> None:
    output_path = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()
