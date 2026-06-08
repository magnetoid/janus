---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/mixture_of_agents_tool.py

Symbols in `tools/mixture_of_agents_tool.py`.

- L90 `_construct_aggregator_prompt(system_prompt: str, responses: List[str])` (function) — Construct the final system prompt for the aggregator including all model responses.
- L105 `_run_reference_model_safe(model: str, user_prompt: str, temperature: float=REFERENCE_TEMPERATURE, max_tokens: int=32000, max_retries: int=6)` (function) — Run a single reference model with retry logic and graceful failure handling.
- L181 `_run_aggregator_model(system_prompt: str, user_prompt: str, temperature: float=AGGREGATOR_TEMPERATURE, max_tokens: int=None)` (function) — Run the aggregator model to synthesize the final response.
- L236 `mixture_of_agents_tool(user_prompt: str, reference_models: Optional[List[str]]=None, aggregator_model: Optional[str]=None)` (function) — Process a complex query using the Mixture-of-Agents methodology.
- L412 `check_moa_requirements()` (function) — Check if all requirements for MoA tools are met.
- L423 `get_moa_configuration()` (function) — Get the current MoA configuration settings.
