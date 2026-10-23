# CLP Website Analytics and Consent

**Status:** Implemented on feature branch; awaiting preview checks, GTM configuration, owner review, and approval before production release.
**Last reviewed:** 2026-10-23

## Purpose

Measure discovery and learning journeys so CLP can improve its learning library using evidence. The initial stack is Google Analytics 4 (GA4), Google Tag Manager (GTM), and Google Search Console. GA4/GTM identifiers are public configuration values, not credentials. The account owner is intended to be `clpvriksha@gmail.com`.

- Production domain: `https://clpvriksha.com`
- GA4 Measurement ID: `G-YMJS96D5TZ`
- GTM Web container: `GTM-KQ49L3GG`
- Runtime configuration: `_config.yml`
- Consent UI: `_includes/analytics-consent.html`
- Consent and GTM loader: `assets/js/analytics-consent.js`
- Interaction event instrumentation: `assets/js/main.js`

## Consent contract

- GTM is dynamically loaded only when the build is `production` and the visitor's saved choice is `accepted`.
- A visitor with no saved choice sees the consent panel. “Accept analytics” opts in; “Reject optional analytics” opts out. The persistent “Privacy choices” control allows the visitor to reopen the panel.
- The choice is stored in browser local storage under `clp-analytics-consent` as `accepted` or `rejected`. If storage is unavailable, consent is not assumed; the visitor can still use the site, but the choice may not persist across pages/visits.
- Preview/development builds show the consent interface for review but set analytics disabled, omit the production GTM ID, and retain noindex protection. No GTM script is loaded from previews.
- The GTM container must be configured so the GA4 Google tag and all analytics tags fire only after the consent-gated container has loaded. Do not add ad, remarketing, session replay, or heatmap tags without separate owner approval.
- On withdrawal after acceptance, the site records rejection, updates Google consent to denied where the runtime exists, and reloads so the container is not loaded on the next page view.
- This is a technical privacy-first default, not legal advice or a guarantee of compliance in every jurisdiction. Review consent wording and legal requirements for CLP's actual audience before launch.

## GTM setup still required in the Google UI

The repository can load the container after consent but cannot create/edit the container's tags through GitHub. Before enabling production collection:

1. In GTM, create a **Google tag** with tag ID `G-YMJS96D5TZ`.
2. Configure it to fire on all pages **within this consent-gated container**. Because the container itself is not loaded before opt-in, do not add a separate direct GA4 snippet to the site.
3. Ensure GA4 page views are not duplicated. Keep GA4 Enhanced Measurement only for supported automatic interactions; do not duplicate scroll or outbound-link events with custom tags.
4. Add GA4 Event tags for the custom events below, using Custom Event triggers with exact event-name matches.
5. Preview the container and confirm no tags fire when consent is rejected. Publish the GTM container only after reviewing its preview/debug output.
6. In GA4, verify events in Realtime/DebugView after accepting analytics. GA4's standard reports may take time to populate.

## Event taxonomy

Custom events are pushed to `dataLayer` only when the saved consent is accepted and the GTM runtime exists. Configure matching Custom Event triggers/tags in GTM.

| Event name | Trigger | Parameters |
|---|---|---|
| `clp_learning_card_click` | Click a learning/resource card link | `content_title`, `content_series`, `destination_path` |
| `clp_content_cta_click` | Click a prominent content CTA | `cta_label`, `destination_path` |
| `clp_series_filter` | Click a learning-series/topic filter | `filter_category` |
| `clp_navigation_click` | Click a primary navigation link | `link_label`, `destination_path` |
| `clp_faq_toggle` | Open/close a shared FAQ item | `faq_question`, `faq_state` |
| `clp_community_intent` | Submit a client-side email-draft form | `intent_type` |

Parameters deliberately exclude email addresses, form field values, topic suggestions, query strings, fragments, and full outbound URLs. The community events indicate only that a visitor initiated an email draft; they do **not** prove the email was sent or a person joined CLP.

## Reporting questions

- Discovery: users, sessions, engaged sessions, acquisition channels, landing pages, device categories, and broad geographic reporting.
- Content: top pages, engagement time, learning-series performance, and onward clicks from cards/CTAs.
- Journey: navigation, filters, FAQ interaction, and community-intent actions.
- Evolution: pages that attract visits but do not lead to related learning; content series with strong engagement; device-specific friction; and topics worth expanding.

Use aggregated reports. Avoid collecting personally identifiable information. Keep GA4 retention at the shortest duration that meets CLP's analysis needs (review the property's retention setting), and restrict access to the people who need it. Search Console is complementary and should be verified separately with the CLP Google account.

## QA and release gates

- [ ] Production build includes the consent panel, production-only GTM ID, and approved CSP origins.
- [ ] Preview build shows consent UI but has no GTM ID and no GTM network script; preview stays `noindex,nofollow`.
- [ ] JavaScript syntax checks pass for both browser scripts.
- [ ] No analytics requests before consent; reject leaves the container unloaded.
- [ ] Accept loads GTM once; subsequent navigation and custom events work without duplicate page views.
- [ ] Reopening privacy choices and rejecting after prior acceptance records rejection and prevents the next page load from loading GTM.
- [ ] Keyboard/focus behavior, mobile portrait/landscape, desktop, light/dark theme, and banner contrast are checked.
- [ ] GTM Preview and GA4 Realtime/DebugView have been checked after consent.
- [ ] Current PR head SHA has a successful build and verified preview deployment.
- [ ] Owner approves before merge/production release.

## Known limitations

- The repository implementation does not publish GTM tags or configure GA4 property settings. The Google UI steps above remain a manual setup requirement.
- GA4 data collection cannot be validated until the GA4 Google tag and event tags are configured in GTM.
- The privacy notice and consent UX need owner review; this is not a substitute for jurisdiction-specific legal review.
