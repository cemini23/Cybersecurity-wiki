#!/usr/bin/env python3
"""Pick ≥2 live free OpenRouter models, excluding DeepSeek and Grok/x-ai.

Usage:
  python3 select_free_or_models.py
  python3 select_free_or_models.py --count 3 --json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from _env import env, load_routing_env  # noqa: E402

EXCLUDE_RE = re.compile(r"(?i)deepseek|grok|x-ai/")
MODALITY_EXCLUDE_RE = re.compile(
    r"(?i)lyria|whisper|tts|embed|embedding|image|vision-only|audio|"
    r"diffusion|flux|stable-diffusion|moderation|content-safety"
)
PREFER_RE = re.compile(
    r"(?i)coder|instruct|chat|nemotron|qwen|llama|gemma|gpt-oss|"
    r"kimi|glm|laguna|north|ling"
)


def _family(model_id: str) -> str:
    mid = model_id.lower().split(":")[0]
    prefix = mid.split("/")[0] if "/" in mid else mid
    aliases = {
        "openai": "openai",
        "nvidia": "nvidia",
        "google": "google",
        "cohere": "cohere",
        "poolside": "poolside",
        "inclusionai": "inclusionai",
        "meta-llama": "meta",
        "meta": "meta",
        "qwen": "qwen",
        "moonshotai": "moonshot",
        "z-ai": "zhipu",
        "openrouter": "openrouter",
    }
    return aliases.get(prefix, prefix)


def _is_free(model: dict) -> bool:
    mid = str(model.get("id") or "")
    if mid.endswith(":free"):
        return True
    pricing = model.get("pricing") or {}
    try:
        pin = float(pricing.get("prompt") or 1)
        pout = float(pricing.get("completion") or 1)
    except (TypeError, ValueError):
        return False
    return pin == 0.0 and pout == 0.0


def fetch_models(base_url: str, api_key: str) -> list[dict]:
    url = base_url.rstrip("/") + "/models"
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return list(data.get("data") or [])


def rank_candidates(models: list[dict]) -> list[dict]:
    out: list[dict] = []
    for m in models:
        mid = str(m.get("id") or "")
        if not mid or not _is_free(m):
            continue
        if EXCLUDE_RE.search(mid):
            continue
        name = str(m.get("name") or "")
        if MODALITY_EXCLUDE_RE.search(mid) or MODALITY_EXCLUDE_RE.search(name):
            continue
        arch = m.get("architecture") or {}
        modality = str(arch.get("modality") or "text")
        if modality and "text" not in modality.lower():
            continue
        try:
            ctx = int(m.get("context_length") or 0)
        except (TypeError, ValueError):
            ctx = 0
        boost = 1 if PREFER_RE.search(mid) else 0
        out.append(
            {
                "id": mid,
                "name": name,
                "context_length": ctx,
                "family": _family(mid),
                "boost": boost,
            }
        )
    out.sort(key=lambda x: (-x["boost"], -x["context_length"], x["id"]))
    return out


def pick_diverse(candidates: list[dict], count: int) -> list[dict]:
    picked: list[dict] = []
    used_families: set[str] = set()
    # Pass 1: distinct families
    for c in candidates:
        if len(picked) >= count:
            break
        fam = c["family"]
        if fam in used_families or fam == "openrouter":
            continue
        picked.append(c)
        used_families.add(fam)
    # Pass 2: fill remaining even if family repeats
    for c in candidates:
        if len(picked) >= count:
            break
        if any(p["id"] == c["id"] for p in picked):
            continue
        picked.append(c)
    if len(picked) < count:
        # degraded: router
        if not any(p["id"] == "openrouter/free" for p in picked):
            picked.append(
                {
                    "id": "openrouter/free",
                    "name": "Free Models Router",
                    "context_length": 0,
                    "family": "openrouter",
                    "boost": 0,
                }
            )
    return picked[:count]


def main() -> int:
    ap = argparse.ArgumentParser(description="Select free OpenRouter models (no DS/Grok)")
    ap.add_argument("--count", type=int, default=2, help="How many models (min 2)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--refresh", action="store_true", help="Ignored (no cache); reserved")
    args = ap.parse_args()
    count = max(2, args.count)

    load_routing_env()
    key = env("OPENROUTER_API_KEY")
    if not key:
        print("OPENROUTER_API_KEY not set (shell or CEMINI_LLM_ROUTING_ENV)", file=sys.stderr)
        return 1
    base = env("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

    try:
        models = fetch_models(base, key)
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError) as e:
        print(f"Failed to list OpenRouter models: {e}", file=sys.stderr)
        return 1

    candidates = rank_candidates(models)
    picked = pick_diverse(candidates, count)
    result = {
        "count": len(picked),
        "requested": count,
        "models": picked,
        "candidate_pool": len(candidates),
        "excluded": "deepseek, grok, x-ai",
        "degraded": any(p["id"] == "openrouter/free" for p in picked) or len(picked) < count,
    }
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for p in picked:
            print(p["id"])
    return 0 if picked else 1


if __name__ == "__main__":
    raise SystemExit(main())
