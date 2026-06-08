---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# skills/creative/comfyui/tests/test_cloud_integration.py

Symbols in `skills/creative/comfyui/tests/test_cloud_integration.py`.

- L18 `TestCloudEndpointsLive` (class)
- L19 `test_system_stats_reachable(self, cloud_key)` (method)
- L26 `test_models_endpoint_routed_to_experiment(self, cloud_key)` (method)
- L33 `test_models_endpoint_returns_dicts(self, cloud_key)` (method)
- L46 `test_history_renamed_to_v2(self, cloud_key)` (method)
- L51 `test_object_info_paid_tier(self, cloud_key)` (method)
- L62 `TestCloudCheckDepsLive` (class)
- L63 `test_check_deps_against_cloud(self, cloud_key, sd15_workflow)` (method)
- L70 `test_flux_workflow_models_resolved_via_aliases(self, cloud_key, flux_workflow)` (method) — Flux uses unet/clip folders; cloud has them in diffusion_models/text_encoders.
- L85 `TestHealthCheckLive` (class)
- L86 `test_health_check_passes(self, cloud_key, capsys)` (method)
