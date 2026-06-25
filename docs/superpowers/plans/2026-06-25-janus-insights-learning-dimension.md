# Janus Insights — Learning Dimension Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a measurable "is the learning loop working?" dimension to the existing `janus insights` surface — eval pass-rate trend, session success rate, mining yield, and knowledge-base/draft-backlog counts — rendered to terminal and exported as `--json`.

**Architecture:** A new pure module `agent/learning_insights.py` reads the file-based learning stores (eval trend, outcomes, lessons, playbook, skill drafts) and returns a report dict, formatted to terminal/gateway text and composed into the three existing `insights` handlers via a shared `render_insights()` dispatcher. One additive, guarded write in `agent/sleep.py` (`learning/sleep_log.jsonl`) turns mining yield from a point-in-time count into a trend. The SQLite-bound `InsightsEngine` is left untouched.

**Tech Stack:** Python 3.11; stdlib `json`/`pathlib`/`datetime`; existing modules `agent/eval_trend.py`, `agent/outcome_tracker.py`, `agent/lessons.py`, `agent/playbook.py`, `agent/sleep.py`, `agent/insights.py`; pytest via `scripts/run_tests.sh`.

## Global Constraints

- **All test runs go through `scripts/run_tests.sh`** (never bare `pytest`) — it pins `TZ=UTC`/`LANG=C.UTF-8`, unsets credentials, and isolates each file. Single test: `scripts/run_tests.sh tests/agent/test_x.py::test_name`. For fast local iteration only: add `--no-isolate`.
- **`generate_learning_report` and all readers are best-effort and MUST NEVER raise** — a missing/empty/corrupt store yields an empty series, not an exception. Each metric is computed in isolation.
- **Never hardcode `~/.janus`** — read paths via the stores' own path helpers (`eval_trend.trend_path()`, `outcome_tracker.get_outcomes_path()`, etc.) and `get_janus_home()`, all of which the autouse `_isolate_janus_home` fixture redirects in tests.
- **No change-detector tests** — assert relationships/invariants (e.g. `rate == successes/total`), never fixed catalog snapshots.
- **The `sleep_log.jsonl` write is additive and guarded** — a write failure must never break the sleep cycle.
- **Every commit message ends with the trailer:** `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`.
- **Reuse existing helpers, don't recompute:** `outcome_tracker.overall_stats()`, `recent_success_rate(window=)`, `skill_stats()` already exist and are tested.

## File Structure

- **Create** `agent/learning_insights.py` — the aggregator (`generate_learning_report`), terminal/gateway formatters (`format_learning_terminal`, `format_learning_gateway`), and the unified `render_insights` dispatcher. One responsibility: turn learning stores into insights output.
- **Modify** `agent/sleep.py` — add `sleep_log_path()` + guarded `_append_sleep_log(report)`, called once per real cycle.
- **Modify** `janus_cli/main.py` (`insights_parser` + `cmd_insights`, ~16375) — add `--json`/`--learning`/`--usage` flags; compose learning report.
- **Modify** `cli.py` (`_show_insights`, ~10805) — parse the same flags from the slash string; compose.
- **Modify** `gateway/runner.py` (insights handler, ~12574) — append the compact learning block.
- **Create** `tests/agent/test_learning_insights.py` — unit tests for the aggregator, formatters, and dispatcher.
- **Modify** `tests/agent/test_sleep.py` — add the sleep-log append tests.

---

### Task 1: Persist sleep-cycle reports to `learning/sleep_log.jsonl`

