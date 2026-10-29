# Public Webmaster Dashboard — Functional Inventory and Acceptance Matrix

**Status snapshot:** 2026-10-29. The static dashboard and manual federation validation are merged to master. The follow-on `feature/dashboard-data-refresh` PR adds a refresh/publish implementation; do not treat it as production until merged, approved and successfully run.
**Foundation PR:** https://github.com/sanjeevkshu/clp/pull/21
**Refresh implementation branch:** `feature/dashboard-data-refresh` (PR to be opened)
**Route:** `/dashboard/`
**Technical design:** [Webmaster Dashboard Data Plan](../WEBMASTER-DASHBOARD-DATA-PLAN.md)

## Status vocabulary
- **Implemented / unmerged:** source exists on the feature branch; not production behavior.
- **Validation workflow implemented / unrun:** workflow source exists; real identity/API access has not yet been demonstrated.
- **Planned:** design requirement; no production implementation claim.
- **Owner gate:** requires explicit product/security/privacy review or approval.

## Functional inventory

| ID | Capability | Expected behavior / acceptance | Current state |
|---|---|---|---|
| DASH-001 | Public dashboard route | Serve `/dashboard/` from static Jekyll/GitHub Pages. | Implemented / unmerged |
| DASH-002 | Discoverability controls | `noindex,follow`; excluded from sitemap; absent from header nav; linked in footer Resources. CI guards these invariants. | Implemented / unmerged; verify latest exact-SHA preview |
| DASH-003 | Honest empty state | Do not imply data is live before integration; missing metrics show unavailable/awaiting-source states. | Implemented / unmerged |
| DASH-004 | KPI overview | Aggregate acquisition, engagement, organic search and performance metrics with definitions. | UI shell exists; live values planned |
| DASH-005 | Acquisition trends | GA4 aggregate active users, sessions and approved aggregate metrics. | Implemented in refresh PR; not yet production-verified |
| DASH-006 | Engagement trends | GA4 engagement rate and average engagement time. | Implemented in refresh PR; event-level content/CTA dimensions remain out of scope |
| DASH-007 | Search visibility | Aggregate Search Console clicks, impressions, CTR and average position; no query/page dimensions. | Implemented in refresh PR; not yet production-verified |
| DASH-008 | Performance signals | Field Core Web Vitals where available; label lab tests separately; show sample/coverage caveats. | Planned; optional PSI/CrUX source |
| DASH-009 | Website engineering health | Display verified CI/deployment/SEO/sitemap health, with run timestamp and source. | Planned integration; existing CI checks are separate |
| DASH-010 | Period comparisons | Compare equivalent, clearly labeled periods; avoid asserting causality from correlation. | Planned |
| DASH-011 | Trend interpretation | Show evidence-based patterns, caveats and suggested investigation; distinguish measurement from AI-generated interpretation. | Planned |
| DASH-012 | Freshness and provenance | Every metric includes source, reporting period, definition, last successful refresh and limitations. | Planned |
| AUTH-001 | GitHub OIDC federation | Actions obtains short-lived identity token and impersonates dedicated service account through WIF. | Validation workflow implemented / unrun |
| AUTH-002 | Trust boundary | Only `sanjeevkshu/clp` at `refs/heads/master` is authorized; no PR/fork credential access. | Workflow and cloud condition configured per owner report; real validation pending |
| AUTH-003 | Least privilege | Service account read-only to intended GA4 property and Search Console property. | Configured per owner report; verify by successful API test |
| AUTH-004 | Configuration | Repository variables `GCP_PROJECT_ID`, `GCP_WIF_PROVIDER`, `GCP_SERVICE_ACCOUNT`, `GA4_PROPERTY_ID`, `GSC_SITE_URL`. | Owner reports Step 7 complete; values inaccessible to this review |
| PIPE-001 | Manual access test | On trusted master, verify OIDC auth and minimal aggregate reads from both APIs; logs contain status/row counts only. | Implemented /unrun |
| PIPE-002 | Scheduled refresh | Weekly Monday 03:30 UTC (09:00 IST), plus manual dispatch; gated by `DASHBOARD_PUBLISH_APPROVED=true`. | Implemented in refresh PR; not yet production-verified |
| PIPE-003 | Minimal data fetch | Request only aggregate GA4 metrics and aggregate Search Console totals, with no dimensions. | Implemented in refresh PR; not yet production-verified |
| PIPE-004 | Normalize and allowlist | Convert source responses to a versioned allowlisted public schema; unknown keys fail closed. | Implemented in refresh PR; not yet production-verified |
| PIPE-005 | Privacy suppression | Suppress all GA4 metric values when active users are fewer than 10; no high-cardinality dimensions are fetched. | Implemented in refresh PR; owner must approve public release |
| PIPE-006 | Forbidden-field detection | Reject PII, identifiers, form text, raw events, raw provider payloads, secrets, full query URLs, stack traces and unknown fields. | Planned |
| PIPE-007 | Atomic publish | Candidate is generated and validated before a separate write-enabled job replaces the single dataset file. | Implemented in refresh PR; not yet production-verified |
| PIPE-008 | Last-known-good fallback | Failed refresh leaves prior dataset unchanged; UI labels data older than 10 days as stale. | Implemented in refresh PR; not yet production-verified |
| PIPE-009 | Synthetic negative tests | Test small cohorts, unknown fields, malformed/stale periods and invalid metric ranges in credential-free CI. | Implemented in refresh PR; broader rare-dimension/partial-source cases remain to add |
| PIPE-010 | Logs and artifacts | Never publish raw API responses, credentials, identifiers, metric values in validation logs, or sensitive artifacts. | Validation workflow avoids metric values; refresh guardrails planned |
| PRIV-001 | Consent consistency | Keep GA4/GTM collection behind approved consent behavior; consent is not permission to publish unsafe fields. | Existing consent contract documented; production configuration/release state must be rechecked |
| PRIV-002 | Public disclosure | Public output is safe for anyone; noindex is not access control. Provide methodology/privacy context. | Contract documented; dashboard UI additions planned |
| QA-001 | Build and static guardrails | Jekyll build, SEO/sitemap tests, dashboard placement checks. | CI present; verify current run |
| QA-002 | Preview exact revision | Confirm preview deployment matches current PR head SHA and inspect mobile/desktop. | Older preview exists; latest SHA verification pending |
| QA-003 | Failure safety | Candidate validation runs before write-enabled publication; failed refresh job prevents publish job from running. | Implemented in refresh PR; verify with workflow test after merge |
| REL-001 | Owner release gate | No merge or production changes without explicit owner approval. | Mandatory policy |
| KB-001 | Model-neutral knowledge | Keep technical design, functional inventory, security contract, skill, handbook links, decision log and workflow instructions synchronized in PR. | This inventory added in PR; sync remainder underway |

