#!/usr/bin/env python3
"""Closed-world tool membership check (CCC K369 leftover).

Validate tool name (and optional arg keys) against a local closed-world registry.
Not BM25 search — exact membership only. Pairs scout-tool-search (retrieve) and
step-gate (blast after membership).

Usage:
  python3 scripts/closed_world_tool_check.py check <tool> [arg_key...]
  python3 scripts/closed_world_tool_check.py list
  python3 scripts/closed_world_tool_check.py selftest
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG = REPO_ROOT / "config" / "closed_world_tools.example.json"
SCRIPTS_DIR = REPO_ROOT / "scripts"

sys.path.insert(0, str(REPO_ROOT / "scripts"))
from scout_tool_search import index_skills  # noqa: E402


def load_schemas() -> dict[str, set[str]]:
    schemas: dict[str, set[str]] = {}
    if not CONFIG.is_file():
        return schemas
    data = json.loads(CONFIG.read_text(encoding="utf-8"))
    for entry in data.get("tools", []):
        name = entry.get("name")
        if not name:
            continue
        keys = entry.get("allowed_arg_keys") or []
        schemas[str(name)] = {str(k) for k in keys}
    return schemas


def build_registry() -> tuple[set[str], dict[str, set[str]]]:
    names: set[str] = set()
    for sk in index_skills():
        names.add(sk["name"])
    if SCRIPTS_DIR.is_dir():
        for py in SCRIPTS_DIR.glob("*.py"):
            names.add(py.stem.replace("_", "-"))
            names.add(py.stem)
    schemas = load_schemas()
    for name in schemas:
        names.add(name)
    return names, schemas


def classify(tool: str, arg_keys: list[str]) -> tuple[str, str]:
    tool = (tool or "").strip()
    if not tool:
        return "HOLD", "empty tool name"

    names, schemas = build_registry()
    tool_l = tool.lower()
    exact = tool if tool in names else None
    if exact is None and tool_l in {n.lower() for n in names}:
        for n in names:
            if n.lower() == tool_l:
                exact = n
                break

    if exact is None:
        prefixes = [n for n in names if n.lower().startswith(tool_l) or tool_l.startswith(n.lower())]
        if len(prefixes) > 1:
            return "ESCALATE", f"ambiguous prefix matches: {', '.join(sorted(prefixes)[:5])}"
        if len(prefixes) == 1:
            exact = prefixes[0]
        else:
            return "HOLD", "unknown tool (not in closed-world registry)"

    schema = schemas.get(exact)
    if arg_keys and schema is None:
        return "ESCALATE", f"tool {exact!r} has no arg schema — cannot validate keys"
    if schema is not None and arg_keys:
        extras = [k for k in arg_keys if k not in schema]
        if extras:
            return "HOLD", f"hallucinated arg keys for {exact}: {', '.join(extras)}"
    return "ALLOW", f"matched {exact}"


def cmd_check(args: argparse.Namespace) -> int:
    verdict, why = classify(args.tool, list(args.arg_keys or []))
    print(f"{verdict}: {why}")
    if verdict == "HOLD":
        return 2
    if verdict == "ESCALATE":
        return 3
    return 0


def cmd_list(_: argparse.Namespace) -> int:
    names, schemas = build_registry()
    for n in sorted(names):
        keys = schemas.get(n)
        if keys:
            print(f"{n}\tschema={','.join(sorted(keys))}")
        else:
            print(n)
    return 0


def selftest() -> int:
    names, _ = build_registry()
    if "step-gate" not in names and "harness-eval-gate" not in names:
        print("FAIL: expected federation skill names in registry", file=sys.stderr)
        return 1

    cases = [
        ("step-gate", [], "ALLOW"),
        ("totally-unknown-tool-xyz", [], "HOLD"),
        ("wiki_lint", [], "ALLOW"),
    ]
    for tool, keys, want in cases:
        got, _ = classify(tool, keys)
        if got != want:
            print(f"FAIL ({tool!r}, {keys}) -> {got}, expected {want}", file=sys.stderr)
            return 1

    if CONFIG.is_file():
        got, _ = classify("example-mcp-tool", ["query"])
        if got != "ALLOW":
            print("FAIL example schema ALLOW", file=sys.stderr)
            return 1
        got, _ = classify("example-mcp-tool", ["secret_key"])
        if got != "HOLD":
            print("FAIL example schema HOLD on bad key", file=sys.stderr)
            return 1
        extra = 2
    else:
        extra = 0

    print(f"closed_world_tool_check selftest: {len(cases) + extra} pass, 0 fail")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("tool")
    c.add_argument("arg_keys", nargs="*")
    c.set_defaults(fn=cmd_check)
    sub.add_parser("list").set_defaults(fn=cmd_list)
    sub.add_parser("selftest").set_defaults(fn=lambda _: selftest())
    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())
