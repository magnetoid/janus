---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/test_langfuse_plugin.py

Symbols in `tests/plugins/test_langfuse_plugin.py`.

- L22 `TestManifest` (class)
- L23 `test_plugin_directory_exists(self)` (method)
- L28 `test_manifest_fields(self)` (method)
- L49 `TestDiscovery` (class)
- L50 `test_plugin_is_discovered_as_standalone_opt_in(self, tmp_path, monkeypatch)` (method) — Scanner should find the plugin but NOT load it by default.
- L77 `TestRuntimeGate` (class)
- L78 `_fresh_plugin(self)` (method) — Import the plugin module fresh (clears any cached client).
- L84 `test_get_langfuse_returns_none_without_credentials(self, monkeypatch)` (method)
- L94 `test_get_langfuse_caches_failure_no_config_load(self, monkeypatch)` (method) — A miss must be cached — no per-hook config.yaml reads, no env re-reads.
- L128 `test_get_langfuse_does_not_import_hermes_config(self, monkeypatch)` (method) — The plugin must not re-read config.yaml per hook.
- L153 `TestHooksInert` (class)
- L154 `test_hooks_noop_without_client(self, monkeypatch)` (method) — All 6 hooks must return without raising when _get_langfuse() is None.
- L190 `_FakeLangfuse` (class) — Stand-in for the real :class:`langfuse.Langfuse` so tests don't
- L200 `__init__(self, **kwargs)` (method)
- L205 `TestPlaceholderKeyDetection` (class)
- L208 `_fresh_plugin(self, monkeypatch=None)` (method)
- L222 `_clear_env(monkeypatch)` (method)
- L232 `test_redact_key_preview_empty(self, monkeypatch)` (method)
- L237 `test_redact_key_preview_short_value_echoed(self, monkeypatch)` (method) — Short placeholder strings are echoed in full so the operator
- L245 `test_redact_key_preview_long_value_truncated(self, monkeypatch)` (method) — If an operator pasted a real secret into the wrong env var the
- L255 `test_validate_langfuse_key_accepts_documented_prefix(self, monkeypatch)` (method)
- L265 `test_validate_langfuse_key_rejects_wrong_prefix(self, monkeypatch)` (method)
- L275 `test_validate_langfuse_key_unknown_name_passes(self, monkeypatch)` (method) — Defensive: an env var with no registered prefix is trusted.
- L287 `test_placeholder_public_key_warns_and_skips(self, monkeypatch, caplog)` (method)
- L304 `test_placeholder_secret_key_warns_and_skips(self, monkeypatch, caplog)` (method)
- L319 `test_both_placeholders_one_warning_with_both_keys(self, monkeypatch, caplog)` (method)
- L336 `test_repeated_calls_do_not_re_warn(self, monkeypatch, caplog)` (method) — The cached ``_INIT_FAILED`` sentinel must short-circuit
- L365 `test_common_placeholders_detected(self, monkeypatch, caplog, placeholder)` (method) — A grab-bag of values that real-world ``.env.example`` templates
- L376 `test_legacy_LANGFUSE_PUBLIC_KEY_also_validated(self, monkeypatch, caplog)` (method) — The plugin reads both the canonical HERMES_-prefixed env var and
- L392 `test_missing_credentials_still_skip_silently(self, monkeypatch, caplog)` (method) — Missing-creds is the documented opt-out path (operator hasn't
- L406 `test_sdk_not_installed_still_skips_silently(self, monkeypatch, caplog)` (method) — If the langfuse SDK isn't installed at all, the placeholder
- L427 `test_valid_prefixes_do_not_trigger_placeholder_warning(self, monkeypatch, caplog)` (method) — Real Langfuse keys (``pk-lf-…`` / ``sk-lf-…``) must pass the
- L448 `TestRequestMessageCoercion` (class)
- L449 `test_prefers_request_messages_then_messages_then_history_then_user_message(self)` (method)
- L471 `TestToolCallOutputBackfill` (class)
- L472 `test_post_tool_call_backfills_matching_turn_tool_call_output(self, monkeypatch)` (method)
- L518 `test_serialize_messages_keeps_tool_name_and_call_id(self)` (method)
- L536 `test_serialize_tool_calls_emits_openai_style_function_shape(self)` (method)
- L561 `TestToolObservationKeying` (class) — Tests for pre/post tool_call observation matching when tool_call_id is absent.
- L564 `_make_mod(self)` (method)
- L568 `test_empty_tool_call_id_single_tool_sets_output(self, monkeypatch)` (method)
- L598 `test_empty_tool_call_id_observations_are_fifo_within_tool_name(self, monkeypatch)` (method) — Two queued observations are consumed in FIFO order so the first
- L635 `test_threaded_post_calls_preserve_fifo_under_lock(self, monkeypatch)` (method) — The actual concurrency contract: when 8 threads race to drain
- L680 `test_explicit_tool_call_id_uses_tools_dict(self, monkeypatch)` (method) — When tool_call_id is present, pending_tools_by_name is not touched.
