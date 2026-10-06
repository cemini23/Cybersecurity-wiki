---
name: benchmark-representation-precheck
description: >-
  K396 benchmark representation sensitivity (TPRS) checklist. An ASR is a
  property of agent + representation. Report sensitivity, not one number.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
federation_owner: cybersecurity-wiki
disable-model-invocation: true
---

# Benchmark Representation Precheck (K396)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k396_benchmark_representation_precheck.py checklist
python3 scripts/k396_benchmark_representation_precheck.py selftest
```

Canon: `@cybersecurity-wiki/concepts/threat-preserving-representation-sensitivity.md` (arXiv **2610.03585**).

Before quoting an agent-security ASR as a robustness claim, hold the security problem fixed and vary only
the **agent-visible representation**. Across 28,904 runs that moved the score 11.67–13.21 pp on ASB and
11.00 pp on MCPTox. On ASB it moved **upward** — the original threat-flavoured tool names were an
unintended defence.

## NEVER

- No attack payloads, tool-name lists, or evasion recipes in wiki.
- Do not treat a single ASR as a robustness certificate.
- Report utility under the same transformations, not security alone.
