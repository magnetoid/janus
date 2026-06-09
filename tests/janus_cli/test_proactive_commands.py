"""Tests for the shared slash-command handlers (CLI + gateway)."""
import pytest

from janus_cli import proactive_commands as pc


def test_aspire_set_list_done_clear(monkeypatch):
    # Avoid a live LLM call for the roadmap.
    monkeypatch.setattr("agent.aspirations.draft_roadmap", lambda *a, **k: ["m1", "m2"])
    out = pc.handle_aspire("set Ship Janus 1.0")
    assert "Aspiration set" in out and "ship-janus-1-0" in out and "1. m1" in out

    lst = pc.handle_aspire("list")
    assert "ship-janus-1-0" in lst and "Ship Janus 1.0" in lst

    assert "achieved" in pc.handle_aspire("done ship-janus-1-0").lower()
    assert "✓ Removed." == pc.handle_aspire("clear ship-janus-1-0")


def test_aspire_set_requires_text():
    assert "Usage" in pc.handle_aspire("set")


def test_interest_add_list_remove():
    out = pc.handle_interest("add graphic design")
    assert "Now tracking" in out and "graphic-design" in out
    assert "graphic-design" in pc.handle_interest("list")
    assert pc.handle_interest("remove graphic-design") == "✓ Stopped tracking."
    assert "No interests yet" in pc.handle_interest("list")


def test_memory_log_empty_and_populated(monkeypatch):
    assert "No daily memory snapshots" in pc.handle_memory("log")
    from datetime import datetime
    from tools.memory_tool import append_daily_snapshot
    monkeypatch.setenv("JANUS_MEMORY_DAILY_SNAPSHOTS", "on")
    append_daily_snapshot("memory", "uses tabs", "add", when=datetime(2026, 6, 9, 12, 0))
    out = pc.handle_memory("log")
    assert "uses tabs" in out


def test_memory_mine_points_to_terminal():
    assert "janus memory mine" in pc.handle_memory("mine")
