---
title: Friend operator lab playbook — start here
type: brief
target: hands-on
created: 2026-08-02
updated: 2026-08-25
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
| **Harness host only** | `cemini23/agent-toolkit` (`~/Projects/agent-toolkit`) | Private | Scripts: `claude-ds`, `route-task`, `adopt-route-always-approve` — **not** TipDrop product ops. TipDrop workspace-kit is redirect-only (retired 2026-08-08). |

**Install (kit umbrella):** from `~/Projects/agent-toolkit` run `pwsh -File ./scripts/adopt-route-always-approve.ps1`. Federation wiki clone helper may still live on TipDrop kit as a redirect; day-1 Cursor paste (`briefs/2026-08-05_friend-day1-cursor-goal-paste.md`) still mentions the kit historically — use agent-toolkit as the live host.

**Day-1 laptop (not the lab box):** Remote call setup — follow tracked **`briefs/2026-08-05_friend-day1-cursor-goal-paste.md`** (PART A manual checkboxes → paste PART B `/goal` into Cursor Agent). Outcome: kit + Cyber + OSINT + `claude-ds` + route + skills/MCP + `friend-day1-cheatsheet.md`. Skip Ollama/Flash weight pulls until path A hardware exists.

**OSINT OPSEC reading order** (skip PM/HL bots, ICE/tickers, TipDrop compliance unless a cyber page cross-links):

1. `@osint-wiki/entities/tools/fingerprint-suite.md` — browser fingerprint gen/injection  
2. `@osint-wiki/entities/tools/octobrowser.md` — profile / antidetect separation  
3. `@concepts/hardware-id-masking-opsec.md` — **host** HWID / MAC / TPM layers (Cyber; not the same as browser fingerprints)  
4. `@osint-wiki/entities/tools/arkham-intelligence.md` — what on-chain attribution looks like from the outside  
5. `@osint-wiki/entities/tools/mitre-atlas.md` — AI-system adversarial taxonomy  
6. `@osint-wiki/entities/tools/cua.md` — agent sandbox patterns (pairs cyber `@concepts/agent-vm-sandboxing.md`)  
7. OSINT `CLAUDE.md` Phase-0 habit — don’t trust README `curl\|sh`; pairs cyber K220 hard stops  

**Lab OPSEC that stays in Cyber** (read with §1–2, not as OSINT substitutes): `@concepts/agent-vm-sandboxing.md`, `@concepts/system-hardening.md`, `@entities/tools/iron-proxy.md`, `@concepts/local-abliterated-llm-pentest-stack.md` (loopback-only), `@concepts/hardware-id-masking-opsec.md` (identifier layers; OS MAC rand is necessary not sufficient; no HWID-spoofer kits).

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


### Deep-research add-ons (2026-08-11)

- **K265 Blast Radius** — long Cursor/agent sessions: prefer reversible bury of concluded missions + recurring build/test chatter over lossy summarization; no unvetted Chalk fork install. See `@concepts/blast-radius-reversible-context-eviction.md`.
- **K266 ShieldAI** — before stocking another OSS eval/guardrail scanner, open `raw-sources/repos/ShieldAI` matrices; expect governance/legal gaps tooling cannot close. See `@concepts/taxonomy-driven-oss-ai-risk-mitigation.md`.
- **K268 SHE (harness hygiene)** — before editing a prod Cursor/Claude harness, **name the owning artifact** (System Prompt / Rule Bank / Safety Memory / Tool Policy) and make the edit artifact-local; HITL + rollback before mutating a live harness; `.local/adopts/SHE` Apache-2.0 REFERENCE only — do not unattended auto-evolve. See `@concepts/safety-harness-evolution.md`.
- **K269 Taboo (refusal-surface audit)** — for any local abliterated / low-refusal lane you ship: mask the top refusal tokens at decode; if policy-violating output appears immediately, alignment is shallow top-token preference, not latent safety. Keep it a scoped eval, not a pass/fail bench. See `@concepts/decoding-level-taboo-diagnostic.md`.
- **K267 ILL (audio lane only)** — only if your box runs audio-enabled LLM lanes (LALM/speech-to-text-first): inaudible 5–20 Hz audio is a real red-team surface; deploy DRG requery on spectral shift. Authorized acoustic lab only, owned devices. See `@concepts/inaudible-low-frequency-audio-attacks.md`.

