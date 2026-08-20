import { PRODUCTS_DATA, IMAGE_BG_MAP } from './products-data.js';

document.addEventListener('DOMContentLoaded', () => {
  initMobileMenu();
  initScrollReveal();
  initHeroSlider();
  initProductExplorer();
  initQuoteForm();
  initFeaturedSlider();
  initWhereToBuy();
});

/**
 * Mobile Menu Toggle Logic
 */
function initMobileMenu() {
  const header = document.querySelector('.main-header');
  const toggleBtn = document.querySelector('.mobile-menu-toggle');
  
  if (!toggleBtn || !header) return;
  
  toggleBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    header.classList.toggle('menu-open');
    if (header.classList.contains('menu-open')) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
    }
  });

  // Close menu when any link inside nav-menu-wrapper is clicked
  const menuLinks = document.querySelectorAll('.nav-menu-wrapper a');
  menuLinks.forEach(link => {
    link.addEventListener('click', () => {
      header.classList.remove('menu-open');
      document.body.style.overflow = '';
    });
  });

  // Close menu when clicking outside the menu wrapper
  document.addEventListener('click', (e) => {
    if (header.classList.contains('menu-open')) {
      const menuWrapper = document.querySelector('.nav-menu-wrapper');
      if (menuWrapper && !menuWrapper.contains(e.target) && !toggleBtn.contains(e.target)) {
        header.classList.remove('menu-open');
        document.body.style.overflow = '';
      }
    }
  });
}


/**
 * Hero Slider Logic
 */
function initHeroSlider() {
  const slides = document.querySelectorAll('.hero-slide');
  const dots = document.querySelectorAll('.hero-dots .dot');
  let currentSlide = 0;
  let slideInterval;

  if (slides.length === 0) return;

  const showSlide = (index) => {
    if (index >= slides.length) index = 0;
    if (index < 0) index = slides.length - 1;

    slides.forEach(slide => slide.classList.remove('active'));
    dots.forEach(dot => dot.classList.remove('active'));

    const activeSlide = slides[index];
    activeSlide.classList.add('active');
    if (dots[index]) dots[index].classList.add('active');
    currentSlide = index;

    // Performance Optimization: Lazy load video if it hasn't been loaded yet
    const video = activeSlide.querySelector('video');
    if (video) {
      const sources = video.querySelectorAll('source');
      let needsLoad = false;
      sources.forEach(source => {
        const dataSrc = source.getAttribute('data-src');
        if (dataSrc) {
          source.setAttribute('src', dataSrc);
          source.removeAttribute('data-src');
          needsLoad = true;
        }
      });
      if (needsLoad) {
        video.load();
      }
    }
  };

  const nextSlide = () => {
    showSlide(currentSlide + 1);
  };

  const startInterval = () => {
    clearInterval(slideInterval);
    slideInterval = setInterval(nextSlide, 5000);
  };

  dots.forEach(dot => {
    dot.addEventListener('click', (e) => {
      const slideIndex = parseInt(e.target.getAttribute('data-slide'), 10);
      showSlide(slideIndex);
      startInterval();
    });
  });

  startInterval();
}

/**
 * Interactive Product Catalog Modal Logic
 */
