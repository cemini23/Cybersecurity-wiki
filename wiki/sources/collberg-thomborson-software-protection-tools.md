---
title: Watermarking, Tamper-Proofing, and Obfuscation — Tools for Software Protection (Collberg & Thomborson, IEEE TSE 2002)
type: source
tags: [source, software-protection, anti-tamper, obfuscation, academic]
keywords: [Collberg, Thomborson, software protection, obfuscation, tamper-proofing, watermarking, malicious host, IEEE TSE 2002]
related:
  - concepts/anti-tamper-protection-classes.md
  - concepts/software-license-binding.md
maturity: draft
read_status: skimmed
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — foundational taxonomy paper; full text not pulled this run"
wire_status: wont_wire
---

## Relations

- @concepts/anti-tamper-protection-classes.md — the academic vocabulary anchor for the class map
- @concepts/software-license-binding.md — tamper-proofing is what keeps the binding check from being one `nop` away

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Watermarking, Tamper-Proofing, and Obfuscation — Tools for Software Protection |
| Author | Christian Collberg, Clark Thomborson |
| Venue | IEEE Transactions on Software Engineering 28(6), 2002 |
| DOI | 10.1109/TSE.2002.1027797 |
| Retrieved | 2026-08-12 (metadata via Semantic Scholar; abstract elided by publisher — full text not pulled) |
| Location | external (DOI only, no PDF archive) |

## Narrative

Foundational survey fixing the three software-protection goals used across the field: **obfuscation** (transform code to resist analysis), **tamper-proofing** (detect and respond to modification), **watermarking** (embed authorship identity in the program). Threat model is the **malicious host**: the attacker controls the machine the protected code runs on — which is why every protection is an economics play (raise cost), never an impossibility proof.

Read-status honesty: `skimmed` — title, venue, DOI verified; the internal taxonomy details are recorded as [TENTATIVE] on @concepts/anti-tamper-protection-classes.md until a full-text deep-read happens. No quotes fabricated from the body.

## Snippets

> Title-level only: "Watermarking, Tamper-Proofing, and Obfuscation—Tools for Software Protection" (IEEE TSE 2002; DOI 10.1109/TSE.2002.1027797). Abstract elided by publisher at retrieval time.
[Source: https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/TSE.2002.1027797 (retrieved 2026-08-12)]
