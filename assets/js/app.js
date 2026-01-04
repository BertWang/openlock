/* =========================================
   app.js - 核心 JavaScript 功能
   Bootstrap 5 + 自訂邏輯
   ========================================= */

(function() {
  'use strict';

  // ===== 配置 =====
  const CONFIG = {
    storageKey: 'openlock-skin',
    defaultSkin: 'base',
    validSkins: ['base', 'mid', 'high'],
    apiEndpoint: '/api',  // 如需表單提交
  };

  // ===== Skin 切換系統 =====

  /**
   * 初始化 Skin 切換
   */
  function initSkinSwitcher() {
    // 讀取 localStorage 或使用預設值
    const savedSkin = localStorage.getItem(CONFIG.storageKey) || CONFIG.defaultSkin;
    applySkin(savedSkin);

    // 綁定所有 skin selector
    document.querySelectorAll('[id*="skinSelector"], [data-skin-selector]').forEach(selector => {
      selector.value = savedSkin;
      selector.addEventListener('change', (e) => {
        applySkin(e.target.value);
        updateAllSelectors(e.target.value);
      });
    });

    // 支援 URL 參數 ?skin=high
    const params = new URLSearchParams(window.location.search);
    const urlSkin = params.get('skin');
    if (urlSkin && CONFIG.validSkins.includes(urlSkin)) {
      applySkin(urlSkin);
      updateAllSelectors(urlSkin);
    }
  }

  /**
   * 應用 Skin 到頁面
   * @param {string} skin - skin 名稱
   */
  function applySkin(skin) {
    if (!CONFIG.validSkins.includes(skin)) {
      skin = CONFIG.defaultSkin;
    }

    document.documentElement.setAttribute('data-skin', skin);
    localStorage.setItem(CONFIG.storageKey, skin);

    // 觸發自訂事件
    window.dispatchEvent(new CustomEvent('skin-changed', { detail: { skin } }));

    console.log(`✓ Skin applied: ${skin}`);
  }

  /**
   * 更新所有 skin selector 的值
   * @param {string} skin - skin 名稱
   */
  function updateAllSelectors(skin) {
    document.querySelectorAll('[id*="skinSelector"], [data-skin-selector]').forEach(selector => {
      if (selector.value !== skin) {
        selector.value = skin;
      }
    });
  }

  /**
   * 獲取當前 Skin
   */
  function getCurrentSkin() {
    return document.documentElement.getAttribute('data-skin') || CONFIG.defaultSkin;
  }

  // ===== Offcanvas 自動關閉 =====

  /**
   * 初始化 Offcanvas（漢堡菜單）
   */
  function initOffcanvas() {
    const offcanvasElement = document.querySelector('[id*="offcanvas"]');
    if (!offcanvasElement) return;

    const bsOffcanvas = new bootstrap.Offcanvas(offcanvasElement);

    // 點選導覽連結後自動關閉
    offcanvasElement.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        // 排除外部連結（如 LINE、電話等）
        const href = link.getAttribute('href');
        if (href && href.startsWith('/') || href.startsWith('#')) {
          bsOffcanvas.hide();
        }
      });
    });

    // ESC 鍵關閉
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        bsOffcanvas.hide();
      }
    });
  }

  // ===== CTA 追蹤 =====

  /**
   * 初始化 CTA 點擊追蹤
   */
  function initCTATracking() {
    // 撥號按鈕
    document.querySelectorAll('[href^="tel:"], .btn-call').forEach(link => {
      link.addEventListener('click', () => {
        trackEvent('call_cta', 'clicked');
      });
    });

    // LINE 按鈕
    document.querySelectorAll('[href*="line"], .btn-line').forEach(link => {
      link.addEventListener('click', () => {
        trackEvent('line_cta', 'clicked');
      });
    });

    // 固定 CTA Bar 按鈕
    document.querySelectorAll('.cta-bar-fixed a').forEach(link => {
      link.addEventListener('click', () => {
        const type = link.classList.contains('btn-call') ? 'call' : 'line';
        trackEvent(`cta_bar_${type}`, 'clicked');
      });
    });
  }

  /**
   * 追蹤事件（GA / 自訂追蹤）
   * @param {string} event - 事件名稱
   * @param {string} action - 動作名稱
   */
  function trackEvent(event, action) {
    // Google Analytics（如有設定）
    if (window.gtag) {
      gtag('event', event, {
        'event_category': 'engagement',
        'event_label': action,
        'value': 1
      });
    }

    // 控制台輸出（開發用）
    console.log(`📊 Event: ${event} | Action: ${action}`);
  }

  // ===== 平滑滾動 =====

  /**
   * 初始化平滑滾動
   */
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href === '#') return;

        e.preventDefault();
        const target = document.querySelector(href);

        if (target) {
          target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });

          // 追蹤錨點點擊
          trackEvent('anchor_click', href);
        }
      });
    });
  }

  // ===== 表單提交 =====

  /**
   * 初始化聯繫表單
   */
  function initContactForm() {
    const form = document.querySelector('[id*="contactForm"], .contact-form');
    if (!form) return;

    form.addEventListener('submit', async (e) => {
      e.preventDefault();

      const formData = new FormData(form);
      const data = Object.fromEntries(formData);

      try {
        // 發送到後端（示例）
        const response = await fetch(CONFIG.apiEndpoint + '/contact', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(data)
        });

        if (response.ok) {
          trackEvent('form_submit', 'success');
          form.reset();
          alert('感謝您的查詢！我們會盡快回復。');
        } else {
          trackEvent('form_submit', 'error');
          alert('提交失敗，請重試。');
        }
      } catch (error) {
        console.error('表單提交錯誤:', error);
        trackEvent('form_submit', 'error');
        alert('提交出錯，請檢查網路連線。');
      }
    });
  }

  // ===== 頁面檢測 =====

  /**
   * 偵測目前頁面類型
   */
  function detectPageType() {
    const path = window.location.pathname;

    if (path === '/' || path.includes('index')) return 'home';
    if (path.includes('services')) return 'service';
    if (path.includes('area-')) return 'area';
    if (path.includes('catalog')) return 'catalog';
    if (path.includes('lock-model')) return 'model';
    if (path.includes('reviews')) return 'reviews';
    if (path.includes('faq')) return 'faq';
    if (path.includes('contact')) return 'contact';

    return 'unknown';
  }

  // ===== 主初始化 =====

  /**
   * 在 DOM 準備就緒時初始化所有功能
   */
  function init() {
    console.log('🔐 強匠鎖店 App 初始化中...');

    // 基礎初始化
    initSkinSwitcher();
    initOffcanvas();
    initCTATracking();
    initSmoothScroll();
    initContactForm();

    // 根據頁面類型執行額外邏輯
    const pageType = detectPageType();
    console.log(`📄 頁面類型: ${pageType}`);

    // 特定頁面的邏輯可以在這裡添加
    switch (pageType) {
      case 'home':
        // 首頁特定邏輯
        break;
      case 'catalog':
        // 型錄篩選邏輯
        initCatalogFilter();
        break;
      case 'service':
        // 服務頁邏輯
        break;
    }

    console.log('✓ App 初始化完成');
  }

  // ===== 型錄篩選（示例） =====

  /**
   * 初始化型錄篩選
   */
  function initCatalogFilter() {
    const filterButtons = document.querySelectorAll('[data-filter]');
    const products = document.querySelectorAll('[data-category]');

    filterButtons.forEach(button => {
      button.addEventListener('click', () => {
        const filter = button.getAttribute('data-filter');

        // 更新按鈕狀態
        filterButtons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');

        // 篩選產品
        products.forEach(product => {
          if (filter === 'all' || product.getAttribute('data-category') === filter) {
            product.style.display = 'block';
          } else {
            product.style.display = 'none';
          }
        });

        trackEvent('catalog_filter', filter);
      });
    });
  }

  // ===== 公開 API =====

  window.OpenLock = {
    applySkin: applySkin,
    getCurrentSkin: getCurrentSkin,
    trackEvent: trackEvent,
    detectPageType: detectPageType
  };

  // ===== 啟動 =====

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();

// ===== Bootstrap 5 提示（Tooltips 和 Popovers） =====

document.addEventListener('DOMContentLoaded', function() {
  // 初始化 Bootstrap Tooltip
  const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });

  // 初始化 Bootstrap Popover
  const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
  popoverTriggerList.map(function (popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl);
  });
});
