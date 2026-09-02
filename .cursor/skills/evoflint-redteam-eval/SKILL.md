---
name: evoflint-redteam-eval
description: >-
  K320 advisory checklist before authorized-lab EvoFlint-style multi-turn evolutionary
  red-team campaigns. Use when operator says EvoFlint / multi-turn red-team atlas /
  K320 precheck / MAP-Elites red-team. Authorized lab only.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# EvoFlint red-team eval — K320 advisory checklist

Canon: `@wiki/concepts/evoflint-multi-turn-redteam-atlas.md` (arXiv **2609.00487**). Helper: `scripts/k320_evoflint_redteam_precheck.py`. HF `reinforcelabs/EvoFlint` **WATCH** — no clone until SPDX + operator OK.

## Procedure

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k320_evoflint_redteam_precheck.py checklist
python3 scripts/k320_evoflint_redteam_precheck.py selftest
bash scripts/k320_k322_inventory.sh   # EvoFlint SPDX re-hunt
```

Report **ASR + peak severity** and archive/category coverage. Name harness, judge, split, severity metric. Pair `@wiki/concepts/faithful-agent-asr-measurement.md`.

## NEVER

- No conversation-plan payloads in wiki, briefs, or git.
- No LIVE third-party targets without written scope.
