# CLP design and authoring principles

These rules apply to **every new page, article, landing page, and future content refresh**. Treat them as a publishing checklist, not optional polish.

## 1. Content owns content; CSS owns presentation

- Choose and configure each page's images in its Markdown/content markup or supported front matter—not in CSS background declarations that hardcode a page's image.
- Keep image paths page-specific and easy to replace. Use Jekyll's `relative_url` filter for local assets.
- Use CSS for sizing, cropping, aspect ratios, spacing, borders, responsive behavior, and decorative treatment.
- Give meaningful images concise, descriptive alt text. Use empty alt text only for purely decorative images.
- Apply the same rule to landing-page hero images, learning-card artwork, and article-header artwork.

## 2. Make primary calls to action look like buttons

- A prominent next step—read a guide, start a challenge, join, contact, or sign up—must use a shared button class, not an unstyled text link.
- On learning-library cards, use the existing `learn-card-button` component.
- In article endings and other content sections, use the shared `content-button` component inside an `article-cta-group` (or the equivalent established shared CTA container).
- Use clear action labels (for example, “Start the challenge” or “Build a 30-Day AI Learning Plan”) and preserve the accessible link destination. Decorative arrows/icons should be hidden from assistive technology with `aria-hidden="true"`.
- Use a clear secondary button for prominent “Back to CLP Learn Library” navigation on learning articles, so it is easy to find and tap.
- Keep ordinary inline references and citations as text links. Do not turn every link into a button; reserve buttons for meaningful primary/secondary actions.

## 3. Use shared components instead of one-off styling

- Reuse existing classes and page patterns before introducing new styles.
- Do not put visual styling inline in content when a reusable CSS class is available.
- If a recurring visual pattern is missing, create a shared component and document it instead of copying slightly different markup across pages.
- Keep page-specific content (titles, copy, image paths, CTA labels and destinations) in the page; keep reusable visual behavior in CSS.

## 4. Every page must be responsive and accessible

- Check narrow mobile portrait and landscape layouts as well as desktop.
- Prevent horizontal overflow; ensure images preserve their intended proportions and text remains readable.
- Make CTA targets comfortably tappable (at least 44px high), with visible keyboard focus and sufficient contrast.
- Use semantic headings in order, descriptive link text, and meaningful alt text. Respect reduced-motion preferences for animated interactions.

## 5. SEO and publishing checks

- Preserve valid YAML front matter, including a unique title, useful description, and intended permalink.
- Use Jekyll's `relative_url` filter for internal paths so links work under the repository's GitHub Pages base path.
- Check internal links, image paths, page metadata, and the rendered page after deployment.
- Do not claim a page is verified until the relevant build and live/preview checks have actually passed.

## 6. Common Questions always use the shared accordion

- Every Common Questions, FAQ, or equivalent question-and-answer section must render as an accordion, wherever it appears on the site—landing pages, learning articles, and future content.
- Use the shared `_includes/faq-accordion.html` component. Do not recreate FAQ markup or one-off styles on individual pages.
- Keep page-specific questions and answers in that page's `faq_items` front matter; pass them to the include with a unique section id and the appropriate title/kicker.
- The component uses native `<details>` and `<summary>` elements for keyboard-accessible, no-JavaScript disclosure behavior, and the shared `.clp-faq-*` styles for consistent responsive and dark-theme presentation.
- Preserve readable answer content, semantic heading order, visible keyboard focus, and unique IDs when reusing the component.

## New-page release checklist

- [ ] Images are configured in content/front matter, not hardcoded as CSS page imagery.
- [ ] Prominent actions and the “Back to CLP Learn Library” navigation use established button components; ordinary inline references remain text links.
- [ ] Shared styles and includes are reused; all Common Questions/FAQ sections use `faq-accordion.html` with page-specific `faq_items`; no duplicate components.
- [ ] Mobile portrait, landscape, keyboard focus, contrast, and image rendering are checked.
- [ ] Front matter, internal links, alt text, and metadata are checked.
- [ ] The preview is reviewed before merge; after merge, verify the production deployment and share its link.


## 7. Homepage launch card, theme parity and footer

- Keep the existing homepage hero and primary navigation unchanged.
- The homepage launch feature is a compact editorial card: teaser image, short description, clear title, and one primary CTA to the launch story. Avoid competing CTAs in this feature.
- Set image source and alt text in page content; use shared CSS classes for layout, crop, responsive behavior, hover and focus treatment.
- Every new card and content section must be checked in both light and dark themes. Use explicit theme-aware foreground, surface, border and accent colors; avoid hard-coded colors that reduce contrast.
- The footer should provide clear, multi-column discovery on wide screens and stack cleanly on mobile. Keep link labels descriptive, spacing consistent, and focus indicators visible.
- On every meaningful CSS change, update the stylesheet cache-busting version in `_layouts/default.html`.
- Validate desktop, tablet, mobile portrait and landscape, keyboard focus, contrast, reduced motion, no horizontal overflow, and preview noindex before requesting review.
