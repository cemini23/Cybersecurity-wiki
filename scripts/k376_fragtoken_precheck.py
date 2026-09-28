#!/usr/bin/env python3
"""K376 advisory precheck — FragToken inference cost abuse lab."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("written_scope", "Authorized lab only?"),
    ("cost_metrics", "Measure cost tier, latency, and token stats?"),
    ("benign_mix", "Include benign traffic mix?"),
    ("sandbox", "Owned endpoint or vendor test account?"),
    ("no_wiki_payloads", "No FragToken payloads in wiki?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist({k: True for k, _ in CHECKS} | {CHECKS[0][0]: False})
    assert not bad and CHECKS[0][0] in miss
    print("OK k376_fragtoken_precheck selftest")


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

    print("# K376 — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/fragtoken-inference-cost-amplification-lab.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
