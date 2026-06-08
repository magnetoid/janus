---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_install_sh_setup_wizard_tty_probe.py

Symbols in `tests/test_install_sh_setup_wizard_tty_probe.py`.

- L31 `_extract_function_body(name: str)` (function) — Return the body of ``<name>()`` as a single string.
- L48 `test_tty_gate_does_not_use_existence_only_check(fn_name: str)` (function) — The bare ``-e`` test is the bug — no spelling of it should remain.
- L74 `test_tty_gate_uses_open_based_probe(fn_name: str)` (function) — The gate must actually attempt to open ``/dev/tty``.
