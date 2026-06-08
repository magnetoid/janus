---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_runner_startup_failures.py

Symbols in `tests/gateway/test_runner_startup_failures.py`.

- L10 `_RetryableFailureAdapter` (class)
- L11 `__init__(self)` (method)
- L14 `connect(self)` (method)
- L22 `disconnect(self)` (method)
- L25 `send(self, chat_id, content, reply_to=None, metadata=None)` (method)
- L28 `get_chat_info(self, chat_id)` (method)
- L32 `_DisabledAdapter` (class)
- L33 `__init__(self)` (method)
- L36 `connect(self)` (method)
- L39 `disconnect(self)` (method)
- L42 `send(self, chat_id, content, reply_to=None, metadata=None)` (method)
- L45 `get_chat_info(self, chat_id)` (method)
- L49 `_SuccessfulAdapter` (class)
- L50 `__init__(self)` (method)
- L53 `connect(self)` (method)
- L56 `disconnect(self)` (method)
- L59 `send(self, chat_id, content, reply_to=None, metadata=None)` (method)
- L62 `get_chat_info(self, chat_id)` (method)
- L67 `test_runner_stays_alive_for_retryable_startup_errors(monkeypatch, tmp_path)` (function) — Retryable startup errors should leave the gateway running in
- L100 `test_runner_allows_cron_only_mode_when_no_platforms_are_enabled(monkeypatch, tmp_path)` (function)
- L120 `test_runner_records_connected_platform_state_on_success(monkeypatch, tmp_path)` (function)
- L145 `test_start_gateway_verbosity_imports_redacting_formatter(monkeypatch, tmp_path)` (function) — Verbosity != None must not crash with NameError on RedactingFormatter (#8044).
- L178 `test_start_gateway_replace_force_uses_terminate_pid(monkeypatch, tmp_path)` (function)
- L228 `test_start_gateway_replace_writes_takeover_marker_before_sigterm(monkeypatch, tmp_path)` (function) — --replace must write a takeover marker BEFORE sending SIGTERM.
- L314 `test_start_gateway_replace_clears_marker_on_permission_denied(monkeypatch, tmp_path)` (function) — If we fail to kill the existing PID (permission denied), clean up the
- L353 `test_runner_degrades_gracefully_when_all_adapters_missing(monkeypatch, tmp_path, caplog)` (function) — When all enabled platforms have no adapter (missing library or credentials),
- L393 `test_runner_warns_when_docker_gateway_lacks_explicit_output_mount(monkeypatch, tmp_path, caplog)` (function)
