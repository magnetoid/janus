---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_redact.py

Symbols in `tests/agent/test_redact.py`.

- L11 `_ensure_redaction_enabled(monkeypatch)` (function) — Ensure HERMES_REDACT_SECRETS is not disabled by prior test imports.
- L18 `TestKnownPrefixes` (class)
- L19 `test_openai_sk_key(self)` (method)
- L26 `test_openrouter_sk_key(self)` (method)
- L31 `test_github_pat_classic(self)` (method)
- L35 `test_github_pat_fine_grained(self)` (method)
- L39 `test_slack_token(self)` (method)
- L44 `test_google_api_key(self)` (method)
- L48 `test_perplexity_key(self)` (method)
- L52 `test_fal_key(self)` (method)
- L56 `test_short_token_fully_masked(self)` (method)
- L61 `TestEnvAssignments` (class)
- L62 `test_export_api_key(self)` (method)
- L68 `test_quoted_value(self)` (method)
- L74 `test_non_secret_env_unchanged(self)` (method)
- L79 `test_path_unchanged(self)` (method)
- L84 `test_lowercase_python_variable_token_unchanged(self)` (method)
- L90 `test_lowercase_python_variable_api_key_unchanged(self)` (method)
- L96 `test_typescript_await_token_unchanged(self)` (method)
- L102 `test_typescript_await_secret_unchanged(self)` (method)
- L108 `test_export_whitespace_preserved(self)` (method)
- L117 `TestJsonFields` (class)
- L118 `test_json_api_key(self)` (method)
- L123 `test_json_token(self)` (method)
- L128 `test_json_non_secret_unchanged(self)` (method)
- L134 `TestAuthHeaders` (class)
- L135 `test_bearer_token(self)` (method)
- L141 `test_case_insensitive(self)` (method)
- L147 `TestTelegramTokens` (class)
- L148 `test_bot_token(self)` (method)
- L154 `test_raw_token(self)` (method)
- L160 `TestPassthrough` (class)
- L161 `test_empty_string(self)` (method)
- L164 `test_none_returns_none(self)` (method)
- L167 `test_non_string_input_int_coerced(self)` (method)
- L170 `test_non_string_input_dict_coerced_and_redacted(self)` (method)
- L174 `test_normal_text_unchanged(self)` (method)
- L178 `test_code_unchanged(self)` (method)
- L182 `test_url_without_key_unchanged(self)` (method)
- L187 `TestRedactingFormatter` (class)
- L188 `test_formats_and_redacts(self)` (method)
- L204 `TestPrintenvSimulation` (class) — Simulate what happens when the agent runs `env` or `printenv`.
- L207 `test_full_env_dump(self)` (method)
- L227 `TestSecretCapturePayloadRedaction` (class)
- L228 `test_secret_value_field_redacted(self)` (method)
- L233 `test_raw_secret_field_redacted(self)` (method)
- L239 `TestElevenLabsTavilyExaKeys` (class) — Regression tests for ElevenLabs (sk_), Tavily (tvly-), and Exa (exa_) keys.
- L242 `test_elevenlabs_key_redacted(self)` (method)
- L247 `test_elevenlabs_key_in_log_line(self)` (method)
- L252 `test_tavily_key_redacted(self)` (method)
- L257 `test_tavily_key_in_log_line(self)` (method)
- L262 `test_exa_key_redacted(self)` (method)
- L267 `test_exa_key_in_log_line(self)` (method)
- L272 `test_all_three_in_env_dump(self)` (method)
- L288 `TestJWTTokens` (class) — JWT tokens start with eyJ (base64 for '{') and have dot-separated parts.
- L291 `test_full_3part_jwt(self)` (method)
- L303 `test_2part_jwt(self)` (method)
- L308 `test_standalone_jwt_header(self)` (method)
- L314 `test_jwt_with_base64_padding(self)` (method)
- L319 `test_short_eyj_not_matched(self)` (method) — eyJ followed by fewer than 10 base64 chars should not match.
- L324 `test_jwt_preserves_surrounding_text(self)` (method)
- L330 `test_home_assistant_jwt_in_memory(self)` (method) — Real-world pattern: HA token stored in agent memory block.
- L344 `TestDiscordMentions` (class) — Discord mention snowflakes (<@ID> / <@!ID>) are public syntax, not
- L349 `test_normal_mention_passes_through(self)` (method)
- L353 `test_nickname_mention_passes_through(self)` (method)
- L357 `test_multiple_mentions_pass_through(self)` (method)
- L361 `test_short_id_passes_through(self)` (method)
- L365 `test_slack_mention_passes_through(self)` (method)
- L369 `test_preserves_surrounding_text(self)` (method)
- L374 `TestWebUrlsNotRedacted` (class) — Web URLs (http/https/wss) pass through unchanged — magic-link
- L382 `test_oauth_callback_code_passes_through(self)` (method)
- L386 `test_access_token_query_passes_through(self)` (method)
- L390 `test_magic_link_checkout_passes_through(self)` (method)
- L394 `test_presigned_signature_passes_through(self)` (method)
- L398 `test_https_userinfo_passes_through(self)` (method)
- L402 `test_websocket_url_query_passes_through(self)` (method)
- L406 `test_http_access_log_request_target_passes_through(self)` (method)
- L414 `test_known_prefix_inside_url_still_redacted(self)` (method) — sk-/ghp_/JWT-shaped values inside a URL are still caught by
- L421 `test_db_connstr_password_still_redacted(self)` (method) — DB schemes (postgres/mysql/mongodb/redis/amqp) keep their
- L430 `TestFormBodyRedaction` (class) — Form-urlencoded body redaction (k=v&k=v with no other text).
- L433 `test_pure_form_body(self)` (method)
- L440 `test_oauth_token_request(self)` (method)
- L447 `test_non_form_text_unchanged(self)` (method) — Sentences with `&` should NOT trigger form redaction.
- L454 `test_multiline_text_not_form(self)` (method) — Multi-line text is never treated as form body.
- L461 `TestXaiToken` (class)
- L464 `test_bare_token_masked(self)` (method)
- L469 `test_env_assignment_masked(self)` (method)
- L473 `test_too_short_not_masked(self)` (method)
- L478 `test_company_name_not_masked(self)` (method)
- L482 `test_prefix_visible_in_masked_output(self)` (method)
