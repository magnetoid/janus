---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# skills/red-teaming/godmode/scripts/auto_jailbreak.py

Symbols in `skills/red-teaming/godmode/scripts/auto_jailbreak.py`.

- L297 `_detect_model_family(model: str)` (function) — Detect model family from model ID string.
- L321 `_get_current_model()` (function) — Read current model and provider from Hermes config.yaml.
- L339 `_get_api_key(base_url: str=None)` (function) — Get the appropriate API key.
- L351 `_test_query(client, model, messages, timeout=45)` (function) — Send a test query and return (content, latency, error).
- L371 `_build_messages(system_prompt=None, prefill=None, query=None)` (function) — Build the messages array for an API call.
- L383 `_write_config(system_prompt: str=None, prefill_file: str=None)` (function) — Write jailbreak settings to config.yaml (merges, doesn't overwrite).
- L410 `_write_prefill(prefill_messages: list)` (function) — Write prefill messages to ~/.hermes/prefill.json.
- L421 `auto_jailbreak(model=None, base_url=None, api_key=None, canary=None, dry_run=False, verbose=True)` (function) — Auto-jailbreak pipeline.
- L716 `undo_jailbreak(verbose=True)` (function) — Remove jailbreak settings from config.yaml and delete prefill.json.
