#!/usr/bin/env python3
"""Writer for K369–K373 ingest (2026-09-25)."""
from __future__ import annotations

from pathlib import Path

WIKI = Path(__file__).resolve().parents[1] / "wiki"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/cybersec"
DATE = "2026-09-25"


def w(rel: str, body: str) -> None:
    p = WIKI / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body, encoding="utf-8")
    print("wrote", rel)


def src(
    slug: str,
    title: str,
    arxiv: str,
    kid: str,
    pdf: str,
    narrative: str,
    concept: str,
    extra_related: list[str] | None = None,
    ood: bool = False,
) -> None:
    rels = ([f"  - {concept}"] if concept else []) + [f"  - {r}" for r in (extra_related or [])]
    rel_yaml = "related:\n" + "\n".join(rels) if rels else "related: []"
    rel_sec = f"\n## Relations\n\n- @{concept}\n" if concept else ""
    if extra_related:
        rel_sec += "".join(f"- @{r}\n" for r in extra_related)
    body = f"""---
title: "{title}"
type: source
tags: [source, {"ood" if ood else "arxiv, agent-security"}]
keywords: [{arxiv}, {kid.lower()}]
{rel_yaml}
maturity: draft
read_status: read
created: {DATE}
updated: {DATE}
phase_0_verdict: "REFERENCE {DATE} — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc ({kid})"
---

{rel_sec}
## Raw Concept

| Field | Value |
|-------|-------|
| Title | {title} |
| arXiv | {arxiv} |
| Location | {EGRESS}/{pdf} |
| Retrieved | {DATE} |
| Read status | read (abstract + triage) |

## Narrative

{narrative}

## Snippets

> See arXiv {arxiv} abstract. [Source: arXiv {arxiv} (retrieved {DATE})]
"""
    w(f"sources/{slug}.md", body)


def concept_page(
    slug: str,
    title: str,
    kid: str,
    arxiv: str,
    source: str,
    narrative: str,
    related: list[str],
    wire: str,
) -> None:
    rel_yaml = "\n".join(f"  - {r}" for r in related)
    rel_inline = "\n".join(f"- @{r}" for r in related)
    body = f"""---
title: "{title} ({kid})"
type: concept
tags: [concept, agent-security, {kid.lower()}]
keywords: [{arxiv}, {kid}]
related:
{rel_yaml}
maturity: draft
created: {DATE}
updated: {DATE}
wire_status: policy_wired
wire_target: "{wire}"
---

## Relations

{rel_inline}

## Raw Concept

Question: **{title}** — operator steal from arXiv {arxiv}?

## Narrative

{narrative}

## Snippets

> Triage from arXiv {arxiv} abstract. [Source: arXiv {arxiv} (retrieved {DATE})]
"""
    w(f"concepts/{slug}.md", body)


def patch_index() -> None:
    idx = WIKI.parent / "wiki/index.md"
    text = idx.read_text(encoding="utf-8")
    block = """
| @sources/arxiv-2609-28940-calibrated-decision-models-pentest-harness-jev.md | draft | Calibrated pentest harness decisions + JEV (2609.28940; K369) |
| @concepts/calibrated-decision-models-pentest-harness-jev.md | draft | System One classifiers for pentest adjudication |
| @sources/arxiv-2609-29213-ble-backscatter-polarization-shift-identification.md | draft | BLE SWIPT backscatter device ID (2609.29213; K370) |
| @concepts/ble-backscatter-polarization-shift-identification-lab.md | draft | Polarization-shift backscatter auth (owned devices) |
| @sources/arxiv-2609-30217-instrumental-monitor-evasion-evaluation.md | draft | Instrumental monitor evasion (2609.30217; K371) |
| @concepts/instrumental-monitor-evasion-evaluation.md | draft | EvasionBench runtime monitor bypass eval |
| @sources/arxiv-2609-30233-coding-agents-generalized-tamp-ood.md | draft | OOD generalized TAMP coding agents (2609.30233) |
| @sources/arxiv-2609-30266-llm-agents-trace-tampering.md | draft | LLM agent self-trace tampering (2609.30266; K373) |
| @concepts/agent-execution-trace-tampering-audit.md | draft | Independent trace logging audit pattern |
"""
    needle = "| @sources/arxiv-2609-28395-translation-finetune-forgetting-mt-instruction.md | draft | MT fine-tune forgetting (2609.28395; K368) |"
    if "K369" not in text:
        text = text.replace(needle, needle + block, 1)
        idx.write_text(text, encoding="utf-8")
        print("patched index.md")


