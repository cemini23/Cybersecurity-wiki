---
name: intermediary-engineer
description: >-
  Agents build/maintain small specialists instead of serving each cheap
  prediction (MetaCaster steal). Use for high-frequency alerts/screeners, or
  when the user says intermediary-engineer / MetaCaster. No TSF runtime.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# Intermediary engineer — don’t sit in the per-decision path

Canon: CCC `@wiki/concepts/agent-as-intermediary-engineer.md` (arXiv **2608.23473**, K308). Clone: CCC `.local/adopts/metacaster` (MIT REFERENCE). TSF runtime **`wont_wire`**. **HITL:** operator-invoked.

For high-frequency cheap numeric surfaces (alerts, screeners, watchers), the LLM **builds and maintains a small specialist**. It does not emit each prediction itself (LLM-as-forecaster is the anti-pattern).

## Cemini mapping

| Surface | Agent role | Not |
|---------|------------|-----|
| GuruWatcher alerts | Design/refresh thresholds + specialist; alert-only | Per-tick LLM forecast; auto `watches.json` |
| CCC eval loops | Meta-harness around a frozen verifier | Rewrite `## Verify` / pass criteria (K281/K162) |
| Screeners | Train/select a compact model from few examples + text | Foundation-model TSF APIs as default |

GuruWatcher: see `.cursor/rules/guruwatcher-k308-metacaster-phase1-wires.mdc` (alert-only). Never place orders.

## Procedure

1. Name the high-frequency decision surface.
2. Keep the **external scorer** frozen. The agent may change prompts/tools used to *build* the specialist, not the pass criteria.
3. Prefer a specialist artifact + HITL before durable config.
4. Do not clone/run MetaCaster trainers on prod.

## NEVER

- No MetaCaster/TSF runtime on CCC, GuruWatcher, or prod.
- No unattended skill evolve. No closed self-eval.
- Dual-ID: **CCC K308** = MetaCaster. Same-day Cybersec K308 if any is a different product — resolve by file+wiki.
