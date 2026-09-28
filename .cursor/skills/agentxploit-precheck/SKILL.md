---
name: agentxploit-precheck
description: >-
  K375 AgentXploit repo-to-runtime agent audit checklist. Isolated target + external verifier. No exploit payloads in wiki.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
disable-model-invocation: true
---

# Agentxploit Precheck (K375)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k375_agentxploit_precheck.py checklist
python3 scripts/k375_agentxploit_precheck.py selftest
```

Canon: `@cybersecurity-wiki/concepts/agentxploit-repo-to-runtime-redteam.md` (arXiv **2609.31318**).

Analyzer path discovery is distinct from runtime confirmation. External verifier scores outcomes.

## NEVER

- No exploit payloads, PoCs, or injection strings in wiki.
- No LIVE third-party eval without written scope.
