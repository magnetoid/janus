---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_vision_native_fast_path.py

Symbols in `tests/tools/test_vision_native_fast_path.py`.

- L34 `TestSupportsMediaInToolResults` (class)
- L35 `test_anthropic_native_yes(self)` (method)
- L38 `test_openrouter_yes(self)` (method)
- L41 `test_nous_yes(self)` (method)
- L44 `test_openai_chat_yes(self)` (method)
- L47 `test_openai_codex_yes(self)` (method)
- L50 `test_gemini_3_yes(self)` (method)
- L53 `test_gemini_2_no(self)` (method)
- L56 `test_unknown_provider_conservative_no(self)` (method)
- L59 `test_empty_provider_no(self)` (method)
- L67 `TestBuildNativeVisionToolResult` (class)
- L68 `test_envelope_shape(self)` (method)
- L84 `test_no_question_omits_question_section(self)` (method)
- L99 `TestVisionAnalyzeNative` (class)
- L100 `test_local_file_returns_multimodal_envelope(self, tmp_path)` (method)
- L114 `test_missing_file_returns_error_string(self, tmp_path)` (method)
- L124 `test_empty_image_url_returns_error(self)` (method)
- L133 `test_file_url_scheme_resolves(self, tmp_path)` (method)
- L142 `test_oversized_image_resized_under_embed_cap(self, tmp_path)` (method) — Regression for the wedged-session incident (May 2026).
- L184 `TestHandleVisionAnalyzeFastPath` (class) — Verify the dispatcher chooses fast-path vs aux-LLM correctly.
- L187 `test_vision_capable_main_model_uses_fast_path(self, tmp_path, monkeypatch)` (method) — Main model supports native vision → fast path returns multimodal.
- L211 `test_non_vision_main_model_falls_through_to_aux(self, tmp_path, monkeypatch)` (method) — Non-vision main model → fast path skipped, aux LLM path attempted.
- L231 `test_fast_path_disabled_for_unsupported_provider(self, tmp_path, monkeypatch)` (method) — Even with vision-capable model, unknown provider → fall through.
- L251 `test_supports_vision_override_bypasses_provider_allowlist(self, tmp_path)` (method) — supports_vision=true enables the fast path on an unlisted provider.
- L276 `test_text_mode_wins_over_supports_vision_override(self, tmp_path)` (method) — Explicit text routing blocks the fast path even with supports_vision.
