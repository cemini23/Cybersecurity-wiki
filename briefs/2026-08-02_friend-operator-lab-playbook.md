---
title: Friend operator lab playbook — start here
type: brief
target: hands-on
created: 2026-08-02
updated: 2026-08-05
---


> **Maintainer note (agents):** Living start-here for the friend. After every ingest / Phase-0 / deep-read that touches local AI, owned lab, product pentest, bounty, AI harnesses, ASVS, or friend dual-wiki / OPSEC onboarding — update this brief (checklist, deep-research add-ons, Sources) or log `friend brief: n/a`. See `CLAUDE.md` ingest step 9b + `LESSONS.md` 2026-08-03.

## Target

hands-on — friend running owned-server whitehat, pre-release product pentest, and side bug bounty on a beefy local AI box. **Primary canon:** Cybersecurity wiki. **OPSEC sidecar:** private OSINT wiki (`llm-wiki-by-cemini`). This brief is the ordered checklist.

## Summary

Authorize → local AI (loopback) → owned lab → product pentest → bounty side lane. Prefer **Strix** (Apache + Docker sandbox) over **CyberStrike** (AGPL, VM-only) when license/isolation matter; MIT `pentest-ai-agents` / `pentest-ai` when you already live in Claude Code. Use Tier-1 LLM assist freely; Tier-2 tools only with declared in-scope targets. Never expose Ollama/vLLM to the public internet. Day-1 laptop = Cursor + route/`claude-ds` + both wikis; Flash-class local models wait for the lab box.

## Body

### Dual-wiki start (before §0)

Cyber = **what to build** (lab, local AI, harnesses, ASVS, bounty). OSINT = **how not to burn yourself** while researching / reconning (collection OPSEC, fingerprint, attribution hygiene, supply-chain discipline). Do not treat OSINT as a trading or TipDrop curriculum.

| Role | Repo | Access | Open in Cursor |
|------|------|--------|----------------|
| **Primary** | `Cybersecurity-wiki` | Public GitHub | Daily root — this brief → `@concepts/operator-lab-playbook.md` |
| **OPSEC sidecar** | `llm-wiki-by-cemini` (OSINT) | Private — accept `cemini23/llm-wiki-by-cemini` invite first | Second root / multi-root so `@osint-wiki/...` resolves |
| **Harness host only** | `tipdrop-workspace-kit` | Public | Scripts: `claude-ds`, `route-task`, `adopt-route-always-approve` — not TipDrop product ops |

**Install (kit umbrella):** from TipDrop kit root run `.\scripts\install-federation-wikis.ps1` (clones Cyber + private OSINT when invite is accepted). See kit `FEDERATION-WIKI-INDEX.md`.

**Day-1 laptop (not the lab box):** Remote call setup — follow tracked **`briefs/2026-08-05_friend-day1-cursor-goal-paste.md`** (PART A manual checkboxes → paste PART B `/goal` into Cursor Agent). Outcome: kit + Cyber + OSINT + `claude-ds` + route + skills/MCP + `friend-day1-cheatsheet.md`. Skip Ollama/Flash weight pulls until path A hardware exists.

**OSINT OPSEC reading order** (skip PM/HL bots, ICE/tickers, TipDrop compliance unless a cyber page cross-links):

1. `@osint-wiki/entities/tools/fingerprint-suite.md` — browser fingerprint gen/injection  
2. `@osint-wiki/entities/tools/octobrowser.md` — profile / antidetect separation  
3. `@osint-wiki/entities/tools/arkham-intelligence.md` — what on-chain attribution looks like from the outside  
4. `@osint-wiki/entities/tools/mitre-atlas.md` — AI-system adversarial taxonomy  
5. `@osint-wiki/entities/tools/cua.md` — agent sandbox patterns (pairs cyber `@concepts/agent-vm-sandboxing.md`)  
6. OSINT `CLAUDE.md` Phase-0 habit — don’t trust README `curl\|sh`; pairs cyber K220 hard stops  

