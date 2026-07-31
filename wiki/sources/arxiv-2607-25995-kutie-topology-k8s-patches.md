---
title: KuTIE topology-aware LLM Kubernetes security patches (arXiv 2607.25995)
type: source
tags: [source, arxiv, kubernetes, llm-remediation, kspm]
keywords: [2607.25995, KuTIE, VulnCare, Istio, Trivy, topology context]
related:
  - concepts/topology-aware-k8s-llm-remediation.md
  - entities/tools/kutie-artifacts.md
  - entities/tools/vulncare.md
  - concepts/container-security.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-07-29
updated: 2026-07-31
phase_0_verdict: "SPLIT 2026-07-29 — vulncare Apache-2.0 GO ~2.6MB; kutie-artifacts Dynatrace internal-lab CONDITIONAL-GO ~2.9MB"
wire_status: wont_wire
wire_target: "Source artifact — pattern covered by thematic rules or REFERENCE"
---

**Briefs:** `briefs/2026-07-29_k224-kutie-topology-k8s-prod.md`

## Relations

- @concepts/topology-aware-k8s-llm-remediation.md
- @entities/tools/kutie-artifacts.md
- @entities/tools/vulncare.md
- @concepts/container-security.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Does Runtime Topology Context Improve LLM-Generated Kubernetes Security Patches? |
| Authors | Farooq Shaikh (Dynatrace Research) |
| arXiv | 2607.25995 |
| Code | github.com/dynatrace-research/kutie-artifacts · vulncare |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.25995-does-runtime-topology-context-improve-llm-genera.pdf` |
| Retrieved | 2026-07-29 |

## Narrative

**KuTIE** conditions LLM patches on Istio call edges + Trivy KSPM + service-account bindings. **VulnCare** = 36-deploy, 4-ns healthcare cluster, 31 findings, 7 dependency classes. 248 trials: topology-dependent patch correctness **11.1% → 78.0%** (Δ=0.669); topology-independent control Δ=0.0. Functional blast radius ≠ attack blast radius.

### Steal

1. Never auto-apply KSPM LLM patches without live call-graph + SA context
2. Gate patches on functional blast radius before apply
3. Lab: VulnCare harness for remediation eval

## Snippets

> "topology context raises topology-dependent patch correctness from 11.1% to 78.0%"
[Source: arxiv-2607.25995 abstract]
