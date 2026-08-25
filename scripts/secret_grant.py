#!/usr/bin/env python3
"""K298 tool-layer grant: run a child with .env loaded; never print secret values.

The planner sees exit code + redacted stdout/stderr only. Prefer this over Read(.env).

Usage:
  python3 scripts/secret_grant.py [--env-file .env] -- <command> [args...]
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

REDACT = "***REDACTED***"


def parse_env_file(path: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    if not path.is_file():
        return env
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if s.startswith("export "):
            s = s[7:].strip()
        if "=" not in s:
            continue
        key, _, val = s.partition("=")
        key = key.strip()
        val = val.strip().strip("'").strip('"')
        if key:
            env[key] = val
    return env


def redact(text: str, secrets: list[str]) -> str:
    out = text
    for secret in sorted({s for s in secrets if s and len(s) >= 4}, key=len, reverse=True):
        out = out.replace(secret, REDACT)
        # also hide URL-encoded / quoted copies of the same token
        out = re.sub(re.escape(secret), REDACT, out)
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run a command with .env injected; redact values from output.")
    parser.add_argument("--env-file", default=".env", help="Path to env file (never printed)")
    parser.add_argument("command", nargs=argparse.REMAINDER, help="Command after --")
    args = parser.parse_args(argv)
    cmd = list(args.command)
    if cmd[:1] == ["--"]:
        cmd = cmd[1:]
    if not cmd:
        print("secret_grant: missing command after --", file=sys.stderr)
        return 2
    root = Path.cwd()
    env_path = Path(args.env_file)
    if not env_path.is_absolute():
        env_path = root / env_path
    loaded = parse_env_file(env_path)
    child_env = os.environ.copy()
    child_env.update(loaded)
    secrets = [v for v in loaded.values() if v]
    try:
        proc = subprocess.run(
            cmd,
            env=child_env,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError as exc:
        print(f"secret_grant: command not found ({exc})", file=sys.stderr)
        return 127
    stdout = redact(proc.stdout or "", secrets)
    stderr = redact(proc.stderr or "", secrets)
    if stdout:
        sys.stdout.write(stdout)
        if not stdout.endswith("\n"):
            sys.stdout.write("\n")
    if stderr:
        sys.stderr.write(stderr)
        if not stderr.endswith("\n"):
            sys.stderr.write("\n")
    print(f"secret_grant: exit={proc.returncode} keys_loaded={len(loaded)} (values not shown)")
    return int(proc.returncode)


if __name__ == "__main__":
    raise SystemExit(main())
