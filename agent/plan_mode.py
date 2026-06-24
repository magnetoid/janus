"""Plan Mode — propose a plan and wait for approval before doing hard work.

Complements Standing Agreements: that keeps the agent from FORGETTING commitments;
this keeps it from ACTING before alignment. For tasks the agent judges hard +
multi-step + state-changing, a static (cache-safe) system-prompt directive tells it
to call ``propose_plan`` FIRST and wait for the user's "go". ``should_plan()`` is the
programmatic gate (reusing the free local complexity classifier) used by the
``/plan`` force flag. Config-gated (default on, hard-only), best-effort, never raises.
"""
from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

_DIRECTIVE = (
    "Plan mode: for any task you judge HARD — multi-step and state-changing "
    "(editing files, running commands, deploying, migrating) — do NOT start "
    "executing. First call the propose_plan tool with your concrete step-by-step "
    "plan, then STOP and wait for the user to approve ('go') or adjust it. Keep "
    "simple questions and quick one-step edits immediate — only plan the genuinely "
    "hard work. Honor any standing agreements when you plan."
)

# Process-local one-shot force flags set by the /plan command (consumed next turn).
_forced: Dict[str, bool] = {}


def enabled(config: Optional[Dict[str, Any]] = None) -> bool:
    """True when Plan mode is on (default on)."""
    try:
        if config is None:
            from janus_cli.config import load_config
            config = load_config()
        pm = (config.get("plan_mode", {}) or {}) if isinstance(config, dict) else {}
        return bool(pm.get("enabled", True))
    except Exception:
        return True


def directive(config: Optional[Dict[str, Any]] = None) -> str:
    """Static system-prompt directive (empty when disabled). Cache-safe: belongs in
    the stable prompt part, set once at session start."""
    return _DIRECTIVE if enabled(config) else ""


def should_plan(prompt: str, config: Optional[Dict[str, Any]] = None, *, forced: bool = False) -> bool:
    """Programmatic gate: plan when enabled AND (forced or the task is 'hard').

    Reuses agent/task_complexity.classify_complexity (free, local — no token cost).
    """
    try:
        if not enabled(config):
            return False
        if forced:
            return True
        from agent.task_complexity import classify_complexity
        return classify_complexity(str(prompt)) == "hard"
    except Exception as exc:
        logger.debug("should_plan failed: %s", exc)
        return False


def set_forced(session: Any) -> None:
    """/plan: force the next task to plan regardless of complexity."""
    _forced[str(session)] = True


def consume_forced(session: Any) -> bool:
    """Read-and-clear the force flag (one-shot)."""
    return bool(_forced.pop(str(session), False))


# --- per-session plan store -------------------------------------------------

def _store_path(session: Any) -> Path:
    from janus_constants import get_janus_home
    safe = "".join(c for c in str(session) if c.isalnum() or c in "-_") or "default"
    return get_janus_home() / "plans" / f"{safe}.json"


def record_plan(session: Any, steps: List[str]) -> List[str]:
    """Persist the proposed plan steps (trimmed, blanks dropped). Returns them."""
    cleaned = [s.strip() for s in (steps or []) if str(s).strip()]
    try:
        p = _store_path(session)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(cleaned, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    except Exception as exc:
        logger.debug("record_plan failed: %s", exc)
    return cleaned


def load_plan(session: Any) -> List[str]:
    p = _store_path(session)
    if not p.is_file():
        return []
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (ValueError, OSError):
        return []


def clear(session: Any) -> int:
    n = len(load_plan(session))
    try:
        p = _store_path(session)
        if p.is_file():
            p.unlink()
    except OSError:
        pass
    return n


def format_plan(steps: List[str]) -> str:
    """Render the plan as a numbered list + approval prompt (empty when no steps)."""
    cleaned = [s.strip() for s in (steps or []) if str(s).strip()]
    if not cleaned:
        return ""
    lines = ["📋 **Plan** — here's what I'll do:"]
    lines.extend(f"{i}. {s}" for i, s in enumerate(cleaned, 1))
    lines.append("\nReply **go** to approve, or tell me what to change.")
    return "\n".join(lines)
