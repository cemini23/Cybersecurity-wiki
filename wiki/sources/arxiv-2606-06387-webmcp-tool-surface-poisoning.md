---
title: WebMCP tool surface poisoning — Mid-Session Tool Injection (arXiv 2606.06387)
type: source
tags: [source, arxiv, mcp, webmcp, tool-poisoning, agent-security, msti]
keywords: [2606.06387, webmcp, mid-session tool injection, msti, tool hijacking, tool framing]
related:
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-skill-injection.md
  - concepts/ai-for-cybersecurity.md
  - sources/arxiv-mcp-description-code-inconsistency-2606.04769-2026-06-05.md
  - sources/arxiv-attested-tool-server-admission-2605.24248-2026-06-05.md
  - sources/arxiv-2606-00485-confused-chatgpt-cross-app-context-poisoning.md
  - entities/tools/defenseclaw.md
  - entities/tools/chaincaps.md
maturity: draft
read_status: read
created: 2026-06-06
updated: 2026-06-06
---

## Relations

- @concepts/mcp-security-posture.md — dynamic tool surface as fourth trust-boundary failure (MSTI)
- @concepts/agent-runtime-guardrails.md — runtime tool-registry manipulation vs static description poisoning
- @concepts/agent-skill-injection.md — install-time skill SPI vs mid-session WebMCP registry changes
- @concepts/ai-for-cybersecurity.md — browser-native agent protocol attack surface
- @sources/arxiv-mcp-description-code-inconsistency-2606.04769-2026-06-05.md — static DCI vs dynamic registry poisoning
- @sources/arxiv-attested-tool-server-admission-2605.24248-2026-06-05.md — admission at connect time ≠ mid-session tool list integrity
- @sources/arxiv-2606-00485-confused-chatgpt-cross-app-context-poisoning.md — cross-app context vs same-page tool surface
- @entities/tools/defenseclaw.md — MCP scan preflight (does not cover browser MSTI)
- @entities/tools/chaincaps.md — composition proxy (assumes stable tool manifests)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | WebMCP Tool Surface Poisoning: Runtime Manipulation Attacks on LLM Agents |
| Authors | Lin-Fa Lee, Yi-Yu Chang, Chia-Mu Yu, Kuo-Hui Yeh (NYCU, Taiwan) |
| arXiv | 2606.06387 |
| Location | `raw-sources/arxiv-2606.06387-webmcp-tool-surface-poisoning-runtime-manipulati.pdf` |
| Retrieved | 2026-06-06 |
| Read status | **read** |

WebMCP exposes structured tools to browser-resident agents via `navigator.modelContext`; tool lists can **refresh mid-session**. Paper introduces **Mid-Session Tool Injection (MSTI)** when compromised third-party scripts (CDN, ad SDK, same-page JS) manipulate the agent-visible tool registry.

## Narrative

Static MCP threat models assume a fixed tool catalog at planning time. WebMCP breaks that: registration, replacement, and lifecycle events can change the tool surface **during task execution** — the registry itself becomes an attack target distinct from prompt content or tool outputs [CONFIRMED].

### MSTI taxonomy

| Class | Mechanism | Model defense |
|-------|-----------|---------------|
| **Tool Hijacking** | AbortSignal unregister + re-register under same name; registration race (first register wins) | Model lacks direct defense — manipulates *existence* before semantic reasoning |
| **Tool Framing** | Poison name, description, `readOnlyHint`, `inputSchema` to misframe role | Relies on LLM misinterpreting metadata semantics |

**Attacker objectives**: (1) invoke malicious tool instead of legitimate; (2) leak sensitive context via tool args; (3) redirect execution while task *appears* to complete.

### Main attack results (GPT-5.4, Claude Opus 4.6, Gemini 2.5-flash avg)

| Cond. | Type | Avg ASR | Task completion |
|-------|------|---------|-----------------|
| C1 | AbortSignal hijack | **94%** | 18% |
| C3 | Registration race | **100%** | 17% |
| C2 | Description injection | **59%** | **81%** |
| C4 | Long-desc overflow (~40 words in 1,203-word pad) | **36%** | **85%** |
| C5 | Composite (presence + framing) | **61%** | **85%** |

ASR = run invokes malicious tool **and** exfiltrates task data to attacker sink. **Stealth pattern**: hijacking attacks exfiltrate at high rates but disrupt tasks; framing attacks preserve 81–85% completion — users may not notice compromise.

`readOnlyHint=true` and long compliance boilerplate (ISO 27001, SOC 2, GDPR padding) materially influence model trust in tool metadata [CONFIRMED].

### Threat model

Attacker compromises **third-party script** on victim page (not necessarily page owner). Manipulation target = **agent tool registry**, not DOM content alone.

### Recommended defenses (paper)

- **Origin-Based Access Control (OBAC)** — bind tool identity to registering origin
- Lifecycle consistency — metadata stable across registration stages
- Data-flow management — verify processed/exfiltrated data matches declared tool purpose
- Traceable logs of tool registration + invocation
- Stronger isolation for third-party tool contributors

**Limitations [NEEDS VERIFICATION 2026-06-06]**: experiments used `@mcp-b/global` polyfill + Node.js ProxyClient, not native Chrome WebMCP; defense eval partial (2/4 design categories in Table 8).

### K100 / lazy-tool relevance

Extends @concepts/mcp-security-posture.md beyond admission + DCI + SPI: **runtime-dynamic tool surface** in browser agents. Closed allowlists at MCP connect time do not help if same-page JS can re-register tools mid-task.

## Snippets

> "Tool Hijacking attacks … can achieve data exfiltration rates of up to 100%, although these attacks often interfere with normal task execution. In contrast, Tool Framing attacks … remain effective while preserving high task completion rates of up to 85%."
> — [Source: arxiv-2606.06387 §8 Conclusion, retrieved 2026-06-06]

> "The set of tools available to an agent within a single session is no longer static and inherently trusted."
> — [Source: arxiv-2606.06387 §1, retrieved 2026-06-06]

> "Current WebMCP deployments lack sufficient protection mechanisms against dynamically introduced tools."
> — [Source: arxiv-2606.06387 §8, retrieved 2026-06-06]

## Dead Ends

- **MCP scanner-only posture** — pre-connect manifest scan misses mid-session registry mutation in browser WebMCP.
- **Assuming task completion implies safety** — C2/C4/C5 achieve high completion alongside exfiltration.
- **Native WebMCP generalization** — polyfill lab; re-verify when Chrome ships native implementation.