## Metric catalog (candidate; each metric requires owner approval before public release)

| Group | Candidate metrics | Dimensions / segmentation guardrail |
|---|---|---|
| Acquisition | Sessions, users, engaged sessions | Broad channel, approved route group, device category only where safe |
| Engagement | Engagement rate, average engagement time, approved content CTA counts | Content series / route group; suppress small or rare cohorts |
| Search | Clicks, impressions, CTR, average position | Aggregate page groups; avoid public query-level output by default |
| Performance | LCP, INP, CLS | Field vs lab clearly separated; include availability/sample caveats |
| Engineering | Latest build/check status, last successful deployment, failed check category | Workflow and route-level health only; no logs/stack traces |
| Synthesis | Period-over-period direction and explanatory notes | No causal claims without evidence; label AI-generated narrative and ground each statement in approved metrics |

Metric definitions, source API fields, units, date ranges, null behavior and comparison formulas must be documented in code/schema before publishing.

## Public JSON contract (target, not yet implemented)
- Top-level fields should be explicitly allowlisted: `schema_version`, `generated_at_utc`, `reporting_period`, `sources`, `metrics`, `trends`, `limitations`.
- Use only pre-approved metric IDs and typed numeric/string values; no arbitrary provider field passthrough.
- Include per-source status and staleness metadata without exposing account identifiers beyond approved public labels.
- Reject unknown keys, malformed dates, impossible ranges, incomplete source windows, stale candidate datasets and unsafe URLs.
- Never include user/session/event records, IDs, contact data, free text, query strings/fragments, credentials, raw responses, stack traces or hidden diagnostic dumps.

## Workflow/runbook
1. Review PR #21 and its checks: https://github.com/sanjeevkshu/clp/pull/21
2. After owner-approved merge, open GitHub Actions: https://github.com/sanjeevkshu/clp/actions
3. Run **Validate Google Analytics Federation** on `master`.
4. Verify both API success lines and row counts; never infer success from variable presence alone.
5. If failure: missing-variable error → verify variable name/value; OIDC error → verify provider resource, audience, attribute condition and service-account impersonation binding; GA4 error → verify numeric property ID, enabled API and Viewer permission; GSC error → verify exact property identifier, API and service-account access.
6. Only after validation passes, implement and test the actual refresh/publication pipeline.
7. Run privacy negative tests and last-known-good failure tests before enabling real public metrics.
8. Review exact-SHA preview, the generated public JSON diff and dashboard rendering; obtain owner approval before production release.

## Explicit non-goals
- No authenticated visitor login for this dashboard; it is intentionally public.
- No raw traffic logs, live visitor feed, person-level analytics, session replay, heatmaps or arbitrary query exploration.
- No browser-side Google API authentication.
- No BigQuery, database, paid backend or external connector in the initial design.
- No automatic merge or production publish from a PR.
- No claim of legal compliance based solely on CI checks or aggregation.

## Change control
Any new metric, dimension, API, GTM tag, event parameter, threshold, refresh frequency, public field, credential scope or publication behavior requires owner approval and updates to this inventory, technical design, security contract, portable skill, and decision log in the same PR.


## Release gate added in refresh implementation
The scheduled/manual refresh workflow requires repository variable `DASHBOARD_PUBLISH_APPROVED=true`. Keep it unset until the owner reviews the public metric set, GA4 consent/GTM behavior, suppression policy, privacy notice/methodology and production preview. The credential-bearing job has `contents: read` plus `id-token: write`; a separate publish job receives only the validated aggregate JSON and has `contents: write`. No public metric values should be published until the approval gate is intentionally enabled.
