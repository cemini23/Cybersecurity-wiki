---
name: wayfinder
description: >-
  Fog-of-war planning with an explicit map, tickets, and session. Use when the
  user says /wayfinder, the goal is fuzzy, or unknown-unknowns must be listed
  before a plan. Bounded one-session paths still use grill-with-docs.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# /wayfinder — map · tickets · session

Canon: CCC `@wiki/concepts/wayfinder-fog-of-war-planning.md`. Steal-from Latent Space wayfinder (2026-08-20). **HITL:** this skill is operator-invoked; do not auto-evolve it.

## When

| Mode | Use |
|------|-----|
| **`/wayfinder`** | Goal is fuzzy; unknown-unknowns first |
| **`/grill-me` / grill-with-docs** | One-session, bounded path — interrogate to converge, then plan |
| Skip | User already named done-criteria (`/goal`) or the task is a single file edit |

**Leading words matter.** “Explore X” ≠ “Ship X”. Treat the request’s first clause as the knowns filter.

## Maintain three artifacts (this turn)

1. **Map** — known terrain, constraints, already-ruled-out paths. Facts only (elicited/observed). No invented fields.
2. **Tickets** — discrete unknowns / subtasks. Each ticket is a question, not an assumption.
3. **Session** — which tickets this run will close vs park.

Write them in the reply (short). Do not start a large tool fan-out until the map lists the critical unknowns.

## Procedure

1. Restate the request’s **leading intent** in one line.
2. List unknown-unknowns as tickets. Re-ask once for a missing critical input, then refuse/escalate — do not invent (pairs K244 / K260).
3. If the path is bounded → run **grill-with-docs** (interview + ADR) instead of a long map.
4. If exploratory → cheapest ticket first; update the map after each finding.
5. Do not treat a ticket as closed without observed evidence.

## NEVER

- Do not rewrite pass criteria / `## Verify` to match a failing run.
- Do not edit `.cursor/skills` as a side effect of this planning mode.
- No secrets in the map.
