"""Migrate a legacy Hermes Agent install (~/.hermes) into Janus (~/.janus).

Janus was rebranded from 'Hermes Agent'; the on-disk layout is IDENTICAL
(config.yaml, .env, memories/, skills/, sessions/, learning/, state DB, …), so
this is a safe directory COPY — not a format translation — plus a targeted
rewrite of two brand tokens inside config.yaml/.env: ``HERMES_HOME`` ->
``JANUS_HOME`` and filesystem paths ``.hermes`` -> ``.janus``.

It deliberately does NOT touch Nous 'Hermes' model IDs (hermes-3-*, Hermes-4-*,
nous-hermes-*) or the 'nous' provider slug — those are real products that must
keep working. The rewrite is anchored to ``HERMES_HOME`` and the dot-prefixed
``/.hermes`` path so model IDs (no leading dot, no HOME suffix) are never hit.

Non-destructive: copies into the Janus home and leaves ~/.hermes intact; the
caller may offer to delete it afterward. Best-effort; never raises.
"""
from __future__ import annotations

import logging
import os
import shutil
from pathlib import Path
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

# files whose CONTENTS get the brand-token rewrite (paths/env vars only)
_REWRITE_FILES = ("config.yaml", ".env")
# markers that a directory really is a Hermes/Janus home (avoid migrating junk)
_HOME_MARKERS = ("config.yaml", ".env", "memories", "skills", "sessions", "state.db")


def default_legacy_dir() -> Optional[Path]:
    r"""The legacy Hermes home: ``$HERMES_HOME``, else ``~/.hermes`` (or
    ``%LOCALAPPDATA%\hermes`` on Windows)."""
    env = os.environ.get("HERMES_HOME")
    if env:
        return Path(env).expanduser()
    if os.name == "nt":
        base = os.environ.get("LOCALAPPDATA")
        if base:
            return Path(base) / "hermes"
    return Path.home() / ".hermes"


def looks_like_home(path: Path) -> bool:
    """True if ``path`` is a directory containing at least one home marker."""
    return path.is_dir() and any((path / m).exists() for m in _HOME_MARKERS)


def legacy_hermes_home() -> Optional[Path]:
    """Return the legacy Hermes home if it exists and looks real, else None."""
    d = default_legacy_dir()
    if d and looks_like_home(d):
        return d
    return None


def _rewrite_brand_tokens(text: str) -> str:
    """Targeted, SAFE rewrite: only the home env var + the .hermes config path.

    Anchored so it never matches 'hermes-N' / 'nous-hermes' model IDs (no
    leading dot, no HOME suffix) or the 'nous' provider slug.
    """
    text = text.replace("HERMES_HOME", "JANUS_HOME")
    text = text.replace("/.hermes", "/.janus")    # POSIX config-dir paths
    text = text.replace("\\.hermes", "\\.janus")  # Windows config-dir paths
    return text


def plan_migration(src: Path, dst: Path) -> Dict[str, Any]:
    """Dry-run preview: classify each top-level entry in ``src`` as import or conflict."""
    result: Dict[str, Any] = {"src": str(src), "dst": str(dst), "import": [], "conflict": []}
    if not src.is_dir():
        return result
    for entry in sorted(src.iterdir(), key=lambda p: p.name):
        target = dst / entry.name
        (result["conflict"] if target.exists() else result["import"]).append(entry.name)
    return result


def migrate(src: Path, dst: Path, *, overwrite: bool = False, apply: bool = True) -> Dict[str, Any]:
    """Copy top-level entries from ``src`` into ``dst`` (non-destructive on src).

    Conflicts (entries already in ``dst``) are skipped unless ``overwrite``.
    After copying, brand tokens in ``dst/config.yaml`` and ``dst/.env`` are
    rewritten. ``apply=False`` is a dry run that creates nothing. Best-effort;
    never raises. Returns a summary dict.
    """
    result: Dict[str, Any] = {
        "imported": [], "skipped": [], "errors": [], "rewritten": [], "applied": apply,
    }
    try:
        if not src.is_dir():
            result["errors"].append(f"source not found: {src}")
            return result
        if apply:
            dst.mkdir(parents=True, exist_ok=True)
        for entry in sorted(src.iterdir(), key=lambda p: p.name):
            target = dst / entry.name
            if target.exists() and not overwrite:
                result["skipped"].append(entry.name)
                continue
            if not apply:
                result["imported"].append(entry.name)
                continue
            try:
                if entry.is_dir():
                    if target.exists() and overwrite and not target.is_dir():
                        target.unlink()
                    shutil.copytree(entry, target, dirs_exist_ok=True)
                else:
                    shutil.copy2(entry, target)
                result["imported"].append(entry.name)
            except Exception as exc:
                result["errors"].append(f"{entry.name}: {exc}")
        if apply:
            for name in _REWRITE_FILES:
                f = dst / name
                if f.is_file():
                    try:
                        original = f.read_text(encoding="utf-8")
                        rewritten = _rewrite_brand_tokens(original)
                        if rewritten != original:
                            f.write_text(rewritten, encoding="utf-8")
                            result["rewritten"].append(name)
                    except Exception as exc:
                        result["errors"].append(f"rewrite {name}: {exc}")
    except Exception as exc:
        logger.debug("hermes migrate failed: %s", exc)
        result["errors"].append(str(exc))
    return result


def remove_legacy(src: Path) -> bool:
    """Delete the legacy Hermes home after a successful migration. Best-effort."""
    try:
        shutil.rmtree(src)
        return True
    except Exception as exc:
        logger.debug("remove legacy hermes home failed: %s", exc)
        return False
