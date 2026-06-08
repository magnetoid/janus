---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_invalid_context_length_warning.py

Symbols in `tests/run_agent/test_invalid_context_length_warning.py`.

- L6 `_build_agent(model_cfg, custom_providers=None, model='anthropic/claude-opus-4.6')` (function) — Build an AIAgent with the given model config.
- L34 `test_valid_integer_context_length_no_warning()` (function) — Plain integer context_length should work silently.
- L46 `test_string_k_suffix_context_length_warns()` (function) — context_length: '256K' should warn the user clearly.
- L60 `test_string_numeric_context_length_works()` (function) — context_length: '256000' (string) should parse fine via int().
- L71 `test_custom_providers_invalid_context_length_warns()` (function) — Invalid context_length in custom_providers should warn.
- L95 `test_custom_providers_valid_context_length()` (function) — Valid integer in custom_providers should work silently.
