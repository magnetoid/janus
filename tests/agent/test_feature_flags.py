"""Gated flag reads: config.yaml value, with an env override on top."""
import yaml

from agent import feature_flags as ff
from janus_constants import get_janus_home


def _write_config(d):
    home = get_janus_home()
    home.mkdir(parents=True, exist_ok=True)
    (home / "config.yaml").write_text(yaml.safe_dump(d), encoding="utf-8")


def test_missing_config_returns_default():
    assert ff.flag_enabled("evals", "autopin", default=False) is False
    assert ff.flag_enabled("learning", "reflexion", default=True) is True


def test_config_value_wins_over_default():
    _write_config({"evals": {"autopin": True}})
    assert ff.flag_enabled("evals", "autopin", default=False) is True


def test_env_override_wins_over_config(monkeypatch):
    _write_config({"evals": {"autopin": False}})
    monkeypatch.setenv("JANUS_FLAG_EVALS__AUTOPIN", "1")
    assert ff.flag_enabled("evals", "autopin", default=False) is True
    monkeypatch.setenv("JANUS_FLAG_EVALS__AUTOPIN", "0")
    assert ff.flag_enabled("evals", "autopin", default=False) is False


def test_nested_key_path():
    _write_config({"evals": {"trend": {"enabled": True}}})
    assert ff.flag_enabled("evals", "trend.enabled", default=False) is True
