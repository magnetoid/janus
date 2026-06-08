"""Tests for the OpenClaw-style daily memory snapshot journal."""
import os
from datetime import datetime

import pytest

from tools import memory_tool
from tools.memory_tool import (
    MemoryStore,
    append_daily_snapshot,
    get_daily_dir,
    read_daily_snapshots,
)


@pytest.fixture(autouse=True)
def _reset_daily_cache():
    # The enable-gate is process-cached; clear it so each test controls it.
    memory_tool._daily_enabled_cache = None
    yield
    memory_tool._daily_enabled_cache = None


def _fixed(dt="2026-06-08 14:32"):
    return datetime.strptime(dt, "%Y-%m-%d %H:%M")


def test_append_creates_dated_file_with_header_and_entry(monkeypatch):
    monkeypatch.setenv("JANUS_MEMORY_DAILY_SNAPSHOTS", "on")
    append_daily_snapshot("memory", "user prefers tabs over spaces", "add", when=_fixed())

    path = get_daily_dir() / "2026-06-08.md"
    assert path.exists()
    text = path.read_text(encoding="utf-8")
    assert text.startswith("# Memory journal — 2026-06-08")
    assert "`14:32` **MEMORY** added: user prefers tabs over spaces" in text


def test_append_is_append_only_across_events(monkeypatch):
    monkeypatch.setenv("JANUS_MEMORY_DAILY_SNAPSHOTS", "on")
    append_daily_snapshot("memory", "fact one", "add", when=_fixed("2026-06-08 09:00"))
    append_daily_snapshot("user", "likes terse replies", "add", when=_fixed("2026-06-08 09:05"))
    append_daily_snapshot("memory", "fact one v2", "replace", when=_fixed("2026-06-08 10:00"))
    append_daily_snapshot("memory", "fact one v2", "remove", when=_fixed("2026-06-08 11:00"))

    text = (get_daily_dir() / "2026-06-08.md").read_text(encoding="utf-8")
    # Single header, four chronological entries, scopes + verbs preserved.
    assert text.count("# Memory journal") == 1
    assert text.index("09:00") < text.index("09:05") < text.index("10:00") < text.index("11:00")
    assert "**USER** added: likes terse replies" in text
    assert "**MEMORY** revised: fact one v2" in text
    assert "**MEMORY** removed: fact one v2" in text


def test_disabled_writes_nothing(monkeypatch):
    monkeypatch.setenv("JANUS_MEMORY_DAILY_SNAPSHOTS", "off")
    append_daily_snapshot("memory", "should not be written", "add", when=_fixed())
    assert not get_daily_dir().exists()


def test_reader_returns_recent_days(monkeypatch):
    monkeypatch.setenv("JANUS_MEMORY_DAILY_SNAPSHOTS", "on")
    for d in ("2026-06-01", "2026-06-05", "2026-06-08"):
        append_daily_snapshot("memory", f"note {d}", "add", when=_fixed(f"{d} 12:00"))

    all_days = read_daily_snapshots()
    assert [d["date"] for d in all_days["days"]] == ["2026-06-01", "2026-06-05", "2026-06-08"]

    one = read_daily_snapshots(date="2026-06-05")
    assert len(one["days"]) == 1 and one["days"][0]["date"] == "2026-06-05"

    last_two = read_daily_snapshots(days=2)
    assert [d["date"] for d in last_two["days"]] == ["2026-06-05", "2026-06-08"]


def test_reader_handles_no_journal():
    assert read_daily_snapshots()["days"] == []


def test_memory_store_add_mirrors_to_journal(monkeypatch):
    monkeypatch.setenv("JANUS_MEMORY_DAILY_SNAPSHOTS", "on")
    store = MemoryStore()
    store.load_from_disk()
    result = store.add("memory", "the deploy script lives at scripts/deploy.sh")
    assert result["success"] is True

    days = read_daily_snapshots()["days"]
    assert len(days) == 1
    assert "the deploy script lives at scripts/deploy.sh" in days[0]["text"]


def test_journal_failure_never_breaks_memory_write(monkeypatch):
    monkeypatch.setenv("JANUS_MEMORY_DAILY_SNAPSHOTS", "on")
    # Force the journal writer to blow up; the memory add must still succeed.
    monkeypatch.setattr(memory_tool, "get_daily_dir", lambda: (_ for _ in ()).throw(RuntimeError("boom")))
    store = MemoryStore()
    store.load_from_disk()
    assert store.add("memory", "resilient entry")["success"] is True
