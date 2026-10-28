#!/usr/bin/env python3
"""Automated CLP SEO and crawl-readiness checks for generated Jekyll output."""
from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
MODE = sys.argv[2] if len(sys.argv) > 2 else "production"
ERRORS: list[str] = []
class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta: dict[str, list[str]] = {}
        self.links: list[dict[str, str]] = []
        self.jsonld: list[str] = []
        self._in_jsonld = False
        self._jsonld_text: list[str] = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta":
            key = attrs.get("name") or attrs.get("property")
            if key:
                self.meta.setdefault(key.lower(), []).append(attrs.get("content", ""))
        elif tag == "link" and attrs.get("rel", "").lower() == "canonical":
            self.links.append(attrs)
        elif tag == "script" and attrs.get("type") == "application/ld+json":
            self._in_jsonld = True
            self._jsonld_text = []

    def handle_data(self, data):
        if self._in_jsonld:
            self._jsonld_text.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self._in_jsonld:
            self.jsonld.append("".join(self._jsonld_text))
            self._in_jsonld = False


def fail(message: str) -> None:
    ERRORS.append(message)


if not ROOT.is_dir():
    print(f"ERROR: generated site directory not found: {ROOT}")
    sys.exit(1)

html_files = sorted(ROOT.rglob("*.html"))
if not html_files:
    fail("No generated HTML pages found.")

for html_file in html_files:
    parser = PageParser()
    parser.feed(html_file.read_text(encoding="utf-8"))
    rel = html_file.relative_to(ROOT).as_posix()

    if not parser.meta.get("description") or not parser.meta["description"][0].strip():
        fail(f"{rel}: missing/empty meta description")
    if len(parser.links) != 1 or not parser.links[0].get("href", "").startswith("https://"):
        fail(f"{rel}: expected exactly one absolute HTTPS canonical URL")
    if rel == "learn/perspective/index.html" and len(parser.links) == 1:
        canonical_path = urlparse(parser.links[0].get("href", "")).path.rstrip("/")
        if canonical_path != "/learn/perspective":
            fail(f"{rel}: canonical URL must resolve to /learn/perspective/")
    if not parser.meta.get("og:title") or not parser.meta.get("og:description"):
        fail(f"{rel}: missing Open Graph title/description")
    if not parser.jsonld:
        fail(f"{rel}: missing JSON-LD structured data")
    for block in parser.jsonld:
        try:
            json.loads(block)
        except json.JSONDecodeError as exc:
            fail(f"{rel}: invalid JSON-LD ({exc})")

    robots = " ".join(parser.meta.get("robots", [])).lower()
    if MODE == "preview":
        if "noindex" not in robots:
            fail(f"{rel}: preview build must include robots noindex")
    elif MODE == "production":
        if rel == "sitemap/index.html":
            if "noindex" not in robots or "follow" not in robots:
                fail(f"{rel}: HTML site map must be noindex,follow")
        elif "noindex" in robots or "index" not in robots:
            fail(f"{rel}: production build must be indexable")

sitemap_file = ROOT / "sitemap.xml"
robots_file = ROOT / "robots.txt"
if not sitemap_file.exists():
    fail("Missing generated sitemap.xml")
if not robots_file.exists():
    fail("Missing generated robots.txt")
else:
    robots_text = robots_file.read_text(encoding="utf-8")
    if not re.search(r"(?m)^Sitemap:\s*https://clpvriksha\.com/sitemap\.xml\s*$", robots_text):
        fail("robots.txt must contain the canonical HTTPS sitemap URL")
    for bot in ("OAI-SearchBot", "Google-Extended", "PerplexityBot", "Claude-SearchBot", "Claude-User", "GPTBot", "ClaudeBot"):
        if not re.search(rf"(?mi)^User-agent:\s*{re.escape(bot)}\s*$", robots_text):
            fail(f"robots.txt missing explicit AI discovery policy for {bot}")
    for bot in ("OAI-SearchBot", "PerplexityBot", "Claude-SearchBot", "Claude-User"):
        if not re.search(rf"(?mi)^User-agent:\s*{re.escape(bot)}\s*\nAllow:\s*/\s*$", robots_text):
            fail(f"robots.txt must explicitly allow {bot}")
    for bot in ("GPTBot", "ClaudeBot", "Google-Extended"):
        if not re.search(rf"(?mi)^User-agent:\s*{re.escape(bot)}\s*\nDisallow:\s*/\s*$", robots_text):
            fail(f"robots.txt must explicitly disallow {bot}")

if MODE == "production" and (ROOT / "perspective" / "index.html").exists():
    fail("Production build must not generate the unpublished legacy /perspective/ route")

if sitemap_file.exists():
    sitemap = sitemap_file.read_text(encoding="utf-8")
    urls = re.findall(r"<loc>(.*?)</loc>", sitemap)
    paths = [urlparse(url).path.rstrip("/") or "/" for url in urls]
    required_routes = ("/", "/learn/", "/learn/ai-agents/", "/learn/30-day-ai-plan/", "/learn/7-day-ai-challenge/", "/learn/build-a-learning-habit/", "/learn/data-literacy-for-decisions/", "/learn/perspective/")
    for route in required_routes:
        normalized = route.rstrip("/") or "/"
        present = any(path == normalized for path in paths)
        if not present:
            fail(f"Sitemap missing required route: {route}")
    if any("/previews/" in url for url in urls):
        fail("Sitemap must not include pull-request preview URLs")
    if any(urlparse(url).path.rstrip("/") == "/perspective" for url in urls):
        fail("Sitemap must not include the unpublished legacy /perspective/ route")
    if any(urlparse(url).path.endswith((".txt", ".xml")) for url in urls):
        fail("Sitemap must not list robots.txt or sitemap.xml")

if ERRORS:
    print("CLP SEO validation FAILED:")
    for error in ERRORS:
        print(f" - {error}")
    sys.exit(1)

print(f"CLP SEO validation passed ({MODE}): {len(html_files)} HTML pages checked; canonical/meta/JSON-LD/robots/sitemap checks passed.")
