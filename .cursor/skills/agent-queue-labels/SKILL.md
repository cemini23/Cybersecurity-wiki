---
name: agent-queue-labels
description: >-
  Osmani software-factory label state machine for agentic work queues.
  Use when triaging tasks across ready-to-spec / ready-to-implement / verify
  / success labels, or when the user says queue labels / only success ships /
  worker not verifier. Operator-invoked; does not replace step-gate for prod.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# Agent queue labels (Osmani k244 steal)

Canon: `@wiki/sources/substack-rss-addy-osmani-2026-08-21-software-factory.md`. Helper: `scripts/agent_queue_labels.py`.

**Worker ≠ verifier.** Only **`success`** ships. Labels `flawed` / `blocked` / `manual` → hold or escalate.

## Procedure

```bash
python3 scripts/agent_queue_labels.py selftest
python3 scripts/agent_queue_labels.py classify --label verify --event verify_success
python3 scripts/agent_queue_labels.py classify --label verify --event verify_flawed
```

Typical flow: `needs-info` → `ready-to-spec` → `ready-to-implement` → `verify` → `success`.

Pair with: `step-gate` for high-blast tool calls, `wayfinder` for fog-of-war planning, K276 RSM (worker ≠ verifier).

## NEVER

- Do not ship on `flawed` or `blocked` without rework + re-verify.
- Do not use labels as a substitute for external authorization (K333/K326).
