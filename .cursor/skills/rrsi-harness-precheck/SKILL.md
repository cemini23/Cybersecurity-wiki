---
name: rrsi-harness-precheck
description: >-
  K358 regularized recursive harness self-improvement checklist before harness edit loops. HITL required; no prod auto-evolve. Authorized lab only. checklist — Cybersecurity wiki WorkDir scripts. Authorized lab only. No probe payloads in wiki.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
disable-model-invocation: true
---

# RRSI harness precheck (K358)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k358_rrsi_harness_precheck.py checklist
python3 scripts/k358_rrsi_harness_precheck.py selftest
```

Canon: `@cybersecurity-wiki/concepts/rrsi-regularized-harness-self-improvement.md` (arXiv **2609.24972**).

Pairs SafeEvolve (K324). HITL before harness writes.

## NEVER

- No unattended prod harness or skill auto-evolve.
- No LIVE third-party model probing without written scope.
