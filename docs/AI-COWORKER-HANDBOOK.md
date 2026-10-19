# CLP Vriksha AI Coworker & Agentic Readiness Handbook

This handbook is the model-agnostic entry point for any AI coworker, coding agent or human contributor working on CLP Vriksha. Read it before changing code, content, architecture, security, or deployment.

## 1. Mission

Help CLP Vriksha build a durable, accessible and trustworthy learning experience that turns knowledge into application and progressive evolution. Brand promise: **Learn. Apply. Evolve.**

The website is a public learning platform, not merely a collection of pages. Changes must preserve brand intent, editorial trust, accessibility, maintainability, and the owner's explicit release controls.

## 2. Required reading order

Before doing project work, inspect:
1. `docs/architecture/decision-log.md` — approved decisions, constraints, current PR and open decisions.
2. `docs/design-and-authoring-principles.md` — visual, content, accessibility and reusable component rules.
3. `docs/content-management.md` — publishing conventions, FAQ accordion and authoring workflow.
4. `docs/security/current-hosting-limitations.md` — security posture and current hosting limitations.
5. Relevant templates in `docs/templates/`.
6. Current GitHub Actions workflows and the target branch/PR state.

Do not rely only on prior chat summaries. The repository is the durable source of truth. If code conflicts with the decision log, flag the conflict and seek owner direction rather than silently choosing.

## 3. Non-negotiable guardrails

- **Never merge or deploy to production without explicit owner approval.**
- Keep work in a feature branch and pull request.
- Preserve the existing homepage hero, primary navigation and menu unless the owner explicitly changes that decision.
- Do not introduce Cloudflare, Supabase, a new backend, a paid service, analytics, tracking, comments or data collection without explicit approval.
- Public comments are on hold.
- Do not publish a contribution email address until the owner supplies a real, monitored inbox.
- Do not invent channel URLs, video metadata, author identities, dates, duration, transcripts, sources or other factual claims.
- Do not commit credentials, tokens, secrets or personal data.
- Treat preview build status as unknown until the actual workflow reports success; do not manufacture preview URLs.
- Do not describe a security issue as fixed without evidence.
- Keep production untouched while PR work is in progress.

## 4. Architecture map

- Static site generator: Jekyll.
- Hosting/deployment: GitHub Pages via GitHub Actions.
- Domain/DNS: `clpvriksha.com`; GoDaddy is the current registrar/DNS management interface.
- Content: Markdown with YAML front matter.
- Layouts and reusable markup: `_layouts/`, `_includes/`.
- Content collections: `_posts/` for Blog, `_media/` for media entries.
- Styles: `assets/css/`, including shared editorial/media styles.
- Templates and guidance: `docs/templates/`, `docs/content-management.md`, design and security documentation.
- PR preview: built by GitHub Actions, noindex protected, and must be validated before review.
- Video: externally hosted on YouTube; use privacy-enhanced embed where compatible with policy.
- No database/backend is part of the approved current architecture.

## 5. UX and authoring contract

- Keep content values in Markdown/front matter and reusable presentation in layouts/includes/CSS.
- Configure page imagery in content/front matter where feasible; use CSS for presentation, not hardcoded page-specific image content.
- Use existing design tokens/classes and button patterns. Do not introduce a new button style if a shared one fits.
- Every Common Questions/FAQ section uses the shared `faq-accordion.html` include with unique IDs and page-specific `faq_items`.
- Prominent actions are buttons; normal citations and inline references remain text links.
- Make layouts responsive at mobile portrait, mobile landscape, tablet and desktop.
- Test both light and dark themes, keyboard navigation, focus visibility, contrast, reduced motion, alt text, iframe title, and no horizontal overflow.
- Preserve semantic headings and descriptive link labels.
- Avoid excessive visual clutter and unnecessary motion.

## 6. Content quality and media truthfulness

For every new article or media entry:
- Use a unique page title, useful description, canonical internal URL and accurate metadata.
- Check source validity, factual accuracy, attribution, usage rights, language, intended audience and next action.
- Never use placeholder/example URLs or fake metadata in public content.
- Verify all outbound links and local routes.
- For YouTube, use the verified video ID; do not upload video files to the repo.
- Add thumbnail alt text, transcript/captions links and duration/date only when verified.
- Use the shared article/media templates and ensure any FAQ follows the reusable accordion rule.
- Email submissions are proposals only; publication still requires review and a merged PR.

## 7. Security and privacy

- Read the current hosting security limitations before changing CSP, embed sources or security configuration.
- Meta CSP is partial mitigation and cannot replace server response headers.
- GitHub Pages cannot set all response headers such as HSTS, X-Content-Type-Options, X-Frame-Options and Permissions-Policy from static HTML. Do not add fake meta substitutes.
- Test CSP against site scripts, styles, images, and YouTube privacy-enhanced embeds.
- Use escaping in templates and safe link attributes.
- Do not add a third-party provider or send user data to a new service without explicit owner approval and documented purpose, privacy implications, cost and exit plan.
- Do not enable comments, contact forms, newsletters or other personal-data collection until moderation/privacy decisions and operational ownership are defined.

## 8. Required change workflow

1. **Understand:** read decision log and relevant implementation; inspect current branch and latest PR state.
2. **Plan:** state intended changes, affected routes/components, risks and checks. Ask one concise question only when an essential owner decision blocks safe work.
3. **Implement:** small, reviewable changes in the existing feature branch. Prefer shared components and no new dependencies.
4. **Document:** update decision log and relevant docs whenever architecture, security, authoring, data handling, deployment or operational decisions change.
5. **Validate:** build, workflow tests, internal links, route output, responsive/theme/accessibility checks, CSP/embed behavior, SEO metadata, and preview noindex.
6. **Report:** include exact changed files, commit/PR URL, latest workflow links/status, preview URL only when verified, known limitations, and next decision needed.
7. **Stop before production:** do not merge without explicit approval.

## 9. Definition of done

A change is not done merely because code was committed. It is done when:
- the implementation matches approved decisions;
- content and metadata are accurate;
- shared components and design standards are followed;
- the build and relevant validation workflows pass;
- the actual PR preview is available and reviewed;
- accessibility, responsiveness, dark/light themes and security policy are checked where relevant;
- documentation/decision records are updated;
- residual risks are explicit;
- production remains unchanged until the owner authorizes merge.

## 10. Agent handoff / session continuity format

At the end of each substantial work session, update a short status section in the decision log or PR description with:
- current branch and PR number;
- latest commit SHA;
- files and behavior changed;
- workflows and their actual state;
- verified preview URL or explicit reason it is unavailable;
- open risks and decisions;
- next action;
- confirmation that production has not been merged/deployed.

Do not store sensitive user information in handoff notes. Do not claim an action succeeded unless tool output confirms it.

## 11. Suggested future skills to maintain

Keep model-independent task recipes in `docs/skills/` (or another agreed documentation path) for:
- architecture review and decision records;
- CLP design system and component reuse;
- content/article and media production;
- asset creation, licensing and accessibility;
- SEO, structured data, AEO/GEO and AI-readiness validation;
- security and privacy review;
- CI/CD and safe preview validation;
- release readiness and post-deployment verification;
- editorial moderation and contribution intake.

Each skill should include purpose, required inputs, constraints, step-by-step workflow, validation checklist, failure modes, expected output, and documentation update requirements. Skills are instructions, not permission to override owner decisions.
