---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/test_google_meet_node.py

Symbols in `tests/plugins/test_google_meet_node.py`.

- L20 `_isolate_home(tmp_path, monkeypatch)` (function)
- L31 `test_protocol_encode_decode_roundtrip()` (function)
- L44 `test_protocol_make_request_autogenerates_id()` (function)
- L53 `test_protocol_make_request_rejects_bad_input()` (function)
- L64 `test_protocol_decode_raises_on_malformed()` (function)
- L77 `test_protocol_validate_request_happy_path()` (function)
- L86 `test_protocol_validate_request_rejects_bad_token()` (function)
- L95 `test_protocol_validate_request_rejects_unknown_type()` (function)
- L104 `test_protocol_validate_request_rejects_missing_id()` (function)
- L113 `test_protocol_validate_request_rejects_non_dict_payload()` (function)
- L121 `test_protocol_error_envelope_shape()` (function)
- L132 `test_registry_add_get_roundtrip_persists(tmp_path)` (function)
- L149 `test_registry_get_returns_none_when_missing(tmp_path)` (function)
- L156 `test_registry_remove(tmp_path)` (function)
- L166 `test_registry_list_all_sorted(tmp_path)` (function)
- L176 `test_registry_resolve_auto_picks_single(tmp_path)` (function)
- L186 `test_registry_resolve_ambiguous_returns_none(tmp_path)` (function)
- L195 `test_registry_resolve_empty_returns_none(tmp_path)` (function)
- L202 `test_registry_resolve_by_name(tmp_path)` (function)
- L214 `test_registry_defaults_to_hermes_home(tmp_path, monkeypatch)` (function)
- L229 `test_server_ensure_token_generates_and_persists(tmp_path)` (function)
- L247 `test_server_get_token_is_idempotent(tmp_path)` (function)
- L254 `_run(coro)` (function)
- L258 `test_server_handle_request_rejects_bad_token(tmp_path)` (function)
- L270 `test_server_handle_request_ping(tmp_path)` (function)
- L283 `test_server_handle_request_status_dispatches_to_pm(tmp_path, monkeypatch)` (function)
- L300 `test_server_handle_request_start_bot_dispatches(tmp_path, monkeypatch)` (function)
- L328 `test_server_handle_request_start_bot_missing_url(tmp_path)` (function)
- L340 `test_server_handle_request_stop_dispatches(tmp_path, monkeypatch)` (function)
- L361 `test_server_handle_request_transcript(tmp_path, monkeypatch)` (function)
- L383 `test_server_handle_request_say_enqueues_when_active(tmp_path, monkeypatch)` (function)
- L405 `test_server_handle_request_say_without_active_still_ok(tmp_path, monkeypatch)` (function)
- L421 `test_server_handle_request_wraps_pm_exceptions(tmp_path, monkeypatch)` (function)
- L443 `_FakeWS` (class) — Minimal context-manager stand-in for websockets.sync.client.connect.
- L446 `__init__(self, reply_builder)` (method)
- L450 `__enter__(self)` (method)
- L453 `__exit__(self, exc_type, exc, tb)` (method)
- L456 `send(self, raw)` (method)
- L459 `recv(self, timeout=None)` (method)
- L463 `_install_fake_ws(monkeypatch, reply_builder)` (function)
- L479 `test_client_rpc_sends_correct_envelope_and_parses_response(monkeypatch)` (function)
- L501 `test_client_rpc_raises_on_error_envelope(monkeypatch)` (function)
- L516 `test_client_rpc_raises_on_id_mismatch(monkeypatch)` (function)
- L530 `test_client_convenience_methods_hit_correct_types(monkeypatch)` (function)
- L561 `test_client_init_rejects_bad_args()` (function)
- L574 `_build_parser()` (function)
- L582 `test_cli_approve_list_remove(capsys)` (function)
- L605 `test_cli_list_empty(capsys)` (function)
- L613 `test_cli_remove_missing_returns_nonzero()` (function)
- L620 `test_cli_status_pings_via_node_client(capsys, monkeypatch)` (function)
- L646 `test_cli_status_unknown_node_fails(capsys)` (function)
- L653 `test_cli_status_reports_client_error(capsys, monkeypatch)` (function)
