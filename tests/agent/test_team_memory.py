"""Tests for shared team memory (agent/team_memory.py)."""
import pytest

from agent import team_memory as tm


@pytest.fixture
def team_dir(tmp_path, monkeypatch):
    """Point memory.team_dir at a shared folder via config.yaml in an isolated home."""
    import yaml
    home = tmp_path / ".janus"
    home.mkdir()
    shared = tmp_path / "shared"
    monkeypatch.setenv("JANUS_HOME", str(home))
    (home / "config.yaml").write_text(
        yaml.safe_dump({"memory": {"team_dir": str(shared)}}), encoding="utf-8")
    return shared


def test_disabled_when_unconfigured(tmp_path, monkeypatch):
    monkeypatch.setenv("JANUS_HOME", str(tmp_path / ".janus"))
    (tmp_path / ".janus").mkdir()
    assert tm.is_enabled() is False
    assert tm.add_team_entry("x") is False
    assert tm.load_team_entries() == []


def test_add_load_with_attribution(team_dir):
    assert tm.is_enabled() is True
    assert tm.add_team_entry("staging deploys on Fridays", author="coder") is True
    entries = tm.load_team_entries()
    assert entries == ["staging deploys on Fridays  — coder"]
    # written to the SHARED dir, readable by another profile pointed at it
    assert (team_dir / "TEAM.md").is_file()


def test_add_dedupes(team_dir):
    tm.add_team_entry("shared fact", author="a")
    tm.add_team_entry("shared fact", author="a")
    assert len(tm.load_team_entries()) == 1


def test_remove(team_dir):
    tm.add_team_entry("keep this", author="a")
    tm.add_team_entry("drop this one", author="b")
    assert tm.remove_team_entry("drop this") is True
    remaining = tm.load_team_entries()
    assert len(remaining) == 1 and "keep this" in remaining[0]
    assert tm.remove_team_entry("nonexistent") is False


def test_render_block(team_dir):
    assert tm.render_team_block() == ""  # empty when no entries
    tm.add_team_entry("api base is api.example.com", author="ops")
    block = tm.render_team_block()
    assert block.startswith("[Shared team memory]")
    assert "api.example.com" in block


def test_two_profiles_share_one_dir(tmp_path, monkeypatch):
    import yaml
    shared = tmp_path / "shared"
    # profile A writes
    homeA = tmp_path / "a" / ".janus"; homeA.mkdir(parents=True)
    monkeypatch.setenv("JANUS_HOME", str(homeA))
    (homeA / "config.yaml").write_text(yaml.safe_dump({"memory": {"team_dir": str(shared)}}), encoding="utf-8")
    tm.add_team_entry("shared across profiles", author="A")
    # profile B (different home, same team_dir) reads
    homeB = tmp_path / "b" / ".janus"; homeB.mkdir(parents=True)
    monkeypatch.setenv("JANUS_HOME", str(homeB))
    (homeB / "config.yaml").write_text(yaml.safe_dump({"memory": {"team_dir": str(shared)}}), encoding="utf-8")
    assert any("shared across profiles" in e for e in tm.load_team_entries())
