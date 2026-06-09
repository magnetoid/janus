"""Tests for knowledge-gap seeking (agent/gap_seeker.py)."""
import json
from types import SimpleNamespace

import pytest

from agent import gap_seeker as gs
from agent import outcome_tracker as ot


def _fake_llm(reply: str):
    def _caller(**kwargs):
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=reply))])
    return _caller


def test_failure_topics_filters_to_failures_with_notes():
    records = [
        {"success": True, "note": "won task"},
        {"success": False, "note": "rust borrow checker"},
        {"success": False, "note": ""},
        {"success": False, "note": "rust lifetimes"},
    ]
    assert gs._failure_topics(records, lookback=30) == ["rust borrow checker", "rust lifetimes"]


def test_identify_gaps_below_threshold_is_noop():
    ot.record_outcome("s1", False, note="one failure")
    res = gs.identify_gaps(llm_caller=_fake_llm("[]"), min_failures=2)
    assert res["gaps"] == [] and res["considered"] == 1


def test_identify_gaps_clusters_failures():
    ot.record_outcome("s1", False, note="rust borrow checker confusion")
    ot.record_outcome("s2", False, note="rust lifetime errors")
    reply = json.dumps([{"topic": "Rust ownership", "why": "repeated borrow/lifetime failures"}])
    res = gs.identify_gaps(llm_caller=_fake_llm(reply))
    assert res["error"] is None
    assert res["gaps"][0]["topic"] == "Rust ownership"


def test_identify_gaps_best_effort_on_failure():
    ot.record_outcome("s1", False, note="a")
    ot.record_outcome("s2", False, note="b")
    def boom(**kw):
        raise RuntimeError("down")
    res = gs.identify_gaps(llm_caller=boom)
    assert res["error"] is not None and res["gaps"] == []


def test_adopt_gap_as_interest():
    rec = gs.adopt_gap_as_interest("Rust ownership")
    from agent import interests as it
    assert any(a["field"] == "Rust ownership" and a["source"] == "gap-seeker" for a in it.load())
