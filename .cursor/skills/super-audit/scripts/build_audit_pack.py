#!/usr/bin/env python3
"""Build a generic super-audit pack from a tailored prompt + artifacts.

Usage:
  python3 build_audit_pack.py \\
    --prompt prompts/my_super_audit.md \\
    --out reports/audit/pack-my-audit \\
    --artifact path/to/file.json:alias.json \\
    --read-order alias.json,other.md

Replaces {pack_index} in prompt with generated PACK_INDEX.md content.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MAX_CHARS = 20_000


def _read_tail(path: Path, max_chars: int) -> str:
    if not path.is_file():
        return f"(missing: {path})"
    text = path.read_text(encoding="utf-8", errors="replace")
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + f"\n\n… truncated {len(text) - max_chars} chars …"


def main() -> int:
    p = argparse.ArgumentParser(description="Build super-audit pack")
    p.add_argument("--prompt", type=Path, required=True, help="Tailored audit prompt markdown")
    p.add_argument("--out", type=Path, required=True, help="Output pack directory")
    p.add_argument(
        "--artifact",
        action="append",
        default=[],
        help="source_path[:dest_name] — copy or snapshot into pack",
    )
    p.add_argument(
        "--cmd",
        action="append",
        default=[],
        help="DISABLED for security — pre-capture output to a file and pass --artifact instead",
    )
    p.add_argument("--read-order", default="", help="Comma-separated dest names for index order")
    p.add_argument("--workspace", type=Path, default=Path.cwd())
    p.add_argument("--max-chars", type=int, default=DEFAULT_MAX_CHARS)
    p.add_argument("--code-path", action="append", default=[], help="Absolute paths listed in index")
    p.add_argument("--brief-path", action="append", default=[], help="Brief paths listed in index")
    args = p.parse_args()

    prompt_path = args.prompt.resolve()
    if not prompt_path.is_file():
        print(f"Missing prompt: {prompt_path}", file=sys.stderr)
        return 1

    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    workspace = args.workspace.resolve()

    artifacts: dict[str, str] = {}

    for spec in args.artifact:
        if ":" in spec:
            src_s, dest = spec.split(":", 1)
        else:
            src_s, dest = spec, Path(spec).name
        src = Path(src_s)
        if not src.is_absolute():
            candidate = (workspace / src).resolve()
            if candidate.is_file():
                src = candidate
            else:
                alt = Path(src_s).resolve()
                src = alt if alt.is_file() else candidate
        body = _read_tail(src, args.max_chars)
        (out / dest).write_text(body, encoding="utf-8")
        artifacts[dest] = str(out / dest)

    if args.cmd:
        print(
            "--cmd is disabled (no in-pack shell capture). "
            "Run the command yourself, save stdout to a file, then pass --artifact.",
            file=sys.stderr,
        )
        return 1

    read_order = [x.strip() for x in args.read_order.split(",") if x.strip()]
    if not read_order:
        read_order = list(artifacts.keys())

    index_lines = [
        f"# Super-audit pack — built {ts}",
        "",
        f"Workspace: `{workspace}`",
        f"Prompt source: `{prompt_path}`",
        "",
        "## Read order",
        "",
    ]
    for name in read_order:
        path = out / name
        if path.is_file():
            index_lines.append(f"- `{path}`")
    for name, path in artifacts.items():
        if name not in read_order:
            index_lines.append(f"- `{path}` (extra)")

    if args.code_path:
        index_lines.extend(["", "## Code paths (absolute)", ""])
        for cp in args.code_path:
            index_lines.append(f"- `{Path(cp).resolve()}`")

    if args.brief_path:
        index_lines.extend(["", "## Briefs", ""])
        for bp in args.brief_path:
            index_lines.append(f"- `{Path(bp).resolve()}`")

    index_path = out / "PACK_INDEX.md"
    index_path.write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    template = prompt_path.read_text(encoding="utf-8")
    audit_prompt = template.replace("{pack_index}", index_path.read_text(encoding="utf-8"))
    if "{{MODEL_SLOT}}" not in audit_prompt:
        audit_prompt = audit_prompt.replace("{{MODEL_SLOT}}", "{{MODEL_SLOT}}")  # no-op guard

    prompt_out = out / "audit_prompt.md"
    prompt_out.write_text(audit_prompt, encoding="utf-8")

    meta = {
        "built": ts,
        "out": str(out),
        "prompt_source": str(prompt_path),
        "prompt_chars": len(audit_prompt),
        "artifacts": list(artifacts.keys()),
        "read_order": read_order,
    }
    (out / "meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(meta, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
