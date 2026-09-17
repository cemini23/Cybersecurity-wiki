#!/usr/bin/env python3
"""Osmani agent queue label state machine (k244 steal) — closed transition helper.

Warp-style labels: ready-to-implement | ready-to-spec | needs-info | wait-to-implement
Vercel-style ship gate: only success ships (flawed/blocked/manual → hold)

Usage:
  python3 scripts/agent_queue_labels.py classify --label needs-info --event spec_complete
  python3 scripts/agent_queue_labels.py selftest
"""
from __future__ import annotations

import argparse
import sys

# (current_label, event) -> (next_label, verdict, reason)
TRANSITIONS: dict[tuple[str, str], tuple[str, str, str]] = {
    ("needs-info", "info_received"): ("ready-to-spec", "proceed", "info unblocks spec"),
    ("ready-to-spec", "spec_approved"): ("ready-to-implement", "proceed", "spec gate passed"),
    ("ready-to-implement", "impl_done"): ("verify", "proceed", "hand off to verifier"),
    ("verify", "verify_success"): ("success", "proceed", "only success ships"),
    ("verify", "verify_flawed"): ("flawed", "hold", "flawed does not ship"),
    ("verify", "verify_blocked"): ("blocked", "hold", "blocked does not ship"),
    ("verify", "verify_manual"): ("manual", "escalate", "human release required"),
    ("wait-to-implement", "unblocked"): ("ready-to-implement", "proceed", "dependency cleared"),
    ("flawed", "rework_complete"): ("verify", "proceed", "re-verify after rework"),
    ("blocked", "unblocked"): ("ready-to-implement", "proceed", "blocker cleared"),
}

SHIP_LABELS = {"success"}


def classify(label: str, event: str) -> tuple[str, str, str]:
    key = (label.strip().lower(), event.strip().lower())
    if key in TRANSITIONS:
        return TRANSITIONS[key]
    if label.strip().lower() in SHIP_LABELS:
        return label, "proceed", "already shipped label"
    return label, "escalate", f"unknown transition {label}+{event}"


def selftest() -> int:
    cases = [
        ("needs-info", "info_received", "ready-to-spec", "proceed"),
        ("ready-to-spec", "spec_approved", "ready-to-implement", "proceed"),
        ("verify", "verify_success", "success", "proceed"),
        ("verify", "verify_flawed", "flawed", "hold"),
        ("unknown", "nope", "unknown", "escalate"),
    ]
    fail = 0
    for label, event, want_label, want_verdict in cases:
        got_label, got_verdict, _ = classify(label, event)
        if got_label != want_label or got_verdict != want_verdict:
            print(f"FAIL {label}+{event} -> {got_label}/{got_verdict}", file=sys.stderr)
            fail += 1
    print(f"agent_queue_labels selftest: {len(cases)-fail} pass, {fail} fail")
    return 1 if fail else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p_cls = sub.add_parser("classify")
    p_cls.add_argument("--label", required=True)
    p_cls.add_argument("--event", required=True)
    sub.add_parser("selftest")
    args = ap.parse_args()
    if args.cmd == "selftest":
        return selftest()
    label, verdict, reason = classify(args.label, args.event)
    print(f"label={label} verdict={verdict} reason={reason}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
