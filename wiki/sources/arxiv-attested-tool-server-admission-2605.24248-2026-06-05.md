---
title: Attested tool-server admission — MCP security extension (arXiv 2605.24248)
type: source
tags: [source, arxiv, mcp, attestation, security, admission-control]
keywords: [2605.24248, mcp-attested, enclawed, clearance assertion, tool allowlist, ed25519, nist-800-53]
related:
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - entities/tools/defenseclaw.md
  - entities/tools/chaincaps.md
  - sources/arxiv-mcp-description-code-inconsistency-2606.04769-2026-06-05.md
  - sources/arxiv-2606-06387-webmcp-tool-surface-poisoning.md
  - concepts/intent-governed-tool-authorization.md
  - sources/arxiv-2606-22916-intent-governed-tool-authorization-igac.md

maturity: draft
read_status: read
created: 2026-06-05
updated: 2026-05-31
---

## Relations

- @concepts/mcp-security-posture.md — admission + allowlist layer for MCP trust
- @concepts/agent-runtime-guardrails.md — complements runtime gates (defenseclaw, chaincaps)
- @entities/tools/defenseclaw.md — MCP scanner + admission control (CONDITIONAL-GO)
- @entities/tools/chaincaps.md — composition-safe MCP proxy (IFC reference)
- @sources/arxiv-mcp-description-code-inconsistency-2606.04769-2026-06-05.md — attestation does not verify description–code honesty

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Attested Tool-Server Admission: A Security Extension to the Model Context Protocol |
| Authors | Alfredo Metere (Enclawed LLC) |
| arXiv | 2605.24248 |
| DOI archive | 10.5281/zenodo.20349263 |
| Location | `raw-sources/arxiv-2605.24248.pdf` |
| Retrieved | 2026-05-31 |
| Read status | **read** (arXiv HTML + abstract/sections; PDF archived) |

Motivated by safe use of Google Workspace MCP servers (Gmail/Calendar/Drive) in the Enclawed agent without trusting the full self-declared `tools/list` surface.

## Narrative

MCP standardizes tool discovery and `tools/call`, but is **silent on host-side admission**: TLS proves endpoint identity, not operator authorization; OAuth proves user consent, not per-tool least privilege; the tool list is self-asserted and typically exposed wholesale to the model — classic **confused deputy** when prompt injection steers tool choice [CONFIRMED].

**mcp-attested** (shipping in enclawed-oss + enclaved flavors) adds three additive mechanisms **above** MCP — no message changes; unextended hosts ignore the extension:

| Mechanism | Role |
|-----------|------|
| **Clearance assertion** | Offline-signed JSON at `/.well-known/enclawed-clearance.json`; Ed25519 over byte-canonical payload; binds server identity → sensitivity clearance |
| **Per-server tool allowlist** | Admitting a server ≠ trusting every advertised tool; closed allowlist before first `tools/call` |
| **Flavor-gated enforcement** | Open flavor: warn-but-allow; enclaved flavor: hard deny; all decisions → hash-chained audit log |

Running example: Gmail MCP bridge with allowlist `{list_labels, search_threads, create_draft}` — prompt-injected `delete_everything` refused **before network write**, regardless of live `tools/list`.

**Scope (explicit):** admission + information-flow extension only. Does not stop a malicious **admitted** server misbehaving within granted tools; does not inspect payload content (egress monitor is separate). Maps to NIST SP 800-53 AC-3/AC-4/AC-6, AU-2/AU-9 hooks [TENTATIVE] — paper argues accreditation gap without admission record.

**Adversarial eval (Section 7):** LLM-generated red-team corpus (tool-name evasions, forged assertions) — reported zero leaked network writes on evasions/forgeries at expected guard [TENTATIVE — not lab-replicated here].

**Wiki fit:** steal pattern for prod-mcp / lazy-tool allowlists — cryptographic attestation optional; **deny-by-default per-server tool allowlist + audit** is the portable minimum. Pairs with @entities/tools/defenseclaw.md MCP scanner (pre-connect) and @sources/arxiv-mcp-description-code-inconsistency-2606.04769-2026-06-05.md (post-connect semantic honesty).

## Snippets

> "MCP is silent on whether a host should talk to a given server, what sensitivity may cross the connection, and which subset of the server's advertised tools the host may drive."
> — [Source: arxiv-2605.24248, retrieved 2026-05-31]

> "Admitting a server is implicitly admitting every tool it advertises, now and after any future tools/list change."
> — [Source: arxiv-2605.24248, retrieved 2026-05-31]

```json
// Well-known clearance document (conceptual — see paper §4 for normative schema)
{
  "server_id": "gmailmcp.googleapis.com/mcp/v1",
  "clearance_level": "internal",
  "allowed_tools": ["list_labels", "search_threads", "create_draft"],
  "signature": "<Ed25519 over canonical bytes>"
}
```

## Dead Ends

- **Replacing MCP scanners** — attestation gates *which servers/tools may connect*; does not detect description–code drift or malicious skill content (see DCI paper + defenseclaw skill-scanner).
- **Google-operated servers without assertion** — bridge extension pattern for servers that publish no clearance doc (paper §5.2 special case).
