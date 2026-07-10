"""Concurrency safety for the JSON learning stores.

The learning stores (``lessons.json``, ``outcomes.json``, ``model_strengths.json``,
``lesson_recall.json``) are read-modify-written from several actors at once —
auto-mine background threads, the sleep cycle, and gateway sessions — and a
lost update there silently erases learned state. ``agent/store_lock.py`` gives
them the same cross-process exclusive-lock + atomic-replace discipline the
memory store already has (``tools/memory_tool.py::_file_lock``).

These tests assert relationships (no lost updates, mutual exclusion, no torn
files), not snapshots.
"""
from __future__ import annotations

import json
import threading
import time


# --------------------------------------------------------------------------
# The lock primitive
# --------------------------------------------------------------------------

def test_locked_store_gives_mutual_exclusion(tmp_path):
    """A second acquirer blocks until the first releases."""
    from agent.store_lock import locked_store

    target = tmp_path / "store.json"
    entered = threading.Event()
    finished = threading.Event()

    def contender():
        with locked_store(target):
            entered.set()
        finished.set()

    with locked_store(target):
        t = threading.Thread(target=contender, daemon=True)
        t.start()
        # The contender must NOT get the lock while we hold it.
        assert not entered.wait(timeout=0.4)
    # After release it proceeds promptly.
    assert finished.wait(timeout=5.0)
    t.join(timeout=5.0)


def test_atomic_write_text_produces_valid_file_and_no_droppings(tmp_path):
    from agent.store_lock import atomic_write_text

    target = tmp_path / "nested" / "store.json"
    atomic_write_text(target, json.dumps({"k": "v"}))
    assert json.loads(target.read_text(encoding="utf-8")) == {"k": "v"}
    # No temp-file droppings next to the store.
    leftovers = [p for p in target.parent.iterdir() if p.name != target.name]
    assert leftovers == []


# --------------------------------------------------------------------------
# Lost-update protection on the real stores
# --------------------------------------------------------------------------

def _hammer(fn, per_thread: int, threads: int = 4):
    errors = []

    def work(tid: int):
        try:
            for i in range(per_thread):
                fn(tid, i)
        except Exception as exc:  # pragma: no cover - surfaced via assert
            errors.append(exc)

    ts = [threading.Thread(target=work, args=(t,)) for t in range(threads)]
    for t in ts:
        t.start()
    for t in ts:
        t.join(timeout=60)
    assert errors == []


def test_concurrent_record_lesson_loses_no_records():
    from agent import lessons

    _hammer(lambda tid, i: lessons.record_lesson(
        f"thread-{tid} lesson number {i} about topic-{tid}-{i}",
        task_type="testing"), per_thread=10)

    stored = {r["lesson"] for r in lessons.load()}
    assert len(stored) == 40


def test_concurrent_record_outcome_loses_no_records():
    from agent import outcome_tracker

    _hammer(lambda tid, i: outcome_tracker.record_outcome(
        f"sess-{tid}-{i}", success=True), per_thread=10)

    assert len(outcome_tracker.load()) == 40


def test_concurrent_model_strength_outcomes_lose_no_samples():
    from agent import model_strengths

    _hammer(lambda tid, i: model_strengths.record_outcome(
        "coding", "test/model", success=True), per_thread=10)

    entries = model_strengths.load().get("coding", [])
    assert len(entries) == 1
    assert entries[0]["samples"] == 40


def test_concurrent_log_recall_merges_all_ids():
    """log_recall RMWs lesson_recall.json; concurrent turns must not drop ids."""
    from unittest.mock import patch

    from agent import lessons

    with patch.object(lessons, "_outcome_tracking_on", return_value=True):
        _hammer(lambda tid, i: lessons.log_recall(
            "sess-shared", [f"lesson-{tid}-{i}"]), per_thread=10)
        state = lessons._load_recall_state()
    assert len(state.get("sess-shared", [])) == 40


def test_reader_never_sees_torn_json():
    """While a writer hammers the lessons store, every read parses cleanly.

    load() swallows ValueError and returns [] — so distinguish 'file mid-write'
    from 'valid store' by parsing the raw bytes ourselves whenever non-empty.
    """
    from agent import lessons

    stop = threading.Event()
    bad: list = []

    def reader():
        path = lessons.get_lessons_path()
        while not stop.is_set():
            if path.is_file():
                raw = path.read_text(encoding="utf-8")
                if raw.strip():
                    try:
                        json.loads(raw)
                    except ValueError:
                        bad.append(raw[:80])
                        return
            time.sleep(0.001)

    r = threading.Thread(target=reader, daemon=True)
    r.start()
    for i in range(30):
        lessons.record_lesson(f"torn-read probe lesson {i} padding {'x' * 500}")
    stop.set()
    r.join(timeout=5)
    assert bad == []
