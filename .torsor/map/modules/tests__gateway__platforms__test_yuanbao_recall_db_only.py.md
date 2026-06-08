---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/gateway/platforms/test_yuanbao_recall_db_only.py

Symbols in `tests/gateway/platforms/test_yuanbao_recall_db_only.py`.

- L15 `_pin_db(monkeypatch, tmp_path)` (function) — Force SessionDB() to write into tmp_path instead of the real ~/.hermes.
- L21 `test_recall_branch_a1_exact_id_match_round_trips_through_db(tmp_path, monkeypatch)` (function) — A user message persisted with ``message_id`` must round-trip through
- L61 `test_recall_branch_a2_content_match_when_no_platform_id(tmp_path, monkeypatch)` (function) — Rows that lack a platform_message_id (e.g. agent-processed @bot
