#!/usr/bin/env python3
"""Conservative whitespace remediation; emits a report for human review.

This tool only normalizes trailing whitespace and final newlines in explicitly
provided, repository-relative text files. It never commits or pushes changes.
"""
from __future__ import annotations
import json
import os
import sys
from pathlib import Path

ALLOWED_SUFFIXES = {".md", ".markdown", ".html", ".css", ".js", ".json", ".yml", ".yaml", ".txt", ".xml", ".py"}
ROOT = Path.cwd().resolve()
changed: list[str] = []
skipped: list[str] = []
for raw in sys.argv[1:]:
    candidate = (ROOT / raw).resolve()
    if ROOT not in candidate.parents or not candidate.is_file() or candidate.suffix.lower() not in ALLOWED_SUFFIXES:
        skipped.append(raw)
        continue
    try:
        original = candidate.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        skipped.append(raw)
        continue
    normalized = "\n".join(line.rstrip() for line in original.splitlines()).rstrip() + "\n"
    if normalized != original:
        candidate.write_text(normalized, encoding="utf-8")
        rel = candidate.relative_to(ROOT).as_posix()
        changed.append(rel)
        print(f"SAFE_FIX: normalized whitespace in {rel}")
report = {"mode": "whitespace-only", "changed_files": changed, "skipped_files": skipped, "writes_commits_or_pushes": False}
# Refuse to follow or overwrite an existing path (including a symlink) in the
# checkout. The report is created atomically and exclusively for this run.
report_path = ROOT / "remediation-report.json"
try:
    report_fd = os.open(report_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
except FileExistsError:
    print("ERROR: remediation-report.json already exists; refusing to overwrite it.")
    raise SystemExit(2)
with os.fdopen(report_fd, "w", encoding="utf-8") as report_file:
    report_file.write(json.dumps(report, indent=2) + "\n")
print(f"Safe auto-remediation complete; files changed: {len(changed)}; skipped: {len(skipped)}")
