#!/usr/bin/env python3
"""Conservative repository hygiene fixer for the CLP quality agent.

Only normalizes trailing whitespace and final newlines in text files passed by
the workflow. It never rewrites URLs, metadata, policies, or structured data.
Changes must remain on a PR branch for human review.
"""
from __future__ import annotations
import sys
from pathlib import Path

ALLOWED_SUFFIXES = {".md", ".markdown", ".html", ".css", ".js", ".json", ".yml", ".yaml", ".txt", ".xml", ".py"}
CHANGED = 0
for raw in sys.argv[1:]:
    path = Path(raw)
    if not path.is_file() or path.suffix.lower() not in ALLOWED_SUFFIXES:
        continue
    try:
        original = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue
    normalized = "\n".join(line.rstrip() for line in original.splitlines()).rstrip() + "\n"
    if normalized != original:
        path.write_text(normalized, encoding="utf-8")
        print(f"SAFE_FIX: normalized whitespace in {path}")
        CHANGED += 1
print(f"Safe auto-remediation complete; files changed: {CHANGED}")
