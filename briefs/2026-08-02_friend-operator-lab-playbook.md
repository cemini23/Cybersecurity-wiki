---
title: Friend operator lab playbook — start here
type: brief
target: hands-on
created: 2026-08-02
updated: 2026-08-03
---

> **Maintainer note (agents):** Living start-here for the friend. After every ingest / Phase-0 / deep-read that touches local AI, owned lab, product pentest, bounty, AI harnesses, or ASVS — update this brief (checklist, deep-research add-ons, Sources) or log `friend brief: n/a`. See `CLAUDE.md` ingest step 9b + `LESSONS.md` 2026-08-03.

## Target

hands-on — friend running owned-server whitehat, pre-release product pentest, and side bug bounty on a beefy local AI box. Canon lives in the Cybersecurity wiki; this brief is the ordered checklist.

## Summary

Authorize → local AI (loopback) → owned lab → product pentest → bounty side lane. Prefer **Strix** (Apache + Docker sandbox) over **CyberStrike** (AGPL, VM-only) when license/isolation matter; MIT `pentest-ai-agents` / `pentest-ai` when you already live in Claude Code. Use Tier-1 LLM assist freely; Tier-2 tools only with declared in-scope targets. Never expose Ollama/vLLM to the public internet.

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

- [ ] Ollama first; MLX / OMLX if you need native efficiency beyond Ollama quants.
- [ ] Still run Tier-2 tools in a VM/sandbox, not on the inference host alone.
- [ ] Optional later: `@entities/tools/strix-omlx.md` wiring (CONDITIONAL-GO clone only — **ask before** setup/PATH).

Wiki: `@concepts/local-abliterated-llm-pentest-stack.md`, `@entities/tools/ollama.md`, `@entities/tools/vllm.md`, `@entities/tools/strix-omlx.md`  
Theory (cross-wiki): `@image-gen-wiki/concepts/de-censoring-techniques.md`

### 2. Owned-target whitehat lab

- [ ] Attack box ≠ target VMs (separate machines or VMs).
- [ ] Snapshots / **golden images** before destructive tests; rebuild after messy runs.
- [ ] Lab VLAN and/or WireGuard; egress allowlist (@entities/tools/iron-proxy.md).
- [ ] Practice pipeline on owned Juice Shop/DVWA-class first: gau → katana → staged Nuclei.
- [ ] Log what you did — learning artifact, not just loot.
- [ ] Follow local brief: `briefs/2026-08-02_owned-lab-golden-image-recon.md` (gitignored OK).

Wiki: `@concepts/owned-target-whitehat-lab.md`, `@concepts/agent-vm-sandboxing.md`, `@concepts/system-hardening.md`

### 3. Pre-release product pentest

- [ ] Asset inventory (web, API, mobile, cloud, CI secrets, third-party SaaS).
- [ ] Threat model → **ASVS 5.0.0 L2** default ship bar (L1 quick / L3 high-assurance when needed).
- [ ] Work the L2 checklist: `briefs/2026-08-02_asvs-l2-product-ship-checklist.md` (gitignored OK).
- [ ] Black / grey / white box against **your** product only; staging secrets sanitized.
- [ ] Findings → fix → retest; residual risk explicit before ship / investor demo.
- [ ] Upstream dependency bugs → responsible disclosure, not drive-by public posts.
- [ ] Tier-1 LLM for plan/report; Tier-2 only on owned staging with scope file.

Wiki: `@concepts/pre-release-product-pentest.md`, `@sources/owasp-asvs-5.md`, `@concepts/web-pentest-methodology.md`, `@concepts/llm-pentest-automation.md`

### 4. Bug bounty side lane (ROI on the beefy box)

- [ ] Specialize (e.g. IDOR / JS mining / subdomain takeover) — do not spray every program.
- [ ] Recon order: gau → katana → one orchestrator (reconftw **or** osmedeus) → manual Burp.
- [ ] Cap infra spend vs realistic payout velocity.
- [ ] Tier-1 for triage/report; Tier-2 only with pinned `allowed_targets` + rate limits.
- [ ] Lab the full pipeline on owned targets first (section 2).

Wiki: `@concepts/bug-bounty.md`, `@entities/tools/gau.md`, `@entities/tools/katana.md`, `@entities/tools/pentest-ai-agents.md`

### 5. AI harness pick (before installing anything)

