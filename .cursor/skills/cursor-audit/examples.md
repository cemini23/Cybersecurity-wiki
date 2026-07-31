# Cursor audit — examples

## Example 1 — User invocation (code bug)

**User:**

> cursor audit — lazy-tool MCP shows red; search_tools returns empty

**Parent:**

1. Scope: `.cursor/mcp.json`, lazy-tool catalog, error = empty search
2. Mode: `config-infra`
3. Roles: config-semantics → `gemini-3.1-pro`, code-implementation → `gpt-5.3-codex`, third-lens → `claude-opus-4-8-thinking-high`
4. Dispatch 3 parallel readonly Tasks with shared audit pack
5. Synthesize: consensus on `reindex` + UI toggle; unique finding from third-lens on allowlist path

**Sample synthesis excerpt:**

```markdown
## Consensus (≥2 auditors agree)
- lazy-tool catalog stale or server disabled in UI — run reindex + enable toggle

## Unique (single auditor — still investigate)
- [third-lens / gemini] `.cursor/lazy-tool.yaml` path mismatch vs mcp.json cwd

## Overall:** SHIP-WITH-FIXES — reindex first; if still empty, fix yaml path
```

---

## Example 2 — Brief GO/NO-GO

**User:**

> /cursor-audit mode brief-plan on briefs/2026-06-01_polymarket-foo.md

**Parent:**

1. Read brief; paste Summary + Body + cost claims into audit pack
2. Mode: `brief-plan`
3. Roles: strategic → Anthropic premium, code-implementation → OpenAI premium, third-lens → Moonshot premium (`kimi-k2.5`)
4. Lens: displacement vs existing wiki tooling, statistical claims, phase 1 scope
5. Run `scripts/skill_audit.py` or `vet briefs/<file>.md --profile brief` after synthesis

**Conflict example:**

| Topic | code-impl | strategic | third-lens |
|-------|-----------|-----------|------------|
| Backtest sample size | n too small | acceptable with caveats | insufficient detail |

Resolution: parent proposes adding explicit n and regime disclosure before ship.

---

## Example 3 — Security pass

**User:**

> council audit on the new auth middleware in ui/proxy/

**Parent:**

1. Mode: `security`
2. Roles: agentic-reasoning → Anthropic premium, adversarial → `grok-4.3`, code-implementation → OpenAI premium
3. Audit pack lists all files in scope + threat model (session fixation, header injection)

---

## Example 4 — Quick triage (premium, shallow)

**User:**

> quick cursor audit on scripts/sync_wiki_to_librarian.sh

**Parent:**

1. Mode: `quick-triage`
2. **Same premium role delegation** as code-debug (agentic-reasoning + code-implementation + third-lens) — not fast/economy models
3. Subagents return **top 3 issues only**

---

## Example 5 — After fix loop

**User:**

> you fixed it but still failing — cursor audit again

**Parent:**

1. Re-scope with **Already ruled out** filled from prior audit
2. Same mode unless evidence shifted (e.g. code-debug → config-infra)
3. **Swap third-lens family** for fresh eyes (e.g. Google → xAI) while keeping agentic-reasoning + code-implementation premium
