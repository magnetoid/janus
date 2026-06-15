# Measurable Self-Improvement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make Janus measurably self-improving — a longitudinal, self-growing eval spine on top of `agent/evals.py` (learning curve + failure-generated regression pins + A/B feature gate), shipped with write-time memory reconciliation as the first proven feature.

**Architecture:** Three spine modules (`agent/eval_trend.py`, `agent/eval_miner.py`, a feature-flag override helper) plus one feature (write-time `ADD/UPDATE/DELETE/NOOP` reconciliation in the memory miner), wired into the existing session-end (`auto_mine`), gateway-cron, CLI (`janus evals`), and dashboard surfaces. All new code is best-effort (never raises), injectable-`llm_caller`, config-gated default-off. No fine-tuning.

**Tech Stack:** Python 3.11, pytest via `scripts/run_tests.sh`, FastAPI (dashboard router), React/Vite (LearningPage), YAML eval specs, JSONL storage under `$JANUS_HOME/`.

---

## Spec reference

`docs/superpowers/specs/2026-06-15-measurable-self-learning-design.md` (committed `197c481`).

## Conventions every task follows

- Tests run **only** via the wrapper: `scripts/run_tests.sh tests/path/test.py`. Never bare `pytest`.
- The autouse `_isolate_janus_home` fixture redirects `get_janus_home()` to a temp dir, so tests write to a throwaway `$JANUS_HOME`. Never hardcode `~/.janus`.
- Timestamps use `janus_time.now()` with a `""` fallback (mirror `agent/outcome_tracker._now_iso`).
- Every public function is best-effort: wrap the body so it never raises; report errors in the return dict.
- Commit after each task with the message shown in its final step.

## File structure (what each new/changed file owns)

- `agent/feature_flags.py` *(new)* — single source of truth for reading a gated config flag, with an env-var override layer so the A/B gate can flip a feature for one suite run.
- `agent/eval_trend.py` *(new)* — longitudinal eval runner: `run_trend`, `learning_curve`, `compare_feature`, `maybe_run_trend`; storage in `$JANUS_HOME/evals/trend.jsonl`.
- `agent/eval_miner.py` *(new)* — failure → draft regression-pin eval spec, quarantined in `$JANUS_HOME/evals/.drafts/`.
- `agent/memory_gardener.py` *(modify)* — add `reconcile_candidate` (per-candidate `ADD/UPDATE/DELETE/NOOP` decision).
- `agent/memory_miner.py` *(modify)* — apply write-time reconciliation in `mine_session_memory` when gated on.
- `agent/auto_mine.py` *(modify)* — route flag reads through `feature_flags`; on failure, also draft a regression pin.
- `janus_cli/config.py` *(modify)* — new `evals` section + `memory.write_time_reconcile` key.
- `janus_cli/evals.py` *(modify)* — `trend` and `ab` subcommands.
- `janus_cli/routers/learning.py` *(modify)* — expose curve + draft-pin count.
- `web/src/pages/LearningPage.tsx` *(modify)* — learning-curve card.
- `gateway/runner.py` *(modify)* — call `maybe_run_trend` next to `maybe_run_sleep`.

---

## Task 1: Config keys

**Files:**
- Modify: `janus_cli/config.py` (the `DEFAULT_CONFIG` dict — add an `evals` block after the `learning` block ~line 1712, and a key inside the existing `memory` block)
- Test: `tests/janus_cli/test_config_learning_keys.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/janus_cli/test_config_learning_keys.py
"""The measurable-self-improvement feature flags exist with safe defaults."""
from janus_cli.config import DEFAULT_CONFIG


def test_evals_trend_defaults_off():
    evals = DEFAULT_CONFIG["evals"]
    assert evals["trend"]["enabled"] is False
    assert evals["trend"]["interval_hours"] == 24
    assert evals["autopin"] is False


def test_write_time_reconcile_default_off():
    assert DEFAULT_CONFIG["memory"]["write_time_reconcile"] is False
```

- [ ] **Step 2: Run test to verify it fails**

Run: `scripts/run_tests.sh tests/janus_cli/test_config_learning_keys.py`
Expected: FAIL — `KeyError: 'evals'`.

- [ ] **Step 3: Add the config blocks**

In `janus_cli/config.py`, immediately after the `"learning": { ... }` block, add:

```python
    # Measurable self-improvement (docs/superpowers/specs/2026-06-15-...).
    # The eval spine runs the $JANUS_HOME/evals/ suite on a schedule and records
    # a pass-rate learning curve; autopin drafts a regression-pin eval from a
    # failed session (quarantined in evals/.drafts/ for review). Opt-in (cost:
    # eval runs spend model calls).
    "evals": {
        "trend": {
            "enabled": False,
            "interval_hours": 24,   # at most once a day automatically
        },
        "autopin": False,           # failed session -> draft regression-pin eval
    },
```

In the existing `"memory": { ... }` block, add this key (next to `session_mining`):

```python
        # Write-time reconciliation: classify each mined fact ADD/UPDATE/DELETE/
        # NOOP against existing memory (Mem0-style) instead of append-only, so
        # stale facts are superseded at write time. Opt-in.
        "write_time_reconcile": False,
```

- [ ] **Step 4: Run test to verify it passes**

Run: `scripts/run_tests.sh tests/janus_cli/test_config_learning_keys.py`
Expected: PASS (2 passed).

- [ ] **Step 5: Commit**

```bash
git add janus_cli/config.py tests/janus_cli/test_config_learning_keys.py
git commit -m "feat(config): add evals.trend / evals.autopin / memory.write_time_reconcile flags"
```

---

## Task 2: Feature-flag override helper

A single flag reader with an env override, so `compare_feature` (Task 5) can flip a feature ON/OFF for one suite run without editing config on disk. Refactor `auto_mine._flag` to delegate to it.

