"""Implicit-feedback sensor network (move 10).

The delivery surfaces carry a dense signal the learning loop wasn't reading:
every time the user has to INTERVENE — interrupt the agent, /steer it mid-task,
deny an action — is evidence about how the interaction is going. This records
those interventions per session as a saturating FRICTION score in [0, 1].

IMPORTANT — this is an OBSERVABILITY signal, deliberately NOT a reward input.
An adversarial review of the first design (which penalised the reward by
friction) surfaced that this would be actively harmful:
  * The SIGN is unvalidated. A user interrupts/steers to ADD scope or redirect
    to a better idea just as often as because the agent is failing. Penalising
    reward for it teaches the agent to be LESS steerable — to avoid visible,
    interruptible, collaborative work — which is the opposite of what we want.
  * ATTRIBUTION is confounded. Friction is a whole-session scalar; debiting it
    against every skill the session used would demote a clean skill that merely
    co-occurred with an unrelated intervention (the same confounder move 4
    removed for lessons — not to be re-introduced for the reward the skill
    graph trusts for promotion).
So friction is measured and SURFACED to humans (learning_metrics / the
dashboard) as an interaction-health indicator, and the reward that drives
self-modification is left untouched. A human can watch friction rise and
investigate; the agent's own optimisation target is not reshaped by a signal
whose meaning we can't yet establish.

Gated on ``learning.track_outcomes`` via the same feature-flag path the consumer
uses (env override > config.yaml > default), so producer and consumer agree.
Pure/best-effort; never raises.
"""
from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict, List

logger = logging.getLogger(__name__)

_MAX_SESSIONS = 1000  # cap the pending store (same LRU discipline as lesson_recall)

# Valence weights: how strong a negative signal each intervention is. An
# interrupt (user hit stop) is the strongest; a steer (course-correction) and a
# denied action are milder. Tune-able, but the ordering is the point.
SIGNAL_WEIGHTS: Dict[str, float] = {
    "interrupt": 1.0,
    "approval_denied": 0.8,
    "edit": 0.7,
    "steer": 0.5,
    "correction": 0.6,
}
# Total intervention weight at which friction saturates to 1.0. ~3 interventions
# in a session = maximally frictional. Keeps one stray interrupt from tanking a
# reward while repeated wrestling does.
_FRICTION_SATURATION = 3.0


def signals_path() -> Path:
    from janus_constants import get_janus_home
    return get_janus_home() / "learning" / "feedback_signals.json"


def _now_iso() -> str:
    try:
        from janus_time import now as _now
        return _now().isoformat()
    except Exception:
        return ""


def _tracking_on() -> bool:
    # Use the SAME gate the consumer (auto_mine → record_outcome) uses:
    # feature_flags honours the JANUS_FLAG_ env override that load_config does
    # not, so a config.yaml-vs-env mismatch can't make the producer inert while
    # the consumer is live (which would zero the signal in its own A/B harness).
    try:
        from agent.feature_flags import flag_enabled
        return flag_enabled("learning", "track_outcomes", default=False)
    except Exception:
        return False


def _load() -> Dict[str, List[Dict[str, Any]]]:
    p = signals_path()
    if not p.is_file():
        return {}
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (ValueError, OSError):
        return {}


def _save(state: Dict[str, List[Dict[str, Any]]]) -> None:
    if len(state) > _MAX_SESSIONS:
        state = dict(list(state.items())[-_MAX_SESSIONS:])
    p = signals_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    # Atomic write: a concurrent reader in a multi-session gateway must never see
    # a half-written file (json.loads would fail and _load would return {} —
    # wiping friction for ALL in-flight sessions, not just the racing pair).
    import os
    tmp = p.with_name(p.name + f".tmp{os.getpid()}")
    tmp.write_text(json.dumps(state, ensure_ascii=False), encoding="utf-8")
    os.replace(str(tmp), str(p))


def record_signal(session_id: str, kind: str, *, weight: float = None) -> None:
    """Record one implicit intervention for ``session_id``. No-op unless outcome
    tracking is on (the only consumer). Best-effort; safe on any hot path."""
    try:
        if not session_id or not _tracking_on():
            return
        w = SIGNAL_WEIGHTS.get(kind, 0.5) if weight is None else float(weight)
        state = _load()
        entries = state.get(session_id, [])
        entries.append({"kind": str(kind), "weight": w, "ts": _now_iso()})
        # Refresh LRU position so an active session isn't evicted mid-flight.
        state.pop(session_id, None)
        state[session_id] = entries
        _save(state)
    except Exception as exc:
        logger.debug("record_signal failed: %s", exc)


def session_friction(session_id: str) -> float:
    """Saturating friction in [0, 1] from a session's recorded interventions.
    0.0 when none / unknown."""
    try:
        entries = _load().get(session_id, [])
        total = sum(float(e.get("weight", 0) or 0) for e in entries)
        return round(min(1.0, total / _FRICTION_SATURATION), 4) if total > 0 else 0.0
    except Exception:
        return 0.0


def clear_session(session_id: str) -> None:
    """Drop a session's signals once its outcome has consumed them (idempotent)."""
    try:
        if not session_id:
            return
        state = _load()
        if state.pop(session_id, None) is not None:
            _save(state)
    except Exception as exc:
        logger.debug("clear_session failed: %s", exc)
