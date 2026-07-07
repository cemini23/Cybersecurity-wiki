"""Prompt-injection filtering for untrusted social text."""

from __future__ import annotations

import re


class InjectionDetected(ValueError):
    """Raised when content tries to steer tools, prompts, or credentials."""

    def __init__(self, flags: list[str]):
        super().__init__(f"prompt injection detected: {', '.join(flags)}")
        self.flags = flags


_HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)

_INJECTION_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("ignore_instructions", re.compile(r"\b(ignore|disregard)\s+(all\s+)?(previous|prior|above)\s+instructions\b", re.I)),
    ("system_prompt_request", re.compile(r"\b(system|developer)\s+(prompt|message|instructions)\b", re.I)),
    ("tool_call_bait", re.compile(r"\b(call|invoke|run|execute)\s+(the\s+)?(tool|shell|bash|python|curl|wget)\b", re.I)),
    ("credential_request", re.compile(r"\b(api[_ -]?key|token|secret|password|credential|cookie|session)\b", re.I)),
    ("prod_ingest_bait", re.compile(r"\b(post|send|publish|ship|push)\s+.*\b(prod|production|ceminisuite|discord|member channel)\b", re.I)),
    ("rule_bypass", re.compile(r"\b(bypass|override|disable)\s+.*\b(policy|guardrail|compliance|safety|rules)\b", re.I)),
]


def sanitize_untrusted_text(raw_text: str) -> tuple[str, list[str]]:
    flags: list[str] = []
    if _HTML_COMMENT_RE.search(raw_text):
        flags.append("hidden_html_comment")

    without_comments = _HTML_COMMENT_RE.sub(" ", raw_text)
    sanitized = " ".join(without_comments.split())

    for name, pattern in _INJECTION_PATTERNS:
        if pattern.search(sanitized):
            flags.append(name)

    return sanitized, sorted(set(flags))


def require_no_prompt_injection(raw_text: str) -> tuple[str, list[str]]:
    sanitized, flags = sanitize_untrusted_text(raw_text)
    if flags:
        raise InjectionDetected(flags)
    return sanitized, flags
