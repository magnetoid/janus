---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_uninstall_node_symlinks.py

Symbols in `tests/hermes_cli/test_uninstall_node_symlinks.py`.

- L18 `fake_home(tmp_path, monkeypatch)` (function) — Redirect Path.home() at the home both the installer-symlink target and
- L28 `_make_hermes_node(hermes_home: Path)` (function) — Create a fake $HERMES_HOME/node/bin/{node,npm,npx} tree.
- L38 `test_removes_symlinks_pointing_into_hermes_node(fake_home)` (function)
- L54 `test_leaves_unrelated_symlinks_untouched(fake_home)` (function) — A node symlink the user repointed at nvm must survive uninstall.
- L73 `test_leaves_real_binaries_untouched(fake_home)` (function) — A real (non-symlink) binary in ~/.local/bin is never deleted.
- L90 `test_handles_missing_local_bin(fake_home)` (function) — No symlinks present -> no-op, no error.
- L98 `test_removes_dangling_symlink_into_hermes_node(fake_home)` (function) — A link into the Hermes node dir is removed even if the target file is
- L116 `test_only_some_links_present(fake_home)` (function) — Removes the Hermes links that exist; ignores the ones that don't.
- L135 `test_removes_fhs_symlinks_in_usr_local_bin(fake_home, tmp_path, monkeypatch)` (function) — Root FHS installs place node symlinks in /usr/local/bin.
