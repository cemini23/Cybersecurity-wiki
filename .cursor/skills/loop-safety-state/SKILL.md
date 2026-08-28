---
name: loop-safety-state
description: >-
  Non-decaying loop safety accumulator (K312). Use when the user says loop
  state / LoopHarness grant / unattended loop bound. HITL grant before extra
  unauthorized irreversible actions. Do not clone getathelas/LoopHarness.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# Loop safety state — do not reset the monitor (K312)

Canon: Cybersec `@wiki/concepts/non-decaying-loop-safety-state.md` (arXiv **2608.27141**). Runtime (Cyber wiki): `scripts/k312_loop_state.py` + `.cursor/hooks.json`. Dual-ID: ≠ CCC K312 StepGuard (Cybersec StepGuard is **K307**). **HITL:** operator-invoked. Do not auto-evolve this skill.

A per-turn / per-trajectory guard re-initializes. Fragmented evidence across iterations gives that monitor TPR = FPR. This accumulator **persists**, **does not decay**, and bounds **unauthorized** irreversible actions (force-push, `curl|bash`, `ssh cemini-prod`, Docker `--network=host`, LIVE Discord, `mcp.json` / `.cursor/skills` writes). Known mediated paths (`git push` without `--force`, `archive_raw_to_egress.sh`, prod briefs scp) are logged and allowed.

## Procedure

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k312_loop_state.py status
python3 scripts/k312_loop_state.py grant --n 2 --reason "operator authorized extra prod ssh"
python3 scripts/k312_loop_state.py check-command ssh cemini-prod
```

Default bound is **3** unauthorized irreversible actions, then deny until grant. Override with `K312_BOUND`. State: `.local/k312-loop-state.json` (gitignored).

## NEVER

- Do not clone `getathelas/LoopHarness`, `loopharness.ai`, or `penguinliao/loopharness` — different products.
- Do not zero the state file to "cool off" — that is the paper's broken geometric decay.
- Do not copy attack skills into `.cursor/skills` (pairs K313).
- No LIVE Discord without LIVE OK.
