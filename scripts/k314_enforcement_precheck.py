#!/usr/bin/env python3
"""K314 advisory precheck — recognition ≠ enforcement (external reference monitor).

Operator-invoked checklist before high-blast MCP/tool exposure. Not a hook;
does not block. Pairs K303 deny/hooks + K285 Mandato + K307 step gate.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("external_pep", "Tool execution gated outside the shared LLM context (PEP / proxy)?"),
    ("authenticated_routing", "Instruction sources authenticated (HMAC/signed routing)?"),
    ("capability_gated", "Tools capability-gated (scoped tokens / deny-by-default)?"),
    ("no_model_arbitration_only", "Policy does NOT rely on model self-arbitration alone?"),
    ("model_clustered_metrics", "Fleet eval uses model-clustered bootstrap CIs?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist({"external_pep": False, "authenticated_routing": True,
                               "capability_gated": True, "no_model_arbitration_only": True,
                               "model_clustered_metrics": True})
    assert not bad and "external_pep" in miss
    print("OK k314_enforcement_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K314 external enforcement advisory checklist")
    ap.add_argument("cmd", choices=("checklist", "selftest", "json"))
    ap.add_argument("--json", dest="json_path", help="JSON bool map for json subcommand")
    args = ap.parse_args()

    if args.cmd == "selftest":
        selftest()
        return 0

    if args.cmd == "json":
        if not args.json_path:
            print("FAIL --json required", file=sys.stderr)
            return 1
        try:
            data = json.loads(Path(args.json_path).read_text(encoding="utf-8"))
        except FileNotFoundError:
            print(f"FAIL file not found: {args.json_path}", file=sys.stderr)
            return 1
        except json.JSONDecodeError as exc:
            print(f"FAIL invalid JSON: {exc}", file=sys.stderr)
            return 1
        ok, missing = run_checklist({k: data.get(k) is True for k, _ in CHECKS})
        print(json.dumps({"ok": ok, "missing": missing}, indent=2))
        return 0 if ok else 2

    print("# K314 external reference monitor — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nRun: python3 scripts/k314_enforcement_precheck.py json --json path/to/answers.json")
    print("Canon: wiki/concepts/recognition-enforcement-gap-instruction-arbitration.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
