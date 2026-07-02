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


# Noise floor for flip detection (learning_curve): with k trials per point,
# an eval only counts as learned/regressed when it moved between the
# consistently-passing and consistently-failing bands; fractions in between
# are flaky. Old single-run records (booleans) coerce to 0.0/1.0 and behave
# exactly as before.
_CONSISTENT_PASS = 0.8
_CONSISTENT_FAIL = 0.2
# A one-point pass-rate JUMP at or above this is ADVISORY only — surfaced for
# human attention, never a gate failure or a governor freeze. A single-suite
# aggregate pass-rate delta cannot distinguish genuine learning (which legitimately
# jumps, e.g. +1/3 when one eval is learned in a 3-eval suite) from a gamed
# evaluator, and gating on it both false-freezes real wins and self-clears on the
# next point — so it warns, it does not block. Durable reward-hacking detection
# needs eval provenance + human-ack (a later move), not a pass-rate heuristic.
_SUSPICIOUS_JUMP = 0.3


def _pass_frac(value) -> float:
    """Coerce a per_eval entry (bool from old records, fraction from new) to [0,1]."""
    try:
        return max(0.0, min(1.0, float(value)))
    except (TypeError, ValueError):
        return 1.0 if bool(value) else 0.0


def _suite_hash(specs) -> str:
    h = hashlib.sha256()
    for s in sorted(specs, key=lambda x: x.name):
        h.update(s.name.encode("utf-8"))
        h.update(json.dumps(s.checks, sort_keys=True, ensure_ascii=False).encode("utf-8"))
        # kind is part of the suite identity: flipping an eval regression↔
        # capability changes what the gate enforces, so it MUST reset the
        # comparison window (a visible history discontinuity + fail-closed's
        # "not enough history"). Otherwise a failing regression eval could be
        # silently exempted by editing one YAML field with no trace.
        h.update(getattr(s, "kind", "regression").encode("utf-8"))
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


def time_horizon(per_eval: Dict[str, Any], minutes: Dict[str, Any]) -> float:
    """METR-style 50%-success time horizon (move 8): the longest task length (in
    estimated human-minutes) the agent passes at least half the time.

    ``per_eval`` maps eval name → pass FRACTION (move 2 pass^k output); ``minutes``
    maps eval name → est_minutes. Only tagged evals (minutes > 0) count. Returns
    0.0 when nothing qualifies. Saturation-resistant: bounded only by the longest
    task in the suite, so it keeps rising as harder tasks are added — unlike a
    pass-rate that caps at 100%.
    """
    try:
        qualifying = [
            float(minutes[name]) for name, frac in per_eval.items()
            if float(minutes.get(name, 0) or 0) > 0 and _pass_frac(frac) >= 0.5
        ]
        return round(max(qualifying), 4) if qualifying else 0.0
    except Exception:
        return 0.0


def _configured_trials() -> int:
    try:
        from janus_cli.config import load_config
        t = ((load_config().get("evals", {}) or {}).get("trend", {}) or {}).get("trials", 3)
        return max(1, int(t))
    except Exception:
        return 3


