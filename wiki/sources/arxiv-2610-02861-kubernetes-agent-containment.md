---
title: "Containment architecture for LLM agents operating Kubernetes"
type: source
tags: [source, routed, agent-security]
keywords: [arXiv 2610.02861]
related:
  - concepts/model-is-not-a-security-boundary-kubernetes-agents.md
  - concepts/coding-agent-supply-chain-install-gap.md
  - concepts/agentic-containment-principles.md
  - concepts/cyber-capable-agent-evaluation-containment.md
maturity: draft
read_status: skimmed (via routed brief)
created: 2026-10-07
updated: 2026-10-09
phase_0_verdict: "REFERENCE 2026-10-07 — routed brief, no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (inbound brief)"
---

## Relations

- @concepts/model-is-not-a-security-boundary-kubernetes-agents.md — K408-K417 ingest / 2026-10-09
- @concepts/coding-agent-supply-chain-install-gap.md — K408-K417 ingest / 2026-10-09
- @concepts/agentic-containment-principles.md — K408-K417 ingest / 2026-10-09
- @concepts/cyber-capable-agent-evaluation-containment.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Containment architecture for LLM agents operating Kubernetes |
| Identifier | arXiv 2610.02861 |
| Type | arXiv paper (routed by CCC as K421) |
| Location | not held locally — routed brief only |
| Retrieved | 2026-10-07 |
| Read status | skimmed (via routed brief) |

## Narrative

**K421 — the model is not a security boundary.** Alignment, system prompts, and input classifiers **lower the probability** of misbehaviour but guarantee nothing, and their failure modes are adversarially discoverable. An agent with cluster credentials must therefore be secured like a multi-tenant workload: **assume it is fully compromised and constrain what it can reach, do, and exfiltrate.**

**What breaks.** Agents collapse the **data/control separation** cloud-native security rests on. Content the agent merely *reads* — a log line written by an attacker-controlled workload, an annotation, a ticket field, a **third-party MCP tool description** — becomes a command it runs with its own credentials. That is the confused deputy returning when the deputy is an LLM.

**The portable rule:** break the combination of **untrusted input + sensitive access + external egress**. Any one alone is survivable; the three together are the lethal trifecta.

**Seven layers, all Kubernetes-native or widely adopted:** identity (ServiceAccounts, audience-bound projected tokens, workload-identity federation); authorization (RBAC plus **ValidatingAdmissionPolicy** in CEL for fine-grained object validation); sandboxing (gVisor / Kata via the SIG Apps Agent Sandbox project); **FQDN-aware** egress (Cilium or managed equivalents); a **tool/MCP gateway applying policy-as-code over tool arguments**; runtime eBPF (Tetragon, Falco); and API-server audit logging.

**Honest limits, stated by the author:** the paper reports a threat–control coverage matrix and four attack walkthroughs but **no measured attack-success or overhead figures**, and names the measurements needed to validate it. Treat it as a **design reference, not evidence.** Same paper family as CCC's `@ccc-wiki/concepts/model-is-not-a-security-boundary.md`. **No cluster attack walkthroughs in wiki.**

## Snippets

> Routed brief, not a first-hand read of the source. [Source: `briefs/` inbound route (2026-10-07)]
