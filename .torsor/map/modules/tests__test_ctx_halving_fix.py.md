---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_ctx_halving_fix.py

Symbols in `tests/test_ctx_halving_fix.py`.

- L38 `TestParseAvailableOutputTokens` (class) — Pure-function tests; no I/O required.
- L41 `_parse(self, msg)` (method)
- L47 `test_anthropic_canonical_format(self)` (method) — Canonical Anthropic error: max_tokens: X > context_window: Y - input_tokens: Z = available_tokens: W
- L55 `test_anthropic_format_large_numbers(self)` (method)
- L62 `test_available_tokens_variant_spacing(self)` (method) — Handles extra spaces around the colon.
- L67 `test_available_tokens_natural_language(self)` (method) — 'available tokens: N' wording (no underscore).
- L72 `test_single_token_available(self)` (method) — Edge case: only 1 token left.
- L79 `test_prompt_too_long_is_not_output_cap_error(self)` (method) — 'prompt is too long' errors must NOT be caught — they need context-overflow recovery.
- L84 `test_generic_context_window_exceeded(self)` (method) — Generic context window errors without available_tokens should not match.
- L89 `test_context_length_exceeded(self)` (method)
- L93 `test_no_max_tokens_keyword(self)` (method) — Error not related to max_tokens at all.
- L98 `test_empty_string(self)` (method)
- L101 `test_rate_limit_error(self)` (method)
- L110 `TestContextOverflowLimitSelection` (class) — Context-overflow recovery must not invent a lower window size.
- L119 `test_generic_overflow_without_provider_limit_keeps_context_length(self)` (method)
- L134 `test_explicit_provider_limit_still_selects_that_limit(self)` (method)
- L141 `test_reported_limit_not_lower_than_current_is_ignored(self)` (method)
- L153 `TestBuildAnthropicKwargsClamping` (class) — The context_length clamp only fires when output ceiling > window.
- L158 `_build(self, model, max_tokens=None, context_length=None)` (method)
- L169 `test_no_clamping_when_output_ceiling_fits_in_window(self)` (method) — Opus 4.6 native output (128K) < context window (200K) — no clamping.
- L174 `test_clamping_fires_for_tiny_custom_window(self)` (method) — When context_length is 8K (local model), output cap is clamped to 7999.
- L179 `test_explicit_max_tokens_respected_when_within_window(self)` (method) — Explicit max_tokens smaller than window passes through unchanged.
- L184 `test_explicit_max_tokens_clamped_when_exceeds_window(self)` (method) — Explicit max_tokens larger than a small window is clamped.
- L189 `test_no_context_length_uses_native_ceiling(self)` (method) — Without context_length the native output ceiling is used directly.
- L199 `TestEphemeralMaxOutputTokens` (class) — _build_api_kwargs consumes _ephemeral_max_output_tokens exactly once
- L204 `_make_agent(self)` (method) — Return a minimal AIAgent with api_mode='anthropic_messages' and
- L230 `test_ephemeral_override_is_used_on_first_call(self)` (method) — When _ephemeral_max_output_tokens is set, it overrides self.max_tokens.
- L238 `test_ephemeral_override_is_consumed_after_one_call(self)` (method) — After one call the ephemeral override is cleared to None.
- L246 `test_subsequent_call_uses_self_max_tokens(self)` (method) — A second _build_api_kwargs call uses the normal max_tokens path.
- L257 `test_no_ephemeral_uses_self_max_tokens_directly(self)` (method) — Without an ephemeral override, self.max_tokens is used normally.
- L270 `TestContextNotHalvedOnOutputCapError` (class) — When the API returns 'max_tokens too large given prompt', the handler
- L275 `_make_agent_with_compressor(self, context_length=200000)` (method)
- L305 `test_output_cap_error_sets_ephemeral_not_context_length(self)` (method) — On 'max_tokens too large' error, _ephemeral_max_output_tokens is set
- L329 `test_prompt_too_long_with_explicit_limit_uses_provider_limit(self)` (method) — Prompt-too-long errors only change context_length when they report a concrete limit.
- L340 `test_output_cap_error_safety_margin(self)` (method) — The ephemeral value includes a 64-token safety margin below available_out.
- L352 `test_safety_margin_never_goes_below_one(self)` (method) — When available_out is very small, safe_out must be at least 1.