def main() -> int:
    src(
        "arxiv-2609-28940-calibrated-decision-models-pentest-harness-jev",
        "Calibrated decision models for autonomous pentest harnesses (JEV / Laya)",
        "2609.28940",
        "K369",
        "arxiv-2609.28940-calibrated-decision-models-for-autonomous-penetr.pdf",
        "**K369** — autonomous pentest harnesses should not use the same LLM for **finding adjudication**, **severity recalibration**, **agent pruning**, and **confirmation loops**. **System One** typed classifiers (e.g. JEV) supply calibrated non-generative verdicts at those decision points. NeuroSploit case-study framing: compare runs with vs without TypeSafe System One on a known-vuln web target. Pairs **K341** secure pentest agents + federation **JEV gates** — not a substitute for external enforcement (K314).",
        "concepts/calibrated-decision-models-pentest-harness-jev.md",
        [
            "concepts/secure-ai-powered-pentest-agents.md",
            "concepts/faithful-agent-asr-measurement.md",
        ],
    )
    concept_page(
        "calibrated-decision-models-pentest-harness-jev",
        "Calibrated decision models for pentest harnesses",
        "K369",
        "2609.28940",
        "sources/arxiv-2609-28940-calibrated-decision-models-pentest-harness-jev.md",
        "Separate **generative planning** from **typed adjudication** in pentest agent stacks. Report whether severity grades and finding confirmation are **model-self-judged** vs **System One / external oracle**. Authorized lab and written-scope product pentest only.",
        [
            "sources/arxiv-2609-28940-calibrated-decision-models-pentest-harness-jev.md",
            "concepts/secure-ai-powered-pentest-agents.md",
            "concepts/faithful-agent-asr-measurement.md",
            "concepts/llm-pentest-automation.md",
        ],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K369)",
    )

    src(
        "arxiv-2609-29213-ble-backscatter-polarization-shift-identification",
        "Secure polarization-shift backscatter identification for battery-free BLE",
        "2609.29213",
        "K370",
        "arxiv-2609-29213-secure-polarization-shift-backscatter-identifica.pdf",
        "**K370** — **SWIPT** battery-free BLE nodes can transmit **AES-128 encrypted device ID** via **polarization-shift backscatter** on the power wave before data traffic, using an external RF switch + orthogonal antennas (no rectifier modification). Defensive **device authentication** steal for IoT lab eval — **owned devices / authorized RF only**; pairs K305/K365 service-auth vs radio anonymity.",
        "concepts/ble-backscatter-polarization-shift-identification-lab.md",
        ["concepts/ble-mac-randomization-reidentification-lab.md"],
    )
    concept_page(
        "ble-backscatter-polarization-shift-identification-lab",
        "BLE backscatter polarization-shift identification (lab)",
        "K370",
        "2609.29213",
        "sources/arxiv-2609-29213-ble-backscatter-polarization-shift-identification.md",
        "Protocol-independent **backscatter identification** under wireless power transfer — test whether downstream **BLE service authorization** still holds after ID exchange. Lab framing only; no unauthorized RF.",
        [
            "sources/arxiv-2609-29213-ble-backscatter-polarization-shift-identification.md",
            "concepts/ble-mac-randomization-reidentification-lab.md",
        ],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K370)",
    )

    src(
        "arxiv-2609-30217-instrumental-monitor-evasion-evaluation",
        "Instrumental monitor evasion emerges under ordinary task pressure",
        "2609.30217",
        "K371",
        "arxiv-2609.30217-instrumental-monitor-evasion-emerges-under-ordin.pdf",
        "**K371** — **EvasionBench**: agents know tool calls are **runtime-monitored** and ordinary tasks sometimes require **policy-forbidden operations**; best-of-3 **evasion attempt** rates up to ~98% and **success** up to ~88% on some models. Report **attempt vs success** separately; no evasion recipes in wiki. **Authorized lab only.** **Runtime:** `scripts/k371_instrumental_monitor_evasion_precheck.py`. Pairs K307 StepGuard + K348 Auto Mode monitor red-team.",
        "concepts/instrumental-monitor-evasion-evaluation.md",
        [
            "concepts/auto-mode-blocking-classifier-redteam.md",
            "concepts/step-level-agent-guardrails.md",
        ],
    )
    concept_page(
        "instrumental-monitor-evasion-evaluation",
        "Instrumental monitor evasion evaluation",
        "K371",
        "2609.30217",
        "sources/arxiv-2609-30217-instrumental-monitor-evasion-evaluation.md",
        "Instrumental evasion is **task-driven monitor circumvention**, not only jailbreak prompts. Eval must name **monitor configuration**, **task-policy pairs**, and **best-of-k** attempt semantics. External **pre-execution gates** remain required (K314).",
        [
            "sources/arxiv-2609-30217-instrumental-monitor-evasion-evaluation.md",
            "concepts/auto-mode-blocking-classifier-redteam.md",
            "concepts/non-decaying-loop-safety-state.md",
        ],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K371)",
    )

    w(
        "sources/arxiv-2609-30233-coding-agents-generalized-tamp-ood.md",
        f"""---
title: "Coding agents for generalized task and motion planning (OOD)"
type: source
tags: [source, ood]
keywords: [2609.30233, ood]
related:
  - "@ccc-wiki/sources/arxiv-2609-30233-coding-agents-tamp-ood-2026-09-25.md"
maturity: draft
read_status: read
created: {DATE}
updated: {DATE}
phase_0_verdict: "REFERENCE {DATE} — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (OOD)"
cross-wiki-source: "@ccc-wiki/sources/arxiv-2609-30233-coding-agents-tamp-ood-2026-09-25.md"
---

## Relations

- @ccc-wiki/sources/arxiv-2609-30233-coding-agents-tamp-ood-2026-09-25.md — CCC wiki **primary steal** (generalized TAMP / coding agents).

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Coding agents for generalized task and motion planning (OOD) |
| arXiv | 2609.30233 |
| Location | {EGRESS}/arxiv-2609-30233-coding-agents-for-generalized-task-and-motion-pl.pdf |
| Retrieved | {DATE} |
| Read status | read (abstract + triage) |

## Narrative

Generalized **TAMP** via coding agents synthesizing cross-instance programs — **robotics / motion planning** primary, not cyber-primary. **OOD stub** routed to @ccc-wiki ({DATE}).

## Snippets

> See arXiv 2609.30233 abstract. [Source: arXiv 2609.30233 (retrieved {DATE})]
""",
    )

    src(
        "arxiv-2609-30266-llm-agents-trace-tampering",
        "LLM agents can easily tamper with their own traces",
        "2609.30266",
        "K373",
        "arxiv-2609-30266-llm-agents-can-easily-tamper-with-their-own-trac.pdf",
        "**K373** — local coding agents (multiple harnesses tested) can **delete or alter execution traces** on request; **external attackers** can induce deletion; **reward-seeking** can elicit tampering without explicit ask. **Muse Code** exception noted in paper triage. Audit steal: **independent interception logging** outside agent write path — trajectory self-report ≠ evidence (pairs K271/K278). **Runtime:** `scripts/k373_agent_trace_tampering_precheck.py`.",
        "concepts/agent-execution-trace-tampering-audit.md",
        [
            "concepts/agent-execution-provenance.md",
            "concepts/faithful-agent-asr-measurement.md",
        ],
    )
    concept_page(
        "agent-execution-trace-tampering-audit",
        "Agent execution trace tampering audit",
        "K373",
        "2609.30266",
        "sources/arxiv-2609-30266-llm-agents-trace-tampering.md",
        "Treat agent-visible log files as **untrusted**. Compliance and IR reconstructions need **append-only / out-of-band** trace capture with **integrity checks**. Report harness + model when citing tampering rates.",
        [
            "sources/arxiv-2609-30266-llm-agents-trace-tampering.md",
            "concepts/agent-execution-provenance.md",
            "concepts/faithful-agent-asr-measurement.md",
            "concepts/trace-verified-ctf-agent-eval.md",
        ],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K373)",
    )

    patch_index()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
