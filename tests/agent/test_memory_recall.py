"""Tests for relevance recall over memory (agent/memory_recall.py)."""
import pytest

from agent import memory_recall as mr
from tools.memory_tool import MemoryStore


def _seed():
    store = MemoryStore()
    store.load_from_disk()
    store.add("memory", "deploy script lives at scripts/deploy.sh; run tests first")
    store.add("memory", "the user prefers dark mode in the editor")
    store.add("memory", "database is postgres 16 on the staging server")
    return store


def test_recall_ranks_relevant_first():
    _seed()
    hits = mr.recall("how do I deploy", include_journal=False)
    assert hits, "should find something"
    assert "deploy" in hits[0]["text"]


def test_recall_empty_query_returns_nothing():
    _seed()
    assert mr.recall("   ", include_journal=False) == []


def test_recall_no_overlap_returns_nothing():
    _seed()
    assert mr.recall("quantum chromodynamics", include_journal=False) == []


def test_recall_includes_journal(monkeypatch):
    monkeypatch.setenv("JANUS_MEMORY_DAILY_SNAPSHOTS", "on")
    from datetime import datetime
    from tools.memory_tool import append_daily_snapshot
    append_daily_snapshot("memory", "kubernetes ingress uses nginx controller", "add",
                          when=datetime(2026, 6, 9, 12, 0))
    hits = mr.recall("kubernetes ingress")
    assert any("kubernetes" in h["text"] for h in hits)
    assert any(h["source"].startswith("journal:") for h in hits)


def test_recall_respects_n():
    store = MemoryStore()
    store.load_from_disk()
    for i in range(8):
        store.add("memory", f"python tip number {i} about testing")
    hits = mr.recall("python testing", n=3, include_journal=False)
    assert len(hits) == 3


def test_recall_prefers_fresher_journal_when_relevance_ties(monkeypatch):
    """Recency breaks ties: equally-relevant entries rank newest-first."""
    monkeypatch.setenv("JANUS_MEMORY_DAILY_SNAPSHOTS", "on")
    from datetime import datetime
    from tools.memory_tool import append_daily_snapshot

    # fix "today" so the test is deterministic regardless of run date
    monkeypatch.setattr(mr, "_today", lambda: datetime(2026, 6, 12))
    append_daily_snapshot("memory", "redis caching layer tuning notes alpha", "add",
                          when=datetime(2026, 1, 1, 12, 0))
    append_daily_snapshot("memory", "redis caching layer tuning notes beta", "add",
                          when=datetime(2026, 6, 10, 12, 0))
    hits = mr.recall("redis caching tuning")
    assert hits[0]["source"] == "journal:2026-06-10"  # fresher wins the tie


def test_durable_memory_outranks_stale_journal(monkeypatch):
    """A curated memory fact (always current) beats an equally-relevant old journal line."""
    monkeypatch.setenv("JANUS_MEMORY_DAILY_SNAPSHOTS", "on")
    from datetime import datetime
    from tools.memory_tool import append_daily_snapshot

    monkeypatch.setattr(mr, "_today", lambda: datetime(2026, 6, 12))
    store = MemoryStore()
    store.load_from_disk()
    store.add("memory", "kafka consumer group rebalance settings xray")
    append_daily_snapshot("memory", "kafka consumer group rebalance settings yankee", "add",
                          when=datetime(2025, 1, 1, 12, 0))  # very old
    hits = mr.recall("kafka consumer rebalance settings")
    assert hits[0]["source"] == "memory"
