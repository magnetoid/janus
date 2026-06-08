---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/homeassistant_tool.py

Symbols in `tools/homeassistant_tool.py`.

- L31 `_get_config()` (function) — Return (hass_url, hass_token) from env vars at call time.
- L63 `_get_headers(token: str='')` (function) — Return authorization headers for HA REST API.
- L77 `_filter_and_summarize(states: list, domain: Optional[str]=None, area: Optional[str]=None)` (function) — Filter raw HA states by domain/area and return a compact summary.
- L105 `_async_list_entities(domain: Optional[str]=None, area: Optional[str]=None)` (function) — Fetch entity states from HA and optionally filter by domain/area.
- L122 `_async_get_state(entity_id: str)` (function) — Fetch detailed state of a single entity.
- L142 `_build_service_payload(entity_id: Optional[str]=None, data: Optional[Dict[str, Any]]=None)` (function) — Build the JSON payload for a HA service call.
- L156 `_parse_service_response(domain: str, service: str, result: Any)` (function) — Parse HA service call response into a structured result.
- L177 `_async_call_service(domain: str, service: str, entity_id: Optional[str]=None, data: Optional[Dict[str, Any]]=None)` (function) — Call a Home Assistant service.
- L207 `_run_async(coro)` (function) — Run an async coroutine from a sync handler.
- L224 `_handle_list_entities(args: dict, **kw)` (function) — Handler for ha_list_entities tool.
- L236 `_handle_get_state(args: dict, **kw)` (function) — Handler for ha_get_state tool.
- L251 `_handle_call_service(args: dict, **kw)` (function) — Handler for ha_call_service tool.
- L295 `_async_list_services(domain: Optional[str]=None)` (function) — Fetch available services from HA and optionally filter by domain.
- L329 `_handle_list_services(args: dict, **kw)` (function) — Handler for ha_list_services tool.
- L344 `_check_ha_available()` (function) — Tool is only available when HASS_TOKEN is set.
