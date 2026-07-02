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


# --- live outcome accumulation (Track D learned routing) --------------------

def test_record_outcome_accumulates_ewma():
    e = ms.record_outcome("delegation-simple", "mini-1", True)
    assert e["score"] == 1.0 and e["samples"] == 1
    ms.record_outcome("delegation-simple", "mini-1", True)
    e = ms.record_outcome("delegation-simple", "mini-1", False, alpha=0.3)
    # 0.7 * 1.0 + 0.3 * 0.0
    assert e["score"] == pytest.approx(0.7) and e["samples"] == 3
    score, samples = ms.outcome_score("delegation-simple", "mini-1")
    assert score == pytest.approx(0.7) and samples == 3


def test_outcome_score_ignores_curated_entries():
    ms.record("delegation-hard", "opus-x", score=9)  # curated seed, no samples
    assert ms.outcome_score("delegation-hard", "opus-x") == (None, 0)
    # First real outcome starts the running rate from the observation, not the seed
    e = ms.record_outcome("delegation-hard", "opus-x", False)
    assert e["score"] == 0.0 and e["samples"] == 1


def test_outcome_score_unknown_model():
    assert ms.outcome_score("delegation-mid", "never-seen") == (None, 0)


# --- canonical taxonomy + cost-joined value ranking (move 6-remainder) -------

def test_canonical_category_classifies():
    assert ms.canonical_category("fix the python bug in my api") == "coding"
    assert ms.canonical_category("write me an essay about dogs") == "writing"
    assert ms.canonical_category("solve this integral equation") == "math"
    assert ms.canonical_category("research the sources and cite them") == "research"
    assert ms.canonical_category("hello there") == "general"       # no keywords
    assert ms.canonical_category("") == "general"


def test_record_outcome_tracks_mean_cost_ewma():
    e = ms.record_outcome("coding", "m1", True, cost=0.10)
    assert e["mean_cost"] == 0.10
    e = ms.record_outcome("coding", "m1", True, cost=0.20, alpha=0.5)
    assert e["mean_cost"] == 0.15                                   # 0.5*0.10 + 0.5*0.20


def test_best_value_models_quality_vs_cost():
    for _ in range(3):
        ms.record_outcome("coding", "cheap-A", True, cost=0.01)
        ms.record_outcome("coding", "pricey-B", True, cost=0.50)
    ms.record_outcome("coding", "cheap-A", False, cost=0.01)        # A slightly worse
    assert ms.best_value_models("coding", cost_weight=0.0)[0] == "pricey-B"   # quality wins
    assert ms.best_value_models("coding", cost_weight=1.0)[0] == "cheap-A"    # cost flips it


def test_best_value_models_requires_min_samples_and_filters_available():
    for _ in range(3):
        ms.record_outcome("math", "proven", True, cost=0.02)
    ms.record_outcome("math", "unproven", True, cost=0.02)          # only 1 sample
    assert ms.best_value_models("math", min_samples=2) == ["proven"]
    # availability filter
    assert ms.best_value_models("math", available=["openrouter/other"], min_samples=2) == []
