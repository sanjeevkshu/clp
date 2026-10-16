# CLP — Continuous Learning & Progressive Evolution

**Learn. Apply. Evolve.**

CLP is a brand-led learning initiative helping curious minds understand change, build practical capabilities, and evolve continuously. The site is built with GitHub Pages, Jekyll, and Markdown so the content remains easy to maintain in GitHub.

## Brand direction
- Deep Ocean: `#0B1F3B`
- Aquatic Blue: `#00A7E9`
- Sky Aqua: `#38BDF8`
- Violet accent: `#8B5CF6`
- Soft white: `#F8FAFC`

The approved CLP logo should remain the source of truth. This first repository version uses a clean vector approximation until the approved original logo file is added.

## Website
- Homepage: `index.md`
- Learning library: `learn.md`
- About: `about.md`
- Community: `community.md`
- Contact: `contact.md`
- Brand system and publishing instructions: `docs/`
- Launch video script and storyboard: `video/`

## GitHub Pages deployment
1. Open **Settings → Pages** and set the source to **GitHub Actions**.
2. The workflow in `.github/workflows/pages.yml` builds the Jekyll site and deploys it.
3. For GitHub Free, a public repository is generally required for GitHub Pages. This repository is currently private; change visibility to public or confirm an eligible plan before expecting a public Pages deployment.
4. Check **Actions** for the build status and **Settings → Pages** for the published URL.

## Agentic engineering handbook

The model-neutral project contract, architecture and design standards, content patterns, digital-asset rules, QA/release process, AI-readiness guidance, decision log, and reusable agent skills live in [`AGENTS.md`](AGENTS.md), [`docs/agentic/`](docs/agentic/), and [`skills/`](skills/). Start with the [handbook index](docs/agentic/README.md). These files are the durable source of project knowledge; do not rely on chat history alone.

## Content workflow
Edit Markdown files directly in GitHub. Keep page front matter intact. See [`docs/content-management.md`](docs/content-management.md).

## Launch status
Source scaffold is ready for initial deployment. Before public launch, verify the approved logo asset, channel URL, domain, signup destination, and actual rendered video are connected.
