---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_model_switch_variant_tags.py

Symbols in `tests/hermes_cli/test_model_switch_variant_tags.py`.

- L21 `_run_switch(raw_input: str, current_provider: str='openrouter')` (function) — Run switch_model with mocked dependencies, return the resolved model name.
- L40 `TestVariantTagPreservation` (class) — OpenRouter variant tags (:free, :extended, :fast) must survive model switching.
- L48 `test_slash_format_preserves_variant_tag(self, model, expected)` (method) — Models already in vendor/model:tag format must not have their tag mangled.
- L52 `test_legacy_colon_format_converts_to_slash(self)` (method) — Legacy vendor:model (no slash) should still be converted to vendor/model.
- L57 `test_legacy_colon_format_with_tag_converts_first_colon_only(self)` (method) — vendor:model:free (no slash) → vendor/model:free — first colon becomes slash.
- L62 `test_bare_model_name_unaffected(self)` (method) — Bare model names without colons or slashes should work normally.
- L67 `test_already_correct_slug_no_tag(self)` (method) — Standard vendor/model slugs without tags pass through unchanged.
