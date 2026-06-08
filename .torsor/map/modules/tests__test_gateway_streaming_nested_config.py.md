---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_gateway_streaming_nested_config.py

Symbols in `tests/test_gateway_streaming_nested_config.py`.

- L7 `_load_with_yaml_dict(yaml_dict: dict)` (function) — Patch filesystem so load_gateway_config() sees *yaml_dict* as config.yaml.
- L25 `TestStreamingConfigNested` (class)
- L26 `test_top_level_streaming(self)` (method)
- L31 `test_nested_gateway_streaming(self)` (method) — Regression for #25676.
- L37 `test_top_level_takes_precedence(self)` (method)