**Lab OPSEC that stays in Cyber** (read with §1–2, not as OSINT substitutes): `@concepts/agent-vm-sandboxing.md`, `@concepts/system-hardening.md`, `@entities/tools/iron-proxy.md`, `@concepts/local-abliterated-llm-pentest-stack.md` (loopback-only).

### 0. Authorization floor

- [ ] Write a self-authorization memo for owned hosts (assets, window, allowed techniques, exclusions).
- [ ] For the product: written scope for staging / preview only; no live customer PII in the lab.
- [ ] For bounty: read program scope + OOS before any active tool runs.
- [ ] Rule: no LIVE third-party outside program / engagement scope.

Wiki: `@concepts/operator-lab-playbook.md`, `@concepts/responsible-disclosure.md`

### 1. Local abliterated / low-refusal AI

**Dual-model pattern (friend choice 2026-08-03) — pick the best planner, not a fixed HF slug:**

| Role | Job | Current best pick (re-check before buy) | Refusal |
|------|-----|----------------------------------------|---------|
| **Planner** | Attack trees, scope, “what next,” long recon dumps | **Abliterated DeepSeek-V4-Flash-0731** (see ranking below) | Low-refusal required |
| **Executor** | Tool loops, payloads, dual-use detail | Smaller **coder-abliterated** 7B–14B Q4 | Low-refusal required |

Upstream capability base (do not skip): official [`deepseek-ai/DeepSeek-V4-Flash-0731`](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731) — agentic jump over preview Flash. Then apply the **best abliterated rebuild** that preserves tool-calling. **Expect better planners soon** — buy for Flash-0731 *class* VRAM/serving; re-pick HF weights when a stronger abliterated 0731+/successor drops (don’t freeze on today’s slug).

**Planner ranking for path A (as of 2026-08-03 — smoke-test before trusting):**

