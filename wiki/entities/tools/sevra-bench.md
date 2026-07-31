---
title: SEVRA-BENCH — malicious PR benchmark for LLM review agents (Reference)
type: entity
tags: [tool, benchmark, code-review, supply-chain, agent-security, reference, inspect-ai]
keywords: [sevra-bench, malicious-pr-bench, gitea, inspect_ai, redai4code, pr merge gate]
related:
  - sources/arxiv-2606-13757-sevra-bench-social-engineering-review-agents.md
  - concepts/llm-code-review-agent-security.md
  - sources/arxiv-2606-12835-internet-of-agentic-ai-communication-coordination.md
  - concepts/internet-of-agentic-ai-ioai.md
  - concepts/social-engineering.md
  - concepts/agent-runtime-guardrails.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/mcp-security-posture.md
  - entities/tools/seclaw-eval.md
  - entities/tools/defenseclaw.md
  - concepts/ai-for-cybersecurity.md
  - sources/arxiv-2606-30587-cognitive-heuristics-llm-vuln-detection.md
  - concepts/cognitive-heuristics-llm-vuln-detection.md
maturity: draft
created: 2026-06-16
updated: 2026-07-31
phase_0_verdict: "Reference 2026-06-17 — re-audit: LICENSE 404 + GitHub API license null; inspect_ai + Docker Gitea harness; HF RedAI4Code/SEVRA; lab eval only until SPDX file"
wire_status: wont_wire
wire_target: "REFERENCE benchmark"
---

## Relations

- @sources/arxiv-2606-13757-sevra-bench-social-engineering-review-agents.md — paper provenance
- @concepts/llm-code-review-agent-security.md — threat model + metrics
- @concepts/seclaw-agent-security-evaluation.md — complementary trajectory eval (tool actions vs merge decision)
- @entities/tools/seclaw-eval.md — sibling Reference-tier agent benchmark
- @entities/tools/defenseclaw.md — governance scanner; does not replace PR-review robustness eval

**Briefs:** `briefs/2026-06-16_sevra-bench-pr-review-agent-eval.md`, `briefs/2026-07-03_cognitive-heuristics-llm-scanner-redteam-checklist.md`, `briefs/2026-07-03_ci-merge-gate-cognitive-context-hardening-handoff.md`

## Raw Concept

Daily digest ingest (2026-06-16). GitHub: [rufimelo99/malicious-pr-bench](https://github.com/rufimelo99/malicious-pr-bench) (~2 stars, pushed 2026-06-01). Dataset: [Hugging Face RedAI4Code/SEVRA](https://huggingface.co/datasets/RedAI4Code/SEVRA). arXiv:2606.13757.

## Narrative

**Reference-tier** benchmark placing LLM agents as **open-source PR reviewers** on live **Gitea** instances. Malicious samples = **reversed CVE fixes** + **15 social-engineering framings**. Runs via **inspect_ai** with MCP-compatible GitHub tools (`github_approve_pull_request`, diff inspection, repo search).

**Use cases (authorized lab only):**
- Regression-test any LLM merge-gate / Copilot-review / custom PR bot before org-wide rollout
- Compare frontier vs open-weight models on **framing susceptibility** (not just CWE detectability)
- Measure false-decline on benign security-fix PRs (347-sample `benign` split)

**Phase-0 audit (2026-06-16):**

| Check | Result |
|-------|--------|
| LICENSE | **FAIL** — GitHub API `license: null`; raw `LICENSE` 404 (re-audit 2026-06-17) |
| Maturity | Early (2★, 0 forks, 3 open issues) |
| Failure mode | Malicious PR corpus + live approve API — **isolated Docker only** |
| vs wiki stack | Complements SeClaw (tool trajectories) + SkillSpector (install-time); unique **merge-gate** surface |

**CONDITIONAL-GO** after LICENSE lands: laptop subset on retained 1,062 challenge split; no prod Gitea credentials.

**Not** an attack toolkit for unauthorized repos — defensive eval only.

See `briefs/2026-06-16_sevra-bench-pr-review-agent-eval.md` for pre-rollout merge-gate checklist.

## Snippets

```bash
# From malicious-pr-bench README pattern — inspect_ai eval (verify LICENSE first)
inspect eval sevra/tasks/reviewer.py --model <reviewer-model>
```

Dataset tags: `deterministic` (2,250 malicious), `benign` (347 legit fixes).

## Dead Ends

- **Production merge automation without SEVRA-class eval** — open-weight models show 14–82 pp framing swings.
- **Code import before LICENSE** — same blocker pattern as @entities/tools/seclaw-eval.md.
