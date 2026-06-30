"""Tests for the compression learning sink (agent/conversation_compression.py).

The pre-compression distilled insight (MemoryProvider.on_pre_compress) was
previously dropped; it is now persisted into the lessons store post-compression.
"""
from agent.conversation_compression import _route_precompress_insight_to_lessons
from agent import lessons


def test_insight_routed_to_lessons_as_compression_source():
    assert _route_precompress_insight_to_lessons("Prefer batching DB writes.", session_id="s1") is True
    recs = lessons.load()
    assert any(r.get("source") == "compression" and "batching" in r["lesson"] for r in recs)


def test_empty_insight_writes_nothing():
    assert _route_precompress_insight_to_lessons("", session_id="s1") is False
    assert _route_precompress_insight_to_lessons(None) is False
    assert _route_precompress_insight_to_lessons("   ") is False
    assert lessons.load() == []


def test_long_insight_is_capped():
    big = "batch writes; " * 100  # ~1400 chars
    assert _route_precompress_insight_to_lessons(big) is True
    rec = lessons.load()[0]
    assert len(rec["lesson"]) <= 600