def run_trend(
    specs: Optional[list] = None,
    agent_runner: Optional[Callable[[Any], Dict[str, Any]]] = None,
    save: bool = True,
    path: Optional[Path] = None,
    trials: Optional[int] = None,
) -> Dict[str, Any]:
    """Run the suite ``trials`` times, append a pass^k point, return the record.

    Single-run pass@1 varies by points even at temperature 0, so one run cannot
    distinguish learning from noise. Each eval is run ``trials`` times
    (``evals.trend.trials``, default 3) and ``per_eval`` records its pass
    FRACTION; an eval counts as passed only when it passed every trial
    (pass^k — the reliability the gate cares about). Best-effort: returns
    ``{"error": ...}`` instead of raising.
    """
    try:
        from agent.evals import load_eval_specs, run_evals
        if specs is None:
            specs = load_eval_specs(path)
        k = max(1, int(trials)) if trials is not None else _configured_trials()
        passes: Dict[str, int] = {}
        for _ in range(k):
            summary = run_evals(specs, agent_runner=agent_runner, save_results=False)
            for r in summary["results"]:
                passes[r["name"]] = passes.get(r["name"], 0) + (1 if r["passed"] else 0)
        total = len(specs)
        per_eval = {name: round(n / k, 4) for name, n in passes.items()}
        passed = sum(1 for frac in per_eval.values() if frac >= 1.0)
        minutes = {s.name: float(getattr(s, "est_minutes", 0) or 0) for s in specs}
        record = {
            "ts": _now_iso(),
            "pass_rate": round(passed / total, 4) if total else None,
            "total": total,
            "passed": passed,
            "trials": k,
            "per_eval": per_eval,
            "kinds": {s.name: getattr(s, "kind", "regression") for s in specs},
            "est_minutes": minutes,
            "horizon_minutes": time_horizon(per_eval, minutes),
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
            name: round(_pass_frac(on_pe.get(name, 0)) - _pass_frac(off_pe.get(name, 0)), 4)
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
        return {"points": [], "learned": [], "regressed": [], "flaky": [],
                "suite_hash": None}
    latest_hash = records[-1].get("suite_hash")
    same = [r for r in records if r.get("suite_hash") == latest_hash]
    if window:
        same = same[-window:]
    points = [{"ts": r["ts"], "pass_rate": r["pass_rate"],
               "horizon_minutes": r.get("horizon_minutes")} for r in same]

    # Per-eval fraction SERIES across the window — not just first-vs-last. The
    # baseline for each eval is the best it was reliably at in any PRIOR point
    # (max), so "learned then broke" (0→1→0) and "passed at point 3, broke at
    # point 7" are caught, and a noisy sub-reliable first point can't blind the
    # detector for the life of the suite version.
    series: Dict[str, List[float]] = {}
    for r in same:
        for name, val in (r.get("per_eval") or {}).items():
            series.setdefault(name, []).append(_pass_frac(val))

    learned: List[str] = []
    regressed: List[str] = []
    flaky: List[str] = []
    if len(same) >= 2:
        for name, seq in series.items():
            if len(seq) < 2:
                continue
            cur, prior = seq[-1], seq[:-1]
            prior_max, prior_min = max(prior), min(prior)
            # Was reliable, now not — but tolerate a single noisy dip (k=3 can't
            # tell 0.67 from 1.0 in one point): a mid-band drop only counts as a
            # regression when SUSTAINED across the last two points; a hard 0/k
            # counts immediately.
            sustained_low = all(x < _CONSISTENT_PASS for x in seq[-2:])
            if prior_max >= _CONSISTENT_PASS and (
                cur <= _CONSISTENT_FAIL or (cur < _CONSISTENT_PASS and sustained_low)
            ):
                regressed.append(name)
            elif prior_min <= _CONSISTENT_FAIL and cur >= _CONSISTENT_PASS:
                learned.append(name)
            elif _CONSISTENT_FAIL < cur < _CONSISTENT_PASS:
                flaky.append(name)
    return {
        "points": points,
        "learned": sorted(learned),
        "regressed": sorted(regressed),
        "flaky": sorted(flaky),
        "suite_hash": latest_hash,
    }


def regression_gate(window: Optional[int] = None, *,
                    fail_closed: bool = False) -> Dict[str, Any]:
    """CI / cron regression check over the eval learning curve.

    ``ok`` is False when any ``kind: regression`` eval consistently flipped
    pass→fail within the latest ``suite_hash`` window (noise-floored via
    learning_curve — a single trial's bad luck can't fail the gate).
    ``kind: capability`` churn and flaky evals are REPORTED but never fail it.
    A large one-point pass-rate jump is surfaced as an advisory ``warnings``
    entry only — see ``_SUSPICIOUS_JUMP``: it is not a reliable reward-hacking
    signal, so it must not false-freeze a genuine win.
    ``fail_closed=True`` (CI) additionally fails on missing history, an empty
    suite, or an internal error, so a broken/emptied harness can't pass
    silently. The default stays fail-open for cron. Reuses ``learning_curve`` —
    the governor freeze reads the same signal.
    """
    try:
        lc = learning_curve(window=window)
        regressed = lc.get("regressed") or []
        learned = lc.get("learned") or []
        flaky = lc.get("flaky") or []
        points = lc.get("points") or []
        pass_rate = points[-1]["pass_rate"] if points else None

        # Only regression-kind evals hard-fail the gate. Kinds come from the
        # latest record; evals unknown to it (or suites predating the field)
        # default to regression — the conservative side. kind is part of
        # suite_hash, so a kind flip resets the window rather than silently
        # re-labelling a failing eval mid-history.
        records = []
        latest_total = None
        try:
            records = [r for r in _load_trend()
                       if r.get("suite_hash") == lc.get("suite_hash")]
            if records:
                kinds = records[-1].get("kinds") or {}
                latest_total = records[-1].get("total")
            else:
                kinds = {}
        except Exception:
            kinds = {}
        hard = [n for n in regressed if kinds.get(n, "regression") == "regression"]
        soft = [n for n in regressed if n not in hard]

        # Advisory only — never sets ok=False (see _SUSPICIOUS_JUMP).
        warnings: List[str] = []
        jump = None
        if len(points) >= 2:
            try:
                jump = round(points[-1]["pass_rate"] - points[-2]["pass_rate"], 4)
            except (TypeError, KeyError):
                jump = None
        if jump is not None and jump >= _SUSPICIOUS_JUMP:
            warnings.append(
                f"pass rate rose {jump:+.0%} in one point — worth confirming the "
                f"evaluator wasn't gamed (advisory, not a gate failure)")

        empty_suite = latest_total == 0
        ok = not hard
        if hard:
            msg = f"REGRESSION — {len(hard)} eval(s) went pass→fail: {', '.join(hard)}"
        elif fail_closed and (len(points) < 2 or empty_suite):
            ok = False
            msg = ("FAIL-CLOSED — the suite ran zero evals" if empty_suite
                   else "FAIL-CLOSED — not enough eval history to compare")
        elif len(points) < 2:
            msg = "OK — not enough eval history to compare yet"
        else:
            extras = []
            if soft:
                extras.append(f"{len(soft)} capability eval(s) churned: {', '.join(soft)}")
            if flaky:
                extras.append(f"{len(flaky)} flaky: {', '.join(flaky)}")
            msg = f"OK — no regressions ({len(learned)} learned" + \
                  (f"; {'; '.join(extras)}" if extras else "") + ")"
        if warnings:
            msg += "  [!] " + "; ".join(warnings)
        return {"ok": ok, "regressed": hard, "capability_churn": soft,
                "flaky": flaky, "learned": learned, "jump": jump,
                "warnings": warnings, "pass_rate": pass_rate,
                "suite_hash": lc.get("suite_hash"), "message": msg}
    except Exception as exc:
        return {"ok": not fail_closed, "regressed": [], "capability_churn": [],
                "flaky": [], "learned": [], "jump": None, "warnings": [],
                "pass_rate": None, "suite_hash": None,
                "message": (f"FAIL-CLOSED — error: {exc}" if fail_closed
                            else f"gate skipped (error: {exc})")}
