"""Per-turn cost ledger + per-session spend ceiling.

Appends one JSONL row per API turn (session, model, tokens, cost) under
``$JANUS_HOME/learning/cost_ledger.jsonl`` so spend is auditable after the fact,
and exposes the configured per-session USD ceiling the conversation loop checks
at the turn boundary to halt a runaway session.

Pure, best-effort, never raises. The ceiling only *stops the loop earlier* — it
never mutates the live conversation / system prompt / toolset, so the
prompt-caching invariant holds. See plans/self-improvement-roadmap (Track B / B-PR2)
and docs/token-optimization-audit.md.
"""
from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


def ledger_path() -> Path:
    from janus_constants import get_janus_home
    return get_janus_home() / "learning" / "cost_ledger.jsonl"


def _now_iso() -> str:
    try:
        from janus_time import now as _now
        return _now().isoformat()
    except Exception:
        return ""


def record_turn(
    session_id: str, model: str, *,
    input_tokens: int = 0, output_tokens: int = 0, cache_read_tokens: int = 0,
    cost_usd: float = 0.0, status: str = "", ts: str = "",
) -> bool:
    """Append one turn's usage + cost to the ledger. Best-effort; returns True
    if a row was written. Never raises."""
    try:
        row = {
            "ts": ts or _now_iso(),
            "session_id": session_id or "",
            "model": model or "",
            "input_tokens": int(input_tokens or 0),
            "output_tokens": int(output_tokens or 0),
            "cache_read_tokens": int(cache_read_tokens or 0),
            "cost_usd": round(float(cost_usd or 0.0), 6),
            "status": status or "",
        }
        path = ledger_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
        return True
    except Exception as exc:
        logger.debug("cost ledger write failed: %s", exc)
        return False


def session_cost_limit_usd(config: Optional[Dict[str, Any]] = None) -> Optional[float]:
    """The per-session USD ceiling from ``budget.session_cost_usd``. Returns None
    when unset / <= 0 (unlimited)."""
    try:
        if config is None:
            from janus_cli.config import load_config
            config = load_config()
        budget = (config.get("budget", {}) or {}) if isinstance(config, dict) else {}
        v = budget.get("session_cost_usd", 0)
        v = float(v) if v is not None else 0.0
        return v if v > 0 else None
    except Exception:
        return None


def over_session_budget(spent_usd: float, limit_usd: Optional[float]) -> bool:
    """True when an enforced ceiling has been reached. Pure; used by the loop gate."""
    try:
        return limit_usd is not None and limit_usd > 0 and float(spent_usd or 0.0) >= limit_usd
    except Exception:
        return False


def load_ledger() -> List[Dict[str, Any]]:
    """Read all ledger rows (for /insights or tests). Best-effort → []."""
    try:
        path = ledger_path()
        if not path.is_file():
            return []
        rows: List[Dict[str, Any]] = []
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except ValueError:
                continue
        return rows
    except Exception:
        return []


def session_total_usd(session_id: str) -> float:
    """Sum of ``cost_usd`` for one session from the ledger. Best-effort → 0.0."""
    try:
        return round(
            sum(float(r.get("cost_usd", 0.0)) for r in load_ledger()
                if r.get("session_id") == session_id),
            6,
        )
    except Exception:
        return 0.0
