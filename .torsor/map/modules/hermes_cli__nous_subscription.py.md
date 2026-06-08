---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/nous_subscription.py

Symbols in `hermes_cli/nous_subscription.py`.

- L47 `_uses_gateway(section: object)` (function) — Return True when a config section explicitly opts into the gateway.
- L55 `NousFeatureState` (class)
- L69 `NousSubscriptionFeatures` (class)
- L77 `web(self)` (method)
- L81 `image_gen(self)` (method)
- L85 `tts(self)` (method)
- L89 `browser(self)` (method)
- L93 `video_gen(self)` (method)
- L97 `modal(self)` (method)
- L100 `items(self)` (method)
- L106 `_model_config_dict(config: Dict[str, object])` (function)
- L115 `_toolset_enabled(config: Dict[str, object], toolset_key: str)` (function)
- L152 `_has_agent_browser()` (function)
- L162 `_local_browser_runnable()` (function) — Return True when the *local* browser backend would actually start.
- L189 `_browser_label(current_provider: str)` (function)
- L200 `_tts_label(current_provider: str)` (function)
- L212 `_resolve_browser_feature_state(*, browser_tool_enabled: bool, browser_provider: str, browser_provider_explicit: bool, browser_local_available: bool, browser_local_runnable: bool, direct_camofox: bool, direct_browserbase: bool, direct_browser_use: bool, direct_firecrawl: bool, managed_browser_available: bool)` (function) — Resolve browser availability using the same precedence as runtime.
- L288 `get_nous_subscription_features(config: Optional[Dict[str, object]]=None, *, force_fresh: bool=False)` (function)
- L627 `apply_nous_managed_defaults(config: Dict[str, object], *, enabled_toolsets: Optional[Iterable[str]]=None, force_fresh: bool=False)` (function)
- L723 `_get_gateway_direct_credentials()` (function) — Return a dict of tool_key -> has_direct_credentials.
- L758 `get_gateway_eligible_tools(config: Optional[Dict[str, object]]=None, *, force_fresh: bool=False)` (function) — Return (unconfigured, has_direct, already_managed) tool key lists.
- L824 `apply_gateway_defaults(config: Dict[str, object], tool_keys: list[str])` (function) — Apply Tool Gateway config for the given tool keys.
- L887 `prompt_enable_tool_gateway(config: Dict[str, object], *, force_fresh: bool=True)` (function) — If eligible tools exist, prompt the user (per tool) to enable the Tool
- L974 `ensure_nous_portal_access(*, capability: str='the Nous Tool Gateway', coverage_category: Optional[str]=None)` (function) — Make sure the user is entitled to the Nous Tool Gateway, logging in if
- L1042 `_run_nous_portal_login_only(*, capability: str)` (function) — Run the Nous Portal device-code OAuth and persist credentials only.
