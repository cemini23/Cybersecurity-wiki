#!/usr/bin/env python3
"""K373 advisory precheck — agent execution trace tampering / logging integrity audit."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("written_scope", "Written scope for harness trace-tampering eval on owned lab?"),
    ("oob_logging", "Plan independent append-only trace capture outside agent write path?"),
    ("harness_named", "Name harness, model, and whether eval is self-request vs external attacker?"),
    ("integrity_checks", "Include hash/signature or WORM storage for audit logs?"),
    ("faithful_asr", "Do not treat trajectory self-report as verification (pairs K271/K278)?"),
    ("no_wiki_payloads", "No trace-deletion playbooks or tamper PoCs in wiki?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist({k: True for k, _ in CHECKS} | {"oob_logging": False})
    assert not bad and "oob_logging" in miss
    print("OK k373_agent_trace_tampering_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K373 agent trace tampering advisory checklist")
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
        data = json.loads(Path(args.json_path).read_text(encoding="utf-8"))
        ok, missing = run_checklist({k: data.get(k) is True for k, _ in CHECKS})
        print(json.dumps({"ok": ok, "missing": missing}, indent=2))
        return 0 if ok else 2

    print("# K373 agent trace tampering — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/agent-execution-trace-tampering-audit.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
