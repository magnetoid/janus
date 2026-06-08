---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/image_gen/openai-codex/__init__.py

Symbols in `plugins/image_gen/openai-codex/__init__.py`.

- L89 `_load_image_gen_config()` (function) — Read ``image_gen`` from config.yaml (returns {} on any failure).
- L102 `_resolve_model()` (function) — Decide which tier to use and return ``(model_id, meta)``.
- L128 `_read_codex_access_token()` (function) — Return a usable Codex OAuth token, or None.
- L146 `_build_responses_payload(*, prompt: str, size: str, quality: str)` (function) — Build the Codex Responses request body for an image_generation call.
- L175 `_extract_image_b64(value: Any)` (function) — Return the newest image b64 embedded in a Responses event payload.
- L198 `_iter_sse_json(response: Any)` (function) — Yield JSON payloads from an SSE response without OpenAI SDK parsing.
- L245 `_collect_image_b64(token: str, *, prompt: str, size: str, quality: str)` (function) — Stream a Codex Responses image_generation call and return the b64 image.
- L283 `OpenAICodexImageGenProvider` (class) — gpt-image-2 routed through ChatGPT/Codex OAuth instead of an API key.
- L287 `name(self)` (method)
- L291 `display_name(self)` (method)
- L294 `is_available(self)` (method)
- L303 `list_models(self)` (method)
- L315 `default_model(self)` (method)
- L318 `get_setup_schema(self)` (method)
- L330 `generate(self, prompt: str, aspect_ratio: str=DEFAULT_ASPECT_RATIO, **kwargs: Any)` (method)
- L440 `register(ctx)` (function) — Plugin entry point — register the Codex-backed image-gen provider.
