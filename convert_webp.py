#!/usr/bin/env python3
"""Convert WebP files to PNG or PDF."""

import sys
import argparse
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Pillow is required. Install it with: pip install Pillow")
    sys.exit(1)


def convert_webp(input_path: Path, output_format: str, output_dir: Path | None = None) -> Path:
    dest_dir = output_dir or input_path.parent
    output_path = dest_dir / input_path.with_suffix(f".{output_format.lower()}").name

    with Image.open(input_path) as img:
        if output_format.upper() == "PDF":
            img.convert("RGB").save(output_path, "PDF")
        else:
            img.save(output_path, "PNG")

    return output_path


def main():
    parser = argparse.ArgumentParser(description="Convert WebP files to PNG or PDF")
    parser.add_argument("input", nargs="+", help="WebP file(s) or directory")
    parser.add_argument(
        "-f", "--format", choices=["png", "pdf"], default="png",
        help="Output format (default: png)"
    )
    parser.add_argument("-o", "--output-dir", help="Output directory (default: same as input)")
    args = parser.parse_args()

    output_dir = Path(args.output_dir) if args.output_dir else None
    if output_dir:
        output_dir.mkdir(parents=True, exist_ok=True)

    files: list[Path] = []
    for item in args.input:
        p = Path(item)
        if p.is_dir():
            files.extend(p.glob("*.webp"))
        elif p.suffix.lower() == ".webp" and p.is_file():
            files.append(p)
        else:
            print(f"Skipping {p} (not a .webp file or directory)")

    if not files:
        print("No WebP files found.")
        sys.exit(1)

    for webp in files:
        try:
            out = convert_webp(webp, args.format, output_dir)
            print(f"Converted: {webp} -> {out}")
        except Exception as e:
            print(f"Failed: {webp}: {e}")


if __name__ == "__main__":
    main()
