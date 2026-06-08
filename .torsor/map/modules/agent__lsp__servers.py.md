---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/lsp/servers.py

Symbols in `agent/lsp/servers.py`.

- L109 `SpawnSpec` (class) — The result of resolving a server for a file.
- L127 `ServerDef` (class) — Definition of one language server.
- L147 `matches(self, file_path: str)` (method) — Return True iff this server handles ``file_path``.
- L154 `ServerContext` (class) — Context passed into :meth:`ServerDef.build_spawn`.
- L174 `_file_ext_or_basename(path: str)` (function) — Return the lower-cased extension OR full basename for extensionless files.
- L188 `_which(*names: str)` (function) — Return the full path of the first command found on PATH.
- L197 `_root_or_workspace(file_path: str, workspace: str, markers: Sequence[str], excludes: Sequence[str]=())` (function) — Common pattern: try ``nearest_root``, fall back to workspace root.
- L229 `_spawn_pyright(root: str, ctx: ServerContext)` (function)
- L261 `_detect_python(root: str)` (function)
- L274 `_spawn_typescript(root: str, ctx: ServerContext)` (function)
- L291 `_spawn_gopls(root: str, ctx: ServerContext)` (function)
- L307 `_spawn_rust_analyzer(root: str, ctx: ServerContext)` (function)
- L323 `_spawn_clangd(root: str, ctx: ServerContext)` (function)
- L342 `_spawn_bash_ls(root: str, ctx: ServerContext)` (function)
- L370 `_spawn_yaml_ls(root: str, ctx: ServerContext)` (function)
- L386 `_spawn_lua_ls(root: str, ctx: ServerContext)` (function)
- L402 `_spawn_intelephense(root: str, ctx: ServerContext)` (function)
- L420 `_spawn_ocamllsp(root: str, ctx: ServerContext)` (function)
- L433 `_spawn_dockerfile_ls(root: str, ctx: ServerContext)` (function)
- L449 `_spawn_terraform_ls(root: str, ctx: ServerContext)` (function)
- L469 `_spawn_dart(root: str, ctx: ServerContext)` (function)
- L482 `_spawn_haskell_ls(root: str, ctx: ServerContext)` (function)
- L497 `_spawn_julia(root: str, ctx: ServerContext)` (function)
- L516 `_spawn_clojure_lsp(root: str, ctx: ServerContext)` (function)
- L529 `_spawn_nixd(root: str, ctx: ServerContext)` (function)
- L542 `_spawn_zls(root: str, ctx: ServerContext)` (function)
- L555 `_spawn_gleam(root: str, ctx: ServerContext)` (function)
- L568 `_spawn_elixir_ls(root: str, ctx: ServerContext)` (function)
- L581 `_spawn_prisma(root: str, ctx: ServerContext)` (function)
- L594 `_spawn_kotlin_ls(root: str, ctx: ServerContext)` (function)
- L609 `_spawn_jdtls(root: str, ctx: ServerContext)` (function)
- L625 `_spawn_vue(root: str, ctx: ServerContext)` (function)
- L643 `_spawn_svelte(root: str, ctx: ServerContext)` (function)
- L661 `_spawn_astro(root: str, ctx: ServerContext)` (function)
- L679 `_resolve_override(ctx: ServerContext, server_id: str)` (function) — User can pin a binary path in config.
- L692 `_root_python(file_path: str, workspace: str)` (function)
- L700 `_root_typescript(file_path: str, workspace: str)` (function)
- L717 `_root_go(file_path: str, workspace: str)` (function)
- L725 `_root_rust(file_path: str, workspace: str)` (function)
- L729 `_root_ruby(file_path: str, workspace: str)` (function)
- L733 `_root_clangd(file_path: str, workspace: str)` (function)
- L741 `_root_bash(file_path: str, workspace: str)` (function)
- L745 `_root_yaml(file_path: str, workspace: str)` (function)
- L749 `_root_lua(file_path: str, workspace: str)` (function)
- L757 `_root_php(file_path: str, workspace: str)` (function)
- L761 `_root_ocaml(file_path: str, workspace: str)` (function)
- L765 `_root_docker(file_path: str, workspace: str)` (function)
- L769 `_root_terraform(file_path: str, workspace: str)` (function)
- L773 `_root_dart(file_path: str, workspace: str)` (function)
- L777 `_root_haskell(file_path: str, workspace: str)` (function)
- L781 `_root_julia(file_path: str, workspace: str)` (function)
- L785 `_root_clojure(file_path: str, workspace: str)` (function)
- L791 `_root_nix(file_path: str, workspace: str)` (function)
- L796 `_root_zig(file_path: str, workspace: str)` (function)
- L800 `_root_elixir(file_path: str, workspace: str)` (function)
- L804 `_root_prisma(file_path: str, workspace: str)` (function)
- L810 `_root_kotlin(file_path: str, workspace: str)` (function)
- L818 `_root_java(file_path: str, workspace: str)` (function)
- L1018 `find_server_for_file(file_path: str)` (function) — Return the registry entry that handles ``file_path``, or None.
- L1026 `language_id_for(path: str)` (function) — Return the LSP languageId to send in didOpen for ``path``.
