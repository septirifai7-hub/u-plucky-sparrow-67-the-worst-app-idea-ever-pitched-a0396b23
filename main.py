#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched - make.fun bounty entry.

Writes a one-sentence pitch for the worst, most useless app imaginable
(Fernly, an on-demand Plant Whisperer for houseplants) to
/output/entry.txt (the file the make.fun harness grades).
"""

import os

ENTRY = "Fernly: an on-demand app that dispatches a certified Plant Whisperer to your home within the hour to encourage your fern, water it with small-batch artisanal rain, and text you a photo of it thriving \u2014 $49 a visit, fern not included."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
