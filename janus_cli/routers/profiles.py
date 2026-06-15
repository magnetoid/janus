from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.get("/api/profiles/sessions")
async def get_profiles_sessions(
    limit: int = 20,
    offset: int = 0,
    min_messages: int = 0,
    archived: str = "exclude",
    order: str = "recent",
    profile: str = "all",
    source: str = None,
    exclude_sources: str = None,
):
    """Unified, read-only session list aggregated across ALL profiles.

    Intentionally process-light: this opens each profile's ``state.db`` directly
    from disk — it does NOT spawn a dashboard backend per profile. Each returned
    session is tagged with its owning ``profile`` so the desktop renders one
    browsable list and only spins up a profile's backend when the user actually
    interacts (sends a message). A user with a single (default) profile gets the
    same rows as ``/api/sessions``, just tagged ``profile="default"``.
    """
    if archived not in ("exclude", "only", "include"):
        raise web_server_mod.HTTPException(status_code=400, detail="archived must be one of: exclude, only, include")
    if order not in ("created", "recent"):
        raise web_server_mod.HTTPException(status_code=400, detail="order must be one of: created, recent")

    from janus_state import SessionDB
    from janus_cli import profiles as profiles_mod

    targets: web_server_mod.List[web_server_mod.Tuple[str, web_server_mod.Path]] = []
    if profile and profile != "all":
        name, home = web_server_mod._cron_profile_home(profile)
        targets.append((name, home))
    else:
        try:
            infos = profiles_mod.list_profiles()
            targets = [(info.name, info.path) for info in infos]
        except Exception:
            web_server_mod._log.exception("GET /api/profiles/sessions: list_profiles failed")
            targets = []
        if not targets:
            targets.append(("default", profiles_mod.get_profile_dir("default")))

    min_message_count = max(0, min_messages)
    archived_only = archived == "only"
    include_archived = archived == "include"
    # Source scoping (see /api/sessions): recents pass exclude_sources=cron,
    # the cron-jobs section passes source=cron — two independent lists so
    # newest cron sessions can't starve the recents page.
    source_filter = source or None
    exclude_list = [s for s in (exclude_sources or "").split(",") if s.strip()]
    # Over-fetch per profile so the merged+sorted window is correct for the
    # requested page. Capped so a huge profile can't blow up the response.
    per_profile = min(max(limit + offset, limit), 500)

    merged: web_server_mod.List[web_server_mod.Dict[str, web_server_mod.Any]] = []
    total = 0
    profile_totals: web_server_mod.Dict[str, int] = {}
    errors: web_server_mod.List[web_server_mod.Dict[str, str]] = []
    now = web_server_mod.time.time()
    for name, home in targets:
        db_path = web_server_mod.Path(home) / "state.db"
        if not db_path.exists():
            continue
        try:
            # Read-only: this loop runs on every sidebar refresh, so it must
            # never DDL/write-lock another profile's live DB (see SessionDB
            # read_only docstring).
            db = SessionDB(db_path=db_path, read_only=True)
        except Exception as exc:
            errors.append({"profile": name, "error": str(exc)})
            continue
        try:
            rows = db.list_sessions_rich(
                source=source_filter,
                exclude_sources=exclude_list or None,
                limit=per_profile,
                offset=0,
                min_message_count=min_message_count,
                include_archived=include_archived,
                archived_only=archived_only,
                order_by_last_active=order == "recent",
            )
            profile_total = db.session_count(
                source=source_filter,
                exclude_sources=exclude_list or None,
                min_message_count=min_message_count,
                include_archived=include_archived,
                archived_only=archived_only,
                exclude_children=True,
            )
            total += profile_total
            profile_totals[name] = profile_total
            for s in rows:
                s["profile"] = name
                s["is_default_profile"] = name == "default"
                s["is_active"] = (
                    s.get("ended_at") is None
                    and (now - s.get("last_active", s.get("started_at", 0))) < 300
                )
                s["archived"] = bool(s.get("archived"))
                merged.append(s)
        except Exception as exc:
            errors.append({"profile": name, "error": str(exc)})
        finally:
            db.close()

    sort_key = "last_active" if order == "recent" else "started_at"
    merged.sort(key=lambda s: s.get(sort_key) or s.get("started_at") or 0, reverse=True)
    window = merged[offset:offset + limit]
    return {
        "sessions": window,
        "total": total,
        "profile_totals": profile_totals,
        "limit": limit,
        "offset": offset,
        "errors": errors,
    }

