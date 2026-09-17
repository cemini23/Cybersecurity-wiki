---
name: asleval-privacy-precheck
description: >-
  K347 ASLEval checklist before agent session privacy eval. Measures privacy
  exposure displacement across multi-step sessions. Operator-invoked only.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
---

# ASLEval privacy precheck (K347)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k347_asleval_precheck.py checklist
```

Canon: `wiki/concepts/asleval-privacy-exposure-displacement.md` (arXiv **2609.18864**).

Do not treat terminal-only or single-action proxies as session privacy certificates.

Pair with: K298 inadvertent context leakage, K271 faithful ASR, `@concepts/agent-runtime-guardrails.md`.
