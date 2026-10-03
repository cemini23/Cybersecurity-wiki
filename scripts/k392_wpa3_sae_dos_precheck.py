#!/usr/bin/env python3
"""K392 advisory precheck — WPA3-SAE availability (DoS) posture review."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("authorized_scope", "Owned AP / authorized wireless lab only?"),
    ("measure_ap_cost", "Measure per-authentication AP CPU cost under repeated failed attempts?"),
    ("report_both_sides", "Report client-side cost alongside AP-side cost (not AP cost alone)?"),
    ("slow_path_intact", "Confirm the slow-path KDF / PE work is not shortened for speed?"),
    ("kdf_cost_real", "KDF iteration count set for production, not left at a prototype value?"),
    ("ticket_replay", "Ticket path has replay handling (bounded window / single-use) and revocation?"),
    ("no_wiki_payloads", "No flood rates, tool commands, or DoS recipes in wiki?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist({k: True for k, _ in CHECKS} | {"slow_path_intact": False})
    assert not bad and "slow_path_intact" in miss
    print("OK k392_wpa3_sae_dos_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K392 WPA3-SAE availability advisory checklist")
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

    print("# K392 WPA3-SAE availability (DoS) posture — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/wpa3-sae-dos-cost-asymmetry.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
