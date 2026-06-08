---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_portal_tags.py

Symbols in `tests/agent/test_portal_tags.py`.

- L6 `test_hermes_client_tag_includes_current_version()` (function) — The client tag must reflect hermes_cli.__version__ verbatim.
- L14 `test_hermes_client_tag_format()` (function) — The client tag has the exact shape Nous Portal expects.
- L25 `test_nous_portal_tags_contains_product_and_client()` (function) — Every Nous Portal request gets BOTH the product tag and the version tag.
- L35 `test_nous_portal_tags_returns_fresh_list()` (function) — Callers mutate the returned list; we must not share state across calls.
- L45 `test_auxiliary_client_nous_extra_body_uses_helper()` (function) — auxiliary_client.NOUS_EXTRA_BODY must match the canonical helper output.
- L53 `test_nous_provider_profile_uses_helper()` (function) — The Nous provider profile (main agent loop) must use the canonical tags.