function initProductExplorer() {
  const modal = document.getElementById('product-modal');
  const modalCloseBtn = document.getElementById('modal-close-btn');
  const modalTitle = document.getElementById('modal-category-title');
  const modalGrid = document.getElementById('modal-products-grid');
  const viewCollectionLinks = document.querySelectorAll('.view-collection-link');
  const headerCategories = document.querySelectorAll('.nav-links .category-item');

  if (!modal || !modalGrid) return;

  // Render the category tabs
  const renderCategoryTabs = (activeCategoryId) => {
    const modalTabs = document.getElementById('modal-tabs');
    if (!modalTabs) return;

    modalTabs.style.display = 'flex';
    modalTabs.innerHTML = PRODUCTS_DATA.map(cat => `
      <button class="modal-tab ${cat.id === activeCategoryId ? 'active' : ''}" data-category-id="${cat.id}">
        ${cat.name}
      </button>
    `).join('');

    // Add event listeners to category tabs
    const tabs = modalTabs.querySelectorAll('.modal-tab');
    tabs.forEach(tab => {
      tab.addEventListener('click', () => {
        const categoryId = tab.getAttribute('data-category-id');
        if (categoryId === 'switches') {
          window.location.href = './switches.html';
          return;
        }
        if (categoryId === 'weatherproof') {
          window.location.href = './weatherproof.html';
          return;
        }
        if (categoryId === 'wiring_accessories') {
          window.location.href = './wiring-accessories.html';
          return;
        }
        if (categoryId === 'cable_management') {
          window.location.href = './cable-management.html';
          return;
        }
        if (categoryId === 'cable_termination') {
          window.location.href = './cable-termination.html';
          return;
        }
        if (categoryId === 'installation_boxes') {
          window.location.href = './installation-boxes.html';
          return;
        }
        if (categoryId === 'ventilation') {
          window.location.href = './air-ventilation.html';
          return;
        }
        if (categoryId === 'insect_killer') {
          window.location.href = './insect-killer.html';
          return;
        }
        setActiveCategory(categoryId);
      });
    });
  };

  // Render ranges list for a category containing multiple ranges
  const renderCategoryRanges = (categoryId, ranges) => {
    modalGrid.innerHTML = '';

    const rangesContainer = document.createElement('div');
    rangesContainer.className = 'modal-ranges-selection-grid';

    Object.entries(ranges).forEach(([rangeName, items]) => {
      const repItem = items[0];
      if (!repItem) return;

      const card = document.createElement('div');
      card.className = 'modal-range-selection-card';
      card.style.cursor = 'pointer';

      const bg = IMAGE_BG_MAP[repItem.img] || '#FFFFFF';

      card.innerHTML = `
        <div class="modal-card-img-box" style="background-color: ${bg};">
          <img src="${repItem.img}" alt="${rangeName}" loading="lazy">
          <span class="range-badge">Collection</span>
        </div>
        <div class="modal-card-body">
          <h4 class="modal-card-title">${rangeName}</h4>
          <p class="modal-card-desc">Explore the premium products in our ${rangeName} collection.</p>
          <span class="modal-explore-link">Explore Collection <span class="arrow">→</span></span>
        </div>
      `;

      card.addEventListener('click', () => {
        renderRangeProducts(categoryId, rangeName, items, true);
      });

      rangesContainer.appendChild(card);
    });

    modalGrid.appendChild(rangesContainer);
  };

  // Render products for a specific range inside the active category
  const renderRangeProducts = (categoryId, rangeName, items, showBackButton) => {
    modalGrid.innerHTML = '';

    if (showBackButton) {
      const backBtn = document.createElement('button');
      backBtn.className = 'modal-back-btn';
      backBtn.innerHTML = `&larr; Back to ${PRODUCTS_DATA.find(cat => cat.id === categoryId).name} Collections`;
      backBtn.addEventListener('click', () => {
        setActiveCategory(categoryId);
      });
      modalGrid.appendChild(backBtn);
    }

    const groupContainer = document.createElement('div');
    groupContainer.className = 'modal-range-group';

    const rangeTitle = document.createElement('h4');
    rangeTitle.className = 'modal-range-title';
    rangeTitle.textContent = rangeName;
    groupContainer.appendChild(rangeTitle);

    const rangeGrid = document.createElement('div');
    rangeGrid.className = 'modal-range-grid';

    items.forEach(item => {
      const card = document.createElement('div');
      card.className = 'modal-product-card';
      card.style.cursor = 'pointer';

      const specsList = item.specs.map(spec => `<li>${spec}</li>`).join('');
      const bg = IMAGE_BG_MAP[item.img] || '#FFFFFF';

      card.innerHTML = `
        <div class="modal-card-img-box" style="background-color: ${bg};">
          <img src="${item.img}" alt="${item.name}" loading="lazy">
          <span class="range-badge">${item.range || 'Standard'}</span>
        </div>
        <div class="modal-card-body">
          <h4 class="modal-card-title">${item.name}</h4>
          <p class="modal-card-desc">${item.desc}</p>
          <ul class="modal-card-specs">
            ${specsList}
          </ul>
          <button class="modal-inquiry-btn" data-category="${categoryId}" data-product="${item.name}">
            Inquire via Email
          </button>
        </div>
      `;

      // Set up click on card itself (briefing page)
      card.addEventListener('click', (e) => {
        if (e.target.classList.contains('modal-inquiry-btn') || e.target.closest('.modal-inquiry-btn')) {
          return;
        }
        const productUrl = `./product.html?category=${categoryId}&product=${encodeURIComponent(item.name)}`;
        window.open(productUrl, '_blank');
      });

      // Set up click on inquiry button only
      const inquiryBtn = card.querySelector('.modal-inquiry-btn');
      if (inquiryBtn) {
        inquiryBtn.addEventListener('click', (e) => {
          e.stopPropagation(); // prevent card click
          const productLink = window.location.origin + "/product.html?category=" + categoryId + "&product=" + encodeURIComponent(item.name);
          const subject = encodeURIComponent(`Product Inquiry: ${item.name}`);
          const body = encodeURIComponent(`Hello, I'm interested in the following product from Blit:\n\nProduct: ${item.name}\nRange: ${item.range || 'Standard'}\nLink: ${productLink}`);
          const mailtoUrl = `mailto:info@blit.com?subject=${subject}&body=${body}`;
          window.open(mailtoUrl, '_self');
          closeModal();
        });
      }

      rangeGrid.appendChild(card);
    });

    groupContainer.appendChild(rangeGrid);
    modalGrid.appendChild(groupContainer);
  };

  // Set the active category and sync states
  const setActiveCategory = (categoryId) => {
    const categoryData = PRODUCTS_DATA.find(cat => cat.id === categoryId);
    if (!categoryData) return;

    modalTitle.textContent = categoryData.name;

    // Update active tab styling
    const tabs = document.querySelectorAll('.modal-tab');
    tabs.forEach(tab => {
      if (tab.getAttribute('data-category-id') === categoryId) {
        tab.classList.add('active');
      } else {
        tab.classList.remove('active');
      }
    });

    // Sync header active link
    headerCategories.forEach(item => {
      const itemCat = item.getAttribute('data-category');
      if (itemCat === categoryId) {
        item.classList.add('active');
      } else {
        item.classList.remove('active');
      }
    });

    // Group items by range to see how many ranges we have
    const ranges = {};
    categoryData.items.forEach(item => {
      const rangeName = item.range || 'Standard';
      if (!ranges[rangeName]) {
        ranges[rangeName] = [];
      }
      ranges[rangeName].push(item);
    });

    const rangeNames = Object.keys(ranges);

    // If there is more than 1 range, show the Range Selection View.
    // Otherwise, directly show the products for the single range.
    if (rangeNames.length > 1) {
      renderCategoryRanges(categoryId, ranges);
    } else {
      renderRangeProducts(categoryId, rangeNames[0] || 'Standard', ranges[rangeNames[0] || 'Standard'] || categoryData.items, false);
    }
  };

  // Open modal and show products for selected category
  const openCategoryModal = (categoryId) => {
    if (categoryId === 'switches') {
      window.location.href = './switches.html';
      return;
    }
    if (categoryId === 'weatherproof') {
      window.location.href = './weatherproof.html';
      return;
    }
    if (categoryId === 'wiring_accessories') {
      window.location.href = './wiring-accessories.html';
      return;
    }
    if (categoryId === 'cable_management') {
      window.location.href = './cable-management.html';
      return;
    }
    if (categoryId === 'cable_termination') {
      window.location.href = './cable-termination.html';
      return;
    }
    if (categoryId === 'installation_boxes') {
      window.location.href = './installation-boxes.html';
      return;
    }
    if (categoryId === 'ventilation') {
      window.location.href = './air-ventilation.html';
      return;
    }
    if (categoryId === 'insect_killer') {
      window.location.href = './insect-killer.html';
      return;
    }
    // Show modal
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';

    // Render tabs and set active category
    renderCategoryTabs(categoryId);
    setActiveCategory(categoryId);
  };

  // Close modal
  const closeModal = () => {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  };

  if (modalCloseBtn) {
    modalCloseBtn.addEventListener('click', closeModal);
  }

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      closeModal();
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('active')) {
      closeModal();
    }
  });

  // Category cards view collection click
  viewCollectionLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const categoryId = link.getAttribute('data-category');
      openCategoryModal(categoryId);
    });
  });

  // Also support clicking anywhere on the category card itself
  document.querySelectorAll('.category-card').forEach(card => {
    card.addEventListener('click', (e) => {
      // Don't trigger if they clicked directly on the anchor, since that handles it
      if (e.target.tagName !== 'A' && !e.target.closest('a')) {
        const categoryId = card.getAttribute('data-category');
        openCategoryModal(categoryId);
      }
    });
  });

  // Sync header links
  headerCategories.forEach(item => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      const categoryId = item.getAttribute('data-category');
      
      // Update header indicators
      headerCategories.forEach(el => el.classList.remove('active'));
      item.classList.add('active');

      // Scroll to products and open modal
      const prodSec = document.getElementById('products');
      if (prodSec) {
        prodSec.scrollIntoView({ behavior: 'smooth' });
      }
      setTimeout(() => {
        openCategoryModal(categoryId);
      }, 500);
    });
  });
}

