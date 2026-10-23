# CLP Project Context and Baseline

## Identity and intent
- Brand: **CLP — Continuous Learning & Progressive Evolution**
- Brand line: **Learn. Apply. Evolve.**
- Repository: `sanjeevkshu/clp`
- Production URL: `https://clpvriksha.com` (verify current `_config.yml` and CNAME before changing).
- Hosting constraint: GitHub Pages. Do not substitute Vercel.
- Primary experience: a mobile-friendly, content-led learning brand with learning library, practical guides, community, and contact surfaces.
- Tone: curious, clear, grounded, practical, evidence-aware; avoid hype and unsupported claims.
- The approved original logo is the source of truth. The repository README notes that a vector approximation was used until the approved original asset is supplied; verify whether that has since changed before replacing any logo.

## Current implementation baseline (verify on each task)
- Static site generated with Jekyll; Markdown pages with YAML front matter.
- Shared layout: `_layouts/default.html`.
- Shared site chrome: `_includes/header.html`, `_includes/footer.html`.
- Shared styling: `assets/css/styles.css` and `assets/css/responsive-polish.css`.
- Shared browser behavior: `assets/js/main.js`.\n- Privacy-first analytics (proposed in PR #13): `_includes/analytics-consent.html`, `assets/js/analytics-consent.js`, and `docs/agentic/analytics-measurement.md`. GTM/GA4 remain inactive in production until PR approval/merge and GTM UI tags are configured.
- Configuration: `_config.yml`; current source has `url: https://clpvriksha.com`, `baseurl: ""`, `permalink: pretty`, and no plugins listed. Recheck current source before changing deployment assumptions.
- Current page sources include `index.md`, `learn.md`, `about.md`, `community.md`, `contact.md`, `learn/ai-agents.md`, `learn/30-day-ai-plan.md`, `learn/7-day-ai-challenge.md`, and `video/` content.
- SEO foundation in default layout includes page title/description, canonical URL, Open Graph/Twitter metadata, favicon, and JSON-LD for Organization, WebSite, and WebPage. Validate emitted HTML rather than assuming every page is correct.
- Theme toggle and responsive navigation exist in shared header/JavaScript; test their current behavior when touching these surfaces.

## Brand tokens documented in README (check CSS for authoritative runtime values)
- Deep Ocean: `#0B1F3B`
- Aquatic Blue: `#00A7E9`
- Sky Aqua: `#38BDF8`
- Violet accent: `#8B5CF6`
- Soft white: `#F8FAFC`

## Information architecture
- Home: orient users to the CLP promise and routes into learning.
- Learn: resource discovery and learning pathways.
- Learning articles: explain concepts, provide actionable practice, answer common questions, and link to related next steps.
- About: mission, learning loop, and values.
- Community: participation, topic suggestions, and interest expression. Current content has described email-app handoff rather than server-side submission; verify before changing claims or forms.
- Contact: contact route and relevant metadata.
- Video: scripts/storyboards and supporting content; do not imply a published video/channel exists unless verified.

## Current work / change boundary
The FAQ accordion, article CTA buttons, and authoring standards are being developed on PR #6:
`https://github.com/sanjeevkshu/clp/pull/6`
Branch: `fix/article-cta-authoring-principles`.
These changes are **unmerged**. The intended preview root is:
`https://sanjeevkshu.github.io/clp/previews/fix-article-cta-authoring-principles/`
Before saying the preview reflects the latest changes, verify the preview deployment workflow posted the exact current PR head SHA. Production remains unchanged until the owner explicitly approves merge.

## Durable project constraints learned from review
- Page-specific images must be chosen in page content/front matter; CSS must not choose a page's image.
- Prominent next-step actions should use established button components; inline references remain text links.
- Prominent “Back to CLP Learn Library” navigation is a secondary button.
- Every Common Questions / FAQ section must use the shared accordion, wherever it appears.
- Reusable patterns must be documented, not only patched in the first page where the issue was noticed.
- When code is pushed, include the relevant preview/deployment link.
- Do not merge without explicit user approval. Do not let a feature preview overwrite production.

## Known items to verify, not silently assume
- Whether the original approved logo has been added.
- Current GitHub Pages settings, default branch, and exact preview workflow status.
- Current cache-busting query values and whether every relevant asset URL is updated consistently.
- Whether contact/community interactions are production-ready or still client-side/email-app handoffs.
- Whether all current FAQ sections use the shared include after the active PR has completed its latest deployment.


## Analytics implementation work (PR #13)
- **Status:** Proposed on `feat/clp-privacy-first-analytics`; do not treat as production behavior until approved and merged.
- PR: https://github.com/sanjeevkshu/clp/pull/13
- GA4 Measurement ID: `G-YMJS96D5TZ`; GTM Web container: `GTM-KQ49L3GG`.
- Consent-gated GTM loader, production-only CSP allowlist, privacy notice, event taxonomy, and build assertions are proposed. The GTM Google tag and custom event tags still require configuration in Google's UI.
