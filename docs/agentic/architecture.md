# CLP Architecture and Component Boundaries

## Architecture summary
CLP is currently a static, repository-driven website. Markdown/YAML content is rendered by Jekyll into HTML and deployed to GitHub Pages through GitHub Actions. Shared HTML includes, CSS, and JavaScript provide site chrome, visual language, and progressive interactions. There is no verified server-side application/API/database in the current baseline.

```text
Page content (.md + YAML front matter) ─┐
Shared includes (_includes/*.html) ─────┼─> Jekyll build ─> generated static site ─> GitHub Pages
Shared layout (_layouts/*.html) ─────────┤                         ▲
CSS (assets/css/*.css) ──────────────────┤                         │
JS (assets/js/*.js) ────────────────────┘                 GitHub Actions workflows
                                                        ├─ production from master
                                                        └─ PR preview under /previews/<slug>/
```

## Responsibilities and boundaries
- **Content layer:** page titles, descriptions, permalinks, body copy, FAQ data, image choices/paths, CTA labels and destinations.
- **Presentation layer:** CSS tokens, typography, layout, responsive breakpoints, states, transitions, crop/fit, focus, and dark-theme styles.
- **Composition layer:** layouts and reusable includes. Use these to centralize shared markup and component contracts.
- **Behavior layer:** small client-side interactions in `assets/js/main.js`; keep functionality progressive and avoid adding JavaScript when native HTML already meets the need.
- **Build/deploy layer:** `_config.yml`, `Gemfile`, and `.github/workflows/*.yml`; maintain explicit separation between production and preview builds.
- **Discovery/metadata layer:** title, description, canonical, social metadata, structured data, sitemap/robots behavior where present. Verify generated output.

## Component reuse contract
Before building a new pattern:
1. Search existing includes, classes, page markup, and styles.
2. Determine whether the pattern is truly recurring and define its inputs, output markup, behavior, accessibility contract, and responsive behavior.
3. Build one shared include/class/module with content supplied through front matter or include parameters.
4. Add usage documentation and a QA check.
5. Migrate existing occurrences together where the scope is understood.

Current reusable patterns include shared header/footer/layout, learning-resource cards, learning article CTA buttons, and (in the active PR) a data-driven FAQ accordion. Confirm implementation state from source and CI.

## URL and asset path rules
- Use Jekyll's `relative_url` for internal links and local asset URLs so the `/clp` base path and preview subpaths are respected.
- Use `absolute_url` where canonical, Open Graph, Twitter, or JSON-LD fields require absolute URLs.
- Do not hardcode production-domain links for internal navigation.
- Treat preview builds as separate baseurl builds. A page can appear correct on root hosting but break under a nested preview prefix; test both.

## CSS and cache invalidation
- Shared styles currently load from `styles.css` and `responsive-polish.css` with query-string version tokens in the layout.
- When changing a stylesheet or another cached asset, inspect the current cache invalidation approach and bump the relevant version token(s) intentionally. Avoid unrelated cache-token churn.
- Keep page-specific image selection in content. CSS may use a content-provided custom property for presentation, but should not embed a page-specific asset choice in a selector.

## Avoid architecture drift
- Do not add a framework, bundler, plugin, CMS, API, analytics service, or external dependency without explaining the need, cost, privacy impact, deployment implication, and maintenance burden.
- Prefer semantic HTML and static generation until a documented requirement justifies a more complex runtime.
- Any future dynamic service must document data flow, ownership, trust boundaries, secrets, failure modes, privacy, and fallback behavior.
- Do not claim agentic functionality exists on the public website merely because the development workflow uses AI agents.
