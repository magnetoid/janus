---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_hermes_logging.py

Symbols in `tests/test_hermes_logging.py`.

- L18 `_reset_logging_state()` (function) — Reset the module-level sentinel and clean up root logger handlers
- L55 `hermes_home(tmp_path, monkeypatch)` (function) — Provide an isolated HERMES_HOME for logging tests.
- L65 `TestSetupLogging` (class) — setup_logging() creates agent.log + errors.log with RotatingFileHandler.
- L68 `test_creates_log_directory(self, hermes_home)` (method)
- L73 `test_creates_agent_log_handler(self, hermes_home)` (method)
- L85 `test_creates_errors_log_handler(self, hermes_home)` (method)
- L97 `test_idempotent_no_duplicate_handlers(self, hermes_home)` (method)
- L109 `test_force_reinitializes(self, hermes_home)` (method)
- L123 `test_custom_log_level(self, hermes_home)` (method)
- L134 `test_custom_max_size_and_backup(self, hermes_home)` (method)
- L148 `test_suppresses_noisy_loggers(self, hermes_home)` (method)
- L155 `test_writes_to_agent_log(self, hermes_home)` (method)
- L170 `test_warnings_appear_in_both_logs(self, hermes_home)` (method)
- L184 `test_info_not_in_errors_log(self, hermes_home)` (method)
- L197 `test_reads_config_yaml(self, hermes_home)` (method) — setup_logging reads logging.level from config.yaml.
- L215 `test_explicit_params_override_config(self, hermes_home)` (method) — Explicit function params take precedence over config.yaml.
- L231 `test_record_factory_installed(self, hermes_home)` (method) — The custom record factory injects session_tag on all records.
- L243 `TestGatewayMode` (class) — setup_logging(mode='gateway') creates a filtered gateway.log.
- L246 `test_gateway_log_created(self, hermes_home)` (method)
- L257 `test_gateway_log_not_created_in_cli_mode(self, hermes_home)` (method)
- L268 `test_gateway_log_created_after_cli_init(self, hermes_home)` (method) — Gateway mode attaches gateway.log even after earlier CLI init.
- L290 `test_gateway_log_created_after_cli_init_without_duplicate_handlers(self, hermes_home)` (method) — Repeated gateway setup calls do not attach duplicate gateway handlers.
- L304 `test_gateway_log_receives_gateway_records(self, hermes_home)` (method) — gateway.log captures records from gateway.* loggers.
- L318 `test_gateway_log_rejects_non_gateway_records(self, hermes_home)` (method) — gateway.log does NOT capture records from tools.*, agent.*, etc.
- L337 `test_agent_log_still_receives_all(self, hermes_home)` (method) — agent.log (catch-all) still receives gateway AND tool records.
- L362 `TestGuiMode` (class) — setup_logging(mode='gui') creates a filtered gui.log.
- L365 `test_gui_log_created(self, hermes_home)` (method)
- L376 `test_gui_log_created_after_cli_init(self, hermes_home)` (method)
- L388 `test_gui_log_receives_only_gui_components(self, hermes_home)` (method)
- L406 `TestSessionContext` (class) — set_session_context / clear_session_context + _SessionFilter.
- L409 `test_session_tag_in_log_output(self, hermes_home)` (method) — When session context is set, log lines include [session_id].
- L425 `test_no_session_tag_without_context(self, hermes_home)` (method) — Without session context, log lines have no session tag.
- L445 `test_clear_session_context(self, hermes_home)` (method) — After clearing, session tag disappears.
- L461 `test_session_context_thread_isolated(self, hermes_home)` (method) — Session context is per-thread — one thread's context doesn't leak.
- L499 `TestRecordFactory` (class) — Unit tests for the custom LogRecord factory.
- L502 `test_record_has_session_tag(self)` (method) — Every record gets a session_tag attribute.
- L508 `test_empty_tag_without_context(self)` (method)
- L514 `test_tag_with_context(self)` (method)
- L520 `test_idempotent_install(self)` (method) — Calling _install_session_record_factory() twice doesn't double-wrap.
- L528 `test_works_with_any_handler(self)` (method) — A handler using %(session_tag)s works even without _SessionFilter.
- L544 `TestComponentFilter` (class) — Unit tests for _ComponentFilter.
- L547 `test_passes_matching_prefix(self)` (method)
- L554 `test_passes_nested_matching_prefix(self)` (method)
- L561 `test_blocks_non_matching(self)` (method)
- L568 `test_multiple_prefixes(self)` (method)
- L584 `TestComponentPrefixes` (class) — COMPONENT_PREFIXES covers the expected components.
- L587 `test_gateway_prefix(self)` (method)
- L594 `test_agent_prefix(self)` (method)
- L600 `test_tools_prefix(self)` (method)
- L603 `test_cli_prefix(self)` (method)
- L608 `test_cron_prefix(self)` (method)
- L611 `test_gui_prefix(self)` (method)
- L617 `TestSetupVerboseLogging` (class) — setup_verbose_logging() adds a DEBUG-level console handler.
- L620 `test_adds_stream_handler(self, hermes_home)` (method)
- L634 `test_idempotent(self, hermes_home)` (method)
- L649 `TestAddRotatingHandler` (class) — _add_rotating_handler() is idempotent and creates the directory.
- L652 `test_creates_directory(self, tmp_path)` (method)
- L670 `test_no_duplicate_for_same_path(self, tmp_path)` (method)
- L697 `test_log_filter_attached(self, tmp_path)` (method) — Optional log_filter is attached to the handler.
- L720 `test_no_session_filter_on_handler(self, tmp_path)` (method) — Handlers rely on record factory, not per-handler _SessionFilter.
- L750 `test_managed_mode_initial_open_sets_group_writable(self, tmp_path)` (method)
- L774 `test_managed_mode_rollover_sets_group_writable(self, tmp_path)` (method)
- L804 `TestReadLoggingConfig` (class) — _read_logging_config() reads from config.yaml.
- L807 `test_returns_none_when_no_config(self, hermes_home)` (method)
- L813 `test_reads_logging_section(self, hermes_home)` (method)
- L823 `test_handles_missing_logging_section(self, hermes_home)` (method)
- L832 `TestExternalRotationRecovery` (class) — _ManagedRotatingFileHandler recovers from external rotation.
- L843 `_make_handler(self, log_path: Path)` (method)
- L852 `_emit(self, handler: logging.Handler, msg: str)` (method)
- L862 `test_recovers_after_external_rename(self, tmp_path)` (method) — logrotate-style external rename: ``mv gateway.log gateway.log.1``.
- L890 `test_recovers_after_external_unlink(self, tmp_path)` (method) — ``rm gateway.log`` then keep writing — handler recreates the file.
- L907 `test_external_truncate_does_not_force_reopen(self, tmp_path)` (method) — ``: > gateway.log`` keeps the same inode — no reopen needed.
- L931 `test_normal_rollover_still_works(self, tmp_path)` (method) — Handler-driven ``doRollover()`` must continue to work normally.
- L960 `test_gateway_log_attached_after_external_rotation_then_re_setup(self, hermes_home)` (method) — End-to-end Allen-reproduction: gateway.log gets externally rotated,
- L1003 `TestSafeStderr` (class) — Tests for _safe_stderr() — Unicode tolerance on Windows console.
- L1006 `test_returns_stderr_on_utf8_system(self, monkeypatch)` (method) — On UTF-8 systems, _safe_stderr() returns sys.stderr unchanged.
- L1016 `test_wraps_non_utf8_stderr(self, monkeypatch)` (method) — On non-UTF-8 systems (e.g. Windows cp949), wraps stderr with UTF-8.
- L1039 `test_handler_emits_unicode_without_crash(self, tmp_path)` (method) — StreamHandler with _safe_stderr can emit Unicode messages.
