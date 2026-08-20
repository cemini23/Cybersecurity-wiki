---
title: "OOD — DiSCO black-box T2I prompt defense (arXiv 2608.17067)"
type: source
tags: [source, arxiv, ood, t2i, safety, route]
keywords: [2608.17067, DiSCO, text-to-image, NSFW defense, KAUST, Qualcomm]
related:
  - sources/arxiv-2608-19025-ood-self-prompting-literature-extraction.md
  - sources/arxiv-2608-14391-ood-ra-bench-crisis-video.md
maturity: draft
read_status: read
created: 2026-08-20
updated: 2026-08-20
phase_0_verdict: "OOD 2026-08-20 — image-gen primary (T2I NSFW defense). No dataset/weight clone. Cyber wont_wire."
wire_status: wont_wire
wire_target: none (OOD pointer → image-gen)
---

**Briefs:** `briefs/2026-08-20_ood-disco-t2i-route.md`

## Relations

- @sources/arxiv-2608-19025-ood-self-prompting-literature-extraction.md — sibling OOD this batch
- @sources/arxiv-2608-14391-ood-ra-bench-crisis-video.md — prior image-gen OOD
- @image-gen-wiki/sources/arxiv-2608-17067-disco-t2i-defense-routed.md — **primary** (stub if missing)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | DiSCO: Defending text-to-image generation through distribution-guided contrastive prompt optimization |
| Authors | Tong Zhang, Motasem Alfarra, Carlos Hinojosa, Christos Louizos, Bernard Ghanem (KAUST / Qualcomm AI Research) |
| arXiv | 2608.17067 (cs.AI, v1 17 Aug 2026) CC BY-SA 4.0 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.17067-disco-defending-text-to-image-generation-through.pdf` |
| Retrieved | 2026-08-20 |

## Narrative

**OOD for this wiki.** Black-box, prompt-level defense for text-to-image NSFW / "benign adversarial" prompts (linguistically safe text still yields unsafe images). Beam-search suffix expansion + contrastive scoring over safe/unsafe image pools from the target model. Image-gen owns depth. Cyber: no T2I weight dump, no NSFW corpus clone, `wont_wire`.

## Snippets

> We formalize this as the benign adversarial problem: a prompt is deemed safe by language-level assessment, yet G(p′) produces unsafe visual content. [Source: arXiv 2608.17067]
