---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_browser_cloud_fallback.py

Symbols in `tests/tools/test_browser_cloud_fallback.py`.

- L14 `_reset_session_state(monkeypatch)` (function) — Clear caches so each test starts fresh.
- L23 `TestCloudProviderRuntimeFallback` (class) — Tests for _get_session_info cloud → local fallback.
- L26 `test_cloud_failure_falls_back_to_local(self, monkeypatch)` (method) — When cloud provider.create_session raises, fall back to local.
- L43 `test_cloud_success_no_fallback(self, monkeypatch)` (method) — When cloud succeeds, no fallback markers are present.
- L63 `test_cloud_and_local_both_fail(self, monkeypatch)` (method) — When both cloud and local fail, raise RuntimeError with both contexts.
- L79 `test_no_provider_uses_local_directly(self, monkeypatch)` (method) — When no cloud provider is configured, local mode is used with no fallback markers.
- L91 `test_cdp_override_bypasses_provider(self, monkeypatch)` (method) — CDP override takes priority — cloud provider is never consulted.
- L104 `test_fallback_logs_warning_with_provider_name(self, monkeypatch, caplog)` (method) — Fallback emits a warning log with the provider class name and error.
- L122 `test_cloud_failure_does_not_poison_next_task(self, monkeypatch)` (method) — A fallback for one task_id doesn't affect a new task_id when cloud recovers.
- L154 `test_cloud_returns_invalid_session_triggers_fallback(self, monkeypatch)` (method) — Cloud provider returning None or empty dict triggers fallback.
