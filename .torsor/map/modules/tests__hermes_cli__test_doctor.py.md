---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_doctor.py

Symbols in `tests/hermes_cli/test_doctor.py`.

- L19 `TestDoctorPlatformHints` (class)
- L20 `test_termux_package_hint(self, monkeypatch)` (method)
- L27 `test_non_termux_package_hint_defaults_to_apt(self, monkeypatch)` (method)
- L36 `TestProviderEnvDetection` (class)
- L37 `test_detects_openai_api_key(self)` (method)
- L41 `test_detects_custom_endpoint_without_openrouter_key(self)` (method)
- L45 `test_detects_kimi_cn_api_key(self)` (method)
- L49 `test_returns_false_when_no_provider_settings(self)` (method)
- L54 `TestDoctorEnvFileEncoding` (class) — Regression for #18637 (bug 3): `hermes doctor` crashed on Windows
- L59 `test_doctor_reads_env_as_utf8_even_when_locale_is_not_utf8(self, monkeypatch, tmp_path)` (method)
- L105 `TestDoctorToolAvailabilityOverrides` (class)
- L106 `test_marks_honcho_available_when_configured(self, monkeypatch)` (method)
- L117 `test_leaves_honcho_unavailable_when_not_configured(self, monkeypatch)` (method)
- L129 `test_marks_kanban_available_only_when_missing_worker_env_gate(self, monkeypatch)` (method)
- L141 `test_leaves_kanban_unavailable_when_worker_env_is_set(self, monkeypatch)` (method)
- L153 `test_leaves_non_worker_kanban_failure_unavailable(self, monkeypatch)` (method)
- L165 `test_kanban_doctor_detail_explains_worker_gate(self, monkeypatch)` (method)
- L171 `TestHonchoDoctorConfigDetection` (class)
- L172 `test_reports_configured_when_enabled_with_api_key(self, monkeypatch)` (method)
- L182 `test_reports_not_configured_without_api_key(self, monkeypatch)` (method)
- L193 `test_run_doctor_sets_interactive_env_for_tool_checks(monkeypatch, tmp_path)` (function) — Doctor should present CLI-gated tools as available in CLI context.
- L222 `test_check_gateway_service_linger_warns_when_disabled(monkeypatch, tmp_path, capsys)` (function)
- L242 `test_check_gateway_service_linger_skips_when_service_not_installed(monkeypatch, tmp_path, capsys)` (function)
- L259 `TestDoctorMemoryProviderSection` (class) — The ◆ Memory Provider section should respect memory.provider config.
- L262 `_make_hermes_home(self, tmp_path, provider='')` (method) — Create a minimal HERMES_HOME with config.yaml.
- L271 `_run_doctor_and_capture(self, monkeypatch, tmp_path, provider='')` (method) — Run doctor and capture stdout.
- L301 `test_no_provider_shows_builtin_ok(self, monkeypatch, tmp_path)` (method)
- L309 `test_honcho_provider_not_installed_shows_fail(self, monkeypatch, tmp_path)` (method)
- L319 `test_mem0_provider_not_installed_shows_fail(self, monkeypatch, tmp_path)` (method)
- L327 `test_run_doctor_termux_treats_docker_and_browser_warnings_as_expected(monkeypatch, tmp_path)` (function)
- L358 `test_run_doctor_accepts_named_provider_from_providers_section(monkeypatch, tmp_path)` (function)
- L410 `test_run_doctor_accepts_bare_custom_provider(monkeypatch, tmp_path)` (function)
- L448 `test_run_doctor_flags_missing_credentials_for_active_openrouter_provider(monkeypatch, tmp_path)` (function)
- L498 `test_run_doctor_accepts_hermes_provider_ids_that_catalog_aliases(monkeypatch, tmp_path, provider, default_model)` (function)
- L545 `test_run_doctor_accepts_kimi_coding_cn_provider(monkeypatch, tmp_path)` (function)
- L584 `test_run_doctor_termux_does_not_mark_browser_available_without_agent_browser(monkeypatch, tmp_path)` (function)
- L628 `test_run_doctor_kimi_cn_env_is_detected_and_probe_is_null_safe(monkeypatch, tmp_path)` (function)
- L676 `test_run_doctor_dashscope_retries_china_endpoint_after_intl_unauthorized(monkeypatch, tmp_path)` (function)
- L732 `test_run_doctor_opencode_go_skips_invalid_models_probe(monkeypatch, tmp_path, base_url)` (function)
- L786 `TestGitHubTokenCheck` (class) — Tests for GitHub token / gh auth detection in doctor.
- L789 `test_no_token_and_not_gh_authenticated_shows_warn(self, monkeypatch, tmp_path)` (method)
- L806 `test_token_env_present_shows_ok(self, monkeypatch, tmp_path)` (method)
- L823 `test_gh_authenticated_without_env_token_shows_ok(self, monkeypatch, tmp_path)` (method)
- L862 `_run_doctor_with_healthy_oauth_fallback(monkeypatch, tmp_path, *, env_key: str, bad_key: str, failing_host: str, gemini_oauth_status: dict, minimax_oauth_status: dict, xai_oauth_status: dict | None=None)` (function)
- L957 `test_run_doctor_ignores_invalid_direct_keys_when_oauth_fallback_is_healthy(monkeypatch, tmp_path, env_key, bad_key, failing_host, gemini_oauth_status, minimax_oauth_status, xai_oauth_status, unexpected_issue)` (function)
- L983 `test_has_healthy_oauth_fallback_returns_false_for_unknown_provider()` (function)
- L988 `TestHasHealthyOauthFallbackForXai` (class)
- L989 `test_returns_true_when_xai_oauth_healthy(self, monkeypatch)` (method)
- L995 `test_returns_false_when_xai_oauth_not_logged_in(self, monkeypatch)` (method)
- L1001 `test_returns_false_when_xai_oauth_returns_none(self, monkeypatch)` (method)
- L1007 `test_returns_false_when_xai_import_unavailable(self, monkeypatch)` (method)
- L1016 `test_xai_import_failure_does_not_affect_gemini(self, monkeypatch)` (method)
- L1032 `TestDoctorXaiOAuthStatus` (class) — The ◆ Auth Providers section must show xAI OAuth login state.
- L1040 `_run(self, monkeypatch, tmp_path, *, xai_auth_fn)` (method) — Run doctor with a controlled xAI auth callable; return stdout.
- L1070 `test_logged_in_shows_ok(self, monkeypatch, tmp_path)` (method)
- L1078 `test_not_logged_in_shows_warn(self, monkeypatch, tmp_path)` (method)
- L1086 `test_error_shown_when_not_logged_in_and_error_present(self, monkeypatch, tmp_path)` (method)
- L1094 `test_no_error_line_when_error_key_absent(self, monkeypatch, tmp_path)` (method)
- L1104 `test_logged_in_does_not_emit_not_logged_in_on_xai_line(self, monkeypatch, tmp_path)` (method)
- L1115 `test_import_failure_does_not_crash_doctor(self, monkeypatch, tmp_path)` (method) — Doctor must not crash when get_xai_oauth_auth_status cannot be imported.
- L1147 `test_import_failure_does_not_affect_other_providers(self, monkeypatch, tmp_path)` (method) — Nous / Codex / Gemini / MiniMax rows must survive an xAI import failure.
- L1179 `test_function_raises_does_not_crash_doctor(self, monkeypatch, tmp_path)` (method) — A runtime exception from get_xai_oauth_auth_status must be swallowed.
- L1187 `test_function_returns_none_does_not_crash_doctor(self, monkeypatch, tmp_path)` (method) — None return is normalised to {} via `or {}` — must not AttributeError.
- L1200 `TestDoctorCodexCliHintPlacement` (class) — The `codex CLI not installed` hint belongs under OpenAI Codex auth.
- L1209 `_run(self, monkeypatch, tmp_path, *, codex_logged_in: bool, codex_cli_present: bool)` (method)
- L1246 `_hint_line()` (method)
- L1249 `test_hint_appears_under_codex_auth_when_missing(self, monkeypatch, tmp_path)` (method)
- L1258 `test_hint_suppressed_when_codex_cli_present(self, monkeypatch, tmp_path)` (method)
- L1263 `test_hint_suppressed_when_codex_logged_in(self, monkeypatch, tmp_path)` (method)
- L1269 `test_hint_never_attaches_to_minimax_row(self, monkeypatch, tmp_path)` (method)
- L1279 `TestDoctorStaleMaxIterationsDrift` (class) — Regression for #17534: a stale HERMES_MAX_ITERATIONS in .env shadows
- L1290 `_run_config_section(self, monkeypatch, tmp_path, *, fix, ghost, cfg_turns, os_environ_value=None)` (method)
- L1330 `test_detects_drift_warn_only(self, monkeypatch, tmp_path)` (method)
- L1340 `test_fix_removes_ghost(self, monkeypatch, tmp_path)` (method)
- L1350 `test_no_drift_when_values_match(self, monkeypatch, tmp_path)` (method)
- L1356 `test_no_drift_when_ghost_absent(self, monkeypatch, tmp_path)` (method)
