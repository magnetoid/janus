"""Resolve JANUS_HOME for standalone skill scripts.

Skill scripts may run outside the Janus process (e.g. system Python,
nix env, CI) where ``janus_constants`` is not importable.  This module
provides the same ``get_janus_home()`` and ``display_janus_home()``
contracts as ``janus_constants`` without requiring it on ``sys.path``.

When ``janus_constants`` IS available it is used directly so that any
future enhancements (profile resolution, Docker detection, etc.) are
picked up automatically.  The fallback path replicates the core logic
from ``janus_constants.py`` using only the stdlib.

All scripts under ``google-workspace/scripts/`` should import from here
instead of duplicating the ``JANUS_HOME = Path(os.getenv(...))`` pattern.
"""

from __future__ import annotations

import os
from pathlib import Path

try:
    from janus_constants import display_janus_home as display_janus_home
    from janus_constants import get_janus_home as get_janus_home
except (ModuleNotFoundError, ImportError):

    def get_janus_home() -> Path:
        """Return the Janus home directory (default: ~/.janus).

        Mirrors ``janus_constants.get_janus_home()``."""
        val = os.environ.get("JANUS_HOME", "").strip()
        return Path(val) if val else Path.home() / ".janus"

    def display_janus_home() -> str:
        """Return a user-friendly ``~/``-shortened display string.

        Mirrors ``janus_constants.display_janus_home()``."""
        home = get_janus_home()
        try:
            return "~/" + str(home.relative_to(Path.home()))
        except ValueError:
            return str(home)
