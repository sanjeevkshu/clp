# CLP Vriksha Architecture & Implementation Decision Log

**Purpose:** Durable, model-agnostic record of architecture, security, editorial, UX and release decisions. Update this file whenever a material decision changes. Treat approved decisions as constraints, not suggestions.

**Last updated:** 2026-10-19  
**Project:** CLP Vriksha — Continuous Learning & Progressive Evolution  
**Production domain:** https://clpvriksha.com  
**Repository:** https://github.com/sanjeevkshu/clp  
**Current work:** PR #8 — Blog, media library and CLP launch milestone  
**Release rule:** Never merge to production without explicit owner approval.

## 1. Product intent

- CLP means **Continuous Learning & Progressive Evolution**.
- Brand promise: **Learn. Apply. Evolve.**
- Learning pathways: CLP Decodes, CLP Masterclass, CLP Perspectives, CLP Evolution Lab.
- The site should feel human, optimistic, editorial, modern and useful—not overly industrial or cluttered.
- Learning should connect knowledge with application, reflection, and sustained evolution.

## 2. Architecture decisions

| ID | Decision | Rationale / constraint | Status |
|---|---|---|---|
| ARCH-001 | Keep the current Jekyll static site on GitHub Pages, with GoDaddy as registrar/DNS management. | Preserve the existing stack and minimize operational complexity. | Approved |
| ARCH-002 | Do not introduce Cloudflare or Supabase. | Explicit owner constraint. | Approved |
| ARCH-003 | Do not add a new backend or paid service without explicit approval. | Control cost, privacy and operational obligations. | Approved |
| ARCH-004 | Use Markdown, YAML front matter, Jekyll layouts/includes and static assets for content. | Version-controlled, portable and reviewable. | Approved |
| ARCH-005 | Blog posts and media records are published only through reviewed pull requests. | Editorial review is the publication gate; merging is a production change. | Approved |
| ARCH-006 | Keep the home hero, primary navigation and menu unchanged during the launch feature work. | Launch content should complement, not disrupt, the established site entry point. | Approved |
| ARCH-007 | Keep launch promotion as a homepage section below the existing hero and a permanent `/launch/` page. | Celebrates the launch without adding a primary-nav item. | Approved |
| ARCH-008 | Use YouTube-hosted video through privacy-enhanced embeds; do not commit video files. | Avoid duplicating video hosting and bloating the repository. | Approved |
| ARCH-009 | Public comments remain on hold. | Static GitHub Pages cannot securely implement first-party comment storage/moderation; GitHub-account requirements are unsuitable for all visitors. | On hold |
| ARCH-010 | Email contributions are documented as a workflow, but the public email address must not be published until a monitored inbox is confirmed. | Never invent a contact address or imply that an unconfigured inbox is operational. | Pending owner input |
| ARCH-011 | Keep Blog and Media discoverability in the footer, not primary navigation. | Add depth without crowding the main menu. | Approved |

## 3. Security decisions and limits

- A Content Security Policy meta element is a **partial mitigation**, not a replacement for HTTP response headers. It must be tested against existing site assets and YouTube embeds before production approval.
- GitHub Pages static HTML cannot set equivalent response headers for HSTS, X-Content-Type-Options, X-Frame-Options or Permissions-Policy. GoDaddy DNS alone cannot add them.
- Do not claim a security scanner issue is fixed unless live response evidence proves it. Record unfixable current-hosting findings as explicit residual risk.
- External links that open a new tab must use appropriate `rel="noopener noreferrer"`.
- Escape untrusted content in templates, use descriptive iframe titles, and avoid adding third-party scripts/services without approval.
- Do not store secrets, credentials, private user data or API keys in the repository.
- Verify the preview's robots/noindex protection and ensure previews do not become canonical or indexable production pages.
- Public comments, email collection, newsletters and other personal-data workflows require a privacy/moderation decision before activation.

See [current hosting security limitations](../security/current-hosting-limitations.md).

## 4. UX, content and accessibility decisions

