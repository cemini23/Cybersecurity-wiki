#!/usr/bin/env python3
"""One-shot writer for K355–K363 ingest pages (2026-09-23)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"


def w(rel: str, body: str) -> None:
    p = WIKI / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body, encoding="utf-8")
    print("wrote", rel)


EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/cybersec"

PAGES: list[tuple[str, str]] = []


def add_source(
    slug: str,
    title: str,
    arxiv: str,
    k: str,
    pdf: str,
    narrative: str,
    concept_rel: str,
    extra_related: str = "",
    ood: bool = False,
) -> None:
    tags = "ood" if ood else "arxiv, agent-security, k355"
    ktag = k.lower().replace(" ", "")
    rel_block = f"  - {concept_rel}\n" if concept_rel else ""
    extra = f"{extra_related}\n" if extra_related else ""
    rel_section = ""
    if concept_rel:
        rel_section = f"\n## Relations\n\n- @{concept_rel} — {k} concept\n"
    body = f"""---
title: "{title}"
type: source
tags: [source, {tags}]
keywords: [{arxiv}, {ktag}]
related:
{rel_block}{extra}maturity: draft
read_status: read
created: 2026-09-23
updated: 2026-09-23
phase_0_verdict: "REFERENCE 2026-09-23 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc ({k})"
---

{rel_section}
## Raw Concept

| Field | Value |
|-------|-------|
| Title | {title} |
| arXiv | {arxiv} |
| Location | {EGRESS}/{pdf} |
| Retrieved | 2026-09-23 |
| Read status | read (abstract + triage) |

## Narrative

{narrative}

## Snippets

> See arXiv {arxiv} abstract. [Source: arXiv {arxiv} (retrieved 2026-09-23)]
"""
    PAGES.append((f"sources/{slug}.md", body))


def add_concept(
    slug: str,
    title: str,
    k: str,
    arxiv: str,
    source_rel: str,
    narrative: str,
    related: list[str],
    wire: str,
) -> None:
    rel_yaml = "\n".join(f"  - {r}" for r in related)
    rel_inline = "\n".join(f"- @{r}" for r in related)
    body = f"""---
title: "{title} ({k})"
type: concept
tags: [concept, agent-security, {k.lower()}]
keywords: [{arxiv}, {k}]
related:
{rel_yaml}
maturity: draft
created: 2026-09-23
updated: 2026-09-23
wire_status: policy_wired
wire_target: "{wire}"
---

## Relations

{rel_inline}

## Raw Concept

Question: **{title}** — what should operators steal from arXiv {arxiv}?

## Narrative

{narrative}

## Snippets

