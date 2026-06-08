"""Regression tests for _apply_profile_override JANUS_HOME guard (issue #22502).

When JANUS_HOME is set to the janus root (e.g. systemd hardcodes
JANUS_HOME=/root/.janus), _apply_profile_override must still read
active_profile and update JANUS_HOME to the profile directory.

When JANUS_HOME is already a profile directory (.../profiles/<name>),
_apply_profile_override must trust it and return without re-reading
active_profile (child-process inheritance contract).
"""

from __future__ import annotations

import os
import sys
from pathlib import Path



def _run_apply_profile_override(
    tmp_path, monkeypatch, *, janus_home: str | None, active_profile: str | None,
    argv: list[str] | None = None,
):
    """Run _apply_profile_override in isolation.

    Returns the value of os.environ["JANUS_HOME"] after the call,
    or None if unset.
    """
    janus_root = tmp_path / ".janus"
    janus_root.mkdir(parents=True, exist_ok=True)

    if active_profile is not None:
        (janus_root / "active_profile").write_text(active_profile)

    if active_profile and active_profile != "default":
        (janus_root / "profiles" / active_profile).mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr(Path, "home", lambda: tmp_path)
    if janus_home is not None:
        monkeypatch.setenv("JANUS_HOME", janus_home)
    else:
        monkeypatch.delenv("JANUS_HOME", raising=False)

    monkeypatch.setattr(sys, "argv", argv or ["janus", "gateway", "start"])

    from janus_cli.main import _apply_profile_override
    _apply_profile_override()

    return os.environ.get("JANUS_HOME")


class TestApplyProfileOverrideJanusHomeGuard:
    """Regression guard for issue #22502.

    Verifies that JANUS_HOME pointing to the janus root does NOT suppress
    the active_profile check, while JANUS_HOME already pointing to a
    profile directory IS trusted as-is.
    """

    def test_janus_home_at_root_with_active_profile_is_redirected(
        self, tmp_path, monkeypatch
    ):
        """JANUS_HOME=/root/.janus + active_profile=coder must redirect
        JANUS_HOME to .../profiles/coder.

        Bug scenario from #22502: systemd sets JANUS_HOME to the janus root
        and the user switches to a profile via `janus profile use`.
        Before the fix, the guard returned early and active_profile was ignored.
        """
        janus_root = tmp_path / ".janus"
        janus_root.mkdir(parents=True, exist_ok=True)

        result = _run_apply_profile_override(
            tmp_path,
            monkeypatch,
            janus_home=str(janus_root),
            active_profile="coder",
        )

        assert result is not None, "JANUS_HOME must be set after profile redirect"
        assert "profiles" in result, (
            f"Expected JANUS_HOME to point into profiles/ dir, got: {result!r}"
        )
        assert result.endswith("coder"), (
            f"Expected JANUS_HOME to end with 'coder', got: {result!r}"
        )

    def test_janus_home_already_profile_dir_is_trusted(self, tmp_path, monkeypatch):
        """JANUS_HOME=.../profiles/coder must not be overridden even when
        active_profile says something different.

        Preserves the child-process inheritance contract: a subprocess spawned
        with JANUS_HOME already set to a specific profile must stay in that
        profile.
        """
        janus_root = tmp_path / ".janus"
        profile_dir = janus_root / "profiles" / "coder"
        profile_dir.mkdir(parents=True, exist_ok=True)

        (janus_root / "active_profile").write_text("other")

        monkeypatch.setattr(Path, "home", lambda: tmp_path)
        monkeypatch.setenv("JANUS_HOME", str(profile_dir))
        monkeypatch.setattr(sys, "argv", ["janus", "gateway", "start"])

        from janus_cli.main import _apply_profile_override
        _apply_profile_override()

        assert os.environ.get("JANUS_HOME") == str(profile_dir), (
            "JANUS_HOME must remain unchanged when already pointing to a profile dir"
        )

    def test_janus_home_unset_reads_active_profile(self, tmp_path, monkeypatch):
        """Classic case: JANUS_HOME unset + active_profile=coder must set
        JANUS_HOME to the profile directory (existing behaviour must not regress).
        """
        result = _run_apply_profile_override(
            tmp_path,
            monkeypatch,
            janus_home=None,
            active_profile="coder",
        )

        assert result is not None
        assert "coder" in result

    def test_janus_home_unset_default_profile_no_redirect(self, tmp_path, monkeypatch):
        """active_profile=default must not redirect JANUS_HOME."""
        janus_root = tmp_path / ".janus"
        janus_root.mkdir(parents=True, exist_ok=True)

        monkeypatch.setattr(Path, "home", lambda: tmp_path)
        monkeypatch.delenv("JANUS_HOME", raising=False)
        monkeypatch.setattr(sys, "argv", ["janus", "gateway", "start"])
        (janus_root / "active_profile").write_text("default")

        from janus_cli.main import _apply_profile_override
        _apply_profile_override()

        assert os.environ.get("JANUS_HOME") is None
