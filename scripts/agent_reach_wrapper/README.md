# Agent-Reach Wrapper

Standalone OSINT wrapper for Agent-Reach-style manual social snapshots. It proves the safe local boundary without adopting upstream logged-in scraping.

## Safety Boundary

- Manual local snapshot input only: no browser cookies, browser profiles, logged-in scraping, live network calls, prod ingest, or Discord output.
- Default output is local `DRY_RUN` JSON under `.local/agent-reach-wrapper/`.
- All content is treated as untrusted data. Batches fail closed on schema errors, unknown sources/domains/authors, prompt-injection hits, duplicates, or empty captures.
- `operator_review` is always `true` in wrapper output. Human review stays between this output and wiki ingest, briefs, or CeminiSuite handoff.

## Local Validation

```bash
python3 -m scripts.agent_reach_wrapper \
  --snapshot fixtures/agent_reach_wrapper/benign_snapshot.json \
  --allowlist config/agent_reach_sources.example.json
```

Focused tests:

```bash
python3 -m unittest scripts.tests.test_agent_reach_wrapper
```

## Adoption Notes

OSINT adopts this wrapper only. Upstream Agent-Reach direct integration remains blocked because browser-cookie/session reuse is outside the workspace safety boundary.
