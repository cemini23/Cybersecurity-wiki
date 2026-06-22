---
title: Agent runtime guardrails — attack surfaces + enforcement paradigms
type: concept
tags: [methodology, agent-security, guardrail, mcp, prompt-injection, runtime-enforcement, formal-methods]
keywords: [agent guardrail, authority confusion, permission laundering, sleeper attack, epca, airguard, chaincaps, adaptive attack rate, tool composition safety]
related:
  - concepts/ai-for-cybersecurity.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/llm-pentest-automation.md
  - concepts/agent-vm-sandboxing.md
  - concepts/agent-skill-injection.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/responsible-disclosure.md
  - entities/tools/llm-defense-lattice.md
  - concepts/seclaw-agent-security-evaluation.md
  - entities/tools/seclaw-eval.md
  - entities/tools/agentredguard.md
  - entities/tools/airguard.md
  - entities/tools/chaincaps.md
  - entities/tools/defenseclaw.md
  - entities/tools/nvidia-skillspector.md
  - entities/tools/iron-proxy.md
  - sources/arxiv-2605-29251-provably-secure-agent-guardrail.md
  - sources/arxiv-2605-28914-airguard-guarding-agent-actions.md
  - sources/arxiv-2605-26542-chaincaps-composition-safe-tool-using-agents.md
  - sources/arxiv-2605-28201-plant-persist-trigger-sleeper-attack.md
  - sources/arxiv-2605-30454-agent-prompt-injection-surface-evaluation.md
  - sources/arxiv-2606-00485-confused-chatgpt-cross-app-context-poisoning.md
  - sources/arxiv-2606-01494-clawhub-security-signals.md
  - sources/arxiv-2606-02240-agentredbench.md
  - sources/arxiv-2606-02302-seclaw-spec-driven-agent-security.md
  - sources/arxiv-2606-02822-owasp-llm-defense-attribution.md
  - sources/arxiv-2606-05252-bas-to-siem-detection-as-code-synthesis.md
  - sources/arxiv-attested-tool-server-admission-2605.24248-2026-06-05.md
  - sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md
  - sources/arxiv-mcp-description-code-inconsistency-2606.04769-2026-06-05.md
  - sources/arxiv-2606-06387-webmcp-tool-surface-poisoning.md
  - concepts/mcp-security-posture.md
  - concepts/docker-agent-sandbox-allowlist-proxy.md
  - sources/arxiv-zero-apt-llm-pentest-2606.05567-2026-06-05.md
  - sources/arxiv-2606-04990-agent-traces-evidence-provenance.md
  - concepts/agent-execution-provenance.md
  - sources/arxiv-2606-07131-malskillbench-runtime-verified-malicious-skills.md
  - sources/arxiv-2606-07943-poise-position-aware-skill-injection.md
  - entities/tools/malskillbench.md
  - sources/arxiv-2606-09084-context-fractured-decomposition-attacks.md
  - sources/arxiv-2606-10749-toward-secure-llm-agents-survey.md
  - concepts/context-fractured-decomposition-attacks.md
  - sources/arxiv-2606-07992-vats-error-path-mcp-injection-2026-06-13.md
  - sources/arxiv-2606-12797-agentic-containment-gap-framework-audit-2026-06-13.md
  - concepts/agentic-containment-principles.md
  - sources/arxiv-2606-10322-game-theoretic-multi-agent-context-control-gt-mcp.md
  - concepts/trajectory-context-control.md
  - sources/arxiv-2606-12835-internet-of-agentic-ai-communication-coordination.md
  - concepts/internet-of-agentic-ai-ioai.md
  - sources/arxiv-2606-13757-sevra-bench-social-engineering-review-agents.md
  - concepts/llm-code-review-agent-security.md
  - entities/tools/sevra-bench.md
  - sources/arxiv-2606-20023-over-privileged-tool-selection-toolprivbench.md
  - concepts/agent-least-privilege-tool-selection.md
  - entities/tools/toolprivbench.md
  - entities/tools/ecc.md
  - entities/tools/skillgate.md
  - sources/openreview-openclaw-real-world-safety-analysis.md
  - sources/arxiv-2606-20510-efficient-sound-probabilistic-verification-ai-agents.md
  - concepts/agent-probabilistic-datalog-verification.md
  - sources/arxiv-2606-18673-prompt-leaking-attacks-area.md
  - concepts/system-prompt-leakage.md
  - entities/tools/leakbench-area.md
maturity: draft
created: 2026-06-01
updated: 2026-06-22
---

# Agent runtime guardrails — attack surfaces + enforcement paradigms

## Relations