- [ ] Read `@concepts/ai-pentest-harness-landscape.md` (decision matrix).
- [ ] Default prefer: **Strix** (Apache-2.0, Docker sandbox) → MIT agents/MCP → CyberStrike only on disposable VM.
- [ ] Strix human gates: no curl\|sh, `STRIX_TELEMETRY=0`, written scope — `briefs/2026-08-02_strix-phase0.md`.
- [ ] CyberStrike human gates: VM-only, AGPL — `briefs/2026-08-02_cyberstrike-phase0.md`.
- [ ] Peers HexStrike / CAI / PentestGPT = **REFERENCE** desk only — do not host-install.

### 6. Daily operator loop (suggested)

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
- `@concepts/buffer-overflow.md` · `@concepts/threat-hunting.md` · `@entities/certifications/ecppt.md` (Joas deep-reads 2026-08-02)
- `@entities/tools/cyberstrike.md`
- `@entities/tools/strix.md`
- `@entities/tools/strix-omlx.md`
- `@entities/tools/hexstrike-ai.md`
- `@entities/tools/cai-framework.md`
- `@entities/tools/pentestgpt.md`
- `@sources/github-ablitafuzzer.md`
- `@sources/devto-red-team-ai-benchmark.md`
- Local briefs (gitignored OK):  
  `briefs/2026-08-02_asvs-l2-product-ship-checklist.md` ·  
  `briefs/2026-08-02_owned-lab-golden-image-recon.md` ·  
  `briefs/2026-08-02_strix-phase0.md` ·  
  `briefs/2026-08-02_cyberstrike-phase0.md` ·  
  `briefs/2026-08-02_strix-omlx-phase0.md`

### Deep research add-ons (2026-08-02)

Read these wiki pages in order after the checklist above:

1. **Harness pick** — `@concepts/ai-pentest-harness-landscape.md`  
   CyberStrike (AGPL, VM-only) vs Strix (Apache, Docker sandbox, CONDITIONAL-GO) vs MIT `pentest-ai-agents` / `pentest-ai`. Peers desk: HexStrike / CAI / PentestGPT = **REFERENCE**.
2. **Local AI wealth** — `@concepts/local-abliterated-llm-pentest-stack.md`  
   Model *classes*, Ollama `11434` harden, Apple OMLX / NVIDIA vLLM·SGLang, benchmark caution.
3. **Owned lab topologies** — `@concepts/owned-target-whitehat-lab.md`  
   Attack VM ≠ targets; golden images; practice gau→katana→Nuclei on Juice Shop/DVWA-class first.  
   **Hands-on:** `briefs/2026-08-02_owned-lab-golden-image-recon.md`
4. **Product ship bar** — `@concepts/pre-release-product-pentest.md` + `@sources/owasp-asvs-5.md`  
   ASVS **5.0.0** L1 quick / L2 default / L3 high-assurance.  
   **Hands-on L2 checklist:** `briefs/2026-08-02_asvs-l2-product-ship-checklist.md`
5. **Bounty ROI** — `@concepts/bug-bounty.md`  
   2026 stack table + anti-noise (tech-detect → staged Nuclei → custom templates).
6. **CyberStrike Phase-0** — `@entities/tools/cyberstrike.md`  
   CONDITIONAL-GO; install only inside a lab VM (`briefs/2026-08-02_cyberstrike-phase0.md`).
7. **Strix Phase-0** — `@entities/tools/strix.md`  
   CONDITIONAL-GO; clone `raw-sources/repos/strix`. No curl\|sh; `STRIX_TELEMETRY=0` (`briefs/2026-08-02_strix-phase0.md`).
8. **strix-omlx Phase-0** — `@entities/tools/strix-omlx.md`  
   CONDITIONAL-GO clone `raw-sources/repos/strix-omlx` @ `b623b9f`; ask before setup/PATH (`briefs/2026-08-02_strix-omlx-phase0.md`).
9. **Harness peers (REFERENCE)** — `@entities/tools/hexstrike-ai.md`, `@entities/tools/cai-framework.md`, `@entities/tools/pentestgpt.md`  
   Desk only; no host install; CAI dual-license restricts commercial use.
10. **Joas deep-reads (2026-08-02)** — BOF intro/guide/beginners + eCPPT notes + CTH intro PT.1  
    Sources upgraded to `deep-read`; wealth in `@concepts/buffer-overflow.md`, `@concepts/threat-hunting.md`, `@entities/certifications/ecppt.md`. PDFs may still sit in `research to be indexed/` pending egress archive.

Operator hub: `@concepts/operator-lab-playbook.md`
