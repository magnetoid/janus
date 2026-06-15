"""Longitudinal eval runner — turn the eval suite into a learning curve.

agent/evals.py runs the suite once and reports pass/fail. This records a
pass-rate point every run to $JANUS_HOME/evals/trend.jsonl so improvement (and
regression) is visible over time, detects which evals flipped, and A/B-compares
a learning feature ON vs OFF. Deterministic checks make the curve trustworthy:
it can't drift the way LLM-judged outcomes can.

Best-effort throughout; an injectable agent_runner makes everything testable
without a live model.
"""
from __future__ import annotations

import hashlib
import json
import logging
import os
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)


def trend_path() -> Path:
    from agent.evals import evals_dir
    return evals_dir() / "trend.jsonl"


def _now_iso() -> str:
    try:
        from janus_time import now as _now
        return _now().isoformat()
    except Exception:
        return ""


def _suite_hash(specs) -> str:
    h = hashlib.sha256()
    for s in sorted(specs, key=lambda x: x.name):
        h.update(s.name.encode("utf-8"))
        h.update(json.dumps(s.checks, sort_keys=True, ensure_ascii=False).encode("utf-8"))
    return h.hexdigest()[:12]


def _append(record: Dict[str, Any]) -> None:
    path = trend_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")


def _load_trend() -> List[Dict[str, Any]]:
    path = trend_path()
    if not path.is_file():
        return []
    out: List[Dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            try:
                out.append(json.loads(line))
            except ValueError:
                continue
    return out


def run_trend(
    specs: Optional[list] = None,
    agent_runner: Optional[Callable[[Any], Dict[str, Any]]] = None,
    save: bool = True,
    path: Optional[Path] = None,
) -> Dict[str, Any]:
    """Run the suite once, append a pass-rate point, return the record.

    Best-effort: returns ``{"error": ...}`` instead of raising.
    """
    try:
        from agent.evals import load_eval_specs, run_evals
        if specs is None:
            specs = load_eval_specs(path)
        summary = run_evals(specs, agent_runner=agent_runner, save_results=False)
        total = summary["total"]
        record = {
            "ts": _now_iso(),
            "pass_rate": round(summary["passed"] / total, 4) if total else None,
            "total": total,
            "passed": summary["passed"],
            "per_eval": {r["name"]: r["passed"] for r in summary["results"]},
            "suite_hash": _suite_hash(specs),
        }
        if save:
            _append(record)
        return record
    except Exception as exc:
        logger.debug("run_trend failed: %s", exc)
        return {"error": str(exc)}


def _flag_env_var(flag: str) -> str:
    section, _, key = flag.partition(".")
    return "JANUS_FLAG_" + section.upper() + "__" + key.upper().replace(".", "__")


def compare_feature(
    flag: str,
    specs: Optional[list] = None,
    agent_runner: Optional[Callable[[Any], Dict[str, Any]]] = None,
    path: Optional[Path] = None,
) -> Dict[str, Any]:
    """Suite pass-rate with ``flag`` ON vs OFF (env override). Returns the delta.

    ``flag`` is a ``section.key`` path (e.g. ``learning.reflexion``). Best-effort.
    For write-time features (memory.write_time_reconcile) the suite must contain
    purpose-built use_memory scenarios; see the spec's seeded-memory note.
    """
    try:
        from agent.evals import load_eval_specs
        if specs is None:
            specs = load_eval_specs(path)
        var = _flag_env_var(flag)
        prior = os.environ.get(var)
        try:
            os.environ[var] = "1"
            on = run_trend(specs=specs, agent_runner=agent_runner, save=False)
            os.environ[var] = "0"
            off = run_trend(specs=specs, agent_runner=agent_runner, save=False)
        finally:
            if prior is None:
                os.environ.pop(var, None)
            else:
                os.environ[var] = prior
        on_pe, off_pe = on.get("per_eval", {}), off.get("per_eval", {})
        per_eval_delta = {
            name: int(bool(on_pe.get(name))) - int(bool(off_pe.get(name)))
            for name in set(on_pe) | set(off_pe)
        }
        pr_on = on.get("pass_rate") or 0.0
        pr_off = off.get("pass_rate") or 0.0
        return {
            "flag": flag,
            "pass_rate_on": pr_on,
            "pass_rate_off": pr_off,
            "delta": round(pr_on - pr_off, 4),
            "per_eval_delta": per_eval_delta,
        }
    except Exception as exc:
        logger.debug("compare_feature failed: %s", exc)
        return {"flag": flag, "error": str(exc)}


def _state_path() -> Path:
    from agent.evals import evals_dir
    return evals_dir() / "trend_state.json"


def _load_state() -> Dict[str, Any]:
    p = _state_path()
    if not p.is_file():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (ValueError, OSError):
        return {}


def _save_state(data: Dict[str, Any]) -> None:
    p = _state_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data), encoding="utf-8")


def _hours_since(iso: str) -> float:
    if not iso:
        return float("inf")
    try:
        from datetime import datetime
        from janus_time import now as _now
        prev = datetime.fromisoformat(iso)
        return (_now() - prev).total_seconds() / 3600.0
    except Exception:
        return float("inf")


def maybe_run_trend(
    agent_runner: Optional[Callable[[Any], Dict[str, Any]]] = None,
) -> Optional[Dict[str, Any]]:
    """Run a trend point iff enabled and the interval has elapsed. Else None."""
    try:
        from agent.feature_flags import flag_enabled
        if not flag_enabled("evals", "trend.enabled", default=False):
            return None
        interval = 24
        try:
            from janus_cli.config import load_config
            interval = int((load_config().get("evals", {}).get("trend", {}) or {}).get("interval_hours", 24))
        except Exception:
            pass
        state = _load_state()
        if _hours_since(state.get("last_run", "")) < interval:
            return None
        rec = run_trend(agent_runner=agent_runner)
        if not rec.get("error"):
            _save_state({"last_run": _now_iso(), "last_pass_rate": rec.get("pass_rate")})
        return rec
    except Exception as exc:
        logger.debug("maybe_run_trend failed: %s", exc)
        return None


def learning_curve(window: Optional[int] = None) -> Dict[str, Any]:
    """Pass-rate time series for the current suite version + which evals flipped.

    Only points sharing the latest ``suite_hash`` are compared, so adding/editing
    evals never creates phantom regressions. ``learned`` = evals that went
    fail->pass between the first and latest point; ``regressed`` = pass->fail.
    """
    records = _load_trend()
    if not records:
        return {"points": [], "learned": [], "regressed": [], "suite_hash": None}
    latest_hash = records[-1].get("suite_hash")
    same = [r for r in records if r.get("suite_hash") == latest_hash]
    if window:
        same = same[-window:]
    points = [{"ts": r["ts"], "pass_rate": r["pass_rate"]} for r in same]
    learned: List[str] = []
    regressed: List[str] = []
    if len(same) >= 2:
        first, last = same[0].get("per_eval", {}), same[-1].get("per_eval", {})
        for name in set(first) & set(last):
            if not first[name] and last[name]:
                learned.append(name)
            elif first[name] and not last[name]:
                regressed.append(name)
    return {
        "points": points,
        "learned": sorted(learned),
        "regressed": sorted(regressed),
        "suite_hash": latest_hash,
    }
