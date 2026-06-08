---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/model_normalize.py

Symbols in `hermes_cli/model_normalize.py`.

- L147 `_normalize_for_deepseek(model_name: str)` (function) — Map a model input to a DeepSeek-accepted identifier.
- L186 `_strip_vendor_prefix(model_name: str)` (function) — Remove a ``vendor/`` prefix if present.
- L203 `_dots_to_hyphens(model_name: str)` (function) — Replace dots with hyphens in a model name.
- L212 `_normalize_provider_alias(provider_name: str)` (function) — Resolve provider aliases to Hermes' canonical ids.
- L225 `_strip_matching_provider_prefix(model_name: str, target_provider: str)` (function) — Strip ``provider/`` only when the prefix matches the target provider.
- L246 `detect_vendor(model_name: str)` (function) — Detect the vendor slug from a bare model name.
- L296 `_prepend_vendor(model_name: str)` (function) — Prepend the detected ``vendor/`` prefix if missing.
- L326 `normalize_model_for_provider(model_input: str, target_provider: str)` (function) — Translate a model name into the format the target provider's API expects.
