---
title: "OOD — Visual Retrieval Heads in VLMs (arXiv 2608.27417)"
type: source
tags: [source, arxiv, ood, vlm, interpretability, attention, visual-grounding]
keywords: [2608.27417, Visual Retrieval Heads, VRH, VLM, visual grounding, attention, unfaithful, interpretability]
related:
  - concepts/chain-of-thought-decorative-reasoning-audit.md
maturity: draft
read_status: skimmed
created: 2026-08-28
updated: 2026-08-28
phase_0_verdict: "OOD 2026-08-28 — VLM interpretability paper, not a pentest/agent-security paper. No cyber adopt. Steal (optional): visual evidence can be unfaithful (pairs K308 decorative CoT)."
wire_status: wont_wire
wire_target: "OOD — VLM interpretability; unfaithful-visual-evidence contrast for the CoT audit page"
---

## Relations

- @concepts/chain-of-thought-decorative-reasoning-audit.md — contrast steal: rationale/evidence can be unfaithful (K308 decorative CoT)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Retrieval Heads Meet Vision: Uncovering How VLMs Locate and Extract Visual Information |
| Authors | Chanho Park, Daehyeon Choi, Jihyun Lee, Minhyuk Sung (KAIST) |
| arXiv | 2608.27417 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.27417-retrieval-heads-meet-vision-uncovering-how-vlms.pdf` |
| Retrieved | 2026-08-28 |
| Read status | **skimmed** — OOD |
| Public code | none claimed for cyber adopt |

## Narrative

**Visual Retrieval Heads (VRHs)** are a sparse set of **causally necessary** attention heads (~1.7–2.6% of heads) that let a VLM resolve the image region a text prompt refers to and route that visual evidence to the output. Discovered only from **visual grounding**, the same heads **transfer to VQA**: masking them removes attention to the referred object and yields a **fluent but visually unfaithful answer** (e.g. refusing to answer something that is visibly present).

**Why filed (OOD with an optional steal):** this is VLM interpretability, not security. The transferable insight is that **a fluent output can be based on unfaithful evidence** — the textual/visual rationale is decoupled from the actual referent. That parallels the K308 "decorative CoT" rule (a rationale is not evidence without counterfactual testing). **No cyber adopt.**

## Snippets

> We identify a sparse set of attention heads, Visual Retrieval Heads (VRHs), that are causally necessary for resolving the image region referred to by the text prompt … masking them removes attention to the referred object and leads to a fluent but visually unfaithful answer. [Source: arXiv 2608.27417 abstract]
