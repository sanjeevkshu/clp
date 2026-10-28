# CLP Webmaster Dashboard — Data and Security Plan

## Current implementation
The first release is a static, noindex dashboard shell at `/dashboard/`. It uses explicit empty KPI values and identifies itself as a demo until the authenticated data service is connected. It is excluded from the XML sitemap and is linked only from the footer Resources column. It is intentionally absent from header navigation.

## KPI design
- **Acquisition (GA4):** active users, sessions, sessions by default channel group, landing pages, referral sources.
- **Engagement (GA4):** engaged sessions, engagement rate, average engagement time, event/key-event counts where configured.
- **Search (Search Console):** clicks, impressions, CTR, average position, top queries and landing pages.
- **Performance (PageSpeed Insights / CrUX):** LCP, INP, CLS field data where available; lab diagnostics clearly separated from field data.
- **Technical quality (CI):** SEO validator, sitemap validator, broken-link checks, deployment smoke tests and Core Web Vitals trend.

Every metric must display source, date range, comparison period, refresh timestamp, and a clear unavailable/insufficient-data state. Do not interpret low-volume data as a statistically reliable trend.

## Production data architecture
Static GitHub Pages cannot safely hold OAuth refresh tokens or service-account credentials. Add a separate authenticated backend (for example, a serverless function behind an identity-aware access layer) that:
1. authenticates an authorized webmaster;
2. reads secrets from a managed secret store;
3. queries GA4 Data API and, optionally, Search Console and PageSpeed Insights/CrUX;
4. applies a narrow allowlist of dimensions/metrics and date ranges;
5. returns aggregated data only, with caching, timeouts, rate limits and error states;
6. records operational logs without exposing credentials or unnecessary visitor-level data.

Do not expose a service account key, OAuth refresh token, or unrestricted API key in HTML, JavaScript, public GitHub Actions logs, or the repository. GA4 property access should be read-only and limited to the required property. Configure authenticated access before showing real metrics; `noindex` is not an access-control mechanism.

## Release guardrails
- Generated `dashboard/index.html` must contain `noindex` and must not contain an index directive.
- `dashboard/` must not appear in `sitemap.xml`.
- Dashboard must not be present in the header/main navigation.
- Footer Resources must link to `/dashboard/`.
- Production and preview SEO/sitemap validators must pass.
- Preview URLs must remain noindex-protected.
- The page must render responsively, have a single H1, semantic headings, accessible card labels and understandable missing-data states.
- Automated whitespace remediation is limited to known text files, emits a reviewable patch artifact, and never pushes to the PR branch automatically. Human review and approval remain required.

## Follow-on decision
Before enabling live metrics, select the hosting/authentication layer, identify the GA4 property and Search Console property, define authorized users, and add credentials through the chosen secret manager. The static dashboard is a safe front-end foundation, not a live analytics connection.
