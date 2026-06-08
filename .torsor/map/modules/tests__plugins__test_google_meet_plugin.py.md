---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/test_google_meet_plugin.py

Symbols in `tests/plugins/test_google_meet_plugin.py`.

- L27 `_isolate_home(tmp_path, monkeypatch)` (function)
- L38 `test_is_safe_meet_url_accepts_standard_meet_codes()` (function)
- L47 `test_is_safe_meet_url_rejects_non_meet_urls()` (function)
- L65 `test_meeting_id_extraction()` (function)
- L79 `test_bot_state_dedupes_captions_and_flushes_status(tmp_path)` (function)
- L102 `test_bot_state_ignores_blank_text(tmp_path)` (function)
- L117 `test_parse_duration()` (function)
- L132 `test_start_refuses_unsafe_url()` (function)
- L140 `test_status_reports_no_active_meeting()` (function)
- L148 `test_start_spawns_subprocess_and_writes_active_pointer(tmp_path)` (function) — Verify start() wires env vars correctly and records the pid.
- L189 `test_transcript_reads_last_n_lines(tmp_path)` (function)
- L213 `test_stop_signals_process_and_clears_pointer(tmp_path)` (function)
- L249 `test_meet_join_handler_missing_url_returns_error()` (function)
- L257 `test_meet_join_handler_respects_safety_gate()` (function)
- L266 `test_meet_join_handler_returns_error_when_playwright_missing()` (function)
- L275 `test_meet_say_requires_text()` (function)
- L283 `test_meet_say_no_active_meeting()` (function)
- L292 `test_meet_status_and_transcript_no_active()` (function)
- L299 `test_meet_leave_no_active()` (function)
- L310 `test_on_session_end_noop_when_nothing_active()` (function)
- L318 `test_on_session_end_stops_live_bot()` (function)
- L332 `test_register_refuses_on_windows()` (function)
- L348 `test_register_wires_tools_cli_and_hook_on_linux()` (function)
- L372 `test_enqueue_say_requires_text()` (function)
- L378 `test_enqueue_say_no_active_meeting()` (function)
- L385 `test_enqueue_say_rejects_transcribe_mode(tmp_path)` (function)
- L400 `test_enqueue_say_writes_jsonl_in_realtime_mode()` (function)
- L421 `test_start_passes_mode_into_active_record()` (function)
- L438 `test_start_realtime_env_vars_threaded_through()` (function)
- L466 `test_meet_join_accepts_realtime_mode()` (function)
- L479 `test_meet_join_rejects_bad_mode()` (function)
- L494 `test_meet_join_unknown_node_returns_clear_error()` (function)
- L505 `test_meet_join_routes_to_registered_node()` (function)
- L524 `test_meet_say_routes_to_node()` (function)
- L539 `test_meet_join_auto_node_selects_sole_registered()` (function)
- L557 `test_meet_join_auto_node_ambiguous_returns_error()` (function)
- L573 `test_cli_register_includes_node_subcommand()` (function) — `hermes meet` argparse tree includes the node subtree.
- L587 `test_cli_join_accepts_mode_and_node_flags()` (function)
- L602 `test_cli_say_subcommand_exists()` (function)
- L618 `test_bot_state_exposes_v2_telemetry_fields(tmp_path)` (function)
- L649 `test_looks_like_human_speaker()` (function)
- L660 `test_detect_admission_returns_false_on_error()` (function)
- L669 `test_detect_admission_true_when_probe_returns_true()` (function)
- L678 `test_detect_denied_returns_false_on_error()` (function)
- L691 `test_realtime_session_cancel_response_when_disconnected()` (function)
- L699 `test_realtime_session_cancel_response_sends_cancel_frame()` (function)
- L716 `test_realtime_session_counters_initialized()` (function)
- L728 `test_cli_install_subcommand_is_registered()` (function)
- L741 `test_cli_install_flags_parse()` (function)
- L753 `test_cmd_install_refuses_windows(capsys)` (function)
- L764 `test_cmd_install_runs_pip_and_playwright(capsys)` (function) — End-to-end wiring: pip + playwright install invoked, returncodes handled.
- L792 `test_cmd_install_realtime_skips_when_deps_present(capsys)` (function) — When paplay + pactl are already on PATH, no sudo call happens.
