---
title: "llm-defense-lattice — OWASP LLM Top 10 defense attribution benchmark (Reference)"
type: entity
tags: [tool, llm-security, owasp, bas, benchmark, docker, reference]
keywords: [llm-defense-lattice, owasp llm top 10, defense lattice, breach attack simulation, alemaiorano]
related:
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-for-cybersecurity.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/llm-pentest-automation.md
  - concepts/siem.md
  - entities/tools/defenseclaw.md
  - entities/tools/cryptex-oss.md
  - entities/tools/seclaw-eval.md
  - sources/arxiv-2605-30454-agent-prompt-injection-surface-evaluation.md
  - sources/arxiv-2606-02822-owasp-llm-defense-attribution.md
  - sources/arxiv-2606-05252-bas-to-siem-detection-as-code-synthesis.md
  - sources/arxiv-2606-10749-toward-secure-llm-agents-survey.md
  - sources/arxiv-2606-18673-prompt-leaking-attacks-area.md
  - concepts/system-prompt-leakage.md
  - entities/tools/leakbench-area.md
  - sources/arxiv-2606-22659-confidently-wrong-prompt-injection-calibration.md
  - concepts/prompt-injection-detector-calibration.md
  - entities/tools/picalib-research.md
maturity: draft
created: 2026-06-04
updated: 2026-07-31
phase_0_verdict: "Reference 2026-06-04 — open lattice + 17-probe corpus; GitHub license NOASSERTION; laptop BAS regression only after LICENSE audit."
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

# llm-defense-lattice — OWASP LLM Top 10 defense attribution benchmark

## Relations

- @concepts/agent-runtime-guardrails.md — maps defense families to OWASP LLM categories
- @concepts/llm-adversarial-fuzzing.md — paraphrase brittleness testing for refusal filters
- @concepts/llm-pentest-automation.md — HTTP-level BAS probes for LLM endpoints
- @entities/tools/defenseclaw.md — enterprise MCP/runtime governance (prod complement)
- @entities/tools/cryptex-oss.md — attack-side mutators for brittleness sweeps
- @entities/tools/seclaw-eval.md — agent trajectory benchmark (different eval axis)
- @sources/arxiv-2606-02822-owasp-llm-defense-attribution.md — paper + methodology provenance
- @sources/arxiv-2606-05252-bas-to-siem-detection-as-code-synthesis.md — companion: bypassed probe → deterministic Sigma starter rules
- @concepts/siem.md — detection-as-code output path from BAS findings

## Raw Concept

Daily digest fetch (2026-06-04). GitHub `alemaiorano/llm-defense-lattice` — four Docker stub targets (L₀–L₃), locked 17-probe OWASP-LLM corpus, Node.js BAS engine with 25 agents. Paper arXiv:2606.02822.

## Narrative

**Reference-tier** open benchmark for attributing **which defense family closes which OWASP LLM Top 10 category** — refusal regex vs token budget vs full stack (tool-registry auth + scrubbing).

**Use cases (authorized lab)**:
- Regression before claiming “OWASP LLM coverage” on a chat/completions API
- Compare refusal-only vs budget-only vs defense-in-depth posture
- Pair with @entities/tools/cryptex-oss.md or LLM paraphrasers to test brittleness of phrase filters

**Phase-0 blockers**:
- GitHub API reports **NOASSERTION** license (2026-06-04) — read LICENSE file before code import
- Stub targets only — L₄ real-LLM backend test showed regex dominated alignment on tested config (paper-scoped claim)

**Not** a substitute for @entities/tools/seclaw-eval.md (tool-using agent trajectories) or commercial BAS (AttackIQ, SafeBreach, etc.).

**Round-trip with 2606.05252**: lattice BAS produces attributed findings on locked 17-probe LLM corpus; companion paper maps bypassed findings → Sigma templates with probe-level traceback URIs — same sha256-pinned corpus discipline, defense-side output.

## Snippets

Lattice targets (paper): `target-llm-naive` (L₀), `target-llm-refusal` (L₁), `target-llm-budget` (L₂), `target-llm-defended` (L₃).

Corpus: `owasp-llm-probe-corpus.json` — 6× LLM01, 3× LLM02, 3× LLM06, 2× LLM07, 3× LLM10.

## Dead Ends

- **Single aggregate BAS pass rate** as ship gate — paper shows refusal-only clears static jailbreak/leak probes while agency/budget gaps persist.
- **Refusal-regex-only** on LLM01/LLM07 — large paraphrase brittleness; budget controls more stable under same mutation in paper.
