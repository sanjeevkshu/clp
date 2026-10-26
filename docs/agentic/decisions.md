## 2026-10-26 — Branded social extensions
- **Status:** Implemented on feature branch; public channels remain disabled pending owner confirmation and external DNS/redirect setup.
- **Decision:** Reserve `instagram.clpvriksha.com`, `x.clpvriksha.com`, `facebook.clpvriksha.com`, and `linkedin.clpvriksha.com` as proposed HTTPS aliases for official CLP profiles. Keep profile destinations in `_data/social_extensions.yml` and render enabled entries through one shared footer include.
- **Rationale:** Give CLP stable, memorable links without scattering platform URLs throughout content or coupling the static website to a social platform.
- **Consequences:** Aliases are not live until DNS and an HTTP redirect/URL-forwarding service are configured. DNS records alone do not redirect; never enable a channel before its official destination and HTTPS redirect are verified. Do not add credentials or tracking parameters.
- **Evidence / open work:** Confirm official profile URLs, DNS provider/owner, redirect mechanism, and live end-to-end verification. No external DNS change has been made by this PR.

## 2026-10-23 — Privacy-first CLP analytics
- **Status:** Implemented on feature branch; awaiting build/preview verification, GTM UI configuration, owner review, and approval.
- **Decision:** Use GA4 (`G-YMJS96D5TZ`) through GTM (`GTM-KQ49L3GG`), owned administratively by `clpvriksha@gmail.com`. Load the GTM container only on production and only after explicit analytics opt-in; do not load it for rejected/unknown consent or preview builds.
- **Rationale:** CLP needs actionable content and journey measurement without collecting data before consent or contaminating production analytics with preview traffic.
- **Consequences:** Keep consent UI, event taxonomy, CSP allowlist, privacy notice, and QA criteria in the repository. Configure GA4 Google tag and custom event tags in GTM separately; no ad/remarketing/session-replay tags without explicit approval. No merge or production change without owner approval.
- **Evidence / open work:** PR checks and exact-SHA preview deployment must be verified; GTM tags still need configuration in the Google UI; owner must review consent/privacy wording and applicable requirements.

## 2026-10-22 — CLP Perspective belongs within Learn
- **Status:** Implemented on feature branch; awaiting preview verification and approval.
- **Decision:** Use `/learn/perspective/` as the canonical route and represent CLP Perspective as a nested item under Learn in the main navigation. Do not create a `/perspective/` compatibility route because the new landing page has not gone live.
- **Rationale:** Information architecture should reflect that Perspectives is a learning substream, not a peer-level top navigation destination.
- **Consequence:** Route changes must update internal links, navigation, metadata/canonical URLs, sitemap coverage, and SEO/AI-readiness checks together. Add a redirect only if a prior route was published or externally linked.

# CLP Decision Log

Record durable decisions here. Add new entries in reverse chronological order. Each entry should state date, status, decision, rationale, consequences, and the evidence or owner needed to revisit it.

## 2026-10-16 — Model-neutral project knowledge pack
- **Status:** Implemented in current feature branch; not merged.
- **Decision:** Keep canonical agent instructions, project architecture, design language, content patterns, asset rules, QA/release, and AI-readiness in plain Markdown under `AGENTS.md`, `docs/agentic/`, and `skills/*/SKILL.md`.
- **Rationale:** Knowledge should travel across AI models and tools without relying on chat history or a proprietary prompt format.
- **Consequence:** Any model can be given the entry contract and only the skills relevant to a task. Durable project changes must update the relevant docs and skill.

## 2026-10-16 — Every FAQ uses one shared accordion
- **Status:** Implemented in current feature branch; deployment/visual verification must be checked against the latest PR head before claiming complete.
- **Decision:** Use `_includes/faq-accordion.html` with page-specific `faq_items` in front matter for every Common Questions / FAQ section.
- **Rationale:** Consistent interaction, accessibility, style, and reduced duplication regardless of page location.
- **Consequence:** Do not add a local FAQ implementation. Extend the shared include if the content needs a new capability.

## 2026-10-16 — Content owns image selection
- **Status:** Established project rule.
- **Decision:** Page content/front matter selects the image and path; CSS controls only display and presentation.
- **Rationale:** Authors must be able to change an image without rewriting CSS or coupling the asset to a selector.
- **Consequence:** New page imagery must be configurable in content and use `relative_url` for local paths.

## 2026-10-16 — Prominent actions use shared buttons
- **Status:** Established project rule.
- **Decision:** Meaningful primary/secondary actions use established button components; inline citations/references remain text links. Learning articles use a secondary “Back to CLP Learn Library” button.
- **Rationale:** Clear affordance and consistent touch/keyboard behavior without turning every link into a button.
- **Consequence:** Reuse `learn-card-button` / `content-button` and the relevant containers unless the design system is deliberately updated.

## 2026-10-15 — GitHub Pages and production safety
- **Status:** Established project constraint; verify current workflows before acting.
- **Decision:** GitHub Pages is the hosting target; production is built from `master` (verify current default branch); PR previews live under a nested `/previews/<branch-slug>/` path.
- **Rationale:** Keep feature validation separate from production and avoid preview content replacing the live site.
- **Consequence:** Do not use Vercel, do not merge without explicit approval, and check that preview deployment is from the exact PR head SHA.

## Open questions / verify before decisions
- **Approved logo:** Is the original approved logo asset now available and approved for use?
- **Custom domain:** Is/when will a custom domain be configured? Do not alter URL/baseurl until approved and planned.
- **Forms:** Is a real backend/CRM integration required, or is the current email-app handoff intentionally sufficient?
- **Analytics/privacy:** Which analytics, if any, are approved, with what consent and data-retention rules?
- **AI features:** Is any public-facing AI functionality planned? Current AI-assisted development does not imply an AI runtime on the site.
- **Content ownership:** Who approves factual, brand, legal, and accessibility-sensitive content changes?
- **Structured data:** Which page types warrant additional schema after review of rendered output and current search guidance?
