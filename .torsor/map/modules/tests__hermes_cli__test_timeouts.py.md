---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_timeouts.py

Symbols in `tests/hermes_cli/test_timeouts.py`.

- L11 `_write_config(tmp_path, body: str)` (function)
- L15 `test_model_timeout_override_wins(monkeypatch, tmp_path)` (function)
- L32 `test_provider_timeout_used_when_no_model_override(monkeypatch, tmp_path)` (function)
- L46 `test_model_stale_timeout_override_wins(monkeypatch, tmp_path)` (function)
- L63 `test_provider_stale_timeout_used_when_no_model_override(monkeypatch, tmp_path)` (function)
- L77 `test_missing_timeout_returns_none(monkeypatch, tmp_path)` (function)
- L94 `test_invalid_timeout_values_return_none(monkeypatch, tmp_path)` (function)
- L115 `test_invalid_stale_timeout_values_return_none(monkeypatch, tmp_path)` (function)
- L133 `test_anthropic_adapter_honors_timeout_kwarg()` (function) — build_anthropic_client(timeout=X) overrides the 900s default read timeout.
- L152 `test_resolved_api_call_timeout_priority(monkeypatch, tmp_path)` (function) — AIAgent._resolved_api_call_timeout() honors config > env > default priority.
- L215 `test_resolved_api_call_stale_timeout_priority(monkeypatch, tmp_path)` (function) — AIAgent stale timeout honors config > env > default priority.
- L271 `test_default_non_stream_stale_timeout_auto_disables_for_local_endpoints(monkeypatch, tmp_path)` (function)
- L291 `test_explicit_non_stream_stale_timeout_is_honored_for_local_endpoints(monkeypatch, tmp_path)` (function)
