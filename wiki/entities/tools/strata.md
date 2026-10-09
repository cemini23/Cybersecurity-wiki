---
title: "Strata (local 125B-MoE inference engine)"
type: entity
tags: [entity, tool, agent-security]
keywords: [github.com/Niko1221/Strata, K284]
related:
  - concepts/reliable-inference-procurement-routing.md
  - concepts/local-abliterated-llm-pentest-stack.md
maturity: draft
created: 2026-10-09
updated: 2026-10-09
phase_0_verdict: "CONDITIONAL-GO K284 — MIT, active, high-star; local only. Verify the host has 35-55GB RAM and NVMe before adopting. No clone this batch."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K284)"
---

## Relations

- @concepts/reliable-inference-procurement-routing.md — K408-K417 ingest / 2026-10-09
- @concepts/local-abliterated-llm-pentest-stack.md — K408-K417 ingest / 2026-10-09

## Raw Concept

Strata (local 125B-MoE inference engine) — evaluated from the inbound routed brief (github.com/Niko1221/Strata).

## Narrative

**MIT, 16,491 stars, active (verified 2026-10-07).** A **125B-parameter MoE** model runs on consumer hardware and is exposed as a **localhost OpenAI/Anthropic-compatible endpoint**. That removes the usual trade-off for the private and air-gapped lanes: frontier-grade local reasoning with **zero token cost** and no data leaving the host.

**Why it matters for this wiki.** Two lanes gain at once. The **local abliterated lab / cyber analysis** lane gets strong local reasoning without a cloud call. **Atto air-gapped Latin/genealogical parsing** gets the privacy-perimeter path that never touches a cloud model. Because the endpoint is OpenAI/Anthropic-shaped, **existing agent code points at it with no code change** — which is the whole attraction.

**Constraints, and they are real.** The **first load locks 35-55 GB of system RAM** and needs a fast **NVMe SSD** for n-gram table paging. It competes for RAM/VRAM with any other local workload. Check the host fits before planning around it. **Human-gated; no install performed.**

## Snippets

> Verified from the routed brief, not a first-hand repo audit. [Source: `briefs/` inbound route (2026-10-09)]
