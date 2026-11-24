#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes a single username-worthy word to /output/entry.txt and prints it.
The word is "Kerfuffle": a commotion in one breath, funny on first read,
impossible to forget, and a handle its owner would happily wear.
"""

import os

WORD = "Kerfuffle"


def main() -> None:
    # The grader collects /output/entry.txt; fall back to a local output
    # folder when /output is not writable (local runs only).
    written = False
    for base in ("/output", "output"):
        try:
            os.makedirs(base, exist_ok=True)
            path = os.path.join(base, "entry.txt")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(WORD)
            os.chmod(path, 0o644)
            written = True
            break
        except OSError:
            continue
    if not written:
        raise OSError("could not write entry.txt to /output or ./output")
    print(WORD)


if __name__ == "__main__":
    main()
