---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/config.py

Symbols in `gateway/config.py`.

- L25 `_coerce_bool(value: Any, default: bool=True)` (function) — Coerce bool-ish config values, preserving a caller-provided default.
- L39 `_coerce_float(value: Any, default: float)` (function) — Coerce numeric config values, falling back on malformed input.
- L49 `_coerce_int(value: Any, default: int)` (function) — Coerce integer config values, falling back on malformed input.
- L59 `_normalize_unauthorized_dm_behavior(value: Any, default: str='pair')` (function) — Normalize unauthorized DM behavior to a supported value.
- L68 `_normalize_notice_delivery(value: Any, default: str='public')` (function) — Normalize notice delivery mode to a supported value.
- L77 `_ensure_platform_extra_dict(platforms_data: dict, name: str)` (function) — Get-or-create ``platforms_data[name]`` and its nested ``extra`` dict.
- L100 `Platform` (class) — Supported messaging platforms.
- L131 `_missing_(cls, value)` (method) — Accept unknown platform names only for known plugin adapters.
- L176 `_scan_bundled_plugin_platforms(cls)` (method) — Return names of bundled platform plugins under ``plugins/platforms/``.
- L203 `HomeChannel` (class) — Default destination for a platform.
- L217 `to_dict(self)` (method)
- L228 `from_dict(cls, data: Dict[str, Any])` (method)
- L238 `SessionResetPolicy` (class) — Controls when sessions reset (lose context).
- L254 `to_dict(self)` (method)
- L264 `from_dict(cls, data: Dict[str, Any])` (method)
- L281 `PlatformConfig` (class) — Configuration for a single messaging platform.
- L304 `to_dict(self)` (method)
- L320 `from_dict(cls, data: Dict[str, Any])` (method)
- L355 `StreamingConfig` (class) — Configuration for real-time token streaming to messaging platforms.
- L387 `to_dict(self)` (method)
- L398 `from_dict(cls, data: Dict[str, Any])` (method)
- L459 `GatewayConfig` (class) — Main gateway configuration.
- L512 `get_connected_platforms(self)` (method) — Return list of platforms that are enabled and configured.
- L522 `_is_platform_connected(self, platform: Platform, config: PlatformConfig)` (method) — Check whether a single platform is sufficiently configured.
- L556 `get_home_channel(self, platform: Platform)` (method) — Get the home channel for a platform.
- L563 `get_reset_policy(self, platform: Optional[Platform]=None, session_type: Optional[str]=None)` (method) — Get the appropriate reset policy for a session.
- L583 `to_dict(self)` (method)
- L609 `from_dict(cls, data: Dict[str, Any])` (method)
- L679 `get_unauthorized_dm_behavior(self, platform: Optional[Platform]=None)` (method) — Return the effective unauthorized-DM behavior for a platform.
- L690 `get_notice_delivery(self, platform: Optional[Platform]=None)` (method) — Return the effective notice-delivery mode for a platform.
- L702 `load_gateway_config()` (function) — Load gateway configuration from multiple sources.
- L1205 `_validate_gateway_config(config: 'GatewayConfig')` (function) — Validate and sanitize a loaded GatewayConfig in place.
- L1274 `_apply_env_overrides(config: GatewayConfig)` (function) — Apply environment variable overrides to config.
