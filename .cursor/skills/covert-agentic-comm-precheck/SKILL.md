---
name: covert-agentic-comm-precheck
description: >-
  K359 advisory checklist. Authorized lab only. No probe payloads in wiki.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
disable-model-invocation: true
---

# Covert agentic communication precheck (K359)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k359_covert_agentic_comm_precheck.py checklist
python3 scripts/k359_covert_agentic_comm_precheck.py selftest
```

Canon: `@cybersecurity-wiki/concepts/inference-time-covert-agentic-communication.md` (arXiv **2609.24994**).

Operator-invoked; HITL before harness writes.

## NEVER

- No attack payloads or evolved harness bodies in wiki.
- No LIVE third-party model probing without written scope.
