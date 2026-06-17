"""Tests for the consensus setup-wizard section (janus_cli/setup.py)."""
from janus_cli import setup as js


def test_enable_with_tier_models(monkeypatch):
    yesno = iter([True, False])  # enable? yes ; ensemble? no
    monkeypatch.setattr(js, "prompt_yes_no", lambda msg, default=False: next(yesno))
    text = iter(["gpt-mini", "claude-opus"])  # cheap, smart
    monkeypatch.setattr(js, "prompt", lambda msg: next(text))

    cfg = {}
    js.setup_consensus(cfg)
    c = cfg["consensus"]
    assert c["enabled"] is True
    assert c["model_tiers"]["cheap"]["model"] == "gpt-mini"
    assert c["model_tiers"]["smart"]["model"] == "claude-opus"
    assert c["ensemble"]["enabled"] is False


def test_decline_disables(monkeypatch):
    monkeypatch.setattr(js, "prompt_yes_no", lambda msg, default=False: False)
    cfg = {}
    js.setup_consensus(cfg)
    assert cfg["consensus"]["enabled"] is False


def test_blank_tier_inherits_and_ensemble_on(monkeypatch):
    yesno = iter([True, True])  # enable? yes ; ensemble? yes
    monkeypatch.setattr(js, "prompt_yes_no", lambda msg, default=False: next(yesno))
    monkeypatch.setattr(js, "prompt", lambda msg: "")  # blank → inherit main model

    cfg = {}
    js.setup_consensus(cfg)
    c = cfg["consensus"]
    assert c["enabled"] is True
    assert c["model_tiers"]["cheap"].get("model", "") == ""
    assert c["ensemble"]["enabled"] is True
