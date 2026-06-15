#!/usr/bin/env python3
"""Imba Labs -> Cloud Industry rebrand sweep (ADR 0004).

Retires the interim company brand 'Imba Labs' in favour of 'Cloud Industry'.
'Imba' was an invented placeholder with NO real-product overlaps, so unlike the
Hermes/Nous sweep this needs no protect-list — only careful token ordering.

Token rules (applied most-specific first):
  imbalabs.com / imbamarketing.com  -> cloud-industry.com   (domains + emails)
  Imba Labs / IMBA LABS / imba labs  -> Cloud Industry ...   (display brand)
  ImbaLabs                           -> CloudIndustry        (CamelCase ids)
  imba-labs                          -> cloud-industry       (hyphen slug)
  imbalabs                           -> cloudindustry         (identifier/package
                                        slug — NO hyphen, since reverse-DNS /
                                        Python / package names forbid hyphens)

Set DRY=1 to report without writing.
"""
import os
import sys
from pathlib import Path

ROOT = Path(".").resolve()
DRY = os.environ.get("DRY") == "1"

EXCLUDE_DIRS = {
    ".git", ".torsor", "node_modules", ".venv", "venv", "__pycache__",
    ".pytest_cache", ".mypy_cache", ".ruff_cache", "dist", "build", ".idea",
    ".egg-info", "web_dist", "pytest-of-magnetoid",
}
EXCLUDE_FILES = {"uv.lock", "package-lock.json", "rebrand_janus.py",
                 "rebrand_cloud_industry.py"}
BINARY_EXT = {
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".icns", ".pdf", ".woff", ".woff2",
    ".ttf", ".otf", ".zip", ".gz", ".tar", ".so", ".dylib", ".bin", ".lock",
    ".webp", ".mp4", ".mp3", ".wav", ".pyc",
}
MAX_BYTES = 6_000_000

# Ordered most-specific -> least so domains are consumed before the bare slug.
REPLACEMENTS = [
    ("imbalabs.com", "cloud-industry.com"),
    ("imbamarketing.com", "cloud-industry.com"),
    ("IMBA LABS", "CLOUD INDUSTRY"),
    ("Imba Labs", "Cloud Industry"),
    ("Imba labs", "Cloud Industry"),
    ("imba labs", "cloud industry"),
    ("Imba-Labs", "Cloud-Industry"),
    ("imba-labs", "cloud-industry"),
    ("ImbaLabs", "CloudIndustry"),
    ("IMBALABS", "CLOUDINDUSTRY"),
    ("imbalabs", "cloudindustry"),
]


def transform(text: str) -> str:
    for a, b in REPLACEMENTS:
        text = text.replace(a, b)
    return text


def iter_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS and not d.endswith(".egg-info")]
        for fn in filenames:
            if fn in EXCLUDE_FILES:
                continue
            p = Path(dirpath) / fn
            if p.suffix.lower() in BINARY_EXT:
                continue
            yield p


def main():
    content_changed = 0
    repl_files = []
    for p in iter_files():
        try:
            if p.stat().st_size > MAX_BYTES:
                continue
            raw = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        new = transform(raw)
        if new != raw:
            content_changed += 1
            repl_files.append(str(p.relative_to(ROOT)))
            if not DRY:
                p.write_text(new, encoding="utf-8")

    print(f"{'DRY-RUN: ' if DRY else ''}content files changed: {content_changed}")
    print("\n-- content files --")
    for f in repl_files:
        print("  ", f)


if __name__ == "__main__":
    main()
