"""Guided first-run opt-in for the read-only learning loop (Phase 2.4).

Every learning flag ships OFF. Rather than silently flip defaults — which would
add per-session aux cost and change behavior on upgrade for every existing user —
we OFFER the read-only loop exactly once, interactively, on an already-configured
install, and remember the answer so we never nag again.

Only the READ-ONLY, no-autonomous-write flags are ever touched here:
outcome tracking, the eval-trend curve, and the health governor's assessment.
Write-side / autonomous features — governor.auto_promote, playbook, dialectic,
self_improve, the proposer, and twin-core review — are NEVER enabled by this
path; they stay individually opt-in behind their own switches and a human.
"""
from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import Any, Callable, Dict, Optional

logger = logging.getLogger(__name__)

# The curated read-only bundle. Each is pure-local or observability-only; none
# performs an autonomous write to a learned artifact.
_READONLY_PRESET = (
    ("learning.track_outcomes", "outcome tracking + reflexion lessons"),
    ("evals.trend.enabled", "longitudinal eval pass-rate curve"),
    ("learning.governor.enabled", "self-improvement health assessment"),
)


def _stamp_path() -> Path:
    from janus_constants import get_janus_home
    return get_janus_home() / "learning" / ".optin_prompted"


def _already_prompted() -> bool:
    try:
        return _stamp_path().exists()
    except Exception:
        return True  # can't tell → treat as prompted (never nag)


def _mark_prompted() -> None:
    try:
        p = _stamp_path()
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("1\n", encoding="utf-8")
    except Exception as exc:
        logger.debug("could not write learning opt-in stamp: %s", exc)


def _readonly_already_on(config: Optional[Dict[str, Any]] = None) -> bool:
    """True if the user already turned on ANY read-only flag — then don't offer."""
    try:
        if config is None:
            from janus_cli.config import load_config
            config = load_config()
        learning = config.get("learning") or {}
        if learning.get("track_outcomes"):
            return True
        if (learning.get("governor") or {}).get("enabled"):
            return True
        if ((config.get("evals") or {}).get("trend") or {}).get("enabled"):
            return True
        return False
    except Exception:
        return True  # fail safe: unknown → don't offer


def _is_interactive() -> bool:
    try:
        return bool(sys.stdin.isatty() and sys.stdout.isatty())
    except Exception:
        return False


def should_offer() -> bool:
    """Only on an interactive, unmanaged, not-yet-prompted, not-already-on CLI."""
    try:
        if not _is_interactive():
            return False
        from janus_cli.config import is_managed
        if is_managed():
            return False
        if _already_prompted():
            return False
        if _readonly_already_on():
            return False
        return True
    except Exception:
        return False


def offer(*, input_fn: Callable[[str], str] = input) -> Optional[bool]:
    """Prompt once to enable the read-only learning loop.

    Returns True if enabled, False if declined, None if skipped (non-interactive,
    managed, already prompted, or already on). ALWAYS stamps once it decides to
    ask, so the prompt appears exactly once whatever the user answers."""
    if not should_offer():
        return None
    _mark_prompted()  # one prompt, ever — regardless of the answer below
    print()
    print("  ⚕ Janus can learn from how your sessions go — a READ-ONLY loop:")
    for _, what in _READONLY_PRESET:
        print(f"      · {what}")
    print("    It only records and measures — no autonomous changes. "
          "~1 auxiliary-model call per session.")
    try:
        reply = str(input_fn("  Enable the read-only learning loop? [y/N] ")).strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        return False
    if reply not in {"y", "yes"}:
        print("  Left off. Enable later anytime with: janus learning enable\n")
        return False
    try:
        from janus_cli.config import set_config_value
        for key, _ in _READONLY_PRESET:
            set_config_value(key, "true")
    except Exception as exc:
        logger.debug("failed to enable learning preset: %s", exc)
        print("  ⚠ Could not update config; enable later with: janus learning enable\n")
        return False
    print("  ✓ Read-only learning loop is ON (applies to new sessions).")
    print("    Turn it off anytime with: janus learning disable\n")
    return True
