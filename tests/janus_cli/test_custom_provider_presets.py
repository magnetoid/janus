"""Built-in custom-provider presets surface in the provider picker (only)."""
from janus_cli.config import (
    BUILTIN_CUSTOM_PROVIDER_PRESETS,
    custom_providers_for_picker,
    get_compatible_custom_providers,
)


def _apikey_entries(entries):
    return [e for e in entries if "apikey.fun" in str(e.get("base_url", "")).lower()]


def test_apikey_fun_preset_defined():
    names = [p["name"] for p in BUILTIN_CUSTOM_PROVIDER_PRESETS]
    assert any("APIKEY.FUN" in n for n in names)


def test_preset_absent_from_runtime_resolution_view():
    # Critical: the runtime view must NOT include unselected presets, or model
    # resolution would pick apikey.fun when nothing is configured.
    assert _apikey_entries(get_compatible_custom_providers({})) == []


def test_apikey_fun_surfaces_in_picker_with_no_user_providers():
    hits = _apikey_entries(custom_providers_for_picker({}))
    assert hits, "apikey.fun preset should appear in the picker"
    e = hits[0]
    assert "third-party" in e["name"].lower()        # the visible note
    assert e["base_url"].rstrip("/") == "https://api.apikey.fun/v1"
    assert e.get("api_mode") == "chat_completions"


def test_user_providers_and_preset_coexist_in_picker():
    cfg = {"custom_providers": [{"name": "MyLocal", "base_url": "http://localhost:1234/v1"}]}
    names = [str(e.get("name") or "") for e in custom_providers_for_picker(cfg)]
    assert any("MyLocal" in n for n in names)
    assert any("APIKEY.FUN" in n for n in names)


def test_user_apikey_entry_takes_precedence_over_preset():
    # A user who already added apikey.fun (same base_url) shouldn't get a dupe.
    cfg = {"custom_providers": [
        {"name": "my apikey", "base_url": "https://api.apikey.fun/v1", "api_key": "sk-x"},
    ]}
    hits = _apikey_entries(custom_providers_for_picker(cfg))
    assert len(hits) == 1
    assert hits[0]["api_key"] == "sk-x"  # the user's entry won the dedup slot


def test_selecting_keyless_preset_prompts_for_key_and_saves(monkeypatch):
    """The reported bug: selecting the keyless APIKEY.FUN preset never asked for
    a key. It must now prompt and persist the key + base_url."""
    import janus_cli.main as m
    import janus_cli.models as models_mod
    import janus_cli.auth as auth_mod
    import janus_cli.curses_ui as curses_mod
    import janus_cli.secret_prompt as sp_mod
    from janus_cli.config import load_config

    preset = next(
        e for e in custom_providers_for_picker({})
        if "apikey.fun" in str(e.get("base_url", "")).lower()
    )

    prompted = {"called": False}

    def _fake_prompt(*a, **k):
        prompted["called"] = True
        return "sk-test-key"

    monkeypatch.setattr(sp_mod, "masked_secret_prompt", _fake_prompt)
    monkeypatch.setattr(models_mod, "fetch_api_models", lambda *a, **k: ["model-a"])
    monkeypatch.setattr(curses_mod, "curses_radiolist", lambda *a, **k: 0)
    monkeypatch.setattr(auth_mod, "_save_model_choice", lambda *a, **k: None)
    monkeypatch.setattr(auth_mod, "deactivate_provider", lambda *a, **k: None)

    m._model_flow_named_custom({}, preset)

    assert prompted["called"], "should prompt for the API key when the preset has none"
    model = load_config().get("model", {})
    assert model.get("provider") == "custom"
    assert "apikey.fun" in str(model.get("base_url", "")).lower()
    assert model.get("api_key") == "sk-test-key"
