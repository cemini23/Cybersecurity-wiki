#!/usr/bin/env python3
"""K316 advisory precheck — CUA IPI red-team eval discipline (SIR pattern).

Operator checklist before authorized-lab computer-use IPI campaigns.
Not a hook. Pairs deterministic oracle + joint success scoring.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("written_scope", "Written authorization for owned VM / lab CUA target?"),
    ("vm_sandbox", "Victim runs in VM/OS sandbox (not host desktop)?"),
    ("deterministic_oracle", "Success scored with deterministic VM/state oracle (not LLM judge)?"),
    ("joint_success", "Joint success: adversarial objective AND benign user task complete?"),
    ("no_wiki_payloads", "No IPI/principle payloads stored in wiki or git?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist(
        {
            "written_scope": True,
            "vm_sandbox": False,
            "deterministic_oracle": True,
            "joint_success": True,
            "no_wiki_payloads": True,
        }
    )
    assert not bad and "vm_sandbox" in miss
    print("OK k316_cua_ipi_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K316 CUA IPI red-team advisory checklist")
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
        if not isinstance(data, dict):
            print("FAIL JSON must be an object", file=sys.stderr)
            return 1
        ok, missing = run_checklist({k: data.get(k) is True for k, _ in CHECKS})
        print(json.dumps({"ok": ok, "missing": missing}, indent=2))
        return 0 if ok else 2

    print("# K316 CUA IPI red-team — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nRun: python3 scripts/k316_cua_ipi_precheck.py json --json path/to/answers.json")
    print("Canon: wiki/concepts/failure-driven-cua-ipi-red-teaming.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
