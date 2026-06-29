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
