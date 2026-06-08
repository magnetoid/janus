#!/usr/bin/env python3
"""Imba Labs / Janus rebrand sweep.

Case-preserving rename of brand/identity tokens, with real external
products/services PROTECTED (model IDs, provider slug, Nous Portal, domains,
GitHub org). Set DRY=1 to report without writing.

  Nous Research -> Imba Labs   (company)
  Hermes / Hermes Agent -> Janus   (agent)
"""
import os
import re
import sys
from pathlib import Path

ROOT = Path(".").resolve()
DRY = os.environ.get("DRY") == "1"

EXCLUDE_DIRS = {
    ".git", ".torsor", "node_modules", ".venv", "venv", "__pycache__",
    ".pytest_cache", ".mypy_cache", ".ruff_cache", "dist", "build", ".idea",
    ".egg-info",
}
EXCLUDE_FILES = {"uv.lock", "package-lock.json", "rebrand_janus.py"}
BINARY_EXT = {
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".icns", ".pdf", ".woff", ".woff2",
    ".ttf", ".otf", ".zip", ".gz", ".tar", ".so", ".dylib", ".bin", ".lock",
    ".webp", ".mp4", ".mp3", ".wav", ".pyc",
}
MAX_BYTES = 6_000_000

# --- PROTECT: real products/services, must survive verbatim ----------------
PROTECT = [
    re.compile(r"(?i)nous[- ]?hermes[\w./-]*"),          # nous-hermes model family
    re.compile(r"(?i)\bhermes[-_ ]?\d[\w.]*"),           # hermes-3, hermes_4, "Hermes 4", hermes-3-405b
    re.compile(r"FP16_Hermes_[\w.]*"),                   # fine-tune naming in tests
    re.compile(r"gl-python/hermes"),                     # genai lib user-agent
    re.compile(r"(?i)nous\s+portal"),                    # Nous Portal product name
    re.compile(r"[\w.-]*nousresearch\.com[\w./-]*"),     # domains incl subdomains+paths
    re.compile(r"NousResearch/[\w.-]+"),                 # github org path (real repo)
]

# --- REPLACE: company brand first, then agent brand (case-preserving) -------
COMPANY = [
    ("NOUS RESEARCH", "IMBA LABS"),
    ("Nous Research", "Imba Labs"),
    ("Nous research", "Imba Labs"),
    ("nous research", "imba labs"),
]
AGENT = [
    ("HERMES", "JANUS"),
    ("Hermes", "Janus"),
    ("hermes", "janus"),
]

SENTINEL = "\x00\x01{}\x02\x00"


def transform(text: str) -> str:
    stash = []

    def _mask(m):
        stash.append(m.group(0))
        return SENTINEL.format(len(stash) - 1)

    for pat in PROTECT:
        text = pat.sub(_mask, text)
    for a, b in COMPANY:
        text = text.replace(a, b)
    for a, b in AGENT:
        text = text.replace(a, b)
    for i, original in enumerate(stash):
        text = text.replace(SENTINEL.format(i), original)
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


def rename_path_component(name: str) -> str:
    # Only infra/brand path tokens; no model IDs live in paths.
    out = name
    for a, b in AGENT:
        out = out.replace(a, b)
    return out


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

    # File/dir renames (deepest first), paths containing 'hermes'
    renames = []
    for dirpath, dirnames, filenames in os.walk(ROOT, topdown=False):
        parts = set(Path(dirpath).relative_to(ROOT).parts)
        if parts & EXCLUDE_DIRS:
            continue
        for name in filenames + dirnames:
            if "hermes" in name.lower():
                src = Path(dirpath) / name
                dst = Path(dirpath) / rename_path_component(name)
                if src != dst:
                    renames.append((str(src.relative_to(ROOT)), str(dst.relative_to(ROOT))))
                    if not DRY:
                        src.rename(dst)

    print(f"{'DRY-RUN: ' if DRY else ''}content files changed: {content_changed}")
    print(f"{'DRY-RUN: ' if DRY else ''}paths renamed: {len(renames)}")
    print("\n-- sample content files (first 15) --")
    for f in repl_files[:15]:
        print("  ", f)
    print("\n-- path renames --")
    for s, d in renames:
        print(f"   {s}  ->  {d}")


if __name__ == "__main__":
    main()
