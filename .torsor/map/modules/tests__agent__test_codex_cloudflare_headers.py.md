---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_codex_cloudflare_headers.py

Symbols in `tests/agent/test_codex_cloudflare_headers.py`.

- L38 `_make_codex_jwt(account_id: str='acct-test-123')` (function) — Build a syntactically valid Codex-style JWT with the account_id claim.
- L60 `TestCodexCloudflareHeaders` (class)
- L61 `test_originator_is_codex_cli_rs(self)` (method) — Cloudflare whitelists codex_cli_rs — any other value is 403'd.
- L67 `test_user_agent_advertises_codex_cli_rs(self)` (method)
- L72 `test_account_id_extracted_from_jwt(self)` (method)
- L78 `test_canonical_header_casing(self)` (method) — Upstream codex-rs uses PascalCase with trailing -ID. Match exactly.
- L87 `test_malformed_token_drops_account_id_without_raising(self)` (method)
- L95 `test_non_string_token_handled(self)` (method)
- L101 `test_jwt_without_chatgpt_account_id_claim(self)` (method) — A valid JWT that lacks the account_id claim should still return headers.
- L119 `TestPrimaryClientWiring` (class)
- L120 `test_init_wires_codex_headers_for_chatgpt_base_url(self)` (method)
- L139 `test_apply_client_headers_on_base_url_change(self)` (method) — Credential-rotation / base-url change path must also emit codex headers.
- L164 `test_apply_client_headers_clears_codex_headers_off_chatgpt(self)` (method) — Switching AWAY from chatgpt.com must drop the codex headers.
- L187 `test_openrouter_base_url_does_not_get_codex_headers(self)` (method)
- L208 `TestAuxiliaryClientWiring` (class)
- L209 `test_build_codex_client_passes_codex_headers(self, monkeypatch)` (method) — _build_codex_client builds the OpenAI client used for compression /
- L235 `test_resolve_provider_client_raw_codex_passes_codex_headers(self, monkeypatch)` (method) — The ``raw_codex=True`` branch (used by the main agent loop for direct
