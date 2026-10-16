---
name: clp-qa
description: Validate CLP content, accessibility, responsive behavior, metadata, assets, shared components, and regression risks.
---

# CLP QA Skill

## Use when
Reviewing any change, preparing a PR, investigating a defect, or validating a release.

## Procedure
1. Read `AGENTS.md` and `docs/agentic/qa-and-release.md`.
2. Turn the request into observable acceptance criteria.
3. Identify shared components and neighboring pages affected by the change.
4. Inspect source and generated output; do not rely only on source-level appearance.
5. Run the available build, syntax, link/asset, and workflow checks.
6. Check semantic HTML, keyboard operation, visible focus, heading order, accessible names, alt text, contrast, touch targets, and reduced motion.
7. Test mobile portrait, mobile landscape/short viewport, intermediate width, and desktop.
8. Check light/dark theme where relevant, navigation, forms, buttons, accordion states, and external links.
9. Verify production route paths and nested preview paths.
10. Report actual evidence and mark unperformed checks as unverified.

## Acceptance criteria
- Every claim is tied to an actual check.
- The latest successful build and preview correspond to the exact current PR head SHA.
- Shared-component regressions are checked across affected pages.
- No merge or production change occurs without explicit approval.
