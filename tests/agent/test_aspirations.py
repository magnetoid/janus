"""Tests for proactive aspirations (agent/aspirations.py)."""
import json
from types import SimpleNamespace

import pytest

from agent import aspirations as asp


def _fake_llm(reply: str):
    def _caller(**kwargs):
        return SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content=reply))]
        )
    return _caller


def test_add_load_get_roundtrip():
    rec = asp.add("Ship Janus 1.0", roadmap=["cut a release", "write docs"])
    assert rec["id"] == "ship-janus-1-0"
    assert rec["status"] == "active"
    assert asp.get(rec["id"])["title"] == "Ship Janus 1.0"
    assert [a["id"] for a in asp.list_active()] == [rec["id"]]


def test_unique_ids_for_same_title():
    a = asp.add("Learn Rust")
    b = asp.add("Learn Rust")
    assert a["id"] == "learn-rust" and b["id"] == "learn-rust-2"


def test_status_and_remove():
    rec = asp.add("Run a marathon")
    assert asp.set_status(rec["id"], "achieved") is True
    assert asp.list_active() == []
    assert asp.remove(rec["id"]) is True
    assert asp.get(rec["id"]) is None
    assert asp.remove("nope") is False


def test_mark_checked_in_sets_timestamp(monkeypatch):
    monkeypatch.setattr(asp, "_now_iso", lambda: "2026-06-09T09:00:00+00:00")
    rec = asp.add("Write a book")
    asp.mark_checked_in([rec["id"]])
    assert asp.get(rec["id"])["last_checkin_at"] == "2026-06-09T09:00:00+00:00"


def test_parse_roadmap_json_and_lines():
    assert asp._parse_roadmap('["a", "b", "c"]') == ["a", "b", "c"]
    assert asp._parse_roadmap("1. first\n2. second\n- third") == ["first", "second", "third"]
    assert asp._parse_roadmap("") == []


def test_draft_roadmap_uses_llm():
    out = asp.draft_roadmap("Open source it", llm_caller=_fake_llm('["publish repo", "write README"]'))
    assert out == ["publish repo", "write README"]


def test_draft_roadmap_best_effort_on_failure():
    def boom(**kwargs):
        raise RuntimeError("down")
    assert asp.draft_roadmap("x", llm_caller=boom) == []


def test_format_checkin_context():
    asp.add("Build a SaaS", roadmap=["validate idea", "MVP"])
    ctx = asp.format_checkin_context()
    assert "Build a SaaS" in ctx
    assert "1. validate idea" in ctx and "2. MVP" in ctx
    # No active aspirations -> empty string.
    assert asp.format_checkin_context([]) == ""


def test_checkin_script_runs_and_prints_active(tmp_path, monkeypatch):
    import os, subprocess, sys
    home = tmp_path / ".janus"
    home.mkdir()
    (home / "aspirations.json").write_text(
        json.dumps([
            {"id": "g1", "title": "Goal One", "roadmap": ["step a"], "status": "active"},
            {"id": "g2", "title": "Done", "roadmap": [], "status": "achieved"},
        ]),
        encoding="utf-8",
    )
    script = tmp_path / "aspire_checkin.py"
    script.write_text(asp.checkin_script_source(), encoding="utf-8")
    env = {**os.environ, "JANUS_HOME": str(home)}
    out = subprocess.run([sys.executable, str(script)], capture_output=True, text=True, env=env)
    assert "Goal One" in out.stdout
    assert "step a" in out.stdout
    assert "Done" not in out.stdout  # achieved ones excluded