> Triage from arXiv {arxiv} abstract. [Source: arXiv {arxiv} (retrieved 2026-09-23)]
"""
    PAGES.append((f"concepts/{slug}.md", body))


def main() -> int:
    add_source(
        "arxiv-2609-23894-agentic-ai-cross-dimensional-taxonomy",
        "Connecting the Dots in Agentic AI Security (cross-dimensional taxonomy)",
        "2609.23894",
        "K355",
        "arxiv-2609.23894-connecting-the-dots-in-agentic-ai-security-a-cro.pdf",
        "**K355** introduces cross-dimensional threat representation **T = ⟨S, B, P, A⟩** linking surfaces, building blocks, phases, and consequences from 66 agentic-AI security studies (2022–2026). Steal: map eval maturity gaps vs known threats; report coverage per dimension, not a single ASR. Pairs K315 bounded-authority SLR and K327 taxonomy-driven red-team. **No attack payloads in wiki.**",
        "concepts/cross-dimensional-agentic-ai-security-taxonomy.md",
        "  - concepts/black-box-agentic-redteam-taxonomy.md\n  - concepts/security-agent-authority-auditability-slr.md",
    )
    add_concept(
        "cross-dimensional-agentic-ai-security-taxonomy",
        "Cross-dimensional agentic AI security taxonomy",
        "K355",
        "2609.23894",
        "sources/arxiv-2609-23894-agentic-ai-cross-dimensional-taxonomy.md",
        "Agentic AI security spans **state, tools, multi-agent interaction, and human channels** — single-axis taxonomies hide composition failures. **K355** steals a **cross-dimensional map** (entry surface → component → phase → consequence) for gap analysis and eval design. When stocking benchmarks, ask which dimensions each paper actually covers vs the known landscape. Audit-only; pairs faithful ASR (K271) and black-box agentic red-team (K327).",
        [
            "sources/arxiv-2609-23894-agentic-ai-cross-dimensional-taxonomy.md",
            "concepts/black-box-agentic-redteam-taxonomy.md",
            "concepts/security-agent-authority-auditability-slr.md",
            "concepts/faithful-agent-asr-measurement.md",
        ],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K355)",
    )

    add_source(
        "arxiv-2609-24173-graw-wifi-har-privacy-perturbation",
        "GRAW — zero-knowledge remote adversarial perturbation against Wi-Fi HAR",
        "2609.24173",
        "K356",
        "arxiv-2609.24173-zero-knowledge-remote-adversarial-attack-against.pdf",
        "**GRAW** defends user privacy by perturbing router signals so CSI-based human-activity recognition degrades — **zero-knowledge** of target HAR models (GAIL-learned perturbations). **K356** is **authorized RF lab / owned spectrum** defensive research steal; not unauthorized eavesdrop tradecraft. Pairs Wi-Fi CSI sensing threat models (K344 class).",
        "concepts/wifi-har-privacy-perturbation-graw.md",
        "  - concepts/through-wall-detection-sdr-pca.md",
    )
    add_concept(
        "wifi-har-privacy-perturbation-graw",
        "Wi-Fi HAR privacy perturbation (GRAW)",
        "K356",
        "2609.24173",
        "sources/arxiv-2609-24173-graw-wifi-har-privacy-perturbation.md",
        "CSI-based activity recognition on consumer Wi-Fi is a **privacy surface**. **K356** documents **GRAW-style** remote perturbation as a defender countermeasure when the HAR stack is unknown. Lab scope: owned devices, authorized spectrum, written RF lab only — no LIVE third-party band manipulation.",
        [
            "sources/arxiv-2609-24173-graw-wifi-har-privacy-perturbation.md",
            "concepts/through-wall-detection-sdr-pca.md",
            "concepts/wifi-rf-fingerprinting-open-set.md",
        ],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K356)",
    )

    add_source(
        "arxiv-2609-24934-culturally-responsive-llm-benchmark-audit",
        "Whose Facts Count? — culturally responsive LLM benchmark audit",
        "2609.24934",
        "K357",
        "arxiv-2609.24934-whose-facts-count-a-culturally-responsive-audit.pdf",
        "Benchmark facts embed **cultural defaults**; safety and factuality evals can silently exclude non-dominant contexts. **K357** steals **culturally responsive audit** methodology for benchmark selection — pairs K272 cross-lingual / localized eval discipline. Audit-only; no benchmark poisoning recipes.",
        "concepts/culturally-responsive-llm-benchmark-audit.md",
        "  - concepts/cross-lingual-safety-transfer-lrl.md",
    )
    add_concept(
        "culturally-responsive-llm-benchmark-audit",
        "Culturally responsive LLM benchmark audit",
        "K357",
        "2609.24934",
        "sources/arxiv-2609-24934-culturally-responsive-llm-benchmark-audit.md",
        "English-centric or Western-default benchmarks **mis-rank** models for global deployments. **K357** requires explicit **whose facts count** review when interpreting safety, RAG, or agent eval scores — extend to culturally localized prompts (not literal translation). Pairs cross-lingual safety transfer (K272) and guardrail construct validity (K321).",
        [
            "sources/arxiv-2609-24934-culturally-responsive-llm-benchmark-audit.md",
            "concepts/cross-lingual-safety-transfer-lrl.md",
            "concepts/guardrail-construct-validity-agent-eval.md",
        ],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K357)",
    )

    add_source(
        "arxiv-2609-24972-rrsi-regularized-harness-self-improvement",
        "RRSI — regularized recursive self-improvement of agent harnesses",
        "2609.24972",
        "K358",
        "arxiv-2609.24972-rrsi-regularized-recursive-self-improvement-of-a.pdf",
        "Harness RSI (prompts, control flow, tools, memory) can amplify capability **and** risk without weight changes. **RRSI** adds **regularization** when iteratively editing harness components. **K358**: treat harness self-improvement as **HITL-gated, bounded, reversible** (pairs K324 SafeEvolve + skill misevolution). **Never unattended prod harness auto-evolve.**",
        "concepts/rrsi-regularized-harness-self-improvement.md",
        "  - concepts/safeevolve-harness-policy-co-evolution.md",
    )
    add_concept(
        "rrsi-regularized-harness-self-improvement",
        "RRSI regularized harness self-improvement",
        "K358",
        "2609.24972",
        "sources/arxiv-2609-24972-rrsi-regularized-harness-self-improvement.md",
        "Recursive harness edits are **system-level RSI**: frozen weights, evolving control plane. **K358** steals **regularized component-wise improvement** with explicit safety–utility tradeoffs. Operators run **validation ratchet + rollback** before any harness write; pairs SafeEvolve (K324) and SHE/misevolution policy. **Runtime:** `scripts/k358_rrsi_harness_precheck.py`.",
        [
            "sources/arxiv-2609-24972-rrsi-regularized-harness-self-improvement.md",
            "concepts/safeevolve-harness-policy-co-evolution.md",
            "concepts/faithful-agent-asr-measurement.md",
        ],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K358) + lab-redteam",
    )

    add_source(
        "arxiv-2609-24994-feedback-coding-covert-agentic-communication",
        "Feedback coding for inference-time covert agentic communication",
        "2609.24994",
        "K359",
        "arxiv-2609-24994-feedback-coding-enables-inference-time-covert-ag.pdf",
        "LLM-generated **benign cover text** can carry **covert agentic channels** via feedback coding — black-box receiver, no shared weights required. **K359** is an **authorized-lab eval surface** (pairs K298 inadvertent leakage); **no steganography recipes, codewords, or decoder PoCs in wiki.**",
        "concepts/inference-time-covert-agentic-communication.md",
        "  - concepts/inadvertent-context-leakage.md",
    )
    add_concept(
        "inference-time-covert-agentic-communication",
        "Inference-time covert agentic communication",
        "K359",
        "2609.24994",
        "sources/arxiv-2609-24994-feedback-coding-covert-agentic-communication.md",
        "Multi-agent and tool-using deployments must treat **public-facing model outputs** as potential **covert channels**. Feedback coding enables inference-time signaling without white-box shared statistics. Defensive steal: monitor **benign-output predicates** and channel capacity under realistic agent loops — not refusal alone. **Runtime:** `scripts/k359_covert_agentic_comm_precheck.py`. Lab only.",
        [
            "sources/arxiv-2609-24994-feedback-coding-covert-agentic-communication.md",
            "concepts/inadvertent-context-leakage.md",
            "concepts/asleval-privacy-exposure-displacement.md",
        ],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K359)",
    )

    add_source(
        "arxiv-2609-25364-quantum-rop-chain-selection",
        "Quantum ROP — QUBO gadget selection for exploit construction",
        "2609.25364",
        "K360",
        "arxiv-2609.25364-quantum-rop-using-quantum-algorithms-for-rop-cha.pdf",
        "Explores **QAOA/QUBO** for ROP gadget selection — combinatorial optimization angle on offensive construction. **K360 REFERENCE only** — no ROP chain templates, gadget lists, or exploit PoCs in wiki. Authorized academic lab context only.",
        "concepts/quantum-rop-combinatorial-selection.md",
    )
    add_concept(
        "quantum-rop-combinatorial-selection",
        "Quantum ROP combinatorial selection (REFERENCE)",
        "K360",
        "2609.25364",
        "sources/arxiv-2609-25364-quantum-rop-chain-selection.md",
        "Quantum advantage narratives extend beyond Shor — **combinatorial exploit construction** is a research axis. **K360** is methodology steal only: formulate gadget selection as QUBO with register-clobber interactions. **No wiki payloads**; do not treat NISQ demos as operational capability.",
        [
            "sources/arxiv-2609-25364-quantum-rop-chain-selection.md",
            "concepts/buffer-overflow-exploitation.md",
        ],
        "REFERENCE only — audit mention in lab-redteam",
    )

    add_source(
        "arxiv-2609-26555-rouxii-deception-aware-ai-pentesters",
        "Rouxii — deception-aware AI pentesters vs honeypots",
        "2609.26555",
        "K361",
        "arxiv-2609.26555-rouxii-exploiting-honeypots-with-deception-aware.pdf",
        "Autonomous LLM pentesters can be **derailed by honeypots**; **Rouxii** assumes **counter-deception** in recon and pivots from honeypot fingerprint to exploitation. **K361 authorized lab only** — owned honeypots / written scope; **no counter-deception playbooks in wiki.** Pairs K341 secure pentest agents.",
        "concepts/deception-aware-honeypot-ai-pentesters-rouxii.md",
        "  - concepts/secure-ai-powered-pentest-agents.md",
    )
    add_concept(
        "deception-aware-honeypot-ai-pentesters-rouxii",
        "Deception-aware honeypot AI pentesters (Rouxii)",
        "K361",
        "2609.26555",
        "sources/arxiv-2609-26555-rouxii-deception-aware-ai-pentesters.md",
        "Honeypot evals that assume **deception-naive** agents overstate defensive wins. **K361** steals the **threat-model flip**: attackers with explicit honeypot awareness. For blue team, update agentic pentest eval to include **deception-aware** baselines. **Runtime:** `scripts/k361_rouxii_honeypot_precheck.py`. Authorized lab targets only.",
        [
            "sources/arxiv-2609-26555-rouxii-deception-aware-ai-pentesters.md",
            "concepts/secure-ai-powered-pentest-agents.md",
            "concepts/faithful-agent-asr-measurement.md",
        ],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K361)",
    )

    add_source(
        "arxiv-2609-26682-genai-access-control-policy-enforcement",
        "From Alignment to Access Control — GenAI policy enforcement framework",
        "2609.26682",
        "K362",
        "arxiv-2609.26682-from-alignment-to-access-control-a-framework-for.pdf",
        "GenAI policy spans **alignment, authorization, and runtime access control** — siloed definitions fail in production. **K362** steals **access-control-first policy enforcement** for agents and apps: explicit grants, separation from prompt-only alignment. Pairs K314 recognition≠enforcement and K303 deny/hooks.",
        "concepts/genai-access-control-policy-enforcement.md",
        "  - concepts/recognition-enforcement-gap-instruction-arbitration.md",
    )
    add_concept(
        "genai-access-control-policy-enforcement",
        "GenAI access-control policy enforcement",
        "K362",
        "2609.26682",
        "sources/arxiv-2609-26682-genai-access-control-policy-enforcement.md",
        "Prompt alignment **does not substitute** for **access control** on tools, data, and actions. **K362** maps policy to enforceable grants (who/what/when) for GenAI systems. Implementation steal: external reference monitor + capability-gated tools — residual risk is semantic authorization on authenticated channels (K314).",
        [
            "sources/arxiv-2609-26682-genai-access-control-policy-enforcement.md",
            "concepts/recognition-enforcement-gap-instruction-arbitration.md",
            "concepts/certified-selective-prediction-guardrails.md",
        ],
        ".cursor/rules/cemini-cybersec-mcp-tool-control.mdc (K362)",
    )

    add_source(
        "arxiv-2609-26725-figma-ai-product-design-ood",
        "Does AI Save Time on Product Design? (Figma RCT) — OOD",
        "2609.26725",
        "OOD",
        "arxiv-2609.26725-does-ai-save-time-on-product-design-a-randomized.pdf",
        "Figma Make prompt-to-design RCT with designers and PMs — **product UX productivity**, not cyber-primary. **OOD stub** for cross-wiki routing (@seo-wiki / design workflow) if needed later.",
        "",
        ood=True,
    )

    add_source(
        "arxiv-2609-26749-llm-vulnerability-repair-metrics-failure",
        "Metrics failure in LLM-based code vulnerability repair",
        "2609.26749",
        "K363",
        "arxiv-2609.26749-metrics-failure-in-llm-based-code-vulnerability.pdf",
        "**Compile rate** is an unreliable proxy for single-function C/C++ vuln repair; paper provides **change-aware screening** and controlled experiments on Big-Vul. **K363 audit steal:** report semantic/fix correctness, not build pass alone — pairs secure codegen eval and K335 decompiler fidelity themes.",
        "concepts/llm-vuln-repair-metrics-audit.md",
    )
    add_concept(
        "llm-vuln-repair-metrics-audit",
        "LLM vulnerability repair metrics audit",
        "K363",
        "2609.26749",
        "sources/arxiv-2609-26749-llm-vulnerability-repair-metrics-failure.md",
        "LLM patch benchmarks that reward **compilable but wrong** fixes inflate progress. **K363** requires **change-aware** validation and semantic checks before treating repair ASR as meaningful. HITL before shipping auto-patch pipelines in prod or client engagements.",
        [
            "sources/arxiv-2609-26749-llm-vulnerability-repair-metrics-failure.md",
            "concepts/llm-decompiler-recompilability-fidelity.md",
            "concepts/prompt-structure-cwe-redistribution.md",
        ],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K363)",
    )

    for rel, body in PAGES:
        w(rel, body)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
