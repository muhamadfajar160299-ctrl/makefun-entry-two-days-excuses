"""Copy the one-line excuse in entry.txt byte-identically to the
grader output directory, with mode 0644 and no temporary files."""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.txt")

try:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
except KeyError:
    print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
    raise SystemExit(1)

OUT = os.path.join(out_dir, "entry.txt")

try:
    with open(SRC, "rb") as f:
        data = f.read()
except OSError as exc:
    print(f"cannot read {SRC}: {exc}", file=sys.stderr)
    raise SystemExit(1)

if not data.strip():
    print("entry.txt is empty or only whitespace", file=sys.stderr)
    raise SystemExit(1)

os.makedirs(out_dir, exist_ok=True)
with open(OUT, "wb") as f:
    f.write(data)
os.chmod(OUT, 0o644)