### Deep-research add-ons (2026-08-12)

- **K271 REDAgentBench (agent ASR discipline)** — for any agent-safety claim on the lab box: never quote a bare attack-success number; report `(harness, judging configuration, evaluation cue, judge backbone)` and verify harm from **service receipts / final-state diffs**, not the transcript (transcript-only judging missed 7.7–11.7 pp and re-labeled 13–21% of rollouts). If an agent *states the rule then violates it* (Recognition–Execution Gap, ~18% of confirmed violations), wire an **action-time policy reminder** at the action boundary (>70 pp confirmed-violation cut in replay). See `@concepts/faithful-agent-asr-measurement.md`.
- **K270 GFlowNet attack-gen (lab-only)** — if you want automated, diversity-preserving LLM attack generation in the lab: GFlowNet attacker–victim–evaluator beats reward-max RL on attack diversity; report ASR **with the evaluator classifier** (swapping Qwen3Guard ↔ LlamaGuard flipped which attacker "won"). Authorized victims only; no public code → pattern REFERENCE. See `@concepts/gflownet-automated-redteam-attack-generation.md`.
- **K272 Cross-lingual safety (eval scope)** — English-only safety eval ≠ low-resource-language safety (English refusal signal retains <10% in Twi/Hausa/Amharic/Swahili on 7B–8B models). If you deploy any local model to non-English users, eval in the target languages with **culturally localized** prompts, not literal translations; probing refusal directions needs weights (not API-only). See `@concepts/cross-lingual-safety-transfer-lrl.md`.

### Deep-research add-ons (2026-08-13)

