---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/conftest.py

Symbols in `tests/conftest.py`.

- L162 `_looks_like_credential(name: str)` (function) — True if env var name matches a credential-shaped pattern.
- L328 `_hermetic_environment(tmp_path, monkeypatch)` (function) — Blank out all credential/behavioral env vars so local and CI match.
- L399 `_isolate_hermes_home(_hermetic_environment)` (function) — Alias preserved for any test that yields this name explicitly.
- L422 `tmp_dir(tmp_path)` (function) — Provide a temporary directory that is cleaned up automatically.
- L428 `mock_config()` (function) — Return a minimal hermes config dict suitable for unit tests.
- L453 `_ensure_current_event_loop(request)` (function) — Provide a default event loop for sync tests that call get_event_loop().
- L528 `pytest_configure(config)` (function) — Register markers used by hermetic conftest.
- L539 `_live_system_guard(request, monkeypatch)` (function) — Block real os.kill / systemctl / gateway-pid scans during tests.
