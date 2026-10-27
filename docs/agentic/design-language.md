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


## Logo contrast across themes
Approved header and footer logo artwork MUST sit on a tight circular white disc in both light and dark themes, with 1px of inset around the header artwork and no container padding around the footer artwork. Keep the artwork unmodified and do not apply theme-specific filters. The header disc is 62px on desktop and 50px on narrow screens. The footer disc is 140px on desktop and 120px on narrow screens; the approved transparent footer PNG is scaled to 124% within the disc to reduce excess apparent white space. Verify the tree, wordmark, and tagline remain fully visible at desktop, mobile portrait, and mobile landscape before merge.
