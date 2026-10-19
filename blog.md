---
title: "The CLP Blog"
description: "Ideas, perspectives and practical lessons from the CLP learning community."
permalink: /blog/
---
<section class="page-hero page-hero-learn" style="--page-hero-image:url('{{ '/assets/images/card-learn.jpg' | relative_url }}')"><p class="eyebrow">CLP BLOG</p><h1>Ideas worth sharing.<br><span>Learning worth applying.</span></h1><p>Perspectives, practical lessons and thoughtful experiments for a changing world.</p></section>
<section class="section editorial-index" aria-labelledby="blog-list-title">
<div class="section-heading"><div><p class="eyebrow">READ · REFLECT · APPLY</p><h2 id="blog-list-title">Latest from the community</h2><p class="section-subtitle">Every published article has passed the CLP editorial review process.</p></div></div>
{% assign published_posts = site.posts | sort: "date" | reverse %}
{% if published_posts.size > 0 %}
<div class="editorial-grid">{% for post in published_posts %}{% unless post.published == false %}
<article class="editorial-card">{% if post.image %}<a class="editorial-card-image" href="{{ post.url | relative_url }}"><img src="{{ post.image | relative_url }}" alt="{{ post.image_alt | default: post.title | escape }}" loading="lazy"></a>{% endif %}<div class="editorial-card-copy">{% if post.category %}<p class="card-kicker">{{ post.category | escape }}</p>{% endif %}<h3><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3><p>{{ post.description | default: post.excerpt | strip_html | normalize_whitespace | truncate: 180 | escape }}</p><p class="editorial-meta"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%-d %B %Y" }}</time>{% if post.author %} · {{ post.author | escape }}{% endif %}</p><a class="learn-card-button" href="{{ post.url | relative_url }}">Read article <span aria-hidden="true">↗</span></a></div></article>
{% endunless %}{% endfor %}</div>
{% else %}
<div class="editorial-empty"><h3>Thoughtful ideas are taking root.</h3><p>CLP blog articles are reviewed before publication. Contributors can use the publishing guide to prepare a post and submit it for editorial approval.</p><a class="learn-card-button" href="{{ '/blog/contribute/' | relative_url }}">Read the contributor publishing guide <span aria-hidden="true">↗</span></a></div>
{% endif %}
</section>