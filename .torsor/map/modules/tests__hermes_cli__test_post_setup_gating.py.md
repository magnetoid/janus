---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_post_setup_gating.py

Symbols in `tests/hermes_cli/test_post_setup_gating.py`.

- L17 `TestPostSetupGate` (class)
- L18 `test_cua_driver_missing_forces_setup(self, monkeypatch, tmp_path)` (method) — When cua-driver isn't on PATH, the gate must return True so the
- L30 `test_cua_driver_installed_skips_setup(self, monkeypatch, tmp_path)` (method) — When cua-driver is already on PATH, the gate must return False
- L46 `test_post_setup_predicate_exception_does_not_block(self, monkeypatch)` (method) — A predicate that raises must be treated as 'satisfied' so a
- L57 `test_unregistered_post_setup_treated_as_satisfied(self)` (method) — post_setup keys without a registered predicate must default to
- L65 `test_cua_driver_predicate_registered(self)` (method) — Keep an explicit pin on the cua_driver entry so accidental
