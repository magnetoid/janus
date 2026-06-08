---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_compression_feasibility.py

Symbols in `tests/run_agent/test_compression_feasibility.py`.

- L20 `_stable_aux_provider_config()` (function) — Keep feasibility tests independent from the developer's config.yaml.
- L29 `_make_agent(*, compression_enabled: bool=True, threshold_percent: float=0.5, main_context: int=200000)` (function) — Build a minimal AIAgent with a compressor, skipping __init__.
- L70 `test_auto_corrects_threshold_when_aux_context_below_threshold(mock_get_client, mock_ctx_len)` (function) — Auto-correction: aux >= 64K floor but < threshold → lower threshold
- L103 `test_rejects_aux_below_minimum_context(mock_get_client, mock_ctx_len)` (function) — Hard floor: aux context < MINIMUM_CONTEXT_LENGTH (64K) → session
- L126 `test_no_warning_when_aux_context_sufficient(mock_get_client, mock_ctx_len)` (function) — No warning when aux model context >= main model threshold.
- L144 `test_feasibility_check_passes_live_main_runtime()` (function) — Compression feasibility should probe using the live session runtime.
- L176 `test_feasibility_check_passes_config_context_length(mock_get_client, mock_ctx_len)` (function) — auxiliary.compression.context_length from config is forwarded to
- L202 `test_feasibility_check_ignores_invalid_context_length(mock_get_client, mock_ctx_len)` (function) — Non-integer context_length in config is silently ignored.
- L224 `test_init_feasibility_check_uses_aux_context_override_from_config()` (function) — Lazy feasibility check should cache and forward auxiliary.compression.context_length.
- L294 `test_warns_when_no_auxiliary_provider(mock_get_client)` (function) — Warning emitted when no auxiliary provider is configured.
- L309 `test_skips_check_when_compression_disabled()` (function) — No check performed when compression is disabled.
- L323 `test_exception_does_not_crash(mock_get_client)` (function) — Exceptions in the check are caught — never blocks startup.
- L340 `test_exact_threshold_boundary_no_warning(mock_get_client, mock_ctx_len)` (function) — No warning when aux context exactly equals the threshold.
- L358 `test_just_below_threshold_auto_corrects(mock_get_client, mock_ctx_len)` (function) — Auto-correct fires when aux context is one token below the threshold
- L383 `test_warning_stored_for_gateway_replay(mock_get_client, mock_ctx_len)` (function) — __init__ stores the warning; _replay sends it through status_callback.
- L412 `test_no_replay_when_no_warning(mock_get_client, mock_ctx_len)` (function) — _replay_compression_warning is a no-op when there's no stored warning.
- L432 `test_replay_without_callback_is_noop()` (function) — _replay_compression_warning doesn't crash when status_callback is None.
- L444 `test_run_conversation_clears_warning_after_replay(mock_get_client, mock_ctx_len)` (function) — After replay in run_conversation, _compression_warning is cleared
