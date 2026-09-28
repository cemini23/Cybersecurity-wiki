#!/usr/bin/env python3
"""K375 advisory precheck — AgentXploit-style repo-to-runtime agent audit."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("written_scope", "Written authorization for pre-deploy audit of an owned agent repo/runtime?"),
    ("isolated_target", "Runtime tests hit an isolated target container, not production?"),
    ("analyzer_exploiter_split", "Keep repository path discovery separate from runtime exploitation?"),
    ("attacker_interface_only", "Runtime probes use only the task-defined attacker interface?"),
    ("external_verifier", "An external deterministic verifier scores outcomes, not the agent?"),
    ("no_wiki_payloads", "No exploit payloads, PoCs, or injection strings in wiki?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist({k: True for k, _ in CHECKS} | {"external_verifier": False})
    assert not bad and "external_verifier" in miss
    print("OK k375_agentxploit_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K375 AgentXploit advisory checklist")
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

    print("# K375 AgentXploit repo-to-runtime — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/agentxploit-repo-to-runtime-redteam.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
