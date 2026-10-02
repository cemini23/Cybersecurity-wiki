---
name: kalibench-tooluse-precheck
description: >-
  K391 KaliBench NL-to-CLI tool-use eval checklist. Score against a fixed
  reference; split tool selection from argument construction. Licence unverified.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
disable-model-invocation: true
---

# KaliBench Precheck (K391)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k391_kalibench_precheck.py checklist
python3 scripts/k391_kalibench_precheck.py selftest
```

Canon: `@cybersecurity-wiki/concepts/kalibench-nl-to-cli-tool-use-eval.md` (arXiv **2610.02206**).

Score a tool invocation against a **fixed reference command**, never against the model's own account of
what it ran, and never by executing model output. Report **tool selection and argument construction
separately** — selection nearly resolves when candidates are narrowed, while exactness does not move
until the arguments are pinned down.

## NEVER

- No clone and no dataset download: `RISys-Lab/KaliBench` returns **null SPDX** with **no LICENSE file**
  and no README licence text (verified 2026-10-02), so the paper's CC BY-NC 4.0 claim is unverified.
- No executable command lists or attack payloads in wiki.
- Note that ground truth comes from build-time manuals — flags drift.
