# CLP Phase 2 — Search, LinkedIn and WhatsApp launch runbook

## Status boundaries

- Website changes are proposed through a feature branch and preview. Do not merge to production without explicit owner approval.
- Google Search Console is an external property. Repository changes cannot verify ownership or submit the sitemap on the owner's behalf.
- LinkedIn Page and WhatsApp Channel creation require the owner's authorized account session. Never request passwords or verification codes in chat.
- Do not invent social URLs. Add only confirmed public profile/channel links.

## A. Google Search Console

1. Open the verified clpvriksha.com property in Google Search Console.
2. Open **Sitemaps** and submit sitemap.xml. The expected sitemap is https://clpvriksha.com/sitemap.xml.
3. Confirm the sitemap status is successful and review discovered URLs.
4. Use **URL Inspection** for https://clpvriksha.com/, /learn/, /learn/perspective/, /about/ and /connect/ after /connect/ is approved and published.
5. Run **Test live URL**. Check crawl allowed, indexing allowed, fetch status and Google-selected canonical.
6. Request indexing only for important public production URLs that pass the live test. Never request indexing for preview URLs.
7. Review **Page indexing** and **Manual actions / Security issues** reports. Record errors and the date checked.
8. Revisit after Google has had time to crawl. Sitemap submission and indexing requests are not guarantees of indexing or ranking.

## B. Create the official LinkedIn Page

1. Sign in to LinkedIn with your own real personal profile. Use desktop if possible.
2. Open the LinkedIn **For Business** menu and choose **Create a Company Page**.
3. Select the page type appropriate to CLP (normally Company, unless CLP's legal/organizational status makes another type more accurate).
4. Proposed Page name: CLP — Learn. Apply. Evolve. If LinkedIn's naming rules make this too long, use CLP and use the tagline below.
5. Proposed public URL: choose the closest available, recognizable CLP slug. Do not assume availability.
6. Website: https://clpvriksha.com/connect/ after the landing page is approved and live.
7. Tagline: Continuous Learning & Progressive Evolution | Learn. Apply. Evolve.
8. Use the existing approved CLP logo asset unchanged for the profile image. Do not generate a replacement logo.
9. Suggested Overview:
   > CLP — Continuous Learning & Progressive Evolution — is a learning initiative for curious minds navigating a changing world. We explore emerging ideas, build practical skills, examine new perspectives and turn knowledge into action. Through CLP Decodes, CLP Masterclass, CLP Perspective and CLP Evolution Lab, we aim to make continuous, applied learning part of everyday life. Learn. Apply. Evolve.
10. Complete all required fields truthfully. Do not invent company size, location, legal entity status or credentials.
11. Confirm you are authorized to represent CLP, create the Page, and review it as a public visitor.
12. Copy the resulting public Page URL. Only then update the website's social-link registry and publish the launch post.

Official guide: https://www.linkedin.com/help/linkedin/answer/a544879

## C. Create the WhatsApp Channel

1. Open WhatsApp or WhatsApp Business using an account you control. The channel can keep the admin's phone number private from followers, but creation still requires a WhatsApp account.
2. Open **Updates** → add/plus icon → **Create channel**.
3. Name: CLP — Learn. Apply. Evolve.
4. Description:
   > Continuous learning for a changing world. Explore practical skills, emerging ideas, fresh perspectives and learning resources from CLP. Learn. Apply. Evolve.
5. Add the existing CLP logo as the channel icon, without altering the artwork.
6. Create the channel, review its public information and publish a welcome update.
7. Use the channel's **Share** option to copy its official invite link. Test the link in a browser or another account before sharing.
8. Add the verified link to the website only after the test succeeds. Do not put the admin's personal phone number on the website.

Official guide: https://faq.whatsapp.com/794229125227200/

## D. Publish the LinkedIn launch post

Use docs/social/linkedin-launch-post.md. Publish only after the official Page exists, the website landing page is live, and the final URLs have been tested. Use the campaign card after exporting to PNG/JPG and reviewing at mobile size.

## E. Acceptance checklist

- [ ] Search Console property verified and sitemap accepted.
- [ ] Important public URLs pass live inspection and have correct canonicals.
- [ ] CLP Connect landing page passes desktop, tablet and mobile preview QA in both themes.
- [ ] Official LinkedIn Page URL verified; profile logo and page description reviewed.
- [ ] WhatsApp Channel created; public invite link tested; phone number not exposed on CLP website.
- [ ] LinkedIn launch post reviewed and published by an authorized Page admin.
- [ ] Website links updated in a separate PR; no production merge before owner approval.