**Files:**
- Create: `agent/feature_flags.py`
- Modify: `agent/auto_mine.py:23-36` (replace the local `_flag` body with a delegate)
- Test: `tests/agent/test_feature_flags.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/agent/test_feature_flags.py
"""Gated flag reads: config.yaml value, with an env override on top."""
import yaml

from agent import feature_flags as ff
from janus_constants import get_janus_home


def _write_config(d):
    home = get_janus_home()
    home.mkdir(parents=True, exist_ok=True)
    (home / "config.yaml").write_text(yaml.safe_dump(d), encoding="utf-8")


def test_missing_config_returns_default():
    assert ff.flag_enabled("evals", "autopin", default=False) is False
    assert ff.flag_enabled("learning", "reflexion", default=True) is True


def test_config_value_wins_over_default():
    _write_config({"evals": {"autopin": True}})
    assert ff.flag_enabled("evals", "autopin", default=False) is True


def test_env_override_wins_over_config(monkeypatch):
    _write_config({"evals": {"autopin": False}})
    monkeypatch.setenv("JANUS_FLAG_EVALS__AUTOPIN", "1")
    assert ff.flag_enabled("evals", "autopin", default=False) is True
    monkeypatch.setenv("JANUS_FLAG_EVALS__AUTOPIN", "0")
    assert ff.flag_enabled("evals", "autopin", default=False) is False


def test_nested_key_path():
    _write_config({"evals": {"trend": {"enabled": True}}})
    assert ff.flag_enabled("evals", "trend.enabled", default=False) is True
```

- [ ] **Step 2: Run test to verify it fails**

Run: `scripts/run_tests.sh tests/agent/test_feature_flags.py`
Expected: FAIL — `ModuleNotFoundError: No module named 'agent.feature_flags'`.

- [ ] **Step 3: Write the implementation**

```python
# agent/feature_flags.py
"""Read a gated boolean config flag, with an env-var override layer.

Precedence (highest first): env override > config.yaml > default. The env layer
exists so the eval A/B gate (agent/eval_trend.compare_feature) can flip a
feature ON/OFF for a single hermetic suite run without mutating config on disk.

Override var name: ``JANUS_FLAG_<SECTION>__<KEY>`` (key dots become double
underscores), e.g. ``JANUS_FLAG_EVALS__TREND__ENABLED``. Truthy = 1/true/yes/on.
Best-effort: any error falls back to ``default``.
"""
from __future__ import annotations

import logging
import os
from typing import Any

logger = logging.getLogger(__name__)

_TRUTHY = {"1", "true", "yes", "on"}
_FALSY = {"0", "false", "no", "off"}


def _env_override(section: str, key: str):
    var = "JANUS_FLAG_" + section.upper() + "__" + key.upper().replace(".", "__")
    raw = os.environ.get(var)
    if raw is None:
        return None
    low = raw.strip().lower()
    if low in _TRUTHY:
        return True
    if low in _FALSY:
        return False
    return None


def _config_value(section: str, key: str):
    try:
        import yaml
        from janus_constants import get_janus_home

        cfg_path = get_janus_home() / "config.yaml"
        if not cfg_path.is_file():
            return None
        cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
        node: Any = cfg.get(section, {})
        for part in key.split("."):
            if not isinstance(node, dict) or part not in node:
                return None
            node = node[part]
        return node
    except Exception as exc:
        logger.debug("flag config read failed: %s", exc)
        return None


def flag_enabled(section: str, key: str, *, default: bool = False) -> bool:
    """True/False for ``section.key``: env override > config.yaml > default."""
    override = _env_override(section, key)
    if override is not None:
        return override
    value = _config_value(section, key)
    if value is None:
        return default
    return bool(value)
```

- [ ] **Step 4: Refactor `auto_mine._flag` to delegate**

In `agent/auto_mine.py`, replace the whole `_flag` function (lines ~23-36) with:

```python
def _flag(section: str, key: str, *, default: bool = False) -> bool:
    from agent.feature_flags import flag_enabled
    return flag_enabled(section, key, default=default)
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `scripts/run_tests.sh tests/agent/test_feature_flags.py tests/agent/test_auto_mine.py`
Expected: PASS (existing auto_mine tests still green — behavior is unchanged when no env override is set).

- [ ] **Step 6: Commit**

```bash
git add agent/feature_flags.py agent/auto_mine.py tests/agent/test_feature_flags.py
git commit -m "feat(learning): feature-flag reader with env override; route auto_mine through it"
```

---

## Task 3: eval_trend — run_trend + trend.jsonl storage

**Files:**
- Create: `agent/eval_trend.py`
- Test: `tests/agent/test_eval_trend.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/agent/test_eval_trend.py
"""Longitudinal eval runner: records a pass-rate point per run."""
from agent import eval_trend as et
from agent.evals import EvalSpec


def _specs():
    return [
        EvalSpec(name="a", prompt="p", checks=[{"type": "contains", "value": "x"}]),
        EvalSpec(name="b", prompt="p", checks=[{"type": "contains", "value": "y"}]),
    ]


def _runner(passing_names):
    # fake agent_runner: response contains 'x'/'y' only for names we want to pass
    def run(spec):
        text = ""
        if spec.name in passing_names:
            text = spec.checks[0]["value"]
        return {"final_response": text, "messages": []}
    return run


def test_run_trend_records_point():
    rec = et.run_trend(specs=_specs(), agent_runner=_runner({"a", "b"}))
    assert rec["pass_rate"] == 1.0
    assert rec["total"] == 2 and rec["passed"] == 2
    assert rec["per_eval"] == {"a": True, "b": True}
    assert rec["suite_hash"]
    # persisted
    assert len(et._load_trend()) == 1


def test_run_trend_partial():
    rec = et.run_trend(specs=_specs(), agent_runner=_runner({"a"}))
    assert rec["pass_rate"] == 0.5
    assert rec["per_eval"] == {"a": True, "b": False}


def test_run_trend_no_specs_is_best_effort():
    # no specs on disk -> best-effort error record, no raise
    rec = et.run_trend(agent_runner=_runner(set()))
    assert rec.get("error")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `scripts/run_tests.sh tests/agent/test_eval_trend.py`
Expected: FAIL — `ModuleNotFoundError: No module named 'agent.eval_trend'`.

- [ ] **Step 3: Write the implementation**

```python
# agent/eval_trend.py
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `scripts/run_tests.sh tests/agent/test_eval_trend.py`
Expected: PASS (3 passed).

- [ ] **Step 5: Commit**

```bash
git add agent/eval_trend.py tests/agent/test_eval_trend.py
git commit -m "feat(evals): longitudinal run_trend with pass-rate learning-curve storage"
```

---

## Task 4: eval_trend — learning_curve (flip detection)

**Files:**
- Modify: `agent/eval_trend.py`
- Test: `tests/agent/test_eval_trend.py` (add cases)

- [ ] **Step 1: Write the failing test**

```python
# append to tests/agent/test_eval_trend.py

