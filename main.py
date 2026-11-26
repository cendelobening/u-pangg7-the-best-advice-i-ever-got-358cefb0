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
    # MAKEFUN_OUTPUT_DIR names the writable output DIRECTORY; older
    # callers may pass a full ".../entry.txt" file path instead, so
    # normalize both shapes to a directory before joining the filename.
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if out.endswith(".txt"):
        out = os.path.dirname(out) or "."
    os.makedirs(out, exist_ok=True)
    output_path = os.path.join(out, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()
