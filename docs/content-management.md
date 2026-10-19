# CLP content management

The site is managed in GitHub. Pages are written in Markdown with YAML front matter; shared presentation lives in the layout, includes and assets folders.

## Edit a page
1. Open a Markdown page in GitHub and select Edit.
2. Keep the front matter fields (title, description, permalink) intact.
3. Preview the Markdown, commit the change, and check the GitHub Actions deployment.

## Blog publishing and approval

Blog posts use Jekyll's standard _posts/YYYY-MM-DD-title.md format. The blog index only lists posts merged into the production branch, so a contributor's draft remains unpublished while it is in a pull request.

1. Copy docs/templates/blog-post-template.md into _posts/ and name it YYYY-MM-DD-short-title.md.
2. Replace every example field, verify sources and image rights, and preview the rendered article.
3. Submit a pull request to master; do not commit contributor drafts directly to master.
4. The editor reviews accuracy, attribution, tone, accessibility, image rights, links and SEO metadata. Request changes or reject the submission when needed.
5. Only merge after explicit editorial approval. Merging is the publication action.
6. If changes are requested, update the same pull request. Keep a record of the reviewer and decision in the PR conversation.

The public Blog link is in the footer only, not the primary navigation.

## Media publishing

Media entries are Jekyll collection documents stored under _media/. Copy docs/templates/media-item-template.md, replace the example metadata, and submit it in a pull request. The media gallery and detail template reference external YouTube/Google-hosted media; the CLP repository does not store or stream video files. Verify the original URL, publication permissions, thumbnail, duration, transcript/captions and descriptive metadata before approval.

For YouTube, set youtube_id to the video ID. For another approved hosted media item, use media_url instead. Do not publish a record with placeholder IDs or example URLs.

## Comments and moderation

Public comments are intentionally on hold. The article template does not display a comment feature while CLP evaluates a guest-friendly hosted option. GitHub Pages is static and cannot securely accept, store or moderate first-party comments on its own. Do not add GitHub Discussions as the default public commenting path because many readers will not have GitHub accounts. Any third-party comment integration requires an explicit owner decision, privacy/moderation review, and configuration before it is enabled.

## Before launch
- Replace the provisional vector wordmark with the approved original CLP logo file when available.
- Confirm url and baseurl in _config.yml match the repository and Pages settings.
- Make the repository public or verify your plan supports Pages for a private repository.
- Check keyboard navigation, mobile layout, links, contrast and page metadata.
- Configure real email/contact and newsletter handling before collecting subscriber data.
- Add YouTube channel and episode URLs only after they exist.

## Design and authoring standards

Apply the CLP design and authoring principles (design-and-authoring-principles.md) to every new page and article. In particular, configure images in page content and use the established button component for prominent calls to action.

## FAQ and Common Questions

All question-and-answer sections must use the shared accordion, no matter which page they appear on. Put the page-specific questions and answers in YAML front matter under faq_items, then render them with the reusable include:

{% raw %}{% include faq-accordion.html id="unique-page-faq" title="Common questions" items=page.faq_items %}{% endraw %}

Use a unique id for each FAQ section. Optional kicker text can be passed when a section needs a short label. The include supplies consistent semantic markup and styling; do not duplicate FAQ HTML or add page-specific accordion CSS.