def test_learning_curve_detects_flips():
    s = _specs()
    et.run_trend(specs=s, agent_runner=_runner({"a"}))       # b fails
    et.run_trend(specs=s, agent_runner=_runner({"a", "b"}))  # b now passes
    curve = et.learning_curve()
    assert len(curve["points"]) == 2
    assert curve["learned"] == ["b"]      # fail -> pass
    assert curve["regressed"] == []


def test_learning_curve_detects_regression():
    s = _specs()
    et.run_trend(specs=s, agent_runner=_runner({"a", "b"}))
    et.run_trend(specs=s, agent_runner=_runner({"a"}))       # b regressed
    curve = et.learning_curve()
    assert curve["regressed"] == ["b"]
    assert curve["learned"] == []


def test_learning_curve_empty():
    assert et.learning_curve()["points"] == []
```

- [ ] **Step 2: Run test to verify it fails**

Run: `scripts/run_tests.sh tests/agent/test_eval_trend.py`
Expected: FAIL — `AttributeError: module 'agent.eval_trend' has no attribute 'learning_curve'`.

- [ ] **Step 3: Add `learning_curve` to `agent/eval_trend.py`**

```python
def learning_curve(window: Optional[int] = None) -> Dict[str, Any]:
    """Pass-rate time series for the current suite version + which evals flipped.

    Only points sharing the latest ``suite_hash`` are compared, so adding/editing
    evals never creates phantom regressions. ``learned`` = evals that went
    fail→pass between the first and latest point; ``regressed`` = pass→fail.
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `scripts/run_tests.sh tests/agent/test_eval_trend.py`
Expected: PASS (6 passed).

- [ ] **Step 5: Commit**

```bash
git add agent/eval_trend.py tests/agent/test_eval_trend.py
git commit -m "feat(evals): learning_curve with fail<->pass flip detection, suite-hash gated"
```

---

## Task 5: eval_trend — compare_feature (A/B gate)

Run the suite with a feature flag forced ON vs OFF (via the env override from Task 2) and report the pass-rate delta. This is the admission gate for inference-time learning features.

**Files:**
- Modify: `agent/eval_trend.py`
- Test: `tests/agent/test_eval_trend.py` (add cases)

- [ ] **Step 1: Write the failing test**

```python
# append to tests/agent/test_eval_trend.py
import os


def test_compare_feature_reports_delta():
    s = _specs()

    def flag_sensitive_runner(spec):
        # 'b' only passes when the feature env override is ON
        on = os.environ.get("JANUS_FLAG_MEMORY__WRITE_TIME_RECONCILE") == "1"
        passing = {"a", "b"} if on else {"a"}
        text = spec.checks[0]["value"] if spec.name in passing else ""
        return {"final_response": text, "messages": []}

    out = et.compare_feature(
        "memory.write_time_reconcile", specs=s, agent_runner=flag_sensitive_runner
    )
    assert out["pass_rate_on"] == 1.0
    assert out["pass_rate_off"] == 0.5
    assert out["delta"] == 0.5
    assert out["per_eval_delta"]["b"] == 1   # b flipped off->on


def test_compare_feature_restores_env(monkeypatch):
    monkeypatch.setenv("JANUS_FLAG_MEMORY__WRITE_TIME_RECONCILE", "preset")
    et.compare_feature(
        "memory.write_time_reconcile", specs=_specs(),
        agent_runner=_runner({"a"}),
    )
    # the original env value is restored after the comparison
    assert os.environ["JANUS_FLAG_MEMORY__WRITE_TIME_RECONCILE"] == "preset"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `scripts/run_tests.sh tests/agent/test_eval_trend.py`
Expected: FAIL — `AttributeError: ... has no attribute 'compare_feature'`.

- [ ] **Step 3: Add `compare_feature` to `agent/eval_trend.py`**

```python
import os


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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `scripts/run_tests.sh tests/agent/test_eval_trend.py`
Expected: PASS (8 passed).

- [ ] **Step 5: Commit**

```bash
git add agent/eval_trend.py tests/agent/test_eval_trend.py
git commit -m "feat(evals): compare_feature A/B gate (flag ON vs OFF pass-rate delta)"
```

---

## Task 6: eval_trend — maybe_run_trend (schedule gate)

**Files:**
- Modify: `agent/eval_trend.py`
- Test: `tests/agent/test_eval_trend.py` (add cases)

- [ ] **Step 1: Write the failing test**

```python
# append to tests/agent/test_eval_trend.py
import yaml
from janus_constants import get_janus_home


def _enable_trend(interval_hours=24):
    home = get_janus_home()
    home.mkdir(parents=True, exist_ok=True)
    (home / "config.yaml").write_text(
        yaml.safe_dump({"evals": {"trend": {"enabled": True, "interval_hours": interval_hours}}}),
        encoding="utf-8",
    )


def test_maybe_run_trend_skips_when_disabled():
    assert et.maybe_run_trend(agent_runner=_runner({"a"})) is None


def test_maybe_run_trend_runs_when_due_then_skips():
    _enable_trend()
    # write specs to disk so load_eval_specs finds them
    from agent.evals import evals_dir
    d = evals_dir(); d.mkdir(parents=True, exist_ok=True)
    (d / "s.yaml").write_text(
        "name: a\nprompt: p\nchecks:\n  - type: contains\n    value: x\n", encoding="utf-8"
    )
    first = et.maybe_run_trend(agent_runner=lambda spec: {"final_response": "x", "messages": []})
    assert first is not None and first.get("pass_rate") == 1.0
    # second call immediately after is not yet due
    assert et.maybe_run_trend(agent_runner=lambda spec: {"final_response": "x", "messages": []}) is None
```

- [ ] **Step 2: Run test to verify it fails**

Run: `scripts/run_tests.sh tests/agent/test_eval_trend.py`
Expected: FAIL — `... has no attribute 'maybe_run_trend'`.

- [ ] **Step 3: Add scheduling to `agent/eval_trend.py`**

```python
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
        from janus_cli.config import load_config  # interval read tolerant of absence
        interval = 24
        try:
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
```

> Note: if `janus_cli.config.load_config` is not importable in this context, the `try/except` falls back to a 24h interval — acceptable, the flag still gates execution.

- [ ] **Step 4: Run test to verify it passes**

Run: `scripts/run_tests.sh tests/agent/test_eval_trend.py`
Expected: PASS (10 passed).

- [ ] **Step 5: Commit**

```bash
git add agent/eval_trend.py tests/agent/test_eval_trend.py
git commit -m "feat(evals): maybe_run_trend scheduled runner (interval-gated, best-effort)"
```

---

## Task 7: eval_miner — failure → draft regression-pin

**Files:**
- Create: `agent/eval_miner.py`
- Test: `tests/agent/test_eval_miner.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/agent/test_eval_miner.py
"""Failure -> quarantined draft regression-pin eval."""
from types import SimpleNamespace

import yaml

from agent import eval_miner as em
from agent.evals import evals_dir


def _fake_llm(reply):
    def _caller(**kwargs):
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=reply))])
    return _caller


_MSGS = [
    {"role": "user", "content": "What test runner does this project use?"},
    {"role": "assistant", "content": "I think it's unittest."},  # wrong -> failed
]


def test_draft_eval_from_failure_parses_spec():
    reply = (
        '{"name": "knows-test-runner", "prompt": "What test runner does this '
        'project use?", "checks": [{"type": "contains", "value": "pytest"}]}'
    )
    spec = em.draft_eval_from_failure(_MSGS, lesson="Project uses pytest.", llm_caller=_fake_llm(reply))
    assert spec is not None
    assert spec.name == "knows-test-runner"
    assert spec.checks == [{"type": "contains", "value": "pytest"}]


def test_draft_rejects_unknown_check_type():
    reply = '{"name": "x", "prompt": "p", "checks": [{"type": "vibes", "value": "z"}]}'
    assert em.draft_eval_from_failure(_MSGS, llm_caller=_fake_llm(reply)) is None


def test_write_eval_draft_quarantines_yaml():
    spec = em.draft_eval_from_failure(
        _MSGS,
        llm_caller=_fake_llm('{"name": "n", "prompt": "p", "checks": [{"type": "contains", "value": "pytest"}]}'),
    )
    path = em.write_eval_draft(spec)
    assert path.parent == evals_dir() / ".drafts"
    loaded = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert loaded["name"] == "n" and loaded["checks"][0]["value"] == "pytest"


def test_garbage_reply_returns_none():
    assert em.draft_eval_from_failure(_MSGS, llm_caller=_fake_llm("not json")) is None
```

- [ ] **Step 2: Run test to verify it fails**

Run: `scripts/run_tests.sh tests/agent/test_eval_miner.py`
Expected: FAIL — `ModuleNotFoundError: No module named 'agent.eval_miner'`.

- [ ] **Step 3: Write the implementation**

```python
# agent/eval_miner.py
"""Failure -> draft regression-pin eval (the self-growing benchmark).

