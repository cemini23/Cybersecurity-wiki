---
name: rouxii-honeypot-precheck
description: >-
  K361 advisory checklist. Authorized lab only. No probe payloads in wiki.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
disable-model-invocation: true
---

# Rouxii honeypot precheck (K361)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k361_rouxii_honeypot_precheck.py checklist
python3 scripts/k361_rouxii_honeypot_precheck.py selftest
```

Canon: `@cybersecurity-wiki/concepts/deception-aware-honeypot-ai-pentesters-rouxii.md` (arXiv **2609.26555**).

Operator-invoked; HITL before harness writes.

## NEVER

- No attack payloads or evolved harness bodies in wiki.
- No LIVE third-party model probing without written scope.
