#!/usr/bin/env python3
"""Select free OR models + write Grok handoff for free-audit.

Usage:
  python3 prepare_free_audit.py \\
    --pack reports/audit/pack-free-foo \\
    --out reports/audit/free-foo \\
    --mode code-debug \\
    --workspace "$(pwd)"
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))
from _env import env, load_routing_env  # noqa: E402
from select_free_or_models import fetch_models, pick_diverse, rank_candidates  # noqa: E402


HANDOFF_TEMPLATE = """# Free audit — Grok handoff (readonly orchestration)

You are **auditor #1 and orchestrator** for a Cemini **free-audit**.

**Mode:** `{mode}`
**Workspace:** `{workspace}`
**Pack:** `{pack}`
**Out dir:** `{out}`

## Hard rules

- Readonly — do **not** edit product code or configs. Write only under `{out}`.
- **No secrets** in prompts or reports (no `.env`, tokens, keys).
- Always-approve / skip-permissions is intentional for this readonly run.
- Free OpenRouter models may log prompts — keep the pack free of credentials.

## Pre-selected free OpenRouter models (≥2, excludes DeepSeek/Grok)

{free_models_block}

## Your steps (do in order)

### 1) Your auditor report

Read `{pack}/PACK_INDEX.md` and `{pack}/audit_prompt.md` (and listed artifacts).
Write your own audit to:

`{out}/auditor-grok.md`

Use the required output format from the audit prompt (Verdict / Findings / Root cause / Confidence / Unique angle).
Lens for this mode: see skill `reference.md` (Grok column).

### 2) Non-Grok legs (claude-ds + free OR)

Run from the workspace:

```bash
python3 "{skill_scripts}/run_non_grok_legs.py" \\
  --pack "{pack}" \\
  --out "{out}" \\
  --models-json "{out}/free_models.json" \\
  --mode "{mode}"
```

This writes `auditor-claude-ds.md` (DeepSeek V4 Flash / claude-ds slot) and `auditor-or-*.md` for each free model.

If DeepSeek key is missing, note it in SYNTHESIS and continue with free OR + your report.

### 3) Synthesize

Write Glasswing rollup to:

`{out}/SYNTHESIS.md`

Use this structure:

```markdown
# Free audit — {title}

**Mode:** {mode} · **Auditors:** Grok + claude-ds + free OR
**Pack:** `{pack}` · **Out:** `{out}`

| Slot | Channel | Model | Verdict |
|------|---------|-------|---------|
| 1 | grok | grok-cli | … |
| 2 | claude-ds | deepseek-v4-flash | … |
| 3 | openrouter-free | … | … |
| 4 | openrouter-free | … | … |

## Consensus (≥2 auditors agree)
## Unique
## Conflicts (Glasswing — do not silently pick)
## Recommended fix order
## Verdict rollup
**Overall:** SHIP | SHIP-WITH-FIXES | REWORK | REJECT — one paragraph
```

### 4) Stop

When `SYNTHESIS.md` exists, you are done. Do not implement fixes unless the handoff explicitly says so (default: report only).

## Skill docs (optional)

- `{skill_root}/SKILL.md`
- `{skill_root}/reference.md`
"""


def main() -> int:
    ap = argparse.ArgumentParser(description="Prepare free-audit Grok handoff")
    ap.add_argument("--pack", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--mode", default="code-debug")
    ap.add_argument("--workspace", type=Path, default=Path.cwd())
    ap.add_argument("--count", type=int, default=2)
    ap.add_argument("--title", default="")
    args = ap.parse_args()

    load_routing_env()
    pack = args.pack.resolve()
    out = args.out.resolve()
    workspace = args.workspace.resolve()
    out.mkdir(parents=True, exist_ok=True)

    if not (pack / "audit_prompt.md").is_file():
        print(f"Missing pack audit_prompt.md under {pack}", file=sys.stderr)
        return 1

    or_key = env("OPENROUTER_API_KEY")
    if not or_key:
        print("OPENROUTER_API_KEY not set — free OR legs will fail", file=sys.stderr)
        return 1
    base = env("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    try:
        ranked = rank_candidates(fetch_models(base, or_key))
        picked = pick_diverse(ranked, max(2, args.count))
    except Exception as e:
        print(f"Model select failed: {e}", file=sys.stderr)
        return 1

    models_path = out / "free_models.json"
    models_payload = {
        "picked_at": datetime.now(timezone.utc).isoformat(),
        "count": len(picked),
        "models": picked,
        "excluded": "deepseek, grok, x-ai",
    }
    models_path.write_text(json.dumps(models_payload, indent=2) + "\n", encoding="utf-8")

    free_block = "\n".join(
        f"- `{m['id']}` (family={m.get('family')}, ctx={m.get('context_length')})"
        for m in picked
    )
    title = args.title or pack.name.replace("pack-free-", "").replace("pack-", "")
    handoff = HANDOFF_TEMPLATE.format(
        mode=args.mode,
        workspace=workspace,
        pack=pack,
        out=out,
        free_models_block=free_block,
        skill_scripts=SCRIPT_DIR,
        skill_root=SKILL_ROOT,
        title=title,
    )
    handoff_path = out / "GROK_HANDOFF.md"
    handoff_path.write_text(handoff, encoding="utf-8")

    kit = Path.home() / "Desktop/projects/tipdrop-workspace-kit/scripts/handoff-to-grok.ps1"
    if kit.is_file():
        cmd = (
            f'pwsh -File "{kit}" -PromptFile "{handoff_path}" -WorkDir "{workspace}"'
        )
    else:
        cmd = f'grok --cwd "{workspace}" --always-approve "$(cat "{handoff_path}")"'

    meta = {
        "mode": args.mode,
        "pack": str(pack),
        "out": str(out),
        "handoff": str(handoff_path),
        "free_models": [m["id"] for m in picked],
        "next_command": cmd,
    }
    (out / "prepare_meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(meta, indent=2))
    print("\n# Next: run handoff to Grok\n" + cmd)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
