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
