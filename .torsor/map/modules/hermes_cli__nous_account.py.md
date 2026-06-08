---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/nous_account.py

Symbols in `hermes_cli/nous_account.py`.

- L37 `NousPortalSubscriptionInfo` (class)
- L48 `NousPaidServiceAccessInfo` (class)
- L64 `NousToolAccessInfo` (class) — Free tool-pool entitlement, decoupled from paid/billing access.
- L77 `NousPortalAccountInfo` (class)
- L102 `is_paid(self)` (method)
- L106 `is_free_tier(self)` (method)
- L110 `tool_gateway_entitled(self)` (method) — Coarse "entitled to any managed tool" gate: paid access OR a live
- L118 `tool_gateway_entitled_for(self, category: str)` (method) — Whether a specific tool category is entitled. Paid users are entitled
- L128 `nous_portal_billing_url(account_info: Optional[NousPortalAccountInfo]=None)` (function) — Return the billing URL for a normalized Nous account snapshot.
- L143 `format_nous_portal_entitlement_message(account_info: Optional[NousPortalAccountInfo], *, capability: str='this feature', include_refresh_hint: bool=True, coverage_category: Optional[str]=None)` (function) — Return user-facing guidance for a missing Nous tool-gateway entitlement.
- L234 `_no_paid_access_message(account_info: NousPortalAccountInfo, capability: str, billing_url: str)` (function)
- L274 `_credit_detail(total_usable: Optional[float], subscription_credits: Optional[float], purchased_credits: Optional[float])` (function)
- L291 `reset_nous_portal_account_info_cache()` (function) — Clear the short-lived account-info cache used by tests.
- L297 `get_nous_portal_account_info(*, force_fresh: bool=False, min_jwt_ttl_seconds: int=60)` (function) — Return normalized Nous Portal account entitlement information.
- L353 `_fresh_account_info(*, state: dict[str, Any], force_fresh: bool, portal_base_url: Optional[str])` (function)
- L406 `_info_from_inference_key_pool(portal_base_url: Optional[str])` (function) — Return an explicit unknown-entitlement snapshot for opaque Nous keys.
- L439 `_info_from_oauth_pool(*, force_fresh: bool, min_jwt_ttl_seconds: int, portal_base_url: Optional[str])` (function)
- L510 `_select_nous_pool_entry()` (function)
- L529 `_pool_entry_is_portal_oauth(entry: Any)` (function)
- L538 `_fetch_nous_account_info(access_token: str, portal_base_url: Optional[str]=None)` (function)
- L554 `_info_from_valid_jwt(token: str, *, state: dict[str, Any], portal_base_url: Optional[str], min_jwt_ttl_seconds: int)` (function)
- L604 `_info_from_account_payload(payload: dict[str, Any], *, state: dict[str, Any], portal_base_url: Optional[str])` (function)
- L642 `_tool_access_from_value(value: Any)` (function) — Parse a Portal ``tool_access`` object (from the JWT claim or the account
- L659 `_subscription_from_payload(value: Any)` (function)
- L673 `_paid_service_access_from_payload(value: Any)` (function)
- L694 `_error_info(*, error: object, logged_in: bool, portal_base_url: Optional[str]=None, raw_account: Optional[dict[str, Any]]=None)` (function)
- L711 `_portal_base_url(state: dict[str, Any])` (function)
- L718 `_cache_key(access_token: str, portal_base_url: Optional[str])` (function)
- L723 `_parse_iso_timestamp(value: Any)` (function)
- L735 `_coerce_str(value: Any)` (function)
- L741 `_coerce_bool(value: Any)` (function)
- L745 `_coerce_int(value: Any)` (function)
- L756 `_coerce_float(value: Any)` (function)
