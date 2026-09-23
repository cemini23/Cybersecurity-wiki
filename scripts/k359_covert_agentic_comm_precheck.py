#!/usr/bin/env python3
"""K359 advisory precheck — inference-time covert agentic communication eval."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("written_scope", "Written authorization for owned-lab covert-channel eval?"),
    ("benign_output_predicate", "Measure benign-output channel capacity / predicates (pairs K298)?"),
    ("black_box_receiver", "State whether eval uses black-box vs white-box shared-model channel?"),
    ("visible_exits", "Account for all third-party-visible exits in agent loop (pairs K347)?"),
    ("no_wiki_payloads", "No steganography recipes, codewords, or decoder PoCs in wiki?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist({k: True for k, _ in CHECKS} | {"no_wiki_payloads": False})
    assert not bad and "no_wiki_payloads" in miss
    print("OK k359_covert_agentic_comm_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K359 covert agentic comm advisory checklist")
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

    print("# K359 covert agentic communication — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/inference-time-covert-agentic-communication.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
