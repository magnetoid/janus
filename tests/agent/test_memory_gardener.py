"""Tests for memory reconciliation (agent/memory_gardener.py)."""
import json
from types import SimpleNamespace

import pytest

from agent import memory_gardener as mg
from tools.memory_tool import MemoryStore


def _fake_llm(reply: str):
    def _caller(**kwargs):
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=reply))])
    return _caller


def test_parse_validates_indices():
    out = mg._parse('[{"drop":0,"kept":1,"reason":"old"},{"drop":9,"kept":1}]', n=2)
    assert out == [{"drop": 0, "kept": 1, "reason": "old"}]  # index 9 out of range dropped


def test_find_stale_empty_for_single_entry():
    assert mg.find_stale(["only one"], llm_caller=_fake_llm("[]")) == []


def test_reconcile_removes_superseded(monkeypatch):
    store = MemoryStore()
    store.load_from_disk()
    store.add("memory", "uses Python 3.11")
    store.add("memory", "now on Python 3.12")
    reply = json.dumps([{"drop": 0, "kept": 1, "reason": "superseded by 3.12"}])
    res = mg.reconcile(store, llm_caller=_fake_llm(reply))
    assert res["error"] is None
    assert res["removed"] == ["uses Python 3.11"]
    assert "uses Python 3.11" not in store.memory_entries
    assert "now on Python 3.12" in store.memory_entries


def test_reconcile_dry_run_changes_nothing():
    store = MemoryStore()
    store.load_from_disk()
    store.add("memory", "a")
    store.add("memory", "b")
    reply = json.dumps([{"drop": 0, "kept": 1}])
    res = mg.reconcile(store, llm_caller=_fake_llm(reply), apply=False)
    assert res["removed"] == ["a"]
    assert "a" in store.memory_entries  # not actually removed


def test_reconcile_never_wipes_everything():
    store = MemoryStore()
    store.load_from_disk()
    store.add("memory", "a")
    store.add("memory", "b")
    # model wrongly says drop both
    reply = json.dumps([{"drop": 0, "kept": 1}, {"drop": 1, "kept": 0}])
    res = mg.reconcile(store, llm_caller=_fake_llm(reply))
    assert len(store.memory_entries) >= 1  # at least one survives


def test_reconcile_best_effort_on_failure():
    store = MemoryStore()
    store.load_from_disk()
    store.add("memory", "a")
    store.add("memory", "b")
    def boom(**kw):
        raise RuntimeError("down")
    res = mg.reconcile(store, llm_caller=boom)
    assert res["error"] is not None and res["removed"] == []
