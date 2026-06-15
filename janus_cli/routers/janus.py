from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.post("/api/janus/update")
async def update_janus():
    """Kick off ``janus update`` in the background."""
    install_method = web_server_mod.detect_install_method(web_server_mod.PROJECT_ROOT)
    if install_method == "docker":
        message = web_server_mod.format_docker_update_message()
        web_server_mod._record_completed_action("janus-update", message, exit_code=1)
        return {
            "ok": False,
            "pid": None,
            "name": "janus-update",
            "error": "docker_update_unsupported",
            "message": message,
            "update_command": web_server_mod.recommended_update_command_for_method(install_method),
        }

    try:
        proc = web_server_mod._spawn_janus_action(["update"], "janus-update")
    except Exception as exc:
        web_server_mod._log.exception("Failed to spawn janus update")
        raise web_server_mod.HTTPException(status_code=500, detail=f"Failed to start update: {exc}")
    return {
        "ok": True,
        "pid": proc.pid,
        "name": "janus-update",
    }

@router.get("/api/janus/update/check")
async def check_janus_update(force: bool = False):
    """Report whether a Janus update is available, without applying it.

    Powers the dashboard's "check before you update" flow: the System page
    shows the commit-behind count and asks the user to confirm before
    ``POST /api/janus/update`` actually runs ``janus update``.

    Returns:
        install_method: 'git' | 'pip' | 'docker' | 'nixos' | 'homebrew' | ...
        current_version: installed Janus version string
        behind: commits behind upstream (>=1), 0 if up to date,
                -1 if behind by an unknown count (nix/pypi), or null if the
                check could not run (offline, no remote, etc.)
        update_available: convenience bool (behind is non-zero and not null)
        can_apply: True when the dashboard's update button can apply it
                   in place (git/pip); False for docker/nix/homebrew where the
                   user must update out-of-band
        update_command: the recommended command for this install method
        message: human-readable guidance for non-applyable methods
    """
    install_method = web_server_mod.detect_install_method(web_server_mod.PROJECT_ROOT)
    update_command = web_server_mod.recommended_update_command_for_method(install_method)

    payload: web_server_mod.Dict[str, web_server_mod.Any] = {
        "install_method": install_method,
        "current_version": web_server_mod.__version__,
        "behind": None,
        "update_available": False,
        "can_apply": install_method in ("git", "pip"),
        "update_command": update_command,
        "message": None,
    }

    if install_method == "docker":
        payload["message"] = web_server_mod.format_docker_update_message()
        return payload

    # banner.check_for_updates() handles git / pypi / nix-revision paths and
    # caches the result for 6h. ``force`` busts the cache so the "Check now"
    # button reflects reality immediately.
    try:
        from janus_cli.banner import check_for_updates

        if force:
            try:
                (web_server_mod.get_janus_home() / ".update_check").unlink()
            except OSError:
                pass

        behind = await web_server_mod.asyncio.to_thread(check_for_updates)
    except Exception:
        web_server_mod._log.exception("Update check failed")
        behind = None

    payload["behind"] = behind
    if behind is None:
        payload["message"] = "Couldn't reach the update source — try again later."
    elif behind == 0:
        payload["message"] = "You're on the latest version."
    else:
        payload["update_available"] = True

    return payload

