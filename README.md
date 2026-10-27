# CLP — Continuous Learning, Continuous Inclusive Learning

**Learn. Apply. Evolve.**

CLP Vriksha is a learning initiative helping people understand change, build practical capabilities, apply learning, and evolve inclusively. The website is maintained as a GitHub Pages/Jekyll project with Markdown content, shared includes, CSS, and reusable digital assets.

## Live website and release model

- Production website: https://clpvriksha.com/
- Repository: https://github.com/sanjeevkshu/clp
- Current logo work: [PR #16 — global header and footer logos](https://github.com/sanjeevkshu/clp/pull/16)
- Preview/deployment workflows: `.github/workflows/pages.yml`
- SEO and AI-readiness guardrails: `.github/workflows/seo-validation.yml`

The website is live. Do not describe the custom domain as a future launch or gated activation. Any statement about current deployment health must be verified against the latest workflow and live site, not inferred from the fact that the domain exists.

### Safe delivery workflow

1. Inspect the current branch, relevant source files, and repository operating contract.
2. Implement a scoped change on a feature branch and open/update a PR.
3. Wait for the preview build for the exact PR head commit.
4. Validate the rendered preview, including responsive layouts and accessibility where relevant.
5. Run build, SEO/metadata, and relevant project guardrails.
6. Update the PR with the exact commit, preview URL, test evidence, and any limitations.
7. Merge only with explicit owner approval. A passing build is not proof of visual correctness. Never claim a deployment or preview exists until verified.

## Brand and digital assets

The approved CLP identity is the detailed Kalpavriksha/tree emblem with an open teal/green circular arc, CLP wordmark, and the tagline **“Learn. Apply. Evolve.”** Preserve the approved artwork exactly; do not redraw it as a simplified SVG or substitute generated approximations. Header, footer, YouTube, and other social assets should look like one connected brand system. Reuse the approved source artwork and adapt only its crop, size, and placement for each channel.

Use the current approved design language and source files in `docs/agentic/design-language.md` and `docs/agentic/digital-assets.md` as the authority for colors, typography, spacing, asset formats, and responsive behavior. If the source of truth is ambiguous, pause and ask rather than inventing brand details.

## Website information architecture

- Home: `index.md`
- Learn library: `learn.md`
- About: `about.md`
- Community: `community.md`
- Contact: `contact.md`
- Shared includes: `_includes/`
- Styles and interaction presentation: `assets/css/` and related assets
- Learning content and semantic routes: inspect current page front matter and `_config.yml` before changing URLs.
- Launch video scripts/storyboards: `video/`

Avoid assuming this list exhausts every route; inspect the current repository before documenting or changing information architecture.

## Automated validation and limitations

The SEO/AI-readiness workflow validates repository-level signals such as rendered metadata, canonical URLs, structured data, robots directives, sitemap coverage, and crawl configuration. These checks are guardrails, not guarantees of search indexing, rankings, GEO/AEO visibility, or AI citation.

For material changes, supplement CI with live preview checks and, where relevant, Google Search Console inspection. Confirm the preview is built from the exact current PR head SHA; a stale preview is not sufficient evidence.

## Agentic engineering handbook

The model-neutral operating contract, architecture, design language, content patterns, digital asset rules, QA/release process, AI-readiness guidance, decisions, and reusable skills are maintained in:

- [`AGENTS.md`](AGENTS.md) — mandatory operating contract.
- [`docs/agentic/README.md`](docs/agentic/README.md) — handbook index.
- [`docs/agentic/agentic-spec.md`](docs/agentic/agentic-spec.md) — model-neutral project specification.
- [`skills/`](skills/) — portable task-specific skills.

These files are durable project memory. Keep them aligned with implemented capabilities and workflow changes; chat history alone is not the source of truth.

## Documentation is part of every change

Every PR MUST review whether README, `AGENTS.md`, agentic specifications, relevant skills, design/architecture decisions, content guidance, and release instructions need updates. Update the documents in the same PR whenever behavior, capabilities, workflows, routes, assets, acceptance criteria, or operating rules change. If no documentation change is needed, state that in the PR description. See [the documentation synchronization skill](skills/documentation-sync/SKILL.md).

## Content workflow

Edit Markdown content while preserving front matter. Follow `docs/content-management.md` and `docs/agentic/content-patterns.md`. Reusable interactions such as common-question FAQs should use the documented shared accordion pattern; article CTAs should follow the documented button/link convention.

## Release readiness

A successful build is necessary but insufficient. For each PR, verify the current preview, relevant desktop/mobile portrait/landscape layouts, approved logo rendering, navigation and shared components, links, page metadata, sitemap/robots output, and structured data as appropriate. Record exact commit and preview URL in the PR. Production remains unchanged until an explicit merge approval.


### Logo contrast and theme behavior
The approved header and footer logo PNGs must render on white containers in both light and dark themes. Theme-specific logo filters must not alter the approved artwork. Any changes to logo placement must be checked at desktop, mobile portrait, and mobile landscape sizes.


### Theme-aware shared logos
The header and footer use `assets/images/clp-vriksha-logo-dark.png` in dark theme and `assets/images/clp-vriksha-logo-light.png` in light theme. The active theme is controlled by the shared theme toggle; see `docs/agentic/design-language.md` and `docs/agentic/digital-assets.md` for the rule.
