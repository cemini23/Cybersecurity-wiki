#!/usr/bin/env python3
"""Discover API + local Ollama models for super-audit API leg (masked output).

Credentials come from the process environment only. Optionally load one
operator-supplied routing file via CEMINI_LLM_ROUTING_ENV (absolute path).
Never scans project dotenv files or hardcoded secret paths.

Usage:
  # preferred: export keys in the shell (or source a local routing file yourself)
  python3 discover_api_keys.py
  python3 discover_api_keys.py --json
  python3 discover_api_keys.py --write-auditors reports/audit/auditors.json
  python3 discover_api_keys.py --workspace /path/to/project
"""
from __future__ import annotations

import argparse
import json
import os
import re
import urllib.error
import urllib.request
from pathlib import Path

# Provider auth / routing vars this skill may read for outbound LLM calls only.
# Values are never logged in full — see _mask().
KEY_VARS = (
    "OPENROUTER_API_KEY",
    "ADVISOR_API_KEY",
    "ANTHROPIC_API_KEY",
    "OPENAI_API_KEY",
)
URL_VARS = (
    "OPENROUTER_BASE_URL",
    "OPENROUTER_PREMIUM_MODEL",
    "OLLAMA_BASE_URL",
    "OLLAMA_MODEL",
    "ADVISOR_BASE_URL",
    "ADVISOR_MODEL",
)

DEFAULT_PREMIUM_MODEL = "z-ai/glm-5.2"
FUSION_MODEL = "openrouter/fusion"
DEFAULT_OLLAMA_HOST = "http://localhost:11434"
DEFAULT_OLLAMA_V1 = f"{DEFAULT_OLLAMA_HOST}/v1"


def _mask(value: str) -> str:
    v = value.strip()
    if len(v) <= 8:
        return "***"
    return f"{v[:6]}…{v[-4:]}"


def _load_env_file(path: Path) -> dict[str, str]:
    """Parse KEY=VALUE lines from an operator-supplied routing file."""
    out: dict[str, str] = {}
    if not path.is_file():
        return out
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        k, v = k.strip(), v.strip().strip('"').strip("'")
        if k:
            out[k] = v
    return out


def _routing_file_from_env() -> Path | None:
    """Single optional path from CEMINI_LLM_ROUTING_ENV (operator-controlled)."""
    custom = os.environ.get("CEMINI_LLM_ROUTING_ENV", "").strip()
    if not custom:
        return None
    return Path(custom).expanduser()


def _ollama_host_from_env(merged: dict[str, str]) -> str:
    base = merged.get("OLLAMA_BASE_URL", "").strip() or DEFAULT_OLLAMA_V1
    base = base.rstrip("/")
    if base.endswith("/v1"):
        return base[: -len("/v1")]
    return base


def _score_ollama_model(name: str) -> tuple[int, int, str]:
    n = name.lower()
    if "embed" in n:
        return (-1, 0, name)
    qwen = 100 if "qwen" in n else 0
    m = re.search(r"(\d+)b", n)
    size = int(m.group(1)) if m else 0
    return (qwen, size, name)


def pick_best_ollama_model(models: list[str]) -> str | None:
    candidates = [m for m in models if _score_ollama_model(m)[0] >= 0]
    if not candidates:
        return models[0] if models else None
    return max(candidates, key=_score_ollama_model)


def discover_ollama(merged: dict[str, str]) -> dict:
    host = _ollama_host_from_env(merged)
    tags_url = f"{host}/api/tags"
    try:
        req = urllib.request.Request(tags_url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=3.0) as resp:
            data = json.loads(resp.read().decode())
        models = [m.get("name", "") for m in data.get("models", []) if m.get("name")]
        models = [m for m in models if m]
        chosen = merged.get("OLLAMA_MODEL", "").strip() or pick_best_ollama_model(models)
        v1 = merged.get("OLLAMA_BASE_URL", "").strip() or f"{host}/v1"
        return {
            "available": bool(models),
            "host": host,
            "base_url_v1": v1.rstrip("/"),
            "installed_models": models,
            "recommended_model": chosen,
            "note": "Free local leg — prefers qwen* tags, then largest *b model",
        }
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as e:
        return {
            "available": False,
            "host": host,
            "error": str(e),
            "installed_models": [],
            "recommended_model": merged.get("OLLAMA_MODEL", "").strip() or None,
        }


def _skip_local_slot() -> bool:
    return os.environ.get("SUPER_AUDIT_SKIP_LOCAL", "").strip().lower() in (
        "1",
        "true",
        "yes",
        "on",
    )


def _fusion_slot() -> dict:
    return {
        "label": "api-adversarial",
        "role": "api-adversarial",
        "base_url_env": "OPENROUTER_BASE_URL",
        "api_key_env": "OPENROUTER_API_KEY",
        "model": FUSION_MODEL,
        "extra": {"plugins": [{"id": "fusion"}]},
        "system": (
            "Super audit — adversarial readonly reviewer (OpenRouter Fusion panel). "
            "Follow required output format exactly."
        ),
        "provider": "openrouter",
    }


