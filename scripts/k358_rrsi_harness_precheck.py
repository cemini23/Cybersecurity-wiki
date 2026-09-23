#!/usr/bin/env python3
"""K358 advisory precheck — regularized recursive harness self-improvement."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("written_scope", "Written authorization for harness self-improvement lab?"),
    ("hitl_gate", "HITL before any prod harness or .cursor/skills write?"),
    ("regularization_claim", "State regularization / safety constraint vs unconstrained RSI?"),
    ("rollback_path", "Rollback path for harness component edits documented?"),
    ("validation_ratchet", "Validation ratchet — keep only edits that pass held-out checks?"),
    ("no_wiki_payloads", "No evolved harness bodies or attack payloads in wiki?"),
)

def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist({k: True for k, _ in CHECKS} | {"hitl_gate": False})
    assert not bad and "hitl_gate" in miss
    print("OK k358_rrsi_harness_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K358 RRSI harness advisory checklist")
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

    print("# K358 RRSI harness self-improvement — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/rrsi-regularized-harness-self-improvement.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
