# CLP Social Extensions

**Status (2026-10-26):** Registry and conditional footer component are implemented on a feature branch. All channels remain disabled. Official profile destinations, DNS ownership/provider, redirect configuration, and live HTTPS verification are open.

## Goal

Give CLP stable, branded links to official social profiles while keeping the main site static and avoiding hard-coded platform URLs across pages.

## Proposed public aliases

| Platform | Branded alias | State |
| --- | --- | --- |
| Instagram | https://instagram.clpvriksha.com/ | Proposed; not activated |
| X | https://x.clpvriksha.com/ | Proposed; not activated |
| Facebook | https://facebook.clpvriksha.com/ | Proposed; not activated |
| LinkedIn | https://linkedin.clpvriksha.com/ | Proposed; not activated |

These are naming proposals only. Do not present them as live links until DNS, redirect behavior, and HTTPS have been tested.

## Source of truth

- Registry: `_data/social_extensions.yml`
- Shared component: `_includes/social-links.html`
- Footer integration: `_includes/footer.html`
- Styling: `assets/css/responsive-polish.css`

Each registry entry includes a platform label, branded subdomain, official `profile_url`, and an `enabled` flag. The shared include renders only enabled entries. Keep every entry disabled until the official profile is confirmed and the branded alias has been verified end-to-end.

## Activation runbook

1. Confirm the official CLP account/page URL for each platform. Never guess a handle or link to a personal profile by assumption.
2. Confirm who controls DNS for `clpvriksha.com` and which redirect/URL-forwarding service is approved.
3. Configure an HTTPS redirect for each requested subdomain to its confirmed profile URL. DNS records alone do not perform HTTP redirects; a CNAME to GitHub Pages is not a substitute for a redirect service.
4. Verify each alias over HTTPS, including final destination, status code, canonical host, mobile behavior, and absence of redirect loops.
5. Update `profile_url` in the registry and enable only the verified entry. Keep the footer link pointed at the branded alias.
6. Run the Jekyll build and PR preview checks; test footer links in desktop, tablet, mobile portrait/landscape, and both themes.
7. Update this document with the DNS/redirect provider, verification date, and any remaining operational owner. Do not commit provider credentials or tokens.

## Design and security rules

- Keep the social extension optional and data-driven; do not show disabled channels.
- Use only verified official CLP profiles. Avoid third-party URL shorteners.
- Preserve keyboard focus, readable labels, responsive wrapping, and the existing footer hierarchy.
- Do not add analytics or tracking parameters to redirects without explicit approval and privacy review.
- Social subdomains are redirect aliases, not separate websites and not native social profile hosts.
- DNS and redirect changes are external to this Jekyll repository and are not completed by merging the code.

## Acceptance criteria

- The Jekyll build succeeds with all entries disabled.
- No inactive alias appears as a clickable public link.
- Enabling an entry makes its platform label appear once in the shared footer and link to its branded alias.
- No profile URL, DNS record, or redirect is described as live until independently verified.
