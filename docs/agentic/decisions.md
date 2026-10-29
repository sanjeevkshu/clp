## 2026-10-29 — Public aggregate webmaster dashboard and Google API federation

- **Status:** Design and documentation implemented on PR #21 feature branch; PR is unmerged. Manual federation/access-validation workflow is committed but has not yet demonstrated real Google API access. Actual scheduled refresh/publication pipeline is not implemented.
- **Decision:** Keep `/dashboard/` publicly accessible but noindex, excluded from the sitemap and header navigation, and linked from footer Resources. Public output must be sanitized, allowlisted aggregate metrics only. Authenticate trusted GitHub Actions runs using GitHub OIDC → Google Cloud Workload Identity Federation (WIF), with trust limited to repository `sanjeevkshu/clp` and `refs/heads/master`; use a dedicated read-only service account and no long-lived JSON key where WIF works.
- **Rationale:** Provide transparent website health reporting without exposing credentials or visitor-level data, and avoid paid backend infrastructure in the initial iteration.
- **Consequences:** PR checks remain secret-free. A master-only manual workflow validates GA4 and Search Console read access before the separate refresh pipeline is built. The future refresh should run weekly Monday 03:30 UTC (09:00 IST) and on demand; validate a versioned public schema, privacy filters, cohort suppression, source completeness and freshness before atomic publication. Preserve last-known-good data on failure. Never publish raw provider responses, identifiers, PII, query strings or partial results. A proposed threshold below 10 is a starting control, not proof of anonymization.
- **Knowledge base:** See [technical design](../WEBMASTER-DASHBOARD-DATA-PLAN.md), [functional inventory](public-analytics-dashboard-functional-inventory.md), [privacy/security contract](public-analytics-dashboard.md), [portable skill](../../skills/public-analytics-dashboard/SKILL.md), and [handbook](README.md).
- **Evidence / open work:** PR #21 https://github.com/sanjeevkshu/clp/pull/21; validation workflow .github/workflows/validate-google-analytics-federation.yml. Owner reports Google Cloud WIF setup and GitHub repository variables are configured. Validate by running the workflow on master after owner-approved merge. Then implement refresh, schema/privacy tests, safe publication and dashboard rendering. No merge/production release without explicit owner approval.

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
