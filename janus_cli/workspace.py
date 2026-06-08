"""Directory-bound workspace profiles.

A project can pin which Janus profile to use when running inside it, via a
``.janus/workspace.yaml`` file holding a ``profile:`` key. Inspired by
OpenClaw's per-workspace agents: ``cd`` into a project and you get that
project's persona, memory, and config — no global ``-p`` flag needed.

Resolution precedence (see janus_cli/main.py ``_apply_profile_override``):
    explicit -p flag  >  profile-specific JANUS_HOME  >  workspace binding
    >  global active_profile  >  default.

Every function here is defensive and never raises — ``find_workspace_profile``
runs at startup before module imports, so a bad binding must fall back to the
default rather than crash the CLI.
"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

WORKSPACE_REL_PATH = Path(".janus") / "workspace.yaml"


def binding_path(directory: Path) -> Path:
    """Path to the workspace binding file for ``directory``."""
    return Path(directory) / WORKSPACE_REL_PATH


def read_binding(directory: Path) -> Optional[str]:
    """Return the profile name bound in ``directory``'s workspace.yaml, or None."""
    path = binding_path(directory)
    if not path.is_file():
        return None
    try:
        import yaml

        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception:
        return None
    prof = data.get("profile") if isinstance(data, dict) else None
    return prof.strip() if isinstance(prof, str) and prof.strip() else None


def find_workspace_profile(
    start_dir: Optional[Path] = None, *, validate: bool = True
) -> Optional[str]:
    """Walk up from ``start_dir`` (default cwd) for a workspace profile binding.

    Returns the nearest bound profile name. When ``validate`` is True the name
    must be a syntactically valid, *existing* profile — otherwise None is
    returned so resolution falls back to the global default. Never raises.
    """
    try:
        directory = Path(start_dir or Path.cwd()).resolve()
    except Exception:
        return None
    try:
        for d in (directory, *directory.parents):
            name = read_binding(d)
            if not name:
                continue
            if not validate:
                return name
            try:
                from janus_cli.profiles import _PROFILE_ID_RE, profile_exists

                if _PROFILE_ID_RE.match(name) and profile_exists(name):
                    return name
            except Exception:
                return None
            # Nearest binding wins; if it's broken, fall back (don't keep walking).
            return None
    except Exception:
        return None
    return None


def set_binding(directory: Path, profile: str) -> Path:
    """Pin ``profile`` for ``directory``. Returns the written file path."""
    import yaml

    path = binding_path(directory)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump({"profile": profile}, default_flow_style=False, sort_keys=False),
        encoding="utf-8",
    )
    return path


def clear_binding(directory: Path) -> bool:
    """Remove ``directory``'s workspace binding. Returns True if one existed."""
    path = binding_path(directory)
    if path.is_file():
        try:
            path.unlink()
            return True
        except OSError:
            return False
    return False
