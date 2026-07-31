---
title: ARENA — autonomous cyber-defense agent transferability (arXiv 2606.21377)
type: source
tags: [source, arxiv, blue-team, soc, autonomous-defense, cyber-range, arena]
keywords: [2606.21377, arena, agent transferability gap, cyber range, stix, telemetry schema]
related:
  - concepts/autonomous-defense-agent-transferability.md
  - concepts/soc-operations.md
  - concepts/threat-hunting.md
  - concepts/adversary-emulation.md
  - concepts/ai-for-cybersecurity.md
  - entities/frameworks/mitre-attack.md
  - sources/arxiv-2606-05252-bas-to-siem-detection-as-code-synthesis.md
  - sources/arxiv-2606-21059-defengraph-knowledge-graph-blue-team.md
maturity: draft
read_status: read
created: 2026-06-24
updated: 2026-07-31
phase_0_verdict: "Reference 2026-06-24 — architecture paper from ITA Brazil; no public ARENA artifact repo; methodology for SOC agent eval design"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

## Relations

- @concepts/autonomous-defense-agent-transferability.md — transferability gap + failure taxonomy synthesis

## Raw Concept

| Field | Value |
|-------|-------|
| Title | ARENA: An Architecture for Measuring the Transferability of Autonomous Cyber Defense |
| Authors | Sidnei Barbieri, Ágney Lopes Roth Ferraz, Wagner Comin Sonaglio, Gioliano de Oliveira Braga, Henrique Curi de Miranda, Lourenço Alves Pereira Júnior |
| Affiliation | Aeronautics Institute of Technology (ITA), Brazil |
| arXiv | 2606.21377 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2606.21377-arena-an-architecture-for-measuring-the-transfer.pdf` |
| Retrieved | 2026-06-24 |
| Read status | **read** (abstract, four-layer architecture, failure taxonomy, controlled experiment) |

## Narrative

SOC LLM defenders are validated in one environment (benchmark, lab, cyber range) then deployed elsewhere. **Agent transferability gap**: success in environment A is not evidence of capability in environment B when telemetry schema, entity grounding, query budget, or policy semantics change.

**ARENA** decomposes evaluation into four independently varying layers:

1. **Attacker emulation** — STIX/ATT&CK-constrained campaigns
2. **System Under Test (SUT) generation** — target platform synthesis
3. **Typed agent runtime** — observation/action interface
4. **Deterministic policy verifier** — ground-truth compliance check

Plus a **failure taxonomy** attributing degradation to: **schema**, **grounding**, **budget**, or **policy**.

### Controlled experiment

Two deterministic agents **indistinguishable under detection recall** in one telemetry stack **diverge** when ECS JSON becomes Splunk CIM (or Windows events become Linux audit records). ARENA attributes loss to **observation semantics**, not attack-recognition failure.

### Wiki relevance

Blue-team complement to ZERO-APT (offensive agent eval under defense). Use when assessing client SOC copilots: test same ATT&CK technique across **at least two telemetry schemas** before production trust.

`[TENTATIVE]` — single controlled experiment; broader platform coverage unverified.

## Snippets

> "Success in one environment is not evidence of capability in the next."

> "ARENA attributes the loss to observation semantics rather than to attack recognition."

[Source: arxiv-2606.21377-arena-an-architecture-for-measuring-the-transfer.pdf]
