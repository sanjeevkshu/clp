# CLP QA, Release, and Deployment Safety

## QA layers
1. **Source review:** YAML front matter, Liquid syntax, semantic HTML, links, image references, shared-component usage, no secrets, no accidental unrelated diffs.
2. **Build validation:** Jekyll build succeeds; JavaScript syntax checks pass; required output files and interaction hooks exist.
3. **Static checks:** local internal links and assets resolve; FAQ sections use the shared include; metadata and route uniqueness are checked.
4. **Accessibility:** keyboard operation, focus visibility, heading order, accessible names, contrast, alt text, reduced motion, touch targets, native disclosure behavior.
5. **Responsive visual QA:** mobile portrait, mobile landscape/short viewport, tablet, desktop.
6. **Runtime QA:** nav open/close, theme toggle, forms' actual behavior, CTA destinations, accordion open/close, console/network errors where tools permit.
7. **Deployment QA:** exact PR SHA built, preview workflow succeeded, deployed preview route reflects the current SHA, production remains intact.
8. **Regression QA:** check nearby pages sharing a component and both the main site and nested preview base path.

## Analytics and consent QA\n- Confirm GTM is not loaded before explicit analytics opt-in.\n- Confirm reject/unknown consent leaves analytics unloaded and the preference can be reopened.\n- Confirm production alone emits the GTM ID and production CSP allows only the required Google endpoints.\n- Confirm preview/development builds omit the GTM ID and remain noindex.\n- Confirm custom events never include personal data, form values, query strings, or full URLs.\n- Confirm GTM Preview and GA4 Realtime/DebugView only after the owner configures tags in Google UI.\n\n## Minimum change checklist
- [ ] Read the relevant skill and current implementation.
- [ ] Define acceptance criteria and impacted routes/components.
- [ ] Reuse existing components; no duplicate FAQ markup.
- [ ] Page-specific image selection is in content/front matter, not hardcoded CSS.
- [ ] Internal links/assets use `relative_url` where appropriate.
- [ ] Prominent actions use the right button component; inline references remain links.
- [ ] Front matter and unique permalinks are valid.
- [ ] Stylesheet/script cache tokens reviewed and bumped when needed.
- [ ] Build and static checks passed.
- [ ] Responsive and accessibility checks performed or explicitly marked unverified.
- [ ] PR preview is deployed from the exact head SHA.
- [ ] Production behavior is unchanged before approval.

## GitHub Pages release model
- Current known workflow: `.github/workflows/pages.yml` builds production from the default branch (historically `master`) and on PR builds the production site plus a nested preview.
- `.github/workflows/pages-preview-deploy.yml` listens for a successful PR workflow and rebuilds current production from `master`, adds a preview generated from the exact PR revision, then deploys the combined artifact.
- This arrangement exists to prevent preview builds from replacing production with feature-branch content.
- **Verify workflow source and current branch protections before every release; workflow implementation may change.**
- A green PR build is not proof that the Pages deployment has completed.
- The latest PR preview comment should identify the exact PR SHA. If the comment is stale, deployment is pending, or the SHA differs, do not claim the preview is current.
- Never merge without explicit user approval. Do not edit Pages settings or change hosting provider without approval.

## Evidence-based status reporting
Report separately:
- Source revision / commit SHA.
- Build workflow URL and conclusion.
- Preview deployment workflow URL and conclusion.
- Preview URL and whether its deployed revision matches the PR head.
- Routes and viewport sizes actually checked.
- Any checks not available or not performed.
- Whether production is unchanged.
- PR link and whether user approval is required.

Use accurate states: “build passed”, “preview deployment passed”, “preview visually checked”, and “production verified” are distinct claims.
