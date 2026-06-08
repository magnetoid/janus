---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cli_init.py

Symbols in `tests/cli/test_cli_init.py`.

- L12 `_make_cli(env_overrides=None, config_overrides=None, **kwargs)` (function) — Create a HermesCLI instance with minimal mocking.
- L57 `TestMaxTurnsResolution` (class) — max_turns must always resolve to a positive integer, never None.
- L60 `test_default_max_turns_is_integer(self)` (method)
- L65 `test_explicit_max_turns_honored(self)` (method)
- L69 `test_none_max_turns_gets_default(self)` (method)
- L74 `test_env_var_max_turns(self)` (method) — Env var is used when config file doesn't set max_turns.
- L79 `test_invalid_env_var_max_turns_falls_back_to_default(self)` (method) — Invalid env values should not crash CLI init.
- L84 `test_legacy_root_max_turns_is_used_when_agent_key_exists_without_value(self)` (method)
- L88 `test_max_turns_never_none_for_agent(self)` (method) — The value passed to AIAgent must never be None (causes TypeError in run_conversation).
- L94 `TestVerboseAndToolProgress` (class)
- L95 `test_default_verbose_is_bool(self)` (method)
- L99 `test_tool_progress_mode_is_string(self)` (method)
- L105 `TestFallbackChainInit` (class)
- L106 `test_merges_new_and_legacy_fallback_config(self)` (method)
- L119 `TestBusyInputMode` (class)
- L120 `test_default_busy_input_mode_is_interrupt(self)` (method)
- L124 `test_busy_input_mode_queue_is_honored(self)` (method)
- L128 `test_unknown_busy_input_mode_falls_back_to_interrupt(self)` (method)
- L132 `test_queue_command_works_while_busy(self)` (method) — When agent is running, /queue should still put the prompt in _pending_input.
- L139 `test_queue_command_works_while_idle(self)` (method) — When agent is idle, /queue should still queue (not reject).
- L146 `test_q_alias_queues_prompt(self)` (method) — The /q alias should resolve to /queue, not /quit.
- L153 `test_queue_mode_routes_busy_enter_to_pending(self)` (method) — In queue mode, Enter while busy should go to _pending_input, not _interrupt_queue.
- L166 `test_interrupt_mode_routes_busy_enter_to_interrupt(self)` (method) — In interrupt mode (default), Enter while busy goes to _interrupt_queue.
- L179 `TestPromptToolkitTerminalCompatibility` (class)
- L180 `test_lf_enter_binds_to_submit_handler_posix(self)` (method) — Some thin PTYs deliver Enter as LF/c-j instead of CR/enter.
- L240 `test_cpr_warning_callback_is_disabled(self)` (method)
- L251 `TestSingleQueryState` (class)
- L252 `test_voice_and_interrupt_state_initialized_before_run(self)` (method) — Single-query mode calls chat() without going through run().
- L262 `TestHistoryDisplay` (class)
- L263 `test_history_numbers_only_visible_messages_and_summarizes_tools(self, capsys)` (method)
- L293 `test_history_shows_recent_sessions_when_current_chat_is_empty(self, capsys)` (method)
- L321 `test_resume_without_target_lists_recent_sessions(self, capsys)` (method)
- L348 `test_resume_updates_hermes_session_id_env_and_context(self, tmp_path)` (method)
- L375 `test_resume_list_shows_full_long_titles(self, capsys)` (method) — Long session titles render in full in the /resume table — not
- L403 `test_sessions_command_no_args_lists_recent_sessions(self, capsys)` (method) — /sessions with no args prints the recent-sessions table (TUI parity).
- L433 `test_sessions_list_subcommand_lists_recent_sessions(self, capsys)` (method) — /sessions list is an explicit alias for the no-arg list view.
- L454 `test_sessions_with_target_delegates_to_resume(self)` (method) — /sessions <id_or_title> behaves identically to /resume <id_or_title>.
- L469 `test_sessions_command_is_dispatched(self)` (method) — /sessions must hit _handle_sessions_command, not fall through.
- L487 `TestRootLevelProviderOverride` (class) — Root-level provider/base_url in config.yaml must NOT override model.provider.
- L490 `test_model_provider_wins_over_root_provider(self, tmp_path, monkeypatch)` (method) — model.provider takes priority — root-level provider is only a fallback.
- L513 `test_root_provider_used_as_fallback_when_model_provider_missing(self, tmp_path, monkeypatch)` (method) — Legacy root-level provider still populates model.provider in the CLI loader.
- L536 `test_root_base_url_used_as_fallback_when_model_base_url_missing(self, tmp_path, monkeypatch)` (method) — Legacy root-level base_url still populates model.base_url in the CLI loader.
- L558 `test_normalize_root_model_keys_moves_to_model(self)` (method) — _normalize_root_model_keys migrates root keys into model section.
- L577 `test_normalize_root_model_keys_does_not_override_existing(self)` (method) — Existing model.provider is never overridden by root-level key.
- L592 `test_normalize_root_context_length_migrates_to_model(self)` (method) — Root-level context_length is migrated into the model section.
- L606 `test_normalize_root_context_length_does_not_override_existing(self)` (method) — Existing model.context_length is not overridden by root-level key.
- L621 `test_normalize_root_context_length_with_string_model(self)` (method) — Root-level context_length is migrated even when model is a string.
- L636 `TestProviderResolution` (class)
- L637 `test_api_key_is_string_or_none(self)` (method)
- L641 `test_base_url_is_string(self)` (method)
- L646 `test_model_is_string(self)` (method)
