---
name: rouxii-honeypot-precheck
description: >-
  K361 deception-aware honeypot AI pentest eval checklist. Owned lab / written scope only.
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

Include deception-aware baselines when evaluating honeypots vs LLM pentesters (pairs K341).

## NEVER

- No counter-deception playbooks in wiki.
- No LIVE third-party model probing without written scope.
