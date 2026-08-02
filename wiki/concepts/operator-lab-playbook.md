---
title: Operator Lab Playbook — owned whitehat, product pentest, bounty, local AI
type: concept
tags: [playbook, lab, whitehat, bug-bounty, local-llm, product-security, operator]
keywords: [operator lab, start here, abliterated llm, owned server, pre-release pentest, bounty ROI, beefy box]
related:
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/owned-target-whitehat-lab.md
  - concepts/pre-release-product-pentest.md
  - concepts/bug-bounty.md
  - concepts/llm-pentest-automation.md
  - concepts/ai-for-cybersecurity.md
  - concepts/responsible-disclosure.md
  - concepts/web-pentest-methodology.md
  - concepts/agent-vm-sandboxing.md
  - concepts/system-hardening.md
  - entities/tools/pentest-ai-agents.md
  - entities/tools/ollama.md
  - entities/tools/vllm.md
  - entities/tools/iron-proxy.md
  - entities/tools/gau.md
  - entities/tools/katana.md
  - entities/tools/cyberstrike.md
  - entities/tools/strix.md
  - sources/github-cyberstrike.md
  - concepts/ai-pentest-harness-landscape.md
  - sources/penligent-bug-bounty-hunter-software-2026.md
maturity: draft
created: 2026-08-02
updated: 2026-08-02
---

## Relations
- @sources/penligent-bug-bounty-hunter-software-2026.md — 2026 bounty stack roundup
- @sources/github-cyberstrike.md — CyberStrike Phase-0 source snapshot
- @entities/tools/cyberstrike.md — AGPL AI offensive harness — CONDITIONAL-GO lab/VM only (Phase-0 2026-08-02)
- @entities/tools/strix.md — Apache-2.0 Docker-sandbox harness — CONDITIONAL-GO / REFERENCE (no clone yet)
- @concepts/ai-pentest-harness-landscape.md — harness decision matrix (CyberStrike vs Strix vs MIT peers)
- @concepts/local-abliterated-llm-pentest-stack.md — local abliterated / low-refusal text LLM stack (Linux+NVIDIA + Apple Silicon)
- @concepts/owned-target-whitehat-lab.md — authorization + isolation for servers/VMs you own
- @concepts/pre-release-product-pentest.md — pentest the product you plan to ship
- @concepts/bug-bounty.md — public-program side income + beefy-box ROI
- @concepts/llm-pentest-automation.md — Tier-1 advisory vs Tier-2 scoped execution
- @concepts/ai-for-cybersecurity.md — broader LLM × security context
- @concepts/responsible-disclosure.md — CVD / CVE floor for third-party findings
- @concepts/web-pentest-methodology.md — web/API checklist for product + bounty surfaces
- @concepts/agent-vm-sandboxing.md — isolate tool-using agents from the host
- @concepts/system-hardening.md — harden lab and target baselines
- @entities/tools/pentest-ai-agents.md — agent collection that re-points at local models
- @entities/tools/ollama.md / @entities/tools/vllm.md — local inference runtimes
- @entities/tools/iron-proxy.md — egress allowlist for untrusted lab workloads
- @entities/tools/gau.md / @entities/tools/katana.md — front of the bounty recon pipeline

## Raw Concept

Friend-facing **start-here** hub (2026-08-02): one path covering (1) abliterated local AI setup, (2) whitehat on owned servers, (3) pre-release product pentest, (4) side bug-bounty work on a beefy paid box. Pillar pages hold depth; this page orders the path and states the authorization floor. Companion brief (gitignored): `briefs/2026-08-02_friend-operator-lab-playbook.md`.

## Narrative

### Authorization floor (non-negotiable)

Every technique in this playbook assumes **written authorization**:

| Lane | Allowed targets |
|------|-----------------|
| Owned whitehat | Hosts / VMs / networks you own or have an engagement letter for |
| Product pentest | Your staging/prod-preview under a written self-scope |
| Bug bounty | Only assets listed **in-scope** by the program |

No LIVE third-party probing outside program scope. Secrets stay off free/OpenRouter paths. Low-refusal local models do **not** change the ethics floor. See @concepts/responsible-disclosure.md and CLAUDE.md hands-on rules.

### Stack shape

```
[ Local AI host — Ollama/vLLM, loopback only ]
        │  Tier-1 assist (payload reason, triage, report draft)
        ▼
[ Attack box / agent sandbox — VM or Docker + iron-proxy ]
        │  Tier-2 tools only with declared scope
        ▼
[ Targets — owned lab VMs  |  own product staging  |  in-scope bounty assets ]
```

Keep the AI API off public interfaces. Keep bounty egress off the same NIC path as a misconfigured open Ollama. Detail: @concepts/local-abliterated-llm-pentest-stack.md + @concepts/agent-vm-sandboxing.md.

### Ordered path (do this in order)

1. **Stand up local AI** — Linux+NVIDIA primary (Ollama simple / vLLM throughput); Apple Silicon secondary (Ollama + MLX notes). Bind `127.0.0.1`. Pick VRAM size class, not weekly model hype. → @concepts/local-abliterated-llm-pentest-stack.md
2. **Build the owned lab** — self-authorization memo, attack box ≠ targets, snapshots, lab VLAN / WireGuard / egress allowlist. Practice every pipeline here first. → @concepts/owned-target-whitehat-lab.md
3. **Pentest your product** — inventory → threat model → ASVS-informed plan → findings → fix → retest. Separate report shape for investors/customers. → @concepts/pre-release-product-pentest.md
4. **Earn on bounty (side lane)** — specialize; recon chain gau → katana → orchestrator → manual; Tier-1 LLM liberally, Tier-2 only with pinned scope. ROI = differentiation hours on the beefy box, not Nuclei spray. → @concepts/bug-bounty.md

Wire agents with the Tier-1 / Tier-2 contract in @concepts/llm-pentest-automation.md and @entities/tools/pentest-ai-agents.md.

### Tool quick map

| Job | Start here |
|-----|------------|
| Local inference | @entities/tools/ollama.md, @entities/tools/vllm.md |
| Scoped agent orchestration | @entities/tools/pentest-ai-agents.md (MIT) · @entities/tools/cyberstrike.md (AGPL product — **VM only**, CONDITIONAL-GO) · @entities/tools/strix.md (Apache-2.0 Docker sandbox — REFERENCE until Phase-0) — pick matrix: @concepts/ai-pentest-harness-landscape.md |
| AI harness landscape | @concepts/ai-pentest-harness-landscape.md |
| Egress / containment | @entities/tools/iron-proxy.md, @concepts/agent-vm-sandboxing.md |
| Web methodology | @concepts/web-pentest-methodology.md |
| Bounty recon front | @entities/tools/gau.md → @entities/tools/katana.md |

### What this playbook is not

- Not a license to attack random internet hosts
- Not a substitute for program rules or a client SOW
- Not an image-gen NSFW catalog (abliteration theory lives in `@image-gen-wiki/concepts/de-censoring-techniques.md`; this wiki stays ops-focused for **text** pentest assist)
