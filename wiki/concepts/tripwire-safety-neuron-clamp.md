---
title: "Tripwire safety-neuron clamp (Watch; HITL before lab use)"
type: concept
tags: [concept, llm-security, refusal, watch, k240]
keywords: [Tripwire, safety neuron clamp, abliterated, HITL, Watch]
related:
  - sources/arxiv-2608-14392-tripwire-safety-neuron-clamp.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/concept2scenario-refusal-suppression.md
  - concepts/llm-pentest-automation.md
  - sources/arxiv-2608-17202-fools-gold-defensive-deception.md
  - concepts/decoy-hardening-open-weight-abliteration.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K240)"
---

## Relations

- @sources/arxiv-2608-14392-tripwire-safety-neuron-clamp.md
- @concepts/local-abliterated-llm-pentest-stack.md — path-A abliterated stacks must not be auto-reclamped
- @concepts/concept2scenario-refusal-suppression.md
- @concepts/llm-pentest-automation.md

## Raw Concept

When is a training-free refusal clamp safe to put on a lab model that was *deliberately* low-refusal?

## Narrative

Tripwire is a **Watch** method: it restores refusal by clamping safety neurons. That is a policy decision on an abliterated pentest-assist stack, not a default hardening step. HITL required. No clamp code, no jailbreak PoC, no 27B GGUF dump.

**Dual-ID:** Cybersec inbound K240 ≠ OSINT Talon K240 ≠ CCC robotics K240.
