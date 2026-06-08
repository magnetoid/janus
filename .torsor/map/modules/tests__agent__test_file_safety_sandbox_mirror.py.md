---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_file_safety_sandbox_mirror.py

Symbols in `tests/agent/test_file_safety_sandbox_mirror.py`.

- L27 `TestClassifySandboxMirrorTarget` (class)
- L28 `test_docker_mirror_soul_md_classified(self, tmp_path)` (method) — The exact path shape reported in #32049.
- L57 `test_other_backends_and_inner_files_match(self, tmp_path, backend, inner)` (method) — The detector is backend-agnostic — sandbox-mirror shape is what matters.
- L74 `test_path_outside_sandbox_returns_none(self, tmp_path)` (method) — A plain Hermes path is not a mirror.
- L84 `test_sandboxes_segment_without_home_hermes_returns_none(self, tmp_path)` (method) — A ``sandboxes/`` directory unrelated to Hermes-state mirroring (e.g.
- L98 `test_sandboxes_segment_with_home_but_no_hermes_returns_none(self, tmp_path)` (method) — ``sandboxes/<backend>/<task>/home/anything-not-hermes`` is not a mirror.
- L111 `test_truncated_sandbox_path_returns_none(self, tmp_path)` (method) — ``…/sandboxes/<backend>/<task>`` without ``home/.hermes/<thing>`` is not a mirror.
- L120 `test_non_existent_path_still_classifies_by_shape(self, tmp_path)` (method) — Detection is path-shape only — it must not require the file to exist
- L146 `TestGetSandboxMirrorWarning` (class)
- L147 `test_non_mirror_returns_none(self, tmp_path)` (method)
- L156 `test_mirror_warning_names_mirror_root_and_inner_path(self, tmp_path)` (method)
- L177 `test_warning_is_defense_in_depth_not_boundary(self, tmp_path)` (method)
- L200 `TestSandboxMirrorIsOrthogonalToCrossProfile` (class) — The sandbox-mirror guard must fire even when the inner path is
- L205 `test_same_profile_mirror_still_flagged(self, tmp_path, monkeypatch)` (method)
