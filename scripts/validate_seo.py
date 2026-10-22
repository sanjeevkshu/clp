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
# The legacy URL is intentionally retained as a noindex compatibility route.
# It must canonicalize to the new Learn route and stay out of the sitemap.
NOINDEX_COMPAT_ROUTES = {
    "perspective/index.html": "/learn/clp-perspective/",
}


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
        if rel in NOINDEX_COMPAT_ROUTES:
            if "noindex" not in robots:
                fail(f"{rel}: legacy compatibility route must remain noindex")
            canonical = parser.links[0].get("href", "") if len(parser.links) == 1 else ""
            expected_path = NOINDEX_COMPAT_ROUTES[rel]
            if urlparse(canonical).path.rstrip("/") != expected_path.rstrip("/"):
                fail(f"{rel}: canonical must point to {expected_path}")
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
    if not re.search(r"(?m)^Sitemap:\\s*https://", robots_text):
        fail("robots.txt must contain an absolute HTTPS Sitemap directive")

if sitemap_file.exists():
    sitemap = sitemap_file.read_text(encoding="utf-8")
    urls = re.findall(r"<loc>(.*?)</loc>", sitemap)
    paths = [urlparse(url).path.rstrip("/") or "/" for url in urls]
    for rel, canonical_path in NOINDEX_COMPAT_ROUTES.items():
        legacy_path = "/" + rel.removesuffix("/index.html").rstrip("/")
        if any(urlparse(url).path.rstrip("/") == legacy_path for url in urls):
            fail(f"Sitemap must not include noindex compatibility route: {legacy_path}")
    required_routes = ("/", "/learn/", "/learn/ai-agents/", "/learn/30-day-ai-plan/", "/learn/7-day-ai-challenge/", "/learn/build-a-learning-habit/", "/learn/data-literacy-for-decisions/", "/learn/clp-perspective/")
    for route in required_routes:
        normalized = route.rstrip("/") or "/"
        if normalized == "/":
            present = any(path == "/" or path.count("/") <= 1 for path in paths)
        else:
            present = any(path == normalized or path.endswith(normalized) for path in paths)
        if not present:
            fail(f"Sitemap missing required route: {route}")
    if any("/previews/" in url for url in urls):
        fail("Sitemap must not include pull-request preview URLs")
    if any(urlparse(url).path.endswith((".txt", ".xml")) for url in urls):
        fail("Sitemap must not list robots.txt or sitemap.xml")

if ERRORS:
    print("CLP SEO validation FAILED:")
    for error in ERRORS:
        print(f" - {error}")
    sys.exit(1)

print(f"CLP SEO validation passed ({MODE}): {len(html_files)} HTML pages checked; canonical/meta/JSON-LD/robots/sitemap checks passed.")
