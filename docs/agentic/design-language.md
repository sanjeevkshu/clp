# CLP Design Language and Interaction Contracts

## Brand expression
- Brand: CLP — Continuous Learning & Progressive Evolution.
- Promise/line: **Learn. Apply. Evolve.**
- Experience should feel clear, thoughtful, practical, welcoming, modern, and trustworthy.
- Prefer calm confidence and useful guidance over AI hype, ornamental complexity, or generic SaaS styling.
- Keep learning approachable while preserving credibility and responsible-use context.

## Color foundation
The repository README documents these brand colors; the actual stylesheet is authoritative for rendered components, so inspect tokens and computed styles before making changes:
- Deep Ocean `#0B1F3B`
- Aquatic Blue `#00A7E9`
- Sky Aqua `#38BDF8`
- Violet accent `#8B5CF6`
- Soft white `#F8FAFC`

Use colors by role, not ad hoc:
- Deep/dark ocean: primary brand surfaces, headings, anchors, strong contrast.
- Aquatic/sky blue: action, focus, selected/active states, educational accents.
- Violet: selective accent only where it supports hierarchy.
- Soft white and restrained cool neutrals: content surfaces and breathing room.
Check contrast in both light and dark themes. Do not introduce arbitrary colors without a documented reason.

## Typography and layout
- Use existing font stacks, heading scales, spacing rhythm, radii, shadows, and breakpoints from CSS.
- Maintain a clear hierarchy: page title, section heading, supporting text, body, metadata/kicker.
- Use readable line lengths and generous spacing for long-form learning content.
- Use cards and decorative treatments only when they clarify hierarchy or affordance.
- Do not create inline CSS for a recurring design pattern when a shared class can express it.

## Interaction contracts
- Main navigation remains semantic navigation; mobile menu state must remain operable by keyboard and assistive technology.
- Theme toggle must preserve accurate accessible state and contrast.
- Prominent primary/secondary actions use established button styles. Inline citations and references remain text links.
- Learning articles use the secondary button for “Back to CLP Learn Library”.
- All FAQ/Common Questions use `_includes/faq-accordion.html`; question/answer data stays in `faq_items` front matter.
- FAQ uses native disclosure behavior and visible focus. Do not add JS merely to reproduce the native open/close interaction.
- Focus states must remain visible. Decorative icons are hidden from assistive technology with `aria-hidden="true"`.
- Interactive targets should generally be at least 44px high; avoid horizontal overflow on mobile.
- Respect `prefers-reduced-motion`.

## Responsive behavior
Validate at minimum:
- Narrow mobile portrait.
- Mobile landscape / short viewport.
- Tablet-like intermediate width.
- Desktop wide viewport.
Look for nav overlap, CTA wrapping, card alignment, hero image cropping, footer overflow, focus clipping, and text becoming too small or too wide.

## Image handling
- Content/front matter determines which image a page uses and its path.
- CSS determines how that selected image is displayed (fit, crop, position, aspect ratio, sizing, responsive behavior).
- Meaningful images require concise, useful alt text; decorative images use empty alt text.
- Never replace a user-approved brand mark or materially alter identity assets without explicit approval.

## Design review checklist
- Is hierarchy obvious in a few seconds?
- Does every action look like its real interaction type?
- Are similar components visually and behaviorally consistent?
- Are both light and dark themes legible?
- Does mobile portrait and landscape preserve intent?
- Does this design add a reusable rule or accidentally create a one-off?



## Theme-aware logo assets
Use the approved repository assets `assets/images/clp-vriksha-logo-dark.png` and `assets/images/clp-vriksha-logo-light.png` for both shared header and footer. Select the dark variant when `html[data-theme="dark"]` is active and the light variant when `html[data-theme="light"]` is active. The theme toggle in `assets/js/main.js` is the source of truth. Keep asset files unchanged, avoid filters that alter logo colors, and preserve established header/footer layout sizing. Validate both themes at desktop and narrow breakpoints.


## Theme-aware logo assets
Use `assets/images/clp-vriksha-logo-dark.png` and `assets/images/clp-vriksha-logo-light.png` for both shared header and footer. `assets/js/main.js` is authoritative for the active root theme (`html[data-theme="dark"]` / `html[data-theme="light"]`); the shared logo images must follow that state. Preserve the assets unchanged, do not apply filters that alter logo colors, and keep header/footer sizing governed by their existing layout rules. Validate both themes on desktop and mobile.


## Theme-aware page-hero contract (mandatory)
- Theme state is controlled by `html[data-theme="light"]` / `html[data-theme="dark"]` in the shared theme implementation. Do not rely on `prefers-color-scheme` for page surfaces when the site has an explicit theme toggle.
- Every inner-page hero must be inspected in both explicit themes. In light mode, use a pale brand-tinted surface and dark readable copy; do not leave dark-mode overlays, dark patches, or white body text behind the copy.
- Gradient headline text must have a theme-specific fallback and maintain readable contrast. Supporting copy, eyebrow/kicker, badges, and status callouts need explicit light-theme contrast as well as dark-theme styling.
- Hero image/overlay behavior must be intentional: keep text readable without hiding the image or creating a harsh rectangular patch. If a page has no hero image, use a coherent theme-aware surface rather than image-overlay rules.
- Theme-specific component surfaces must key off `html[data-theme]`, not the operating system preference. Validate theme switching without reloading, plus mobile portrait, mobile landscape/short viewport, tablet and desktop.
- Before marking a page ready, record both light- and dark-theme hero verification. A successful build alone is not visual verification.


## Mobile navigation theme contract (mandatory)
- The compact hamburger menu is a shared component. Keep Home, Learn, and the nested CLP Perspective link readable and visually aligned in both explicit themes.
- On mobile/tablet navigation, use a clearly bounded menu surface with theme-specific foreground/background/border colors; do not inherit hero text colors or transparent desktop-navigation treatments.
- Maintain a consistent minimum 44px row target, visible hover/focus feedback, and a clear nested indent for CLP Perspective under Learn.
- Theme state must follow `html[data-theme="light"]` / `html[data-theme="dark"]`; do not substitute operating-system preference media queries.
- When changing shared navigation styles, bump the corresponding stylesheet cache token in `_layouts/default.html` and validate both themes at mobile portrait, mobile landscape, tablet, and desktop. Confirm keyboard focus and menu open/close behavior remain functional.