def _premium_slot(premium_model: str) -> dict:
    return {
        "label": "api-deep-reasoning",
        "role": "api-deep-reasoning",
        "base_url_env": "OPENROUTER_BASE_URL",
        "api_key_env": "OPENROUTER_API_KEY",
        "model_env": "OPENROUTER_PREMIUM_MODEL",
        "model": premium_model,
        "system": (
            "Super audit — deep reasoning readonly reviewer (OpenRouter premium). "
            "Follow required output format exactly."
        ),
        "provider": "openrouter",
    }


def _local_slot(*, label: str, role: str, model: str, kind: str) -> dict:
    if kind == "adversarial":
        system = (
            "Super audit — adversarial readonly reviewer (local Ollama, free). "
            "Be contrarian; stress-test deploy claims. Follow required output format exactly."
        )
    elif kind == "cross-check":
        system = (
            "Super audit — local cross-check readonly reviewer (Ollama, free). "
            "You are slot 6 — independent sanity check vs cloud auditors. "
            "Flag gaps Fusion/premium missed; do not repeat their consensus verbatim. "
            "Follow required output format exactly."
        )
    else:
        system = (
            "Super audit — deep reasoning readonly reviewer (local Ollama, free). "
            "Follow required output format exactly."
        )
    return {
        "label": label,
        "role": role,
        "base_url_env": "OLLAMA_BASE_URL",
        "api_key_env": "OLLAMA_API_KEY",  # pragma: allowlist secret
        "api_key_optional": True,
        "model_env": "OLLAMA_MODEL",
        "model": model,
        "local": True,
        "max_tokens": 8192,
        "system": system,
        "provider": "ollama",
    }


def recommend_auditors(discovery: dict) -> dict:
    """Default routing (operator may override via custom auditors.json):

    - OpenRouter + Ollama: 3 Cursor + Fusion + premium OR + local cross-check (6)
    - OpenRouter only:     3 Cursor + Fusion + premium OR (5)
    - Ollama only (no OR): 3 Cursor + 2× local (5) — fallback
    - Neither:             3 Cursor only — degraded
    """
    or_ready = discovery["keys"]["OPENROUTER_API_KEY"]["present"]
    ollama = discovery["ollama"]
    ollama_ready = ollama.get("available") and ollama.get("recommended_model")
    skip_local = _skip_local_slot()
    premium = discovery["default_premium_model"]
    local_model = ollama.get("recommended_model") or "qwen3.5:32b"

    slots: list[dict] = []
    tier = "degraded-cursor-only"
    auditor_count = 3

    if or_ready:
        slots = [_fusion_slot(), _premium_slot(premium)]
        auditor_count = 5
        tier = "default-5-model"
        if ollama_ready and not skip_local:
            slots.append(
                _local_slot(
                    label="api-local-cross-check",
                    role="api-local-cross-check",
                    model=local_model,
                    kind="cross-check",
                )
            )
            auditor_count = 6
            tier = "default-6-model"
    elif ollama_ready:
        slots = [
            _local_slot(
                label="api-local-adversarial",
                role="api-adversarial",
                model=local_model,
                kind="adversarial",
            ),
            _local_slot(
                label="api-local-reasoning",
                role="api-deep-reasoning",
                model=local_model,
                kind="reasoning",
            ),
        ]
        auditor_count = 5
        tier = "fallback-local-only"

    return {
        "slots": slots,
        "tier": tier,
        "auditor_count": auditor_count,
        "local_model": local_model if ollama_ready else None,
        "skip_local": skip_local,
    }


def _merged_routing() -> tuple[dict[str, str], list[str]]:
    """Build routing map from process env + optional CEMINI_LLM_ROUTING_ENV file."""
    merged: dict[str, str] = {}
    sources: list[str] = []
    routing = _routing_file_from_env()
    if routing is not None:
        chunk = _load_env_file(routing)
        if chunk:
            sources.append(str(routing))
            merged.update(chunk)
    for k in KEY_VARS + URL_VARS:
        val = os.environ.get(k, "").strip()
        if val:
            merged[k] = val
    return merged, sources


