---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_apply_model_switch_result_context.py

Symbols in `tests/hermes_cli/test_apply_model_switch_result_context.py`.

- L21 `_FakeModelInfo` (class)
- L25 `has_cost_data(self)` (method)
- L28 `format_capabilities(self)` (method)
- L32 `_StubCLI` (class) — Minimum attrs ``_apply_model_switch_result`` reads on ``self``.
- L46 `_run_display(monkeypatch, result)` (function)
- L57 `test_picker_path_uses_provider_aware_context_on_codex(monkeypatch)` (function) — ``_apply_model_switch_result`` must prefer the provider-aware resolver
- L91 `test_picker_path_shows_vendor_value_when_no_provider_cap(monkeypatch)` (function) — On providers with no enforced cap (e.g. OpenRouter), the picker path
- L123 `test_picker_path_falls_back_to_model_info_when_resolver_empty(monkeypatch)` (function) — If ``get_model_context_length`` returns nothing (rare — truly unknown
