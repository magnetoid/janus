"""Learning-loop insights — does the closed loop actually make the agent better?

Reads the file-based learning stores (eval trend, outcomes, mining log, lessons,
playbook, skill drafts) and returns a report dict, rendered to terminal/gateway
text and composed into the `insights` command. Pure and best-effort: every
metric is independently guarded and a missing store yields an empty series, not
an exception. No model calls.
"""
from __future__ import annotations

import json
import logging
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


def _ts_to_epoch(ts: str) -> Optional[float]:
    if not ts:
        return None
    try:
        return datetime.fromisoformat(ts).timestamp()
    except (ValueError, TypeError):
        return None


def _eval_section(days: int, now: float) -> Dict[str, Any]:
    out: Dict[str, Any] = {"points": [], "latest": None, "first": None,
                           "delta": None, "runs": 0, "per_eval_latest": {}}
    try:
        from agent.eval_trend import trend_path
        p = trend_path()
        if not p.is_file():
            return out
        records: List[Dict[str, Any]] = []
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.strip():
                try:
                    records.append(json.loads(line))
                except ValueError:
                    continue
        if not records:
            return out
        out["runs"] = len(records)
        out["points"] = [{"ts": r.get("ts"), "pass_rate": r.get("pass_rate")}
                         for r in records]
        rated = [r.get("pass_rate") for r in records if isinstance(r.get("pass_rate"), (int, float))]
        if rated:
            out["latest"], out["first"] = rated[-1], rated[0]
            out["delta"] = round(rated[-1] - rated[0], 4)
        out["per_eval_latest"] = records[-1].get("per_eval", {}) or {}
    except Exception as exc:
        logger.debug("learning-insights eval section failed: %s", exc)
    return out


def _outcomes_section(days: int, now: float) -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "all_time": {"sessions": 0, "successes": 0, "success_rate": None},
        "windowed": {"sessions": 0, "successes": 0, "success_rate": None},
        "recent": None, "by_skill": {}, "by_persona": {},
    }
    try:
        from agent import outcome_tracker as ot
        out["all_time"] = ot.overall_stats()
        out["recent"] = ot.recent_success_rate(window=10)
        out["by_skill"] = ot.skill_stats()
        records = ot.load()
        cutoff = now - days * 86400
        win = [r for r in records
               if (_ts_to_epoch(r.get("ts", "")) or 0) >= cutoff]
        wins = sum(1 for r in win if r.get("success"))
        wn = len(win)
        out["windowed"] = {
            "sessions": wn, "successes": wins,
            "success_rate": round(wins / wn, 3) if wn else None,
        }
        personas: Dict[str, List[bool]] = {}
        for r in records:
            personas.setdefault(r.get("persona") or "(none)", []).append(bool(r.get("success")))
        out["by_persona"] = {
            k: {"sessions": len(v), "success_rate": round(sum(v) / len(v), 3)}
            for k, v in personas.items() if v
        }
    except Exception as exc:
        logger.debug("learning-insights outcomes section failed: %s", exc)
    return out


def _mining_section(days: int, now: float) -> Dict[str, Any]:
    out: Dict[str, Any] = {"cycles": 0, "graduated_facts": 0, "graduated_skills": 0,
                           "lessons": 0, "pruned": 0, "points": []}
    try:
        from agent.sleep import sleep_log_path
        p = sleep_log_path()
        if not p.is_file():
            return out
        cutoff = now - days * 86400
        for line in p.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            ep = _ts_to_epoch(rec.get("ts", ""))
            if ep is not None and ep < cutoff:
                continue
            out["cycles"] += 1
            out["graduated_facts"] += int(rec.get("graduated_facts", 0) or 0)
            out["graduated_skills"] += int(rec.get("graduated_skills", 0) or 0)
            out["lessons"] += int(rec.get("lessons", 0) or 0)
            out["pruned"] += int(rec.get("pruned", 0) or 0)
            out["points"].append(rec)
    except Exception as exc:
        logger.debug("learning-insights mining section failed: %s", exc)
    return out


def _count_skill_dirs(base: Path) -> int:
    try:
        if not base.is_dir():
            return 0
        return sum(1 for d in base.iterdir()
                   if d.is_dir() and not d.name.startswith(".")
                   and (d / "SKILL.md").is_file())
    except OSError:
        return 0


def _knowledge_section() -> Dict[str, Any]:
    out = {"lessons": 0, "playbook_entries": 0, "active_skills": 0, "draft_skills": 0}
    try:
        from agent import lessons as _lessons
        out["lessons"] = len(_lessons.load())
    except Exception as exc:
        logger.debug("learning-insights lessons count failed: %s", exc)
    try:
        from agent import playbook as _pb
        out["playbook_entries"] = len(_pb.load())
    except Exception as exc:
        logger.debug("learning-insights playbook count failed: %s", exc)
    try:
        from janus_constants import get_janus_home
        home = get_janus_home()
        out["active_skills"] = _count_skill_dirs(home / "skills")
        out["draft_skills"] = _count_skill_dirs(home / "skills" / ".drafts")
    except Exception as exc:
        logger.debug("learning-insights skill counts failed: %s", exc)
    return out


def generate_learning_report(days: int = 30, *, now: Optional[float] = None) -> Dict[str, Any]:
    """Aggregate learning-loop metrics. Pure, best-effort, never raises."""
    now = time.time() if now is None else now
    return {
        "days": days,
        "eval": _eval_section(days, now),
        "outcomes": _outcomes_section(days, now),
        "mining": _mining_section(days, now),
        "knowledge": _knowledge_section(),
    }
