---
name: agentic-redteam-taxonomy-precheck
description: >-
  K327 black-box agentic red-team checklist before multi-step agent eval.
  Use for taxonomy-driven agent risk discovery lab runs. Pairs faithful ASR
  and security-agent SLR audit axes. Operator-invoked only.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
---

# Agentic red-team taxonomy precheck (K327)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k327_agentic_redteam_precheck.py checklist
```

Canon: `wiki/concepts/black-box-agentic-redteam-taxonomy.md` (arXiv **2609.09647**).

**Authorized lab only.** No attack payloads in wiki. Report ASR as `(harness, judge, taxonomy domain, verification mode)`.

Pair with: K271 faithful ASR, K315 security-agent SLR, K320 EvoFlint multi-turn atlas.