/**
 * Contact & Quote Form Handling
 */
function initQuoteForm() {
  const form = document.querySelector('.quote-form');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('client-name').value;
      const email = document.getElementById('client-email').value;
      const category = document.getElementById('client-needs').value;

      alert(`Thank you, ${name}! Your quote request for ${category.toUpperCase()} has been submitted. We will contact you at ${email} shortly.`);
      form.reset();
    });
  }
}

/**
 * Featured Switch Card Side Slider Logic
 */
function initFeaturedSlider() {
  const track = document.querySelector('.featured-slides-track');
  const slides = document.querySelectorAll('.featured-slide');
  const dots = document.querySelectorAll('.featured-dots .dot');

  if (!track || slides.length === 0) return;

  let currentSlide = 0;
  let autoSlideTimer;

  const goToSlide = (index) => {
    if (index < 0) index = slides.length - 1;
    if (index >= slides.length) index = 0;

    currentSlide = index;
    track.style.transform = `translateX(-${currentSlide * 100}%)`;

    dots.forEach((dot, idx) => {
      if (idx === currentSlide) {
        dot.classList.add('active');
      } else {
        dot.classList.remove('active');
      }
    });
  };

  const startAutoSlide = () => {
    clearInterval(autoSlideTimer);
    autoSlideTimer = setInterval(() => {
      goToSlide(currentSlide + 1);
    }, 4000);
  };

  dots.forEach((dot, idx) => {
    dot.addEventListener('click', () => {
      goToSlide(idx);
      startAutoSlide();
    });
  });

  startAutoSlide();
}

/**
 * Scroll Reveal Animations using Intersection Observer
 */
function initScrollReveal() {
  const revealElements = document.querySelectorAll('.reveal');
  if (revealElements.length === 0) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        observer.unobserve(entry.target); // Animate once
      }
    });
  }, {
    threshold: 0.05,
    rootMargin: '0px 0px -40px 0px' // triggers slightly before section enters the fold
  });

  revealElements.forEach(el => observer.observe(el));
}

/**
 * Legrand-Inspired Where to Buy: Interactive Store & Distributor Locator
 */
