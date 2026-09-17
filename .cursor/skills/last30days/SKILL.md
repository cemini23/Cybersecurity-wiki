---
name: last30days
description: >-
  GuruWatcher / OSINT recent-research synthesis (last30days-skill patterns).
  Alert-only — never orders; never auto-rewrite watches.json. Use for macro/PM
  narrative research packs, not live trading.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# Last30days research synthesis

Canon: `@wiki/entities/tools/last30days-skill.md` · clone `.local/adopts/last30days-skill` (MIT).

## Procedure

1. Human-gate: operator confirms alert-only scope (no order placement).
2. Prefer wiki + Exa for URL verification; do not paste Barone PII into free models.
3. Output: brief or wiki delta with claim + locator tags — FILE, do not WIRE `watches.json`.

## NEVER

- Never place orders from GuruWatcher.
- Never auto-rewrite prod `watches.json`.
- No secrets on free-tier models.
