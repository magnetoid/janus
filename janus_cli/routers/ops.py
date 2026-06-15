from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.post("/api/ops/prompt-size")
async def run_prompt_size():
    try:
        proc = web_server_mod._spawn_janus_action(["prompt-size"], "prompt-size")
    except Exception as exc:
        raise web_server_mod.HTTPException(status_code=500, detail=f"Failed: {exc}")
    return {"ok": True, "pid": proc.pid, "name": "prompt-size"}

@router.post("/api/ops/dump")
async def run_dump():
    try:
        proc = web_server_mod._spawn_janus_action(["dump"], "dump")
    except Exception as exc:
        raise web_server_mod.HTTPException(status_code=500, detail=f"Failed: {exc}")
    return {"ok": True, "pid": proc.pid, "name": "dump"}

@router.post("/api/ops/config-migrate")
async def run_config_migrate():
    try:
        proc = web_server_mod._spawn_janus_action(["config", "migrate"], "config-migrate")
    except Exception as exc:
        raise web_server_mod.HTTPException(status_code=500, detail=f"Failed: {exc}")
    return {"ok": True, "pid": proc.pid, "name": "config-migrate"}

@router.post("/api/ops/debug-share")
async def run_debug_share_endpoint(body: web_server_mod.DebugShareRequest | None = None):
    """Upload a redacted debug report + full logs and return the paste URLs.

    Unlike the other diagnostics actions (doctor, dump, prompt-size) this is
    *synchronous*: the whole point of ``debug share`` is the set of shareable
    URLs it produces, so we run the upload in a worker thread and return the
    structured ``{urls, failures, redacted, ...}`` payload directly. The
    dashboard renders those as real, copyable links instead of scraping a log
    tail. Pastes auto-delete after 6 hours (handled inside the share core).
    """
    from janus_cli.debug import build_debug_share

    req = body or web_server_mod.DebugShareRequest()
    try:
        result = await web_server_mod.asyncio.to_thread(
            build_debug_share,
            log_lines=max(1, min(int(req.lines), 5000)),
            redact=bool(req.redact),
        )
    except RuntimeError as exc:
        # Required summary-report upload failed (offline / paste service down).
        raise web_server_mod.HTTPException(status_code=502, detail=f"Upload failed: {exc}")
    except Exception as exc:
        web_server_mod._log.exception("debug share failed")
        raise web_server_mod.HTTPException(status_code=500, detail=f"Failed: {exc}")

    return {
        "ok": True,
        "urls": result.urls,
        "failures": result.failures,
        "redacted": result.redacted,
        "auto_delete_seconds": result.auto_delete_seconds,
    }

@router.post("/api/ops/doctor")
async def run_doctor():
    try:
        proc = web_server_mod._spawn_janus_action(["doctor"], "doctor")
    except Exception as exc:
        web_server_mod._log.exception("Failed to spawn doctor")
        raise web_server_mod.HTTPException(status_code=500, detail=f"Failed to run doctor: {exc}")
    return {"ok": True, "pid": proc.pid, "name": "doctor"}

@router.post("/api/ops/security-audit")
async def run_security_audit():
    try:
        proc = web_server_mod._spawn_janus_action(["security", "audit"], "security-audit")
    except Exception as exc:
        web_server_mod._log.exception("Failed to spawn security audit")
        raise web_server_mod.HTTPException(status_code=500, detail=f"Failed to run security audit: {exc}")
    return {"ok": True, "pid": proc.pid, "name": "security-audit"}

@router.post("/api/ops/backup")
async def run_backup(body: web_server_mod.BackupRequest):
    args = ["backup"]
    if body.output:
        args.append(body.output.strip())
    try:
        proc = web_server_mod._spawn_janus_action(args, "backup")
    except Exception as exc:
        web_server_mod._log.exception("Failed to spawn backup")
        raise web_server_mod.HTTPException(status_code=500, detail=f"Failed to run backup: {exc}")
    return {"ok": True, "pid": proc.pid, "name": "backup"}

@router.post("/api/ops/import")
async def run_import(body: web_server_mod.ImportRequest):
    archive = (body.archive or "").strip()
    if not archive:
        raise web_server_mod.HTTPException(status_code=400, detail="archive path is required")
    if not web_server_mod.os.path.isfile(archive):
        raise web_server_mod.HTTPException(status_code=404, detail=f"Archive not found: {archive}")
    try:
        proc = web_server_mod._spawn_janus_action(["import", archive], "import")
    except Exception as exc:
        web_server_mod._log.exception("Failed to spawn import")
        raise web_server_mod.HTTPException(status_code=500, detail=f"Failed to run import: {exc}")
    return {"ok": True, "pid": proc.pid, "name": "import"}

@router.get("/api/ops/hooks")
async def list_hooks():
    """List configured shell hooks from config.yaml with consent + health.

    Reports each hook's allowlist (consent) status and whether the script is
    currently executable, plus the set of valid hook events so the create
    form can offer them.
    """
    from janus_cli.config import load_config as _load_config
    from agent import shell_hooks

    try:
        from janus_cli.plugins import VALID_HOOKS
        valid_events = sorted(VALID_HOOKS)
    except Exception:
        valid_events = []

    specs = []
    try:
        specs = shell_hooks.iter_configured_hooks(_load_config())
    except Exception:
        web_server_mod._log.exception("iter_configured_hooks failed")

    out = []
    for spec in specs:
        entry = None
        try:
            entry = shell_hooks.allowlist_entry_for(spec.event, spec.command)
        except Exception:
            pass
        executable = False
        try:
            executable = shell_hooks.script_is_executable(spec.command)
        except Exception:
            pass
        out.append({
            "event": spec.event,
            "matcher": spec.matcher,
            "command": spec.command,
            "timeout": spec.timeout,
            "allowed": entry is not None,
            "approved_at": (entry or {}).get("approved_at"),
            "executable": executable,
        })

    return {"hooks": out, "valid_events": valid_events}

