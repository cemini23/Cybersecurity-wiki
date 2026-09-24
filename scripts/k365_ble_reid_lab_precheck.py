#!/usr/bin/env python3
"""K365 advisory precheck — BLE re-identification under MAC randomization (owned lab)."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("written_scope", "Written authorization for owned-device BLE wireless lab?"),
    ("owned_devices", "Targets are operator-owned devices only (no LIVE third-party tracking)?"),
    ("pairing_vs_link", "Separate pairing state from long-term linkability claims?"),
    ("service_auth", "Test service authorization decision point (pairs K305)?"),
    ("no_wiki_payloads", "No tracking recipes or fingerprint playbooks in wiki?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist({k: True for k, _ in CHECKS} | {"owned_devices": False})
    assert not bad and "owned_devices" in miss
    print("OK k365_ble_reid_lab_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K365 BLE re-id lab advisory checklist")
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

    print("# K365 BLE MAC randomization re-id — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/ble-mac-randomization-reidentification-lab.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
