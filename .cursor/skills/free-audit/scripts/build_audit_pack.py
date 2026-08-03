#!/usr/bin/env python3
"""Build a free-audit pack from a tailored prompt + artifacts.

Usage:
  python3 build_audit_pack.py \\
    --prompt reports/audit/free-foo/prompt.md \\
    --out reports/audit/pack-free-foo \\
    --artifact path/to/file.json:alias.json
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_MAX_CHARS = 20_000


def _read_tail(path: Path, max_chars: int) -> str:
    """Read artifact; if over max_chars keep head + tail so mid-file heuristics survive."""
    if not path.is_file():
        return f"(missing: {path})"
    text = path.read_text(encoding="utf-8", errors="replace")
    if len(text) <= max_chars:
        return text
    # Head+tail split: packs previously starved mid-file extractors
    # (e.g. GuruWatcher propose_from_text) when only the file head was kept.
    mark = (
        f"\n\n… truncated middle ({len(text) - max_chars} chars omitted; "
        f"head+tail kept) …\n\n"
    )
    budget = max_chars - len(mark)
    if budget < 2_000:
        return text[:max_chars] + f"\n\n… truncated {len(text) - max_chars} chars …"
    head_n = budget // 2
    tail_n = budget - head_n
    return text[:head_n] + mark + text[-tail_n:]


def main() -> int:
    p = argparse.ArgumentParser(description="Build free-audit pack")
    p.add_argument("--prompt", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--artifact", action="append", default=[])
    p.add_argument("--read-order", default="")
    p.add_argument("--workspace", type=Path, default=Path.cwd())
    p.add_argument("--max-chars", type=int, default=DEFAULT_MAX_CHARS)
    p.add_argument("--code-path", action="append", default=[])
    p.add_argument("--brief-path", action="append", default=[])
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
            src = candidate if candidate.is_file() else Path(src_s).resolve()
        body = _read_tail(src, args.max_chars)
        (out / dest).write_text(body, encoding="utf-8")
        artifacts[dest] = str(out / dest)

    read_order = [x.strip() for x in args.read_order.split(",") if x.strip()]
    if not read_order:
        read_order = list(artifacts.keys())

    index_lines = [
        f"# Free-audit pack — built {ts}",
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
    prompt_out = out / "audit_prompt.md"
    prompt_out.write_text(audit_prompt, encoding="utf-8")

    meta = {
        "built": ts,
        "skill": "free-audit",
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
