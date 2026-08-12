---
title: "REDAgentBench — executable red teaming + faithful ASR measurement (arXiv 2608.10669)"
type: source
tags: [source, arxiv, agent-security, red-team, benchmark, faithful-measurement]
keywords: [2608.10669, REDAgentBench, ASR, exposure-execution-observation-adjudication, Recognition-Execution Gap, IVC, trajectory-state-hybrid judge, service sandbox]
related:
  - concepts/faithful-agent-asr-measurement.md
  - entities/tools/redagentbench.md
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/agent-data-injection-attacks.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — benchmark not yet released (no public repo at Phase-0; harnesses in paper are third-party Codex/Hermes/OpenClaw). K271 lab-redteam + agent-audit wires."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc + cemin-cybersec-agent-audit.mdc (K271)"
---

**Briefs:** `briefs/2026-08-12_k271-redagentbench-faithful-asr.md`

## Relations

- @concepts/faithful-agent-asr-measurement.md
- @entities/tools/redagentbench.md
- @concepts/agent-runtime-guardrails.md
- @concepts/ai-redteam-evidential-ceiling.md
- @concepts/agent-data-injection-attacks.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | REDAgentBench: Executable Red Teaming and Faithful Measurement of LLM Agent Systems |
| Authors | Zixing Chen (Fudan), Xingyuan Liu (HKUST), Jie Zhu, Huaixia Dou, Shuo Jiang, Lifan Guo, Feng Chen, Chi Zhang (Qwen DianJin Team, Alibaba Cloud), Junhui Li (Soochow) |
| arXiv | 2608.10669 |
| Code | None found at Phase-0 (no public REDAgentBench repo; paper cites third-party harnesses Codex/Hermes/OpenClaw) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.10669-redagentbench-executable-red-teaming-and-faithfu.pdf` |
| Retrieved | 2026-08-12 |
| Read status | read (9 pp) |

## Narrative

REDAgentBench is an **executable** agent red-teaming framework that treats the sandbox as a measurement instrument. Attacks are derived from explicit safety constraints + agent-system vulnerabilities, run in isolated service sandboxes, and verified from **service receipts and final-state changes** rather than the agent's own claims.

**Structure:** 1,661 executable cases across 5 service surfaces, 15 intervention strategies, 11 vulnerability types, 28 constraints — organized by an intervention–vulnerability–constraint (IVC) taxonomy.

**Faithful measurement:** reported ASR is decomposed into four stages — **exposure** (does an intervention reach the agent?), **execution** (what does the agent actually do?), **observation** (which evidence is available?), **adjudication** (how is evidence mapped to a label?). A Trajectory–State–Hybrid (2+1) judge system shares one judge backbone but applies view-specific proof contracts.

**Key results (6 models × 3 harnesses: Codex / Hermes / OpenClaw):**
- Macro-average ASR **65.69%**; per-cell ASR swings widely (e.g. Qwen-plus 40.62%→95.00% across harnesses on one surface; GLM-5.2 43.62% lowest, Qwen-plus 81.74% highest). Model **rankings reverse across harnesses** — a single-harness ASR is insufficient.
- State judge reports ASR **+7.73–11.72 pp** higher than trajectory judge and flips 12.97–21.20% of paired labels (all six models significant, exact McNemar p≤6.54e-5); 23/64 slices contain strict pairwise reversals (43 inversions).
- **Evaluation awareness:** disclosing an authorized mock-eval context lowers ASR by 6.59 (Qwen3.7-plus) and 4.77 (Qwen3.5-plus) pp — but not uniformly (OpenClaw/T4 moves opposite). Evaluation cue must be reported as a variable.
- **Recognition–Execution Gap (REG):** of 2,846 resolved state-confirmed violations, 17.92% (broad) / 5.48% (strict) occur after the agent *stated the applicable constraint* — the rule is in its own pre-action text but does not control execution. Concentrated in evidence-ambiguity attacks (data/RAG poisoning 50.64%, authority pressure 37.79%, tool-output tampering 36.59%, workspace-file poisoning 32.14%).
- **Training-free action-time defense:** replaying harmful cases with a case-specific policy reminder cuts ASR by **74.19 pp** on the 510-case Qwen-plus cohort (88.25%→14.06%), preventing 368/434 baseline harmful executions.
- Human judge audit: 91.94% reviewer agreement (κ=0.838), precision 97.84%, recall 91.27%; raw judged ASR 55.43% vs human-audited 59.42%.

`[CONFIRMED]` — headline numbers from paper tables; no local repro (benchmark not yet released).

## Snippets

> We therefore treat the executable environment not merely as a sandbox for running attacks, but as a measurement instrument. In our framework, reported ASR emerges through four stages: exposure determines whether an intervention reaches the agent; execution captures what the agent actually does in the environment; observation determines which trajectory or state evidence is available; and adjudication maps that evidence to a label. [Source: arXiv:2608.10669 §1]

> A training-free policy reminder reduces confirmed violations by more than 70 percentage points in matched replay. [Source: arXiv:2608.10669 abstract]

## Dead Ends

- No public benchmark repo at Phase-0 → **REFERENCE**; cannot reproduce the matrix in-lab yet. Re-check for a GitHub release; harnesses cited (Codex CLI, Hermes Agent, OpenClaw) are third-party, not the benchmark itself.
- Headline ASR is API-model-dependent (GPT-5.2, Qwen3.x-plus, KIMI-2.6, GLM-5.2) — a local repro would need API keys and the three harnesses; expensive, defer.
- Policy-reminder defense is a replay probe, not a full-benchmark estimate; reminders cannot replace hard access controls.
