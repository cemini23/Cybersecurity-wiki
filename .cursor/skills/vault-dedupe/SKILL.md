---
name: vault-dedupe
description: >-
  Atto vault APFS/CoW dedupe with fclones (human-gated). Use before large vault
  imports or mirror jobs — not unattended delete on Barone paths.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# Vault dedupe (fclones)

Canon: `@wiki/entities/tools/fclones.md` · clone `.local/adopts/fclones` (MIT).

## Procedure

1. Dry-run only first: `fclones group --dry-run` on operator-chosen paths (never Barone paths in git examples).
2. Human confirms candidate groups before any `--reflink=never` delete path.
3. PII strip unchanged — dedupe does not replace privacy-filter.

## NEVER

- No unattended `--delete` on vault paths.
- No Barone family paths in committed scripts or examples.
- AGPL/GPL tools stay extract-only — fclones is MIT but still HITL.
