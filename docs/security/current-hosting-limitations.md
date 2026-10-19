# Security headers with the current hosting stack

**Status: verified architectural constraint, 2026-10-19**

CLP is a Jekyll static site deployed to GitHub Pages. GoDaddy is the registrar/DNS management interface currently used for the domain. No Cloudflare or Supabase service is part of the approved architecture.

## What can be done in the repository

- Keep canonical HTTPS URLs and the existing strict-origin-when-cross-origin referrer policy.
- Add a carefully tested Content Security Policy using a CSP meta element only when its directives are verified against the actual site's scripts, styles, images and YouTube embeds.
- Use safe HTML defaults, escaped content fields, accessible embeds, and dependency/build checks.
- Test both clpvriksha.com and www.clpvriksha.com for TLS, redirects and response headers after deployment.

## What static HTML cannot set

HTML meta elements cannot set all HTTP response headers. In particular, Strict-Transport-Security (HSTS), X-Content-Type-Options, X-Frame-Options and Permissions-Policy cannot be set as equivalent response headers from a static page. These must be supplied by the hosting/server layer or a reverse proxy. GoDaddy DNS records alone do not add HTTP response headers.

Do not claim these headers are fixed merely because a meta element was added. If a scanner flags a header that GitHub Pages does not let the project configure, record the gap as a hosting limitation rather than adding misleading markup.

## Current-stack remediation

1. Re-run live header checks for the apex and www domains and save exact response-header evidence.
2. Fix issues addressable in source, such as mixed content, unsafe external links, or an unnecessarily broad referrer policy.
3. Keep unfixable response-header findings documented and prioritised. Full remediation of server-only headers requires a hosting layer that supports custom response headers; that is explicitly out of scope under the no-proxy decision.
4. Test the YouTube privacy-enhanced player against any policy change before merging.