- Preserve the existing homepage hero, primary navigation and menu for the launch milestone.
- Images belong in page content/front matter; CSS owns presentation, cropping and responsive behavior.
- Use shared button styles for prominent actions; ordinary citations and inline references remain text links.
- All Common Questions/FAQ sections must use the reusable FAQ accordion, wherever they appear.
- Reuse existing components/layouts before adding one-off markup or styling.
- Check dark/light themes, mobile portrait and landscape, desktop, keyboard focus, contrast, reduced motion, accessible labels and horizontal overflow.
- Never invent media title, creator, duration, transcript or learning takeaways. Verify before stating them as facts.
- The CLP launch date is **19 October 2026**. The supplied YouTube URL is the official CLP Vriksha channel launch video: https://youtu.be/_i6jUribYSA.
- Launch treatment: homepage feature below hero, permanent `/launch/` story page, featured media detail page, and contextual footer links. No new primary navigation item.

See [design and authoring principles](../design-and-authoring-principles.md).

## 5. Content publishing contracts

### Blog
1. Draft using `docs/templates/blog-post-template.md`.
2. Put posts in `_posts/YYYY-MM-DD-short-title.md`.
3. Verify factual claims, source links, image rights, metadata, accessibility and CTA patterns.
4. Submit a PR; preview it.
5. Merge only after explicit editorial approval.

### Media
1. Draft using `docs/templates/media-item-template.md` in `_media/`.
2. Use the canonical source URL/video ID and verify playback.
3. Add accurate summary, creator attribution, category, duration/date if verified, thumbnail alt text and transcript/captions where available.
4. The detail page and gallery must be reviewed in preview.
5. Do not publish placeholder metadata or fabricated claims.

### Email submissions
- The public guide may explain the required subject and metadata fields before an inbox is configured.
- Do not display a fake or guessed address.
- Once an owner-confirmed monitored inbox exists, add a mailto link and clear review/response expectations.
- Email receipt is not publication approval; accepted material still follows editorial review and PR publication.

## 6. Release and environment rules

- Work on a feature branch and PR; never push content directly to `master` for production.
- Each meaningful push should include the relevant Actions/preview link in the project update.
- Verify build and validation checks, route output, internal links, media embed, CSP behavior, and preview noindex before recommending merge.
- Keep production unchanged until the owner explicitly approves the merge.
- After approved merge, verify production deployment and provide the live URL.
- If a workflow fails, inspect the failing step/log and correct the root cause; do not claim a preview is ready while deployment is pending or failed.
- Use stylesheet cache-busting query strings when shared CSS changes, following existing project convention.

## 7. Current PR #8 scope

- Static Blog index and article layout.
- Media library and media detail layout.
- Contributor guides and authoring templates.
- Conservative CSP meta policy with documented hosting limitations.
- CLP Vriksha launch feature below the unchanged home hero.
- Permanent launch story at `/launch/`.
- Featured launch film at `/media/featured-video/`, using YouTube video ID `_i6jUribYSA`.
- Footer enhancements linking to launch story, launch film, Blog, Media Library and learning.
- Public comments remain disabled/absent pending a guest-friendly service decision.
- Contribution email address remains unpublished pending owner input.
- Production merge is not authorized by this document.

## 8. Decision change protocol

When changing a decision:
1. Identify the decision ID.
2. Explain the new context, options, risks and impact.
3. Record the owner's explicit decision and date.
4. Update the relevant code, templates, checks and contributor documentation in the same PR where practical.
5. Update the agentic handbook if agent instructions or validation rules change.

## 9. Open decisions / follow-up

- [ ] Confirm the CLP contribution inbox before adding email links.
- [ ] Verify the launch video's exact title, channel attribution and on-video details if not already visible/verified.
- [ ] Test the CSP and YouTube embed in the actual PR preview.
- [ ] Verify the current preview build and SEO/AI readiness workflow.
- [ ] Review and explicitly approve or reject PR #8 before production deployment.
- [ ] Revisit guest-friendly public comments only when the owner is ready to evaluate privacy, moderation, cost and provider dependency.
