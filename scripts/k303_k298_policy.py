#!/usr/bin/env python3
"""K303/K298 deterministic deny + path policy (Cursor hooks + tests).

K303: NL rules in CLAUDE.md are not enforcement. This module is the control.
K298: secret file bytes must not reach the planner. Deny the read; use secret_grant.py.

Fail-closed for hook callers (--hook). Never print file contents or secret values.
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

DENY_BASENAMES = frozenset(
    {
        ".env",
        ".netrc",
        ".npmrc",
        ".pypirc",
        "credentials.json",
        "credentials.yml",
        "credentials.yaml",
        "secrets.json",
        "secrets.yml",
        "secrets.yaml",
        "id_rsa",
        "id_ed25519",
        "id_ecdsa",
        "id_dsa",
    }
)
ALLOW_ENV_BASENAMES = frozenset(
    {".env.example", ".env.sample", ".env.template", ".env.example.local"}
)
DENY_SUFFIXES = frozenset({".pem", ".p12", ".pfx", ".key"})
GRANT_MARKERS = ("scripts/secret_grant.py", "scripts/k303_k298_policy.py")
SAFE_ENV_META = re.compile(
    r"\b(test\s+-f|test\s+-e|ls(\s|$)|git\s+check-ignore|git\s+status)\b",
    re.I,
)
# git commit messages may mention .env; still deny `git add/show/checkout` of secret paths.
GIT_COMMIT_RE = re.compile(r"^\s*git\s+commit\b", re.I)
GIT_DUMP_RE = re.compile(r"^\s*git\s+(add|show|checkout|restore|diff)\b", re.I)
BARE_ENV_DUMP_RE = re.compile(r"^\s*(printenv|env)\s*$", re.I)
ENV_FILE_RE = re.compile(r"(?:^|[^\w.-])(\.env(?:\.[A-Za-z0-9_.-]+)?)(?:$|[^\w.-])")
PRINTENV_SECRET_RE = re.compile(
    r"\b(printenv|env)\b[^\n]*(?:KEY|TOKEN|SECRET|PASSWORD|PASSWD|CREDENTIAL)",
    re.I,
)
SHELL_SPLIT_RE = re.compile(r"\s*(?:&&|\|\||;|\n)\s*")

DENY_MSG = (
    "K303/K298 deny: secret material is not returned to the planner. "
    "Use `python3 scripts/secret_grant.py -- <command>` (values redacted). "
    ".env.example remains readable."
)


def _norm(path: str) -> Path:
    try:
        return Path(path).expanduser()
    except Exception:
        return Path(str(path))


def is_allowed_env_example(path: Path) -> bool:
    return path.name in ALLOW_ENV_BASENAMES


def is_secret_path(path: str | Path | None) -> bool:
    if not path:
        return False
    p = _norm(str(path))
    name = p.name
    if is_allowed_env_example(p):
        return False
    if name in DENY_BASENAMES:
        return True
    if name.startswith(".env."):
        return True
    if name.endswith(".pub"):
        return False
    suffix = p.suffix.lower()
    if suffix in DENY_SUFFIXES:
        return True
    parts = {part.lower() for part in p.parts}
    if ".ssh" in parts and name not in {"config", "known_hosts", "authorized_keys"}:
        if not name.endswith(".pub"):
            return True
    return False


def is_grant_command(command: str) -> bool:
    return any(m in command for m in GRANT_MARKERS)


def _is_secret_command_segment(command: str) -> bool:
    if not command or not command.strip():
        return False
    if is_grant_command(command):
        return False
    if GIT_COMMIT_RE.match(command):
        return False
    if BARE_ENV_DUMP_RE.match(command):
        return True
    if PRINTENV_SECRET_RE.search(command):
        return True
    for m in ENV_FILE_RE.finditer(command):
        token = m.group(1)
        if token in ALLOW_ENV_BASENAMES:
            continue
        if GIT_DUMP_RE.match(command):
            return True
        if SAFE_ENV_META.search(command) and "cat" not in command.lower() and "head" not in command.lower():
            continue
        return True
    for raw in re.findall(r"(?:^|[\s\"'=])(/[^\s\"']+|~\/[^\s\"']+|\.\/[^\s\"']+)", command):
        if is_secret_path(raw):
            if SAFE_ENV_META.search(command) and not is_allowed_env_example(_norm(raw)):
                if any(x in command.lower() for x in ("cat ", "head ", "tail ", "less ", "more ", "type ")):
                    return True
                continue
            return True
    return False


def is_secret_command(command: str | None) -> bool:
    if not command or not command.strip():
        return False
    if is_grant_command(command):
        return False
    return any(_is_secret_command_segment(part) for part in SHELL_SPLIT_RE.split(command))


def _collect_paths(obj, acc: list[str]) -> None:
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in {"file_path", "path", "target_file", "target_notebook"} and isinstance(v, str):
                acc.append(v)
            else:
                _collect_paths(v, acc)
    elif isinstance(obj, list):
        for item in obj:
            _collect_paths(item, acc)


def extract_command(payload: dict) -> str:
    if isinstance(payload.get("command"), str) and payload.get("hook_event_name") != "beforeMCPExecution":
        # MCP stdio servers also have "command" — only treat as shell when it looks like a user command
        cmd = payload["command"]
        if payload.get("hook_event_name") == "beforeMCPExecution":
            return ""
        return cmd
    tool_input = payload.get("tool_input")
    if isinstance(tool_input, dict) and isinstance(tool_input.get("command"), str):
        return tool_input["command"]
    if isinstance(tool_input, str):
        try:
            parsed = json.loads(tool_input)
            if isinstance(parsed, dict) and isinstance(parsed.get("command"), str):
                return parsed["command"]
        except json.JSONDecodeError:
            pass
    return ""


def decide(payload: dict) -> tuple[str, str]:
    """Return (permission, agent_message)."""
    command = extract_command(payload)
    if is_secret_command(command):
        return "deny", DENY_MSG
    paths: list[str] = []
    _collect_paths(payload, paths)
    for path in paths:
        if is_secret_path(path):
            return "deny", DENY_MSG
    return "allow", ""


def hook_main() -> int:
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        # fail-closed: invalid JSON from Cursor
        sys.stdout.write(json.dumps({"permission": "deny", "agent_message": DENY_MSG, "user_message": DENY_MSG}))
        return 0
    permission, msg = decide(payload)
    out = {"permission": permission}
    if permission == "deny":
        out["agent_message"] = msg
        out["user_message"] = msg
    sys.stdout.write(json.dumps(out))
    return 0


def cli_main(argv: list[str]) -> int:
    if "--hook" in argv or not argv:
        return hook_main()
    if argv[:1] == ["--check-path"] and len(argv) >= 2:
        denied = is_secret_path(argv[1])
        print("deny" if denied else "allow")
        return 1 if denied else 0
    if argv[:1] == ["--check-command"] and len(argv) >= 2:
        denied = is_secret_command(" ".join(argv[1:]))
        print("deny" if denied else "allow")
        return 1 if denied else 0
    print("usage: k303_k298_policy.py --hook | --check-path PATH | --check-command CMD", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(cli_main(sys.argv[1:]))
