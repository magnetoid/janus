---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# skills/creative/comfyui/tests/test_run_workflow.py

Symbols in `skills/creative/comfyui/tests/test_run_workflow.py`.

- L16 `TestParseInputImageArg` (class)
- L17 `test_with_name(self, tmp_path)` (method)
- L24 `test_without_name_defaults(self, tmp_path)` (method)
- L30 `test_custom_name(self, tmp_path)` (method)
- L37 `TestInjectParams` (class)
- L38 `test_basic_injection(self, sd15_workflow)` (method)
- L50 `test_unknown_param_warns(self, sd15_workflow)` (method)
- L55 `test_seed_minus_one_randomizes(self, sd15_workflow)` (method)
- L62 `test_randomize_seed_when_unset(self, sd15_workflow)` (method)
- L69 `test_does_not_mutate_original(self, sd15_workflow)` (method)
- L75 `test_refuses_to_overwrite_link(self)` (method)
- L105 `TestDownloadOutputsWalk` (class) — Test that download_outputs walks the structure correctly.
- L108 `test_handles_videos_plural(self, tmp_path, monkeypatch)` (method) — Local ComfyUI uses 'videos'/'gifs' (plural) keys.
- L130 `test_handles_video_singular_cloud(self, tmp_path)` (method) — Cloud uses 'video' (singular).
- L146 `test_preserves_subfolder(self, tmp_path)` (method) — When preserve_subfolder=True, server subfolder becomes local subdir.
- L176 `TestRunnerConstruction` (class)
- L177 `test_local_default(self)` (method)
- L182 `test_cloud_detection(self)` (method)
- L187 `test_cloud_subdomain_detected(self)` (method)
- L191 `test_partner_key_does_not_pollute_extra_data(self)` (method)
- L197 `test_url_routing_local(self)` (method)
- L202 `test_url_routing_cloud(self)` (method)
- L207 `test_url_routing_cloud_history_renamed(self)` (method)
