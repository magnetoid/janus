---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_minimax_provider.py

Symbols in `tests/agent/test_minimax_provider.py`.

- L6 `TestMinimaxContextLengths` (class) — Verify context length entries match official docs.
- L13 `test_minimax_prefix_has_correct_context(self)` (method)
- L17 `test_minimax_models_resolve_via_prefix(self)` (method)
- L24 `test_minimax_m3_resolves_to_1m(self)` (method)
- L35 `TestMinimaxM3StaleCacheGuard` (class) — Pre-catalog builds resolved M3 via the generic 'minimax' catch-all
- L42 `test_suggests_minimax_m3(self)` (method)
- L49 `test_stale_m3_cache_dropped_and_reresolves(self, tmp_path, monkeypatch)` (method)
- L67 `test_correct_m3_cache_preserved(self, tmp_path, monkeypatch)` (method)
- L79 `test_m2_cache_not_clobbered(self, tmp_path, monkeypatch)` (method)
- L95 `TestMinimaxThinkingSupport` (class) — Verify that MiniMax gets manual thinking (not adaptive).
- L104 `test_minimax_m27_gets_manual_thinking(self)` (method)
- L119 `test_minimax_m25_gets_manual_thinking(self)` (method)
- L131 `test_thinking_still_works_for_claude(self)` (method)
- L143 `TestMinimaxAuxModel` (class) — Verify auxiliary model is the current frontier standard (not highspeed).
- L159 `test_minimax_aux_is_standard(self)` (method)
- L173 `test_minimax_aux_not_highspeed(self)` (method)
- L180 `TestMinimaxBetaHeaders` (class) — MiniMax Anthropic-compat endpoints reject fine-grained-tool-streaming beta.
- L193 `_build_and_get_betas(self, api_key, base_url=None)` (method) — Build client, return the anthropic-beta header string.
- L204 `test_minimax_global_omits_tool_streaming(self)` (method)
- L211 `test_minimax_global_trailing_slash(self)` (method)
- L219 `test_minimax_cn_omits_tool_streaming(self)` (method)
- L226 `test_minimax_cn_trailing_slash(self)` (method)
- L234 `test_native_anthropic_keeps_tool_streaming(self)` (method)
- L239 `test_third_party_proxy_keeps_tool_streaming(self)` (method)
- L245 `test_custom_base_url_keeps_tool_streaming(self)` (method)
- L253 `test_common_betas_none_url(self)` (method)
- L257 `test_common_betas_empty_url(self)` (method)
- L261 `test_common_betas_minimax_url(self)` (method)
- L267 `test_common_betas_minimax_cn_url(self)` (method)
- L272 `test_common_betas_regular_url(self)` (method)
- L277 `TestMinimaxApiMode` (class) — Verify determine_api_mode returns anthropic_messages for MiniMax providers.
- L286 `test_minimax_returns_anthropic_messages(self)` (method)
- L290 `test_minimax_cn_returns_anthropic_messages(self)` (method)
- L294 `test_minimax_with_url_also_works(self)` (method)
- L299 `test_anthropic_still_returns_anthropic_messages(self)` (method)
- L303 `test_openai_returns_chat_completions(self)` (method)
- L310 `TestMinimaxMaxOutput` (class) — Verify _get_anthropic_max_output returns correct limits for MiniMax models.
- L317 `test_minimax_m27_output_limit(self)` (method)
- L321 `test_minimax_m25_output_limit(self)` (method)
- L325 `test_minimax_m2_output_limit(self)` (method)
- L329 `test_claude_output_unaffected(self)` (method)
- L335 `TestMinimaxPreserveDots` (class) — Verify that MiniMax model names preserve dots through the Anthropic adapter.
- L342 `test_minimax_provider_preserves_dots(self)` (method)
- L348 `test_minimax_cn_provider_preserves_dots(self)` (method)
- L354 `test_minimax_url_preserves_dots(self)` (method)
- L360 `test_minimax_cn_url_preserves_dots(self)` (method)
- L366 `test_anthropic_does_not_preserve_dots(self)` (method)
- L372 `test_opencode_zen_provider_preserves_dots(self)` (method)
- L378 `test_opencode_zen_url_preserves_dots(self)` (method)
- L384 `test_zai_provider_preserves_dots(self)` (method)
- L390 `test_bigmodel_cn_url_preserves_dots(self)` (method)
- L396 `test_normalize_preserves_m25_free_dot(self)` (method)
- L400 `test_normalize_preserves_m27_dot(self)` (method)
- L404 `test_normalize_preserves_non_anthropic_dots_without_preserve(self)` (method)
- L410 `test_normalize_still_converts_claude_dots_without_preserve(self)` (method)
- L415 `TestMinimaxSwitchModelCredentialGuard` (class) — Verify switch_model() does not leak Anthropic credentials to MiniMax.
- L424 `test_switch_to_minimax_does_not_resolve_anthropic_token(self)` (method) — switch_model() should NOT call resolve_anthropic_token() for MiniMax.