**Files:**
- Modify: `agent/sleep.py` (add helpers near top; call inside `run_sleep_cycle`'s `if not dry_run:` block, ~255-260)
- Test: `tests/agent/test_sleep.py`

**Interfaces:**
- Produces: `sleep_log_path() -> Path` (returns `get_janus_home()/"learning"/"sleep_log.jsonl"`); `_append_sleep_log(report: dict) -> None` (guarded append of one JSON line `{"ts", "graduated_facts", "graduated_skills", "lessons", "pruned"}`). Consumed by Task 3.

- [ ] **Step 1: Write the failing test**

Add to `tests/agent/test_sleep.py`:

```python
def test_sleep_cycle_appends_one_sleep_log_line():
    from agent import sleep
    from tools.memory_tool import MemoryStore
    import json
    store = MemoryStore()
    sleep.run_sleep_cycle(store, llm_caller=_fake_llm("[]"))
    p = sleep.sleep_log_path()
    assert p.is_file()
    lines = [l for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
    assert len(lines) == 1
    rec = json.loads(lines[0])
    assert set(rec) >= {"ts", "graduated_facts", "graduated_skills", "lessons", "pruned"}
    assert isinstance(rec["graduated_facts"], int)


def test_sleep_dry_run_writes_no_sleep_log():
    from agent import sleep
    from tools.memory_tool import MemoryStore
    store = MemoryStore()
    sleep.run_sleep_cycle(store, llm_caller=_fake_llm("[]"), dry_run=True)
    assert not sleep.sleep_log_path().is_file()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `scripts/run_tests.sh tests/agent/test_sleep.py::test_sleep_cycle_appends_one_sleep_log_line`
Expected: FAIL with `AttributeError: module 'agent.sleep' has no attribute 'sleep_log_path'`

- [ ] **Step 3: Add the helpers to `agent/sleep.py`**

Add near the other path/state helpers (after the imports / `_now_iso`):

```python
def sleep_log_path() -> Path:
    from janus_constants import get_janus_home
    return get_janus_home() / "learning" / "sleep_log.jsonl"


def _append_sleep_log(report: Dict[str, Any]) -> None:
    """Append one line summarizing a completed (non-dry-run) cycle. Guarded."""
    try:
        rec = {
            "ts": _now_iso(),
            "graduated_facts": int(report.get("graduated_facts", 0) or 0),
            "graduated_skills": int(report.get("graduated_skills", 0) or 0),
            "lessons": len(report.get("lessons") or []),
            "pruned": len(report.get("pruned") or []),
        }
        p = sleep_log_path()
        p.parent.mkdir(parents=True, exist_ok=True)
        with p.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    except Exception as exc:  # never break the cycle over a log line
        logger.debug("sleep-log append failed: %s", exc)
```

- [ ] **Step 4: Call it in `run_sleep_cycle`**

In `agent/sleep.py`, inside the `if not dry_run:` block that saves sleep state (~255-260), add the append immediately after `save_sleep_state(state)`:

```python
        if not dry_run:
            state = load_sleep_state()
            state["last_run"] = _now_iso()
            state["last_report"] = {k: (len(v) if isinstance(v, list) else v)
                                    for k, v in report.items() if k != "error"}
            save_sleep_state(state)
            _append_sleep_log(report)   # <-- add this line
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `scripts/run_tests.sh tests/agent/test_sleep.py`
Expected: PASS (both new tests + existing sleep tests green)

- [ ] **Step 6: Commit**

```bash
git add agent/sleep.py tests/agent/test_sleep.py
git commit -m "feat(sleep): persist per-cycle mining yield to learning/sleep_log.jsonl

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 2: Aggregator — eval-trend + outcomes sections

**Files:**
- Create: `agent/learning_insights.py`
- Test: `tests/agent/test_learning_insights.py`

**Interfaces:**
- Consumes: `eval_trend.trend_path()`; `outcome_tracker.load()`, `overall_stats()`, `recent_success_rate(window=)`, `skill_stats()`.
- Produces: `generate_learning_report(days: int = 30, *, now: float | None = None) -> dict` returning at least keys `{"days", "eval", "outcomes"}`. `eval` = `{"points": [{"ts","pass_rate"}], "latest", "first", "delta", "runs", "per_eval_latest"}`. `outcomes` = `{"all_time": {"sessions","successes","success_rate"}, "windowed": {...same...}, "recent", "by_skill", "by_persona"}`. Consumed by Tasks 3, 4.

- [ ] **Step 1: Write the failing test**

Create `tests/agent/test_learning_insights.py`:

```python
"""Tests for the learning-insights aggregator (agent/learning_insights.py)."""
import json

from agent import learning_insights as li
from agent import eval_trend, outcome_tracker as ot


def _write_trend(records):
    p = eval_trend.trend_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("".join(json.dumps(r) + "\n" for r in records), encoding="utf-8")


def test_eval_section_trend_and_delta():
    _write_trend([
        {"ts": "2026-06-01T00:00:00", "pass_rate": 0.6, "passed": 6, "total": 10,
         "per_eval": {"a": True, "b": False}},
        {"ts": "2026-06-02T00:00:00", "pass_rate": 0.9, "passed": 9, "total": 10,
         "per_eval": {"a": True, "b": True}},
    ])
    rep = li.generate_learning_report(days=365)
    ev = rep["eval"]
    assert ev["runs"] == 2
    assert ev["latest"] == 0.9 and ev["first"] == 0.6
    assert round(ev["delta"], 4) == 0.3
    assert [p["pass_rate"] for p in ev["points"]] == [0.6, 0.9]  # input order preserved
    assert ev["per_eval_latest"] == {"a": True, "b": True}


def test_outcomes_section_rate_is_successes_over_total():
    ot.record_outcome("s1", True, skills=["deploy"])
    ot.record_outcome("s2", False, skills=["deploy"])
    ot.record_outcome("s3", True, skills=["test"])
    rep = li.generate_learning_report(days=365)
    oc = rep["outcomes"]
    assert oc["all_time"]["sessions"] == 3
    assert oc["all_time"]["successes"] == 2
    assert oc["all_time"]["success_rate"] == round(2 / 3, 3)
    assert "deploy" in oc["by_skill"]


def test_empty_stores_never_raise():
    rep = li.generate_learning_report(days=30)
    assert rep["eval"]["runs"] == 0 and rep["eval"]["points"] == []
    assert rep["outcomes"]["all_time"]["sessions"] == 0
```

- [ ] **Step 2: Run test to verify it fails**

Run: `scripts/run_tests.sh tests/agent/test_learning_insights.py::test_empty_stores_never_raise`
Expected: FAIL with `ModuleNotFoundError: No module named 'agent.learning_insights'`

- [ ] **Step 3: Create `agent/learning_insights.py` with the eval + outcomes sections**

```python
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


def generate_learning_report(days: int = 30, *, now: Optional[float] = None) -> Dict[str, Any]:
    """Aggregate learning-loop metrics. Pure, best-effort, never raises."""
    now = time.time() if now is None else now
    return {
        "days": days,
        "eval": _eval_section(days, now),
        "outcomes": _outcomes_section(days, now),
    }
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `scripts/run_tests.sh tests/agent/test_learning_insights.py`
Expected: PASS (all three tests)

- [ ] **Step 5: Commit**

```bash
git add agent/learning_insights.py tests/agent/test_learning_insights.py
git commit -m "feat(insights): learning-insights aggregator — eval trend + outcomes

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 3: Aggregator — mining yield + knowledge counts

**Files:**
- Modify: `agent/learning_insights.py`
- Test: `tests/agent/test_learning_insights.py`

**Interfaces:**
- Consumes: `sleep.sleep_log_path()` (Task 1); `lessons.get_lessons_path()`/`lessons.load()`; `playbook.load()`; `get_janus_home()/"skills"` and `.../"skills"/".drafts"`.
- Produces: `generate_learning_report` now also returns `"mining"` = `{"cycles","graduated_facts","graduated_skills","lessons","pruned","points"}` and `"knowledge"` = `{"lessons","playbook_entries","active_skills","draft_skills"}`. Consumed by Task 4.

- [ ] **Step 1: Write the failing test**

Add to `tests/agent/test_learning_insights.py`:

```python
def test_mining_section_sums_sleep_log_within_window():
    from agent import sleep
    p = sleep.sleep_log_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(
        json.dumps({"ts": "2026-06-01T00:00:00", "graduated_facts": 2,
                    "graduated_skills": 1, "lessons": 1, "pruned": 0}) + "\n"
        + json.dumps({"ts": "2026-06-02T00:00:00", "graduated_facts": 3,
                      "graduated_skills": 0, "lessons": 2, "pruned": 4}) + "\n",
        encoding="utf-8")
    rep = li.generate_learning_report(days=3650)
    mn = rep["mining"]
    assert mn["cycles"] == 2
    assert mn["graduated_facts"] == 5 and mn["graduated_skills"] == 1
    assert mn["lessons"] == 3 and mn["pruned"] == 4


def test_knowledge_counts_active_vs_draft_skills():
    from janus_constants import get_janus_home
    home = get_janus_home()
    (home / "skills" / "alpha").mkdir(parents=True, exist_ok=True)
    (home / "skills" / "alpha" / "SKILL.md").write_text("x", encoding="utf-8")
    (home / "skills" / ".drafts" / "beta").mkdir(parents=True, exist_ok=True)
    (home / "skills" / ".drafts" / "beta" / "SKILL.md").write_text("y", encoding="utf-8")
    rep = li.generate_learning_report(days=30)
    kn = rep["knowledge"]
    assert kn["active_skills"] == 1
    assert kn["draft_skills"] == 1


def test_mining_and_knowledge_empty_never_raise():
    rep = li.generate_learning_report(days=30)
    assert rep["mining"]["cycles"] == 0 and rep["mining"]["points"] == []
    assert rep["knowledge"]["active_skills"] == 0 and rep["knowledge"]["draft_skills"] == 0
```

- [ ] **Step 2: Run test to verify it fails**

Run: `scripts/run_tests.sh tests/agent/test_learning_insights.py::test_mining_and_knowledge_empty_never_raise`
Expected: FAIL with `KeyError: 'mining'`

- [ ] **Step 3: Add the two sections to `agent/learning_insights.py`**

Add these functions and extend `generate_learning_report`:

```python
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
```

Then update `generate_learning_report`'s return to include both:

```python
    return {
        "days": days,
        "eval": _eval_section(days, now),
        "outcomes": _outcomes_section(days, now),
        "mining": _mining_section(days, now),
        "knowledge": _knowledge_section(),
    }
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `scripts/run_tests.sh tests/agent/test_learning_insights.py`
Expected: PASS (all six tests)

- [ ] **Step 5: Commit**

```bash
git add agent/learning_insights.py tests/agent/test_learning_insights.py
git commit -m "feat(insights): add mining-yield + knowledge-base counts to learning report

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 4: Formatters + `render_insights` dispatcher + JSON

**Files:**
- Modify: `agent/learning_insights.py`
- Test: `tests/agent/test_learning_insights.py`

**Interfaces:**
- Consumes: a learning report dict (Tasks 2-3).
- Produces: `format_learning_terminal(report: dict) -> str`; `format_learning_gateway(report: dict) -> str`; `render_insights(*, usage_report: dict, usage_text: str, learning_report: dict, mode: str = "both", as_json: bool = False) -> str`. `mode` ∈ {"both","usage","learning"}. Consumed by Tasks 5-7.

- [ ] **Step 1: Write the failing test**

Add to `tests/agent/test_learning_insights.py`:

```python
def test_format_learning_terminal_contains_key_labels():
    rep = li.generate_learning_report(days=30)
    text = li.format_learning_terminal(rep)
    assert "Learning" in text
    assert "Eval pass-rate" in text
    assert "Success rate" in text
    assert "drafts" in text.lower()


def test_render_insights_json_round_trips_and_respects_mode():
    usage = {"overview": {"x": 1}}
    learning = li.generate_learning_report(days=30)
    out = li.render_insights(usage_report=usage, usage_text="USAGE-TEXT",
                             learning_report=learning, mode="both", as_json=True)
    parsed = json.loads(out)
    assert parsed["usage"] == usage
    assert parsed["learning"]["outcomes"]["all_time"]["sessions"] == 0

    only = json.loads(li.render_insights(usage_report=usage, usage_text="U",
                                         learning_report=learning, mode="learning", as_json=True))
    assert "usage" not in only and "learning" in only


def test_render_insights_terminal_respects_mode():
    learning = li.generate_learning_report(days=30)
    both = li.render_insights(usage_report={}, usage_text="USAGE-TEXT",
                              learning_report=learning, mode="both", as_json=False)
    assert "USAGE-TEXT" in both and "Learning" in both

    usage_only = li.render_insights(usage_report={}, usage_text="USAGE-TEXT",
                                    learning_report=learning, mode="usage", as_json=False)
    assert "USAGE-TEXT" in usage_only and "Learning" not in usage_only
```

- [ ] **Step 2: Run test to verify it fails**

Run: `scripts/run_tests.sh tests/agent/test_learning_insights.py::test_render_insights_json_round_trips_and_respects_mode`
Expected: FAIL with `AttributeError: module 'agent.learning_insights' has no attribute 'render_insights'`

- [ ] **Step 3: Add the formatters and dispatcher to `agent/learning_insights.py`**

```python
def _fmt_rate(v: Optional[float]) -> str:
    return "—" if v is None else f"{v * 100:.0f}%"


def format_learning_terminal(report: Dict[str, Any]) -> str:
    ev, oc = report.get("eval", {}), report.get("outcomes", {})
    mn, kn = report.get("mining", {}), report.get("knowledge", {})
    lines = ["", "=== Learning ===" ]
    delta = ev.get("delta")
    arrow = "" if not delta else (f"  ▲ +{delta:.2f}" if delta > 0 else f"  ▼ {delta:.2f}")
    lines.append(f"  Eval pass-rate: {_fmt_rate(ev.get('latest'))} "
                 f"({ev.get('runs', 0)} runs){arrow}")
    at = oc.get("all_time", {})
    lines.append(f"  Success rate: {_fmt_rate(at.get('success_rate'))} "
                 f"({at.get('successes', 0)}/{at.get('sessions', 0)} sessions, "
                 f"recent {_fmt_rate(oc.get('recent'))})")
    lines.append(f"  Mining yield ({report.get('days')}d): "
                 f"{mn.get('graduated_facts', 0)} facts, "
                 f"{mn.get('graduated_skills', 0)} skills, "
                 f"{mn.get('lessons', 0)} lessons over {mn.get('cycles', 0)} cycles")
    lines.append(f"  Knowledge base: {kn.get('active_skills', 0)} skills, "
                 f"{kn.get('draft_skills', 0)} drafts awaiting review, "
                 f"{kn.get('lessons', 0)} lessons, "
                 f"{kn.get('playbook_entries', 0)} playbook entries")
    return "\n".join(lines)


def format_learning_gateway(report: Dict[str, Any]) -> str:
    ev, oc = report.get("eval", {}), report.get("outcomes", {})
    kn = report.get("knowledge", {})
    at = oc.get("all_time", {})
    return ("📈 *Learning*\n"
            f"• Eval pass-rate: {_fmt_rate(ev.get('latest'))}\n"
            f"• Success rate: {_fmt_rate(at.get('success_rate'))}\n"
            f"• {kn.get('active_skills', 0)} skills, {kn.get('draft_skills', 0)} drafts")


def render_insights(*, usage_report: Dict[str, Any], usage_text: str,
                    learning_report: Dict[str, Any], mode: str = "both",
                    as_json: bool = False) -> str:
    if as_json:
        payload: Dict[str, Any] = {}
        if mode in ("both", "usage"):
            payload["usage"] = usage_report
        if mode in ("both", "learning"):
            payload["learning"] = learning_report
        return json.dumps(payload, indent=2, ensure_ascii=False, default=str)
    parts: List[str] = []
    if mode in ("both", "usage"):
        parts.append(usage_text)
    if mode in ("both", "learning"):
        parts.append(format_learning_terminal(learning_report))
    return "\n".join(p for p in parts if p)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `scripts/run_tests.sh tests/agent/test_learning_insights.py`
Expected: PASS (all nine tests)

- [ ] **Step 5: Commit**

```bash
git add agent/learning_insights.py tests/agent/test_learning_insights.py
git commit -m "feat(insights): learning formatters + unified render_insights dispatcher

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 5: Wire into the `janus insights` CLI subcommand

**Files:**
- Modify: `janus_cli/main.py` (`insights_parser` + `cmd_insights`, ~16375-16400)
- Test: `tests/janus_cli/test_insights_cli_flags.py` (create)

**Interfaces:**
- Consumes: `generate_learning_report`, `render_insights` (Task 4); existing `InsightsEngine.generate`/`format_terminal`.
- Produces: `--json`, `--learning`, `--usage` flags on the `insights` subcommand; composed output.

- [ ] **Step 1: Write the failing test**

Create `tests/janus_cli/test_insights_cli_flags.py`:

```python
"""The insights subcommand resolves the learning/usage flags to a render mode."""
import janus_cli.main as m


def test_resolve_insights_mode_helper():
    assert m._resolve_insights_mode(learning=False, usage=False) == "both"
    assert m._resolve_insights_mode(learning=True, usage=False) == "learning"
    assert m._resolve_insights_mode(learning=False, usage=True) == "usage"
    # both flags -> both
    assert m._resolve_insights_mode(learning=True, usage=True) == "both"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `scripts/run_tests.sh tests/janus_cli/test_insights_cli_flags.py::test_resolve_insights_mode_helper`
Expected: FAIL with `AttributeError: module 'janus_cli.main' has no attribute '_resolve_insights_mode'`

- [ ] **Step 3: Add the helper and flags, and rewrite `cmd_insights`**

Add this module-level helper to `janus_cli/main.py` (near the insights setup):

```python
def _resolve_insights_mode(*, learning: bool, usage: bool) -> str:
    if learning and not usage:
        return "learning"
    if usage and not learning:
        return "usage"
    return "both"
```

Add flags after the existing `--source` argument (~16385):

```python
    insights_parser.add_argument("--json", action="store_true", dest="as_json",
                                 help="Emit the report as JSON (usage + learning)")
    insights_parser.add_argument("--learning", action="store_true",
                                 help="Show only the learning-loop metrics")
    insights_parser.add_argument("--usage", action="store_true",
                                 help="Show only the usage metrics")
```

Rewrite `cmd_insights` (~16387):

```python
    def cmd_insights(args):
        try:
            from janus_state import SessionDB
            from agent.insights import InsightsEngine
            from agent.learning_insights import generate_learning_report, render_insights

            db = SessionDB()
            engine = InsightsEngine(db)
            usage_report = engine.generate(days=args.days, source=args.source)
            usage_text = engine.format_terminal(usage_report)
            db.close()
            learning_report = generate_learning_report(days=args.days)
            mode = _resolve_insights_mode(learning=args.learning, usage=args.usage)
            print(render_insights(usage_report=usage_report, usage_text=usage_text,
                                  learning_report=learning_report, mode=mode,
                                  as_json=args.as_json))
        except Exception as e:
            print(f"Error generating insights: {e}")
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `scripts/run_tests.sh tests/janus_cli/test_insights_cli_flags.py`
Expected: PASS

- [ ] **Step 5: Manual smoke (optional, non-blocking)**

Run: `python -m janus_cli.main insights --json --days 7` and `... insights --learning`
Expected: valid JSON with `usage`+`learning` keys; learning-only block.

- [ ] **Step 6: Commit**

```bash
git add janus_cli/main.py tests/janus_cli/test_insights_cli_flags.py
git commit -m "feat(insights): --json/--learning/--usage on the insights subcommand

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 6: Wire into the `/insights` slash command

**Files:**
- Modify: `cli.py` (`_show_insights`, ~10805-10839)
- Test: `tests/test_cli_insights_slash.py` (create) — flag parsing only

**Interfaces:**
- Consumes: `generate_learning_report`, `render_insights`, `_resolve_insights_mode` (reuse from `janus_cli.main`).
- Produces: `/insights [days] [--json] [--learning] [--usage] [--source X]` composed output.

- [ ] **Step 1: Write the failing test**

Create `tests/test_cli_insights_slash.py`:

```python
"""The /insights slash parser extracts days/source/mode/json from the command string."""
from cli import _parse_insights_command


def test_parse_insights_defaults():
    opts = _parse_insights_command("/insights")
    assert opts == {"days": 30, "source": None, "mode": "both", "as_json": False}


def test_parse_insights_flags():
    opts = _parse_insights_command("/insights 7 --json --learning --source telegram")
    assert opts["days"] == 7
    assert opts["source"] == "telegram"
    assert opts["mode"] == "learning"
    assert opts["as_json"] is True
```

- [ ] **Step 2: Run test to verify it fails**

Run: `scripts/run_tests.sh tests/test_cli_insights_slash.py::test_parse_insights_defaults`
Expected: FAIL with `ImportError: cannot import name '_parse_insights_command' from 'cli'`

- [ ] **Step 3: Extract a pure parser + rewrite `_show_insights`**

Add this module-level function to `cli.py` (near `_show_insights`):

```python
def _parse_insights_command(command: str) -> dict:
    """Parse `/insights [days] [--json] [--learning] [--usage] [--source X]`."""
    parts = command.split()
    opts = {"days": 30, "source": None, "mode": "both", "as_json": False}
    learning = usage = False
    i = 1
    while i < len(parts):
        tok = parts[i]
        if tok == "--days" and i + 1 < len(parts) and parts[i + 1].isdigit():
            opts["days"] = int(parts[i + 1]); i += 2
        elif tok == "--source" and i + 1 < len(parts):
            opts["source"] = parts[i + 1]; i += 2
        elif tok == "--json":
            opts["as_json"] = True; i += 1
        elif tok == "--learning":
            learning = True; i += 1
        elif tok == "--usage":
            usage = True; i += 1
        elif tok.isdigit():
            opts["days"] = int(tok); i += 1
        else:
            i += 1
    opts["mode"] = "learning" if (learning and not usage) else "usage" if (usage and not learning) else "both"
    return opts
```

Rewrite the body of `_show_insights`:

```python
    def _show_insights(self, command: str = "/insights"):
        """Show usage + learning insights from session history."""
        opts = _parse_insights_command(command)
        try:
            from janus_state import SessionDB
            from agent.insights import InsightsEngine
            from agent.learning_insights import generate_learning_report, render_insights

            db = SessionDB()
            engine = InsightsEngine(db)
            usage_report = engine.generate(days=opts["days"], source=opts["source"])
            usage_text = engine.format_terminal(usage_report)
            db.close()
            learning_report = generate_learning_report(days=opts["days"])
            print(render_insights(usage_report=usage_report, usage_text=usage_text,
                                  learning_report=learning_report, mode=opts["mode"],
                                  as_json=opts["as_json"]))
        except Exception as e:
            print(f"  Error generating insights: {e}")
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `scripts/run_tests.sh tests/test_cli_insights_slash.py`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add cli.py tests/test_cli_insights_slash.py
git commit -m "feat(insights): learning metrics + flags in the /insights slash command

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 7: Append the learning block to the gateway insights handler

**Files:**
- Modify: `gateway/runner.py` (insights handler, ~12574-12585)
- Test: covered by `format_learning_gateway` unit test (Task 4) + a focused composition test below.

**Interfaces:**
- Consumes: `generate_learning_report`, `format_learning_gateway` (Task 4); existing `InsightsEngine.format_gateway`.
- Produces: gateway insights reply = usage gateway text + learning gateway block.

- [ ] **Step 1: Read the current handler to find the exact lines**

Run: `sed -n '12570,12590p' gateway/runner.py`
Expected: shows `engine = InsightsEngine(db)`, `report = engine.generate(...)`, `result = engine.format_gateway(report)`.

- [ ] **Step 2: Write the failing test**

Add to `tests/agent/test_learning_insights.py`:

```python
def test_gateway_block_is_compact_and_labeled():
    rep = li.generate_learning_report(days=30)
    block = li.format_learning_gateway(rep)
    assert "Learning" in block
    assert block.count("\n") <= 4  # stays compact for chat platforms
```

- [ ] **Step 3: Run test to verify it fails (if format_learning_gateway absent) or passes**

Run: `scripts/run_tests.sh tests/agent/test_learning_insights.py::test_gateway_block_is_compact_and_labeled`
Expected: PASS if Task 4 landed `format_learning_gateway`; otherwise FAIL → implement it as in Task 4 Step 3.

- [ ] **Step 4: Append the learning block in `gateway/runner.py`**

Immediately after `result = engine.format_gateway(report)` (~12582), before the result is returned/sent:

```python
                from agent.learning_insights import generate_learning_report, format_learning_gateway
                try:
                    _lrep = generate_learning_report(days=days)
                    result = result + "\n\n" + format_learning_gateway(_lrep)
                except Exception as _exc:
                    logger.debug("gateway insights learning block failed: %s", _exc)
```

(Use the `days` value already in scope for that handler; if the variable has a different name there, match it.)

- [ ] **Step 5: Run the learning-insights + gateway test suites**

Run: `scripts/run_tests.sh tests/agent/test_learning_insights.py`
Run: `scripts/run_tests.sh tests/gateway/`
Expected: PASS (no regressions in gateway tests)

- [ ] **Step 6: Commit**

```bash
git add gateway/runner.py tests/agent/test_learning_insights.py
git commit -m "feat(insights): append learning block to gateway insights reply

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 8: Full-suite verification

- [ ] **Step 1: Run the affected suites end to end**

Run: `scripts/run_tests.sh tests/agent/test_learning_insights.py tests/agent/test_sleep.py tests/janus_cli/test_insights_cli_flags.py tests/test_cli_insights_slash.py`
Expected: PASS

- [ ] **Step 2: Lint the new/changed Python**

Run: `ruff check agent/learning_insights.py agent/sleep.py janus_cli/main.py cli.py gateway/runner.py`
Expected: clean (only `PLW1514` is enforced; all file opens above pass `encoding=`).

- [ ] **Step 3: Final manual smoke (optional)**

Run: `python -m janus_cli.main insights --json` → valid `{"usage":…,"learning":…}` JSON.

---

## Self-Review

**Spec coverage:**
- Learning dimension metrics (eval trend, outcomes, mining yield, knowledge/draft counts) → Tasks 2-3. ✓
- Both terminal + `--json` from one report object → Task 4 (`render_insights`) + Tasks 5-6. ✓
- `sleep_log.jsonl` additive guarded write → Task 1. ✓
- Composed into existing `insights` surface without touching `InsightsEngine` → Tasks 5-7 (engine called, not modified). ✓
- Gateway compact learning block → Task 7. ✓
- Best-effort/never-raises + invariants-not-snapshots tests → every aggregator test asserts a relationship; "empty never raise" tests in Tasks 2-3. ✓
- Fact/memory count "only if a cheap API exists" → omitted from `knowledge` (no such API surfaced); spec permitted omission. ✓ (No task needed.)

**Placeholder scan:** No TBD/TODO; every code step shows full code; every test step shows real assertions. ✓

**Type consistency:** `generate_learning_report(days, *, now)` returns `{days, eval, outcomes, mining, knowledge}` consistently across Tasks 2-4; `render_insights` keyword args match call sites in Tasks 5-7; `_resolve_insights_mode` (main) and the inline mode resolution (slash) produce the same `{"both","usage","learning"}` values consumed by `render_insights`. ✓
