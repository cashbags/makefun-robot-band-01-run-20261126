#!/usr/bin/env python3
"""Name the Robot Band — entry program (program/v1).

Writes one funny robot-band name plus a few words on its hit song to
/output/entry.txt. The text is fixed: the humour was chosen by a pairwise
self-judge tournament against the competition's published five criteria
(see DESIGN.md), so the program's job is only to emit that winning line
byte-identically on every run. No input, no network, no randomness.
"""
import os

ENTRY = (
    "The Delivery Bots \u2014 hit single 'Your Order Is 3 Minutes Away' "
    "has been 3 minutes away since Tuesday; the encore went to the "
    "wrong address."
)


def main() -> None:
    # Gate check, mirroring the competition's sealed scorer: the entry
    # must be UTF-8 text of 1 to 200 characters, not only whitespace.
    # Failing loudly here beats shipping an invalid artifact.
    text = ENTRY.encode("utf-8").decode("utf-8")
    if not 1 <= len(text) <= 200 or not text.strip():
        raise SystemExit("entry violates the 1-200 character gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
