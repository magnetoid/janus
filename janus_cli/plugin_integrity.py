"""Integrity pinning for user-installed plugins.

Supply-chain guard for ``~/.janus/plugins/`` (and project ``.janus/plugins/``):
the first time a plugin is loaded its content digest is recorded; on later
loads the digest is re-verified. A plugin whose code changed on disk without
the user's knowledge — a compromised update, a tampered checkout — is the
canonical agent supply-chain attack, and plugins run with full process
privileges the moment they're imported.

Modes (``security.plugin_integrity`` in config.yaml):

- ``warn`` (default): log a prominent warning on change, then re-pin so the
  warning fires once per change. Loading proceeds.
- ``block``: refuse to load a changed plugin until the user re-trusts it
  with ``janus plugins trust <name>``.
- ``off``: skip verification entirely.

Bundled plugins (shipped in the repo) and pip entry-point plugins (managed
by pip's own integrity machinery) are not pinned — only directory plugins
the user dropped in.

Pins live in ``$JANUS_HOME/plugins/.integrity.json``.
"""

from __future__ import annotations

import hashlib
import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Optional, Tuple

from janus_constants import get_janus_home

logger = logging.getLogger(__name__)

# File types that constitute the plugin's executable/config surface.
_HASHED_SUFFIXES = frozenset({
    ".py", ".yaml", ".yml", ".json", ".toml", ".sh", ".js", ".ts", ".cfg", ".ini",
})
_SKIP_DIRS = frozenset({"__pycache__", ".git", ".venv", "node_modules", ".mypy_cache"})

MODE_WARN = "warn"
MODE_BLOCK = "block"
MODE_OFF = "off"


def _pins_path() -> Path:
    return get_janus_home() / "plugins" / ".integrity.json"


def get_integrity_mode() -> str:
    """Read ``security.plugin_integrity`` from config (default: warn)."""
    try:
        from janus_cli.config import read_raw_config
        sec = read_raw_config().get("security", {})
        mode = str(sec.get("plugin_integrity", MODE_WARN)).strip().lower()
        if mode in {MODE_WARN, MODE_BLOCK, MODE_OFF}:
            return mode
        logger.warning(
            "security.plugin_integrity: unknown mode %r — using 'warn'", mode
        )
    except Exception:
        pass
    return MODE_WARN


def compute_plugin_digest(plugin_dir: Path) -> str:
    """SHA-256 digest over the plugin's code and config files.

    Deterministic: files are walked in sorted relative-path order and both
    the path and content feed the hash, so renames count as changes.
    """
    digest = hashlib.sha256()
    plugin_dir = Path(plugin_dir)
    files = sorted(
        p for p in plugin_dir.rglob("*")
        if p.is_file()
        and p.suffix.lower() in _HASHED_SUFFIXES
        and not any(part in _SKIP_DIRS for part in p.relative_to(plugin_dir).parts)
    )
    for f in files:
        rel = f.relative_to(plugin_dir).as_posix()
        digest.update(rel.encode("utf-8"))
        digest.update(b"\0")
        try:
            digest.update(f.read_bytes())
        except OSError:
            digest.update(b"<unreadable>")
        digest.update(b"\0")
    return digest.hexdigest()


def _load_pins() -> Dict[str, Dict[str, str]]:
    path = _pins_path()
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (OSError, json.JSONDecodeError) as exc:
        logger.warning("plugin integrity pins unreadable (%s) — treating as empty", exc)
        return {}


def _save_pins(pins: Dict[str, Dict[str, str]]) -> None:
    path = _pins_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(pins, indent=2, sort_keys=True), encoding="utf-8")


def pin_plugin(key: str, plugin_dir: Path) -> str:
    """Record (or update) the digest pin for *key*. Returns the digest."""
    digest = compute_plugin_digest(plugin_dir)
    pins = _load_pins()
    pins[key] = {
        "digest": digest,
        "pinned_at": datetime.now(timezone.utc).isoformat(),
    }
    _save_pins(pins)
    return digest


def unpin_plugin(key: str) -> None:
    """Drop the pin for *key* (e.g. after the plugin is removed)."""
    pins = _load_pins()
    if key in pins:
        del pins[key]
        _save_pins(pins)


def check_before_load(key: str, plugin_dir: Path) -> Tuple[bool, Optional[str]]:
    """Verify a user/project plugin before it is imported.

    Returns ``(allowed, message)``. ``message`` is non-None when something
    noteworthy happened (changed in warn mode, blocked in block mode).
    Verification failures fail open in warn mode — integrity must not turn
    an IO hiccup into a broken plugin ecosystem.
    """
    mode = get_integrity_mode()
    if mode == MODE_OFF:
        return True, None

    try:
        current = compute_plugin_digest(plugin_dir)
        pins = _load_pins()
        pinned = (pins.get(key) or {}).get("digest")

        if pinned is None:
            pin_plugin(key, plugin_dir)
            logger.debug("plugin '%s': integrity pin recorded", key)
            return True, None

        if pinned == current:
            return True, None

        if mode == MODE_BLOCK:
            msg = (
                f"plugin '{key}' changed on disk since it was trusted — "
                f"blocked by security.plugin_integrity: block. Review the "
                f"changes, then re-trust with `janus plugins trust {key}`."
            )
            logger.warning(msg)
            return False, msg

        # warn mode: surface loudly, re-pin so the warning fires once per change
        msg = (
            f"plugin '{key}' changed on disk since it was last loaded "
            f"(re-pinned). If you didn't update this plugin, inspect it: "
            f"{plugin_dir}"
        )
        logger.warning(msg)
        pin_plugin(key, plugin_dir)
        return True, msg
    except Exception as exc:
        logger.warning("plugin '%s': integrity check failed (%s) — allowing", key, exc)
        return True, None
