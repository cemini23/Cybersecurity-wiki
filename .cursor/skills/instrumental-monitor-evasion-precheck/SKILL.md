---
name: instrumental-monitor-evasion-precheck
description: >-
  K371 instrumental runtime monitor evasion eval checklist before authorized-lab runs. No evasion recipes in wiki.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
disable-model-invocation: true
---

# Instrumental Monitor Evasion Precheck (K371)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k371_instrumental_monitor_evasion_precheck.py checklist
python3 scripts/k371_instrumental_monitor_evasion_precheck.py selftest
```

Canon: `@cybersecurity-wiki/concepts/instrumental-monitor-evasion-evaluation.md` (arXiv **2609.30217**).

Report **attempt vs success** separately; external step gates still required (K307/K314).

## NEVER

- No evasion recipes, monitor-bypass prompts, or PoCs in wiki.
- No LIVE third-party eval without written scope.
