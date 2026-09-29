#!/usr/bin/env python3
"""K381 advisory precheck — distillation defenses after post-distill RL."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("post_rl_reeval", "Re-evaluate the defense after post-distillation reinforcement learning?"),
    ("threat_model_includes_rl", "Threat model includes attacker RL continuation after distill?"),
    ("owned_or_procured_models", "Eval uses owned or procured models only?"),
    ("no_distill_attack_recipes", "No distillation attack recipes or trace-theft procedures in wiki?"),
    ("dual_metric_pre_post_rl", "Report dual metrics: pre-RL and post-RL defense strength?"),
    ("no_wiki_payloads", "No attack payloads or stolen traces in wiki?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist({k: True for k, _ in CHECKS} | {"post_rl_reeval": False})
    assert not bad and "post_rl_reeval" in miss
    print("OK k381_distillation_defense_rl_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K381 distillation-defense RL advisory checklist")
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

    print("# K381 distillation defense vs post-distill RL — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/distillation-defense-reinforcement-learning-threat-model.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