@router.get("/api/profiles")
async def list_profiles_endpoint():
    from janus_cli import profiles as profiles_mod
    try:
        return {"profiles": [web_server_mod._profile_to_dict(p) for p in profiles_mod.list_profiles()]}
    except Exception:
        web_server_mod._log.exception("GET /api/profiles failed; falling back to profile directory scan")
        return {"profiles": web_server_mod._fallback_profile_dicts(profiles_mod)}

@router.post("/api/profiles")
async def create_profile_endpoint(body: web_server_mod.ProfileCreate):
    from janus_cli import profiles as profiles_mod
    explicit_source = (body.clone_from or "").strip()
    if explicit_source:
        # Duplicating a specific profile: clone its config/skills/SOUL (or full
        # state when clone_all) from the named source rather than "default".
        clone = True
        clone_from = explicit_source
        clone_config = not body.clone_all
    else:
        clone = body.clone_from_default or body.clone_all
        clone_from = "default" if clone else None
        clone_config = body.clone_from_default and not body.clone_all
    try:
        path = profiles_mod.create_profile(
            name=body.name,
            clone_from=clone_from,
            clone_all=body.clone_all,
            clone_config=clone_config,
            no_skills=body.no_skills,
            description=body.description,
        )
        # Match the CLI's profile-create flow: fresh named profiles get the
        # bundled skills installed. When cloning from default, create_profile()
        # has already copied the source profile's skills, including any
        # user-installed skills. When no_skills=True, create_profile() wrote
        # the opt-out marker and seed_profile_skills() will no-op.
        if not clone:
            profiles_mod.seed_profile_skills(path, quiet=True)

        # Match the CLI's profile-create flow: named profiles should get a
        # wrapper in ~/.local/bin when the alias is safe to create.
        collision = profiles_mod.check_alias_collision(body.name)
        if not collision:
            profiles_mod.create_wrapper_script(body.name)
    except (ValueError, FileExistsError, FileNotFoundError) as e:
        raise web_server_mod.HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        web_server_mod._log.exception("POST /api/profiles failed")
        raise web_server_mod.HTTPException(status_code=500, detail=str(e))

    # Optional explicit model assignment for the new profile. Best-effort:
    # the profile already exists, so a model-write hiccup must not 500 the
    # whole create — the user can set the model later from the Models page
    # or `<profile> setup`.
    provider = (body.provider or "").strip()
    model = (body.model or "").strip()
    model_set = False
    if provider and model:
        try:
            web_server_mod._write_profile_model(path, provider, model)
            model_set = True
        except Exception:
            web_server_mod._log.exception("Setting model for new profile %s failed", body.name)

    return {"ok": True, "name": body.name, "path": str(path), "model_set": model_set}

@router.get("/api/profiles/active")
async def get_active_profile_endpoint():
    """Return the sticky active profile and the profile this dashboard
    process is currently running as.

    ``active`` is the sticky default written by ``janus profile use`` —
    the profile new CLI invocations pick up. ``current`` is the profile
    the running dashboard/gateway is scoped to (derived from JANUS_HOME).
    """
    from janus_cli import profiles as profiles_mod
    try:
        active = profiles_mod.get_active_profile() or "default"
    except Exception:
        active = "default"
    try:
        current = profiles_mod.get_active_profile_name() or "default"
    except Exception:
        current = "default"
    return {"active": active, "current": current}

@router.post("/api/profiles/active")
async def set_active_profile_endpoint(body: web_server_mod.ProfileActiveUpdate):
    """Set the sticky active profile (mirrors ``janus profile use``).

    Note: this does not retarget the already-running dashboard process —
    it changes which profile subsequent CLI commands and gateways use.
    """
    from janus_cli import profiles as profiles_mod
    try:
        profiles_mod.set_active_profile(body.name)
    except FileNotFoundError as e:
        raise web_server_mod.HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise web_server_mod.HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        web_server_mod._log.exception("POST /api/profiles/active failed")
        raise web_server_mod.HTTPException(status_code=500, detail=str(e))
    return {"ok": True, "active": profiles_mod.normalize_profile_name(body.name)}

