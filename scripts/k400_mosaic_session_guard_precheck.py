#!/usr/bin/env python3
"""K400 advisory precheck — multi-turn "mosaic" session-guard review.

Run before claiming a conversation guard defends against multi-turn attacks.
A fixed bounded window of recent turns is provably insufficient (arXiv 2610.05346).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("carries_state", "Does the guard carry state across turns rather than re-deciding per turn?"),
    ("no_fixed_window", "Is there no fixed window of the last N turns acting as the safety boundary?"),
    ("state_survives_boundaries", "Does the state survive session/turn boundaries (not reset or decayed)?"),
    ("watchman_labelled", "If a learned guard: trained on labelled examples, not on worst-case certificates?"),
    ("zero_failure_stated", "Is a zero-failure claim stated with its benign-helpfulness cost?"),
    ("selfplay_not_proof", "Is self-play equilibrium NOT treated as proof of usefulness?"),
    ("benign_measured", "Is worst-case benign helpfulness measured, not average?"),
    ("no_wiki_payloads", "No attack fragments, payloads, or prompt sequences in wiki?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist({k: True for k, _ in CHECKS} | {"no_fixed_window": False})
    assert not bad and "no_fixed_window" in miss
    print("OK k400_mosaic_session_guard_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K400 mosaic session-guard advisory checklist")
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

    print("# K400 multi-turn mosaic session guard — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/mosaic-attack-bounded-window-insufficiency.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
