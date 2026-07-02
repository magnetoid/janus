"""The safety floor for unattended operation (move 3).

One choke point every autonomous entry point (cron tick, kanban worker spawn,
delegate_task fan-out) consults BEFORE it spends money or runs a tool on its
own: ``blocked_reason()``. It combines two independent controls —

  1. a master FREEZE (kill switch) — a human (or the governor) can halt all
     autonomous action instantly, independent of config reloads, via a sentinel
     file under $JANUS_HOME or ``autonomy.frozen`` in config; and
  2. rolling USD spend caps (agent/cost_ledger) that bound cross-session
     fan-out — the failure mode the per-session ceiling can't see.

Detection-based prompt-injection defenses are provably evadable, so the credible
controls for a self-improving agent are structural: a kill switch and budgets
that live OUTSIDE the agent's own decision loop.

Honest scope (what this does NOT do):
  - It gates NEW autonomous work (cron ticks, kanban/delegate spawns). Work
    already IN FLIGHT when the freeze/cap engaged runs to completion, bounded
    only by the per-session ceiling (B-PR2) — so a rolling cap can be overshot
    by in-flight work.
  - Spend caps sum the cost ledger, which records $0 for models the pricing
    layer can't price; real spend on an un-priced model does NOT accrue toward
    a cap. Caps bound PRICED spend.
  - ``blocked_reason`` fails OPEN on any internal error (returns None) so a
    guard bug can't wedge the whole system. The SENTINEL FILE is therefore the
    reliable global kill switch: it survives a corrupt/unreadable config, which
    would otherwise fail-open both the ``autonomy.frozen`` flag and the caps.
Pure, best-effort, never raises.
"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

_FREEZE_SENTINEL = "AUTONOMY_FROZEN"


def _sentinel_path() -> Path:
    from janus_constants import get_janus_home
    return get_janus_home() / _FREEZE_SENTINEL


def frozen(config: Optional[Dict[str, Any]] = None) -> bool:
    """True when autonomous operation is halted — by the sentinel file OR by
    ``autonomy.frozen`` in config. The file wins so a freeze survives a config
    reload and can be flipped without editing YAML."""
    try:
        if _sentinel_path().exists():
            return True
        if config is None:
            from janus_cli.config import load_config
            config = load_config()
        auto = (config.get("autonomy", {}) or {}) if isinstance(config, dict) else {}
        return bool(auto.get("frozen", False))
    except Exception:
        return False


def freeze(reason: str = "") -> bool:
    """Engage the kill switch (write the sentinel). Best-effort; returns success."""
    try:
        p = _sentinel_path()
        p.parent.mkdir(parents=True, exist_ok=True)
        from agent.cost_ledger import _now_iso
        p.write_text(f"{_now_iso()}\n{reason}\n", encoding="utf-8")
        return True
    except Exception as exc:
        logger.debug("autonomy freeze failed: %s", exc)
        return False


def unfreeze() -> bool:
    """Release the kill switch (remove the sentinel). Note: does NOT clear
    ``autonomy.frozen`` in config — that must be edited separately, by design,
    so a config-level freeze can't be lifted by an automated unfreeze."""
    try:
        p = _sentinel_path()
        if p.exists():
            p.unlink()
        return True
    except Exception as exc:
        logger.debug("autonomy unfreeze failed: %s", exc)
        return False


def freeze_reason_text() -> str:
    """The recorded reason from the sentinel file, or "" if none/unavailable."""
    try:
        p = _sentinel_path()
        if not p.exists():
            return ""
        lines = p.read_text(encoding="utf-8").splitlines()
        return (lines[1].strip() if len(lines) > 1 else "").strip()
    except Exception:
        return ""


def blocked_reason(config: Optional[Dict[str, Any]] = None, *,
                   now_ts: Optional[float] = None) -> Optional[str]:
    """The single guard autonomous entry points call. Returns a human-readable
    reason to REFUSE (freeze engaged, or a rolling spend cap hit), else None.

    Best-effort: returns None (allow) on internal error — a guard failure must
    not itself halt operation, and blocking is only ever an explicit signal.
    """
    try:
        if frozen(config):
            rt = freeze_reason_text()
            return "autonomy is frozen (kill switch engaged)" + (f": {rt}" if rt else "")
        from agent.cost_ledger import spend_cap_exceeded
        cap = spend_cap_exceeded(config, now_ts=now_ts)
        if cap:
            return cap
        return None
    except Exception:
        return None
