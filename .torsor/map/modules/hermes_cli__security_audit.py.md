---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/security_audit.py

Symbols in `hermes_cli/security_audit.py`.

- L58 `Component` (class) — A single (name, version, ecosystem) tuple discovered on disk.
- L68 `Vulnerability` (class)
- L76 `Finding` (class)
- L84 `_discover_venv()` (function) — Every dist installed in the running Python's import path.
- L119 `_parse_requirements(text: str)` (function) — Extract ``name==version`` pins. Everything else (>=, ~=, no pin) is skipped.
- L137 `_parse_pyproject_pins(text: str)` (function) — Pull ``name==version`` pins from a ``pyproject.toml`` ``dependencies`` list.
- L167 `_discover_plugins(hermes_home: Path)` (function) — Python deps declared by plugins under ``~/.hermes/plugins``.
- L216 `_extract_mcp_component(server_name: str, command: str, args: list[str])` (function) — Best-effort: parse `command/args` into a (name, version, ecosystem).
- L258 `_discover_mcp()` (function) — Pinned MCP server packages from ``config.yaml``.
- L285 `_http_post_json(url: str, payload: dict)` (function)
- L294 `_http_get_json(url: str)` (function)
- L300 `_osv_query_batch(components: list[Component])` (function) — Return {component -> [osv_id, ...]} for components with any vulns.
- L332 `_osv_severity_from_record(record: dict)` (function) — Extract CVSS-derived severity tier from an OSV vuln record.
- L369 `_osv_fixed_versions(record: dict)` (function)
- L386 `_osv_fetch_details(vuln_ids: Iterable[str])` (function) — Fetch summary/severity for each unique vuln id, in parallel.
- L414 `run_audit(*, skip_venv: bool=False, skip_plugins: bool=False, skip_mcp: bool=False, hermes_home: Optional[Path]=None)` (function) — Discover components, query OSV, return findings sorted by severity desc.
- L463 `_render_human(findings: list[Finding], total_components: int)` (function)
- L491 `_render_json(findings: list[Finding], total_components: int)` (function)
- L512 `_count_components(*, skip_venv: bool, skip_plugins: bool, skip_mcp: bool, hermes_home: Path)` (function)
- L528 `cmd_security_audit(args: argparse.Namespace)` (function) — Implementation of `hermes security audit`.
