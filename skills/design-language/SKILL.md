---
name: clp-design-language
description: Apply and evolve CLP visual identity, design tokens, responsive layouts, and accessible interaction patterns.
---

# CLP Design Language Skill

## Use when
Creating or modifying page layouts, components, typography, colors, spacing, interaction states, responsive behavior, buttons, navigation, themes, or illustrations.

## Procedure
1. Read `AGENTS.md` and `docs/agentic/design-language.md`.
2. Inspect current CSS tokens, component classes, and similar pages before inventing styles.
3. State which existing component/pattern will be reused or why a new shared component is needed.
4. Keep page content and asset selection separate from presentation.
5. Preserve the CLP tone: clear, practical, calm, trustworthy, and learner-centered.
6. Validate contrast, visible keyboard focus, semantic HTML, touch targets, reduced motion, and light/dark themes. For every inner-page hero, explicitly inspect kicker, headline/gradient text, supporting copy, status/badges, overlay and surface colors in both themes; use `html[data-theme]` rather than `prefers-color-scheme` when theme toggle state exists.
7. For the hamburger menu, verify explicit light/dark foreground, surface, border, hover/focus and nested-link hierarchy; confirm Home, Learn and CLP Perspective remain readable and aligned.
8. Test mobile portrait, mobile landscape/short viewport, intermediate width, and desktop.
9. Update the design language doc when a new token, component contract, or global rule is introduced.

## Acceptance criteria
- Existing design language is coherent; no unexplained one-off colors or inline styles.
- Actions are visually distinguishable from ordinary links.
- No horizontal overflow or clipped focus indicators.
- Meaningful images have useful alt text; decorative imagery is appropriately hidden.
- Shared patterns are documented and usable by future authors.
- Inner-page hero text and overlays remain legible and visually coherent in both explicit themes, including after switching themes without a reload.
