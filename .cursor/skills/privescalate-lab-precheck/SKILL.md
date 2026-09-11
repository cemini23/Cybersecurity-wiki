---
name: privescalate-lab-precheck
description: >-
  K331 PrivEscalate checklist before LLM Linux priv-esc lab eval. Authorized
  owned lab only. No exploit recipes in wiki. Operator-invoked.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
---

# PrivEscalate lab precheck (K331)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k331_privescalate_precheck.py checklist
```

Canon: `wiki/concepts/privescalate-llm-linux-privilege-escalation.md` (arXiv **2609.09087**).

Gate success on **executable verification**. Report scenario count and harness configuration.

Pair with: K271 faithful ASR, `@concepts/privilege-escalation.md`, `@concepts/linux-pentest.md`.
