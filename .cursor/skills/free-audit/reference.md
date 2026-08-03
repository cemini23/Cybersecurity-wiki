# Free audit — reference

## Mode → role matrix (full set)

Inherits cursor-audit modes + super-audit `prod-ship`. Roles label **intent** for each channel; free OR models are not Cursor slugs.

| Mode | Grok lens | claude-ds lens | Free OR #1 prefer | Free OR #2 prefer | When |
|------|-----------|----------------|-------------------|-------------------|------|
| **code-debug** | code-implementation | agentic-reasoning | coding family | alt coding/general | Stack traces, bugs (**default**) |
| **security** | adversarial | agentic-reasoning | general/reasoning | coding | Auth, injection, secrets |
| **config-infra** | config-semantics | code-implementation | general | coding | MCP, hooks, YAML, CI |
| **brief-plan** | strategic | agentic-reasoning | general/reasoning | alt family | Adoption / GO/NO-GO |
| **architecture** | agentic-reasoning | third-lens | general | coding | Refactors, boundaries |
| **quick-triage** | agentic-reasoning | code-implementation | coding | general | Fast top-3 only |
| **prod-ship** | agentic-reasoning | code-implementation | coding | general/reasoning | Bot/config deploy |

Mode heuristics: same as [cursor-audit reference](../cursor-audit/reference.md#mode-classification-heuristics).

## Free OpenRouter selection

Script: `scripts/select_free_or_models.py`

| Rule | Detail |
|------|--------|
| Price | `$0` prompt + completion, or id ends with `:free` |
| Exclude | `deepseek`, `grok`, `x-ai/` (case-insensitive) |
| Exclude modalities | embed, tts, whisper, image-only, audio, diffusion, moderation, lyria, content-safety |
| Count | Default **2**; `--count N` for more (min 2) |
| Diversity | Prefer **distinct provider families** (openai / nvidia / google / cohere / poolside / inclusionai / meta / qwen / other) |
| Rank | Prefer coder/instruct/chat/gpt-oss/nemotron/laguna/north/gemma tokens; then larger `context_length` |
| Fallback | If &lt;2 after filter → include `openrouter/free` once + best remaining; note degraded in JSON |

Live catalog changes often — never hardcode IDs as the only path.

## Keys / env

| Variable | Used for |
|----------|----------|
| `OPENROUTER_API_KEY` | Free OR legs (required for slots 3–4) |
| `OPENROUTER_BASE_URL` | Default `https://openrouter.ai/api/v1` |
| `DEEPSEEK_API_KEY` | claude-ds slot via DeepSeek API |
| `DEEPSEEK_BASE_URL` | Default `https://api.deepseek.com/v1` |
| `DEEPSEEK_MODEL` | Default `deepseek-v4-flash` |
| `CEMINI_LLM_ROUTING_ENV` | Optional absolute path to a routing env file |

Scripts hydrate from process env, then optional `CEMINI_LLM_ROUTING_ENV` only. They do **not** scan home trees or project dotenv files.

## Per-auditor output format

Every auditor file (`auditor-grok.md`, `auditor-claude-ds.md`, `auditor-or-*.md`) uses:

```markdown
### Verdict
PASS | WARN | FAIL — one line why

### Findings
| Severity | Finding | Evidence (file:line or quote) | Fix |
|----------|---------|----------------------------------|-----|
| critical/warn/info | ... | ... | ... |

### Root cause (if debugging)
…

### Confidence
high | medium | low — and what would change your mind

### Unique angle
One thing other models might miss
```

## SYNTHESIS.md template (Grok writes this)

```markdown
# Free audit — {target summary}

**Mode:** {mode} · **Auditors:** Grok + claude-ds ({deepseek model}) + free OR ({m1}, {m2})
**Pack:** `{pack}` · **Out:** `{out}`

| Slot | Channel | Model | Verdict |
|------|---------|-------|---------|
| 1 | grok | grok-cli | … |
| 2 | claude-ds | deepseek-v4-flash | … |
| 3 | openrouter-free | {m1} | … |
| 4 | openrouter-free | {m2} | … |

## Consensus (≥2 auditors agree)
- …

## Unique (single auditor — still investigate)
- [{model}] …

## Conflicts (Glasswing — resolve before ship)
| Topic | Grok | claude-ds | OR1 | OR2 | Resolution |
|-------|------|-----------|-----|-----|------------|
| … | … | … | … | … | … |

## Recommended fix order
1. …

## Verdict rollup
**Overall:** SHIP | SHIP-WITH-FIXES | REWORK | REJECT — one paragraph
```

## HTTP leg reliability

`run_non_grok_legs.py` inlines pack artifacts and sets `tool_choice=none`. It:
- sends DeepSeek `thinking: {type: disabled}` so V4 Flash fills `content` (not endless `reasoning_content`)
- still falls back to `reasoning_content` if `content` is empty
- rejects tool-stub / incomplete audits (DSML, missing Findings/Confidence, meta-"let me" drafts)
- retries once, finalize-from-notes, then falls back to another free OR family
- treats OpenRouter bodies without `choices` (rate limits) as errors; 429 retries with backoff

Treat degraded stubs as channel failure, not product FAIL.

## Cost discipline

- Free-audit ≈ Grok plan tokens + DeepSeek Flash + $0 OR.
- Escalate to cursor-audit / super-audit when free council is split on critical severity.
- Do not paste secrets into free OR prompts.
