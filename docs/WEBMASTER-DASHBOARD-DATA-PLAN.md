# CLP Public Webmaster Dashboard — Technical Design

**Status (2026-10-29):** The static dashboard shell and manual Google federation/access-validation workflow are merged to `master`. The owner reports the federation validation workflow now succeeds. This feature branch adds the first refresh/publish implementation for review; scheduled publication, real metric output, and production rendering remain unverified until the PR is reviewed, merged, and the refresh workflow succeeds.
**Owner intent:** Public, transparent, aggregate-only website health reporting.
**Canonical route:** `/dashboard/`
**Primary sources:** GA4 Data API, Google Search Console API; PageSpeed Insights / CrUX is a later optional source. CI/deployment health comes from GitHub Actions, not Google APIs.

## 1. Product and information architecture
- `/dashboard/` is intentionally public, marked noindex, excluded from XML sitemap, absent from header navigation, and linked in footer Resources.
- Noindex is not access control. The dashboard must contain only information safe for anyone to read and archive.
- Do not display individual visitor records, user/session/event exports, live visitor feeds, drill-downs, or data that could identify a person or small group.
- Each published metric shows source, reporting period, comparison period where applicable, definition, last successful refresh, coverage/latency caveats, and freshness state.
- Until a validated public dataset exists, render empty/“not connected” states. Never use illustrative values that could be mistaken for live measurements.

## 2. Architecture and trust boundaries
```text
GitHub Actions (trusted master only; schedule/manual)
  ├─ GitHub OIDC token (id-token: write)
  ├─ Google Cloud Workload Identity Federation (WIF)
  └─ Dedicated read-only service account
       ├─ GA4 Data API ─────────────┐
       └─ Search Console API ───────┤
                                    v
                         Fetch minimal aggregates
                                    |
                         Normalize into internal model
                                    |
                      Allowlist + privacy + freshness QA
                                    |
                      Build public schema (versioned JSON)
                                    |
                 Validate entire candidate before publication
                                    |
                Publish static aggregate dataset to GitHub Pages
                                    |
                  /dashboard/ renders only sanitized JSON
```

GitHub Pages is static; browser JavaScript must never authenticate to Google or hold a credential. The public page reads only the committed/generated public dataset. Raw API payloads must not be written to the repository, public artifacts, logs, job summaries, caches, or browser. Do not run PR-controlled code in any job with Google credentials or write permissions.

## 3. Identity and configuration
Preferred auth is short-lived GitHub OIDC → Google Cloud Workload Identity Federation, not a long-lived service-account JSON key.

Repository variables (identifiers, not secrets):
- `GCP_PROJECT_ID`: Google Cloud project ID.
- `GCP_WIF_PROVIDER`: full provider resource `projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/github-clp/providers/clp-repository`.
- `GCP_SERVICE_ACCOUNT`: dedicated service-account email.
- `GA4_PROPERTY_ID`: numeric GA4 property ID.
- `GSC_SITE_URL`: exact Search Console property identifier, e.g. `sc-domain:clpvriksha.com` or the verified URL-prefix property.

Expected federation trust is restricted to repository `sanjeevkshu/clp` and ref `refs/heads/master`. Workflow requires `id-token: write`, `contents: read`, no PR secrets, no broad token permissions. The service account should have read-only access only to the intended GA4 property and Search Console property. Do not store a JSON key when WIF works.

## 4. Workflows and environments
- PR checks: build and validate source/schema/tests without Google credentials or publishing privileges.
- Federation validation workflow: manual-only, runs only when ref is `master`; checks variables, authenticates via OIDC, performs minimal read-only aggregate queries, and prints authorization outcome and row counts only. It is a connectivity test, not a dashboard refresh.
- Future data refresh workflow: weekly Monday 03:30 UTC (09:00 IST) plus `workflow_dispatch`; only trusted protected `master`; minimal read-only APIs; explicit timeout and concurrency guard.
- Refresh must validate the complete candidate dataset before publishing. On API, schema, privacy, or freshness failure, do not replace the last-known-good dataset; report a non-sensitive failure/stale status. Never publish partial data.
- Do not grant a PR workflow access to the Google identity. Keep refresh code on trusted master and do not checkout or execute arbitrary PR refs in a credential-bearing job.
- Initial target is no incremental paid infrastructure: static JSON + GitHub Actions, subject to current Actions quotas and API limits. No database, BigQuery, server, or paid connector unless separately approved.

