"""Tests for the model-strengths intelligence layer."""
import json
from types import SimpleNamespace

import pytest

from agent import model_strengths as ms


def _fake_llm(reply: str):
    def _caller(**kwargs):
        return SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content=reply))]
        )
    return _caller


def test_record_and_best_models_ranked_by_score():
    ms.record("coding", "deepseek-v3.2", score=5)
    ms.record("coding", "claude-opus-4.6", score=9)
    ms.record("coding", "gpt-5.4", score=7)
    assert ms.best_models_for("coding", n=2) == ["claude-opus-4.6", "gpt-5.4"]


def test_record_updates_existing_entry():
    ms.record("math", "gemini-3-pro", score=3, note="ok")
    ms.record("math", "gemini-3-pro", score=8, note="great")
    entries = ms.load()["math"]
    assert len(entries) == 1 and entries[0]["score"] == 8 and entries[0]["note"] == "great"


def test_task_normalization():
    ms.record("Tool Use!!", "claude-opus-4.6", score=9)
    assert "tool-use" in ms.load()
    assert ms.best_models_for("tool use") == ["claude-opus-4.6"]


def test_best_models_filters_by_available_substring():
    ms.record("coding", "claude-opus-4.6", score=9)
    ms.record("coding", "gpt-5.4", score=7)
    # KB names match provider-prefixed available ids by substring.
    avail = ["anthropic/claude-opus-4.6", "openrouter/deepseek-v3.2"]
    assert ms.best_models_for("coding", available=avail) == ["claude-opus-4.6"]


def test_parse_ranked_models_strings_and_objects():
    assert [r["model"] for r in ms._parse_ranked_models('["a","b"]')] == ["a", "b"]
    objs = ms._parse_ranked_models('[{"model":"x","note":"why","score":9}]')
    assert objs[0]["model"] == "x" and objs[0]["score"] == 9
    assert ms._parse_ranked_models("not json") == []


def test_research_records_from_web_and_llm():
    web = lambda q: "Article: Claude leads coding, GPT close behind."
    res = ms.research(
        "coding",
        web_search_caller=web,
        llm_caller=_fake_llm('[{"model":"claude-opus-4.6","note":"best"},{"model":"gpt-5.4"}]'),
    )
    assert res["error"] is None
    assert [r["model"] for r in res["ranked"]] == ["claude-opus-4.6", "gpt-5.4"]
    # recorded into the KB with source web-research
    entries = ms.load()["coding"]
    assert any(e["source"] == "web-research" for e in entries)
    assert ms.best_models_for("coding")[0] == "claude-opus-4.6"


def test_research_best_effort_on_failure():
    def boom(q):
        raise RuntimeError("network down")
    res = ms.research("coding", web_search_caller=boom, llm_caller=_fake_llm("[]"))
    assert res["error"] is not None and res["ranked"] == []
