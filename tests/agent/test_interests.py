"""Tests for interest-driven self-learning (agent/interests.py)."""
import json
from types import SimpleNamespace

import pytest

from agent import interests as it


def _fake_llm(reply: str):
    def _caller(**kwargs):
        return SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content=reply))]
        )
    return _caller


def test_add_dedupes_by_field_case_insensitive():
    a = it.add("Graphic Design")
    b = it.add("graphic design")
    assert a["id"] == b["id"] == "graphic-design"
    assert len(it.load()) == 1


def test_list_active_and_remove():
    r = it.add("Typography")
    assert [x["id"] for x in it.list_active()] == [r["id"]]
    assert it.remove(r["id"]) is True
    assert it.list_active() == []
    assert it.remove("nope") is False


def test_mark_researched(monkeypatch):
    monkeypatch.setattr(it, "_now_iso", lambda: "2026-06-09T09:00:00+00:00")
    r = it.add("Web Design")
    it.mark_researched(r["id"])
    assert it.get(r["id"])["last_researched_at"] == "2026-06-09T09:00:00+00:00"


def test_parse_findings_strings_and_objects():
    assert it._parse_findings('["a","b"]') == [{"trend": "a", "why": ""}, {"trend": "b", "why": ""}]
    objs = it._parse_findings('[{"trend":"X","why":"matters"}]')
    assert objs == [{"trend": "X", "why": "matters"}]
    assert it._parse_findings("nope") == []


def test_research_interest_uses_web_and_llm():
    web = lambda q: "Designers are adopting variable fonts and AI tooling."
    res = it.research_interest(
        "graphic design",
        web_search_caller=web,
        llm_caller=_fake_llm('[{"trend":"Variable fonts","why":"flexible typography"}]'),
    )
    assert res["error"] is None
    assert res["findings"][0]["trend"] == "Variable fonts"


def test_research_best_effort_on_failure():
    def boom(q):
        raise RuntimeError("offline")
    res = it.research_interest("x", web_search_caller=boom, llm_caller=_fake_llm("[]"))
    assert res["error"] is not None and res["findings"] == []


def test_format_discovery_is_consent_gated():
    msg = it.format_discovery("typography", [{"trend": "Variable fonts", "why": "flexible"}])
    assert "typography" in msg
    assert "Variable fonts" in msg
    assert "?" in msg  # it asks permission
    assert it.format_discovery("x", []) == ""


def test_discovery_script_prints_active_only(tmp_path):
    import os, subprocess, sys
    home = tmp_path / ".janus"
    home.mkdir()
    (home / "interests.json").write_text(json.dumps([
        {"id": "a", "field": "Design", "status": "active", "note": "logos"},
        {"id": "b", "field": "Old", "status": "archived"},
    ]), encoding="utf-8")
    script = tmp_path / "interest_discover.py"
    script.write_text(it.discovery_script_source(), encoding="utf-8")
    out = subprocess.run(
        [sys.executable, str(script)], capture_output=True, text=True,
        env={**os.environ, "JANUS_HOME": str(home)},
    )
    assert "Design" in out.stdout and "logos" in out.stdout
    assert "Old" not in out.stdout
