---
title: SEVRA-BENCH — social engineering of vulnerabilities in review agents (arXiv 2606.13757)
type: source
tags: [source, arxiv, benchmark, code-review, supply-chain, social-engineering, mcp, gitea]
keywords: [2606.13757, sevra-bench, pr review agent, cve reversal, framing strategy, refusal rate]
related:
  - entities/tools/sevra-bench.md
  - concepts/llm-code-review-agent-security.md
  - concepts/social-engineering.md
  - concepts/agent-runtime-guardrails.md
  - concepts/llm-vulnerability-discovery.md
  - concepts/mcp-security-posture.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/ai-for-cybersecurity.md
  - concepts/npm-supply-chain-defense.md
  - sources/arxiv-2606-02302-seclaw-spec-driven-agent-security.md
  - sources/arxiv-2606-10749-toward-secure-llm-agents-survey.md
  - sources/arxiv-2606-12835-internet-of-agentic-ai-communication-coordination.md
  - concepts/internet-of-agentic-ai-ioai.md
  - sources/arxiv-2606-30587-cognitive-heuristics-llm-vuln-detection.md
  - concepts/cognitive-heuristics-llm-vuln-detection.md
maturity: draft
read_status: read
created: 2026-06-16
updated: 2026-07-31
phase_0_verdict: "Reference 2026-06-17 — re-audit: LICENSE 404 + GitHub API license null; laptop Docker+inspect-ai eval only after SPDX file"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

## Relations

- @entities/tools/sevra-bench.md — benchmark entity + Phase-0
- @concepts/llm-code-review-agent-security.md — merge-gate threat model synthesis
- @concepts/social-engineering.md — 15 PR framing strategies as automated SE
- @concepts/mcp-security-posture.md — reviewer uses MCP Gitea tool subset

## Raw Concept

| Field | Value |
|-------|-------|
| Title | SEVRA-BENCH: Social Engineering of Vulnerabilities in Review Agents |
| Authors | Rui Melo, Riccardo Fogliato, Sean Zhou, Pratiksha Thaker, Zhiwei Steven Wu |
| Affiliation | CMU; Microsoft Core AI; Amazon AWS; Databricks |
| arXiv | 2606.13757 |
| Artifact | GitHub `rufimelo99/malicious-pr-bench`; HF `RedAI4Code/SEVRA`; paper cites `RedAI4Code/SEVRA` (org repo 404 at Phase-0) |
| Location | `raw-sources/arxiv-2606.13757-sevra-bench-social-engineering-review-agents.pdf` |
| Retrieved | 2026-06-16 |
| Read status | **read** (abstract + construction + Tables 1–2 + limitations) |

## Narrative

Benchmarks **LLM code-review agents as merge gates** when the attacker controls **both the diff and the PR narrative**. Each episode reverses a real **CVE-linked security fix** (`git apply -R` on Secommits records), then wraps the reintroduced vulnerability in one of **15 social-engineering framings** (claims, evidence, urgency, prior approval, authority). Diff is held fixed across framings to isolate **narrative susceptibility** from intrinsic vuln detectability [CONFIRMED].

### Scale

| Release | Count | Notes |
|---------|-------|-------|
| Malicious PRs (deterministic) | 2,250 | 10 CWE Top-25 classes × 15 framings |
| Retained challenge split | **1,062** | PRs where ≥1 baseline (Haiku 4.5 / GPT-5.4-nano) approved |
| Benign security-fix PRs | 347 | False-decline measurement |

Reviewer interacts with **live isolated Gitea** via **MCP/API tools** (diff, file read, search, approve/decline). Optional Docker mode for Claude Code / Copilot / Codex with bash. Eval harness: **inspect_ai**; fresh agent per PR; system prompt is **routine code review** (no explicit security instruction).

### Metrics

- **Refusal rate (RR)** — fraction of malicious PRs not approved (↑ better)
- **Security reason rate (SRR)** — among blocks, fraction citing security (vs incidental decline)

### Headline results (retained challenge split) [CONFIRMED]

| Model class | Overall RR | Notes |
|-------------|------------|-------|
| Claude Opus 4.7 | **98%** | 84–100% across all 15 framings |
| GPT-5.5 | **95%** | Consistent across framings |
| GLM-5 | **83%** | Strong open-weight outlier |
| DeepSeek V4-Flash / Kimi K2.5 / Haiku 4.5 | **52–53%** | High framing variance |
| GPT-5.4-nano | **36%** | Weakest closed-source in set |

**Framing swing (open-weight):** DeepSeek 100% on Appeal to Authority vs **18%** on Prior Approval Signal (82 pp gap). Kimi **14–80%** range across framings.

**Worst framings (aggregate):** Prior Approval Signal, Dependency Compat Claim, Build System Laundering, Unsafe Optimization — exploit authority/automation bias.

### Threat model

Contributor-level adversary; standard PR interface only (branch, commits, title/description, inline comments). Success = approved merge reintroducing documented CVE class.

### vs adjacent evals

| Eval | Question |
|------|----------|
| CyberSecEval / vuln detection | Can model find/fix flaws in code snippets? |
| AgentDojo / prompt injection | Tool/memory hijack in agent tasks |
| **SEVRA-BENCH** | Will reviewer **approve** adversarial PR with real reversed CVE patch? |

## Snippets

> "When an automated reviewer approves a malicious contribution, the failure is not only a missed warning; it can become a software-supply-chain path for landing vulnerable code."
> — [Source: arxiv-2606.13757 §1, retrieved 2026-06-16]

> "The system prompt does not mention security concerns, threat detection, vulnerability classes, or malicious patterns."
> — [Source: arxiv-2606.13757 §3.5, retrieved 2026-06-16]

## Dead Ends

- **Routine-review prompt only for prod merge gates** — paper shows 36–53% RR on weaker models; security-explicit prompts may help but are not evaluated here.
- **RedAI4Code/SEVRA GitHub org repo** — 404 at Phase-0; use `rufimelo99/malicious-pr-bench` + HF dataset instead.
- **Importing benchmark code without LICENSE** — GitHub API reports `license: null` [NEEDS VERIFICATION 2026-06-16].
