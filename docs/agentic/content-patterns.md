# CLP Content Model and Authoring Patterns

## Page front matter
Every content page should preserve the Jekyll front matter structure and normally include:
- `title`: unique, useful page title.
- `description`: concise, accurate summary suitable for metadata and search snippets.
- `permalink`: stable intended route, with trailing slash convention consistent with `permalink: pretty`.
- Page-specific data such as `faq_items` and image paths when that improves authoring clarity and repeatability.

Do not invent unsupported metadata or promise capabilities that the current site does not deliver.

## Content principles
- Lead with the learner's need, not internal jargon.
- Explain the concept in plain language before adding complexity.
- Use a practical example and an action a reader can try.
- State limitations, uncertainty, and responsible-use boundaries when relevant.
- Prefer useful, specific headings and concise paragraphs.
- Avoid unsupported statistics, fabricated citations, exaggerated claims, and generic filler.
- Keep language consistent with “Learn. Apply. Evolve.” and the CLP tone.

## Page patterns
### Landing/home page
1. Clear promise and context.
2. Route into key pathways/resources.
3. Explain the value of the learning loop.
4. Meaningful CTA(s).
5. Relevant FAQs, if present, through the shared accordion.

### Learning library/resource card
- Series/category label.
- Clear title.
- Outcome-oriented summary.
- Content-selected image with meaningful alt text.
- Existing `learn-card-button` pattern for the card's primary action.
- Avoid duplicate links that create confusing repeated focus stops unless the card pattern intentionally requires them.

### Learning article
- YAML title/description/permalink.
- Article hero image selected in page content and meaningful alt text.
- Eyebrow/kicker and one H1 with a useful lede.
- Structured body with examples, actionable steps, key takeaway, and relevant guardrails.
- Secondary “Back to CLP Learn Library” button near the top.
- FAQ items stored as `faq_items` in front matter and rendered by the shared accordion.
- Related learning CTAs grouped using the established `content-button` and `article-cta-group` pattern.
- Use distinct IDs for section headings and CTA aria labels.

## FAQ authoring contract
Front matter example:
```yaml
faq_items:
  - question: "How do I get started?"
    answer: >-
      Start with one low-risk task and compare the result with your usual approach.
```
Render:
```liquid
{% raw %}{% include faq-accordion.html id="unique-page-faq" title="Common questions" items=page.faq_items %}{% endraw %}
```
Optional `kicker` is supported. The section `id` must be unique on the page. All FAQs use this include, no matter where they appear. Keep answers concise, direct, accurate, and useful. If richer answer markup is required, extend the component contract intentionally rather than bypassing it.

## CTA contract
- Use buttons for primary/secondary actions with a clear verb and destination.
- Ordinary inline references/citations remain text links.
- Reuse `learn-card-button` for learning cards and `content-button` for article/content CTAs unless the design system has been deliberately evolved.
- Keep destination URLs in content, use `relative_url` for internal links, and hide decorative arrow glyphs from assistive technology.

## Content integrity and lifecycle
- Verify claims and external references before publication.
- Identify content that may go stale (product features, policy, statistics, dates) and either date it or avoid brittle claims.
- Do not fabricate testimonials, community participation, video publication, subscriptions, backend form submission, or analytics.
- If a form opens the visitor's email app instead of submitting to a server, state that clearly.
- New content patterns should be documented and added to the QA checklist.


## Information architecture and series balance
CLP is a continuous-learning destination, not an AI-only publication. Keep the four editorial series distinct and useful:
- **CLP Decodes:** plain-language explanations of concepts, including data literacy and emerging technology.
- **CLP Masterclass:** structured, step-by-step practical learning plans and skills.
- **CLP Perspectives:** implications, trade-offs, and considered viewpoints about work, technology, and change.
- **CLP Evolution Lab:** small experiments, learning habits, and reflective challenges that turn ideas into practice.

A new article should serve a clear learner need, add a distinct destination, and link to a relevant next step. Avoid publishing several near-duplicate AI explainers simply to increase page count. The learning library should balance technology fluency with transferable capabilities such as learning how to learn, data-informed decisions, critical thinking, and responsible application.

The current expansion adds:
- **Learning Habit Kaise Banayein?** — Evolution Lab; practical learning loop, active recall, cues, and reflection.
- **Data Literacy: Turn Data into Better Decisions** — Decodes; asking useful questions, checking context and data quality, interpreting patterns, and communicating uncertainty.

For every new page, verify that it is linked from the Learn library, has a unique title/description/canonical URL, uses the shared FAQ accordion, includes relevant internal links, and appears in generated sitemap output. The SEO validation workflow's required-route list should be updated when the project intentionally adds or removes core learning routes; sitemap generation itself should remain automatic for eligible pages.
