---
name: clp-content-patterns
description: Create and maintain CLP pages, learning articles, CTAs, and FAQ content using reusable Jekyll authoring patterns.
---

# CLP Content Patterns Skill

## Use when
Writing or restructuring Markdown pages, YAML front matter, learning resources, articles, FAQs, navigation links, metadata, or editorial CTAs.

## Procedure
1. Read `AGENTS.md`, `docs/agentic/content-patterns.md`, and `docs/content-management.md`.
2. Inspect nearby pages for established patterns and current facts.
3. Preserve valid YAML front matter and stable permalinks; use a unique title and accurate description.
4. Keep page-specific copy, FAQ data, CTA destinations, and selected image paths in content/front matter.
5. Render every FAQ/Common Questions section with `_includes/faq-accordion.html` and `faq_items`.
6. Use `learn-card-button` for learning cards and `content-button` for prominent content/article actions. Keep inline references as text links.
7. Learning articles need a secondary “Back to CLP Learn Library” button and a clear, relevant next step.
8. Use `relative_url` for internal links and local assets.
9. Check factual accuracy, source quality, reader value, accessibility, metadata, and rendered output.
10. Update documentation and tests if a new content pattern is introduced.

## Acceptance criteria
- Content is specific, actionable, accurate, and aligned with CLP tone.
- No unsupported product, community, video, form, or AI-capability claims.
- All FAQs use the shared accordion; no duplicated FAQ markup.
- Prominent CTAs use shared buttons; citations/references remain inline links.
