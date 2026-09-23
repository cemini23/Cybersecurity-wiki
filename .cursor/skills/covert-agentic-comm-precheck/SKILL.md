---
name: covert-agentic-comm-precheck
description: >-
  K359 inference-time covert agentic communication eval checklist. Authorized lab only. Pairs K298/K347.
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

Measure benign-output predicates; account for all visible exits in agent loops.

## NEVER

- No channel encoding recipes or decoder PoCs in wiki.
- No LIVE third-party model probing without written scope.
