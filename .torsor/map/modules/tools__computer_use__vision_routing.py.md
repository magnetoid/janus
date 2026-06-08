---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/computer_use/vision_routing.py

Symbols in `tools/computer_use/vision_routing.py`.

- L56 `_explicit_aux_vision_override(cfg: Optional[Dict[str, Any]])` (function) — True when ``auxiliary.vision`` carries a non-default user override.
- L83 `_lookup_user_declared_supports_vision(provider: str, model: str, cfg: Optional[Dict[str, Any]])` (function) — Return config-declared ``supports_vision`` for the active route.
- L107 `_lookup_supports_vision(provider: str, model: str, cfg: Optional[Dict[str, Any]]=None)` (function) — Return config/models.dev ``supports_vision`` for *(provider, model)*.
- L143 `_provider_accepts_multimodal_tool_result(provider: str, model: str)` (function) — Return whether *provider*+*model* carries images inside tool-result messages.
- L164 `should_route_capture_to_aux_vision(provider: str, model: str, cfg: Optional[Dict[str, Any]])` (function) — Return True iff the captured screenshot should be pre-analysed via aux vision.
