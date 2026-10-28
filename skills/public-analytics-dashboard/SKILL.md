---
name: public-analytics-dashboard
description: Securely implement and operate CLP's public aggregate analytics dashboard.
---

# Public Analytics Dashboard Skill

## Mandatory references
Read `AGENTS.md`, `docs/agentic/public-analytics-dashboard.md`, and `docs/agentic/analytics-measurement.md`.

## Before changing the pipeline
1. Record data source, purpose, metrics, dimensions, reporting period, refresh cadence and audience.
2. Confirm every metric/dimension is approved for public release and collection/consent behavior is documented.
3. Treat repository files, GitHub Pages, logs, summaries and artifacts as public unless access controls prove otherwise.
4. Never request, print or commit credentials. Never grant secrets to PR validation jobs.

## Credential guardrails
- Prefer short-lived workload identity federation when practical; otherwise use a dedicated read-only identity and scoped secret.
- Credentialed refresh runs only on trusted protected `master` via scheduled/manual workflow.
- Fork/PR code cannot access secrets. No untrusted checkout or arbitrary script runs in a secret-bearing job.
- Minimal GitHub token permissions; no shell tracing or raw API response logging.
- Publish only sanitized public JSON; raw data and credentials are never artifacts.
- Review secret scanning and workflow permissions.

## Data safety checklist
- [ ] Versioned schema allowlist; unknown fields fail closed.
- [ ] No direct identifiers, contact details, form text, event/session-level exports, raw API responses, secrets or query-string URLs.
- [ ] Suppress small cohorts and rare dimensions; assess cross-filter/differencing risk.
- [ ] Only approved aggregate metrics and broad dimensions.
- [ ] Show source, period, refresh timestamp, definitions and limitations.
- [ ] Synthetic tests cover forbidden fields, small cohorts, malformed data and stale results.
- [ ] Owner approval and documentation update for every new metric, dimension, API, tag or threshold.

## Release
- [ ] Dashboard is public but noindex, absent from header navigation, linked in footer Resources, excluded from XML sitemap.
- [ ] No individual-level drill-down or live visitor feed.
- [ ] Build, SEO, sitemap, schema, accessibility and exact-SHA preview checks pass.
- [ ] CI is not described as legal-compliance certification.

## Failure response
Fail closed on unsafe or malformed data. Preserve the last known-good dataset with a stale/error indicator. On suspected credential exposure, revoke/rotate it and follow the incident-response process in the privacy/security contract.
