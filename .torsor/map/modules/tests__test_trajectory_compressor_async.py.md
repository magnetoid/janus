---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_trajectory_compressor_async.py

Symbols in `tests/test_trajectory_compressor_async.py`.

- L19 `TestAsyncClientLazyCreation` (class) — trajectory_compressor.py — _get_async_client()
- L22 `test_async_client_none_after_init(self)` (method) — async_client should be None after __init__ (not eagerly created).
- L36 `test_get_async_client_creates_new_client(self)` (method) — _get_async_client() should create a fresh AsyncOpenAI instance.
- L56 `test_get_async_client_creates_fresh_each_call(self)` (method) — Each call to _get_async_client() creates a NEW client instance,
- L86 `TestSourceLineVerification` (class) — Verify the actual source has the lazy pattern applied.
- L90 `_read_file()` (method)
- L96 `test_no_eager_async_openai_in_init(self)` (method) — __init__ should NOT create AsyncOpenAI eagerly.
- L112 `test_get_async_client_method_exists(self)` (method) — _get_async_client method should exist.
- L119 `test_generate_summary_async_kimi_omits_temperature()` (function) — Kimi models should have temperature omitted — server manages it.
- L147 `test_generate_summary_async_public_moonshot_kimi_k2_5_omits_temperature()` (function) — kimi-k2.5 on the public Moonshot API should not get a forced temperature.
- L176 `test_generate_summary_async_public_moonshot_cn_kimi_k2_5_omits_temperature()` (function) — kimi-k2.5 on api.moonshot.cn should not get a forced temperature.
