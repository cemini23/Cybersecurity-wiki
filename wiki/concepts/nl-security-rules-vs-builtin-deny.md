---
title: "NL security rules vs built-in deny — instruction-file prose is not enforcement (K303)"
type: concept
tags: [concept, agent-security, usable-security, claude-md, deny, k303, defensive]
keywords: [CLAUDE.md, AGENTS.md, deny, permission rule, sandbox, PreToolUse, write-only channel, enforcement gap, security rule]
related:
  - sources/arxiv-2608-23550-claude-md-vs-builtin-deny.md
  - concepts/agent-runtime-guardrails.md
  - concepts/llm-codegen-prompt-security-redistribution.md
  - concepts/step-level-agent-guardrails.md
  - concepts/recognition-enforcement-gap-instruction-arbitration.md
  - concepts/mcp-security-posture.md
  - concepts/coding-agent-supply-chain-install-gap.md
  - concepts/system-prompt-leakage.md
maturity: draft
created: 2026-08-25
updated: 2026-08-25
wire_status: runtime_wired
wire_target: ".cursor/hooks.json + scripts/k303_k298_policy.py + claude_settings.json.example (K303)"
---

## Relations

- @sources/arxiv-2608-23550-claude-md-vs-builtin-deny.md
- @concepts/agent-runtime-guardrails.md — enforcement paradigms: where deny/sandbox actually live
- @concepts/mcp-security-posture.md — tool admission: description/prose ≠ runtime enforcement
- @concepts/coding-agent-supply-chain-install-gap.md — adjacent write-only-channel gap (pre-install gates vs prose instructions)
- @concepts/system-prompt-leakage.md — instruction-file content is attacker-visible surface; rules leak like prompts

## Raw Concept

Question this page answers: **when is a natural-language security rule in an agent instruction file (CLAUDE.md / AGENTS.md) an enforceable control, and when is it just a suggestion?**

## Narrative

Agent instruction files are a **write-only channel**: a developer writes "never push to production" in prose and receives no signal about whether a control will enforce it. The paper (K303, 2608.23550) measures the gap across 481 public CLAUDE.md files: only **~4–16%** of extracted security rules match a built-in platform control (strict estimate **4.4%**, 95% CI 2.6–6.7%; extraction recall 66.3%). The rest are model-interpreted text — unless a team adds a hook or script. Two rules with identical prose form behave completely differently: "never run npm publish" maps to a deterministic `deny` rule; "never put customer secrets in logs" requires the model to judge what counts as a secret.

**The core distinction:**
- **Enforceable** — permission rules (allow/ask/deny), tool/command/path/domain patterns, permission modes, filesystem/network sandboxing, managed restrictions. Deterministic; block before the action.
- **Model-mediated** — everything left to interpretation; enforcement quality equals the model's judgment, which prior work shows is fragile (command denylists 69.0–98.6% fragile; removing one scope sentence raises out-of-scope actions 0.0→17.1%).

**Operator steal (this workspace directly):**
1. **Do not treat CLAUDE.md / `.cursor/rules` prose as enforcement.** Rule text is steering + documentation. Real enforcement = PreToolUse deny hooks, sandbox, permission rules, verified gates (the EnvHarness "keep the verifier" principle — `wrap-don't-rebuild`). **This wiki:** `.cursor/hooks.json` runs `python3 scripts/k303_k298_policy.py --hook` with `failClosed: true` (deny `.env` / key files / `cat .env`). Claude Code deny list: copy `claude_settings.json.example` → `.claude/settings.json` (gitignored).
2. **Secrets never live in NL rules only.** A prose rule "never print the API key" is a request, not a control; the tool-layer grant (secret never returned to the model) is the control (pairs `concepts/inadvertent-context-leakage.md`).
3. **When you write a security rule, ask which control enforces it.** If none exists deterministically, add the hook/deny or accept it as a model-mediated best-effort and say so.
4. **Write-only feedback is a defect to engineer around**: prefer rules that name an enforceable pattern (tool, path, domain) so the gap between intent and enforcement shrinks.
5. Any prompt/rule content in instruction files is attacker-visible surface (pairs `system-prompt-leakage`) — never put secrets or unguarded escalation paths there.

## Snippets

> A developer writes a security rule but gets no feedback on whether a control will enforce it. The same plain-text form hides two kinds of rule: those a permission rule, mode, or sandbox can enforce, and those left to the model to interpret. [Source: arXiv 2608.23550 abstract]

> CLAUDE.md shapes what the model attempts, whereas permission rules and related controls determine what the platform permits. [Source: arXiv 2608.23550 §1, citing Claude Code docs]
