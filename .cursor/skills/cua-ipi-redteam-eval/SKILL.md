---
name: cua-ipi-redteam-eval
description: >-
  K316 advisory checklist before authorized-lab CUA indirect prompt injection
  red-team (SIR pattern). Use when operator says CUA IPI / SIR / computer-use
  red-team / K316 precheck. Does not replace VM containment policy.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# CUA IPI red-team eval — K316 advisory checklist

Canon: `@wiki/concepts/failure-driven-cua-ipi-red-teaming.md` (arXiv **2608.30207**). Helper: `scripts/k316_cua_ipi_precheck.py`. **Authorized lab only.** No IPI/principle payloads in wiki.

## Procedure

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k316_cua_ipi_precheck.py checklist
python3 scripts/k316_cua_ipi_precheck.py selftest
bash scripts/k316_k319_inventory.sh   # SIR HF / repo SPDX re-hunt
```

Score with **deterministic VM/state oracle** + **joint success** (adversarial + benign task). Pair `@wiki/concepts/agent-vm-sandboxing.md`.

## NEVER

- No LIVE third-party CUAs without written scope.
- No injection/principle payloads in wiki, briefs, or `.cursor/skills`.
- Do not treat LLM-judge ASR as faithful measurement (pairs K271).
