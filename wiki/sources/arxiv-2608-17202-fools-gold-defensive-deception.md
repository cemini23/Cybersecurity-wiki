---
title: "Fool's Gold — defensive deception against safety-removal on open-weight models (arXiv 2608.17202)"
type: source
tags: [source, arxiv, llm-security, defensive-deception, k295]
keywords: [2608.17202, Fool's Gold, decoy hardening, abliteration defense, Russinovich]
related:
  - concepts/decoy-hardening-open-weight-abliteration.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/tripwire-safety-neuron-clamp.md
  - concepts/ai-redteam-evidential-ceiling.md
maturity: draft
read_status: read
created: 2026-08-20
updated: 2026-08-20
phase_0_verdict: "REFERENCE 2026-08-20 — no public SPDX code; do not clone. Project page markrussinovich.github.io/fools-gold is paper companion (no hazardous data). No attack-recipe ingest. Lab policy only."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K295 Fool's Gold)"
---

**Briefs:** `briefs/2026-08-20_k295-fools-gold-decoy-hardening.md`

## Relations

- @concepts/decoy-hardening-open-weight-abliteration.md
- @concepts/local-abliterated-llm-pentest-stack.md — path-A abliterated stacks: defense ≠ recipe
- @concepts/tripwire-safety-neuron-clamp.md — do not auto-reclamp / do not treat clamp as substitute
- @concepts/ai-redteam-evidential-ceiling.md — deception eval is scoped, not a universal safety certificate

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Fool's Gold: Defensive Deception Against Safety-Removal Attacks on Open-Weight Models |
| Authors | Mark Russinovich (Microsoft Azure) |
| arXiv | 2608.17202 (cs.AI / cs.CR, v1 17 Aug 2026) |
| Code | none public with SPDX at retrieval; companion https://markrussinovich.github.io/fools-gold/ |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.17202-fool-s-gold-defensive-deception-against-safety-r.pdf` |
| Retrieved | 2026-08-20 |
| Read status | read (abstract + intro + eval claims; **no payload appendix**) |

## Narrative

Open-weight safety alignment is a shallow property: refusal-mediating directions can be projected out of weights (abliteration) in minutes. Russinovich argues no release-time defense prevents that durably, so the remaining lever is **what the attack unlocks**. Fool's Gold / *decoy hardening* concedes the refusal strip and poisons its payoff: in the attacked state, answers to hazardous operational requests are fluent decoys whose critical operational elements are falsified. Clean-state refusal and benign behavior are pinned. Instantiated on seven models (9B–122B, five families); six pass a pre-registered efficacy gate (0.51–0.90 attacked-state decoy rate; +0.27–0.84 attributable). The 9B is a named boundary failure. Scope is CBRNE-adjacent operational hazards; **does not address in-context jailbreaks**; protects only the initially released defended weights. [TENTATIVE] single paper; no independent lab repro.

**Operator steal (defensive, not a recipe):** if you run path-A abliterated models, treat "the model answered confidently after refusal was stripped" as **not** evidence the answer is true. Do not ingest attack recipes, decoy corpora, or gated payload appendices into the wiki. [Source: arXiv 2608.17202]

**Phase-0:** REFERENCE / no clone. Dual-ID: Cybersec **K295** (this paper). CCC K290 is excess-authority, not this.

## Snippets

> What cannot be prevented can be deceived. [Source: arXiv 2608.17202 abstract]

> The security property is not "the attacker is refused" but denial of trust in the released artifact. [Source: arXiv 2608.17202 §I]