@router.get("/api/profiles/{name}/setup-command")
async def get_profile_setup_command(name: str):
    return {"command": web_server_mod._profile_setup_command(name)}

@router.post("/api/profiles/{name}/open-terminal")
async def open_profile_terminal_endpoint(name: str):
    try:
        command = web_server_mod._profile_setup_command(name)

        if web_server_mod.sys.platform.startswith("win"):
            web_server_mod.subprocess.Popen(["cmd.exe", "/c", "start", "", command])
        elif web_server_mod.sys.platform == "darwin":
            escaped = command.replace("\\", "\\\\").replace('"', '\\"')
            applescript = (
                'tell application "Terminal"\n'
                "activate\n"
                f'do script "{escaped}"\n'
                "end tell"
            )
            web_server_mod.subprocess.Popen(["osascript", "-e", applescript])
        else:
            terminal_commands = [
                ("x-terminal-emulator", ["x-terminal-emulator", "-e", "sh", "-lc", command]),
                ("gnome-terminal", ["gnome-terminal", "--", "sh", "-lc", command]),
                ("konsole", ["konsole", "-e", "sh", "-lc", command]),
                ("xfce4-terminal", ["xfce4-terminal", "-e", f"sh -lc '{command}'"]),
                ("mate-terminal", ["mate-terminal", "-e", f"sh -lc '{command}'"]),
                ("lxterminal", ["lxterminal", "-e", f"sh -lc '{command}'"]),
                ("tilix", ["tilix", "-e", "sh", "-lc", command]),
                ("alacritty", ["alacritty", "-e", "sh", "-lc", command]),
                ("kitty", ["kitty", "sh", "-lc", command]),
                ("xterm", ["xterm", "-e", "sh", "-lc", command]),
            ]
            for executable, popen_args in terminal_commands:
                if web_server_mod.subprocess.call(
                    ["which", executable],
                    stdout=web_server_mod.subprocess.DEVNULL,
                    stderr=web_server_mod.subprocess.DEVNULL,
                ) == 0:
                    web_server_mod.subprocess.Popen(popen_args)
                    break
            else:
                raise web_server_mod.HTTPException(
                    status_code=400,
                    detail="No supported terminal emulator found",
                )
    except FileNotFoundError as e:
        raise web_server_mod.HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise web_server_mod.HTTPException(status_code=400, detail=str(e))
    except web_server_mod.HTTPException:
        raise
    except Exception as e:
        web_server_mod._log.exception("POST /api/profiles/%s/open-terminal failed", name)
        raise web_server_mod.HTTPException(status_code=500, detail=str(e))
    return {"ok": True, "command": command}

@router.patch("/api/profiles/{name}")
async def rename_profile_endpoint(name: str, body: web_server_mod.ProfileRename):
    from janus_cli import profiles as profiles_mod
    try:
        path = profiles_mod.rename_profile(name, body.new_name)
    except FileNotFoundError as e:
        raise web_server_mod.HTTPException(status_code=404, detail=str(e))
    except (ValueError, FileExistsError) as e:
        raise web_server_mod.HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        web_server_mod._log.exception("PATCH /api/profiles/%s failed", name)
        raise web_server_mod.HTTPException(status_code=500, detail=str(e))
    return {"ok": True, "name": body.new_name, "path": str(path)}

@router.delete("/api/profiles/{name}")
async def delete_profile_endpoint(name: str):
    """Delete a profile. The dashboard collects the user's confirmation in
    its own dialog before this request, so we always pass ``yes=True`` to
    skip the CLI's interactive prompt."""
    from janus_cli import profiles as profiles_mod
    try:
        path = profiles_mod.delete_profile(name, yes=True)
    except FileNotFoundError as e:
        raise web_server_mod.HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise web_server_mod.HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        web_server_mod._log.exception("DELETE /api/profiles/%s failed", name)
        raise web_server_mod.HTTPException(status_code=500, detail=str(e))
    return {"ok": True, "path": str(path)}

