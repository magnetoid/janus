"""Tests for session-end memory mining (agent/memory_miner.py)."""
import os
from types import SimpleNamespace

import pytest

from agent import memory_miner
from agent.memory_miner import _parse_facts, _render_transcript, mine_session_memory
from tools.memory_tool import MemoryStore, read_daily_snapshots


def _fake_llm(reply: str):
    """Return an llm_caller that yields `reply` as the model's content."""
    def _caller(**kwargs):
        return SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content=reply))]
        )
    return _caller


TRANSCRIPT = [
    {"role": "user", "content": "I'm Marko, I work in Belgrade and prefer terse replies."},
    {"role": "assistant", "content": "Noted."},
    {"role": "tool", "content": "irrelevant tool noise"},
    {"role": "user", "content": "Our deploy script is scripts/deploy.sh; always run tests first."},
]


def test_render_transcript_keeps_only_user_assistant_text():
    out = _render_transcript(TRANSCRIPT)
    assert "USER: I'm Marko" in out
    assert "ASSISTANT: Noted." in out
    assert "tool noise" not in out  # tool turns dropped


def test_parse_facts_tolerates_code_fences_and_prose():
    raw = 'Here you go:\n```json\n{"user": ["likes tabs"], "memory": ["uses pytest"]}\n```'
    facts = _parse_facts(raw)
    assert facts == {"user": ["likes tabs"], "memory": ["uses pytest"]}


def test_parse_facts_bad_json_returns_empty():
    assert _parse_facts("not json at all") == {"user": [], "memory": []}
    assert _parse_facts("") == {"user": [], "memory": []}


def test_mine_writes_to_memory_and_journal(monkeypatch):
    monkeypatch.setenv("JANUS_MEMORY_DAILY_SNAPSHOTS", "on")
    store = MemoryStore()
    store.load_from_disk()
    reply = (
        '{"user": ["Marko is based in Belgrade", "prefers terse replies"], '
        '"memory": ["deploy script is scripts/deploy.sh", "run tests before deploy"]}'
    )
    summary = mine_session_memory(TRANSCRIPT, store, llm_caller=_fake_llm(reply))

    assert summary["added"] == {"user": 2, "memory": 2}
    assert summary["error"] is None
    # landed in the live stores
    assert any("Belgrade" in e for e in store.user_entries)
    assert any("deploy.sh" in e for e in store.memory_entries)
    # and mirrored into the daily journal (the feature we built earlier)
    journal = read_daily_snapshots()["days"]
    assert journal and "scripts/deploy.sh" in journal[0]["text"]


def test_mine_dedupes_against_existing_entries(monkeypatch):
    monkeypatch.setenv("JANUS_MEMORY_DAILY_SNAPSHOTS", "off")
    store = MemoryStore()
    store.load_from_disk()
    store.add("user", "Marko is based in Belgrade")
    reply = '{"user": ["Marko is based in Belgrade"], "memory": []}'
    summary = mine_session_memory(TRANSCRIPT, store, llm_caller=_fake_llm(reply))

    assert summary["added"]["user"] == 0
    assert summary["skipped_duplicates"] >= 1
    assert sum("Belgrade" in e for e in store.user_entries) == 1  # no duplicate


def test_mine_is_best_effort_on_llm_failure():
    store = MemoryStore()
    store.load_from_disk()

    def _boom(**kwargs):
        raise RuntimeError("model exploded")

    summary = mine_session_memory(TRANSCRIPT, store, llm_caller=_boom)
    assert summary["error"] is not None
    assert summary["added"] == {"user": 0, "memory": 0}


def test_mine_empty_transcript_noop():
    store = MemoryStore()
    store.load_from_disk()
    summary = mine_session_memory([], store, llm_caller=_fake_llm('{"user":["x"]}'))
    assert summary["added"] == {"user": 0, "memory": 0}
