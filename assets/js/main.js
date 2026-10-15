document.addEventListener('DOMContentLoaded', () => {
  // Accessible theme switch: saved preference wins; otherwise follow system preference.
  const themeToggle = document.querySelector('#theme-toggle');
  const root = document.documentElement;
  const savedTheme = (() => { try { return localStorage.getItem('clp-theme'); } catch (_) { return null; } })();
  const preferredTheme = savedTheme || (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
  const applyTheme = theme => {
    root.dataset.theme = theme;
    if (themeToggle) {
      const light = theme === 'light';
      themeToggle.setAttribute('aria-pressed', String(light));
      themeToggle.setAttribute('aria-label', light ? 'Switch to dark theme' : 'Switch to light theme');
      const label = themeToggle.querySelector('.theme-toggle-label');
      const icon = themeToggle.querySelector('.theme-toggle-icon');
      if (label) label.textContent = light ? 'Dark theme' : 'Light theme';
      if (icon) icon.textContent = light ? '☾' : '☼';
    }
    const meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.content = theme === 'light' ? '#f5faff' : '#061329';
  };
  applyTheme(preferredTheme);
  if (themeToggle) themeToggle.addEventListener('click', () => {
    const next = root.dataset.theme === 'light' ? 'dark' : 'light';
    applyTheme(next);
    try { localStorage.setItem('clp-theme', next); } catch (_) { /* Theme still works for this visit. */ }
  });

  // Join request: opens a user-controlled email draft; no email is stored or silently transmitted.
  const joinForm = document.querySelector('#join-form');
  if (joinForm) joinForm.addEventListener('submit', event => {
    event.preventDefault();
    const email = document.querySelector('#join-email')?.value.trim() || '';
    const consent = document.querySelector('#join-consent');
    if (!email || !consent?.checked) return;
    const subject = encodeURIComponent('Join the CLP learning community');
    const body = encodeURIComponent('Hello CLP,\n\nI would like to join the CLP learning community and receive occasional updates.\n\nMy email address: ' + email + '\n\nI consent to CLP receiving this email as my request to join.\n');
    const statusEl = document.querySelector('#join-status');
    if (statusEl) statusEl.textContent = 'Opening your email app with your request addressed to clpvriksha@gmail.com. Please review and send it there.';
    window.location.href = 'mailto:clpvriksha@gmail.com?subject=' + subject + '&body=' + body;
  });
  // Shared responsive navigation: one source of truth for the button and menu state.
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('#site-nav');
  const closeMenu = () => {
    if (!toggle || !nav) return;
    toggle.setAttribute('aria-expanded', 'false');
    nav.classList.remove('is-open');
  };
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      nav.classList.toggle('is-open', !open);
    });
    nav.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape') closeMenu();
    });
    document.addEventListener('click', event => {
      if (!nav.contains(event.target) && !toggle.contains(event.target)) closeMenu();
    });
  }

  // Learning-page topic filters.
  const tabs = [...document.querySelectorAll('.topic-tab')];
  const cards = [...document.querySelectorAll('.learning-card')];
  const status = document.querySelector('#filter-status');
  tabs.forEach(tab => tab.addEventListener('click', () => {
    const filter = tab.dataset.filter;
    tabs.forEach(item => {
      const active = item === tab;
      item.classList.toggle('is-active', active);
      item.setAttribute('aria-pressed', String(active));
    });
    let shown = 0;
    cards.forEach(card => {
      const visible = filter === 'all' || card.dataset.topic === filter;
      card.hidden = !visible;
      if (visible) shown++;
    });
    if (status) status.textContent = filter === 'all'
      ? 'Showing all ' + shown + ' learning paths.'
      : 'Showing ' + shown + ' ' + tab.textContent.trim().toLowerCase() + ' learning path' + (shown === 1 ? '' : 's') + '.';
  }));

  // Reveal content when it enters the viewport, with a safe fallback.
  const revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    }), { threshold: 0.12 });
    revealEls.forEach(el => observer.observe(el));
  } else {
    revealEls.forEach(el => el.classList.add('is-visible'));
  }

  // Community topic form prepares an email; it does not transmit data itself.
  const form = document.querySelector('#topic-form');
  if (form) {
    form.addEventListener('submit', event => {
      event.preventDefault();
      const topic = document.querySelector('#topic')?.value.trim() || '';
      const interest = document.querySelector('#interest')?.value || '';
      const subject = encodeURIComponent('CLP topic suggestion');
      const body = encodeURIComponent('Hello CLP,\n\nI would like CLP to explore:\n' + topic + '\n\nMy learning interest: ' + interest + '\n');
      const statusEl = document.querySelector('#form-status');
      if (statusEl) statusEl.textContent = 'Your email app will open with the suggestion prepared. No data is sent to CLP by this page.';
      window.location.href = 'mailto:?subject=' + subject + '&body=' + body;
    });
  }

  // Homepage featured-resource filters.
  const section = document.querySelector('#home-latest');
  if (section) {
    const homeTabs = [...section.querySelectorAll('[data-home-filter]')];
    const homeCards = [...section.querySelectorAll('[data-home-topic]')];
    const homeStatus = section.querySelector('#home-filter-status');
    const applyFilter = (filter, activeTab) => {
      homeTabs.forEach(tab => {
        const active = tab === activeTab;
        tab.classList.toggle('is-active', active);
        tab.setAttribute('aria-pressed', String(active));
      });
      let count = 0;
      homeCards.forEach(card => {
        const visible = filter === 'all' || card.dataset.homeTopic === filter;
        card.hidden = !visible;
        card.style.display = visible ? '' : 'none';
        card.setAttribute('aria-hidden', String(!visible));
        if (visible) count++;
      });
      if (homeStatus) {
        const label = activeTab ? activeTab.textContent.trim() : 'All';
        homeStatus.textContent = filter === 'all'
          ? 'Showing all ' + count + ' learning resources.'
          : 'Showing ' + count + ' ' + label + ' resource' + (count === 1 ? '' : 's') + '.';
      }
    };
    homeTabs.forEach(tab => tab.addEventListener('click', () => applyFilter(tab.dataset.homeFilter, tab)));
    applyFilter('all', homeTabs.find(tab => tab.dataset.homeFilter === 'all') || homeTabs[0]);
  }
});
