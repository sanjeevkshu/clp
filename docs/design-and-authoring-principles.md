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

## New-page release checklist

- [ ] Images are configured in content/front matter, not hardcoded as CSS page imagery.
- [ ] Prominent actions and the “Back to CLP Learn Library” navigation use established button components; ordinary inline references remain text links.
- [ ] Shared styles are reused; no unnecessary inline CSS or duplicate components.
- [ ] Mobile portrait, landscape, keyboard focus, contrast, and image rendering are checked.
- [ ] Front matter, internal links, alt text, and metadata are checked.
- [ ] The preview is reviewed before merge; after merge, verify the production deployment and share its link.
