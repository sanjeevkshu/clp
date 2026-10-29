---
layout: default
title: "Health Board"
description: "A practical CLP webmaster dashboard for website usage, engagement, search visibility and performance signals."
permalink: /dashboard/
noindex: true
sitemap: false
---

<section class="page-hero dashboard-hero">
  <p class="eyebrow">CLP HEALTH BOARD</p>
  <h1>Website signals, <span>made clear.</span></h1>
  <p class="hero-lede">A single place to understand whether people are finding CLP, engaging with learning resources, and experiencing a fast, reliable website.</p>
  <p class="dashboard-status"><strong>Connection status:</strong> Not connected — Google Analytics and Search Console data are not available yet.</p>
</section>

<section class="content-section dashboard-content" aria-labelledby="dashboard-overview">
  <div class="section-heading">
    <p class="eyebrow">THE QUICK READ</p>
    <h2 id="dashboard-overview">Your website health at a glance</h2>
    <p>Metrics are not connected yet. Values remain intentionally blank until a validated, privacy-safe data feed is available.</p>
  </div>

  <div class="dashboard-grid" aria-label="Illustrative KPI cards">
    <article class="dashboard-card">
      <p class="dashboard-kpi-label">Active users</p><p class="dashboard-kpi-value">—</p>
      <p class="dashboard-kpi-note">People active in the selected period.</p><span class="dashboard-signal signal-neutral">Awaiting GA4</span>
    </article>
    <article class="dashboard-card">
      <p class="dashboard-kpi-label">Engagement rate</p><p class="dashboard-kpi-value">—</p>
      <p class="dashboard-kpi-note">Share of sessions that were engaged.</p><span class="dashboard-signal signal-neutral">Awaiting GA4</span>
    </article>
    <article class="dashboard-card">
      <p class="dashboard-kpi-label">Organic search clicks</p><p class="dashboard-kpi-value">—</p>
      <p class="dashboard-kpi-note">Visits earned from Google Search results.</p><span class="dashboard-signal signal-neutral">Awaiting Search Console</span>
    </article>
    <article class="dashboard-card">
      <p class="dashboard-kpi-label">Core Web Vitals</p><p class="dashboard-kpi-value">—</p>
      <p class="dashboard-kpi-note">Field experience for real visitors, where data is available.</p><span class="dashboard-signal signal-neutral">Awaiting CrUX / PSI</span>
    </article>
  </div>

  <div class="dashboard-panels">
    <article class="dashboard-panel">
      <p class="eyebrow">ACQUISITION</p><h3>How are people finding CLP?</h3>
      <p>Track sessions by channel, organic landing pages, referral sources and search clicks. Compare the same date range with the previous period before treating a change as a trend.</p>
      <ul><li>Watch: organic search and referral contribution.</li><li>Investigate: sudden traffic drops, new 404s or untagged campaigns.</li><li>Act: improve the landing page that should answer the visitor's intent.</li></ul>
    </article>
    <article class="dashboard-panel">
      <p class="eyebrow">ENGAGEMENT</p><h3>Are visitors learning and exploring?</h3>
      <p>Use engaged sessions, engagement rate, average engagement time and high-value page paths. A longer visit is not automatically better; interpret it alongside the page's purpose.</p>
      <ul><li>Watch: learning article entry and onward journeys.</li><li>Investigate: high exits on key learning pages.</li><li>Act: clarify the next step with useful, accessible CTA buttons.</li></ul>
    </article>
    <article class="dashboard-panel">
      <p class="eyebrow">PERFORMANCE</p><h3>Is the experience healthy?</h3>
      <p>Prioritize field Core Web Vitals when sufficient real-user data exists; use PageSpeed Insights lab results to diagnose issues, not as a substitute for field data.</p>
      <ul><li>Good targets: LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1.</li><li>Investigate: slow mobile pages, layout shifts and broken assets.</li><li>Act: fix the highest-impact template or asset first.</li></ul>
    </article>
    <article class="dashboard-panel">
      <p class="eyebrow">SEARCH & DISCOVERY</p><h3>Can the right content be discovered?</h3>
      <p>Pair Search Console impressions, clicks, CTR and average position with the site's automated canonical, robots, structured-data and sitemap checks.</p>
      <ul><li>Watch: queries with impressions but weak CTR.</li><li>Investigate: excluded pages, canonical mismatches and crawl errors.</li><li>Act: improve titles and answers without sacrificing accuracy.</li></ul>
    </article>
  </div>

  <aside class="dashboard-next-steps">
    <h2>Connect real data safely</h2>
    <ol>
      <li>Use a server-side integration with Google Analytics Data API and least-privilege access to the intended GA4 property.</li>
      <li>Optionally connect Google Search Console and PageSpeed Insights / CrUX for search and performance signals.</li>
      <li>Store credentials only in a protected backend or secret manager. Never put service-account keys, OAuth refresh tokens or API secrets in this static page, Git history, or browser JavaScript.</li>
      <li>Keep public output aggregate-only and sanitized. <strong>Noindex is not access control.</strong></li>
      <li>Show the date range, last refresh, source, comparison period and data gaps next to each KPI. Label missing or delayed data instead of inventing values.</li>
    </ol>
    <p class="dashboard-note">This GitHub Pages site is static. A live private dashboard needs a separate authenticated data layer; until that is provisioned, the page intentionally displays no fabricated metrics.</p>
  </aside>
