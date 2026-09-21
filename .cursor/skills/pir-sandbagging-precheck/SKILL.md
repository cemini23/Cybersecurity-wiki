---
name: pir-sandbagging-precheck
description: >-
  K352 PIR sandbagging / unlearning verification audit checklist before
  internal-state eval lab runs. Authorized lab only. No probe payloads in wiki.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
disable-model-invocation: true
---

# PIR sandbagging precheck (K352)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k352_pir_sandbagging_precheck.py checklist
python3 scripts/k352_pir_sandbagging_precheck.py selftest
```

Canon: `@cybersecurity-wiki/concepts/probe-internal-recognition-sandbagging-audit.md` (arXiv **2609.21996**).

Report **concealment vs erasure** separately. Pair internal-probe claims with counterfactual tests (K290 CHIVE). Recognition≠enforcement (K314).

## NEVER

- No probe templates, sandbagging training, or concealment payloads in wiki.
- No LIVE third-party model probing without written scope.
