#!/usr/bin/env python3
"""Convert HEIC files to JPG."""

import sys
import glob
from pathlib import Path
from pillow_heif import register_heif_opener
from PIL import Image

register_heif_opener()


def convert(paths, quality=95):
    for p in paths:
        img = Image.open(p)
        out = str(Path(p).with_suffix(".jpg"))
        img.convert("RGB").save(out, "JPEG", quality=quality)
        print(f"Converted: {out}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: heic2jpg.py <file.heic ...>")
        print("       heic2jpg.py *.heic")
        sys.exit(1)

    # Expand any glob patterns (useful on Windows where shell doesn't expand)
    files = []
    for arg in sys.argv[1:]:
        expanded = glob.glob(arg)
        files.extend(expanded if expanded else [arg])

    convert(files)