- @concepts/ai-for-cybersecurity.md — LLM agents in offensive/defensive workflows
- @concepts/llm-adversarial-fuzzing.md — jailbreak/refusal testing vs agent side-effect attacks
- @concepts/llm-pentest-automation.md — Tier-2 agents with MCP tools need runtime guards
- @concepts/agent-vm-sandboxing.md — VM isolation complements but does not replace authority control
- @concepts/crescendo-multi-turn-jailbreak.md — multi-turn jailbreak vs sleeper persist-and-trigger
- @concepts/responsible-disclosure.md — agent guardrail bypass findings follow CVD timelines
- @entities/tools/llm-defense-lattice.md — OWASP LLM Top 10 per-defense attribution (BAS lattice)
- @concepts/seclaw-agent-security-evaluation.md — trajectory eval methodology (SeClaw)
- @entities/tools/seclaw-eval.md — trajectory-aware Docker benchmark (SeClaw)
- @entities/tools/agentredguard.md — SaaS integration-aware guard (AgentRedBench paper)
- @entities/tools/airguard.md — MIT runtime authority guard (AgentTrap / DTAP-150)
- @entities/tools/chaincaps.md — MCP proxy for composition-safe tool chains
- @entities/tools/defenseclaw.md — enterprise agent governance + MCP scanner
- @entities/tools/nvidia-skillspector.md — skill supply-chain preflight
- @entities/tools/iron-proxy.md — egress firewall for agent workloads
- @sources/arxiv-2605-29251-provably-secure-agent-guardrail.md — ePCA / formal guardrail anchor
- @sources/arxiv-2605-28914-airguard-guarding-agent-actions.md — authority confusion
- @sources/arxiv-2605-26542-chaincaps-composition-safe-tool-using-agents.md — permission laundering
- @sources/arxiv-2605-28201-plant-persist-trigger-sleeper-attack.md — sleeper attack
- @sources/arxiv-2605-30454-agent-prompt-injection-surface-evaluation.md — per-surface eval
- @sources/arxiv-2606-01494-clawhub-security-signals.md — layered skill scanners (VT / static / SkillSpector)
- @sources/arxiv-2606-02240-agentredbench.md — dynamic redteam + integration read→write attacks
- @sources/arxiv-2606-02302-seclaw-spec-driven-agent-security.md — spec-driven tasks + trajectory scoring (SeClaw)
- @sources/arxiv-2606-02822-owasp-llm-defense-attribution.md — OWASP LLM defense-family attribution + paraphrase brittleness
- @sources/arxiv-2606-06387-webmcp-tool-surface-poisoning.md — WebMCP mid-session tool injection (MSTI)
- @sources/arxiv-2606-04990-agent-traces-evidence-provenance.md — provenance eval hygiene
- @concepts/agent-execution-provenance.md — accountability layer for guardrail eval
- @concepts/mcp-security-posture.md — MCP trust-boundary layer model
- @sources/arxiv-2606-07992-vats-error-path-mcp-injection-2026-06-13.md — error-path implicit authority (K114)
- @sources/arxiv-2606-12797-agentic-containment-gap-framework-audit-2026-06-13.md — framework containment audit (K114)
- @concepts/agentic-containment-principles.md — P1–P6 structural gates
- @sources/arxiv-2606-10322-game-theoretic-multi-agent-context-control-gt-mcp.md — GT-MCP trajectory context control (Reference)
- @concepts/trajectory-context-control.md — memory-commit gate pattern (CCI/AGR/CDS + rollback)
- @sources/arxiv-2606-20510-efficient-sound-probabilistic-verification-ai-agents.md — probabilistic Datalog + DRO (2606.20510)
- @concepts/agent-probabilistic-datalog-verification.md — noisy-classifier runtime verification layer
- @sources/arxiv-2606-18673-prompt-leaking-attacks-area.md — system prompt leakage measurement + AREA (2606.18673)
- @concepts/system-prompt-leakage.md — LLM07 exfiltration vs injection distinction

## Raw Concept

Synthesized from daily-digest inbox clusters (2026-06-01, 2026-06-02): seven arXiv papers on tool-using agent security — defensive guardrails (ePCA, AIRGuard, ChainCaps, AgentRedGuard), skill supply-chain scanning (ClawHub / SkillSpector), and attack/eval advances (sleeper attack, dual-surface injection, SaaS integration redteam).

## Narrative

Tool-using agents (MCP, shell, APIs, email) shift the security problem from **refusal robustness** to **side-effect authorization**. A step can look benign in isolation yet violate policy in composition or across time. This page clusters 2026 research into failure modes, defenses, and evaluation hygiene for pentest/SOC copilot deployments.

### Failure modes (offensive / red-team lens)

