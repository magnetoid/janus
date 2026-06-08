---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/model-providers/bedrock/__init__.py

Symbols in `plugins/model-providers/bedrock/__init__.py`.

- L7 `BedrockProfile` (class) — AWS Bedrock — no REST /v1/models endpoint; uses AWS SDK.
- L10 `fetch_models(self, *, api_key: str | None=None, timeout: float=8.0)` (method) — Bedrock model listing requires AWS SDK, not a REST call.
