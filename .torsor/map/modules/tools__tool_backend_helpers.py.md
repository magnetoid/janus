---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/tool_backend_helpers.py

Symbols in `tools/tool_backend_helpers.py`.

- L17 `managed_nous_tools_enabled(*, force_fresh: bool=False)` (function) — Return True when the user is entitled to the Nous Tool Gateway.
- L44 `nous_tool_gateway_unavailable_message(capability: str='the Nous Tool Gateway', *, force_fresh: bool=False)` (function) — Return account-aware guidance for an unavailable Nous Tool Gateway path.
- L71 `normalize_browser_cloud_provider(value: object | None)` (function) — Return a normalized browser provider key.
- L77 `coerce_modal_mode(value: object | None)` (function) — Return the requested modal mode when valid, else the default.
- L85 `normalize_modal_mode(value: object | None)` (function) — Return a normalized modal execution mode.
- L90 `has_direct_modal_credentials()` (function) — Return True when direct Modal credentials/config are available.
- L102 `resolve_modal_backend_state(modal_mode: object | None, *, has_direct: bool, managed_ready: bool, managed_enabled: bool | None=None)` (function) — Resolve direct vs managed Modal backend selection.
- L141 `resolve_openai_audio_api_key()` (function) — Prefer the voice-tools key, but fall back to the normal OpenAI key.
- L149 `prefers_gateway(config_section: str)` (function) — Return True when the user opted into the Tool Gateway for this tool.
- L164 `fal_key_is_configured()` (function) — Return True when FAL_KEY is set to a non-whitespace value.