| Mode | Mechanism | Source |
|------|-----------|--------|
| **Authority confusion** | Untrusted docs/MCP/skills *inform* reasoning but must not *authorize* writes, sends, or exec | AIRGuard |
| **Permission laundering** | Each tool call passes local ACL; composed workflow exfiltrates (read → summarize → send) | ChainCaps |
| **Sleeper attack** | Payload persists in session/memory/skills; benign later query triggers harm | PLANT |
| **Dual-surface injection** | Same bytes succeed on tool *output* or tool *description* depending on model | Surface paper |
| **Mid-session tool injection (MSTI)** | Third-party JS mutates WebMCP tool registry during task — hijack (race/AbortSignal) or frame via metadata | WebMCP 2606.06387 |
| **Error-path implicit authority** | Tool **error** JSON triggers corrective mode; adversarial recovery steps bypass skepticism | VATS 2606.07992 |
| **Memory poisoning (architectural)** | Single untrusted write to persistent memory corrupts all subsequent reasoning cycles | Containment gap 2606.12797 |
| **Trajectory steering** | Locally plausible fragments accumulate across turns; accepted outputs update persistent context without drift gate | GT-MCP 2606.10322 |
| **Over-privileged tool selection** | Agent picks broader **authorized** tool when narrow sufficient alternative exists; amplified by transient narrow-tool failures | TOOLPRIVBENCH 2606.20023 |
| **System prompt leakage** | Adversarial query exfiltrates hidden system/skill instructions — API keys, tool rules | LLM07 / 2606.18673 |
| **Semantic decoupling** | Natural-language intent hides unsafe tool args from LLM-as-Judge guards | ePCA motivation |

These are **not jailbreaks** in the classic sense — the model may comply with user intent while attacker-controlled context steers authorized access off-scope. [CONFIRMED] across AIRGuard + sleeper paper framing.

### Defense paradigms (defensive / blue-team lens)

1. **Formal pre-action verification (ePCA)** — SMT/formal constraints on intended actions before execution; maps unsafe transitions to UNSAT deadlocks. Aims for deterministic lower bound under explicit assumptions. `[TENTATIVE]` — lab validation pending; complements not replaces semantic alignment.

1b. **Probabilistic Datalog + DRO (2606.20510)** — when upstream PII/secret/redaction classifiers are noisy and **correlated**, sound upper bounds on policy-violation probability via distributionally robust optimization over Datalog derivation graphs (Praline/Soufflé). Complements ePCA for imperfect predicates; Phase-0 **Reference** until Google artifact ships. See @concepts/agent-probabilistic-datalog-verification.md.

2. **Runtime authority control (AIRGuard)** — Action-time least privilege: task authority → step authority (narrow-only), source/target trust, side-effect simulation, cross-step audit. Prompt-only policy insufficient in paper ablation.

3. **Composition-safe IFC (ChainCaps)** — MCP proxy; sink-specific capability budgets propagate by intersection (monotonic attenuation). Requires **trusted manifests** — naive manifests block only ~27% of attacks in paper.

4. **Stack with existing wiki tools** — @entities/tools/nvidia-skillspector.md (skill preflight), @entities/tools/defenseclaw.md (enterprise governance), @entities/tools/iron-proxy.md (egress), @concepts/agent-vm-sandboxing.md (substrate isolation).

5. **Layered skill governance (ClawHub study)** — On 67k+ OpenClaw skill versions, VirusTotal, static heuristics, and SkillSpector **disagree** (max pair overlap 10.4%; 81.9% of positives from one scanner only). SkillSpector leads on semantic agentic-risk; VT leads on bundled-code malware. **Do not** treat any single scanner as allow/block. [Source: arXiv:2606.01494] `[TENTATIVE]` — automated registry labels, not human ground truth.

6. **Integration-aware guards (AgentRedBench)** — Enterprise copilots with many SaaS integrations: poison via **read** on one app, harm via **write** on another. Chat-trained guards miss tool-response injections; paper’s AgentRedGuard targets that channel. Compare with AIRGuard authority model before adoption. [Source: arXiv:2606.02240] `[TENTATIVE]` — benchmark scenarios via maintainer channel.

### Evaluation hygiene

