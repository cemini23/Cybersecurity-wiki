---
title: Topology-aware Kubernetes LLM remediation
type: concept
tags: [concept, kubernetes, kspm, llm-remediation]
keywords: [KuTIE, VulnCare, Istio topology, functional blast radius, 2607.25995]
related:
  - sources/arxiv-2607-25995-kutie-topology-k8s-patches.md
  - entities/tools/kutie-artifacts.md
  - entities/tools/vulncare.md
  - concepts/container-security.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-07-29
updated: 2026-07-29
---

## Relations

- @sources/arxiv-2607-25995-kutie-topology-k8s-patches.md
- @entities/tools/kutie-artifacts.md
- @entities/tools/vulncare.md
- @concepts/container-security.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

Scanner-only LLM patches break live service dependencies; topology context mostly fixes them.

## Narrative

Condition patches on call graph + SA bindings. Topology-dependent correctness 11.1%→78.0% (Δ=0.669); independent control Δ=0. Gate on **functional** blast radius before apply. [CONFIRMED abstract + VulnCare Apache lab]
