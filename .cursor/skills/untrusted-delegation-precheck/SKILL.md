---
name: untrusted-delegation-precheck
description: >-
  K333 untrusted-model delegation checklist before multi-agent or sub-agent
  credential wiring. Use when the operator says untrusted model / delegation
  broker / K333 precheck / scoped sub-agent. Pairs external-reference-monitor
  and K285/K310/K326 policy. Does not install VotalAI products.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# Untrusted-model delegation precheck (K333)

Canon: `@wiki/concepts/untrusted-model-delegation-governance.md` (arXiv **2609.00267**). Helper: `scripts/delegation_broker_precheck.py`. **HITL:** operator-invoked. **Cybersec-primary** — no PoCs, no attack payloads, no product install.

Security must hold when the model is **fully prompt-injected**. Never gate authority inside model reasoning.

## Procedure

From CCC WorkDir:

```bash
python3 scripts/delegation_broker_precheck.py checklist
python3 scripts/delegation_broker_precheck.py selftest
```

Answer the five checklist keys in a local JSON file (`external_broker`, `scoped_credentials`, `subagent_attenuation`, `audit_trail`, `fail_closed`), then:

```bash
python3 scripts/delegation_broker_precheck.py json --json /tmp/k333-answers.json
```

Pair with: `@external-reference-monitor` (K326 recognition ≠ enforcement), K285 Mandato, K310 pre-auth intent, K312 step-gate, K328 attestation (audit only).

## NEVER

- Do not treat model refusal as authorization.
- Do not hand bearer credentials to the agent runtime.
- No VotalAI / LLM Shield install without operator ticket and Phase-0 SPDX.
- No spoof templates or attack prompts in wiki or briefs.
