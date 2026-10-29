# CLP Agent Operating Contract

This file is the entry point for any AI model, coding agent, human contributor, or future automation working on CLP — Continuous Learning & Progressive Evolution.

## Before making a change
1. For every feature, enhancement, integration, or meaningful behavior change, follow [Feature Development Skill](skills/feature-development/SKILL.md). Its self-inclusive documentation review is a required development step performed by the author/agent, not a GitHub Actions documentation gate.
2. Read [the agentic project handbook](docs/agentic/README.md) and the relevant skill(s) under `skills/`.
3. Inspect the current branch, working tree/PR, repository structure, and actual implementation before assuming prior notes are still current.
4. Treat repository source, merged decisions, and current automated checks as stronger evidence than conversational recollection. Use the decision log to understand why constraints exist.
5. Identify scope, affected routes/components/assets, acceptance criteria, regression risks, and verification steps before editing.
6. Preserve user-visible behavior unless the request explicitly changes it.

## Non-negotiable project rules
- **Production safety:** production is GitHub Pages built from `master` (confirm the current default branch/workflow). Never merge or change production settings without explicit user approval. A successful build is not the same as a successful deployment or visual verification.
- **Analytics privacy:** load GTM/GA4 only on production and only after explicit analytics opt-in. Preview/development builds must not load the production GTM container. Follow [analytics measurement and consent](docs/agentic/analytics-measurement.md) for event taxonomy, CSP, consent behavior, and QA gates. For the public webmaster dashboard, also follow the [technical design](docs/WEBMASTER-DASHBOARD-DATA-PLAN.md), [functional inventory](docs/agentic/public-analytics-dashboard-functional-inventory.md), [privacy/security contract](docs/agentic/public-analytics-dashboard.md), and [portable skill](skills/public-analytics-dashboard/SKILL.md). Public dashboard data must be allowlisted aggregate-only data; noindex is not access control. Never run credentialed Google API work on PR/fork code. WIF refresh is trusted-master-only; never publish partial data or replace last-known-good data after failed validation.\n- **Preview safety:** use the repository's GitHub Pages branch preview. Do not use Vercel. Confirm the preview was built from the exact current PR head SHA. Do not claim preview success based on an older run or merely on a green build.
- **Deployment link:** whenever changes are pushed, provide the relevant preview/deployment link and the Actions run used to verify it.
- **Content versus presentation:** page-specific copy, FAQ items, and image selection/path belong in page content/front matter. CSS owns presentation (layout, sizing, crop, spacing, responsive states), not the choice of which image a page uses.
- **Reuse first:** use existing shared includes, classes, layouts, tokens, and patterns. If a pattern is recurring and missing, introduce one shared component and document its contract rather than copying one-off markup/styles.
- **Actions versus links:** meaningful primary/secondary actions use the established button components; ordinary inline references and citations remain text links.
- **FAQ invariant:** every Common Questions / FAQ section, wherever it appears, uses `_includes/faq-accordion.html` and page-specific `faq_items` front matter. No one-off FAQ markup.
- **Responsive and accessible by default:** validate mobile portrait, mobile landscape, desktop, keyboard focus, semantic structure, contrast, alt text, touch targets, and reduced-motion behavior where relevant.
- **No unsupported claims:** report exactly what was changed, which checks ran, their outcomes, the tested revision, and what remains unverified.

## Change workflow
1. Read relevant docs and skills, including Feature Development for feature work.
2. Make the smallest coherent change with a clear purpose.
3. Run available local checks and/or repository Actions; add regression checks for repeated failure modes.
4. Run the Documentation Synchronization Skill as part of development and record docs updated/linked/unchanged in the PR; do not rely on a GitHub Actions gate for this judgment.
5. Review the diff for unrelated changes, hardcoded page-specific assets in CSS, duplicate components, broken base paths, stale cache keys, and accidental production impact.
6. Push to a feature branch and open/update a PR. Keep production untouched until approval.
7. Verify the PR head SHA, successful build, successful preview deployment, and the actual preview route. Review the page in mobile and desktop layouts.
8. Report summary, changed files, checks with exact status, preview link, Actions link, PR link, risks/limitations, and approval needed.

## Knowledge preservation
- Put durable decisions and constraints in `docs/agentic/`, not only in chat.
- Update the relevant skill and decision log whenever a rule, component contract, workflow, or architecture changes.
- Date decisions and label facts as **verified**, **current assumption**, or **open question**. Do not silently convert assumptions into facts.
- Keep this contract model-neutral. Provider-specific adapters may point to it but must not redefine project policy.

Start at [docs/agentic/README.md](docs/agentic/README.md).
