#!/usr/bin/env python3
"""Run API leg of super-audit (slots 4–5) via OpenAI-compatible endpoints.

Usage:
  python3 discover_api_keys.py
  python3 build_audit_pack.py --prompt ... --out reports/audit/pack-foo
  python3 run_api_auditors.py --pack reports/audit/pack-foo --out reports/audit/premium-foo
  python3 run_api_auditors.py --pack ... --auditors path/to/auditors.json --dry-run
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_ROOT = SCRIPT_DIR.parent

DEFAULT_AUDITORS = SKILL_ROOT / "auditors.default.json"

# When slot.base_url_env is unset in the process env, use these hosts.
# Without this map, DEEPSEEK_BASE_URL / ADVISOR_BASE_URL fall through to
# OpenRouter and DeepSeek keys get sent to the wrong API (silent misroute).
BASE_URL_DEFAULTS: dict[str, str] = {
    "OPENROUTER_BASE_URL": "https://openrouter.ai/api/v1",
    "OLLAMA_BASE_URL": "http://localhost:11434/v1",
    "DEEPSEEK_BASE_URL": "https://api.deepseek.com/v1",
    "ADVISOR_BASE_URL": "https://openrouter.ai/api/v1",
}

REQUIRED_SLOT_KEYS = ("label", "model")


def _load_env(_workspace: Path) -> None:
    """Hydrate process env from optional CEMINI_LLM_ROUTING_ENV path only.

    Operator should export provider keys in the shell, or point
    CEMINI_LLM_ROUTING_ENV at a local routing file. This skill does not
    scan project dotenv trees.
    """
    custom = os.environ.get("CEMINI_LLM_ROUTING_ENV", "").strip()
    if custom:
        p = Path(custom).expanduser()
        if p.is_file():
            for line in p.read_text().splitlines():
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, _, v = line.partition("=")
                k, v = k.strip(), v.strip().strip('"').strip("'")
                if k and k not in os.environ:
                    os.environ[k] = v

    os.environ.setdefault("OLLAMA_BASE_URL", "http://localhost:11434/v1")


def _resolve_env(name: str, default: str = "") -> str:
    return os.environ.get(name, default).strip()


def _bearer_for_slot(slot: dict) -> str:
    """Resolve outbound Authorization token for one auditor slot (no env mutation)."""
    key_env = slot.get("api_key_env", "OPENROUTER_API_KEY")
    token = _resolve_env(key_env) if key_env else ""
    if token:
        return token
    # Advisor slots may reuse OpenRouter when ADVISOR_* is unset (read-only fallback).
    if key_env == "ADVISOR_API_KEY":
        return _resolve_env("OPENROUTER_API_KEY")
    return ""


def _call_openai_compat(
    *,
    base_url: str,
    api_key: str,
    model: str,
    prompt: str,
    system: str,
    extra: dict | None = None,
    max_tokens: int = 16_000,
) -> str:
    import httpx

    url = base_url.rstrip("/") + "/chat/completions"
    body: dict = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.2,
        "max_tokens": max_tokens,
    }
    if extra:
        body.update(extra)
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    elif "11434" not in base_url and "localhost" not in base_url:
        headers["Authorization"] = "Bearer "
    if "openrouter.ai" in base_url:
        headers["HTTP-Referer"] = _resolve_env(
            "OPENROUTER_HTTP_REFERER", "https://github.com/cemini23"
        )
        headers["X-Title"] = _resolve_env("OPENROUTER_APP_TITLE", "super-audit")
    r = httpx.post(url, headers=headers, json=body, timeout=600.0)
    r.raise_for_status()
    return (r.json()["choices"][0]["message"]["content"] or "").strip()


def _default_base_url(base_env: str, slot: dict) -> str:
    if slot.get("local") or base_env == "OLLAMA_BASE_URL":
        return BASE_URL_DEFAULTS["OLLAMA_BASE_URL"]
    if base_env in BASE_URL_DEFAULTS:
        return BASE_URL_DEFAULTS[base_env]
    # Unknown env name — prefer OpenRouter only for OPENROUTER_* keys
    if base_env.startswith("OPENROUTER"):
        return BASE_URL_DEFAULTS["OPENROUTER_BASE_URL"]
    if base_env.startswith("DEEPSEEK"):
        return BASE_URL_DEFAULTS["DEEPSEEK_BASE_URL"]
    return BASE_URL_DEFAULTS["OPENROUTER_BASE_URL"]


def _validate_slots(slots: list[dict], *, source: str) -> list[dict]:
    if not isinstance(slots, list):
        raise ValueError(f"{source}: auditors file must have a 'slots' array")
    out: list[dict] = []
    for i, slot in enumerate(slots):
        if not isinstance(slot, dict):
            raise ValueError(f"{source}: slots[{i}] must be an object")
        missing = [k for k in REQUIRED_SLOT_KEYS if not str(slot.get(k, "")).strip()]
        # model may be supplied only via model_env if model is present as fallback —
        # require at least one of model / model_env
        if "model" in missing and str(slot.get("model_env", "")).strip():
            missing = [k for k in missing if k != "model"]
        if missing:
            raise ValueError(
                f"{source}: slots[{i}] missing required field(s) {missing} "
                f"(label={slot.get('label')!r}). "
                "Expected shape: {\"slots\":[{\"label\",\"model\", ...}]}"
            )
        out.append(slot)
    return out


def _load_auditors(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        slots = data
    elif isinstance(data, dict):
        slots = data.get("slots")
        if slots is None:
            # Common agent mistake: a single slot object as the file root
            if "label" in data and ("model" in data or "model_env" in data):
                raise ValueError(
                    f"{path}: root is a single slot object — wrap it as "
                    '{"slots":[ ... ]}'
                )
            raise ValueError(f"{path}: auditors file must have a 'slots' array")
        if slots == []:
            return []
    else:
        raise ValueError(f"{path}: auditors file must be a JSON object or array")
    return _validate_slots(slots, source=str(path))


def main() -> int:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--pack", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--auditors", type=Path, default=None)
    ap.add_argument(
        "--discover",
        action="store_true",
        help="Build auditors.json from discover_api_keys (OpenRouter + Ollama)",
    )
    ap.add_argument("--workspace", type=Path, default=Path.cwd())
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--slot", default="", help="Run single label only")
    args = ap.parse_args()

    workspace = args.workspace.resolve()
    _load_env(workspace)

    pack = args.pack.resolve()
    prompt_path = pack / "audit_prompt.md"
    if not prompt_path.is_file():
        print(f"Missing {prompt_path} — run build_audit_pack.py first", file=sys.stderr)
        return 1

    base_prompt = prompt_path.read_text(encoding="utf-8")
    out_dir = args.out.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")

    tier = ""
    if args.discover or args.auditors is None:
        sys.path.insert(0, str(SCRIPT_DIR))
        from discover_api_keys import discover, recommend_auditors  # noqa: E402

        disc = discover(workspace)
        rec = recommend_auditors(disc)
        slots = _validate_slots(rec["slots"], source="discover")
        tier = rec["tier"]
        auditors_path = out_dir / f"auditors_{ts}.json"
        auditors_path.write_text(
            json.dumps(
                {"slots": slots, "tier": tier, "auditor_count": rec["auditor_count"]},
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        print(f"Discovered tier={tier} → {auditors_path}")
        if not slots:
            if DEFAULT_AUDITORS.is_file():
                print(
                    f"No discovered API slots — falling back to {DEFAULT_AUDITORS}",
                    file=sys.stderr,
                )
                slots = _load_auditors(DEFAULT_AUDITORS)
                auditors_path = DEFAULT_AUDITORS
                tier = tier or "default-file"
            else:
                print(
                    "No API slots available (need OpenRouter key or running Ollama)",
                    file=sys.stderr,
                )
                return 1
    else:
        auditors_path = args.auditors.resolve()
        if not auditors_path.is_file():
            print(f"Missing auditors config: {auditors_path}", file=sys.stderr)
            return 1
        try:
            slots = _load_auditors(auditors_path)
        except (ValueError, json.JSONDecodeError) as e:
            print(f"auditors.json schema error: {e}", file=sys.stderr)
            return 1
    if args.slot:
        slots = [s for s in slots if s.get("label") == args.slot]
        if not slots:
            print(f"No slot label {args.slot!r}", file=sys.stderr)
            return 1

    if args.dry_run:
        print(f"Prompt {len(base_prompt)} chars → {out_dir}")
        print(f"Slots: {[s.get('label') for s in slots]}")
        for s in slots:
            be = s.get("base_url_env", "OPENROUTER_BASE_URL")
            print(
                f"  {s.get('label')}: model={s.get('model')} "
                f"base={_resolve_env(be, _default_base_url(be, s))}"
            )
        return 0

    written: dict[str, Path] = {}
    errors: list[str] = []

    for slot in slots:
        label = slot.get("label") or "api-auditor"
        key_env = slot.get("api_key_env", "OPENROUTER_API_KEY")
        base_env = slot.get("base_url_env", "OPENROUTER_BASE_URL")
        api_key_optional = bool(slot.get("api_key_optional"))
        model_env = slot.get("model_env", "").strip()
        model_fallback = str(slot.get("model", "")).strip()
        model = _resolve_env(model_env, model_fallback) if model_env else model_fallback
        if not model:
            msg = f"{label}: empty model (set model or model_env)"
            errors.append(msg)
            err_path = out_dir / f"{label}_{ts}_SKIPPED.txt"
            err_path.write_text(msg + "\n", encoding="utf-8")
            written[label] = err_path
            print(f"  SKIP {msg}", file=sys.stderr)
            continue
        api_key = _bearer_for_slot(slot)
        if base_env == "ADVISOR_BASE_URL" and not _resolve_env(base_env):
            # Prefer OpenRouter when ADVISOR_* unset but OR key present
            if _resolve_env("OPENROUTER_API_KEY"):
                base_env = "OPENROUTER_BASE_URL"
            elif _resolve_env("DEEPSEEK_API_KEY"):
                base_env = "DEEPSEEK_BASE_URL"
        base_url = _resolve_env(base_env, _default_base_url(base_env, slot))
        max_tokens = int(slot.get("max_tokens", 16_000))
        system = slot.get(
            "system",
            "Super audit — expert readonly reviewer. Follow required output format exactly.",
        )
        extra = slot.get("extra")
        if model == "openrouter/fusion" and not extra:
            extra = {"plugins": [{"id": "fusion"}]}

        if not api_key and not api_key_optional:
            msg = f"{label}: missing {key_env}"
            errors.append(msg)
            err_path = out_dir / f"{label}_{ts}_SKIPPED.txt"
            err_path.write_text(msg + "\n", encoding="utf-8")
            written[label] = err_path
            print(f"  SKIP {msg}", file=sys.stderr)
            continue

        prompt = base_prompt.replace("{{MODEL_SLOT}}", label)
        provider = slot.get("provider", "api")
        models_to_try = [model]
        fb = str(slot.get("fallback_model", "")).strip()
        if fb and fb not in models_to_try:
            models_to_try.append(fb)

        last_err: Exception | None = None
        ok = False
        for attempt_model in models_to_try:
            if attempt_model == "openrouter/fusion":
                attempt_extra = extra or {"plugins": [{"id": "fusion"}]}
            elif attempt_model == model:
                attempt_extra = extra
            else:
                # Do not reuse fusion plugins when retrying a different model
                attempt_extra = None
            print(f"Calling {label} ({attempt_model}) via {provider} @ {base_url}...")
            try:
                text = _call_openai_compat(
                    base_url=base_url,
                    api_key=api_key,
                    model=attempt_model,
                    prompt=prompt,
                    system=system,
                    extra=attempt_extra,
                    max_tokens=max_tokens,
                )
                out_path = out_dir / f"{label}_{ts}.md"
                out_path.write_text(text, encoding="utf-8")
                written[label] = out_path
                print(f"  OK {len(text)} chars → {out_path.name}")
                ok = True
                break
            except Exception as e:
                last_err = e
                print(f"  FAIL {attempt_model}: {e}", file=sys.stderr)
                if attempt_model != models_to_try[-1]:
                    print(
                        f"  retry with fallback_model={models_to_try[-1]!r}...",
                        file=sys.stderr,
                    )
        if not ok and last_err is not None:
            err_path = out_dir / f"{label}_{ts}_ERROR.txt"
            err_path.write_text(str(last_err), encoding="utf-8")
            written[label] = err_path
            errors.append(f"{label}: {last_err}")

    meta = {
        "timestamp": ts,
        "pack": str(pack),
        "auditors_file": str(auditors_path),
        "tier": tier or None,
        "models": list(written.keys()),
        "errors": errors,
    }
    (out_dir / f"meta_{ts}.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(meta, indent=2))

    ok = sum(1 for p in written.values() if p.suffix == ".md")
    return 0 if ok > 0 and not errors else (1 if not ok else 0)


if __name__ == "__main__":
    raise SystemExit(main())
