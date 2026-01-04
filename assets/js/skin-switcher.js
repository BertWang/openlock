/* =========================================
   Skin Switcher - JavaScript
   Manages data-skin attribute switching
   with localStorage persistence
   ========================================= */

(function() {
  'use strict';

  // Configuration
  const STORAGE_KEY = 'openlock-skin';
  const DEFAULT_SKIN = 'base';
  const AVAILABLE_SKINS = ['base', 'mid', 'high'];

  /**
   * Initialize skin switcher
   */
  function init() {
    // Get current skin from localStorage or use default
    const savedSkin = localStorage.getItem(STORAGE_KEY) || DEFAULT_SKIN;
    
    // Apply saved skin
    applySkin(savedSkin);
    
    // Find all skin selectors and bind events
    const selectors = document.querySelectorAll('#skinSelector, [data-skin-selector]');
    selectors.forEach(selector => {
      // Set current value
      selector.value = savedSkin;
      
      // Bind change event
      selector.addEventListener('change', (e) => {
        const newSkin = e.target.value;
        applySkin(newSkin);
        updateAllSelectors(newSkin);
      });
    });

    // Also handle direct clicks on skin buttons (if any)
    document.querySelectorAll('[data-skin-button]').forEach(button => {
      button.addEventListener('click', (e) => {
        const newSkin = e.target.getAttribute('data-skin-button');
        applySkin(newSkin);
        updateAllSelectors(newSkin);
      });
    });
  }

  /**
   * Apply skin to the document
   * @param {string} skin - Skin name (base, mid, high)
   */
  function applySkin(skin) {
    // Validate skin
    if (!AVAILABLE_SKINS.includes(skin)) {
      console.warn(`Invalid skin: ${skin}. Using default: ${DEFAULT_SKIN}`);
      skin = DEFAULT_SKIN;
    }

    // Get root element
    const htmlElement = document.documentElement;

    // Apply skin attribute
    htmlElement.setAttribute('data-skin', skin);

    // Save to localStorage
    localStorage.setItem(STORAGE_KEY, skin);

    // Dispatch custom event for other scripts to listen
    window.dispatchEvent(new CustomEvent('skin-changed', { 
      detail: { skin: skin } 
    }));

    // Log for debugging
    console.log(`Skin changed to: ${skin}`);
  }

  /**
   * Update all skin selector elements
   * @param {string} skin - Current skin
   */
  function updateAllSelectors(skin) {
    const selectors = document.querySelectorAll('#skinSelector, [data-skin-selector]');
    selectors.forEach(selector => {
      if (selector.value !== skin) {
        selector.value = skin;
      }
    });
  }

  /**
   * Get current skin
   * @returns {string} Current skin name
   */
  function getCurrentSkin() {
    return document.documentElement.getAttribute('data-skin') || DEFAULT_SKIN;
  }

  /**
   * Reset to default skin
   */
  function resetSkin() {
    applySkin(DEFAULT_SKIN);
    updateAllSelectors(DEFAULT_SKIN);
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Expose API globally for manual control
  window.SkinSwitcher = {
    applySkin: applySkin,
    getCurrentSkin: getCurrentSkin,
    resetSkin: resetSkin,
    AVAILABLE_SKINS: AVAILABLE_SKINS
  };

})();

/* =========================================
   Utility: Query Parameter Skin Selection
   Allows ?skin=high in URL
   ========================================= */

(function() {
  'use strict';

  // Check URL query parameters
  function checkQueryParams() {
    const params = new URLSearchParams(window.location.search);
    const querySkin = params.get('skin');
    
    if (querySkin && ['base', 'mid', 'high'].includes(querySkin)) {
      window.SkinSwitcher.applySkin(querySkin);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', checkQueryParams);
  } else {
    checkQueryParams();
  }
})();

/* =========================================
   Mobile Menu Closer (Bootstrap Navbar)
   ========================================= */

(function() {
  'use strict';

  // Close mobile menu when clicking on a link
  document.querySelectorAll('.navbar-collapse a').forEach(link => {
    link.addEventListener('click', function() {
      const navbarCollapse = document.querySelector('.navbar-collapse');
      if (navbarCollapse.classList.contains('show')) {
        const bsCollapse = new bootstrap.Collapse(navbarCollapse, {
          toggle: false
        });
        bsCollapse.hide();
      }
    });
  });
})();

/* =========================================
   Smooth Scroll for Anchor Links
   ========================================= */

(function() {
  'use strict';

  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      
      // Skip if it's just "#"
      if (href === '#') return;
      
      e.preventDefault();
      const target = document.querySelector(href);
      
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
})();
