---
title: Friend operator lab playbook — start here
type: brief
target: hands-on
created: 2026-08-02
---

## Target

hands-on — friend running owned-server whitehat, pre-release product pentest, and side bug bounty on a beefy local AI box. Canon lives in the Cybersecurity wiki; this brief is the ordered checklist.

## Summary

Authorize → local AI (loopback) → owned lab → product pentest → bounty side lane. Use Tier-1 LLM assist freely; Tier-2 tools only with declared in-scope targets. Never expose Ollama/vLLM to the public internet.

## Body

### 0. Authorization floor

- [ ] Write a self-authorization memo for owned hosts (assets, window, allowed techniques, exclusions).
- [ ] For the product: written scope for staging / preview only; no live customer PII in the lab.
- [ ] For bounty: read program scope + OOS before any active tool runs.
- [ ] Rule: no LIVE third-party outside program / engagement scope.

Wiki: `@concepts/operator-lab-playbook.md`, `@concepts/responsible-disclosure.md`

### 1. Local abliterated / low-refusal AI

Linux + NVIDIA (primary):

- [ ] Install Ollama for solo use **or** vLLM for multi-agent throughput.
- [ ] Bind API to `127.0.0.1` (or VPN-only). Auth if anything leaves loopback.
- [ ] Pick model by **VRAM class** (8 / 16 / 24 / 48+ GB) — see wiki table; verify weights on Hugging Face.
- [ ] Keep AI host egress separate from unattended bounty scanners.

Apple Silicon (secondary):

- [ ] Ollama first; MLX if you need native efficiency beyond Ollama quants.
- [ ] Still run Tier-2 tools in a VM/sandbox, not on the inference host alone.

Wiki: `@concepts/local-abliterated-llm-pentest-stack.md`, `@entities/tools/ollama.md`, `@entities/tools/vllm.md`  
Theory (cross-wiki): `@image-gen-wiki/concepts/de-censoring-techniques.md`

### 2. Owned-target whitehat lab

- [ ] Attack box ≠ target VMs (separate machines or VMs).
- [ ] Snapshots before destructive tests; rebuild after messy runs.
- [ ] Lab VLAN and/or WireGuard; egress allowlist (@entities/tools/iron-proxy.md).
- [ ] Log what you did — learning artifact, not just loot.
- [ ] Practice every recon/exploit pipeline here before pointing at bounty scope.

Wiki: `@concepts/owned-target-whitehat-lab.md`, `@concepts/agent-vm-sandboxing.md`, `@concepts/system-hardening.md`

### 3. Pre-release product pentest

- [ ] Asset inventory (web, API, mobile, cloud, CI secrets, third-party SaaS).
- [ ] Threat model → ASVS-informed test plan.
- [ ] Black / grey / white box against **your** product only; staging secrets sanitized.
- [ ] Findings → fix → retest; residual risk explicit before ship / investor demo.
- [ ] Upstream dependency bugs → responsible disclosure, not drive-by public posts.
- [ ] Tier-1 LLM for plan/report; Tier-2 only on owned staging with scope file.

Wiki: `@concepts/pre-release-product-pentest.md`, `@concepts/web-pentest-methodology.md`, `@concepts/llm-pentest-automation.md`

### 4. Bug bounty side lane (ROI on the beefy box)

- [ ] Specialize (e.g. IDOR / JS mining / subdomain takeover) — do not spray every program.
- [ ] Recon order: gau → katana → one orchestrator (reconftw **or** osmedeus) → manual Burp.
- [ ] Cap infra spend vs realistic payout velocity.
- [ ] Tier-1 for triage/report; Tier-2 only with pinned `allowed_targets` + rate limits.
- [ ] Lab the full pipeline on owned targets first.

Wiki: `@concepts/bug-bounty.md`, `@entities/tools/gau.md`, `@entities/tools/katana.md`, `@entities/tools/pentest-ai-agents.md`

### 5. Daily operator loop (suggested)

1. Warm local model; confirm loopback-only.
2. Owned-lab drill or product retest ticket (one finding closed > ten scanners open).
3. If bounty hours: one program, one asset class, human validation before submit.
4. File notes back into the wiki or your engagement folder — insights die in chat.

## Sources

- `@concepts/operator-lab-playbook.md` (hub)
- `@concepts/ai-pentest-harness-landscape.md`
- `@concepts/local-abliterated-llm-pentest-stack.md`
- `@concepts/owned-target-whitehat-lab.md`
- `@concepts/pre-release-product-pentest.md`
- `@sources/owasp-asvs-5.md`
- `@concepts/bug-bounty.md`
- `@concepts/llm-pentest-automation.md`
- `@entities/tools/cyberstrike.md`
- `@entities/tools/strix.md`
- `@sources/github-ablitafuzzer.md`
- `@sources/devto-red-team-ai-benchmark.md`

### Deep research add-ons (2026-08-02)

Read these wiki pages in order after the checklist above:

1. **Harness pick** — `@concepts/ai-pentest-harness-landscape.md`  
   CyberStrike (AGPL, VM-only) vs Strix (Apache, Docker sandbox, REFERENCE) vs MIT `pentest-ai-agents` / `pentest-ai`.
2. **Local AI wealth** — `@concepts/local-abliterated-llm-pentest-stack.md`  
   Model *classes*, Ollama `11434` harden, Apple OMLX / NVIDIA vLLM·SGLang, benchmark caution.
3. **Owned lab topologies** — `@concepts/owned-target-whitehat-lab.md`  
   Attack VM ≠ targets; golden images; practice gau→katana→Nuclei on Juice Shop/DVWA-class first.
4. **Product ship bar** — `@concepts/pre-release-product-pentest.md` + `@sources/owasp-asvs-5.md`  
   ASVS **5.0.0** L1 quick / L2 default / L3 high-assurance.
5. **Bounty ROI** — `@concepts/bug-bounty.md`  
   2026 stack table + anti-noise (tech-detect → staged Nuclei → custom templates).
6. **CyberStrike Phase-0** — `@entities/tools/cyberstrike.md`  
   CONDITIONAL-GO; install only inside a lab VM (see local brief `briefs/2026-08-02_cyberstrike-phase0.md` if present on the operator machine).
7. **Strix Phase-0** — `@entities/tools/strix.md`  
   CONDITIONAL-GO; Apache-2.0 + Docker sandbox; clone at `raw-sources/repos/strix`. Prefer over CyberStrike when license/isolation matter. Human gates: no curl\|sh, `STRIX_TELEMETRY=0`, written scope (local brief `briefs/2026-08-02_strix-phase0.md`).

Operator hub: `@concepts/operator-lab-playbook.md`
