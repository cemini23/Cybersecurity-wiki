# Cursor audit — model delegation

Audits are **premium**: always pick flagship-tier models matched to **auditor roles**, not a fixed triple. Slugs must match Cursor Task `model` exactly.

## Selection procedure (parent — Step 2)

1. **Classify mode** from scope (table below).
2. **Resolve three roles** from the mode → role matrix.
3. For each role, pick the **highest available premium slug** from the catalog (preferred family first, then alternates).
4. Enforce **three distinct provider families** across the triple.
5. **User override:** `models: a, b, c` replaces slots 1–3; still require three families when possible.
6. **Dispatch failure:** substitute from the same family’s fallback chain; note swap in synthesis.
7. **Announce before dispatch** — mode, roles, chosen slugs, one-line rationale each:

   > Cursor audit — mode: `code-debug` · roles: code-implementation → `gpt-5.3-codex`, agentic-reasoning → `claude-opus-4-8-thinking-high`, third-lens → `gemini-3.1-pro`

## Premium tier policy

| Rule | Detail |
|------|--------|
| Default tier | **Premium only** — flagship reasoning / coding models per provider |
| Never default | `composer-2.5-fast`, flash/lite variants, economy or “fast” SKUs |
| Mid-tier fallback | `gpt-5.5-medium`, `claude-4.6-sonnet-medium-thinking` — only when flagship slug unavailable; **note in synthesis** |
| `quick-triage` | Same premium tier; **narrow scope** (top 3 issues), not cheaper models |
| Diversity | Three **different provider families** whenever possible |

## Auditor roles

| Role | Optimizes for | Preferred family | Acceptable alternates |
|------|---------------|------------------|------------------------|
| **agentic-reasoning** | Root cause, agentic traces, prod judgment, architecture depth | Anthropic | — |
| **code-implementation** | Patches, test failures, concrete fixes, stack traces | OpenAI | — |
| **third-lens** | Cross-vendor blind spots, alt structure, fresh eyes | Google | xAI, Moonshot |
| **adversarial** | Exploit paths, attacker model, trust boundaries | xAI | Anthropic (security mode) |
| **config-semantics** | YAML/MCP/hooks/deploy wiring, startup failure modes | Google | Anthropic |
| **strategic** | Brief GO/NO-GO, displacement, cost/timeline claims | Anthropic | Moonshot |

## Mode → role matrix

| Mode | Slot 1 | Slot 2 | Slot 3 | Use when |
|------|--------|--------|--------|----------|
| **code-debug** | code-implementation | agentic-reasoning | third-lens | Stack traces, failing tests, logic bugs (**default**) |
| **security** | agentic-reasoning | adversarial | code-implementation | Auth, injection, secrets, trust boundaries |
| **config-infra** | config-semantics | code-implementation | third-lens | MCP, hooks, YAML, CI, deploy scripts |
| **brief-plan** | strategic | code-implementation | third-lens | Adoption briefs, GO/NO-GO, phase 0 |
| **architecture** | agentic-reasoning | third-lens | code-implementation | Refactors, module boundaries, API shape |
| **quick-triage** | agentic-reasoning | code-implementation | third-lens | User asked quick/fast — **premium models, shallow depth** |

## Premium catalog (Cursor Task slugs)

Pick **first available** slug in each role’s list. Do not skip to mid-tier if a premium slug works.

| Family | Premium slugs (best → acceptable) | Mid-tier fallback (flag if used) |
|--------|-----------------------------------|----------------------------------|
| **Anthropic** | `claude-opus-4-8-thinking-high` | `claude-4.6-sonnet-medium-thinking` |
| **OpenAI** | `gpt-5.3-codex` | `gpt-5.5-medium` |
| **Google** | `gemini-3.1-pro` | — (use xAI/Moonshot for third family) |
| **xAI** | `grok-4.3` | `grok-build-0.1` |
| **Moonshot** | `kimi-k2.5` | — |

### Role → slug resolution (quick lookup)

| Role | Try in order (first available, unused family) |
|------|-----------------------------------------------|
| agentic-reasoning | Anthropic premium |
| code-implementation | OpenAI premium |
| third-lens | Google premium → xAI premium → Moonshot premium |
| adversarial | xAI premium → Anthropic premium |
| config-semantics | Google premium → Anthropic premium |
| strategic | Anthropic premium → Moonshot premium |

> **2026-06-13:** `claude-fable-5-thinking-high` removed from Cursor subagents. Opus class is the Anthropic premium default.

## Mode classification heuristics

| User language | Mode |
|---------------|------|
| test fail, exception, traceback, bug, doesn't work | `code-debug` |
| XSS, SQLi, auth bypass, secret leak, CVE | `security` |
| mcp.json, hook, yaml, workflow, tunnel, deploy | `config-infra` |
| brief, adopt, GO/NO-GO, phase 0, rollout | `brief-plan` |
| refactor, design, module split, API shape | `architecture` |
| quick, fast, triage, skim | `quick-triage` |

## Fresh eyes on re-audit

When re-running after a failed fix, **swap the third-lens family** (e.g. Google → xAI or Moonshot) while keeping agentic-reasoning + code-implementation premium.

## Audit pack checklist

Before dispatch, verify the pack includes:

- [ ] Absolute file paths or pasted error output
- [ ] Single primary question
- [ ] Ruled-out hypotheses (even if empty)
- [ ] Required output format block
- [ ] Readonly constraint stated
- [ ] Announced roles + slugs recorded in synthesis header

## Synthesis severity rollup

Map subagent severities to parent action:

| Pattern | Overall verdict |
|---------|-----------------|
| Any **critical** with consensus | FAIL → REJECT or REWORK |
| **critical** from one auditor only | WARN → investigate before ship |
| All PASS | SHIP (still note unique warns) |
| Split root cause | REWORK until conflict resolved |

## Integration with static brief audit

For files under `briefs/`:

1. Run cursor audit (multi-model, qualitative)
2. Run `python3 scripts/skill_audit.py briefs/<file>.md` or `vet briefs/<file>.md --profile brief` (mechanical veto gates)

Static REJECT overrides multi-model SHIP.
