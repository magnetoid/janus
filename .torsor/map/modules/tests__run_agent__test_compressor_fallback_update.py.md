---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_compressor_fallback_update.py

Symbols in `tests/run_agent/test_compressor_fallback_update.py`.

- L9 `_make_agent_with_compressor()` (function) — Build a minimal AIAgent with a context_compressor, skipping __init__.
- L47 `test_compressor_updated_on_fallback(mock_ctx_len, mock_resolve)` (function) — After fallback activation, the compressor must reflect the fallback model.
- L77 `test_compressor_not_present_does_not_crash(mock_ctx_len, mock_resolve)` (function) — If the agent has no compressor, fallback should still succeed.
