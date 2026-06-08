---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_voice_wrapper.py

Symbols in `tests/hermes_cli/test_voice_wrapper.py`.

- L20 `TestPublicAPI` (class)
- L21 `test_gateway_symbols_importable(self)` (method) — Match the exact import shape tui_gateway/server.py uses.
- L34 `TestNormalizeVoiceRecordKeyForPromptToolkit` (class) — Round-9 Copilot review regression on #19835.
- L44 `test_ctrl_and_alt_map_to_prompt_toolkit_form(self)` (method)
- L50 `test_control_option_opt_aliases_match_tui_parser(self)` (method)
- L57 `test_case_insensitive(self)` (method)
- L63 `test_non_string_falls_back_to_default(self)` (method)
- L71 `test_empty_string_falls_back(self)` (method)
- L76 `test_super_win_fall_back_to_default_in_cli(self)` (method) — prompt_toolkit has no super modifier, so ``super+b`` / ``win+o``
- L89 `test_strips_whitespace_within_and_around(self)` (method) — ``ctrl + b`` / ``  option + space  `` are accepted by the TUI
- L98 `test_named_key_aliases_collapse_to_prompt_toolkit_canonical(self)` (method) — TUI accepts ``return`` / ``esc`` / ``bs`` / ``del`` etc.;
- L109 `test_typoed_named_keys_fall_back_to_default(self)` (method) — ``ctrl+spcae`` would otherwise pass through as ``c-spcae`` and
- L117 `test_bare_char_and_multi_modifier_fall_back(self)` (method) — TUI parser rejects bare-char (``o``) and multi-modifier
- L126 `test_reserved_ctrl_chars_fall_back(self)` (method) — ``ctrl+c`` / ``ctrl+d`` / ``ctrl+l`` are always claimed by
- L136 `test_unknown_modifier_falls_back(self)` (method) — ``meta+b`` is ambiguous on the wire (Alt on xterm, Cmd on
- L150 `test_alt_cdl_rejected_on_macos(self, monkeypatch)` (method)
- L164 `test_alt_cdl_allowed_on_non_macos(self, monkeypatch)` (method)
- L174 `TestVoiceRecordKeyFromConfig` (class) — Round-11 Copilot review regression on #19835.
- L185 `test_dict_voice_with_string_record_key(self)` (method)
- L190 `test_non_dict_config_root(self)` (method)
- L196 `test_non_dict_voice_entry(self)` (method)
- L202 `test_missing_record_key_returns_none(self)` (method)
- L208 `test_normalizer_accepts_extractor_output_directly(self)` (method) — voice_record_key_from_config + normalize_… must compose —
- L221 `TestFormatVoiceRecordKeyForStatus` (class) — Round-10 Copilot review regression on #19835.
- L230 `test_ctrl_and_alt_letter_keys_render_canonically(self)` (method)
- L237 `test_named_keys_render_in_title_case(self)` (method)
- L244 `test_aliases_render_via_normalized_form(self)` (method)
- L251 `test_non_string_scalar_falls_back_to_ctrl_b_label(self)` (method)
- L262 `test_malformed_configs_fall_back_to_ctrl_b(self)` (method)
- L271 `TestStopWithoutStart` (class)
- L272 `test_returns_none_when_no_recording_active(self, monkeypatch)` (method) — Idempotent no-op: stop before start must not raise or touch state.
- L281 `TestSpeakTextGuards` (class)
- L283 `test_empty_text_is_noop(self, text)` (method) — Empty / whitespace-only text must return without importing tts_tool
- L293 `TestContinuousAPI` (class) — Continuous (VAD) mode API — CLI-parity loop entry points.
- L296 `test_continuous_exports(self)` (method)
- L307 `test_not_active_by_default(self, monkeypatch)` (method)
- L317 `test_stop_continuous_idempotent_when_inactive(self, monkeypatch)` (method) — stop_continuous must not raise when no loop is active — the
- L329 `test_double_start_is_idempotent(self, monkeypatch)` (method) — A second start_continuous while already active is a no-op — prevents
- L353 `test_start_returns_false_while_stopping(self, monkeypatch)` (method)
- L362 `TestContinuousLoopSimulation` (class) — End-to-end simulation of the VAD loop with a fake recorder.
- L371 `fake_recorder(self, monkeypatch)` (method)
- L424 `test_loop_auto_restarts_after_transcript(self, fake_recorder, monkeypatch)` (method)
- L455 `test_auto_restart_false_stops_after_first_transcript(self, fake_recorder, monkeypatch)` (method)
- L480 `test_auto_restart_false_retains_silent_strikes_across_starts(self, fake_recorder, monkeypatch)` (method)
- L506 `test_force_transcribe_stop_delivers_current_buffer(self, fake_recorder, monkeypatch)` (method)
- L538 `test_force_transcribe_empty_single_shots_hit_silent_limit(self, fake_recorder, monkeypatch)` (method)
- L572 `test_force_transcribe_valid_single_shot_resets_silent_strikes(self, fake_recorder, monkeypatch)` (method)
- L607 `test_force_transcribe_stop_failure_cancels_and_clears_stopping(self, fake_recorder, monkeypatch)` (method)
- L634 `test_restart_failure_reports_idle(self, fake_recorder, monkeypatch)` (method)
- L653 `test_silent_limit_halts_loop_after_three_strikes(self, fake_recorder, monkeypatch)` (method)
- L682 `test_stop_during_transcription_discards_restart(self, fake_recorder, monkeypatch)` (method) — User hits Ctrl+B mid-transcription: the in-flight transcript must
