---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_file_write_safety.py

Symbols in `tests/tools/test_file_write_safety.py`.

- L14 `TestStaticDenyList` (class) — Basic sanity checks for the static write deny list.
- L17 `test_temp_file_not_denied_by_default(self, tmp_path: Path)` (method)
- L21 `test_ssh_key_is_denied(self)` (method)
- L24 `test_etc_shadow_is_denied(self)` (method)
- L28 `TestSafeWriteRoot` (class) — HERMES_WRITE_SAFE_ROOT should sandbox writes to a specific subtree.
- L31 `test_writes_inside_safe_root_are_allowed(self, tmp_path: Path, monkeypatch)` (method)
- L39 `test_writes_to_safe_root_itself_are_allowed(self, tmp_path: Path, monkeypatch)` (method)
- L46 `test_writes_outside_safe_root_are_denied(self, tmp_path: Path, monkeypatch)` (method)
- L55 `test_safe_root_env_ignores_empty_value(self, tmp_path: Path, monkeypatch)` (method)
- L60 `test_safe_root_unset_allows_all(self, tmp_path: Path, monkeypatch)` (method)
- L65 `test_safe_root_with_tilde_expansion(self, tmp_path: Path, monkeypatch)` (method) — ~ in HERMES_WRITE_SAFE_ROOT should be expanded.
- L75 `test_safe_root_does_not_override_static_deny(self, tmp_path: Path, monkeypatch)` (method) — Even if a static-denied path is inside the safe root, it's still denied.
- L82 `TestCheckSensitivePathMacOSBypass` (class) — Verify _check_sensitive_path blocks /private/etc paths (issue #8734).
- L85 `test_etc_hosts_blocked(self)` (method)
- L89 `test_private_etc_hosts_blocked(self)` (method)
- L93 `test_private_etc_ssh_config_blocked(self)` (method)
- L97 `test_private_var_blocked(self)` (method)
- L101 `test_boot_still_blocked(self)` (method)
- L105 `test_safe_path_allowed(self)` (method)
- L110 `TestAtomicWrite` (class) — write_file / patch land via a temp-file + atomic rename.
- L120 `ops(self, tmp_path: Path)` (method)
- L126 `test_overwrite_changes_inode(self, ops, tmp_path: Path)` (method)
- L137 `test_overwrite_preserves_mode(self, ops, tmp_path: Path)` (method)
- L145 `test_failed_write_leaves_original_intact(self, ops, tmp_path: Path)` (method)
- L164 `test_no_temp_file_leaked_on_success(self, ops, tmp_path: Path)` (method)
- L169 `test_special_chars_roundtrip(self, ops, tmp_path: Path)` (method)
- L176 `test_patch_routes_through_atomic_write(self, ops, tmp_path: Path)` (method)
- L186 `TestBomHandling` (class) — UTF-8 BOM is stripped on read and preserved across write/patch.
- L198 `ops(self, tmp_path: Path)` (method)
- L204 `test_helpers(self)` (method)
- L215 `test_read_strips_bom(self, ops, tmp_path: Path)` (method)
- L226 `test_read_raw_strips_bom(self, ops, tmp_path: Path)` (method)
- L234 `test_write_preserves_bom(self, ops, tmp_path: Path)` (method)
- L244 `test_write_no_bom_when_original_had_none(self, ops, tmp_path: Path)` (method)
- L251 `test_write_does_not_double_bom(self, ops, tmp_path: Path)` (method)
- L262 `test_patch_roundtrip_preserves_bom(self, ops, tmp_path: Path)` (method)
- L271 `test_patch_matches_first_line_through_bom(self, ops, tmp_path: Path)` (method)
