# Public Analytics Dashboard — Privacy and Security Contract

**Decision (2026-10-28):** CLP will pursue a publicly accessible, aggregate-only webmaster dashboard. Keep the dashboard public but keep Google credentials and underlying account access private. Public availability is intentional; `noindex` is not access control.

## Credential boundary
- Prefer short-lived workload identity federation where practical. Otherwise use a dedicated Google service identity with read-only access to the exact GA4 property and only the required Search Console property.
- If a service-account key is needed, store it as a GitHub Actions secret, never in source, generated HTML, browser JavaScript, logs, or artifacts.
- Only a trusted scheduled/manual workflow on protected `master` may access Google credentials. Pull-request workflows must not receive them or execute untrusted PR code in a secret-bearing job.
- Use minimum GitHub token permissions, no shell tracing, no raw API logging, and rotate/revoke credentials if exposure is suspected. Secret masking is best-effort, not a guarantee.
- Restrict repository write access: writers may be able to change workflows that use repository secrets.

## Public-data allowlist
Candidate metrics: aggregate GA4 users/sessions/engagement, broad channel/device categories, Search Console clicks/impressions/CTR/average position over meaningful periods, CrUX field Core Web Vitals, PageSpeed lab diagnostics clearly labelled, and non-sensitive CI health status.

Never publish user/client/cookie IDs, IPs, emails, form values, session/event-level exports, raw API responses, access tokens, service-account keys, stack traces, or URLs containing query strings/fragments. Do not create individual visitor drill-downs or near-real-time activity feeds. Keep user-entered text out of GA4 event parameters.

## Aggregation and suppression
- Publish only versioned, explicitly allowlisted JSON; reject unknown fields and validate types, ranges, freshness and forbidden keys.
- Aggregate over daily/weekly/monthly periods and broad dimensions. Suppress small cohorts (initial proposal: fewer than 10 users/events) and rare geographies/queries/categories. Review threshold suitability per metric; thresholds reduce risk but do not prove anonymity.
- Consider cross-filtering/differencing risks. Do not expose combinations that could reveal small cohorts.
- Publish no raw extraction files or raw API response artifacts.
- If refresh or validation fails, preserve the last known-good dataset and display a non-sensitive stale/error indicator.

## Workflow guardrails
1. PR checks are secret-free and validate code only.
2. Trusted scheduled/manual refresh on protected `master` fetches the minimum data needed.
3. Transform and sanitize data before any public write; publish only the approved JSON schema.
4. Include synthetic negative tests for PII-like fields, small cohorts, rare dimensions, malformed responses and stale data.
5. Require owner approval for new metrics/dimensions, thresholds, APIs, tags, consent behavior or public fields.
6. Keep dashboard `noindex`, out of header navigation, in footer Resources and excluded from XML sitemap.

## Compliance and transparency
Show source, reporting period, last refresh, definitions and coverage limitations. Link to privacy notice/methodology. Explain that analytics platforms may process identifiers under their own settings; do not claim “anonymous” solely because the public view is aggregated.

This is an engineering baseline, not legal advice or certification. Review the actual collection, consent, retention, disclosures and applicable jurisdictions with qualified counsel. For India, consider the DPDP Act 2023 and DPDP Rules 2025 with their phased commencement; do not assume every provision began on the same date. Google Analytics terms prohibit sending PII to Analytics, and public aggregation does not cure unlawful collection at source.

## Required release gates
- Secret scan and workflow trust-boundary review pass.
- No credentials in tracked files, public site, logs or artifacts.
- Public schema allowlist, forbidden-field tests, aggregation suppression and freshness checks pass.
- Dashboard page/sitemap/navigation guardrails pass.
- Exact-SHA build and preview checks pass.
- Owner review completed. CI success is not legal-compliance certification.

## References
- GitHub Actions secrets: https://docs.github.com/en/actions/concepts/security/secrets
- GitHub Actions secure use: https://docs.github.com/en/actions/reference/security/secure-use
- Google Analytics API quickstart: https://developers.google.com/analytics/devguides/config/admin/v1/quickstart
- Google Analytics safeguards / PII: https://support.google.com/analytics/answer/6004245
- Google Cloud authentication: https://cloud.google.com/docs/authentication
- MeitY DPDP Rules, 2025: https://www.meity.gov.in/documents/act-and-policies/digital-personal-data-protection-rules-2025-gDOxUjMtQWa


## Implementation status and source of truth (2026-10-29)
The static dashboard shell, baseline noindex/sitemap/navigation checks, this privacy contract, portable skill, and manual Google OIDC/WIF access-validation workflow are merged to `master`. The owner reports that the manual federation workflow now succeeds after the provider-audience fix; independently confirm the run record when available.

The follow-on `feature/dashboard-data-refresh` PR introduces aggregate-only GA4 and Search Console queries, a versioned allowlisted JSON contract, suppression of GA4 metrics below 10 active users, credential-free synthetic tests, and separate refresh/publish jobs. The refresh job uses read-only repository access plus OIDC; the publishing job receives only the sanitized candidate and has contents-write permission. Publication is gated by repository variable `DASHBOARD_PUBLISH_APPROVED=true`. Until the PR is reviewed/merged, the gate is approved, and the first refresh and site rendering are verified, do not describe the dashboard as live. Failed refreshes leave the prior dataset unchanged; the UI labels data older than 10 days as stale.

Use the [technical design](../WEBMASTER-DASHBOARD-DATA-PLAN.md) and [functional inventory](public-analytics-dashboard-functional-inventory.md) as the feature-specific operational source of truth. Update both, this contract, the skill, the handbook index and decision log when behavior changes.
