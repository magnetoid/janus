"""Tests for janus_cli/plugin_integrity.py — user plugin integrity pinning."""

import json

import pytest

from janus_cli.plugin_integrity import (
    MODE_BLOCK,
    MODE_OFF,
    MODE_WARN,
    _pins_path,
    check_before_load,
    compute_plugin_digest,
    get_integrity_mode,
    pin_plugin,
    unpin_plugin,
)


@pytest.fixture
def plugin_dir(tmp_path):
    d = tmp_path / "myplugin"
    d.mkdir()
    (d / "plugin.yaml").write_text("name: myplugin\n", encoding="utf-8")
    (d / "__init__.py").write_text("def register(ctx):\n    pass\n", encoding="utf-8")
    return d


def _write_config(mode):
    import yaml
    from janus_constants import get_janus_home

    cfg = get_janus_home() / "config.yaml"
    cfg.parent.mkdir(parents=True, exist_ok=True)
    cfg.write_text(
        yaml.safe_dump({"security": {"plugin_integrity": mode}}), encoding="utf-8"
    )


class TestDigest:
    def test_deterministic(self, plugin_dir):
        assert compute_plugin_digest(plugin_dir) == compute_plugin_digest(plugin_dir)

    def test_content_change_changes_digest(self, plugin_dir):
        before = compute_plugin_digest(plugin_dir)
        (plugin_dir / "__init__.py").write_text("EVIL = 1\n", encoding="utf-8")
        assert compute_plugin_digest(plugin_dir) != before

    def test_rename_changes_digest(self, plugin_dir):
        before = compute_plugin_digest(plugin_dir)
        (plugin_dir / "__init__.py").rename(plugin_dir / "helper.py")
        (plugin_dir / "__init__.py").write_text(
            "def register(ctx):\n    pass\n", encoding="utf-8"
        )
        assert compute_plugin_digest(plugin_dir) != before

    def test_pycache_ignored(self, plugin_dir):
        before = compute_plugin_digest(plugin_dir)
        cache = plugin_dir / "__pycache__"
        cache.mkdir()
        (cache / "x.py").write_text("ignored", encoding="utf-8")
        assert compute_plugin_digest(plugin_dir) == before

    def test_non_code_files_ignored(self, plugin_dir):
        before = compute_plugin_digest(plugin_dir)
        (plugin_dir / "README.md").write_text("docs", encoding="utf-8")
        assert compute_plugin_digest(plugin_dir) == before


class TestCheckBeforeLoad:
    def test_first_load_pins_and_allows(self, plugin_dir):
        allowed, msg = check_before_load("myplugin", plugin_dir)
        assert allowed is True
        assert msg is None
        pins = json.loads(_pins_path().read_text(encoding="utf-8"))
        assert pins["myplugin"]["digest"] == compute_plugin_digest(plugin_dir)

    def test_unchanged_allows_silently(self, plugin_dir):
        check_before_load("myplugin", plugin_dir)
        allowed, msg = check_before_load("myplugin", plugin_dir)
        assert allowed is True
        assert msg is None

    def test_changed_warn_mode_allows_and_repins(self, plugin_dir):
        check_before_load("myplugin", plugin_dir)
        (plugin_dir / "__init__.py").write_text("CHANGED = 1\n", encoding="utf-8")
        allowed, msg = check_before_load("myplugin", plugin_dir)
        assert allowed is True
        assert msg and "changed" in msg
        # Re-pinned: next load is silent
        allowed, msg = check_before_load("myplugin", plugin_dir)
        assert allowed is True
        assert msg is None

    def test_changed_block_mode_refuses(self, plugin_dir):
        check_before_load("myplugin", plugin_dir)
        _write_config(MODE_BLOCK)
        (plugin_dir / "__init__.py").write_text("CHANGED = 1\n", encoding="utf-8")
        allowed, msg = check_before_load("myplugin", plugin_dir)
        assert allowed is False
        assert "janus plugins trust" in msg
        # trust re-pins → allowed again
        pin_plugin("myplugin", plugin_dir)
        allowed, msg = check_before_load("myplugin", plugin_dir)
        assert allowed is True

    def test_off_mode_skips(self, plugin_dir):
        _write_config(MODE_OFF)
        allowed, msg = check_before_load("myplugin", plugin_dir)
        assert allowed is True
        assert not _pins_path().exists()

    def test_unpin_removes_entry(self, plugin_dir):
        check_before_load("myplugin", plugin_dir)
        unpin_plugin("myplugin")
        pins = json.loads(_pins_path().read_text(encoding="utf-8"))
        assert "myplugin" not in pins

    def test_corrupt_pins_file_fails_open(self, plugin_dir):
        _pins_path().parent.mkdir(parents=True, exist_ok=True)
        _pins_path().write_text("{not json", encoding="utf-8")
        allowed, _ = check_before_load("myplugin", plugin_dir)
        assert allowed is True


class TestModeResolution:
    def test_default_is_warn(self):
        assert get_integrity_mode() == MODE_WARN

    def test_unknown_mode_falls_back_to_warn(self):
        _write_config("paranoid")
        assert get_integrity_mode() == MODE_WARN

    def test_block_mode_read(self):
        _write_config(MODE_BLOCK)
        assert get_integrity_mode() == MODE_BLOCK
