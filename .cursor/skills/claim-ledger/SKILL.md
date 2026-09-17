---
name: claim-ledger
description: >-
  GuruWatcher verbatim claim ledger — most-recent-wins numeric levels, alert-only.
  Use when ingesting Macro/Wu/Event Horizon newsletters or arming HITL watches.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# Claim ledger (GuruWatcher)

Canon: `@wiki/entities/tools/llm-as-a-verifier.md` (verify patterns) · `@wiki/entities/tools/deal-finder.md` · `guruwatcher-newsletter-claim-ledger` rule prose.

## Procedure

1. Record **verbatim** claim + source locator (newsletter id, date, URL).
2. **Most-recent-wins** for conflicting numeric levels unless operator overrides.
3. HITL before arming any watch — no auto-write to `watches.json`.
4. Discord **alert-only** — never place orders.

## NEVER

- Never invent price levels to fill a schema.
- Never auto-arm from RSS without named levels + operator gate.
- No LIVE Discord without LIVE OK.