def discover(workspace: Path) -> dict:
    merged, sources = _merged_routing()
    merged.setdefault("OLLAMA_BASE_URL", DEFAULT_OLLAMA_V1)

    keys: dict[str, dict] = {}
    for k in KEY_VARS:
        val = merged.get(k, "").strip()
        keys[k] = {"present": bool(val), "masked": _mask(val) if val else None}

    urls = {k: merged.get(k) for k in URL_VARS if merged.get(k)}
    premium_model = merged.get("OPENROUTER_PREMIUM_MODEL", "").strip() or DEFAULT_PREMIUM_MODEL
    ollama = discover_ollama(merged)

    or_ready = keys["OPENROUTER_API_KEY"]["present"]
    ollama_ready = ollama.get("available") and bool(ollama.get("recommended_model"))
    api_leg_ready = or_ready or ollama_ready

    partial: dict = {
        "workspace": str(workspace.resolve()),
        "sources_loaded": sources,
        "keys": keys,
        "urls": urls,
        "ollama": ollama,
        "default_premium_model": premium_model,
    }
    rec = recommend_auditors(
        {**partial, "keys": keys, "default_premium_model": premium_model, "ollama": ollama}
    )

    if rec["tier"] == "default-6-model":
        lm = ollama.get("recommended_model", "local")
        coverage = f"default 6-model (3 Cursor + Fusion + OR premium + local `{lm}`)"
    elif rec["tier"] == "default-5-model":
        coverage = "default 5-model (3 Cursor + Fusion + OpenRouter premium) — no local Ollama"
    elif rec["tier"] == "fallback-local-only":
        lm = ollama.get("recommended_model", "local")
        coverage = (
            f"fallback 5-model (3 Cursor + 2× Ollama `{lm}`) — "
            "add OPENROUTER_API_KEY for default stack"
        )
    else:
        coverage = "degraded (3-model Cursor only) — need OpenRouter and/or Ollama"

    suggestions: list[dict] = []
    for slot in rec["slots"]:
        suggestions.append(
            {
                "role": slot.get("role", slot["label"]),
                "label": slot["label"],
                "model": slot.get("model"),
                "provider": slot.get("provider"),
                "note": "free" if slot.get("local") else "paid",
            }
        )

    return {
        **partial,
        "recommended_auditors": rec,
        "suggested_api_slots": suggestions,
        "api_leg_ready": api_leg_ready,
        "coverage": coverage,
        "tier": rec["tier"],
        "auditor_count": rec["auditor_count"],
        "setup_hint": (
            "Export OPENROUTER_API_KEY (and optionally set CEMINI_LLM_ROUTING_ENV to a "
            "routing file path), with Ollama running → 6 auditors. "
            "No Ollama → 5 auditors (3 Cursor + 2 OpenRouter). "
            "Set SUPER_AUDIT_SKIP_LOCAL=1 to force 5-model when Ollama is up."
        ),
        "note": (
            "Slots 1–3: Cursor. Slot 4: Fusion @ OR. Slot 5: premium @ OR. "
            "Slot 6 (default when Ollama up): local cross-check (qwen* auto-picked)."
        ),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--workspace", type=Path, default=Path.cwd())
    p.add_argument("--json", action="store_true")
    p.add_argument("--write-auditors", type=Path, help="Write recommended auditors.json")
    args = p.parse_args()

    result = discover(args.workspace)

    if args.write_auditors:
        slots = result["recommended_auditors"]["slots"]
        payload = {
            "slots": slots,
            "tier": result["tier"],
            "auditor_count": result["auditor_count"],
        }
        args.write_auditors.parent.mkdir(parents=True, exist_ok=True)
        args.write_auditors.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {args.write_auditors} ({len(slots)} slots, tier={result['tier']})")

    if args.json:
        print(json.dumps(result, indent=2))
        return 0 if result["api_leg_ready"] else 1

    print(f"workspace: {result['workspace']}")
    if result["sources_loaded"]:
        print("sources:")
        for s in result["sources_loaded"]:
            print(f"  - {s}")

    print("\nkeys:")
    for k, info in result["keys"].items():
        status = info["masked"] if info["present"] else "missing"
        mark = "  ← premium API leg" if k == "OPENROUTER_API_KEY" else ""
        print(f"  {k}: {status}{mark}")

    ollama = result["ollama"]
    print("\nollama (free local leg):")
    if ollama.get("available"):
        print(f"  status: running @ {ollama.get('host')}")
        print(f"  recommended: {ollama.get('recommended_model')}")
        if ollama.get("installed_models"):
            print(f"  installed: {', '.join(ollama['installed_models'][:8])}")
    else:
        print(f"  status: not reachable ({ollama.get('error', 'unknown')})")
        print("  tip: ollama serve && ollama pull qwen3.5:32b")

    print(f"\ntier: {result['tier']} · auditors: {result.get('auditor_count', 3)}")
    print(f"coverage: {result['coverage']}")

    print("\nrecommended API slots:")
    for s in result["suggested_api_slots"]:
        note = s.get("note", "")
        print(f"  - {s['label']}: {s['model']} [{s.get('provider')}]{' (' + note + ')' if note else ''}")

    print(f"\napi_leg_ready: {result['api_leg_ready']}")
    if not result["api_leg_ready"]:
        print(f"\nACTION: {result['setup_hint']}")
    return 0 if result["api_leg_ready"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
