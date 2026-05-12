#!/usr/bin/env python3
"""Generate one wiki/sources/<slug>.md per row in .scratch/drive_inventory.tsv.

Each stub gets minimal frontmatter, the Drive file ID, the original title, and
a one-line Narrative summarizing what the source covers based on the title.
Read status defaults to `unread-stub`; the few PDFs the LLM deep-reads are
upgraded by hand after this script runs.

Run from repo root:
    python3 scripts/build_source_stubs.py
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / ".scratch" / "drive_inventory.tsv"
SOURCES = ROOT / "wiki" / "sources"

TODAY = "2026-05-12"

# Heuristics: keyword in title -> entity/concept page(s) to wire as `related`.
# Keep these conservative — better to undercast and let the lint pass surface
# missing edges than to overcast and produce noise.
TAG_RULES: list[tuple[re.Pattern[str], list[str]]] = [
    (re.compile(r"\bmitre|att&ck|att\\&ck\b", re.I), ["entities/frameworks/mitre-attack.md"]),
    (re.compile(r"\bkill chain\b", re.I), ["entities/frameworks/cyber-kill-chain.md"]),
    (re.compile(r"\bcobalt strike\b", re.I), ["entities/tools/cobalt-strike.md"]),
    (re.compile(r"\bcaldera\b", re.I), ["entities/tools/caldera.md"]),
    (re.compile(r"\bmetasploit\b", re.I), ["entities/tools/metasploit.md"]),
    (re.compile(r"\bburp\b", re.I), ["entities/tools/burp-suite.md"]),
    (re.compile(r"\bmaltego\b", re.I), ["entities/tools/maltego.md"]),
    (re.compile(r"\bwazuh\b", re.I), ["entities/tools/wazuh.md"]),
    (re.compile(r"\boscp\b", re.I), ["entities/certifications/oscp.md"]),
    (re.compile(r"\bcrto\b|certified red team", re.I), ["entities/certifications/crto.md"]),
    (re.compile(r"\bceh\b", re.I), ["entities/certifications/ceh.md"]),
    (re.compile(r"\beCPPT|eCPTX|eWPT|eCXD|eCIR|eWPTX|eLearnSecurity\b", re.I), ["entities/vendors/elearnsecurity.md"]),
    (re.compile(r"\bcomptia\b", re.I), ["entities/vendors/comptia.md"]),
    (re.compile(r"\boffensive security\b|\boffsec\b", re.I), ["entities/vendors/offensive-security.md"]),
    (re.compile(r"\bhackthebox|vulnhub|tryhackme\b", re.I), ["entities/platforms/hackthebox.md"]),
    (re.compile(r"\bred team\b|\bred[\s_-]?team\b", re.I), ["concepts/red-team-operations.md"]),
    (re.compile(r"\bblue team|soc analyst|security operation\b", re.I), ["concepts/soc-operations.md"]),
    (re.compile(r"\bpurple team\b", re.I), ["concepts/purple-team-operations.md"]),
    (re.compile(r"\bbug bounty\b", re.I), ["concepts/bug-bounty.md"]),
    (re.compile(r"\badversary emulation|adversary simulation\b", re.I), ["concepts/adversary-emulation.md"]),
    (re.compile(r"\bAV.*bypass|EDR.*bypass|bypass.*AV|bypass.*EDR|evasion technique|bypassing defenses\b", re.I), ["concepts/av-edr-bypass.md"]),
    (re.compile(r"\bbuffer overflow|exploit development|shellcode\b", re.I), ["concepts/exploit-development.md"]),
    (re.compile(r"\bosint\b", re.I), ["concepts/osint-for-cybersecurity.md"]),
    (re.compile(r"\bweb (penTest|pentest|exploit)|web app|vulnerabilidades.*web|ataques web|web attack|WSTG|OWASP\b", re.I), ["concepts/web-pentest-methodology.md"]),
    (re.compile(r"\breverse engineering|malware|threat hunt\b", re.I), ["concepts/malware-analysis.md"]),
    (re.compile(r"\bincident response\b", re.I), ["concepts/incident-response.md"]),
    (re.compile(r"\bcyber.{0,2}war|cyberwarfare\b", re.I), ["concepts/cyberwarfare.md"]),
    (re.compile(r"\b(kids|children|crianças|cyberbullying|child safety|school attack|sexual predator|stalker|safe internet)\b", re.I), ["concepts/cyber-for-kids.md"]),
    (re.compile(r"\bsocial engineering|engenharia social|phishing\b", re.I), ["concepts/social-engineering.md"]),
    (re.compile(r"\bactive directory\b|\bAD\b|\bO365\b|\bWindows.*PenTest|powershell\b", re.I), ["concepts/windows-pentest.md"]),
    (re.compile(r"\blinux.*priv esc|privilege escalation\b", re.I), ["concepts/privilege-escalation.md"]),
    (re.compile(r"\bcloud|AWS|Azure|Google Cloud|GCP|Office365|multi.?cloud\b", re.I), ["concepts/cloud-pentest.md"]),
    (re.compile(r"\bcontainer|kubernetes\b", re.I), ["concepts/container-security.md"]),
    (re.compile(r"\bmobile|iOS|android\b", re.I), ["concepts/mobile-pentest.md"]),
    (re.compile(r"\bIoT|OT|hardware hacking|firewall|wireless\b", re.I), ["concepts/network-security.md"]),
    (re.compile(r"\bblockchain|smart contract\b", re.I), ["concepts/blockchain-security.md"]),
    (re.compile(r"\bgame hacking|anti.cheat\b", re.I), ["concepts/game-hacking.md"]),
    (re.compile(r"\bmetaverso|metaverse\b", re.I), ["concepts/metaverse-security.md"]),
    (re.compile(r"\btor|onion\b", re.I), ["concepts/anonymity-networks.md"]),
    (re.compile(r"\bAPT28\b", re.I), ["entities/threat-actors/apt28.md"]),
    (re.compile(r"\bC for Hackers|C# for|C/C\+\+|programming.{0,3}language\b", re.I), ["entities/programming-languages/c.md"]),
    (re.compile(r"\bpython for hackers|python libs\b", re.I), ["entities/programming-languages/python.md"]),
    (re.compile(r"\bjavascript for hackers\b", re.I), ["entities/programming-languages/javascript.md"]),
    (re.compile(r"\bpowershell\b", re.I), ["entities/programming-languages/powershell.md"]),
    (re.compile(r"\bcareer|carreira|certification|certifications|jr.{0,3}especialista|infosec proeficiency\b", re.I), ["concepts/cybersecurity-careers.md"]),
    (re.compile(r"\bchatgpt\b", re.I), ["concepts/ai-for-cybersecurity.md"]),
    (re.compile(r"\bzero trust\b", re.I), ["concepts/zero-trust.md"]),
    (re.compile(r"\bjoas\b", re.I), ["entities/people/joas-a-santos.md"]),
]


def slugify(title: str) -> str:
    """Stable, filesystem-safe slug derived from the PDF title."""
    base = title.replace(".pdf", "")
    nfkd = unicodedata.normalize("NFKD", base)
    ascii_only = "".join(c for c in nfkd if not unicodedata.combining(c))
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_only).strip("-").lower()
    return slug[:80] or "untitled"


def related_for(title: str) -> list[str]:
    seen: list[str] = []
    for pattern, targets in TAG_RULES:
        if pattern.search(title):
            for t in targets:
                if t not in seen:
                    seen.append(t)
    return seen


def write_stub(file_id: str, title: str) -> Path:
    slug = slugify(title)
    out = SOURCES / f"{slug}.md"
    related = related_for(title)
    related.append("entities/people/joas-a-santos.md")
    related = list(dict.fromkeys(related))  # preserve order, dedupe

    relations_block = "\n".join(f"- {r}" for r in related)
    relations_inline = "\n".join(f"- @{r}" for r in related)

    safe_title = title.replace('"', '\\"').replace('.pdf', '')
    bare_title = title.replace('.pdf', '')
    body = f"""---
