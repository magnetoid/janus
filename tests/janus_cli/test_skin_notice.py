"""One-time 'new look' notice after the redesign ships."""
from janus_cli import skin_notice
from janus_cli.skin_engine import set_active_skin


def test_shows_once_then_never_again():
    set_active_skin("default")
    lines = []
    assert skin_notice.maybe_show_redesign_notice(print_fn=lines.append) is True
    assert any("/skin classic" in str(l) for l in lines)
    lines.clear()
    assert skin_notice.maybe_show_redesign_notice(print_fn=lines.append) is False
    assert lines == []


def test_silent_when_user_already_switched_skins():
    set_active_skin("classic")
    lines = []
    try:
        assert skin_notice.maybe_show_redesign_notice(print_fn=lines.append) is False
        assert lines == []
    finally:
        set_active_skin("default")


def test_never_raises(monkeypatch):
    monkeypatch.setattr(skin_notice, "_stamp_path",
                        lambda: (_ for _ in ()).throw(RuntimeError("disk")))
    assert skin_notice.maybe_show_redesign_notice(print_fn=print) is False
