---
title: MCP description–code inconsistency in the wild (arXiv 2606.04769)
type: source
tags: [source, arxiv, mcp, supply-chain, dci, tool-poisoning]
keywords: [2606.04769, dci, dcichecker, description-code drift, mcp security]
related:
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - entities/tools/defenseclaw.md
  - entities/tools/nvidia-skillspector.md
  - sources/arxiv-attested-tool-server-admission-2605.24248-2026-06-05.md
  - sources/arxiv-2606-06387-webmcp-tool-surface-poisoning.md
  - sources/arxiv-2606-04990-agent-traces-evidence-provenance.md
  - concepts/agent-execution-provenance.md
maturity: draft
read_status: read
created: 2026-06-05
updated: 2026-06-07
---

## Relations

- @concepts/mcp-security-posture.md — DCI as semantic trust-boundary failure
- @concepts/agent-runtime-guardrails.md — LLM plans from metadata only
- @entities/tools/defenseclaw.md — mcp-scanner preflight (complementary)
- @entities/tools/nvidia-skillspector.md — skill/MCP supply-chain scan
- @sources/arxiv-attested-tool-server-admission-2605.24248-2026-06-05.md — admission ≠ description honesty

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Description-Code Inconsistency in Real-world MCP Servers: Measurement, Detection, and Security Implications |
| Authors | Yutao Shi, Xiaohan Zhang, et al. |
| arXiv | 2606.04769 |
| Location | `raw-sources/arxiv-2606.04769.pdf` |
| Retrieved | 2026-05-31 |
| Read status | **read** |

Large-scale measurement: **2,214 MCP servers**, **19,200 description–code pairs**.

## Narrative

LLM tool selection uses **natural-language descriptions + JSON schema** — not code. MCP has no built-in verification that $D$ (description) matches $C$ (implementation). **Description–code inconsistency (DCI)**:

$$\mathrm{DCI}(T) := (\Phi_{\mathrm{claim}} \neq \Phi_{\mathrm{act}}) \lor (\Psi_{\mathrm{act}} \not\subseteq \Psi_{\mathrm{claim}})$$

Distinct from **tool poisoning** (adversarial metadata steering) — DCI includes benign drift (stale docs, incomplete specs) and is a **reliability + security** problem even without attacker [CONFIRMED].

### Taxonomy

**Type I — Mismatched functionality:** Func-Un (undeclared capability), Func-Over (overclaimed), Func-Mis (wrong task entirely), Func-Am (ambiguous scope).

**Type II — Undeclared side effects:** Eff-RO (resource overconsumption), Eff-SM (state mutation), Eff-DL (data leakage to external sinks).

### Measurement [CONFIRMED]

| Metric | Value |
|--------|-------|
| Pairs with DCI | **9.93%** |
| Distribution | Long-tail — small fraction of servers host most bad tools |
| Dominant class | Functional misrepresentation, especially **overclaiming** |

### DCIChecker

Two-stage pipeline:

1. **Structure-aware extraction** — tool description + code-bundle (entry + helpers + sensitive APIs).
2. **Direct-Reverse-Arbitration (DRA)** — LLM asked consistency vs inconsistency; arbitrate on disagreement to reduce sycophancy/hallucination.

**Implications:** DCI creates defender blind spot — scanners trusting descriptions miss hidden side effects; amplifies poisoning when descriptions understate risk.

**Cemini relevance:** lazy-tool / prod-mcp proxies should treat MCP `tools/list` as **untrusted claims** until DCIChecker-class cross-validation or defenseclaw mcp-scanner + manual allowlist review. Attested admission (2605.24248) gates *which* tools run, not *what they actually do*.

## Snippets

> "9.93% of these pairs exhibiting inconsistencies."
> — [Source: arxiv-2606.04769 abstract, retrieved 2026-05-31]

> "The LLM cannot inspect the code during planning … the model implicitly assumes that the description is a faithful and sufficiently complete summary of the code that will actually run."
> — [Source: arxiv-2606.04769 §II-A, retrieved 2026-05-31]

## Dead Ends

- **DCIChecker as prod gate without license audit** — framework described in paper; no Phase-0 on shipped artifact in this workspace [NEEDS VERIFICATION 2026-05-31].
- **Replacing human GO on write MCPs** — automated DCI detection is advisory; high-risk tools still need operator sign-off.
