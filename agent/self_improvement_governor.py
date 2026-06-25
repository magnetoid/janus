"""Graduated-trust governor for the self-improvement loop.

The continual-learning metrics in ``outcome_tracker.learning_metrics()`` already
detect when the agent is degrading — forgetting, and a skill-diversity drop that
is the classic model-collapse early warning. Until now nothing *consumed* those
signals. This module is that missing consumer: a circuit-breaker that the
autonomous-admission paths (verifiable skill auto-promotion, and later mining
admission) check before changing the agent.

States:
  OK      — healthy; autonomous promotion runs at normal thresholds.
  CAUTION — mild decline; promotion runs but with tightened thresholds.
  FROZEN  — collapse / forgetting warning; autonomous promotion is paused.

Design contract (deliberately asymmetric):
  * **FROZEN on bad signals.** A health warning should pause self-modification —
    the safe direction is "don't change the agent while it's degrading."
  * **Fail-OPEN on exceptions.** A *crash* inside the governor must never block
    the agent; an internal error returns OK. (Uncertainty about health → pause;
    a broken governor → get out of the way.)

Everything here runs post-session / offline (sleep cron, CLI inspect) and reads
only ``outcomes.json`` — it never touches the live conversation or prompt cache.
Thresholds are imported from ``outcome_tracker`` so the warning logic and the
governor can never drift.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional

from agent.outcome_tracker import (
    DIVERSITY_TREND_WARN,
    FORGETTING_WARN,
    FORWARD_TRANSFER_WARN,
    INSUFFICIENT_DATA_SESSIONS,
)

logger = logging.getLogger(__name__)

STATE_OK = "ok"
STATE_CAUTION = "caution"
STATE_FROZEN = "frozen"

_DEFAULTS = {
    "enabled": False,
    "auto_promote": False,
    "caution_ratio": 0.6,
    "caution_extra_uses": 2,
    "caution_success_floor": 0.85,
}


def _gov_cfg(key: str, default: Any) -> Any:
    """Read a ``learning.governor.<key>`` value, best-effort."""
    try:
        from janus_cli.config import read_raw_config

        gov = (read_raw_config().get("learning") or {}).get("governor") or {}
        if isinstance(gov, dict) and key in gov and gov[key] is not None:
            return gov[key]
    except Exception:
        logger.debug("governor config read failed for %r", key, exc_info=True)
    return default


def governor_enabled() -> bool:
    return bool(_gov_cfg("enabled", _DEFAULTS["enabled"]))


def auto_promote_enabled() -> bool:
    """The write action (verifiable auto-promotion) is a separate opt-in."""
    return bool(_gov_cfg("auto_promote", _DEFAULTS["auto_promote"]))


def assess_admission_state(metrics: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Classify the learning loop's health into OK / CAUTION / FROZEN.

    ``metrics`` is injectable for tests; otherwise it is pulled from
    ``outcome_tracker.learning_metrics()``. Never raises — on any internal
    error it fails open to OK.
    """
    try:
        if not governor_enabled():
            return {"state": STATE_OK, "reasons": ["governor disabled"], "metrics": metrics or {}}

        if metrics is None:
            from agent.outcome_tracker import learning_metrics

            metrics = learning_metrics()
        metrics = metrics or {}

        sessions = metrics.get("sessions")
        if not isinstance(sessions, (int, float)) or sessions < INSUFFICIENT_DATA_SESSIONS:
            return {
                "state": STATE_OK,
                "reasons": [f"insufficient data ({sessions} sessions)"],
                "metrics": metrics,
            }

        fgt = metrics.get("forgetting")
        dtrend = metrics.get("diversity_trend")
        fwt = metrics.get("forward_transfer")
        ratio = float(_gov_cfg("caution_ratio", _DEFAULTS["caution_ratio"]))

        reasons: List[str] = []

        # FROZEN: collapse / forgetting warnings — the same conditions that
        # populate learning_metrics()["warnings"].
        if isinstance(fgt, (int, float)) and fgt > FORGETTING_WARN:
            reasons.append(f"forgetting {fgt:.2f} > {FORGETTING_WARN} — skills regressing")
        if isinstance(dtrend, (int, float)) and dtrend < DIVERSITY_TREND_WARN:
            reasons.append(
                f"diversity trend {dtrend:.2f} < {DIVERSITY_TREND_WARN} — possible model collapse"
            )
        if reasons:
            return {"state": STATE_FROZEN, "reasons": reasons, "metrics": metrics}

        # CAUTION: milder decline, or a soft band approaching the freeze line.
        if isinstance(fwt, (int, float)) and fwt < FORWARD_TRANSFER_WARN:
            reasons.append(f"forward transfer {fwt:.2f} < {FORWARD_TRANSFER_WARN} — success declining")
        if isinstance(fgt, (int, float)) and fgt > FORGETTING_WARN * ratio:
            reasons.append(f"forgetting {fgt:.2f} approaching freeze threshold")
        if isinstance(dtrend, (int, float)) and dtrend < DIVERSITY_TREND_WARN * ratio:
            reasons.append(f"diversity trend {dtrend:.2f} approaching freeze threshold")
        if reasons:
            return {"state": STATE_CAUTION, "reasons": reasons, "metrics": metrics}

        return {"state": STATE_OK, "reasons": ["learning loop healthy"], "metrics": metrics}
    except Exception:
        logger.debug("governor assessment failed — failing open to OK", exc_info=True)
        return {"state": STATE_OK, "reasons": ["governor error — failing open"], "metrics": metrics or {}}


def admission_allowed(metrics: Optional[Dict[str, Any]] = None) -> bool:
    """True unless the governor is FROZEN. Autonomous admission gates on this."""
    return assess_admission_state(metrics).get("state") != STATE_FROZEN


def promotion_thresholds(metrics: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
    """Threshold overrides for verifiable promotion, scaled to the current state.

    Returns ``None`` when FROZEN (caller must not promote). On OK returns an
    empty dict (use the ``graph.*`` config defaults). On CAUTION returns
    tightened ``min_uses`` / ``promo_thr`` the caller passes into
    ``skill_graph.assess_promotability``.
    """
    state = assess_admission_state(metrics).get("state")
    if state == STATE_FROZEN:
        return None
    if state != STATE_CAUTION:
        return {}

    try:
        from agent.skill_graph import _graph_cfg

        base_uses = int(_graph_cfg("min_uses_for_promotion", 3))
        base_thr = float(_graph_cfg("promotion_success_threshold", 0.75))
    except Exception:
        base_uses, base_thr = 3, 0.75

    extra = int(_gov_cfg("caution_extra_uses", _DEFAULTS["caution_extra_uses"]))
    floor = float(_gov_cfg("caution_success_floor", _DEFAULTS["caution_success_floor"]))
    return {
        "min_uses": base_uses + extra,
        "promo_thr": max(base_thr, floor),
    }
