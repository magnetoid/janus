"""One-time notice shown after the CLI redesign ships.

The redesign changes the default look for everyone; this tells each user —
exactly once — that the old look is one command away. Stamp-file pattern
(same as janus_cli/learning_onboarding.py): decide-to-show writes the stamp,
so the notice can never nag."""
from __future__ import annotations

from pathlib import Path


def _stamp_path() -> Path:
    from janus_constants import get_janus_home
    return get_janus_home() / "skins" / ".redesign-notice-shown"


def maybe_show_redesign_notice(print_fn=print) -> bool:
    """Show the one-time notice when the (new) default skin is active.
    Returns True when shown. Never raises."""
    try:
        from janus_cli.skin_engine import get_active_skin_name
        if get_active_skin_name() != "default":
            return False          # user already chose a skin — nothing to say
        stamp = _stamp_path()
        if stamp.exists():
            return False
        stamp.parent.mkdir(parents=True, exist_ok=True)
        stamp.write_text("1\n", encoding="utf-8")
        from janus_cli.design import note
        print_fn(f"  {note('new look — /skin classic restores the previous one')}")
        return True
    except Exception:
        return False
