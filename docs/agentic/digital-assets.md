# CLP Digital Asset Governance

## Asset categories
- **Brand identity:** approved logo/wordmark, emblem, favicon, lockups.
- **Editorial imagery:** hero, article, resource-card, and explanatory images.
- **Illustrations/diagrams:** learning frameworks, workflows, and concept visuals.
- **Media:** video thumbnails, launch/storyboard materials, audio/video files.
- **Interface assets:** icons and small decorative elements.

## Source-of-truth rules
- Store assets in the repository under `assets/images/` or the most appropriate existing assets directory unless there is a documented reason to change the structure.
- Page content/front matter chooses the asset and path; CSS controls presentation.
- Use `relative_url` for internal asset references and `absolute_url` for absolute metadata URLs.
- Prefer descriptive, stable, lowercase, hyphen-separated filenames. Do not rename referenced assets without updating all references and verifying the build.
- Do not commit secrets, personal data, unlicensed stock images, temporary exports, or unnecessary duplicates.
- Preserve original/approved brand assets. Do not redraw, recolor, crop, or replace them without approval.
- Document provenance, license/permission, intended use, and alt text for externally sourced or generated assets when relevant.

## Image selection and display
- Content markup should specify the selected image.
- Alt text should communicate the image's useful meaning in context, not merely say “image” or repeat a nearby heading.
- Decorative images use empty alt text; CSS-only decoration needs no redundant accessible name.
- Use responsive sizing, aspect ratio, crop, and object position in CSS.
- Avoid using CSS selectors to hardcode a specific page's background image. If an existing hero pattern uses a content-provided custom property, keep the asset choice in the page and presentation in CSS.
- For responsive or high-density assets, consider file size, format, loading priority, and appropriate dimensions.

## Performance and caching
- Use lazy loading for below-the-fold imagery where appropriate.
- Avoid lazy-loading a critical above-the-fold hero image; use high fetch priority only when it is genuinely critical.
- Check SVG markup for accidental external references, oversized embedded data, or accessibility issues.
- When a cached stylesheet/script changes, bump the corresponding cache-version token in the shared layout if that is the repository's current cache-busting mechanism.
- Keep output size reasonable and remove only assets proven unused; search references first.

## Asset QA
- Verify every local asset resolves in production and the nested PR preview.
- Check image appearance/crop at mobile portrait, mobile landscape, and desktop.
- Confirm alt text, licensing/provenance, dimensions, file size, and fallback behavior.
- Check browser console/network failures where browser tooling is available.


## Theme-aware CLP Vriksha lockups
- Dark-theme logo: `assets/images/clp-vriksha-logo-dark.png`.
- Light-theme logo: `assets/images/clp-vriksha-logo-light.png`.
- Both the global header and footer use these same approved assets, selected from the explicit active theme (`html[data-theme="dark|light"]`).
- Do not use alternate generated logo variants or recolor the files with filters.
- Test the visible logo in both themes and at desktop, mobile portrait, and mobile landscape widths. Existing header/footer sizing and spacing remain independently controlled by the shared CSS.


## Theme-aware CLP Vriksha lockups
- Dark-theme asset: `assets/images/clp-vriksha-logo-dark.png`.
- Light-theme asset: `assets/images/clp-vriksha-logo-light.png`.
- The same approved pair is used in both header and footer and selected from the explicit root theme set by `assets/js/main.js`.
- Do not substitute generated variants or recolor the PNGs with filters.
- Check both themes and desktop, mobile portrait, and mobile landscape. Keep layout sizing separate from asset selection.
