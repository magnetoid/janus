"""Tests for directory-bound workspace profiles (janus_cli/workspace.py)."""
from pathlib import Path

import pytest

from janus_cli import workspace as ws


def test_set_read_clear_roundtrip(tmp_path):
    assert ws.read_binding(tmp_path) is None
    path = ws.set_binding(tmp_path, "coder")
    assert path == tmp_path / ".janus" / "workspace.yaml"
    assert path.is_file()
    assert ws.read_binding(tmp_path) == "coder"
    assert ws.clear_binding(tmp_path) is True
    assert ws.read_binding(tmp_path) is None
    assert ws.clear_binding(tmp_path) is False  # nothing left to clear


def test_find_walks_up_to_nearest_binding(tmp_path):
    ws.set_binding(tmp_path, "root-prof")
    nested = tmp_path / "a" / "b" / "c"
    nested.mkdir(parents=True)
    # No validation here — just the walk-up logic.
    assert ws.find_workspace_profile(nested, validate=False) == "root-prof"

    # A nearer binding overrides the ancestor.
    ws.set_binding(tmp_path / "a", "inner-prof")
    assert ws.find_workspace_profile(nested, validate=False) == "inner-prof"


def test_find_returns_none_when_unbound(tmp_path):
    assert ws.find_workspace_profile(tmp_path, validate=False) is None


def test_read_binding_tolerates_garbage(tmp_path):
    p = ws.binding_path(tmp_path)
    p.parent.mkdir(parents=True)
    p.write_text(": not valid yaml : [", encoding="utf-8")
    assert ws.read_binding(tmp_path) is None  # never raises


def test_read_binding_ignores_non_string_profile(tmp_path):
    p = ws.binding_path(tmp_path)
    p.parent.mkdir(parents=True)
    p.write_text("profile:\n  - a\n  - b\n", encoding="utf-8")
    assert ws.read_binding(tmp_path) is None


def test_find_validate_requires_existing_profile(tmp_path, monkeypatch):
    ws.set_binding(tmp_path, "ghost")
    # Profile doesn't exist -> validated lookup returns None (falls back).
    monkeypatch.setattr("janus_cli.profiles.profile_exists", lambda name: False)
    assert ws.find_workspace_profile(tmp_path, validate=True) is None
    # Now it exists -> returned.
    monkeypatch.setattr("janus_cli.profiles.profile_exists", lambda name: True)
    assert ws.find_workspace_profile(tmp_path, validate=True) == "ghost"


def test_find_validate_rejects_bad_name(tmp_path, monkeypatch):
    ws.set_binding(tmp_path, "ok")
    # Even if profile_exists says yes, an invalid id is rejected by the regex.
    ws.binding_path(tmp_path).write_text("profile: 'Bad Name!'\n", encoding="utf-8")
    monkeypatch.setattr("janus_cli.profiles.profile_exists", lambda name: True)
    assert ws.find_workspace_profile(tmp_path, validate=True) is None
