"""Tamper-evident autonomy audit log (gap G12).

A hash-chained append-only JSONL stream for autonomy-critical events (freeze /
unfreeze, promotions, injection blocks). Each row commits to the previous row's
hash, so removing, reordering, or editing any row breaks the chain from that
point — an operator (or a governance review) can prove the record is intact.
"""
from __future__ import annotations

import json

from agent import audit_log


def test_append_returns_chained_row():
    r1 = audit_log.append_event("autonomy_freeze", {"reason": "manual"})
    r2 = audit_log.append_event("autonomy_unfreeze", {})
    assert r1["prev_hash"] == ""              # genesis
    assert r2["prev_hash"] == r1["hash"]      # chained
    assert r1["hash"] != r2["hash"]
    assert r1["kind"] == "autonomy_freeze"
    assert r1["data"] == {"reason": "manual"}


def test_verify_ok_on_intact_chain():
    for i in range(5):
        audit_log.append_event("event", {"i": i})
    ok, broken = audit_log.verify()
    assert ok is True
    assert broken is None


def test_verify_detects_edited_row():
    for i in range(4):
        audit_log.append_event("event", {"i": i})
    path = audit_log.audit_path()
    rows = [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]
    rows[1]["data"] = {"i": 999}  # tamper with the payload, leave the hash
    path.write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")
    ok, broken = audit_log.verify()
    assert ok is False
    assert broken == 1


def test_verify_detects_removed_row():
    for i in range(4):
        audit_log.append_event("event", {"i": i})
    path = audit_log.audit_path()
    rows = [x for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]
    del rows[2]  # drop a row → the next row's prev_hash no longer matches
    path.write_text("\n".join(rows) + "\n", encoding="utf-8")
    ok, broken = audit_log.verify()
    assert ok is False
    assert broken == 2


def test_verify_empty_log_is_ok():
    ok, broken = audit_log.verify()
    assert ok is True
    assert broken is None


def test_append_never_raises_on_bad_payload():
    # Non-JSON-serializable data must not blow up the caller (best-effort).
    r = audit_log.append_event("event", {"obj": object()})
    assert r is None or isinstance(r, dict)


def test_freeze_unfreeze_are_audited():
    """The kill switch writes tamper-evident freeze/unfreeze events (gap G12)."""
    from agent import autonomy_guard as ag
    ag.freeze("manual test")
    ag.unfreeze()
    rows = audit_log._load_rows(audit_log.audit_path())
    kinds = [r["kind"] for r in rows]
    assert "autonomy_freeze" in kinds
    assert "autonomy_unfreeze" in kinds
    ok, broken = audit_log.verify()
    assert ok is True and broken is None
