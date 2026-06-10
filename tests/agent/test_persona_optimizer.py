"""Tests for persona optimization + outcome_tracker persona/trajectory additions (F2)."""
import pytest

from agent import outcome_tracker as ot
from agent import persona_optimizer as po


def test_record_outcome_active_persona_backward_compat():
    # default keeps working
    r1 = ot.record_outcome("s1", True, skills=["x"])
    assert r1["persona"] == ""
    # and accepts a persona
    r2 = ot.record_outcome("s2", True, active_persona="terse")
    assert r2["persona"] == "terse"


def test_persona_stats_aggregates_by_persona():
    ot.record_outcome("s1", True, active_persona="terse")
    ot.record_outcome("s2", False, active_persona="terse")
    ot.record_outcome("s3", True, active_persona="verbose")
    ot.record_outcome("s4", True)  # no persona -> "default"
    stats = po.persona_stats()
    assert stats["terse"] == {"uses": 2, "successes": 1, "success_rate": 0.5}
    assert stats["verbose"]["success_rate"] == 1.0
    assert stats["default"]["uses"] == 1


def test_recommend_persona_insufficient_data():
    ot.record_outcome("s1", True, active_persona="terse")
    rec = po.recommend_persona(min_samples=10)
    assert rec["recommended"] is None and "insufficient" in rec["reason"]


def test_recommend_persona_picks_best():
    for i in range(5):
        ot.record_outcome(f"a{i}", True, active_persona="terse")
    for i in range(5):
        ot.record_outcome(f"b{i}", i < 2, active_persona="verbose")  # 40%
    rec = po.recommend_persona(min_samples=3)
    assert rec["recommended"] == "terse" and rec["success_rate"] == 1.0


def test_list_personas_reads_existing_config(tmp_path, monkeypatch):
    import yaml
    home = tmp_path / ".janus"; home.mkdir()
    monkeypatch.setenv("JANUS_HOME", str(home))
    (home / "config.yaml").write_text(
        yaml.safe_dump({"agent": {"personalities": {"terse": {"system_prompt": "be brief"}}}}),
        encoding="utf-8")
    assert po.list_personas() == ["default", "terse"]  # reuses agent.personalities, no parallel store


def test_skill_success_trajectory():
    ot.record_outcome("s1", True, skills=["deploy"])
    ot.record_outcome("s2", False, skills=["deploy", "test"])
    ot.record_outcome("s3", True, skills=["test"])
    assert ot.skill_success_trajectory("deploy") == [True, False]
    assert ot.skill_success_trajectory("test") == [False, True]
    assert ot.skill_success_trajectory("nope") == []
