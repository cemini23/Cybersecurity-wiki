---
name: skilldre-precheck
description: >-
  K378 SkillDRE dual-stage skill evolution lab checklist. Pre-exec + runtime
  feedback; null SPDX REFERENCE — no clone. No skill payloads in wiki.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
disable-model-invocation: true
---

# SkillDRE Precheck (K378)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k378_skilldre_precheck.py checklist
python3 scripts/k378_skilldre_precheck.py selftest
```

Canon: `@cybersecurity-wiki/concepts/skilldre-dual-stage-malicious-skill-evolution-lab.md` (arXiv **2609.32400**).

Close the loop across pre-execution scan and runtime defense; keep a benign-task metric.

## NEVER

- No skill bodies, evolution recipes, or attack payloads in wiki.
- Do not clone `github.com/whfeLingYu/SkillDRE` (null SPDX REFERENCE).
- No LIVE third-party eval without written scope.
