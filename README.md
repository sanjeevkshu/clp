# CLP — Continuous Learning & Progressive Evolution

**Learn. Apply. Evolve.**

CLP is a brand-led learning initiative helping curious minds understand change, build practical capabilities, and evolve continuously. The site is built with GitHub Pages, Jekyll, and Markdown so the content remains easy to maintain in GitHub.

## Brand direction
- Deep Ocean: `#0B1F3B`
- Aquatic Blue: `#00A7E9`
- Sky Aqua: `#38BDF8`
- Violet accent: `#8B5CF6`
- Soft white: `#F8FAFC`

The current Kalpavriksha logo and CLP identity are maintained in the repository's shared digital assets. Do not replace the approved circular emblem or green tree without an explicit brand decision.

## Website
- Homepage: `index.md`
- Learning library: `learn.md`
- About: `about.md`
- Community: `community.md`
- Contact: `contact.md`
- Brand system and publishing instructions: `docs/`
- Launch video script and storyboard: `video/`

## GitHub Pages deployment and preview
The `.github/workflows/pages.yml` workflow builds the production site from the default branch and publishes a branch-specific preview for pull requests. Production remains unchanged until a PR is reviewed and merged. Review the preview generated for the exact current PR head SHA; an older preview is not sufficient evidence.

## Automated SEO / GEO / AIO readiness checks
The `.github/workflows/seo-validation.yml` workflow builds the Jekyll site and validates rendered page metadata, canonical URLs, JSON-LD, robots directives, sitemap coverage, and crawl configuration on pull requests and pushes. The checks are guardrails, not a guarantee of search indexing or AI citation. Live browser verification and Google Search Console checks remain part of launch QA.

The sitemap is generated from eligible site pages, so new learning articles are included automatically unless explicitly excluded with `sitemap: false`. The sitemap URL in `robots.txt` is generated from the Jekyll site configuration rather than hard-coded.

## Domain
The selected launch domain is **clpvriksha.com**. Domain activation, DNS changes, the production `url` / `baseurl` change, and the GitHub Pages custom-domain setting are deliberately gated until the SEO validation workflow passes and the production site, current PR preview, and live rendering have been verified. Do not add a `CNAME` file or change production canonical URLs before that gate is cleared.

## Agentic engineering handbook

The model-neutral project contract, architecture and design standards, content patterns, digital-asset rules, QA/release process, AI-readiness guidance, decision log, and reusable agent skills live in [`AGENTS.md`](AGENTS.md), [`docs/agentic/`](docs/agentic/), and [`skills/`](skills/). Start with the [handbook index](docs/agentic/README.md). These files are the durable source of project knowledge; do not rely on chat history alone.

## Content workflow
Edit Markdown files directly in GitHub. Keep page front matter intact. See [`docs/content-management.md`](docs/content-management.md).

## Release readiness
A successful build is necessary but not sufficient. Before custom-domain activation, verify the current PR preview, mobile portrait and landscape layouts, logo and homepage hover behavior, FAQ accordions, page-specific metadata, sitemap and robots output, JSON-LD validity, and live Search Console URL inspection. Record the exact commit and deployment URL in the PR.
