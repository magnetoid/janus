---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_security_audit.py

Symbols in `tests/hermes_cli/test_security_audit.py`.

- L20 `TestRequirementsParser` (class)
- L21 `test_extracts_pinned_versions(self)` (method)
- L28 `test_skips_comments_and_options(self)` (method)
- L32 `test_skips_unpinned(self)` (method)
- L37 `test_handles_extras_and_markers(self)` (method)
- L44 `test_handles_empty(self)` (method)
- L49 `TestMCPComponentExtraction` (class)
- L50 `test_npx_scoped_pinned(self)` (method)
- L61 `test_npx_full_path_command(self)` (method)
- L69 `test_uvx_pinned(self)` (method)
- L76 `test_unpinned_returns_none(self)` (method)
- L80 `test_docker_returns_none(self)` (method)
- L84 `test_empty_args(self)` (method)
- L91 `TestPluginDiscovery` (class)
- L92 `test_reads_requirements_txt(self, tmp_path: Path)` (method)
- L101 `test_skips_when_no_plugins_dir(self, tmp_path: Path)` (method)
- L104 `test_skips_hidden_dirs(self, tmp_path: Path)` (method)
- L111 `test_reads_pyproject_dependencies(self, tmp_path: Path)` (method)
- L127 `TestSeverityExtraction` (class)
- L128 `test_database_specific_severity(self)` (method)
- L132 `test_unknown_when_no_severity(self)` (method)
- L135 `test_ecosystem_specific_fallback(self)` (method)
- L139 `test_fixed_versions_extracted_and_deduped(self)` (method)
- L161 `TestRunAudit` (class)
- L162 `test_no_components_returns_empty(self, tmp_path: Path)` (method)
- L168 `test_findings_sorted_by_severity_desc(self, tmp_path: Path)` (method)
- L199 `TestExitCodes` (class)
- L200 `_build_args(self, **kwargs)` (method)
- L213 `test_clean_audit_exits_zero(self, tmp_path: Path, monkeypatch, capsys)` (method)
- L221 `test_finding_above_threshold_exits_one(self, tmp_path: Path, monkeypatch)` (method)
- L241 `test_finding_below_threshold_exits_zero(self, tmp_path: Path, monkeypatch)` (method)
- L260 `test_unknown_fail_on_value_exits_two(self, tmp_path: Path, monkeypatch, capsys)` (method)
- L267 `test_json_output_shape(self, tmp_path: Path, monkeypatch, capsys)` (method)
