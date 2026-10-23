(() => {
  'use strict';

  const CONSENT_KEY = 'clp-analytics-consent';
  const consentPanel = document.getElementById('analytics-consent');
  const acceptButton = document.getElementById('analytics-accept');
  const rejectButton = document.getElementById('analytics-reject');
  const preferencesButton = document.getElementById('analytics-preferences');
  if (!consentPanel || !acceptButton || !rejectButton || !preferencesButton) return;

  const analyticsEnabled = consentPanel.dataset.analyticsEnabled === 'true';
  const containerId = consentPanel.dataset.gtmId || '';
  const readChoice = () => {
    try {
      const value = localStorage.getItem(CONSENT_KEY);
      return value === 'accepted' || value === 'rejected' ? value : null;
    } catch (_) {
      return null;
    }
  };
  const saveChoice = value => {
    try {
      localStorage.setItem(CONSENT_KEY, value);
      return true;
    } catch (_) {
      return false;
    }
  };
  const setPanel = (visible) => {
    consentPanel.hidden = !visible;
    preferencesButton.setAttribute('aria-expanded', String(visible));
    preferencesButton.hidden = visible;
    if (visible) acceptButton.focus();
  };

  const initialiseDataLayer = () => {
    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
    window.gtag('consent', 'default', {
      analytics_storage: 'granted',
      ad_storage: 'denied',
      ad_user_data: 'denied',
      ad_personalization: 'denied',
      functionality_storage: 'denied',
      personalization_storage: 'denied',
      security_storage: 'granted'
    });
  };

  const loadContainer = () => {
    if (!analyticsEnabled || !/^GTM-[A-Z0-9]+$/i.test(containerId)) return;
    if (document.querySelector('script[data-clp-gtm="true"]')) return;
    initialiseDataLayer();
    window.dataLayer.push({ 'gtm.start': Date.now(), event: 'gtm.js' });
    const script = document.createElement('script');
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtm.js?id=' + encodeURIComponent(containerId);
    script.dataset.clpGtm = 'true';
    script.onerror = () => {
      script.remove();
      console.warn('CLP analytics container could not be loaded.');
    };
    document.head.appendChild(script);
  };

  const choice = readChoice();
  if (choice === 'accepted') loadContainer();
  if (!choice) setPanel(true);
  else setPanel(false);

  acceptButton.addEventListener('click', () => {
    saveChoice('accepted');
    setPanel(false);
    loadContainer();
  });

  rejectButton.addEventListener('click', () => {
    saveChoice('rejected');
    if (typeof window.gtag === 'function') {
      window.gtag('consent', 'update', {
        analytics_storage: 'denied',
        ad_storage: 'denied',
        ad_user_data: 'denied',
        ad_personalization: 'denied'
      });
    }
    setPanel(false);
    // Reload so a previously loaded container cannot continue handling new UI events.
    if (analyticsEnabled && document.querySelector('script[data-clp-gtm="true"]')) window.location.reload();
  });

  preferencesButton.addEventListener('click', () => setPanel(true));
})();
