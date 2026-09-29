---
name: curriculum-pi-redteam-precheck
description: >-
  K379 curriculum prompt-injection red-team checklist for frontier models.
  Cold-start curriculum; owned lab only. No injection payloads in wiki.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
disable-model-invocation: true
---

# Curriculum PI Red-team Precheck (K379)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k379_curriculum_pi_redteam_precheck.py checklist
python3 scripts/k379_curriculum_pi_redteam_precheck.py selftest
```

Canon: `@cybersecurity-wiki/concepts/curriculum-prompt-injection-redteam-frontier-models.md` (arXiv **2609.33628**).

Document curriculum and cold-start; report harness and judge.

## NEVER

- No injection payloads or attacker prompts in wiki.
- No LIVE third-party frontier eval without written scope.
