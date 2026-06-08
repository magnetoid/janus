---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# skills/creative/comfyui/scripts/extract_schema.py

Symbols in `skills/creative/comfyui/scripts/extract_schema.py`.

- L48 `infer_type(value: Any)` (function)
- L64 `trace_to_node(workflow: dict, link: list, *, max_hops: int=8)` (function) — Follow a [node_id, slot] link, hopping through Reroute / Primitive nodes
- L96 `find_negative_prompt_node(workflow: dict)` (function) — Trace `negative` input of a sampler back to the source text encoder.
- L113 `find_positive_prompt_node(workflow: dict)` (function)
- L129 `extract_schema(workflow: dict)` (function) — Extract controllable parameters from a workflow.
- L274 `main(argv: list[str] | None=None)` (function)