</section>

<style>
.dashboard-hero{min-height:360px;padding-top:58px;padding-bottom:58px}
.dashboard-hero .hero-lede{max-width:700px}
.dashboard-hero .dashboard-status{max-width:100%;color:inherit}
html[data-theme="light"] .dashboard-hero{background:linear-gradient(135deg,#f5faff 0%,#eaf5fb 68%,#e2f0f8 100%);color:#10243e}
html[data-theme="light"] .dashboard-hero .eyebrow{color:#075b70}
html[data-theme="light"] .dashboard-hero h1,
html[data-theme="light"] .dashboard-hero h1 span{color:#10243e}
html[data-theme="light"] .dashboard-hero h1 span{background:linear-gradient(90deg,#00647b,#5140a8);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
html[data-theme="light"] .dashboard-hero .hero-lede{color:#334d64}
html[data-theme="light"] .dashboard-hero .dashboard-status{background:#ffffffb8;border-color:#b8d6e5;color:#18364f}
html[data-theme="dark"] .dashboard-hero .hero-lede{color:#d7e8fa}
html[data-theme="dark"] .dashboard-hero .dashboard-status{background:#20d7f410;border-color:#20d7f466;color:#d7e8fa}
.dashboard-hero h1{max-width:900px}
.dashboard-status{display:inline-block;margin-top:16px;padding:10px 14px;border:1px solid #20d7f466;border-radius:12px;background:#20d7f410;font-size:.92rem}
.dashboard-content{max-width:1200px;margin:0 auto;padding:24px clamp(20px,4vw,48px) 72px}
.dashboard-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin:28px 0}
.dashboard-card,.dashboard-panel,.dashboard-next-steps{border:1px solid var(--line);border-radius:20px;background:var(--paper);padding:22px;box-shadow:0 12px 32px #0613290a}
.dashboard-kpi-label{font-size:.85rem;font-weight:800;color:var(--muted);margin:0}
.dashboard-kpi-value{font-size:2.25rem;line-height:1.2;font-weight:850;letter-spacing:-.04em;margin:12px 0}
.dashboard-kpi-note{font-size:.88rem;color:var(--muted);min-height:3em}
.dashboard-signal{display:inline-flex;font-size:.73rem;font-weight:800;border-radius:99px;padding:5px 9px;background:#64748b18}
html[data-theme="light"] .dashboard-signal{color:#52677d;background:#e8eef5}
html[data-theme="dark"] .dashboard-signal{color:#c4d2e2;background:#263d56}
.dashboard-panels{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;margin:32px 0}
.dashboard-panel h3{font-size:1.3rem;line-height:1.25;margin:8px 0 12px}
.dashboard-panel p,.dashboard-panel li,.dashboard-next-steps li{color:var(--muted)}
.dashboard-panel ul,.dashboard-next-steps ol{padding-left:22px}
.dashboard-next-steps{margin-top:30px;background:linear-gradient(135deg,#20d7f410,#8b5cf608)}
.dashboard-next-steps h2{margin-top:0}
.dashboard-note{padding-top:12px;border-top:1px solid var(--line);font-size:.9rem}
@media(max-width:900px){.dashboard-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:620px){.dashboard-grid,.dashboard-panels{grid-template-columns:1fr}.dashboard-card,.dashboard-panel,.dashboard-next-steps{padding:18px}.dashboard-hero{min-height:unset}}
html[data-theme="dark"] .dashboard-card,html[data-theme="dark"] .dashboard-panel,html[data-theme="dark"] .dashboard-next-steps{background:var(--ocean-2);border-color:#ffffff20}
html[data-theme="dark"] .dashboard-kpi-label,html[data-theme="dark"] .dashboard-kpi-note,html[data-theme="dark"] .dashboard-panel p,html[data-theme="dark"] .dashboard-panel li,html[data-theme="dark"] .dashboard-next-steps li{color:#b8cbe0}
html[data-theme="light"] .dashboard-card,html[data-theme="light"] .dashboard-panel,html[data-theme="light"] .dashboard-next-steps{background:#fff;border-color:#d9e8f4}
html[data-theme="light"] .dashboard-kpi-label,html[data-theme="light"] .dashboard-kpi-note,html[data-theme="light"] .dashboard-panel p,html[data-theme="light"] .dashboard-panel li,html[data-theme="light"] .dashboard-next-steps li{color:#52677d}
</style>
