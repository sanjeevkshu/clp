---
name: clp-ai-readiness
description: Improve CLP technical SEO, answerability, GEO/AIO readiness, metadata, structured data, and factual trust without promising rankings.
---

# CLP AI Readiness Skill

## Use when
Creating content, changing metadata, structured data, URL strategy, social cards, search discoverability, or preparing pages for answer engines and AI-assisted retrieval.

## Procedure
1. Read `AGENTS.md` and `docs/agentic/ai-readiness.md`.
2. Identify page intent, audience, and one primary question/task.
3. Validate title, description, canonical, permalink, language, H1, heading structure, and internal links.
4. Make the main answer direct, self-contained, and clear enough to be understood in an excerpt.
5. Define acronyms, explain technical terms, include useful examples/steps, and state relevant limits.
6. Verify claims against credible sources; distinguish fact, interpretation, estimate, and recommendation.
7. Inspect generated HTML and validate JSON-LD. Add schema only when visible content supports it.
8. Ensure social metadata and image metadata are accurate.
9. Check robots/sitemap behavior from actual build output; ensure sitemap covers eligible pages, collection entries, and posts with canonical production URLs and last-modified values where available.
10. For any IA/URL change, trace every internal link, menu item, legacy route, canonical URL, sitemap entry, and required-route guardrail; check for orphaned or duplicate content.
11. Ensure previews are blocked from indexing and production canonicals do not point to previews.
12. Avoid keyword stuffing, fabricated citations, ungrounded claims, and ranking/citation guarantees.

## Acceptance criteria
- Human readers and machines can identify the page's purpose and answer.
- Metadata, canonical, structured data, and visible content agree.
- Claims and references are trustworthy and contextually complete.
- No promise of search ranking, indexing, or AI citation is made.
