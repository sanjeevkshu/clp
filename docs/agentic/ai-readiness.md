# CLP Search and AI Readiness (SEO / GEO / AIO)

This document defines practical publishing requirements for discoverability in search engines, answer engines, generative interfaces, and AI-assisted research. It does not promise ranking, citation, or recommendation outcomes.

## Technical foundation
- Preserve a unique, descriptive `title`, `description`, and stable `permalink` for each indexable page.
- Verify canonical URLs use the intended production origin and route, not a preview URL.
- Use valid semantic HTML, a clear H1, ordered headings, descriptive links, meaningful image alt text, and accessible interaction.
- Use `relative_url` for internal paths and `absolute_url` for metadata.
- Inspect the generated HTML for metadata, canonical URL, robots directives, social cards, and structured data.
- Verify sitemap and robots behavior from the actual build/configuration; include eligible pages, media collection items, and posts automatically, with canonical production URLs and last-modified dates where available; do not assume files exist.
- When routes or information architecture change, update all internal links, menu hierarchy, legacy-route handling, sitemap output, required-route checks, canonical metadata, and structured-data URLs in the same change.
- PR preview paths should remain blocked from indexing, as implemented by the current preview workflow's `robots.txt`; verify the generated output and do not publish preview URLs as canonical content.

## Structured data
- The current default layout emits JSON-LD for Organization, WebSite, and WebPage. Treat this as a starting point, not proof of complete schema coverage.
- Structured data must describe visible, accurate page content and follow the relevant schema vocabulary.
- Add FAQPage, Article, VideoObject, BreadcrumbList, or other schema only when the page content and search-engine guidance justify it; never add schema merely to chase rich results.
- Validate JSON syntax and emitted values after Jekyll/Liquid rendering. Avoid duplicate/conflicting entities and unsupported claims.

## Answerability and citation readiness
- Lead with a direct, self-contained explanation that answers the page's main question.
- Define uncommon terms, explain acronyms at first use, and provide context sufficient for an excerpt to make sense outside the page.
- Prefer clear question headings, concise answers, meaningful examples, steps, comparisons, and explicit limitations.
- Attribute claims to trustworthy primary sources when needed; include publication/update dates for time-sensitive content.
- Distinguish established facts, interpretation, estimates, and recommendations.
- Avoid vague marketing copy, keyword stuffing, fabricated references, and ungrounded claims about model capabilities.
- Keep pages focused around one primary learner intent and useful adjacent questions.

## Trust and provenance
- Show clear authorship/organization identity where appropriate.
- Explain limitations, prerequisites, risks, and responsible use of AI where relevant.
- Keep contact/community and media publication claims aligned with what actually works.
- Preserve source links and asset provenance. Generated content should be reviewed by a knowledgeable human before publication.
- Do not publish personal, confidential, or sensitive data as examples.

## Machine-readable and human-usable content
- Use HTML that preserves meaning without relying exclusively on CSS or JavaScript.
- Keep important text as text, not baked into images.
- Use descriptive filenames and alt text.
- Avoid duplicate pages and conflicting canonical URLs.
- Use stable internal links and consistent naming for CLP series and learning resources.

## AI-readiness review checklist
- [ ] Page intent and intended audience are clear.
- [ ] Title, description, canonical, route, and language are correct.
- [ ] H1 and section headings accurately describe content.
- [ ] Core question is answered directly and accurately.
- [ ] Claims are sourced or clearly framed as interpretation.
- [ ] Examples are practical, safe, and non-sensitive.
- [ ] Relevant structured data is valid and supported by visible content.
- [ ] Internal links, external references, and media claims are verified.
- [ ] Preview is not indexable and production canonical does not point to preview.
- [ ] No ranking, indexing, or AI-citation guarantee is implied.