@router.post("/api/ops/hooks")
async def create_hook(body: web_server_mod.HookCreate):
    """Add a shell hook to config.yaml (and optionally approve it).

    Shell hooks run arbitrary commands, so this is a privileged action: it
    writes to the ``hooks:`` config block and, when ``approve`` is set, records
    consent in the allowlist so the hook actually fires.  Takes effect on the
    next session / gateway restart.
    """
    from agent import shell_hooks

    event = (body.event or "").strip()
    command = (body.command or "").strip()
    if not event or not command:
        raise web_server_mod.HTTPException(status_code=400, detail="event and command are required")

    try:
        from janus_cli.plugins import VALID_HOOKS
        if event not in VALID_HOOKS:
            raise web_server_mod.HTTPException(
                status_code=400,
                detail=f"Unknown event '{event}'. Valid: {', '.join(sorted(VALID_HOOKS))}",
            )
    except web_server_mod.HTTPException:
        raise
    except Exception:
        pass

    cfg = web_server_mod.load_config()
    hooks_cfg = cfg.get("hooks")
    if not isinstance(hooks_cfg, dict):
        hooks_cfg = {}
        cfg["hooks"] = hooks_cfg
    entries = hooks_cfg.get(event)
    if not isinstance(entries, list):
        entries = []
        hooks_cfg[event] = entries

    new_entry: web_server_mod.Dict[str, web_server_mod.Any] = {"command": command}
    if body.matcher:
        new_entry["matcher"] = body.matcher
    if body.timeout is not None:
        new_entry["timeout"] = int(body.timeout)
    entries.append(new_entry)
    web_server_mod.save_config(cfg)

    approved = False
    if body.approve:
        try:
            shell_hooks._record_approval(event, command)
            approved = True
        except Exception:
            web_server_mod._log.exception("hook consent record failed")

    return {"ok": True, "event": event, "command": command, "approved": approved}

@router.delete("/api/ops/hooks")
async def delete_hook(body: web_server_mod.HookDelete):
    """Remove a hook from config.yaml and revoke its consent allowlist entry."""
    from agent import shell_hooks

    event = (body.event or "").strip()
    command = (body.command or "").strip()
    if not event or not command:
        raise web_server_mod.HTTPException(status_code=400, detail="event and command are required")

    cfg = web_server_mod.load_config()
    hooks_cfg = cfg.get("hooks")
    removed = False
    if isinstance(hooks_cfg, dict) and isinstance(hooks_cfg.get(event), list):
        before = len(hooks_cfg[event])
        hooks_cfg[event] = [
            e for e in hooks_cfg[event]
            if not (isinstance(e, dict) and e.get("command") == command)
        ]
        removed = len(hooks_cfg[event]) < before
        if not hooks_cfg[event]:
            del hooks_cfg[event]
        if not hooks_cfg:
            cfg.pop("hooks", None)
        web_server_mod.save_config(cfg)

    # Revoke consent regardless so a re-add re-prompts.
    try:
        shell_hooks.revoke(command)
    except Exception:
        pass

    if not removed:
        raise web_server_mod.HTTPException(status_code=404, detail="No matching hook found")
    return {"ok": True}

@router.get("/api/ops/checkpoints")
async def list_checkpoints():
    """List the /rollback shadow store checkpoints (read-only)."""
    # Checkpoints live under <janus_home>/checkpoints/.  Surface a count +
    # total size so the dashboard can show what a prune would reclaim; the
    # actual prune is a spawned action so confirmation/pruning logic stays
    # in one place (the CLI).
    cp_dir = web_server_mod.get_janus_home() / "checkpoints"

    def _scan_checkpoints() -> tuple[list, int]:
        sessions = []
        total_bytes = 0
        if cp_dir.is_dir():
            for child in sorted(cp_dir.iterdir()):
                if not child.is_dir():
                    continue
                size = 0
                count = 0
                for f in child.rglob("*"):
                    if f.is_file():
                        try:
                            size += f.stat().st_size
                            count += 1
                        except OSError:
                            pass
                total_bytes += size
                sessions.append({
                    "session": child.name,
                    "files": count,
                    "bytes": size,
                })
        return sessions, total_bytes

    sessions, total_bytes = await web_server_mod.asyncio.to_thread(_scan_checkpoints)
    return {"sessions": sessions, "total_bytes": total_bytes}

@router.post("/api/ops/checkpoints/prune")
async def prune_checkpoints():
    try:
        proc = web_server_mod._spawn_janus_action(["checkpoints", "prune"], "checkpoints-prune")
    except Exception as exc:
        web_server_mod._log.exception("Failed to spawn checkpoints prune")
        raise web_server_mod.HTTPException(status_code=500, detail=f"Failed to prune checkpoints: {exc}")
    return {"ok": True, "pid": proc.pid, "name": "checkpoints-prune"}

