---
title: "CLP Media Library"
description: "Explore CLP videos, explainers and conversations hosted on YouTube and Google platforms."
permalink: /media/
---
<section class="page-hero page-hero-learn" style="--page-hero-image:url('{{ '/assets/images/card-community.jpg' | relative_url }}')"><p class="eyebrow">WATCH · LISTEN · EXPLORE</p><h1>Ideas in motion.<br><span>Learning in every format.</span></h1><p>Explore CLP videos, explainers and conversations. Playback is delivered by the original media host.</p></section>
<section class="section editorial-index" aria-labelledby="media-library-title"><div class="section-heading"><div><p class="eyebrow">CLP MEDIA LIBRARY</p><h2 id="media-library-title">Explore the collection</h2><p class="section-subtitle">Browse by topic, format and learning pathway.</p></div></div>
{% assign media_items = site.media | sort: "date" | reverse %}
{% if media_items.size > 0 %}
<div class="media-library-grid">{% for item in media_items %}<article class="media-library-card"><a class="media-library-thumb" href="{{ item.url | relative_url }}" aria-label="View {{ item.title | escape }}">{% if item.thumbnail %}<img src="{{ item.thumbnail | escape }}" alt="{{ item.thumbnail_alt | default: item.title | escape }}" loading="lazy">{% elsif item.youtube_id %}<img src="https://i.ytimg.com/vi/{{ item.youtube_id | escape }}/hqdefault.jpg" alt="{{ item.title | escape }}" loading="lazy">{% else %}<span class="media-placeholder" aria-hidden="true">▶</span>{% endif %}{% if item.duration %}<span class="media-duration">{{ item.duration | escape }}</span>{% endif %}</a><div class="media-library-copy">{% if item.category %}<p class="card-kicker">{{ item.category | escape }}</p>{% endif %}<h3><a href="{{ item.url | relative_url }}">{{ item.title | escape }}</a></h3><p>{{ item.description | escape }}</p><a class="learn-card-button" href="{{ item.url | relative_url }}">View media details <span aria-hidden="true">↗</span></a></div></article>{% endfor %}</div>
{% else %}
<div class="editorial-empty"><h3>The media library is ready for its first feature.</h3><p>Each entry can reference a YouTube video or other approved Google-hosted media. The site stores metadata and embeds, not video files.</p><a class="learn-card-button" href="{{ '/docs/content-management/' | relative_url }}">Read the media publishing guide <span aria-hidden="true">↗</span></a></div>
{% endif %}</section>
