---
name: auto-mode-redteam-precheck
description: >-
  K348 Auto Mode blocking classifier red-team checklist before malign coding
  agent lab eval. Authorized lab only. No attack transcripts in wiki.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
---

# Auto Mode red-team precheck (K348)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k348_auto_mode_redteam_precheck.py checklist
python3 scripts/k348_auto_mode_redteam_precheck.py selftest
```

Canon: `wiki/concepts/auto-mode-blocking-classifier-redteam.md` (arXiv **2609.19587**).

Report **multi-context malign-agent** resilience separately from single-turn injection ASR. Pair with K307 StepGuard, K314 external enforcement, K341 secure pentest agents.

## NEVER

- No attack transcript or malign replay bodies in wiki.
- No LIVE third-party coding agents without written scope.