- Report **per-surface** ASR (tool output vs tool description), not single-channel headline numbers. [Source: arXiv:2605.30454]
- Use **Adaptive Attack Rate (AAR)** = max ASR over surfaces for the model×task cell.
- Test **multi-session** persist targets (memory, skills), not only single-interaction injection. [Source: arXiv:2605.28201]
- Test **multi-tool compositions**, not isolated tool permissions. [Source: arXiv:2605.26542]
- Score **tool trajectories**, not final chat politeness — unsafe intermediate steps can hide behind benign summaries. [Source: arXiv:2606.02302 SeClaw]
- Use **spec-driven task synthesis** for coverage scaling vs static prompt lists alone. [Source: arXiv:2606.02302] `[TENTATIVE]` — local Docker repro pending
- Attribute **per-defense-family** OWASP LLM coverage (refusal vs budget vs full stack), not one aggregate BAS score. [Source: arXiv:2606.02822]
- Test **paraphrase brittleness** on refusal-phrase filters — static jailbreak strings overstate block rate. [Source: arXiv:2606.02822]
- For **browser WebMCP** agents: test mid-session tool list mutation (registration race, description framing) — not only static MCP manifests. [Source: arXiv:2606.06387]
- Score **provenance completeness** (trace + claim attribution), not final-answer politeness alone. [Source: arXiv:2606.04990]
- For **skill packages**: report CI vs PI recall separately; avoid wild-only vendor benchmarks (up to 66-point swing). [Source: arXiv:2606.07131]
- Test **task-verifier-pass + payload-execute** (ASR), not payload alone — POISE-style stealth. [Source: arXiv:2606.07943]
- Test **artifact-mediated cross-session composition** (CFD), not only contiguous multi-turn jailbreaks. [Source: arXiv:2606.09084]
- Report **OPUR/PED** on paired narrow+broad authorized tools; inject transient failures on narrow tier — harm refusal benchmarks do not proxy least privilege. [Source: arXiv:2606.20023]

### Pentest / engagement implications

When assessing client agent copilots: poison both MCP tool descriptions and return payloads; attempt persist-via-memory/skill; chain read+transform+external-send; measure whether guards sit **before** tool execution (AIRGuard/ChainCaps pattern) or only in system prompt.

## Snippets

Defense layering (recommended order for authorized lab):

1. **Layered** skill/MCP scan (static + VT/reputation + SkillSpector-class semantic) — not one gate [Source: arXiv:2606.01494]
2. Egress policy (iron-proxy / VM sandbox)
3. Runtime authority or composition proxy (AIRGuard / ChainCaps-class)
4. Integration/tool-response guard for multi-SaaS copilots (AgentRedGuard-class) `[NEEDS VERIFICATION 2026-06-02]`
5. Formal constraint layer where policy is machine-expressible (ePCA-class) `[NEEDS VERIFICATION 2026-06-01]`

## Dead Ends

- **LLM-as-Judge alone** for high-privilege agents — paper consensus: probabilistic semantic guards lack verifiable lower bound under decoupling attacks.
- **Single-surface ASR** as pass/fail metric — systematically overstates defense and understates attack (Surface paper).
- **Per-tool ACL only** — does not stop permission laundering across composed MCP chains.
- **Single-scanner skill allowlist** — ClawHub data shows high false-negative/positive disagreement across VT, static, and SkillSpector.
- **Refusal-regex-only LLM posture** — OWASP lattice paper: paraphrase drops LLM01/LLM07 block rates 15–25 pp; budget controls more stable.
- **Session-only prompt guards** — K100 SPI paper: 32–42% E2E-ASR when poison persists across session reset (@sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md).
- **Trusting MCP tool descriptions** — 9.93% description–code inconsistency in wild MCP servers; attestation gates admission not semantic honesty (@concepts/mcp-security-posture.md).

### K114 addendum (2026-06-13)

**VATS (2606.07992):** Error-path injection is not a jailbreak — it exploits **operational framing** in tool failure responses. Mean baseline IPI ACR 16.7% vs error seed 50%; post-mutation **100%** on Gemini 3.1 Pro, GPT-5.5, GLM-5.1, Qwen3-Coder. GPT-5.5 **detect-but-comply** profile: flags ~44% of successful attacks yet still executes. Evaluation hygiene: add **error-path mutation** (VATS $M_1$–$M_7$) alongside per-surface IPI and multi-session SPI tests.

**Containment gap (2606.12797):** Runtime guards at **framework layer** (Codex/Gemini CLI) can block raw-model vulnerabilities, but LangChain/AutoGPT/OpenAI SDK ship **zero native P1–P6 compliance**. Deterministic P1 policy gate + P3 memory validator drop corruption/bypass from 1.000 → 0.000 at sub-ms overhead — steal pattern for high-privilege Cemini loops. Complex policies enable **concealed targeted harm** (3–3.5× wrongful denials, stable aggregate accuracy) — monitoring must track subgroup outcomes, not headline accuracy alone.

### GT-MCP addendum (2026-06-15)

**Trajectory context control (2606.10322):** Side-effect guards and SPI write-path governance still leave a gap if **any accepted model output** appends to persistent context without a drift gate. GT-MCP pattern: multi-agent candidates → trust score (causal consistency + agreement − candidate-specific drift) → rollback/quarantine on threshold breach. Paper eval: **0.0%** controller ISR vs **17.8%** single-agent over 500 turns. **Reference** until implementation ships — harness draft at `briefs/2026-06-15_gt-mcp-trajectory-context-control-harness.md`.
