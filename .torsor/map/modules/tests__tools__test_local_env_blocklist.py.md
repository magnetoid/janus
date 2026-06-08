---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_local_env_blocklist.py

Symbols in `tests/tools/test_local_env_blocklist.py`.

- L22 `_make_fake_popen(captured: dict)` (function) — Return a fake Popen constructor that records the env kwarg.
- L35 `_run_with_env(extra_os_env=None, self_env=None)` (function) — Execute a command via LocalEnvironment with mocked Popen
- L59 `TestProviderEnvBlocklist` (class) — Provider env vars loaded from ~/.hermes/.env must not leak.
- L62 `test_blocked_vars_are_stripped(self)` (method) — OPENAI_BASE_URL and other provider vars must not appear in subprocess env.
- L76 `test_registry_derived_vars_are_stripped(self)` (method) — Vars from the provider registry (ANTHROPIC_TOKEN, ZAI_API_KEY, etc.)
- L96 `test_bedrock_bearer_token_is_stripped(self)` (method) — The Bedrock-specific bearer token is a Hermes inference secret
- L115 `test_general_aws_credential_chain_is_preserved(self)` (method) — The GENERAL AWS credential chain must STILL pass through to
- L149 `test_non_registry_provider_vars_are_stripped(self)` (method) — Extra provider vars not in PROVIDER_REGISTRY must also be blocked.
- L167 `test_tool_and_gateway_vars_are_stripped(self)` (method) — Tool and gateway secrets/config must not leak into subprocess env.
- L195 `test_safe_vars_are_preserved(self)` (method) — Standard env vars (PATH, HOME, USER) must still be passed through.
- L204 `test_self_env_blocked_vars_also_stripped(self)` (method) — Blocked vars in self.env are stripped; non-blocked vars pass through.
- L216 `TestForceEnvOptIn` (class) — Callers can opt in to passing a blocked var via _HERMES_FORCE_ prefix.
- L219 `test_force_prefix_passes_blocked_var(self)` (method) — _HERMES_FORCE_OPENAI_API_KEY in self.env should inject OPENAI_API_KEY.
- L230 `test_force_prefix_overrides_os_environ_block(self)` (method) — Force-prefix in self.env wins even when os.environ has the blocked var.
- L240 `TestBlocklistCoverage` (class) — Sanity checks that the blocklist covers all known providers.
- L243 `test_issue_1002_offenders(self)` (method) — Blocklist includes the main offenders from issue #1002.
- L254 `test_registry_vars_are_in_blocklist(self)` (method) — Every api_key_env_var and base_url_env_var from PROVIDER_REGISTRY
- L270 `test_bedrock_bearer_token_is_in_blocklist(self)` (method) — auth_type='aws_sdk' providers contribute their Hermes-managed
- L276 `test_general_aws_chain_not_in_blocklist(self)` (method) — The general AWS credential chain must NOT be in the blocklist —
- L300 `test_extra_auth_vars_covered(self)` (method) — Non-registry auth vars (ANTHROPIC_TOKEN, CLAUDE_CODE_OAUTH_TOKEN)
- L306 `test_non_registry_provider_vars_are_in_blocklist(self)` (method)
- L321 `test_optional_tool_and_messaging_vars_are_in_blocklist(self)` (method) — Tool/messaging vars from OPTIONAL_ENV_VARS should stay covered.
- L336 `test_gateway_runtime_vars_are_in_blocklist(self)` (method)
- L379 `TestSanePathIncludesHomebrew` (class) — Verify _SANE_PATH includes macOS Homebrew directories.
- L382 `test_sane_path_includes_homebrew_bin(self)` (method)
- L386 `test_sane_path_includes_homebrew_sbin(self)` (method)
- L390 `test_make_run_env_appends_homebrew_on_minimal_path(self)` (method) — When PATH is minimal (no /usr/bin), _make_run_env should append
- L400 `test_make_run_env_does_not_duplicate_on_full_path(self)` (method) — When PATH already has /usr/bin, _make_run_env should not append.
