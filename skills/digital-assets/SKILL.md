---
name: clp-digital-assets
description: Select, add, optimize, reference, and validate CLP logos, images, illustrations, and media.
---

# CLP Digital Assets Skill

## Use when
Adding/replacing logos, page hero images, card artwork, article images, icons, diagrams, video thumbnails, or other media.

## Procedure
1. Read `AGENTS.md` and `docs/agentic/digital-assets.md`.
2. Search for an existing approved asset and all current references before creating or replacing one.
3. Confirm provenance, permission/license, intended use, and whether the asset is brand-approved.
4. Put the asset in the appropriate repository assets directory with a descriptive stable filename.
5. Select the asset in page content/front matter; do not hardcode a page-specific image choice in CSS.
6. Use `relative_url` for local asset paths; `absolute_url` only where metadata needs an absolute URL.
7. Add meaningful alt text or mark the image decorative where appropriate.
8. Check dimensions, file size, format, responsive crop, loading behavior, and cached references.
9. Update cache-busting tokens when the shared stylesheet/script changes, using the existing mechanism.
10. Verify the asset in production build output and nested PR preview.

## Acceptance criteria
- Asset provenance is known, and brand assets are not altered without approval.
- No broken references, duplicate unnecessary assets, secrets, or unlicensed media.
- Correct responsive display and accessibility.
- Page author can change the chosen image without changing CSS.
