# Super audit — examples

## Example 1 — Poker Tournament S1 (reference run)

**User:**

> super audit before Tournament S1 — should we ship current decide commit?

**Parent:**

1. **Tailor** — `agents/devfun-poker-arena/prompts/tournament_s1_super_audit.md` (S1 win table, S2 struggle, env toggles, VPIP band)
2. **Pack** — `build_tournament_super_audit_pack.py` (domain-specific) or generic `build_audit_pack.py` with HL artifacts
3. **Mode** — `prod-ship`
4. **Cursor roles** — agentic-reasoning, code-implementation, third-lens → premium slugs per reference
5. **API roles** — api-adversarial (`openrouter/fusion`), api-deep-reasoning (`OPENROUTER_PREMIUM_MODEL` / `z-ai/glm-5.2`) via `run_api_auditors.py`
6. **Synthesize** — `briefs/2026-06-09_tournament-s1-super-audit-synthesis.md`

**Outcome:** 4/5 recommended `70f2527` revert; operator shipped lane-gate hybrid `4a6df45` after conflict resolution.

---

## Example 2 — WC bot prod posture

**User:**

> super audit on world cup conviction config before match day

**Parent:**

1. **Tailor** prompt with 43-team matrix, `conviction.yaml` excerpts, LP safety cadence, inflow posture
2. **Artifacts** — `gemini-wc-conviction-config-audit` snippets, prod pull briefs, `wiki/meta/wc-lp-safety-cadence.md`
3. **Mode** — `prod-ship` + brief-plan tailoring on API leg
4. **API roles** — api-advisor (pro `ADVISOR_MODEL`) + api-deep-reasoning (`auditors.json` override)

```json
{
  "slots": [
    {
      "label": "api-advisor",
      "role": "api-advisor",
      "base_url_env": "ADVISOR_BASE_URL",
      "api_key_env": "ADVISOR_API_KEY",
      "model": "google/gemini-2.5-pro"
    },
    {
      "label": "api-deep-reasoning",
      "role": "api-deep-reasoning",
      "base_url_env": "DEEPSEEK_BASE_URL",
      "api_key_env": "DEEPSEEK_API_KEY",
      "model": "deepseek-reasoner"
    }
  ]
}
```

5. **Synthesize** — team downgrade list, cancel-window risk, SHIP-WITH-FIXES on stale `fade_watch` rows

**Keys:** `source scripts/source_llm_routing_env.sh` wires `ADVISOR_*` from OpenRouter when set.

---

## Example 3 — Quick super audit

**User:**

> quick super audit on scripts/sync_wiki_to_librarian.sh

**Parent:**

1. Mode `quick-triage` — premium Cursor roles (agentic-reasoning + code-implementation + third-lens)
2. API: api-deep-reasoning only (skip api-adversarial)
3. Minimal pack — script source + recent log excerpt
4. Top-3 issues synthesis only

---

## Example 4 — Missing API keys

**Discovery output:**

```
OPENROUTER_API_KEY: present (sk-or-…xxxx)
DEEPSEEK_API_KEY: missing
```

**Parent (gated — wait for operator reply before any paid API call):**

> API leg: api-deep-reasoning skipped (DeepSeek key absent). Options:
> 1) Continue with 4 auditors (3 Cursor premium + api-adversarial) after you say OK
> 2) Export `DEEPSEEK_API_KEY` in your shell (or set `CEMINI_LLM_ROUTING_ENV`) and tell me to retry
>
> I will not call paid endpoints or change routing files until you confirm.

Do not ask the operator to paste secret values into chat.

---

## Example 5 — Re-audit after deploy

**User:**

> we shipped 4a6df45 but VPIP still low — super audit again

**Parent:**

1. Copy prior synthesis into **Already ruled out** / prior consensus section
2. Refresh pack with new `deploys.jsonl` + playground status
3. Swap third-lens Cursor family and one API role candidate for fresh eyes
4. Compare deploy commit recommendations vs previous rollup