title: "{safe_title}"
type: source
tags: [cybersecurity, joas-corpus]
keywords: [cybersecurity, pdf]
related:
{relations_block}
maturity: draft
created: {TODAY}
updated: {TODAY}
read_status: unread-stub
---

## Relations

{relations_inline}

## Raw Concept

- **Title:** {bare_title}
- **Author:** Joas A Santos (see @entities/people/joas-a-santos.md)
- **Type:** PDF e-book / slide deck
- **Location:** Google Drive — `ebooks Joas` folder, file ID `{file_id}` ([open in Drive](https://drive.google.com/file/d/{file_id}/view))
- **Retrieved:** {TODAY}
- **Read status:** unread-stub

## Narrative

Source stub. Title-derived metadata only — body has not been read end-to-end. Upgrade `read_status` to `skimmed`, `read`, or `deep-read` when the source is processed during a future ingest session.

The file lives in the public Google Drive folder shared by the author. The wiki cites this stub from any related entity/concept page so that downstream readers can re-verify by opening the PDF directly.
"""
    out.write_text(body)
    return out


def main() -> None:
    if not INVENTORY.exists():
        raise SystemExit(f"Inventory file not found: {INVENTORY}")
    SOURCES.mkdir(parents=True, exist_ok=True)

    count = 0
    for line in INVENTORY.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        file_id, _, title = line.partition("\t")
        if not (file_id and title):
            continue
        write_stub(file_id, title)
        count += 1

    print(f"Wrote {count} source stubs to {SOURCES}")


if __name__ == "__main__":
    main()