## 5. Data contract and analytics semantics
Proposed public metric groups:
- Acquisition: aggregate users/sessions, engaged sessions, broad channel grouping, selected landing-page groups.
- Engagement: engagement rate, average engagement time, approved aggregate content/CTA interactions.
- Search: clicks, impressions, CTR, average position; query-level dimensions require separate sensitivity review and may be excluded.
- Performance: field LCP, INP, CLS where available; label PageSpeed lab diagnostics separately from field measurements.
- Technical health: build/SEO/sitemap checks, broken-link checks and deployment status from CI.
- Trends: compare equivalent periods; distinguish observed values from interpretation and recommendations.

Use an explicit allowlisted, versioned schema (e.g. `schema_version`, `generated_at_utc`, `reporting_period`, `sources`, `metrics`, `trends`, `limitations`). Define units, time zone, aggregation, null/missing behavior, period boundaries, source latency and comparison logic. Unknown keys fail closed. Do not publish raw provider responses.

## 6. Privacy and public-release rules
- No PII to Google Analytics; no emails, names, contact details, form text, visitor IDs, client IDs, user/session IDs, raw events, raw API responses, access tokens, secrets, full URLs with query strings/fragments, stack traces, or arbitrary source fields.
- Strip query strings/fragments and normalize paths to approved route groups. Review high-cardinality dimensions and rare values.
- Proposed initial suppression threshold: fewer than 10 users/events per segment. This is a starting control, not proof of anonymization; assess rare categories, cross-filtering, differencing across refreshes, and longitudinal disclosure. Suppress or coarsen sensitive dimensions.
- Consent implementation remains governed by `docs/agentic/analytics-measurement.md`; consent does not make unsafe collection or public disclosure acceptable.
- Show data source, dates, last refresh, definitions, caveats and methodology/privacy links.
- Review actual collection, consent, retention, disclosures and applicable jurisdiction with qualified counsel. India's DPDP Act 2023 and DPDP Rules 2025 have phased commencement; do not assume all provisions took effect simultaneously. This is not legal advice.

## 7. Publication transaction and failure behavior
1. Fetch only required aggregate fields.
2. Normalize to an internal typed model; discard unknown/raw fields immediately.
3. Validate schema version, numeric ranges, date order, metric definitions, required metadata and source completeness.
4. Apply aggregation/suppression, path normalization and forbidden-field checks.
5. Run synthetic negative tests: PII-like key/value, small cohort, rare dimension, query-string URL, malformed response, stale data, missing source and partial API failure.
6. Generate a candidate public JSON file in a temporary location.
7. Validate candidate file and diff for safe allowlisted changes.
8. Publish atomically only after all checks pass. Preserve last-known-good data on any failure.
9. Log only status, stage, non-sensitive error category and counts needed for operations; never raw response or metric values.

## 8. Acceptance and release gates
- Dashboard page: noindex, sitemap exclusion, no header-nav link, footer Resources link.
- OIDC trust is limited to the repository and master ref; least-privilege read-only API access confirmed.
- PR CI is secret-free; refresh cannot execute untrusted PR code.
- Schema allowlist/versioning, forbidden-field checks, suppression/rare-category controls, freshness and source completeness pass.
- No raw payload, secret, identifier or unsafe URL in public artifacts/logs.
- Failure tests prove last-known-good data is preserved and no partial candidate is published.
- Accessibility, responsive rendering, SEO/sitemap checks, exact-SHA preview, and owner review pass.
- No merge or production changes without explicit owner approval.

## 9. Current implementation and next sequence
1. **Merged to master:** static shell; noindex/sitemap/navigation guardrails; privacy contract and portable skill; manual WIF/GA4/GSC access-validation workflow.
2. **Owner-reported validation:** the manual federation workflow now succeeds after the audience configuration fix. The connected GitHub interface could not independently retrieve the run record during this session.
3. **In this PR:** typed aggregate dataset builder, allowlisted schema checks, low-volume GA4 suppression, synthetic tests, trusted scheduled/manual refresh workflow, safe candidate validation, and dashboard rendering from the public dataset.
4. **Still to verify:** exact-SHA preview; PR checks; a successful refresh run on `master`; actual dashboard data publication and UI rendering; protected-branch push compatibility.
5. **Before live data:** review metrics and suppression rules; confirm consent/GTM state and Google property settings; validate generated public file and exact production release with owner approval.

## Related source of truth
- [Functional inventory and acceptance matrix](agentic/public-analytics-dashboard-functional-inventory.md)
- [Public analytics privacy/security contract](agentic/public-analytics-dashboard.md)
- [Portable dashboard skill](../skills/public-analytics-dashboard/SKILL.md)
- [Analytics measurement and consent](agentic/analytics-measurement.md)
- [Agentic engineering handbook](agentic/README.md)
