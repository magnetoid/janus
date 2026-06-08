---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_save_conversation_location.py

Symbols in `tests/cli/test_save_conversation_location.py`.

- L23 `hermes_home(tmp_path, monkeypatch)` (function)
- L35 `_make_stub_cli(history)` (function) — Build a minimal object exposing just what save_conversation uses.
- L45 `test_save_conversation_writes_under_hermes_home(hermes_home, tmp_path, monkeypatch, capsys)` (function) — Snapshot must land under ~/.hermes/sessions/saved/, not CWD.
- L90 `test_save_conversation_empty_history_does_nothing(hermes_home, capsys)` (function)
