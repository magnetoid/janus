---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_nous_inference_url_validation.py

Symbols in `tests/hermes_cli/test_nous_inference_url_validation.py`.

- L33 `TestValidatorRules` (class)
- L34 `test_allowlisted_https_host_returned(self)` (method)
- L38 `test_trailing_slash_stripped(self)` (method)
- L42 `test_attacker_host_rejected(self, caplog)` (method)
- L50 `test_subdomain_of_allowlist_host_rejected(self)` (method) — *.nousresearch.com is NOT in the allowlist — exact hostname only.
- L63 `test_http_scheme_rejected(self, caplog)` (method)
- L73 `test_file_scheme_rejected(self)` (method)
- L78 `test_javascript_scheme_rejected(self)` (method)
- L86 `test_empty_string_rejected(self)` (method)
- L89 `test_whitespace_only_rejected(self)` (method)
- L92 `test_none_rejected(self)` (method)
- L95 `test_non_string_rejected(self)` (method)
- L99 `test_malformed_url_rejected(self)` (method) — Even garbled input must fall back safely, not raise.
- L106 `test_default_inference_url_is_in_allowlist(self)` (method) — Sanity check: DEFAULT_NOUS_INFERENCE_URL must itself validate.
- L119 `test_allowlist_contains_inference_api_host(self)` (method) — The default's host must be in the allowlist set.
- L126 `TestCallSiteWiring` (class) — Verify the validator is actually wired into all auth.py NETWORK call sites.
- L143 `_read_auth_source(self)` (method)
- L148 `test_no_unvalidated_inference_base_url_assignments_remain(self)` (method) — No remaining ``_optional_base_url(...inference_base_url...)`` reads
- L163 `test_validator_wired_at_all_known_call_sites(self)` (method) — All 2 known auth.py NETWORK sites use the validator. If this count
- L177 `test_proxy_adapter_also_validates(self)` (method) — The Nous proxy adapter applies the validator as defense-in-depth
- L188 `TestEnvOverrideNotGated` (class) — The documented dev/staging env-var override must keep working.
- L199 `test_env_override_path_does_not_call_validator(self)` (method) — In resolve_nous_runtime_credentials, the env override is
