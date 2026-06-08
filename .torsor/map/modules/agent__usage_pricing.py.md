---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/usage_pricing.py

Symbols in `agent/usage_pricing.py`.

- L30 `CanonicalUsage` (class)
- L40 `prompt_tokens(self)` (method)
- L44 `total_tokens(self)` (method)
- L49 `BillingRoute` (class)
- L57 `PricingEntry` (class)
- L70 `CostResult` (class)
- L539 `_to_decimal(value: Any)` (function)
- L548 `_to_int(value: Any)` (function)
- L555 `resolve_billing_route(model_name: str, provider: Optional[str]=None, base_url: Optional[str]=None)` (function)
- L584 `_normalize_anthropic_model_name(model: str)` (function) — Normalize Anthropic model name variants to canonical form.
- L601 `_lookup_official_docs_pricing(route: BillingRoute)` (function)
- L617 `_openrouter_pricing_entry(route: BillingRoute)` (function)
- L626 `_pricing_entry_from_metadata(metadata: Dict[str, Dict[str, Any]], model_id: str, *, source_url: str, pricing_version: str)` (function)
- L670 `get_pricing_entry(model_name: str, provider: Optional[str]=None, base_url: Optional[str]=None, api_key: Optional[str]=None)` (function)
- L700 `normalize_usage(response_usage: Any, *, provider: Optional[str]=None, api_mode: Optional[str]=None)` (function) — Normalize raw API response usage into canonical token buckets.
- L773 `estimate_usage_cost(model_name: str, usage: CanonicalUsage, *, provider: Optional[str]=None, base_url: Optional[str]=None, api_key: Optional[str]=None)` (function)
- L852 `has_known_pricing(model_name: str, provider: Optional[str]=None, base_url: Optional[str]=None, api_key: Optional[str]=None)` (function) — Check whether we have pricing data for this model+route.
- L871 `format_duration_compact(seconds: float)` (function)
- L885 `format_token_count_compact(value: int)` (function)