| Rank | Repo | Why | Host fit |
|------|------|-----|----------|
| **1 — default** | [`cebeuq/DeepSeek-V4-Flash-0731-abliterated`](https://huggingface.co/cebeuq/DeepSeek-V4-Flash-0731-abliterated) | Native **FP4+FP8** (~167 GB); published refusal drop (AdvBench sample → 0%); **tool-call compliance kept at 1.0**; DSpark draft acceptance ~parity | NVIDIA multi-GPU **~160–320 GB** (vLLM) |
| **2 — FP8 / Apple tree** | [`apetersson/DeepSeek-V4-Flash-0731-Abliterated-FP8`](https://huggingface.co/apetersson/DeepSeek-V4-Flash-0731-Abliterated-FP8) (+ MLX/DS4 quants) | Solid rank-1 abliteration of 0731; FP8 ~280 GB class; quants for **≥128 GB** Apple | Multi-GPU NVIDIA **or** 128–256 GB unified via quant |
| **3 — cyber-smoke GGUF** | [`cyberneurova/CyberNeurova-DeepSeek-V4-Flash-abliterated-GGUF`](https://huggingface.co/cyberneurova/CyberNeurova-DeepSeek-V4-Flash-abliterated-GGUF) | Explicit hacking/bug-finding compliance numbers in card; llama.cpp path | Depends on quant; re-validate tools |
| **4 — Blackwell throughput** | [`fraserprice/DeepSeek-V4-Flash-Abliterated`](https://huggingface.co/fraserprice/DeepSeek-V4-Flash-Abliterated) | Tuned for **2× RTX Pro 6000** (~170 GB) high tok/s | Only if buying that GPU class |
| **Fallback (not path A)** | R1-Distill 14B–32B heretic/abliterated | Workstation-only if Flash budget slips | Single 24–48 GB |

**Locked buy path A:** real Flash-class abliterated planner locally (rank 1–4), **not** a 48 GB distill as the primary plan.

| Track | Hardware target | Notes |
|-------|-----------------|-------|
| **A1 — NVIDIA (primary)** | Multi-GPU **~160–320 GB** total (2×H200-class or 4×80 GB) | Default for **cebeuq** native ~167 GB + KV/headroom + optional executor |
| **A2 — Apple (alt)** | **≥128 GB** unified (**256 GB** preferred) | Use apetersson/cyberneurova **quants**; re-smoke refusal after quant |
| **Executor** | Extra **~10–24 GB** | 7B–14B coder-abliterated always hot |
| **Do not buy for A** | Single **48 GB** as Flash host | Wrong class |

Also: **2 TB+ NVMe**, **64 GB+** system RAM, lab VLAN, attack host ≠ target VMs.

Linux + NVIDIA (path A1):

- [ ] Provision multi-GPU for **rank-1 planner** (default cebeuq) via current vLLM/SGLang docs — verify revision before download.
- [ ] Bind API to `127.0.0.1` (or VPN-only). Auth if anything leaves loopback.
- [ ] Second model: smaller coder-abliterated executor (leftover VRAM or second GPU).
- [ ] Smoke-test **both** with in-scope dual-use + tool-call prompts (abliteration ≠ universal uncensor; quants regress).
- [ ] Wire: plan → Flash-abliterated; tool/execute → small coder-abliterated.
- [ ] Keep AI host egress separate from unattended bounty scanners.

Apple Silicon (path A2):

- [ ] **≥128 GB** unified (256 GB preferred); pick quant from rank 2–3; re-smoke refusal + tools.
- [ ] Tier-2 tools in VM/sandbox, not on inference host alone.
- [ ] Optional: `@entities/tools/strix-omlx.md` after operator OK.

Wiki: `@concepts/local-abliterated-llm-pentest-stack.md`, `@entities/tools/ollama.md`, `@entities/tools/vllm.md`, `@entities/tools/strix-omlx.md`  
Theory (cross-wiki): `@image-gen-wiki/concepts/de-censoring-techniques.md`

### 2. Owned-target whitehat lab

- [ ] Attack box ≠ target VMs (separate machines or VMs).
- [ ] Snapshots / **golden images** before destructive tests; rebuild after messy runs.
- [ ] Lab VLAN and/or WireGuard; egress allowlist (@entities/tools/iron-proxy.md).
- [ ] Practice pipeline on owned Juice Shop/DVWA-class first: gau → katana → staged Nuclei.
- [ ] Optional niche lab: Damn-Vulnerable-Drone (ArduPilot/MAVLink) if you care about IoT/drone — MIT, owned Docker only (`@entities/tools/damn-vulnerable-drone.md`).
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
- [ ] CDN / origin-IP (in-scope only): CloakQuest3r (MIT) peer to CF-Hero — `@entities/tools/cloakquest3r.md`.
- [ ] Optional scanner study: Raccoon (MIT Reference) — `@entities/tools/raccoon.md`. Do not auto-install null-SPDX tools.
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
- [ ] **Steal-from (no clone):** Black-cat hypothesis→evidence ledger (RECON ⇄ ENUMERATE ⇄ VALIDATE + JSONL + verify-before-REPORT). Null SPDX — patterns only; keep HITL on high-blast actions (`@entities/tools/black-cat.md`, K220).
- [ ] Hard stops from K220: no auto-install null-SPDX; TorBot / BypassAV / HackTools = study or authorized lab only (`@sources/osint-k220-cyber-agent-harness-eval-2026-08-03.md`).

### 6. Daily operator loop (suggested)

1. Warm local model; confirm loopback-only.
2. Owned-lab drill or product retest ticket (one finding closed > ten scanners open).
3. If bounty hours: one program, one asset class, human validation before submit.
4. File notes back into the wiki or your engagement folder — insights die in chat.

## Sources

- Dual-wiki + day-1 setup: `briefs/2026-08-05_friend-day1-cursor-goal-paste.md` · `@concepts/operator-lab-playbook.md` (hub) · TipDrop kit `FEDERATION-WIKI-INDEX.md` + `scripts/install-federation-wikis.ps1` · `@osint-wiki/entities/tools/fingerprint-suite.md` · `@osint-wiki/entities/tools/octobrowser.md` · `@osint-wiki/entities/tools/arkham-intelligence.md` · `@osint-wiki/entities/tools/mitre-atlas.md` · `@osint-wiki/entities/tools/cua.md`
- `@concepts/operator-lab-playbook.md` (hub)
- `@concepts/ai-pentest-harness-landscape.md`
- `@concepts/local-abliterated-llm-pentest-stack.md`
- `@concepts/owned-target-whitehat-lab.md`
- `@concepts/pre-release-product-pentest.md`
- `@sources/owasp-asvs-5.md`
- `@concepts/bug-bounty.md`
- `@concepts/llm-pentest-automation.md`
- `@concepts/buffer-overflow.md` · `@concepts/threat-hunting.md` · `@entities/certifications/ecppt.md` (Joas deep-reads; egress 2026-08-03)
- `@concepts/toktier-exact-stateful-tokenization.md` · `@concepts/stair-hierarchical-repair-plans.md` (K235/K234)
- `briefs/2026-08-03_ecppt-exam-cram.md` (gitignored OK)
- `@entities/tools/cyberstrike.md`
- `@entities/tools/strix.md`
- `@entities/tools/strix-omlx.md`
- `@entities/tools/hexstrike-ai.md`
- `@entities/tools/cai-framework.md`
- `@entities/tools/pentestgpt.md`
- `@sources/github-ablitafuzzer.md`
- `@sources/devto-red-team-ai-benchmark.md`
- `@sources/osint-k220-cyber-agent-harness-eval-2026-08-03.md` (K220 tool register)
- `@entities/tools/black-cat.md` · `@entities/tools/cloakquest3r.md` · `@entities/tools/raccoon.md` · `@entities/tools/damn-vulnerable-drone.md`
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
10. **Joas deep-reads (closed 2026-08-03)** — BOF intro/guide/beginners + eCPPT notes + CTH intro PT.1  
    Wealth in `@concepts/buffer-overflow.md` (**validated**), `@concepts/threat-hunting.md`, `@entities/certifications/ecppt.md`. PDFs on egress-fi. Cram: `briefs/2026-08-03_ecppt-exam-cram.md` (gitignored OK).
11. **TokTier / agent TTFT (K235)** — `@concepts/toktier-exact-stateful-tokenization.md`  
    Under high prompt-cache hit rates, tokenization dominates TTFT for tool-loop agents. Keep exact tokenize contract on local vLLM path A; pair with InferScale KV caution.
12. **STAIR repair plans (K234)** — light: if using coding/repair agents, abstract past trajectories into hierarchical plans before re-inject (`@concepts/stair-hierarchical-repair-plans.md`). CWEEP (K233) only if you touch RTL.
13. **K220 tool register (2026-08-03)** — `@sources/osint-k220-cyber-agent-harness-eval-2026-08-03.md`  
    Steal Black-cat ledger pattern (no clone). Recon desk: CloakQuest3r + Raccoon (MIT). Optional lab: Damn-Vulnerable-Drone. Skip TorBot/BypassAV/HackTools installs unless license + scope clear. Catalog brief: `briefs/2026-08-03_k220-cyber-context-catalog.md`.

13. **Salami / collusive memory (K238)** — `@concepts/salami-collusive-memory-poisoning.md`
14. **OpenART agent RT (K237)** — `@entities/tools/openart.md` (AGPL lab only)
15. **AirKey PIN side channel (K242)** — `@concepts/airkey-wifi-acoustic-pin-sidechannel.md`  
    Nearby Wi-Fi + cheap mic can target PIN entry without joining the WLAN. Owned-lab / physical scope only; hygiene + shield PIN entry.
16. **Adaptive TTS sampling (K243)** — `@concepts/adaptive-fuzzy-test-time-sampling.md`  
    On path A vLLM: do not burn a fixed best-of-N on every query — scale samples with hardness/confidence. Wi-Fi expert-sharding (K241) is usually irrelevant on NVLink/PCIe boxes.

Operator hub: `@concepts/operator-lab-playbook.md`
