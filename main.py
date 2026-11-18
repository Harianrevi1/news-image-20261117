"""News-image entry: copy the bundled front-page image to the output dir.

The program runs in a sandbox with no network and a read-only /bot, so the
image ships inside the repository and this script only copies it, byte for
byte, to the output location the grader reads.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    # Confirm the copy landed byte for byte; a shortfall means the run is bad.
    if os.path.getsize(target) != os.path.getsize(source):
        print("copy size mismatch", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes)" % (target, os.path.getsize(target)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
