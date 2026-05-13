---
title: "Awesome_GPT_Super_Prompting — jailbreak / prompt-injection corpus"
type: entity
tags: [tool, jailbreak-corpus, prompt-injection, adversarial-ai, gpl-3, offensive-security]
keywords: [awesome_gpt_super_prompting, cyberalbsecop, jailbreak corpus, prompt injection, gpt-4o, claude 3.5, deepseek r1]
related:
  - "@osint-wiki/entities/tools/awesome-gpt-super-prompting.md"
  - "@osint-wiki/sources/evaluating-github-repos-trading-stack-2026-05-12.md"
  - concepts/llm-vulnerability-discovery.md
maturity: draft
created: 2026-05-12
updated: 2026-05-12
osint_eval_origin: doc1-url-14 (cross-routed; cybersec primary for adversarial-AI study)
---

## Relations

- `@osint-wiki/entities/tools/awesome-gpt-super-prompting.md` — OSINT cross-route (rejected on ToS risk)
- `@osint-wiki/sources/evaluating-github-repos-trading-stack-2026-05-12.md` — origin eval (URL 14)
- `@concepts/llm-vulnerability-discovery.md` — methodology synthesis

## Raw Concept

- **Repo**: `github.com/CyberAlbSecOP/Awesome_GPT_Super_Prompting`
- **License**: GPL-3.0
- **Tier**: Study / Reference (do not operationalize against any production LLM API)

## Narrative

Curated corpus of jailbreaks, leaked system prompts, and prompt-injection techniques targeting GPT-4o, Claude 3.5, DeepSeek R1, and other frontier LLMs.

### Usage guidance

**Read-only / study-only.** Operationalizing these techniques against the production DeepSeek / OpenAI / Anthropic APIs violates enterprise ToS and risks API key bans. Acceptable use: defensive — understand the attack surface to design prompt-injection-resistant Cemini surfaces.

### Methodology relevance

Cross-routed because the corpus is genuinely useful for **defensive** red-teaming. Pair with OpenAnt (vuln discovery) + multi-model-redteam (parallel adversarial pass) for a full LLM-attack-pattern toolkit.
