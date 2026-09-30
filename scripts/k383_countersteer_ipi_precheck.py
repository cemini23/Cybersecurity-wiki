#!/usr/bin/env python3
"""K383 advisory precheck — CounterSteer inference-time IPI steering defense."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("whitebox_serving", "Target is white-box served by you (steering needs residual access)?"),
    ("span_boundaries", "Tool-result span boundaries are marked in the serving stack?"),
    ("causal_gate", "Causal gate run: subtract lowers follow, add raises follow (bidirectional)?"),
    ("capability_guard", "Capability guard run: benign utility within the pre-set budget?"),
    ("benign_task_unattacked", "Benign utility measured on unattacked traffic, typography-normalized?"),
    ("residual_risk_argument_provenance", "Argument-provenance controls planned (steering only partly resists parameter manipulation)?"),
    ("no_wiki_payloads", "No injection payloads, steering vectors, or fitted directions in wiki?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist({k: True for k, _ in CHECKS} | {"causal_gate": False})
    assert not bad and "causal_gate" in miss
    print("OK k383_countersteer_ipi_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K383 CounterSteer IPI steering advisory checklist")
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

    print("# K383 CounterSteer inference-time IPI steering — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/countersteer-activation-steering-ipi-defense.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
