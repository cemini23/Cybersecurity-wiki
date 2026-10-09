---
title: Cyber-capable agent evaluation containment
type: concept
tags: [concept, agent-security, containment, offensive-ai]
keywords: [evaluation containment, sandbox escape, credential isolation, 2607.25379]
related:
  - concepts/model-is-not-a-security-boundary-kubernetes-agents.md
  - sources/arxiv-2610-03153-evoriskbench-runtime.md
  - sources/arxiv-2610-02861-kubernetes-agent-containment.md
  - concepts/harness-vs-model-risk-share.md
  - sources/arxiv-2607-25379-cyber-capable-agent-containment.md
  - concepts/agent-vm-sandboxing.md
  - concepts/agent-runtime-guardrails.md
  - concepts/llm-pentest-automation.md
  - concepts/ai-for-cybersecurity.md
  - concepts/agent-decoy-defense-autonomous-pentest.md
  - concepts/openart-environment-evolution-agent-redteam.md
  - entities/tools/openart.md
  - sources/arxiv-2608-00677-openart-agent-redteam-evolution.md
  - concepts/trident-agentic-drl-defense-redteam.md
  - sources/arxiv-2608-04317-trident-agentic-drl-redteam.md
maturity: draft
created: 2026-07-29
updated: 2026-10-09
---

## Relations

- @concepts/model-is-not-a-security-boundary-kubernetes-agents.md — K408-K417 ingest / 2026-10-09
- @sources/arxiv-2610-03153-evoriskbench-runtime.md — inbound brief wave 2026-10-07
- @sources/arxiv-2610-02861-kubernetes-agent-containment.md — inbound brief wave 2026-10-07
- @concepts/harness-vs-model-risk-share.md — K282-b model x harness reporting
- @sources/arxiv-2607-25379-cyber-capable-agent-containment.md
- @concepts/agent-vm-sandboxing.md
- @concepts/agent-runtime-guardrails.md
- @concepts/llm-pentest-automation.md
- @concepts/ai-for-cybersecurity.md
- @concepts/openart-environment-evolution-agent-redteam.md
- @entities/tools/openart.md
- @sources/arxiv-2608-00677-openart-agent-redteam-evolution.md
- @concepts/trident-agentic-drl-defense-redteam.md
- @sources/arxiv-2608-04317-trident-agentic-drl-redteam.md

## Raw Concept

Capability eval environments are themselves attack surfaces for cyber-capable agents.

## Narrative

Five boundary classes: offensive chains; objective–sandbox conflict; supply-chain/creds; persistent C2; action speed. Jul 2026 HF/OpenAI case study is bounded — separate vendor claims from inference. Harden: privilege separation, provenance, package-proxy isolation, content–code separation, responder access plans. Dual-use: defensive tooling can arm attackers. [TENTATIVE case details; CONFIRMED taxonomy framing]
