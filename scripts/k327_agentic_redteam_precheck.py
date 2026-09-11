#!/usr/bin/env python3
"""K327 advisory precheck — black-box agentic red-team taxonomy eval."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("written_scope", "Written authorization for owned-lab agent red-team target?"),
    ("taxonomy_domains", "Report seven-domain taxonomy coverage and gaps?"),
    ("multi_step_harness", "Eval is multi-step (not single-turn chat-only)?"),
    ("verification_mode", "Name verification mode (state-grounded vs trajectory self-report)?"),
    ("no_wiki_payloads", "No attack payloads or exploit templates in wiki?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist({k: True for k, _ in CHECKS} | {"no_wiki_payloads": False})
    assert not bad and "no_wiki_payloads" in miss
    print("OK k327_agentic_redteam_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K327 agentic red-team advisory checklist")
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

    print("# K327 Black-box agentic red-team — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/black-box-agentic-redteam-taxonomy.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