@router.get("/api/profiles/{name}/soul")
async def get_profile_soul(name: str):
    soul_path = web_server_mod._resolve_profile_dir(name) / "SOUL.md"
    if soul_path.exists():
        try:
            return {"content": soul_path.read_text(encoding="utf-8"), "exists": True}
        except OSError as e:
            raise web_server_mod.HTTPException(status_code=500, detail=f"Could not read SOUL.md: {e}")
    return {"content": "", "exists": False}

@router.put("/api/profiles/{name}/soul")
async def update_profile_soul(name: str, body: web_server_mod.ProfileSoulUpdate):
    soul_path = web_server_mod._resolve_profile_dir(name) / "SOUL.md"
    try:
        soul_path.write_text(body.content, encoding="utf-8")
    except OSError as e:
        web_server_mod._log.exception("PUT /api/profiles/%s/soul failed", name)
        raise web_server_mod.HTTPException(status_code=500, detail=f"Could not write SOUL.md: {e}")
    return {"ok": True}

@router.put("/api/profiles/{name}/description")
async def update_profile_description_endpoint(name: str, body: web_server_mod.ProfileDescriptionUpdate):
    """Set or clear a profile's role description (kanban routing signal).

    Empty string clears the description. Non-empty stores it as a
    user-authored description (``description_auto: false``) so the
    auto-describer won't overwrite it on a sweep.
    """
    from janus_cli import profiles as profiles_mod
    profile_dir = web_server_mod._resolve_profile_dir(name)
    text = (body.description or "").strip()
    try:
        profiles_mod.write_profile_meta(
            profile_dir,
            description=text,
            description_auto=False,
        )
    except Exception as e:
        web_server_mod._log.exception("PUT /api/profiles/%s/description failed", name)
        raise web_server_mod.HTTPException(status_code=500, detail=str(e))
    return {"ok": True, "description": text, "description_auto": False}

@router.put("/api/profiles/{name}/model")
async def update_profile_model_endpoint(name: str, body: web_server_mod.ProfileModelUpdate):
    """Set the main model (``model.default`` + ``model.provider``) for a
    specific profile's config.yaml, without touching the dashboard's own
    active profile. Mirrors ``POST /api/model/set`` (main scope) but scoped
    to the named profile via the JANUS_HOME override.
    """
    profile_dir = web_server_mod._resolve_profile_dir(name)
    provider = (body.provider or "").strip()
    model = (body.model or "").strip()
    if not provider or not model:
        raise web_server_mod.HTTPException(status_code=400, detail="provider and model are required")
    try:
        web_server_mod._write_profile_model(profile_dir, provider, model)
    except Exception as e:
        web_server_mod._log.exception("PUT /api/profiles/%s/model failed", name)
        raise web_server_mod.HTTPException(status_code=500, detail=str(e))
    return {"ok": True, "provider": provider, "model": model}

@router.post("/api/profiles/{name}/describe-auto")
async def describe_profile_auto_endpoint(name: str, body: web_server_mod.ProfileDescribeAuto):
    """Auto-generate a profile's description via the auxiliary LLM
    (``auxiliary.profile_describer``). Mirrors ``janus profile describe
    <name> --auto``.

    A failed generation (no aux client, LLM error, …) is returned as
    ``ok: false`` with a reason rather than an HTTP error so the UI can
    surface it inline and let the operator fix config and retry.
    """
    web_server_mod._resolve_profile_dir(name)
    try:
        from janus_cli import profile_describer
        outcome = profile_describer.describe_profile(name, overwrite=bool(body.overwrite))
    except Exception as e:
        web_server_mod._log.exception("POST /api/profiles/%s/describe-auto failed", name)
        raise web_server_mod.HTTPException(status_code=500, detail=str(e))
    return {
        "ok": bool(outcome.ok),
        "reason": outcome.reason,
        "description": outcome.description,
        # Only a successful generation is an auto-authored description. A failed
        # sweep leaves any existing description untouched, so don't claim it's
        # auto-generated.
        "description_auto": bool(outcome.ok),
    }