function initWhereToBuy() {
  const mapContainer = document.getElementById('where-to-buy-map');
  const cardsContainer = document.getElementById('wtb-cards-container');
  if (!mapContainer || !cardsContainer) return;

  // Comprehensive Distributor & Stockist Directory
  const DISTRIBUTORS_DATA = [
    {
      id: 'blit-deira-hub',
      name: 'BLIT Distribution Hub - Deira',
      category: 'distributor',
      categoryLabel: 'Regional Distributor',
      regionKey: 'dubai',
      regionName: 'Dubai, UAE',
      cityName: 'Deira / Al Sabkha',
      address: 'Shop 14-16, Al Nakheel Street, Deira Electrical Market, Dubai, UAE',
      phone: '+971 50 199 5589',
      whatsapp: '971501995589',
      email: 'info@blit.com',
      hours: 'Mon - Sat: 8:00 AM - 8:30 PM',
      lat: 25.2697,
      lng: 55.3095
    },
    {
      id: 'blit-alquoz-logistics',
      name: 'BLIT Central Logistics & Warehouse',
      category: 'distributor',
      categoryLabel: 'Regional Distributor',
      regionKey: 'dubai',
      regionName: 'Dubai, UAE',
      cityName: 'Al Quoz Industrial',
      address: 'Warehouse 12, Street 18B, Al Quoz Industrial Area 3, Dubai, UAE',
      phone: '+971 4 345 8820',
      whatsapp: '971501995589',
      email: 'logistics@blitelectric.com',
      hours: 'Mon - Fri: 8:00 AM - 6:00 PM',
      lat: 25.1325,
      lng: 55.2285
    },
    {
      id: 'apex-switchgear-bb',
      name: 'Apex Electrical Switchgears LLC',
      category: 'stockist',
      categoryLabel: 'Authorised Stockist',
      regionKey: 'dubai',
      regionName: 'Dubai, UAE',
      cityName: 'Business Bay',
      address: 'Showroom 4, Bay Square Building 07, Business Bay, Dubai, UAE',
      phone: '+971 4 228 9110',
      whatsapp: '97142289110',
      email: 'sales@apexswitchgears.ae',
      hours: 'Sat - Thu: 8:30 AM - 7:30 PM',
      lat: 25.1884,
      lng: 55.2798
    },
    {
      id: 'blit-experience-barsha',
      name: 'BLIT Flagship Specification Studio',
      category: 'showroom',
      categoryLabel: 'Flagship Experience Center',
      regionKey: 'dubai',
      regionName: 'Dubai, UAE',
      cityName: 'Al Barsha / SZR',
      address: 'Ground Floor, Al Barsha Heights, Near Dubai Internet City Metro, Dubai, UAE',
      phone: '+971 4 399 2211',
      whatsapp: '971501995589',
      email: 'showroom@blitelectric.com',
      hours: 'Mon - Sat: 9:00 AM - 9:00 PM',
      lat: 25.0975,
      lng: 55.1764
    },
    {
      id: 'gulf-electro-mussafah',
      name: 'Gulf Electro Supplies & Lighting LLC',
      category: 'stockist',
      categoryLabel: 'Authorised Stockist',
      regionKey: 'abudhabi',
      regionName: 'Abu Dhabi, UAE',
      cityName: 'Mussafah Industrial',
      address: 'Plot 44, Sector M-14, Mussafah Industrial Area, Abu Dhabi, UAE',
      phone: '+971 2 554 6780',
      whatsapp: '97125546780',
      email: 'abudhabi@gulfelectro.ae',
      hours: 'Sat - Thu: 8:00 AM - 7:00 PM',
      lat: 24.3468,
      lng: 54.5122
    },
    {
      id: 'alnaboodah-wholesale-ad',
      name: 'Al Naboodah Electrical Wholesale Hub',
      category: 'stockist',
      categoryLabel: 'Authorised Stockist',
      regionKey: 'abudhabi',
      regionName: 'Abu Dhabi, UAE',
      cityName: 'Al Danah / Electra St',
      address: 'Electra Street, Al Danah Zone 1, Abu Dhabi, UAE',
      phone: '+971 2 677 3344',
      whatsapp: '97126773344',
      email: 'orders@alnaboodah-elec.ae',
      hours: 'Sat - Thu: 8:00 AM - 8:00 PM',
      lat: 24.4920,
      lng: 54.3725
    },
    {
      id: 'emirates-power-sharjah',
      name: 'Emirates Power & Wiring Hardware LLC',
      category: 'stockist',
      categoryLabel: 'Authorised Stockist',
      regionKey: 'northern',
      regionName: 'Sharjah, UAE',
      cityName: 'Industrial Area 4',
      address: 'Industrial Area 4, Double Road, Sharjah, UAE',
      phone: '+971 6 533 1928',
      whatsapp: '97165331928',
      email: 'sharjah@emiratespower.ae',
      hours: 'Sat - Thu: 8:00 AM - 8:00 PM',
      lat: 25.3218,
      lng: 55.4026
    },
    {
      id: 'northern-elec-rak',
      name: 'Northern Emirates Electric Trade',
      category: 'stockist',
      categoryLabel: 'Authorised Stockist',
      regionKey: 'northern',
      regionName: 'Ras Al Khaimah, UAE',
      cityName: 'Al Nakheel',
      address: 'Al Muntasir Road, Al Nakheel, Ras Al Khaimah, UAE',
      phone: '+971 7 227 4410',
      whatsapp: '97172274410',
      email: 'rak@northernelec.ae',
      hours: 'Sat - Thu: 8:30 AM - 7:30 PM',
      lat: 25.7952,
      lng: 55.9754
    },
    {
      id: 'alfanar-riyadh',
      name: 'Al Fanar Electrical Supplies Co.',
      category: 'distributor',
      categoryLabel: 'Regional Distributor',
      regionKey: 'saudi',
      regionName: 'Riyadh, Saudi Arabia',
      cityName: 'Al Olaya District',
      address: 'King Fahd Road, Al Olaya Commercial District, Riyadh, Saudi Arabia',
      phone: '+966 11 465 9900',
      whatsapp: '966114659900',
      email: 'riyadh@alfanarelec.sa',
      hours: 'Sat - Thu: 8:00 AM - 6:00 PM',
      lat: 24.7136,
      lng: 46.6753
    },
    {
      id: 'jeddah-switchgear',
      name: 'Jeddah Modern Switchgear Trading',
      category: 'stockist',
      categoryLabel: 'Authorised Stockist',
      regionKey: 'saudi',
      regionName: 'Jeddah, Saudi Arabia',
      cityName: 'Al Andalus',
      address: 'Madinah Road, Al Andalus District, Jeddah, Saudi Arabia',
      phone: '+966 12 660 4422',
      whatsapp: '966126604422',
      email: 'jeddah@modernswitch.sa',
      hours: 'Sat - Thu: 8:30 AM - 7:00 PM',
      lat: 21.5433,
      lng: 39.1728
    },
    {
      id: 'qatar-switchgear-doha',
      name: 'Qatar Switchgear & Distribution Hub',
      category: 'distributor',
      categoryLabel: 'Regional Distributor',
      regionKey: 'international',
      regionName: 'Doha, Qatar',
      cityName: 'Salwa Industrial Area',
      address: 'Salwa Road, Gate 42, Industrial Area, Doha, Qatar',
      phone: '+974 4450 1199',
      whatsapp: '97444501199',
      email: 'doha@qatarswitchgear.qa',
      hours: 'Sat - Thu: 7:30 AM - 5:30 PM',
      lat: 25.2285,
      lng: 51.4682
    },
    {
      id: 'blit-uk-hub',
      name: 'BLIT UK Central Hub & Studio',
      category: 'showroom',
      categoryLabel: 'Flagship Experience Center',
      regionKey: 'international',
      regionName: 'London, United Kingdom',
      cityName: 'Central London',
      address: '45 Great Portland Street, Marylebone, London W1W 7NE, United Kingdom',
      phone: '+44 20 7946 0912',
      whatsapp: '442079460912',
      email: 'uk@blitelectric.com',
      hours: 'Mon - Fri: 9:00 AM - 6:00 PM',
      lat: 51.5186,
      lng: -0.1425
    }
  ];

  // Dynamic filter state
  let currentCategory = 'all';
  let currentRegion = 'all';
  let currentCity = 'all';
  let searchQuery = '';
  let activeDealerId = null;

  let leafletMap = null;
  let markerMap = new Map();

  // Initialize dropdown options
  const initDropdowns = () => {
    // 1. Regions
    const regionOptions = document.getElementById('wtb-region-options');
    if (regionOptions) {
      const regions = [
        { val: 'all', label: 'All States / Regions' },
        { val: 'dubai', label: 'Dubai (UAE)' },
        { val: 'abudhabi', label: 'Abu Dhabi (UAE)' },
        { val: 'northern', label: 'Sharjah & RAK (UAE)' },
        { val: 'saudi', label: 'Saudi Arabia (Riyadh & Jeddah)' },
        { val: 'international', label: 'Qatar & United Kingdom' }
      ];
      regionOptions.innerHTML = regions.map(r => `
        <li class="wtb-option-item ${r.val === currentRegion ? 'selected' : ''}" data-val="${r.val}">${r.label}</li>
      `).join('');
    }

    // Dropdown toggle triggers
    const triggerBoxes = document.querySelectorAll('.wtb-trigger-box');
    triggerBoxes.forEach(trigger => {
      trigger.addEventListener('click', (e) => {
        e.stopPropagation();
        if (trigger.classList.contains('is-disabled')) return;
        
        const list = trigger.nextElementSibling;
        const isActive = trigger.classList.contains('active');

        // Close other dropdowns
        document.querySelectorAll('.wtb-options-list').forEach(l => l.style.display = 'none');
        document.querySelectorAll('.wtb-trigger-box').forEach(t => t.classList.remove('active'));

        if (!isActive && list) {
          trigger.classList.add('active');
          list.style.display = 'block';
        }
      });
    });

    // Close dropdowns on document click
    document.addEventListener('click', () => {
      document.querySelectorAll('.wtb-options-list').forEach(l => l.style.display = 'none');
      document.querySelectorAll('.wtb-trigger-box').forEach(t => t.classList.remove('active'));
    });

    // Option selections
    // Category Option click
    document.querySelectorAll('#wtb-cat-options .wtb-option-item').forEach(opt => {
      opt.addEventListener('click', function(e) {
        e.stopPropagation();
        const val = this.getAttribute('data-val');
        currentCategory = val;
        document.getElementById('wtb-val-cat').value = val;
        document.getElementById('wtb-cat-label').textContent = this.textContent;
        document.querySelectorAll('#wtb-cat-options .wtb-option-item').forEach(o => o.classList.remove('selected'));
        this.classList.add('selected');
        document.getElementById('wtb-cat-options').style.display = 'none';
        document.getElementById('wtb-drop-cat').classList.remove('active');
        updateCityDropdown();
      });
    });

    // Region Option click
    document.addEventListener('click', (e) => {
      const opt = e.target.closest('#wtb-region-options .wtb-option-item');
      if (!opt) return;
      e.stopPropagation();
      const val = opt.getAttribute('data-val');
      currentRegion = val;
      document.getElementById('wtb-val-region').value = val;
      document.getElementById('wtb-region-label').textContent = opt.textContent;
      document.querySelectorAll('#wtb-region-options .wtb-option-item').forEach(o => o.classList.remove('selected'));
      opt.classList.add('selected');
      document.getElementById('wtb-region-options').style.display = 'none';
      document.getElementById('wtb-drop-region').classList.remove('active');
      
      // Update city dropdown
      updateCityDropdown();
    });

    // City Option click
    document.addEventListener('click', (e) => {
      const opt = e.target.closest('#wtb-city-options .wtb-option-item');
      if (!opt) return;
      e.stopPropagation();
      const val = opt.getAttribute('data-val');
      currentCity = val;
      document.getElementById('wtb-val-city').value = val;
      document.getElementById('wtb-city-label').textContent = opt.textContent;
      document.querySelectorAll('#wtb-city-options .wtb-option-item').forEach(o => o.classList.remove('selected'));
      opt.classList.add('selected');
      document.getElementById('wtb-city-options').style.display = 'none';
      document.getElementById('wtb-drop-city').classList.remove('active');
    });

    // Search button
    const btnSearch = document.getElementById('wtb-btn-search');
    if (btnSearch) {
      btnSearch.addEventListener('click', () => {
        applyFilters();
      });
    }

    // Clear button
    const btnClear = document.getElementById('wtb-btn-clear');
    if (btnClear) {
      btnClear.addEventListener('click', () => {
        resetAllFilters();
      });
    }

    // Search text input (live filtering)
    const searchInput = document.getElementById('wtb-search-input');
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        searchQuery = e.target.value.toLowerCase().trim();
        applyFilters(false);
      });
    }

    // Map quick filter pills
    const quickPills = document.querySelectorAll('#wtb-quick-filters .wtb-quick-pill');
    quickPills.forEach(pill => {
      pill.addEventListener('click', () => {
        quickPills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        const rKey = pill.getAttribute('data-region');
        currentRegion = rKey;
        
        // Update sidebar region label
        const rLabel = pill.textContent.split('(')[0].trim();
        document.getElementById('wtb-region-label').textContent = rKey === 'all' ? 'Select State / Region' : rLabel;
        document.getElementById('wtb-val-region').value = rKey;
        
        currentCity = 'all';
        document.getElementById('wtb-city-label').textContent = 'Select City / Area';
        document.getElementById('wtb-val-city').value = 'all';

        updateCityDropdown();
        applyFilters(true);
      });
    });
  };

  // Update dynamic city dropdown based on selected region
  const updateCityDropdown = () => {
    const dropCity = document.getElementById('wtb-drop-city');
    const cityOptions = document.getElementById('wtb-city-options');
    if (!dropCity || !cityOptions) return;

    if (currentRegion === 'all') {
      dropCity.classList.add('is-disabled');
      cityOptions.innerHTML = '';
      currentCity = 'all';
      document.getElementById('wtb-city-label').textContent = 'Select City / Area';
      return;
    }

    dropCity.classList.remove('is-disabled');
    
    // Find unique cities for this region
    const matchingDealers = DISTRIBUTORS_DATA.filter(d => d.regionKey === currentRegion);
    const cities = [{ val: 'all', label: 'All Cities in Region' }];
    matchingDealers.forEach(d => {
      if (!cities.some(c => c.val === d.cityName)) {
        cities.push({ val: d.cityName, label: d.cityName });
      }
    });

    cityOptions.innerHTML = cities.map(c => `
      <li class="wtb-option-item ${c.val === currentCity ? 'selected' : ''}" data-val="${c.val}">${c.label}</li>
    `).join('');
  };

  // Reset all filters
  const resetAllFilters = () => {
    currentCategory = 'all';
    currentRegion = 'all';
    currentCity = 'all';
    searchQuery = '';

    document.getElementById('wtb-val-cat').value = 'all';
    document.getElementById('wtb-cat-label').textContent = 'Select Category';

    document.getElementById('wtb-val-region').value = 'all';
    document.getElementById('wtb-region-label').textContent = 'Select State / Region';

    document.getElementById('wtb-val-city').value = 'all';
    document.getElementById('wtb-city-label').textContent = 'Select City / Area';

    document.getElementById('wtb-search-input').value = '';

    document.querySelectorAll('#wtb-quick-filters .wtb-quick-pill').forEach(p => {
      p.classList.toggle('active', p.getAttribute('data-region') === 'all');
    });

    updateCityDropdown();
    applyFilters(true);
  };

  // Filter computation
  const getFilteredDealers = () => {
    return DISTRIBUTORS_DATA.filter(dealer => {
      // Category filter
      if (currentCategory !== 'all' && dealer.category !== currentCategory) {
        return false;
      }
      // Region filter
      if (currentRegion !== 'all' && dealer.regionKey !== currentRegion) {
        return false;
      }
      // City filter
      if (currentCity !== 'all' && dealer.cityName !== currentCity) {
        return false;
      }
      // Text search
      if (searchQuery) {
        const fullText = `${dealer.name} ${dealer.address} ${dealer.regionName} ${dealer.cityName} ${dealer.categoryLabel}`.toLowerCase();
        if (!fullText.includes(searchQuery)) {
          return false;
        }
      }
      return true;
    });
  };

  // Render dealer cards in sidebar
  const renderDealerCards = (dealers) => {
    const resultsCountEl = document.getElementById('wtb-results-count');
    if (resultsCountEl) {
      resultsCountEl.textContent = `${dealers.length} Location${dealers.length === 1 ? '' : 's'} Found`;
    }

    if (dealers.length === 0) {
      cardsContainer.innerHTML = `
        <div class="wtb-empty-state">
          <svg viewBox="0 0 24 24" fill="none" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="8" y1="12" x2="16" y2="12"></line>
          </svg>
          <h4 style="font-size: 15px; color: #1A1A1A; margin-bottom: 6px; font-weight: 700;">No distributors found</h4>
          <p style="font-size: 13px; color: #777777; margin-bottom: 14px;">Try searching for another area or clear your filter criteria.</p>
          <button type="button" class="wtb-btn-clear" id="wtb-btn-reset-empty" style="padding: 8px 16px; font-size: 12px;">Reset All Filters</button>
        </div>
      `;
      const btnReset = document.getElementById('wtb-btn-reset-empty');
      if (btnReset) btnReset.addEventListener('click', resetAllFilters);
      return;
    }

    cardsContainer.innerHTML = dealers.map(dealer => `
      <div class="wtb-card ${activeDealerId === dealer.id ? 'highlight-active' : ''}" id="wtb-card-${dealer.id}" data-dealer-id="${dealer.id}">
        <div class="wtb-card-top">
          <h4 class="wtb-card-title">${dealer.name}</h4>
          <span class="wtb-cat-pill ${dealer.category}">${dealer.categoryLabel}</span>
        </div>
        <p class="wtb-card-address">${dealer.address}</p>
        
        <div class="wtb-card-info-row">
          <svg viewBox="0 0 24 24" fill="none" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
            <circle cx="12" cy="10" r="3"></circle>
          </svg>
          <span><strong>${dealer.regionName}</strong> (${dealer.cityName})</span>
        </div>

        <div class="wtb-card-info-row">
          <svg viewBox="0 0 24 24" fill="none" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
          </svg>
          <span>${dealer.phone}</span>
        </div>

        <div class="wtb-card-actions">
          <a href="tel:${dealer.phone.replace(/\s+/g, '')}" class="wtb-card-btn wtb-card-btn-call" onclick="event.stopPropagation();">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
            <span>Call</span>
          </a>
          <a href="https://wa.me/${dealer.whatsapp}?text=${encodeURIComponent('Hello BLIT, I am inquiring about genuine products at ' + dealer.name)}" target="_blank" rel="noopener" class="wtb-card-btn wtb-card-btn-whatsapp" onclick="event.stopPropagation();">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.312.045-.634.07-1.745-.39-1.418-.588-2.316-2.029-2.387-2.123-.07-.095-.572-.76-.572-1.45 0-.69.362-1.03.49-1.173.129-.144.281-.18.375-.18.094 0 .188.001.271.006.087.004.204-.033.319.244.12.287.41 1.002.446 1.074.036.072.06.156.012.251-.048.096-.072.156-.144.24-.072.084-.153.188-.218.252-.072.072-.148.15-.064.294.084.144.373.615.8 1.003.549.498 1.012.653 1.156.725.144.072.228.06.312-.036.084-.096.362-.42.458-.564.096-.144.192-.12.324-.072.132.048.837.394.981.466.144.072.24.108.276.168.036.06.036.348-.108.753z"/></svg>
            <span>WhatsApp</span>
          </a>
          <button type="button" class="wtb-card-btn wtb-card-btn-map">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"></polygon><line x1="8" y1="2" x2="8" y2="18"></line><line x1="16" y1="6" x2="16" y2="22"></line></svg>
            <span>View Map</span>
          </button>
        </div>
      </div>
    `).join('');

    // Attach card click handlers
    document.querySelectorAll('.wtb-card').forEach(card => {
      card.addEventListener('click', () => {
        const dealerId = card.getAttribute('data-dealer-id');
        selectDealer(dealerId, true);
      });
    });
  };

  // Helper: Create Leaflet marker icon
  const createMarkerIcon = (isActive = false) => {
    if (typeof L === 'undefined') return null;
    const color = isActive ? '#8A0B0E' : '#C10914';
    return L.divIcon({
      className: 'custom-blit-marker-wrap',
      html: `
        <div class="custom-blit-marker ${isActive ? 'is-active' : ''}" style="position: relative; width: 32px; height: 38px;">
          ${isActive ? '<div class="blink-ring" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);"></div>' : ''}
          <svg class="custom-marker-pin" viewBox="0 0 32 40" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: 100%; filter: drop-shadow(0 4px 8px rgba(138, 11, 14, 0.4));">
            <path d="M16 0C7.163 0 0 7.163 0 16c0 13 16 24 16 24s16-11 16-24C32 7.163 24.837 0 16 0z" fill="${color}"/>
            <circle cx="16" cy="15" r="7" fill="#FFFFFF"/>
            <path d="M13 15h6M16 12v6" stroke="${color}" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </div>
      `,
      iconSize: [32, 40],
      iconAnchor: [16, 38],
      popupAnchor: [0, -36]
    });
  };

  // Select dealer and synchronize map + sidebar
  const selectDealer = (dealerId, panMap = true) => {
    activeDealerId = dealerId;
    const dealer = DISTRIBUTORS_DATA.find(d => d.id === dealerId);
    if (!dealer) return;

    // Highlight card
    document.querySelectorAll('.wtb-card').forEach(c => {
      c.classList.toggle('highlight-active', c.getAttribute('data-dealer-id') === dealerId);
    });

    const activeCard = document.getElementById(`wtb-card-${dealerId}`);
    if (activeCard) {
      activeCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    // Update marker icons on map
    markerMap.forEach((marker, dId) => {
      if (marker && marker.setIcon) {
        marker.setIcon(createMarkerIcon(dId === dealerId));
      }
    });

    // Fly to coordinates & open popup
    if (leafletMap && panMap) {
      leafletMap.flyTo([dealer.lat, dealer.lng], 14, {
        duration: 0.8,
        easeLinearity: 0.25
      });
      const marker = markerMap.get(dealerId);
      if (marker) {
        setTimeout(() => {
          marker.openPopup();
        }, 400);
      }
    }
  };

  // Update map markers according to filtered list
  const updateMapMarkers = (dealers, fitBounds = true) => {
    if (!leafletMap || typeof L === 'undefined') return;

    // Clear existing markers
    markerMap.forEach(marker => {
      leafletMap.removeLayer(marker);
    });
    markerMap.clear();

    if (dealers.length === 0) return;

    const bounds = L.latLngBounds();

    dealers.forEach(dealer => {
      const isSelected = activeDealerId === dealer.id;
      const marker = L.marker([dealer.lat, dealer.lng], {
        icon: createMarkerIcon(isSelected),
        title: dealer.name
      }).addTo(leafletMap);

      // Popup Content
      const popupHtml = `
        <div class="wtb-popup-body">
          <div style="margin-bottom: 6px;">
            <span class="wtb-cat-pill ${dealer.category}">${dealer.categoryLabel}</span>
          </div>
          <h4 class="wtb-popup-title">${dealer.name}</h4>
          <div class="wtb-popup-addr">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#8A0B0E" stroke-width="2.2" style="flex-shrink:0; margin-top:2px;"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
            <span>${dealer.address}</span>
          </div>
          <div class="wtb-popup-phone">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#8A0B0E" stroke-width="2.2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
            <span>${dealer.phone}</span>
          </div>
          <div class="wtb-popup-actions">
            <a href="tel:${dealer.phone.replace(/\s+/g, '')}" class="wtb-popup-btn wtb-popup-btn-call">CALL NOW</a>
            <a href="https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(dealer.name + ' ' + dealer.address)}" target="_blank" rel="noopener" class="wtb-popup-btn wtb-popup-btn-dir">DIRECTIONS</a>
          </div>
        </div>
      `;

      marker.bindPopup(popupHtml, { maxWidth: 300, minWidth: 260 });

      // Marker click event
      marker.on('click', () => {
        selectDealer(dealer.id, false);
      });

      markerMap.set(dealer.id, marker);
      bounds.extend([dealer.lat, dealer.lng]);
    });

    if (fitBounds && dealers.length > 0) {
      if (dealers.length === 1) {
        leafletMap.setView([dealers[0].lat, dealers[0].lng], 13);
      } else {
        leafletMap.fitBounds(bounds, { padding: [40, 40], maxZoom: 12 });
      }
    }
  };

  // Apply active filters to UI & Map
  const applyFilters = (fitMap = true) => {
    const filtered = getFilteredDealers();
    renderDealerCards(filtered);
    updateMapMarkers(filtered, fitMap);
  };

  // Initialize Leaflet Map
  const initMap = () => {
    if (typeof L === 'undefined') {
      setTimeout(initMap, 150);
      return;
    }

    try {
      leafletMap = L.map('where-to-buy-map', {
        scrollWheelZoom: false,
        zoomControl: true
      }).setView([25.2048, 55.2708], 10);

      // Add CartoDB Positron / Voyager high-performance tile layer
      L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="https://carto.com/attributions">CARTO</a>',
        subdomains: 'abcd',
        maxZoom: 19
      }).addTo(leafletMap);

      // Invalidate size when section comes into view or window resizes
      window.addEventListener('resize', () => {
        if (leafletMap) leafletMap.invalidateSize();
      });

      // Initial populate
      applyFilters(true);
    } catch (err) {
      console.warn('Map initialization:', err);
    }
  };

  // Modal Controllers
  const distModal = document.getElementById('distributor-modal');
  const distModalClose = document.getElementById('distributor-modal-close');
  const partnerModal = document.getElementById('partner-modal');
  const partnerModalClose = document.getElementById('partner-modal-close');

  const openDistributorModal = (e) => {
    if (e && typeof e.preventDefault === 'function') e.preventDefault();
    if (!distModal) return;
    distModal.classList.add('active');
    document.body.style.overflow = 'hidden';
    setTimeout(() => {
      if (leafletMap) {
        leafletMap.invalidateSize();
        applyFilters(true);
      }
    }, 200);
  };

  const closeDistributorModal = () => {
    if (!distModal) return;
    distModal.classList.remove('active');
    document.body.style.overflow = '';
  };

  const openPartnerModal = (e) => {
    if (e && typeof e.preventDefault === 'function') e.preventDefault();
    if (!partnerModal) return;
    partnerModal.classList.add('active');
    document.body.style.overflow = 'hidden';
  };

  const closePartnerModal = () => {
    if (!partnerModal) return;
    partnerModal.classList.remove('active');
    document.body.style.overflow = '';
  };

  // Bind trigger buttons & links for distributor locator modal
  document.querySelectorAll('.open-distributor-modal, a[href*="#distributor"], .quote-btn').forEach(btn => {
    btn.addEventListener('click', openDistributorModal);
  });

  if (distModalClose) {
    distModalClose.addEventListener('click', closeDistributorModal);
  }

  if (distModal) {
    distModal.addEventListener('click', (e) => {
      if (e.target === distModal) closeDistributorModal();
    });
  }

  // Bind trigger buttons & links for become distributor modal
  document.querySelectorAll('.open-partner-modal, a[href*="#become-distributor"]').forEach(btn => {
    btn.addEventListener('click', openPartnerModal);
  });

  if (partnerModalClose) {
    partnerModalClose.addEventListener('click', closePartnerModal);
  }

  if (partnerModal) {
    partnerModal.addEventListener('click', (e) => {
      if (e.target === partnerModal) closePartnerModal();
    });
  }

  // Global Escape key dismiss
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeDistributorModal();
      closePartnerModal();
    }
  });

  // Handle URL hash on load
  if (window.location.hash === '#distributor') {
    setTimeout(openDistributorModal, 400);
  } else if (window.location.hash === '#become-distributor') {
    setTimeout(openPartnerModal, 400);
  }

  // Run initialization
  initDropdowns();
  initMap();
}

