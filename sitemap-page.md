---
title: "CLP Site Map"
description: "Find your way around CLP Vriksha: explore learning guides, perspectives, articles, media, and information about the CLP community."
permalink: /sitemap/
sitemap: false
noindex: true
---

<section class="page-hero page-hero-learn" style="--page-hero-image:url('{{ '/assets/images/card-learn.jpg' | relative_url }}')">
  <p class="eyebrow">FIND YOUR WAY</p>
  <h1>Explore CLP.<br><span>Every path starts somewhere.</span></h1>
  <p>A simple guide to the pages, learning resources and stories available across CLP Vriksha.</p>
</section>

<section class="section" aria-labelledby="site-map-main">
  <div class="prose">
    <h2 id="site-map-main">Start here</h2>
    <ul class="clp-site-map-list">
      <li><a href="{{ '/' | relative_url }}">Home</a> — the CLP vision and featured pathways</li>
      <li><a href="{{ '/learn/' | relative_url }}">Learn with CLP</a> — practical guides, explainers and challenges</li>
      <li><a href="{{ '/learn/perspective/' | relative_url }}">CLP Perspective</a> — ideas and viewpoints on continuous learning</li>
      <li><a href="{{ '/about/' | relative_url }}">About CLP</a> — purpose, principles and the learning loop</li>
      <li><a href="{{ '/community/' | relative_url }}">Community</a> — ways to participate and share ideas</li>
      <li><a href="{{ '/contact/' | relative_url }}">Contact</a> — get in touch with CLP</li>
      <li><a href="{{ '/launch/' | relative_url }}">Our story</a> — the CLP vision and launch story</li>
    </ul>

    <h2 id="site-map-learning">Learning library</h2>
    <p>Explore practical topics, learning experiments and perspectives. New resources may be added over time.</p>
    <ul class="clp-site-map-list">
    {% assign learning_pages = site.pages | sort: "title" %}
    {% for item in learning_pages %}
      {% if item.url contains "/learn/" and item.sitemap != false and item.title and item.url != "/learn/" %}
      <li><a href="{{ item.url | relative_url }}">{{ item.title | escape }}</a>{% if item.description %} — {{ item.description | strip_html | normalize_whitespace | escape }}{% endif %}</li>
      {% endif %}
    {% endfor %}
    </ul>

    <h2 id="site-map-stories">Stories and media</h2>
    <ul class="clp-site-map-list">
      <li><a href="{{ '/blog/' | relative_url }}">CLP Blog</a> — articles, ideas and practical lessons</li>
      <li><a href="{{ '/media/' | relative_url }}">Media Library</a> — videos and other learning media</li>
    {% assign published_posts = site.posts | sort: "date" | reverse %}
    {% for item in published_posts %}
      {% unless item.published == false or item.sitemap == false %}
      <li><a href="{{ item.url | relative_url }}">{{ item.title | escape }}</a>{% if item.description %} — {{ item.description | strip_html | normalize_whitespace | escape }}{% endif %}</li>
      {% endunless %}
    {% endfor %}
    {% assign media_items = site.media | sort: "title" %}
    {% for item in media_items %}
      {% if item.sitemap != false %}
      <li><a href="{{ item.url | relative_url }}">{{ item.title | escape }}</a>{% if item.description %} — {{ item.description | strip_html | normalize_whitespace | escape }}{% endif %}</li>
      {% endif %}
    {% endfor %}
    </ul>

    <h2 id="site-map-policies">Helpful information</h2>
    <ul class="clp-site-map-list">
      <li><a href="{{ '/privacy/' | relative_url }}">Privacy</a> — how CLP approaches privacy and analytics</li>
      <li><a href="{{ '/blog/contribute/' | relative_url }}">Blog contribution guide</a> — prepare an article for editorial review</li>
      <li><a href="{{ '/media/contribute/' | relative_url }}">Media contribution guide</a> — propose a media feature</li>
    </ul>
  </div>
</section>
