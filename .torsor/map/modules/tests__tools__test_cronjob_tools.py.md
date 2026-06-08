---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_cronjob_tools.py

Symbols in `tests/tools/test_cronjob_tools.py`.

- L17 `TestScanCronPrompt` (class)
- L18 `test_clean_prompt_passes(self)` (method)
- L22 `test_prompt_injection_blocked(self)` (method)
- L27 `test_disregard_rules_blocked(self)` (method)
- L30 `test_system_override_blocked(self)` (method)
- L33 `test_exfiltration_curl_blocked(self)` (method)
- L37 `test_exfiltration_wget_blocked(self)` (method)
- L40 `test_authorization_header_api_examples_allowed(self)` (method)
- L45 `test_authorization_header_quoted_url_allowed(self)` (method)
- L56 `test_authorization_header_secret_to_arbitrary_host_blocked(self)` (method)
- L64 `test_read_secrets_blocked(self)` (method)
- L68 `test_ssh_backdoor_blocked(self)` (method)
- L71 `test_sudoers_blocked(self)` (method)
- L74 `test_destructive_rm_blocked(self)` (method)
- L77 `test_invisible_unicode_blocked(self)` (method)
- L82 `test_emoji_zwj_sequences_allowed(self)` (method)
- L87 `test_non_emoji_zwj_still_blocked(self)` (method)
- L90 `test_deception_blocked(self)` (method)
- L101 `TestScanCronSkillAssembled` (class) — The looser scanner used when skill content is part of the assembled
- L112 `test_clean_prompt_passes(self)` (method)
- L117 `test_prompt_injection_still_blocked(self)` (method)
- L123 `test_invisible_unicode_sanitized_not_blocked(self)` (method) — A stray zero-width space in vetted skill content is stripped, not
- L132 `test_bom_sanitized_not_blocked(self)` (method)
- L138 `test_bidi_override_sanitized_not_blocked(self)` (method)
- L143 `test_injection_with_invisible_unicode_still_blocked(self)` (method) — Sanitizing the invisible char must not let a real injection slip
- L150 `test_emoji_zwj_sequences_allowed(self)` (method)
- L156 `test_descriptive_attack_command_prose_allowed(self)` (method) — Security postmortems and runbooks routinely describe attack
- L175 `test_github_auth_header_still_allowed(self)` (method) — The GitHub auth-header allowlist works for both scanners.
- L182 `TestCronjobRequirements` (class)
- L183 `test_requires_no_crontab_binary(self, monkeypatch)` (method) — Cron is internal (JSON-based scheduler), no system crontab needed.
- L192 `test_accepts_interactive_mode(self, monkeypatch)` (method)
- L199 `test_accepts_gateway_session(self, monkeypatch)` (method)
- L206 `test_accepts_exec_ask(self, monkeypatch)` (method)
- L213 `test_rejects_when_no_session_env(self, monkeypatch)` (method) — Without any session env vars, cronjob tool should not be available.
- L222 `test_rejects_false_like_interactive_env(self, monkeypatch, false_like_value)` (method)
- L233 `test_rejects_false_like_any_session_env(self, monkeypatch, var_name, false_like_value)` (method) — All three session env vars share the same truthy semantics.
- L243 `TestUnifiedCronjobTool` (class)
- L245 `_setup_cron_dir(self, tmp_path, monkeypatch)` (method)
- L250 `test_create_and_list(self)` (method)
- L267 `test_list_handles_partial_legacy_job_records(self)` (method)
- L289 `test_pause_and_resume(self)` (method)
- L301 `test_update_schedule_recomputes_display(self)` (method)
- L312 `test_update_runtime_overrides_can_set_and_clear(self)` (method)
- L339 `test_create_skill_backed_job(self)` (method)
- L355 `test_create_multi_skill_job(self)` (method)
- L371 `test_multi_skill_default_name_prefers_prompt_when_present(self)` (method)
- L383 `test_update_can_clear_skills(self)` (method)
- L399 `test_create_normalizes_list_form_deliver(self)` (method) — deliver=['telegram'] (list) is stored as the string 'telegram'.
- L422 `test_create_normalizes_multi_element_list_deliver(self)` (method) — deliver=['telegram', 'discord'] is stored as 'telegram,discord'.
- L438 `test_update_normalizes_list_form_deliver(self)` (method) — update with deliver=['telegram'] stores the canonical string.