When a session is classified a failure and a lesson is distilled, also draft a
deterministic eval that pins the behavior the agent should exhibit next time.
Drafts are quarantined in $JANUS_HOME/evals/.drafts/ (NOT the live suite) for
user review — so the agent can never inflate its own learning curve.

Reuses agent/evals.py's EvalSpec + check-type validation. Best-effort,
injectable llm_caller; never raises.
"""
from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)

_SYSTEM = (
    "You write a single regression test for an AI agent that just FAILED a task. "
    "Produce a deterministic eval: a prompt that recreates the situation and "
    "checks that would PASS only if the agent now behaves correctly. Use only "
    "deterministic checks (string/tool presence), never subjective judgment."
)


def _build_prompt(transcript: str, lesson: str) -> str:
    return (
        "From this failed session" + (f" and its lesson ({lesson})" if lesson else "") +
        ", write ONE eval as JSON:\n"
        '  {"name": "<kebab-case-id>", "prompt": "<prompt that recreates the '
        'task>", "checks": [{"type": "<contains|not_contains|regex|tool_called|'
        'tool_not_called|min_length|max_length>", "value": "<value>"}]}\n'
        "Return ONLY the JSON object.\n\nSESSION:\n" + transcript
    )


def _drafts_dir() -> Path:
    from agent.evals import evals_dir
    return evals_dir() / ".drafts"


def _slug(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", str(name).strip().lower()).strip("-")
    return s or "regression-pin"


def draft_eval_from_failure(
    messages: List[Dict[str, Any]], *, lesson: str = "",
    llm_caller: Optional[Callable[..., Any]] = None,
    provider: Optional[str] = None, model: Optional[str] = None,
):
    """Draft an EvalSpec pinning correct behavior. None if nothing valid. Best-effort."""
    try:
        from agent.evals import _spec_from_dict
        from agent.memory_miner import _render_transcript
        transcript = _render_transcript(messages, max_chars=6000)
        if not transcript.strip():
            return None
        if llm_caller is None:
            from agent.auxiliary_client import call_llm as llm_caller
        resp = llm_caller(
            task="eval_pin", provider=provider, model=model,
            messages=[{"role": "system", "content": _SYSTEM},
                      {"role": "user", "content": _build_prompt(transcript, lesson)}],
            temperature=0, max_tokens=300,
        )
        raw = resp.choices[0].message.content or ""
        m = re.search(r"\{.*\}", raw, re.DOTALL)
        if not m:
            return None
        data = json.loads(m.group(0))
        data["name"] = _slug(data.get("name", ""))
        return _spec_from_dict(data, source_file="(draft)")  # validates checks
    except Exception as exc:
        logger.debug("eval pin draft failed: %s", exc)
        return None


def write_eval_draft(spec, drafts_dir: Optional[Path] = None) -> Path:
    """Write the spec as quarantined YAML in evals/.drafts/ (auto-suffix on clash)."""
    import yaml
    drafts_dir = drafts_dir or _drafts_dir()
    drafts_dir.mkdir(parents=True, exist_ok=True)
    base = spec.name
    target = drafts_dir / f"{base}.yaml"
    n = 2
    while target.exists():
        target = drafts_dir / f"{base}-{n}.yaml"
        n += 1
    target.write_text(
        yaml.safe_dump({"name": spec.name, "prompt": spec.prompt, "checks": spec.checks},
                       sort_keys=False),
        encoding="utf-8",
    )
    return target
```

> The live suite is unaffected: `load_eval_specs` globs `*.yaml` in `evals/` non-recursively, so files under `evals/.drafts/` are never loaded until a human moves them up.

- [ ] **Step 4: Run test to verify it passes**

Run: `scripts/run_tests.sh tests/agent/test_eval_miner.py`
Expected: PASS (4 passed).

- [ ] **Step 5: Commit**

```bash
git add agent/eval_miner.py tests/agent/test_eval_miner.py
git commit -m "feat(evals): eval_miner — quarantined regression-pin drafts from failures"
```

---

## Task 8: Wire eval_miner into auto_mine (autopin)

**Files:**
- Modify: `agent/auto_mine.py` (inside the `if verdict is False ...` block added in Tier 1)
- Test: `tests/agent/test_eval_miner.py` (add a wiring case)

- [ ] **Step 1: Write the failing test**

```python
# append to tests/agent/test_eval_miner.py
def test_autopin_writes_draft_on_failure(monkeypatch):
    import yaml as _yaml
    from janus_constants import get_janus_home
    from agent import auto_mine, outcome_tracker

    home = get_janus_home(); home.mkdir(parents=True, exist_ok=True)
    (home / "config.yaml").write_text(
        _yaml.safe_dump({"learning": {"track_outcomes": True, "reflexion": True},
                         "evals": {"autopin": True}}),
        encoding="utf-8",
    )
    monkeypatch.setattr(outcome_tracker, "classify_session", lambda *a, **k: False)
    monkeypatch.setattr("agent.lessons.reflect_on_failure", lambda *a, **k: {"task_type": "t", "lesson": "Use pytest."})
    spec = em.draft_eval_from_failure(
        _MSGS, llm_caller=_fake_llm('{"name": "p", "prompt": "p", "checks": [{"type": "contains", "value": "pytest"}]}'))
    monkeypatch.setattr(em, "draft_eval_from_failure", lambda *a, **k: spec)

    msgs = [{"role": "user", "content": "q", "session_id": "s1"},
            {"role": "assistant", "content": "a"}] * 3
    auto_mine.maybe_automine(msgs, run_in_thread=False)

    drafts = list((evals_dir() / ".drafts").glob("*.yaml"))
    assert drafts, "a regression-pin draft should have been written"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `scripts/run_tests.sh tests/agent/test_eval_miner.py::test_autopin_writes_draft_on_failure`
Expected: FAIL — no draft written (autopin not wired).

- [ ] **Step 3: Wire it into `agent/auto_mine.py`**

Inside the `if verdict is False and _flag("learning", "reflexion", default=True):` block (added in Tier 1), after the `record_lesson(...)` call, extend the body so it reads:

```python
                        if verdict is False and _flag("learning", "reflexion", default=True):
                            try:
                                from agent.lessons import reflect_on_failure, record_lesson
                                r = reflect_on_failure(snapshot)
                                if r:
                                    record_lesson(r["lesson"], task_type=r.get("task_type", ""),
                                                  session_id=session_id)
                                # Self-growing benchmark: draft a quarantined
                                # regression-pin eval from the same failure.
                                if _flag("evals", "autopin", default=False):
                                    from agent.eval_miner import (
                                        draft_eval_from_failure, write_eval_draft,
                                    )
                                    spec = draft_eval_from_failure(
                                        snapshot, lesson=(r or {}).get("lesson", ""))
                                    if spec:
                                        write_eval_draft(spec)
                            except Exception as exc:
                                logger.debug("reflexion/autopin write-back failed: %s", exc)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `scripts/run_tests.sh tests/agent/test_eval_miner.py`
Expected: PASS (5 passed).

- [ ] **Step 5: Commit**

```bash
git add agent/auto_mine.py tests/agent/test_eval_miner.py
git commit -m "feat(evals): autopin — draft a regression-pin from each classified failure"
```

---

## Task 9: memory_gardener — reconcile_candidate (ADD/UPDATE/DELETE/NOOP)

**Files:**
- Modify: `agent/memory_gardener.py`
- Test: `tests/agent/test_memory_reconcile.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/agent/test_memory_reconcile.py
"""Per-candidate write-time reconciliation decision."""
from types import SimpleNamespace

from agent import memory_gardener as mg


def _fake_llm(reply):
    def _caller(**kwargs):
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=reply))])
    return _caller


_EXISTING = ["User is on Python 3.11.", "Deploy script is scripts/deploy.sh."]


def test_add_new_fact():
    d = mg.reconcile_candidate("User prefers dark mode.", _EXISTING, llm_caller=_fake_llm('{"action": "ADD"}'))
    assert d["action"] == "ADD"


def test_update_supersedes():
    d = mg.reconcile_candidate(
        "User is on Python 3.12.", _EXISTING,
        llm_caller=_fake_llm('{"action": "UPDATE", "target_index": 0}'))
    assert d["action"] == "UPDATE" and d["target_index"] == 0


def test_delete_contradiction():
    d = mg.reconcile_candidate(
        "Deploy is now via CI, no script.", _EXISTING,
        llm_caller=_fake_llm('{"action": "DELETE", "target_index": 1}'))
    assert d["action"] == "DELETE" and d["target_index"] == 1


def test_noop_already_known():
    d = mg.reconcile_candidate("User is on Python 3.11.", _EXISTING,
                               llm_caller=_fake_llm('{"action": "NOOP"}'))
    assert d["action"] == "NOOP"


def test_bad_index_falls_back_to_add():
    d = mg.reconcile_candidate("x", _EXISTING,
                               llm_caller=_fake_llm('{"action": "UPDATE", "target_index": 99}'))
    assert d["action"] == "ADD"   # out-of-range target is unsafe -> ADD


def test_garbage_reply_falls_back_to_add():
    d = mg.reconcile_candidate("x", _EXISTING, llm_caller=_fake_llm("nonsense"))
    assert d["action"] == "ADD"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `scripts/run_tests.sh tests/agent/test_memory_reconcile.py`
Expected: FAIL — `AttributeError: module 'agent.memory_gardener' has no attribute 'reconcile_candidate'`.

- [ ] **Step 3: Add `reconcile_candidate` to `agent/memory_gardener.py`**

```python
_RECONCILE_SYSTEM = (
    "You decide how a NEW candidate memory fact relates to EXISTING memory. "
    "Choose exactly one action: ADD (genuinely new), UPDATE (supersedes a "
    "specific existing fact — give its index), DELETE (directly contradicts a "
    "specific existing fact, which should be removed — give its index), or NOOP "
    "(already covered by existing memory). Be conservative."
)


def _reconcile_prompt(candidate: str, existing: List[str]) -> str:
    numbered = "\n".join(f"[{i}] {e}" for i, e in enumerate(existing)) or "(none)"
    return (
        f"EXISTING:\n{numbered}\n\nCANDIDATE:\n{candidate}\n\n"
        'Return ONLY JSON: {"action": "ADD|UPDATE|DELETE|NOOP", "target_index": '
        '<int, required for UPDATE/DELETE>}.'
    )


def reconcile_candidate(
    candidate: str, existing: List[str], *,
    llm_caller: Optional[Callable[..., Any]] = None,
    provider: Optional[str] = None, model: Optional[str] = None,
) -> Dict[str, Any]:
    """Classify a candidate fact vs existing memory. Always returns a safe dict.

    ``{"action": "ADD"|"UPDATE"|"DELETE"|"NOOP", "target_index": int|None}``.
    Any error or out-of-range index degrades to ``ADD`` (never destructive on
    bad input). Best-effort; never raises.
    """
    safe = {"action": "ADD", "target_index": None}
    try:
        if not existing:
            return safe
        if llm_caller is None:
            from agent.auxiliary_client import call_llm as llm_caller
        resp = llm_caller(
            task="memory_reconcile_candidate", provider=provider, model=model,
            messages=[{"role": "system", "content": _RECONCILE_SYSTEM},
                      {"role": "user", "content": _reconcile_prompt(candidate, existing)}],
            temperature=0, max_tokens=60,
        )
        raw = resp.choices[0].message.content or ""
        m = re.search(r"\{.*\}", raw, re.DOTALL)
        if not m:
            return safe
        data = json.loads(m.group(0))
        action = str(data.get("action", "")).strip().upper()
        if action not in {"ADD", "UPDATE", "DELETE", "NOOP"}:
            return safe
        if action in {"UPDATE", "DELETE"}:
            try:
                idx = int(data.get("target_index"))
            except (TypeError, ValueError):
                return safe
            if not (0 <= idx < len(existing)):
                return safe   # unsafe index -> ADD
            return {"action": action, "target_index": idx}
        return {"action": action, "target_index": None}
    except Exception as exc:
        logger.debug("reconcile_candidate failed: %s", exc)
        return safe
```

- [ ] **Step 4: Run test to verify it passes**

Run: `scripts/run_tests.sh tests/agent/test_memory_reconcile.py`
Expected: PASS (6 passed).

- [ ] **Step 5: Commit**

```bash
git add agent/memory_gardener.py tests/agent/test_memory_reconcile.py
git commit -m "feat(memory): reconcile_candidate — ADD/UPDATE/DELETE/NOOP decision (safe fallback to ADD)"
```

---

## Task 10: Integrate write-time reconciliation into mine_session_memory

**Files:**
- Modify: `agent/memory_miner.py:203-217` (the per-fact write loop)
- Test: `tests/agent/test_memory_reconcile.py` (add an integration case)

- [ ] **Step 1: Write the failing test**

```python
# append to tests/agent/test_memory_reconcile.py
from agent import memory_miner as mm
from tools.memory_tool import MemoryStore


def test_write_time_update_replaces_stale(monkeypatch):
    import yaml
    from janus_constants import get_janus_home
    home = get_janus_home(); home.mkdir(parents=True, exist_ok=True)
    (home / "config.yaml").write_text(
        yaml.safe_dump({"memory": {"write_time_reconcile": True}}), encoding="utf-8")

    store = MemoryStore(); store.load_from_disk()
    store.add("memory", "User is on Python 3.11.")

    # miner extracts the new fact; reconcile says UPDATE index 0
    monkeypatch.setattr(mm, "_parse_facts", lambda raw: {"user": [], "memory": ["User is on Python 3.12."]})
    monkeypatch.setattr(
        "agent.memory_gardener.reconcile_candidate",
        lambda cand, existing, **k: {"action": "UPDATE", "target_index": 0},
    )
    msgs = [{"role": "user", "content": "I upgraded to Python 3.12"},
            {"role": "assistant", "content": "noted"}]
    mm.mine_session_memory(msgs, store, llm_caller=_fake_llm("{}"))

    assert "User is on Python 3.12." in store.memory_entries
    assert "User is on Python 3.11." not in store.memory_entries  # stale replaced
```

- [ ] **Step 2: Run test to verify it fails**

Run: `scripts/run_tests.sh tests/agent/test_memory_reconcile.py::test_write_time_update_replaces_stale`
Expected: FAIL — both facts present (append-only path still active).

- [ ] **Step 3: Modify the write loop in `agent/memory_miner.py`**

Replace the per-fact loop (the `for target in ("user", "memory"):` block, lines ~203-217) with:

```python
        from agent.feature_flags import flag_enabled
        reconcile_on = flag_enabled("memory", "write_time_reconcile", default=False)

        for target in ("user", "memory"):
            live = list(getattr(memory_store, f"{target}_entries", []))
            for content in facts.get(target, [])[:max_facts_per_target]:
                content = content.strip()
                if not content:
                    continue
                if _is_duplicate(content, existing[target]):
                    result["skipped_duplicates"] += 1
                    continue

                if reconcile_on and live:
                    from agent.memory_gardener import reconcile_candidate
                    decision = reconcile_candidate(content, live, llm_caller=llm_caller,
                                                   provider=provider, model=model)
                    action = decision["action"]
                    idx = decision.get("target_index")
                    if action == "NOOP":
                        result["skipped_duplicates"] += 1
                        continue
                    if action in ("UPDATE", "DELETE") and idx is not None and 0 <= idx < len(live):
                        old = live[idx]
                        try:
                            memory_store.remove(target, old)
                        except Exception as exc:
                            logger.debug("reconcile remove failed: %s", exc)
                        live.pop(idx)
                        result.setdefault("reconciled", {"updated": 0, "deleted": 0})
                        if action == "DELETE":
                            result["reconciled"]["deleted"] += 1
                            existing[target] = [e for e in existing[target] if e != _normalize(old)]
                            # DELETE removes the contradicting old fact AND skips
                            # adding the candidate (it only signalled the conflict)
                            continue
                        result["reconciled"]["updated"] += 1
                        existing[target] = [e for e in existing[target] if e != _normalize(old)]
                    # UPDATE and ADD both fall through to the add below

                add_result = memory_store.add(target, content)
                if isinstance(add_result, dict) and add_result.get("success"):
                    result["added"][target] += 1
                    existing[target].append(_normalize(content))
                    live.append(content)
                else:
                    result["skipped_duplicates"] += 1
```

> `MemoryStore.remove(target, text)` removes by exact entry text (verified in `tools/memory_tool.py`); the dated journal preserves history, so reconciliation is non-destructive to the audit trail.

- [ ] **Step 4: Run test to verify it passes**

Run: `scripts/run_tests.sh tests/agent/test_memory_reconcile.py tests/agent/test_memory_miner.py`
Expected: PASS — new integration test passes; existing memory-miner tests still green (reconcile is off by default).

- [ ] **Step 5: Commit**

```bash
git add agent/memory_miner.py tests/agent/test_memory_reconcile.py
git commit -m "feat(memory): apply write-time ADD/UPDATE/DELETE/NOOP in mine_session_memory (gated)"
```

---

## Task 11: CLI — `janus evals trend` and `janus evals ab`

**Files:**
- Modify: `janus_cli/evals.py` (add `_cmd_trend`, `_cmd_ab`, and register both in `register_cli`)
- Test: `tests/janus_cli/test_evals_cli_trend.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/janus_cli/test_evals_cli_trend.py
"""`janus evals trend` records a curve point and prints it."""
import argparse

from janus_cli import evals as ev
from agent.evals import evals_dir
from agent import eval_trend as et


def _setup_specs():
    d = evals_dir(); d.mkdir(parents=True, exist_ok=True)
    (d / "s.yaml").write_text(
        "name: a\nprompt: p\nchecks:\n  - type: contains\n    value: x\n", encoding="utf-8")


def test_register_adds_trend_and_ab():
    parent = argparse.ArgumentParser()
    ev.register_cli(parent)
    # parsing the subcommands should not error
    ns = parent.parse_args(["trend"])
    assert hasattr(ns, "func")
    ns2 = parent.parse_args(["ab", "memory.write_time_reconcile"])
    assert ns2.flag == "memory.write_time_reconcile"


def test_cmd_trend_runs(monkeypatch, capsys):
    _setup_specs()
    monkeypatch.setattr(et, "run_trend",
                        lambda **k: {"pass_rate": 1.0, "total": 1, "passed": 1,
                                     "per_eval": {"a": True}, "suite_hash": "h"})
    args = argparse.Namespace(path=None)
    rc = ev._cmd_trend(args)
    assert rc == 0
    assert "pass_rate" in capsys.readouterr().out
```

- [ ] **Step 2: Run test to verify it fails**

Run: `scripts/run_tests.sh tests/janus_cli/test_evals_cli_trend.py`
Expected: FAIL — `AttributeError: module 'janus_cli.evals' has no attribute '_cmd_trend'`.

- [ ] **Step 3: Add the subcommands to `janus_cli/evals.py`**

Add these functions before `register_cli`:

```python
def _cmd_trend(args) -> int:
    from agent import eval_trend as et

    rec = et.run_trend(path=_resolve_path(args))
    if rec.get("error"):
        print(f"evals: trend run failed — {rec['error']}", file=sys.stderr)
        return 1
    print(f"trend point: pass_rate={rec['pass_rate']} "
          f"({rec['passed']}/{rec['total']}) suite={rec['suite_hash']}")
    curve = et.learning_curve()
    if curve["learned"]:
        print(f"  learned since first run: {', '.join(curve['learned'])}")
    if curve["regressed"]:
        print(f"  REGRESSED since first run: {', '.join(curve['regressed'])}")
    return 0


def _cmd_ab(args) -> int:
    from agent import eval_trend as et

    out = et.compare_feature(args.flag, path=_resolve_path(args))
    if out.get("error"):
        print(f"evals: ab failed — {out['error']}", file=sys.stderr)
        return 1
    print(f"A/B {out['flag']}: ON={out['pass_rate_on']} OFF={out['pass_rate_off']} "
          f"delta={out['delta']:+.4f}")
    return 0
```

Inside `register_cli`, after the existing `p_results` block, add:

```python
    p_trend = subs.add_parser("trend", help="Run the suite and record a learning-curve point")
    p_trend.add_argument("--path", help="Spec file or directory (default $JANUS_HOME/evals/)")
    p_trend.set_defaults(func=_cmd_trend)

    p_ab = subs.add_parser("ab", help="A/B a feature flag: suite pass-rate ON vs OFF")
    p_ab.add_argument("flag", help="section.key flag, e.g. memory.write_time_reconcile")
    p_ab.add_argument("--path", help="Spec file or directory (default $JANUS_HOME/evals/)")
    p_ab.set_defaults(func=_cmd_ab)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `scripts/run_tests.sh tests/janus_cli/test_evals_cli_trend.py`
Expected: PASS (2 passed).

- [ ] **Step 5: Commit**

```bash
git add janus_cli/evals.py tests/janus_cli/test_evals_cli_trend.py
git commit -m "feat(cli): janus evals trend (learning curve) + ab (feature A/B)"
```

---

## Task 12: Dashboard — learning curve in the learning router + LearningPage

**Files:**
- Modify: `janus_cli/routers/learning.py` (the `/api/learning/stats` handler — add a `curve` block)
- Modify: `web/src/pages/LearningPage.tsx` (render the curve)
- Test: `tests/janus_cli/test_dashboard_learning_endpoints.py` (add a case)

- [ ] **Step 1: Write the failing test**

```python
# append a test to tests/janus_cli/test_dashboard_learning_endpoints.py
def test_learning_stats_includes_curve(client):
    # client fixture = starlette TestClient with the auth header (see existing tests)
    r = client.get("/api/learning/stats", headers=AUTH)
    assert r.status_code == 200
    body = r.json()
    assert "curve" in body
    assert "points" in body["curve"]
    assert "draft_pins" in body["curve"]
```

> Use the same `client` fixture and `AUTH` header constant the existing tests in this file already define.

- [ ] **Step 2: Run test to verify it fails**

Run: `scripts/run_tests.sh tests/janus_cli/test_dashboard_learning_endpoints.py::test_learning_stats_includes_curve`
Expected: FAIL — `KeyError: 'curve'`.

- [ ] **Step 3: Extend the handler in `janus_cli/routers/learning.py`**

In the `get_learning_stats` handler, before the `return {...}`, add:

```python
        try:
            from agent import eval_trend as _et
            from agent.evals import evals_dir as _evals_dir
            curve = _et.learning_curve()
            drafts = list((_evals_dir() / ".drafts").glob("*.yaml"))
            curve["draft_pins"] = len(drafts)
        except Exception:
            curve = {"points": [], "learned": [], "regressed": [], "draft_pins": 0}
```

and add `"curve": curve,` to the returned dict.

- [ ] **Step 4: Run test to verify it passes**

Run: `scripts/run_tests.sh tests/janus_cli/test_dashboard_learning_endpoints.py`
Expected: PASS (all green).

- [ ] **Step 5: Render the curve in `web/src/pages/LearningPage.tsx`**

Extend the `LearningStats` interface:

```tsx
interface LearningCurve {
  points: { ts: string; pass_rate: number | null }[];
  learned: string[];
  regressed: string[];
  draft_pins: number;
}
// add to LearningStats:
//   curve?: LearningCurve;
```

Add a card after the "Continual-learning health" card:

```tsx
{stats?.curve && stats.curve.points.length > 0 && (
  <Card>
    <CardContent className="space-y-2 p-4">
      <div className="flex items-center gap-2 text-sm font-medium text-muted-foreground">
        <TrendingUp className="h-4 w-4" /> Learning curve (eval pass-rate)
      </div>
      <div className="text-sm">
        latest:{" "}
        <strong>{pct(stats.curve.points[stats.curve.points.length - 1].pass_rate)}</strong>
        <span className="ml-2 text-muted-foreground">
          over {stats.curve.points.length} runs
        </span>
      </div>
      {stats.curve.learned.length > 0 && (
        <div className="text-xs text-emerald-500">learned: {stats.curve.learned.join(", ")}</div>
      )}
      {stats.curve.regressed.length > 0 && (
        <div className="text-xs text-rose-500">regressed: {stats.curve.regressed.join(", ")}</div>
      )}
      {stats.curve.draft_pins > 0 && (
        <div className="text-xs text-muted-foreground">
          {stats.curve.draft_pins} regression-pin draft(s) awaiting review in evals/.drafts/
        </div>
      )}
    </CardContent>
  </Card>
)}
```

- [ ] **Step 6: Commit**

```bash
git add janus_cli/routers/learning.py web/src/pages/LearningPage.tsx tests/janus_cli/test_dashboard_learning_endpoints.py
git commit -m "feat(dashboard): learning-curve card (pass-rate over time + flips + draft pins)"
```

---

## Task 13: Wire maybe_run_trend into the gateway cron

**Files:**
- Modify: `gateway/runner.py:17832-17833` (next to the `maybe_run_sleep` call)
- Test: `tests/agent/test_eval_trend.py` (the scheduling behavior is already covered by Task 6; this task is a one-line wiring + a smoke import check)

- [ ] **Step 1: Add the call in `gateway/runner.py`**

Immediately after the existing:

```python
                from agent.sleep import maybe_run_sleep
                maybe_run_sleep(idle_for_seconds=float("inf"))
```

add:

```python
                from agent.eval_trend import maybe_run_trend
                maybe_run_trend()
```

- [ ] **Step 2: Smoke-test the import path**

Run: `scripts/run_tests.sh tests/agent/test_eval_trend.py`
Expected: PASS (all trend tests, including scheduling, still green).

- [ ] **Step 3: Verify the gateway module imports cleanly**

Run: `python -c "import gateway.runner"`
Expected: no error.

- [ ] **Step 4: Commit**

```bash
git add gateway/runner.py
git commit -m "feat(gateway): run the eval trend on the cron tick (interval-gated)"
```

---

## Final verification (after all tasks)

- [ ] **Full affected-suite run**

```bash
scripts/run_tests.sh tests/agent/test_eval_trend.py tests/agent/test_eval_miner.py \
  tests/agent/test_memory_reconcile.py tests/agent/test_memory_miner.py \
  tests/agent/test_feature_flags.py tests/agent/test_auto_mine.py \
  tests/janus_cli/test_evals_cli_trend.py tests/janus_cli/test_dashboard_learning_endpoints.py \
  tests/janus_cli/test_config_learning_keys.py
```
Expected: all PASS.

- [ ] **Lint the changed Python**

```bash
ruff check agent/eval_trend.py agent/eval_miner.py agent/feature_flags.py \
  agent/memory_gardener.py agent/memory_miner.py agent/auto_mine.py janus_cli/evals.py
```
Expected: `All checks passed!`

- [ ] **Scaffold + smoke the new CLI end-to-end** (optional manual check)

```bash
python run_agent.py >/dev/null 2>&1 || true   # ensure import graph is intact
janus evals init        # writes starter specs
janus evals trend       # records the first learning-curve point
janus evals ab memory.write_time_reconcile   # prints an ON/OFF delta
```

---

## Self-review notes (author)

- **Spec coverage:** Component 1 (Tasks 3,4,6,13) · Component 2 (Tasks 7,8) · Component 3 (Tasks 2,5) · Component 4 (Tasks 9,10) · Component 5 (Task 12) · config (Task 1) · CLI (Task 11). All spec sections map to a task.
- **Write-time A/B caveat honored:** `compare_feature` is the generic inference-time gate; write-time reconciliation is proven by the Task 10 integration test (UPDATE replaces stale), matching the spec's two-flag-class note.
- **Type/name consistency:** `run_trend`/`learning_curve`/`compare_feature`/`maybe_run_trend` names are used identically across Tasks 3–6, 11, 12, 13; `reconcile_candidate` signature is identical in Tasks 9 and 10; `flag_enabled(section, key, *, default)` identical in Tasks 2, 6, 10.
- **No placeholders:** every code step shows complete code; every run step shows the exact command + expected result.