- **K276 withhold contract (harness guardrail)** — for any agent lane that must *refuse a capability it has* (e.g., a coding agent that must not self-complete a sensitive action): enforce withholding as a **per-turn machine-checkable contract**, not a prompt — binding decision in a **non-LLM policy core fed only trusted state** (injection-proof + unit-testable), a **deterministic detector** for the forbidden output that outranks the model, and a **collusion-resistant judge** on risky turns. Calibrate with a reason-capturing loop (scripted personas → stronger auditor; record each rejection's reason — violations descend a gross→subtle ladder). Treat **over-blocking as a measured failure**; HITL before mutating a prod harness. See `@concepts/refusal-under-knowledge-withhold-contract.md`.
- **K277 RSM (tool coordination)** — when you run several LLM tools on the box (Claude Code + Ollama local + a CLI), assign each an **explicit capability-matched role** and enforce scope boundaries; unplanned role drift (one tool silently absorbing another's job) is a coordination failure driven by absent scope boundaries + functional overlap + context-switch inertia. Prompt hardening: **explicit negative constraints** ("DO NOT run tools / create the file") for pure-content tasks. See `@concepts/role-specialization-multi-tool-coordination.md`.
- **K275 AInf (product-pentest only)** — if a product under test has BLE or Wi-Fi Direct reconnection pairing: allowlist Association-Inference is the privacy failure class to check — any **distinguishable condition response** (ok/err, plaintext status, silent-discard, plaintext replay-counter echo) lets an observer infer device association + location via replay/relay. Mitigation pattern: condition-oblivious responses + fresh-session-key replay resistance + distance bounding. Authorized test devices only. See `@concepts/association-inference-attack-wireless.md`.

### Deep-research add-ons (2026-08-14)

- **K278 ATOBench (agent-verification discipline)** — for any agent claim you evaluate on the lab box (LLM agent, coding agent, automation): do **not** trust activity or a confident report as verification. An agent can stay busy (repeat probes, produce a plausible report) after its **evidence chain** has broken — in ATOBench's SQLi contract, deceptive observations added a median **14 actions + 9 repetitions** yet *no* route restored a supported finding, while JWT kept 44/45 supported reports when primary evidence survived to the report. Score **activity and grounded verification separately**; for agent-produced conclusions, ask whether the claim traces to source-level evidence, not just the transcript. Authorized-lab framing only. See `@concepts/atobench-verification-chain-deception.md`.
- **K281 E2EE vault (product choice)** — if you're choosing an E2EE cloud for personal files/photos or auditing one: ente (Photos/Auth/Locker, Cure53/Symbolic/Fallible audited, AGPL self-host) is the reference for the **zero-knowledge + recovery-key + share-gating** UX. Remember zero-knowledge is about the *server*, not the system — client compromise, **recovery keys**, share-link recipients, and metadata are still surfaces; E2EE ≠ deniable storage. If you self-host a vault, design **recovery** (offline bearer key, multi-device re-registration) as the critical identity surface. See `@entities/tools/ente.md` · `@concepts/e2ee-consumer-cloud-threat-model.md`.

### Deep-research add-ons (2026-08-20)

- **K295 Fool's Gold (abliterated lab)** — refusal-strip does not certify the answer. Do not ingest safety-removal recipes. See `@concepts/decoy-hardening-open-weight-abliteration.md`.
- **K296 Trusted Workflow Relays** — product-pentest owned/written-scope email/M365 only; SPF/DKIM/DMARC pass ≠ send-authorization. See `@concepts/trusted-workflow-relay-email-abuse.md`.
- **K242 BloodBash** — Extract-only on already-collected authorized SharpHound JSON; OSINT shelf; no path payloads. See `@entities/tools/bloodbash.md`.
- **K241 bbot** — AGPL isolate; authorized-target recon only; never vendor Atto. See `@entities/tools/bbot.md`.
- **Rule-blindness** — guard verdict ≠ stated rule until a crossed-rule test. See `@concepts/compliance-detector-rule-blindness.md`.

### Deep-research add-ons (2026-08-15)

- **Skill misevolution (do not auto-evolve skills)** — a "successful" trajectory can write an unsafe shortcut into a persistent skill; later clean sessions retrieve it after the original attack is gone. HITL on *write* does not cover *retrieval-time* harm. Score authoring / retrieval / execution separately; prefer delete-only repair + retirement after evidenced harmful reuse. **No unattended auto-evolve** of `.cursor/skills/*`. See `@concepts/skill-misevolution.md`.
- **HARD defense loop (lab harness only)** — improve runtime defenses from failed attack traces: gate only high-confidence, low-FP, pre-execution-matchable action shapes; else evolve policy. Held-out eval; over-restriction is a failure. HITL + rollback before mutating a live Cursor/Claude harness. See `@concepts/self-evolving-runtime-defense.md`.
- **Scraper / RustScan (owned lab only)** — CyberScraper-2077 and RustScan live on the OSINT shelf; do **not** re-clone here. Use only against written-scope / owned targets; RustScan still hands interesting ports to nmap. See `@entities/tools/cyberscraper-2077.md` · `@entities/tools/rustscan.md`.
- **Labels ≠ endpoints (when you read an ASR)** — a security-eval "attack" label is a claim over treatment bytes, executed behavior, authorization, outcome rule, and analysis unit. Campaign counts are not population rates or defense-efficacy. Pair with ATOBench: activity ≠ verification. See `@concepts/measurement-integrity-mcp-security-eval.md`.
- **InterSAGE (identity for federated agents)** — if you ever expose solver/MCP callers across machines: bind developer × package × operator × deployment independently (Agent Identity Card); treat skill/tool ads as provenance-checked credentials, not grants. See `@concepts/intersage-trust-native-ioa-protocol.md`.

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
- `@concepts/decoy-hardening-open-weight-abliteration.md` (K295)
- `@concepts/trusted-workflow-relay-email-abuse.md` (K296)
- `@entities/tools/bloodbash.md` (K242 Extract)
- `@entities/tools/bbot.md` (K241 AGPL Extract)
- `@concepts/compliance-detector-rule-blindness.md`
- `@concepts/task-conditioned-excess-authority.md` (CCC K290 ≠ CHIVE)
- `@concepts/inadvertent-context-leakage.md` · `@concepts/agent-runtime-identity-adr.md` · `@concepts/agent-safety-executable-evaluation.md` · `@concepts/committee-certified-rag-provenance.md` · `@concepts/llm-generated-dependency-breaking-tests.md` (K298–K300, 2026-08-21)
- `@concepts/buffer-overflow.md` · `@concepts/threat-hunting.md` · `@entities/certifications/ecppt.md` (Joas deep-reads; egress 2026-08-03)
- `@concepts/toktier-exact-stateful-tokenization.md` · `@concepts/stair-hierarchical-repair-plans.md` (K235/K234)
- `@entities/tools/piminer.md` · `@concepts/gradient-immunity-malicious-finetune.md` · `@concepts/trident-agentic-drl-defense-redteam.md` (K248/K246/K244)
- `@concepts/aria-instruction-backdoor-redteam.md` · `@concepts/post-training-adaptation-taxonomy.md` · `@concepts/harnessopt-bench.md` (K249/K250/K252)
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
- `@concepts/audio-grounded-lalm-redteaming.md` · `@concepts/evolving-attack-skill-libraries.md` · `@concepts/planner-state-integrity-embodied-agents.md` · `@concepts/tripwire-safety-neuron-clamp.md` (2026-08-18)
- `@entities/tools/black-cat.md` · `@entities/tools/cloakquest3r.md` · `@entities/tools/raccoon.md` · `@entities/tools/damn-vulnerable-drone.md`
- `@concepts/safety-harness-evolution.md` · `@concepts/decoding-level-taboo-diagnostic.md` · `@concepts/inaudible-low-frequency-audio-attacks.md` (K268/K269/K267; briefs 2026-08-11_k26*)
- `@concepts/faithful-agent-asr-measurement.md` · `@concepts/gflownet-automated-redteam-attack-generation.md` · `@concepts/cross-lingual-safety-transfer-lrl.md` (K271/K270/K272; briefs 2026-08-12_k27*)
- `@concepts/hardware-id-masking-opsec.md` (2026-08-12 ingest — identifier layers; MAC rand ≠ unlinkability; no HWID-spoofer kits)
- `@concepts/hardware-bound-identity-anticheat-licensing.md` (2026-08-12 — AC/licensing identifier map for **owned** product / written-scope lab; not third-party unban)
- `@concepts/software-license-binding.md` · `@concepts/anti-tamper-protection-classes.md` · `@concepts/mobile-app-attestation.md` (2026-08-12 — license-bind / anti-tamper / CI stack / mobile attestation; own product only, no kits)
- `@concepts/metadata-traffic-analysis-anonymity.md` · `@concepts/censorship-circumvention-pluggable-transports.md` · `@concepts/commercial-spyware-stalkerware-defense.md` · `@concepts/account-recovery-deanonymization.md` (2026-08-12 — OPSEC/anonymity/product-defense batch; defense + freedom-of-information framing; no kits)
- `@concepts/endpoint-encryption-deniable-storage.md` · `@concepts/product-build-integrity-slsa-sigstore.md` · `@concepts/secure-boot-vs-device-ownership.md` (2026-08-12 — FDE/deniable classes, SLSA/sigstore build integrity, Secure Boot vs ownership; architecture only, no kits)
- `@concepts/hardened-alternative-operating-systems.md` · `@entities/tools/grapheneos.md` · `@entities/tools/qubes-os.md` (2026-08-12 — GrapheneOS / Qubes / Whonix / Kicksecure / Tails landscape; Pixel-only Graphene; no flash kits)
- `@concepts/skill-misevolution.md` · `@concepts/self-evolving-runtime-defense.md` · `@entities/tools/cyberscraper-2077.md` · `@entities/tools/rustscan.md` (2026-08-15 brief-sync — no unattended skill evolve; HARD lab-only; owned-lab scraper/scan)
- `@concepts/measurement-integrity-mcp-security-eval.md` · `@concepts/intersage-trust-native-ioa-protocol.md` · `@concepts/atobench-verification-chain-deception.md` · `@entities/tools/ente.md` (labels ≠ endpoints; InterSAGE identity; ATOBench verification chain; E2EE vault steal)
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
17. **PIMiner PI red team (K248)** — `@entities/tools/piminer.md`  
    MIT lab clone ~28MB under `raw-sources/repos/PIMiner`. Written scope + owned agents only; dual ASR; Claude Code CLI is a **human gate** — ask before host install. Pair with OpenART (AGPL) for agent RT, not as always-on.
18. **Gradient Immunity (K246)** — `@concepts/gradient-immunity-malicious-finetune.md`  
    Complementary to DataShield: subspace gates at open-weight release. Path A abliterated stacks intentionally weaken refusal — do not expect USG without provider tooling. No clone (empty / no LICENSE).
19. **Trident DRL-defense RT (K244)** / **HoRFFI (K245)** — light: adaptive red vs DRL cyber defenses (REFERENCE); high-openness RFFI if you do RF auth labs. Chiplet/LLM-EDA survey (K247) desk only unless you touch RTL (then CWEEP).
20. **ARIA instruction-backdoor RT (K249)** — `@concepts/aria-instruction-backdoor-redteam.md`  
    Customized coding assistants (system-prompt platforms) need instruction-backdoor red team — score stealth + clean utility + ASR. Lab/written-scope only; no public ARIA code yet.
21. **Post-training taxonomy (K250)** — `@concepts/post-training-adaptation-taxonomy.md`  
    When documenting path-A abliteration / FT / unlearning, use the six axes. Pair with DataShield + Gradient Immunity.
22. **HarnessOpt (K252)** — light: do not unbounded auto-optimize your agent harness; keep HITL + rollback (`@concepts/harnessopt-bench.md`). NL→LTL (K251) only if you formalize security requirements.
23. **Hardware ID / OPSEC (2026-08-12)** — `@concepts/hardware-id-masking-opsec.md`  
    Inventory identifier **layers** (firmware / TPM / MAC / OS install / browser / RF). Turn on OS MAC randomization; do **not** install HWID-spoofer kits. Isolation (Tails session / disposable VM) beats in-place spoof. Hands-on: `briefs/2026-08-12_hardware-id-opsec-checklist.md` (gitignored OK).
24. **Own license / anti-cheat bind (2026-08-12)** — `@concepts/hardware-bound-identity-anticheat-licensing.md`  
    If you ship a license or AC on **your** product: bind to a multi-field hardware hash (OA3-style), not a single registry GUID; treat boot-start kernel AC as a different load-order class than demand-start; Vanguard On-Demand still uses TPM EK + driver attestation. Written scope before touching any third-party AC. Do **not** install HWID spoofers to unban someone else's title — Epic pled that as DMCA circumvention (`Epic v. Araujo`).
25. **License bind + mobile attestation (2026-08-12)** — `@concepts/software-license-binding.md` + `@concepts/mobile-app-attestation.md` (+ `@concepts/anti-tamper-protection-classes.md`)  
    For **your** product's license: bind to **≥2** of {account, device hash, TPM/attestation, online lease} — never a single registry GUID — and document a re-bind path the way Autopilot does. For **your** mobile app: Play Integrity (Android) + App Attest (iOS) verdicts must be verified **server-side**; never trust a client bool; don't cache verdicts (proxying). Anti-tamper is a class problem (integrity checks / packing / virtualization / server authority), not a brand problem. Out of scope: keygens, unpackers, DRM bypasses — architecture only, no kits.

26. **OPSEC / anonymity / product defense (2026-08-12)** — `@concepts/metadata-traffic-analysis-anonymity.md` + `@concepts/censorship-circumvention-pluggable-transports.md` + `@concepts/commercial-spyware-stalkerware-defense.md` + `@concepts/account-recovery-deanonymization.md`. Tor hides the path, **not the metadata** — an AS/global observer still links circuits by timing/volume (Murdoch & Danezis); MAC rand / VPN ≠ unlinkability. Blocking (DPI/IP) is a different threat than traffic confirmation: Snowflake / obfs4 / WebTunnel are *censorship* tools for users in hostile networks, not crime tools. Mercenary spyware + stalkerware are **endpoint compromise**, not a Tor failure — if you're at high threat: Lockdown Mode on; run Amnesty MVT before re-trusting a device; assume disk/mic/certs burned and replace hardware on high-confidence infection. Anonymity dies at **account recovery**: dedicated numbers/emails are identity, no SMS 2FA on high-value lanes, hardware keys; and for **your product**, test the recovery flow as an authz-bypass class (every alternate way in: phone, email, SSO, passkeys, backup codes). No kits — this is the defense side.

27. **Endpoint encryption + build integrity + device ownership (2026-08-12)** — `@concepts/endpoint-encryption-deniable-storage.md` + `@concepts/product-build-integrity-slsa-sigstore.md` + `@concepts/secure-boot-vs-device-ownership.md`. FDE (BitLocker/FileVault) protects the **lost disk**, not the running OS — TPM-only unlock self-unlocks, so "we encrypted the disk" is not "our secrets are safe." The deniable-storage class (hidden volume) exists to answer a **coerced password** and has real limits: it does not beat a live implant on the device, and it does not hide that encryption exists. For **your product**: sign release artifacts and verify on the update path (SLSA L2 provenance + Sigstore keyless + reproducible builds) — client anti-tamper is useless if the shipped binary isn't the built binary; that's a separate layer from npm dependency pinning. Product policy: STRONG attestation (Play Integrity / Secure Boot / Vanguard Pre-Check) excludes rooted / custom-ROM / dual-boot owners — pick a lane (lock STRONG vs allow custom at lower trust) and document the user-freedom cost. Operator: Secure Boot + TPM on for the daily driver; written-scope lab exceptions. No kits — no hidden-volume how-tos, no Secure Boot / DSE / Magisk bypass.

28. **Hardened alternate OSes (2026-08-12)** — `@concepts/hardened-alternative-operating-systems.md` + `@entities/tools/grapheneos.md` + `@entities/tools/qubes-os.md`. "Graphine" = **GrapheneOS**: Pixel-only official production, relock the bootloader (unlocked = incomplete install), sandboxed Play optional, exploit mitigations (hardened_malloc / MTE) — **not** anonymity and **not** Play Integrity STRONG. Desktop secrets: **Qubes** (contain compromise). Tor-forced: **Whonix** (Kicksecure + Gateway/Workstation); Kicksecure alone is hardening without Tor. Leave-no-trace session: **Tails**. Kali is the pentest suite, not a high-assurance daily driver. If **your** app must serve Graphene users, do not binary-deny on STRONG. No unofficial non-Pixel "Graphene" ports; no flash runbooks.

29. **Audio LALM RT + evolving attack skills + planner-state (2026-08-18)** — `@concepts/audio-grounded-lalm-redteaming.md` (ARENA K282; pairs ILL; owned devices only) · `@concepts/evolving-attack-skill-libraries.md` (JailbreakSkill K283; lab eval only; do not auto-evolve `.cursor/skills`) · `@concepts/planner-state-integrity-embodied-agents.md` (ESTI K288; treat env-state as untrusted; P-ASR ≠ E-ASR) · `@concepts/tripwire-safety-neuron-clamp.md` — **do not** neuron-clamp path-A abliterated models without HITL; no 27B GGUF dump. CHIVE (`@entities/tools/chive.md`) is explanation-eval, not a pentest tool.
30. **Fool's Gold vs abliteration + email-relay scope + BloodBash/bbot (2026-08-20)** — `@concepts/decoy-hardening-open-weight-abliteration.md` (K295): abliteration removes refusal, **not** truth — do not treat fluent post-strip answers as verified; no safety-removal recipes. `@concepts/trusted-workflow-relay-email-abuse.md` (K296): product-pentest **owned tenant / written scope only**; SPF/DKIM/DMARC pass ≠ send-authorization; no live phishing. `@entities/tools/bloodbash.md` (K242) Extract-only on already-collected authorized SharpHound JSON (OSINT shelf, no re-clone; no path payloads). `@entities/tools/bbot.md` (K241) **AGPL isolate** — authorized-target recon only; never vendor into Atto/prod; no mass internet scan. Bonus: `@concepts/compliance-detector-rule-blindness.md` — guard verdict ≠ stated rule until a crossed-rule test.

31. **Inadvertent context leakage + tool-layer secrets + TrustRAG + BreakGuard (2026-08-21)** — `@concepts/inadvertent-context-leakage.md` (K298): **never put vault/API secrets in model context when the completion can leave the box** (email drafts, Slack, PR bodies, "write a paragraph with numbers") — benign outputs are covert channels even under refusal (2-digit near-perfect; 4-digit 82% on Opus 4.6); prefer **tool-layer grants that never return the secret to the model** (1Password pattern). `@concepts/agent-runtime-identity-adr.md` (K298): ADR telemetry + SPIFFE `act=agent` (`sub=human`/`act=agent`, short-lived SVIDs, no standing key on disk) + Cloudflare task-scoped access/Trust Ratchet as the detection/identity side; SecPro: automate **gather**, not **decide**. `@concepts/committee-certified-rag-provenance.md` (K299): RAG ranking/provenance is an integrity boundary — schema-valid chunks ≠ authenticated; pin corpus version + ranking inputs for replay. **Name collision: not Zhou/HuichiZhou TrustRAG (2501.00879).** `@concepts/llm-generated-dependency-breaking-tests.md` (K300): LLM dependency tests are **candidates, not a merge gate** (30.3% BUMP BCs; crash-type > behavioral; human review before update gate). **Name collision: not ProgrammerNomad BreakGuard.**

32. **CLAUDE.md-deny gap + PsychJail lab-only + safety-FT + BT-NFT scope + LLM-compliance HITL (2026-08-25)** — `@concepts/nl-security-rules-vs-builtin-deny.md` (K303): **a prose security rule in CLAUDE.md / AGENTS.md / `.cursor/rules` is not a control** — only ~4–16% of real rules match a built-in deny/permission/sandbox control (strict 4.4%, CI 2.6–6.7%); write rules so a **deterministic control** (PreToolUse deny, permission rules, sandbox) enforces them, **never put secrets in NL rules only**, and treat rule-writing as needing an explicit verification step. `@concepts/psychological-multiturn-jailbreaks.md` (K302): interactive LLM deployments are social-engineering surfaces — refusal is **not turn-stable** (PsychJail avg ASR 87.3%); test guardrail verdicts across turns, not per-message; **authorized lab only, no persuasion scripts in the wiki**, repo NO-GO (null SPDX + ~2GB). `@concepts/conditional-safety-adapter-routing.md` + `@concepts/reasoning-induced-misalignment.md` (K301/K304): a global safety LoRA/SFT is **not** a proof of safety (alignment tax), and fine-tuning on *harmless* reasoning data can itself weaken safety (RIM, Qwen2.5-3B/7B) — re-run safety evals after any fine-tune; no clamp recipes. `@concepts/bluetooth-nft-soft-pairing.md` (K305): pairing ≠ authorization — test the service-auth decision point + revocation path on **owned devices only**; no LIVE pairing manipulation. `@concepts/llm-generated-compliance-artifacts.md` (K306): LLM compliance artifacts (DPIA/DPP) are **candidates, not deliverables** — strict formats hallucinate more, vague standards need more context; HITL required; private data stays off third-party APIs.

Operator hub: `@concepts/operator-lab-playbook.md`
