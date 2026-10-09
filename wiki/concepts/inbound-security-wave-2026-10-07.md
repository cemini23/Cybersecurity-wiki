---
title: "Inbound brief wave — agent verification, refusal bias, jailbreak benchmark (Wave)"
type: concept
tags: [concept, agent-security, wave]
keywords: [OSINT K282/K283 + CCC K421-K423, Wave]
related:
  - concepts/coding-agent-supply-chain-install-gap.md
  - concepts/agentic-containment-principles.md
  - concepts/k277-security-wave.md
maturity: draft
created: 2026-10-07
updated: 2026-10-09
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (inbound wave)"
---

## Relations

- @concepts/coding-agent-supply-chain-install-gap.md — K408-K417 ingest / 2026-10-09
- @concepts/agentic-containment-principles.md — K408-K417 ingest / 2026-10-09
- @concepts/k277-security-wave.md

## Raw Concept

Question: **Inbound brief wave — agent verification, refusal bias, jailbreak benchmark** — operator steal from the inbound brief (OSINT K282/K283 + CCC K421-K423)?

## Narrative

Digest of the inbound briefs of 2026-10-05..07 whose items did not each warrant a page. Each entry is **second-hand from the routed brief**, not a first-hand read.

**Agent verification (K283).** **CLIFT** (2610.06829) replaces an LLM judge with a **conformal-rectified bank of URL-scoped verification questions**, a Mondrian-ACI tracker per URL tier giving a trust weight, and an **additive-only** training reward: **+11.3 pp on OM2W at K=4 with zero policy training.** **Wikidata Search Traces** (2610.06650): a persistent-Python-state harness beats stateless tool-calling (gpt-6-luna 49→61; Qwen3.8-27B 60→74). **T-Search** (2610.06782, Apache-2.0): return **ranked evidence chunks with reasons, not answers**, keeping verifier and generator swappable. **BTTF** (2610.06790): multi-agent text-to-SQL over a normalised DB beats a single agent by **17.3%**. The shared pattern: **verification should be a separate, certified, judge-free layer.**

**Refusal surface (K282).** **PowerBench** (2610.02303), 24 models: refusals rank **power-grabbing > disempowerment > self-empowerment**; average refusal 1.0–35.1%; refusal **triples** when the request is framed at society scale; AI-agent requesters were refused more than humans. **MLCommons Jailbreak Benchmark v1.0** (2610.02827): unsafe-response rate **11.08% → 18.65%**, average **Resilience Gap 7.57 pp** (was 19.8 in v0.5), Role-Play and Template strongest at 35.7%. The reusable idea is the **paired metric** — attack-conditioned result against a baseline, so the attack's effect is separated from the model's starting disposition. **MoE router gradient** (2610.02910): router-gradient expert selection cuts refusals more than activation frequency does, in 24 of 25 conditions; OLMoE refusals fell **34 → 9 of 100**. Dual-use and local-lab only — the same gradient that finds the experts gating a refusal is what an attacker would target.

**Also noted (K283), headlines only.** Liquid Network consensus exploit — cache-key ambiguity in Elements Rangeproof verification, ~4,000 unbacked L-BTC minted, ~602 BTC unrecovered: **a validation cache is part of the consensus security boundary.** iOS **DarkSword** exploit kit reused in the wild (WebKit → PAC bypass → sandbox escape → kernel). NetScaler: **a patch does not undo a compromise** — patch and recovery are separate decisions. LLM vulnerability discovery produced >1,000 reports on Bitcoin Core, mostly false positives — prefer fuzzing and property tests. OWASP **Securing Agentic Applications**: watch for the Agentic TOP 10, ANS, and A2AS standards.

**Boundary:** FILE only. No PoC, no exploit steps, no payloads, no injection strings anywhere in this wiki.

## Snippets

> Synthesised from the routed inbound brief. [Source: `briefs/` inbound route (2026-10-07)]
