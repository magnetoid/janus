---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_inventory.py

Symbols in `tests/hermes_cli/test_inventory.py`.

- L35 `_cfg(model=None, providers=None, custom_providers=None)` (function)
- L43 `test_load_picker_context_full_dict()` (function)
- L65 `test_load_picker_context_falls_back_to_name_when_default_missing()` (function)
- L73 `test_load_picker_context_string_model_legacy_shape()` (function) — config.model can be a bare string in older configs.
- L83 `test_load_picker_context_empty_config()` (function)
- L97 `_empty_ctx(provider='orig', model='orig-model', base_url='orig-url')` (function)
- L107 `test_with_overrides_truthy_only_strings()` (function) — Empty strings must NOT clobber disk config — TUI calls this with
- L121 `test_with_overrides_truthy_value_replaces()` (function)
- L128 `test_with_overrides_no_args_returns_self_or_equivalent()` (function)
- L136 `_list_auth_returning(rows: list[dict])` (function) — Patch list_authenticated_providers to return a fixed row list.
- L144 `_nous_row(model: str='openai/gpt-5.5')` (function)
- L156 `test_build_models_payload_returns_expected_shape()` (function)
- L171 `test_build_models_payload_does_not_call_provider_model_ids()` (function) — ``build_models_payload`` is a thin shape adapter — it delegates the
- L188 `test_build_models_payload_uses_cached_nous_tier_by_default()` (function) — Picker payloads should not force fresh Nous account checks.
- L207 `test_build_models_payload_can_force_fresh_nous_tier()` (function)
- L220 `test_list_authenticated_providers_force_fresh_is_keyword_only()` (function) — ``force_fresh_nous_tier`` must be keyword-only on the public listing API.
- L238 `test_pricing_uses_cached_nous_tier_by_default()` (function)
- L259 `test_pricing_can_force_fresh_nous_tier()` (function)
- L280 `test_include_unconfigured_appends_canonical_skeletons()` (function) — include_unconfigured=True adds CANONICAL_PROVIDERS rows that
- L306 `test_include_unconfigured_skips_already_present_slugs()` (function) — If list_authenticated_providers already returned a row for a
- L325 `test_picker_hints_marks_authed_rows_authenticated()` (function)
- L337 `test_picker_hints_adds_warning_to_skeleton_rows()` (function) — Skeleton rows (unconfigured canonical providers) must carry the
- L361 `test_picker_hints_api_key_warning_format()` (function) — For api_key providers with a defined env var, the warning must
- L381 `test_canonical_order_uses_slug_not_is_user_defined_flag()` (function) — Section 3 of list_authenticated_providers sets is_user_defined=True
- L416 `test_canonical_order_with_unconfigured_preserves_full_universe()` (function) — Combined picker call: include_unconfigured + picker_hints +
- L447 `test_end_to_end_with_real_context_no_credentials_leak(monkeypatch)` (function) — Full pipeline: real load_picker_context + real
- L465 `test_payload_shape_compatible_with_modelpickerdialog_frontend()` (function) — Frontend (web/src/components/ModelPickerDialog.tsx) reads:
