#!/usr/bin/env python3
"""K312 non-decaying loop safety state (Cursor hooks + CLI).

Trajectory-scoped guards re-init each loop. This accumulator persists across
hook invocations, does not decay, and bounds *unauthorized* irreversible
actions. Mediated / known-safe paths are logged but do not consume the bound.

Grant: python3 scripts/k312_loop_state.py grant --n 2 --reason "…"
State: .local/k312-loop-state.json (gitignored). Override with K312_STATE_PATH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STATE = ROOT / ".local" / "k312-loop-state.json"
DEFAULT_BOUND = 3
MAX_EVENTS = 200

DENY_MSG = (
    "K312 deny: unauthorized irreversible actions hit the loop bound. "
    "State does not decay. Mediate with "
    "`python3 scripts/k312_loop_state.py grant --n N --reason '…'`."
)

GRANT_MARKERS = (
    "scripts/k312_loop_state.py",
    "scripts/k303_k298_policy.py",
    "scripts/secret_grant.py",
)

# Known operator-mediated durable writes (still logged; do not consume bound).
AUTHORIZED_RES = (
    re.compile(r"archive_raw_to_egress\.sh\b"),
    re.compile(r"scp_harness_briefs_to_prod\.sh\b"),
    re.compile(r"\bgit\s+push\b(?!.*(?:\s-f\b|\s--force\b))"),
    re.compile(r"\bgit\s+commit\b"),
    re.compile(r"cemini-prod:/opt/cemini/briefs"),
)

UNAUTHORIZED_RES = (
    re.compile(r"\bgit\s+push\b.*(?:\s-f\b|\s--force\b)"),
    re.compile(r"curl\s+[^|\n]*\|\s*(?:ba)?sh\b"),
    re.compile(r"wget\s+[^|\n]*\|\s*(?:ba)?sh\b"),
    re.compile(r"docker\b[^\n]*--network=host"),
    re.compile(r"\bssh\s+cemini-prod\b"),
    re.compile(r"\bLIVE\b.*\b[Dd]iscord\b|\b[Dd]iscord\b.*\bLIVE\b"),
    re.compile(r"rm\s+-[^\n]*r[^\n]*f\s+/\s*$"),
)

SENSITIVE_PATH_RES = (
    re.compile(r"(?:^|/)(?:\.cursor/)?mcp\.json$"),
    re.compile(r"(?:^|/)\.cursor/skills(?:/|$)"),
    re.compile(r"(?:^|/)\.claude/settings\.json$"),
)

sys.path.insert(0, str(ROOT / "scripts"))
try:
    from k303_k298_policy import extract_command, _collect_paths  # type: ignore
except Exception:  # pragma: no cover — tests import both from scripts/
    extract_command = None  # type: ignore
    _collect_paths = None  # type: ignore


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def state_path() -> Path:
    raw = os.environ.get("K312_STATE_PATH")
    return Path(raw) if raw else DEFAULT_STATE


def bound() -> int:
    raw = os.environ.get("K312_BOUND", str(DEFAULT_BOUND))
    try:
        n = int(raw)
    except ValueError:
        n = DEFAULT_BOUND
    return max(1, n)


def empty_state() -> dict:
    return {
        "loop_id": hashlib.sha256(_now().encode()).hexdigest()[:12],
        "created": _now(),
        "bound": bound(),
        "unauthorized_count": 0,
        "authorized_irreversible_count": 0,
        "granted_irreversible_count": 0,
        "grant_remaining": 0,
        "events": [],
    }


def load_state(path: Path | None = None) -> dict:
    p = path or state_path()
    if not p.is_file():
        return empty_state()
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return empty_state()
    if not isinstance(data, dict) or "unauthorized_count" not in data:
        return empty_state()
    data.setdefault("events", [])
    data.setdefault("grant_remaining", 0)
    data.setdefault("authorized_irreversible_count", 0)
    data.setdefault("granted_irreversible_count", 0)
    data["bound"] = bound()
    return data


def save_state(state: dict, path: Path | None = None) -> None:
    p = path or state_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    events = state.get("events") or []
    if len(events) > MAX_EVENTS:
        state["events"] = events[-MAX_EVENTS:]
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    tmp.replace(p)


def cmd_hash(command: str) -> str:
    return hashlib.sha256(command.encode("utf-8", "replace")).hexdigest()[:16]


def is_grant_command(command: str) -> bool:
    return any(m in command for m in GRANT_MARKERS)


def classify_command(command: str | None) -> str:
    """observe | authorized | unauthorized"""
    if not command or not command.strip():
        return "observe"
    if is_grant_command(command):
        return "observe"
    for rx in UNAUTHORIZED_RES:
        if rx.search(command):
            return "unauthorized"
    for rx in AUTHORIZED_RES:
        if rx.search(command):
            return "authorized"
    return "observe"


def classify_paths(paths: list[str]) -> str:
    for raw in paths:
        norm = raw.replace("\\", "/")
        for rx in SENSITIVE_PATH_RES:
            if rx.search(norm):
                return "unauthorized"
    return "observe"


def classify_payload(payload: dict) -> str:
    command = ""
    if extract_command is not None:
        command = extract_command(payload) or ""
    elif isinstance(payload.get("command"), str):
        command = payload["command"]
    kind = classify_command(command)
    if kind != "observe":
        return kind
    paths: list[str] = []
    if _collect_paths is not None:
        _collect_paths(payload, paths)
    for key in ("file_path", "path", "target_file"):
        val = payload.get(key)
        if isinstance(val, str):
            paths.append(val)
    return classify_paths(paths)


def _append_event(state: dict, kind: str, decision: str, command: str) -> None:
    state["events"].append(
        {
            "ts": _now(),
            "class": kind,
            "decision": decision,
            "cmd_sha16": cmd_hash(command) if command else "",
        }
    )


def apply_decision(state: dict, kind: str, command: str = "") -> tuple[str, str]:
    """Mutate state. Return (permission, message). Counts never decay."""
    if kind == "observe":
        return "allow", ""
    if kind == "authorized":
        state["authorized_irreversible_count"] = int(state.get("authorized_irreversible_count", 0)) + 1
        _append_event(state, kind, "allow", command)
        return "allow", ""
    # unauthorized
    grant_left = int(state.get("grant_remaining", 0))
    if grant_left > 0:
        state["grant_remaining"] = grant_left - 1
        state["granted_irreversible_count"] = int(state.get("granted_irreversible_count", 0)) + 1
        _append_event(state, kind, "allow-grant", command)
        return "allow", ""
    used = int(state.get("unauthorized_count", 0))
    cap = int(state.get("bound", bound()))
    if used >= cap:
        _append_event(state, kind, "deny", command)
        return "deny", DENY_MSG
    state["unauthorized_count"] = used + 1
    _append_event(state, kind, "allow", command)
    return "allow", ""


def decide(payload: dict, persist: bool = True) -> tuple[str, str]:
    kind = classify_payload(payload)
    command = ""
    if extract_command is not None:
        command = extract_command(payload) or ""
    elif isinstance(payload.get("command"), str):
        command = payload["command"]
    state = load_state()
    permission, msg = apply_decision(state, kind, command)
    if persist and kind != "observe":
        save_state(state)
    return permission, msg


def grant(n: int, reason: str, persist: bool = True) -> dict:
    state = load_state()
    add = max(1, n)
    state["grant_remaining"] = int(state.get("grant_remaining", 0)) + add
    state.setdefault("grants", []).append({"ts": _now(), "n": add, "reason": reason[:200]})
    if persist:
        save_state(state)
    return state


def hook_main() -> int:
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        sys.stdout.write(json.dumps({"permission": "deny", "agent_message": DENY_MSG, "user_message": DENY_MSG}))
        return 0
    permission, msg = decide(payload, persist=True)
    out: dict = {"permission": permission}
    if permission == "deny":
        out["agent_message"] = msg
        out["user_message"] = msg
    sys.stdout.write(json.dumps(out))
    return 0


def cli_main(argv: list[str]) -> int:
    if "--hook" in argv or not argv:
        return hook_main()
    parser = argparse.ArgumentParser(prog="k312_loop_state.py")
    sub = parser.add_subparsers(dest="cmd")
    sub.add_parser("status")
    g = sub.add_parser("grant")
    g.add_argument("--n", type=int, default=1)
    g.add_argument("--reason", required=True)
    chk = sub.add_parser("check-command")
    chk.add_argument("command", nargs="+")
    args = parser.parse_args(argv)
    if args.cmd == "status":
        st = load_state()
        print(json.dumps({k: st[k] for k in st if k != "events"}, indent=2))
        print(f"events: {len(st.get('events') or [])}", file=sys.stderr)
        return 0
    if args.cmd == "grant":
        st = grant(args.n, args.reason)
        print(json.dumps({"grant_remaining": st["grant_remaining"], "reason": args.reason}))
        return 0
    if args.cmd == "check-command":
        command = " ".join(args.command)
        kind = classify_command(command)
        print(kind)
        return 0 if kind != "unauthorized" else 1
    parser.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(cli_main(sys.argv[1:]))
