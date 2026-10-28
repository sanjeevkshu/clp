# CLP Webmaster Dashboard — Data and Security Plan

## Approved direction (2026-10-28)
The owner supports a **public aggregate-only webmaster dashboard** to demonstrate transparency about CLP website performance. The dashboard itself may be public; Google credentials and underlying account access must remain private.

The page at `/dashboard/` remains noindex, excluded from the XML sitemap, absent from header navigation, and linked from footer Resources. Public availability is intentional; noindex is not access control.

## KPI design
- **Acquisition (GA4):** aggregate users, sessions, engaged sessions, broad channel and landing-page trends.
- **Engagement (GA4):** engagement rate, average engagement time and approved aggregate interactions.
- **Search Console:** clicks, impressions, CTR and average position over meaningful periods. Query-level visibility requires a sensitivity review.
- **Performance (PageSpeed Insights / CrUX):** LCP, INP and CLS field data where available; label lab diagnostics separately.
- **Technical quality (CI):** build, SEO/sitemap validation, broken-link checks and deployment health.

Every metric must show source, period, last refresh, definition and limitations.

## Secure pipeline
GitHub Pages is static. A trusted scheduled GitHub Actions workflow can fetch data, transform it to a strict public schema, validate privacy rules and publish only aggregate JSON. The browser must never call Google with a secret.

Use a dedicated read-only service identity and least privilege. Prefer short-lived identity federation where feasible; if a service-account key is required initially, store it as a GitHub Actions secret and restrict it to a trusted protected-branch job. PR workflows must not access Google secrets or execute untrusted PR code in a secret-bearing job. Never expose credentials in source, logs, artifacts, HTML or browser JavaScript.

## Public data controls
Follow [the public analytics privacy/security contract](agentic/public-analytics-dashboard.md) and [the portable skill](../skills/public-analytics-dashboard/SKILL.md). Publish aggregate metrics only, suppress small cohorts and rare dimensions, reject forbidden fields, strip URL query strings, and avoid visitor-level paths or drill-downs. The proposed initial threshold is fewer than 10 users/events per segment; confirm suitability for each metric. This reduces risk but does not prove anonymisation.

Google Analytics must not receive PII. Public aggregation does not make unlawful source collection lawful. Review consent, privacy disclosures, retention, international transfers and the phased commencement of applicable Indian DPDP provisions with qualified counsel.

## Required release gates
- Dashboard noindex, absent from XML sitemap and header navigation, present in footer Resources.
- Credentialed refresh runs only on trusted protected master; PR workflows are secret-free.
- Public JSON schema is allowlisted, versioned, freshness-checked and tested against forbidden keys and small cohorts.
- No raw data or secrets in public artifacts/logs; stale-data fallback is tested.
- Build, SEO, sitemap, schema, accessibility and exact-SHA preview checks pass.
- Owner approval is required for new public metrics/dimensions, collection changes, thresholds, APIs or publication behavior.

## Current implementation state
The current PR implements the static dashboard shell and basic page/sitemap/navigation guardrails. It does **not yet** implement the Google data pipeline, credential configuration, aggregation suppression, public JSON schema validator or synthetic privacy tests. Those are required before live metrics are enabled.
