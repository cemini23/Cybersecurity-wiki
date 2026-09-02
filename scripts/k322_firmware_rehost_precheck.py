#!/usr/bin/env python3
"""K322 advisory precheck — firmware rehosting peripheral fidelity lab discipline."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("owned_device_scope", "Written authorization for owned / in-scope hardware target?"),
    ("fidelity_criterion", "Explicit rehost fidelity acceptance criterion documented?"),
    ("peripheral_modeling", "Peripheral state updated reactively from firmware I/O?"),
    ("emulator_not_device", "Treat 'runs in emulator' ≠ 'matches on-device behavior'?"),
    ("no_wiki_exploit_payloads", "No exploit payloads or PoCs in wiki or briefs?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist(
        {
            "owned_device_scope": True,
            "fidelity_criterion": False,
            "peripheral_modeling": True,
            "emulator_not_device": True,
            "no_wiki_exploit_payloads": True,
        }
    )
    assert not bad and "fidelity_criterion" in miss
    print("OK k322_firmware_rehost_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K322 firmware rehost advisory checklist")
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

    print("# K322 firmware rehost — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nRun: python3 scripts/k322_firmware_rehost_precheck.py json --json path/to/answers.json")
    print("Canon: wiki/concepts/firmware-rehosting-peripheral-fidelity.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
