---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/providers/test_transport_parity.py

Symbols in `tests/providers/test_transport_parity.py`.

- L15 `transport()` (function)
- L19 `_simple_messages()` (function)
- L23 `_max_tokens_fn(n)` (function)
- L27 `TestNvidiaParity` (class) — NVIDIA NIM: default max_tokens=16384.
- L30 `test_default_max_tokens(self, transport)` (method) — NVIDIA default max_tokens=16384 comes from profile, not legacy is_nvidia_nim flag.
- L44 `test_user_max_tokens_overrides(self, transport)` (method)
- L59 `TestKimiParity` (class) — Kimi: OMIT temperature, max_tokens=32000, thinking + reasoning_effort.
- L62 `test_temperature_omitted(self, transport)` (method)
- L72 `test_default_max_tokens(self, transport)` (method)
- L82 `test_thinking_enabled(self, transport)` (method)
- L95 `test_thinking_enabled_without_effort(self, transport)` (method)
- L107 `test_thinking_disabled(self, transport)` (method)
- L118 `test_reasoning_effort_top_level(self, transport)` (method) — Kimi reasoning_effort is a TOP-LEVEL api_kwargs key, NOT in extra_body.
- L130 `test_reasoning_effort_default_no_effort(self, transport)` (method)
- L145 `TestOpenRouterParity` (class) — OpenRouter: provider preferences, reasoning in extra_body.
- L148 `test_provider_preferences(self, transport)` (method)
- L159 `test_reasoning_passes_full_config(self, transport)` (method) — OpenRouter passes the FULL reasoning_config dict, not just effort.
- L172 `test_default_reasoning_when_no_config(self, transport)` (method) — When supports_reasoning=True but no config, adds default.
- L184 `TestNousParity` (class) — Nous: product tags, reasoning, omit when disabled.
- L187 `test_tags(self, transport)` (method)
- L197 `test_reasoning_omitted_when_disabled(self, transport)` (method) — Nous special case: reasoning omitted entirely when disabled.
- L209 `test_reasoning_enabled(self, transport)` (method)
- L222 `TestQwenParity` (class) — Qwen: max_tokens=65536, vl_high_resolution, metadata top-level.
- L225 `test_default_max_tokens(self, transport)` (method)
- L235 `test_vl_high_resolution(self, transport)` (method)
- L244 `test_metadata_top_level(self, transport)` (method) — Qwen metadata goes to top-level api_kwargs, NOT extra_body.
- L258 `TestCustomOllamaParity` (class) — Custom/Ollama: num_ctx, thinking controls — now tested via profile.
- L261 `test_ollama_num_ctx(self, transport)` (method)
- L271 `test_think_false_when_disabled(self, transport)` (method)
