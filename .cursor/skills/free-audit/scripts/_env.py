"""Shared env hydration for free-audit scripts.

Matches super-audit: process env wins; optional absolute path via
CEMINI_LLM_ROUTING_ENV only. Does not scan home trees or project dotenv files.
"""
from __future__ import annotations

import os
from pathlib import Path


def load_routing_env() -> None:
    custom = os.environ.get("CEMINI_LLM_ROUTING_ENV", "").strip()
    if not custom:
        return
    p = Path(custom).expanduser()
    if not p.is_file():
        return
    for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        k, v = k.strip(), v.strip().strip('"').strip("'")
        if k and k not in os.environ:
            os.environ[k] = v


def env(name: str, default: str = "") -> str:
    return os.environ.get(name, default).strip()
