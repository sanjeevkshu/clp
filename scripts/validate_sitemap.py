#!/usr/bin/env python3
"""Validate the generated CLP XML sitemap as XML and check URL hygiene."""
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

root_dir = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
file = root_dir / "sitemap.xml"
if not file.is_file():
    raise SystemExit(f"ERROR: missing {file}")

try:
    xml_root = ET.parse(file).getroot()
except ET.ParseError as exc:
    raise SystemExit(f"ERROR: sitemap.xml is not well-formed XML: {exc}")

ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
if xml_root.tag != f"{ns}urlset":
    raise SystemExit(f"ERROR: unexpected sitemap root/namespace: {xml_root.tag}")

entries = xml_root.findall(f"{ns}url")
if not entries:
    raise SystemExit("ERROR: sitemap.xml contains no <url> entries")

seen = set()
for entry in entries:
    loc = entry.findtext(f"{ns}loc")
    if not loc:
        raise SystemExit("ERROR: sitemap entry is missing <loc>")
    parsed = urlparse(loc.strip())
    if parsed.scheme != "https" or parsed.netloc.lower() != "clpvriksha.com":
        raise SystemExit(f"ERROR: sitemap URL must be absolute HTTPS on clpvriksha.com: {loc}")
    if loc in seen:
        raise SystemExit(f"ERROR: duplicate sitemap URL: {loc}")
    seen.add(loc)
    if parsed.path.rstrip("/") == "/sitemap":
        raise SystemExit("ERROR: user-facing /sitemap/ page must be excluded from XML sitemap")
    if "/previews/" in parsed.path:
        raise SystemExit(f"ERROR: preview URL in sitemap: {loc}")

required = {
    "https://clpvriksha.com/",
    "https://clpvriksha.com/learn/",
    "https://clpvriksha.com/learn/perspective/",
}
missing = sorted(required - seen)
if missing:
    raise SystemExit("ERROR: sitemap missing required routes: " + ", ".join(missing))

print(f"Sitemap validation passed: {len(entries)} valid, unique, absolute HTTPS URLs; namespace and required routes verified.")
