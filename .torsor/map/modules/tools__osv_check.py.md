---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/osv_check.py

Symbols in `tools/osv_check.py`.

- L26 `check_package_for_malware(command: str, args: list)` (function) — Check if an MCP server package has known malware advisories.
- L65 `_infer_ecosystem(command: str)` (function) — Infer package ecosystem from the command name.
- L75 `_parse_package_from_args(args: list, ecosystem: str)` (function) — Extract package name and optional version from command args.
- L119 `_parse_npm_package(token: str)` (function) — Parse npm package: @scope/name@version or name@version.
- L136 `_parse_pypi_package(token: str)` (function) — Parse PyPI package: name==version or name[extras]==version.
- L145 `_query_osv(package: str, ecosystem: str, version: Optional[str]=None)` (function) — Query the OSV API for MAL-* advisories. Returns list of malware vulns.
