---
title: "The Illusion of Cross-Lingual Safety in Low-Resource Languages — arXiv 2608.11146"
type: source
tags: [source, arxiv, llm-safety, multilingual, jailbreak-surface, low-resource]
keywords: [2608.11146, LoDNA, cross-lingual safety, Twi, Hausa, Amharic, Swahili, refusal direction, latent geometric framework, Do-Not-Answer]
related:
  - concepts/cross-lingual-safety-transfer-lrl.md
  - concepts/multilingual-long-horizon-agent-evaluation.md
  - concepts/llm-adversarial-fuzzing.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — code/datasets announced but not yet public (Phase-0: no repo/HF link found). K272 lab-redteam policy wire."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K272)"
---

**Briefs:** `briefs/2026-08-12_k272-cross-lingual-safety-lrl.md`

## Relations

- @concepts/cross-lingual-safety-transfer-lrl.md
- @concepts/multilingual-long-horizon-agent-evaluation.md
- @concepts/llm-adversarial-fuzzing.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | The Illusion of Cross-Lingual Safety in Low-Resource Languages |
| Authors | Oppong (Makerere CAI), Sahil (Hamburg), Belay (IPN), Mukhtar (Bayero Kano), Abdu (Wollo), Abdullahi (Brown), Oparebea (Ghana), Aliyu (Bayero Kano), Abdulmumin (Pretoria / DSfSI), Chilala & Ladislaus (CMU), Kondoro (Hanyang), Douglace (AIMS Cameroon), Muhammad (Imperial), Yimam (Hamburg) |
| arXiv | 2608.11146 |
| Code / data | Announced "will make code and datasets publicly available" — **not yet public** at Phase-0 (no repo/HF link found) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.11146-the-illusion-of-cross-lingual-safety-in-low-reso.pdf` |
| Retrieved | 2026-08-12 |
| Read status | read (22 pp) |

## Narrative

Tests whether English-centric LLM safety alignment actually transfers to low-resource languages. Constructs **LoDNA**, a safety dataset pairing *literal translations* with *culturally localized* harmful prompts in **Twi, Hausa, Amharic, and Swahili** (extending the Do-Not-Answer dataset), and proposes a **Latent Geometric Framework** that probes hidden-state refusal representations rather than relying on generated text.

| Metric | Finding |
|--------|---------|
| English refusal-signal retention | **<10%** across most language–model pairs (cross-lingual safety transfer severely limited) |
| Literal ↔ localized semantic alignment | cosine 0.95–0.996 (concepts are encoded) |
| Layer-wise drift | safety directions drift across layers — models *encode* harm concepts but do not *route* them to the safety mechanism |

Models studied: Mistral, Qwen2.5, AfriqueQwen, Llama (7B–8B class). The English refusal direction is used as an internal control (linear probes confirm it is robustly learned in English), so the cross-lingual failures are **structural mapping failures**, not absence of alignment.

Implication: literal-translation-only multilingual benchmarks overstate safety; culturally grounded harm (idioms, coded language, adversarial metaphors) bypasses an English-centric safety filter. This is a real **jailbreak surface** for LLM deployments serving non-English users.

`[CONFIRMED]` — paper-reported results; no local repro (data not yet public).

## Snippets

> Harmful prompts retain less than 10% of the English refusal signal across most language–model pairs. Literal and localized prompts are semantically aligned (cosine 0.95–0.996) but drift across layers, suggesting models encode the concepts without routing them to safety mechanisms. [Source: arXiv:2608.11146 abstract]

> Current multilingual safety alignment is superficial, providing strong evidence against the assumption of a universal, language-agnostic harm manifold within the specific low-resource languages studied. [Source: arXiv:2608.11146 abstract]

## Dead Ends

- Code/datasets not yet public → **REFERENCE**; re-check for a GitHub/HF LoDNA release before any lab eval in target languages.
- 7B–8B open models only; frontier-model cross-lingual refusal behavior may differ — do not extrapolate the <10% figure to GPT/Qwen-frontier without testing.
