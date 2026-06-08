---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_model_normalize.py

Symbols in `tests/hermes_cli/test_model_normalize.py`.

- L18 `TestIssue5211OpenCodeGoDotPreservation` (class) — OpenCode Go model names with dots must pass through unchanged.
- L28 `test_opencode_go_preserves_dots(self, model, expected)` (method)
- L32 `test_opencode_go_not_in_dot_to_hyphen_set(self)` (method) — opencode-go must NOT be in the dot-to-hyphen provider set.
- L39 `TestAnthropicDotToHyphen` (class) — Anthropic API still needs dots→hyphens.
- L46 `test_anthropic_converts_dots(self, model, expected)` (method)
- L50 `test_anthropic_strips_vendor_prefix(self)` (method)
- L57 `TestOpenCodeZenModelNormalization` (class) — OpenCode Zen preserves dots for most models, but Claude stays hyphenated.
- L69 `test_zen_normalizes_models(self, model, expected)` (method)
- L73 `test_zen_strips_vendor_prefix(self)` (method)
- L77 `test_zen_strips_vendor_prefix_for_non_claude(self)` (method)
- L84 `TestCopilotDotPreservation` (class) — Copilot preserves dots in model names.
- L91 `test_copilot_preserves_dots(self, model, expected)` (method)
- L98 `TestCopilotModelNormalization` (class) — Copilot requires bare dot-notation model IDs.
- L131 `test_copilot_normalization(self, model, expected)` (method)
- L140 `test_copilot_acp_normalization(self, model, expected)` (method) — Copilot ACP shares the same API expectations as HTTP Copilot.
- L144 `test_openai_codex_still_strips_openai_prefix(self)` (method) — Regression: openai-codex must still strip the openai/ prefix.
- L151 `TestAggregatorProviders` (class) — Aggregators need vendor/model slugs.
- L154 `test_openrouter_prepends_vendor(self)` (method)
- L158 `test_nous_prepends_vendor(self)` (method)
- L162 `test_vendor_already_present(self)` (method)
- L167 `TestIssue6211NativeProviderPrefixNormalization` (class)
- L176 `test_native_provider_prefixes_are_only_stripped_on_matching_provider(self, model, target_provider, expected)` (method)
- L184 `TestDetectVendor` (class)
- L192 `test_detects_known_vendors(self, model, expected)` (method)
- L198 `TestDeepseekVSeriesPassThrough` (class) — DeepSeek's V-series IDs (``deepseek-v4-pro``, ``deepseek-v4-flash``,
- L217 `test_v_series_passes_through(self, model)` (method)
- L221 `test_deepseek_provider_preserves_v4_pro(self)` (method) — End-to-end via normalize_model_for_provider — user selecting
- L227 `test_deepseek_provider_preserves_v4_flash(self)` (method)
- L234 `TestDeepseekCanonicalAndReasonerMapping` (class) — Canonical pass-through and reasoner-keyword folding stay intact.
- L242 `test_canonical_models_pass_through(self, model, expected)` (method)
- L252 `test_reasoner_keywords_map_to_reasoner(self, model)` (method)
- L261 `test_unknown_names_fall_back_to_chat(self, model)` (method)
