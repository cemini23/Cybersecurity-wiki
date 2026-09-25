---
name: agent-trace-tampering-precheck
description: >-
  K373 agent execution trace tampering audit checklist. Plan out-of-band append-only logging. No tamper PoCs in wiki.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
disable-model-invocation: true
---

# Agent Trace Tampering Precheck (K373)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k373_agent_trace_tampering_precheck.py checklist
python3 scripts/k373_agent_trace_tampering_precheck.py selftest
```

Canon: `@cybersecurity-wiki/concepts/agent-execution-trace-tampering-audit.md` (arXiv **2609.30266**).

Trajectory self-report is not verification (pairs K271/K278).

## NEVER

- No trace-deletion playbooks or tamper PoCs in wiki.
- No LIVE third-party eval without written scope.
