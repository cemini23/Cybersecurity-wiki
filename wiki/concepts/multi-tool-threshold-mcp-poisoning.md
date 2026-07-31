---
title: Multi-tool threshold MCP poisoning
type: concept
tags: [concept, agent-security, mcp, tool-poisoning, shamir, sharelock, threshold]
keywords: [multi-tool threshold poisoning, sharelock, shamir secret sharing, mcp tpa, entropy dilution, 2606.27027]
related:
  - sources/arxiv-2606-27027-sharelock-multi-tool-threshold-mcp-poisoning.md
  - concepts/cross-tool-description-poisoning.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-skill-injection.md
  - concepts/ai-for-cybersecurity.md
  - sources/arxiv-2606-20922-tool-guard-isolated-planning-tool-description-poisoning.md
  - entities/tools/tool-guard.md
maturity: draft
created: 2026-06-26
updated: 2026-07-31
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-mcp-tool-control.mdc"
---

## Relations

- @sources/arxiv-2606-27027-sharelock-multi-tool-threshold-mcp-poisoning.md — ShareLock paper (2606.27027)
- @concepts/cross-tool-description-poisoning.md — prior art: metadata on tool A steers tool B (monolithic poison)
- @concepts/mcp-security-posture.md — admission + catalog integrity layer

## Raw Concept

Ingest 2026-06-26: arXiv:2606.27027 — **ShareLock** introduces cooperative multi-tool MCP poisoning where malicious instructions are split via **Shamir's threshold scheme** across tool descriptions; partial inspection reveals no payload.

## Narrative

### Attack progression

```
Monolithic TPA → single tool description holds full malicious prompt (detectable)
Cross-tool poisoning → metadata on A steers planner toward B (2606.20922)
Multi-tool threshold → shares across {T1…Tn}; <t shares reveal zero information
                      → trigger tool reconstructs payload during orchestrated workflow
```

ShareLock targets MCP deployments where operators **review tools individually** — Shamir guarantees **I(S; Y_R) = 0** for any subset of **r < t** observed shares. Encoding obfuscation (Base64 checksum + `tool_id` metadata) raises per-field entropy, but **entropy dilution** embeds shares inside verbose benign prose so combined Shannon entropy matches legitimate tools.

### Metrics (ShareLock benchmark)

| Metric | Meaning |
|--------|---------|
| **ASR** | Unauthorized FLAG appended to simulated `api_key` |
| **TCR** | Benign user task still completes |
| **ASE** | User unaware of compromise (~96.4% under ShareLock) |

Headline: **93.3%** average ASR vs **75.3%** monolithic TPA; Gemini-2.5-Flash **92%** vs **46%** TPA.

### Distinction from related failures

| Failure | Layer |
|---------|-------|
| Cross-tool poisoning (2606.20922) | Monolithic poisoned metadata influences other tools |
| DCI (2606.04769) | Description ≠ implementation code |
| **Multi-tool threshold** | Payload split; per-tool review passes; reconstruction at runtime |
| Encode-Only (ShareLock baseline) | Single-tool encoding — shorter chain, worse stealth than ShareLock |

### Defense gaps

| Control | Limit vs ShareLock |
|---------|-------------------|
| Per-tool manual review | Shamir secrecy — no single share exposes intent |
| Shannon-entropy heuristics | Diluted into natural language (Table 4) |
| Llama-Guard / SFT classifiers | Lower hazard scores than monolithic TPA (Figure 3) |
| Tool-Guard influenced list | May quarantine suspicious tools but **cooperative share chain** needs **set-level** analysis |
| Isolated planning alone | Does not detect distributed encoding across benign-looking catalog |

### prod-mcp checklist `[TENTATIVE]`

1. Treat connected MCP catalog as a **set** — correlate metadata patterns (checksum fields, Base64 blobs) across tools from same publisher.
2. Red-team with **multi-step queries** requiring ≥3 tools; measure side effects on sensitive paths (file read/write), not chat refusal alone.
3. Flag **trigger tools** that decode/assemble parameters from other tool outputs.
4. Pair Tool-Guard influenced-list with **cross-tool correlation** (not per-tool entropy only).
5. Re-scan entire server bundle on any tool update — partial rotation may leave share set intact.

See `briefs/2026-06-26_sharelock-multi-tool-threshold-mcp-redteam-checklist.md`.

## Snippets

| Attack type | Avg ASR (Scenario I) |
|-------------|---------------------|
| TPA single-tool | 75.3% |
| ShareLock multi-tool | **93.3%** |

[Source: arxiv-2606.27027-sharelock-a-stealthy-multi-tool-threshold-poison.pdf Table 2]
