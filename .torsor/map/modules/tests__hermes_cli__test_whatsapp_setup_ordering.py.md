---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_whatsapp_setup_ordering.py

Symbols in `tests/hermes_cli/test_whatsapp_setup_ordering.py`.

- L26 `isolated_home(tmp_path, monkeypatch)` (function)
- L39 `_env_value(hermes_home: Path, key: str)` (function)
- L52 `test_aborted_setup_does_not_enable_whatsapp(isolated_home, monkeypatch)` (function) — User picks mode 1, then Ctrl+C's at the allowed-users prompt.
- L87 `test_existing_pairing_skip_branch_enables_whatsapp(isolated_home, monkeypatch)` (function) — User runs ``hermes whatsapp`` with an existing paired session and
