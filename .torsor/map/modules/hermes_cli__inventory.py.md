---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/inventory.py

Symbols in `hermes_cli/inventory.py`.

- L44 `ConfigContext` (class) — Snapshot of the model + provider config every inventory caller
- L56 `with_overrides(self, *, current_provider: Optional[str]=None, current_model: Optional[str]=None, current_base_url: Optional[str]=None)` (method) — Return a copy with truthy overrides applied.
- L79 `load_picker_context()` (function) — Load the disk-config snapshot every consumer needs.
- L111 `build_models_payload(ctx: ConfigContext, *, include_unconfigured: bool=False, picker_hints: bool=False, canonical_order: bool=False, pricing: bool=False, capabilities: bool=False, force_fresh_nous_tier: bool=False, max_models: int=50)` (function) — Build the ``{providers, model, provider}`` shape every consumer
- L178 `_apply_capabilities(rows: list[dict])` (function) — Attach a ``{model: {fast, reasoning}}`` map to each provider row.
- L219 `_append_unconfigured_rows(rows: list[dict], ctx: ConfigContext)` (function) — Build skeleton rows for canonical providers missing from ``rows``.
- L243 `_apply_picker_hints(rows: list[dict])` (function) — Add ``authenticated``/``auth_type``/``key_env``/``warning`` per row.
- L281 `_reorder_canonical(rows: list[dict])` (function) — Canonical slugs in ``CANONICAL_PROVIDERS`` declaration order;
- L302 `_apply_pricing(rows: list[dict], *, force_fresh_nous_tier: bool=False)` (function) — Enrich each provider row with per-model pricing + Nous tier gating.
