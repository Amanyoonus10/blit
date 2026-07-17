import { PRODUCTS_DATA, IMAGE_BG_MAP } from './products-data.js';

document.addEventListener('DOMContentLoaded', () => {
  initMobileMenu();
  initScrollReveal();
  initHeroSlider();
  initProductExplorer();
  initQuoteForm();
  initFeaturedSlider();
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

  // Close menu when a navigation category link is clicked
  const categoryItems = document.querySelectorAll('.nav-menu-wrapper .category-item');
  categoryItems.forEach(item => {
    item.addEventListener('click', () => {
      header.classList.remove('menu-open');
      document.body.style.overflow = '';
    });
  });

  // Close menu when quote button is clicked
  const quoteBtn = document.querySelector('.nav-menu-wrapper .quote-btn');
  if (quoteBtn) {
    quoteBtn.addEventListener('click', () => {
      header.classList.remove('menu-open');
      document.body.style.overflow = '';
    });
  }

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

    slides[index].classList.add('active');
    if (dots[index]) dots[index].classList.add('active');
    currentSlide = index;
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

  // Open modal and show products for selected category
  const openCategoryModal = (categoryId) => {
    const categoryData = PRODUCTS_DATA.find(cat => cat.id === categoryId);
    if (!categoryData) return;

    modalTitle.textContent = categoryData.name;
    modalGrid.innerHTML = '';

    categoryData.items.forEach((item, idx) => {
      const card = document.createElement('div');
      card.className = 'modal-product-card';
      card.style.cursor = 'pointer';

      const specsList = item.specs.map(spec => `<li>${spec}</li>`).join('');
      const bg = IMAGE_BG_MAP[item.img] || '#FFFFFF';

      card.innerHTML = `
        <div class="modal-card-img-box" style="background-color: ${bg};">
          <img src="${item.img}" alt="${item.name}" loading="lazy">
          <span class="range-badge">${item.range}</span>
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
        // If they click the button, don't trigger the card click
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
          const body = encodeURIComponent(`Hello, I'm interested in the following product from Blit:\n\nProduct: ${item.name}\nRange: ${item.range}\nLink: ${productLink}`);
          const mailtoUrl = `mailto:info@blit.com?subject=${subject}&body=${body}`;
          window.open(mailtoUrl, '_self');
          closeModal();
        });
      }

      modalGrid.appendChild(card);
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

    // Show modal
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
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

  // Pre-fill Quote Form logic
  const triggerInquiry = (categoryVal, productVal) => {
    const quoteFormSelect = document.getElementById('client-needs');
    const quoteFormTextarea = document.getElementById('client-message');
    const quoteSection = document.getElementById('quote');

    if (quoteFormSelect) {
      let selectVal = 'switches';
      if (categoryVal === 'weatherproof') selectVal = 'weatherproof';
      else if (categoryVal === 'wiring_accessories') selectVal = 'wiring_accessories';
      else if (categoryVal === 'cable_management') selectVal = 'cable_management';
      else if (categoryVal === 'cable_termination') selectVal = 'cable_termination';
      else if (categoryVal === 'industrial_plug_socket') selectVal = 'industrial_plug_socket';
      else if (categoryVal === 'installation_boxes') selectVal = 'installation_boxes';

      quoteFormSelect.value = selectVal;
    }

    if (quoteFormTextarea) {
      quoteFormTextarea.value = `I am interested in requesting a quote for: ${productVal}.\n\nPlease provide specifications, pricing, and minimum order quantity.`;
    }

    if (quoteSection) {
      quoteSection.scrollIntoView({ behavior: 'smooth' });
      const quoteBox = quoteSection.querySelector('.quote-box');
      if (quoteBox) {
        quoteBox.classList.add('pulse-highlight');
        setTimeout(() => quoteBox.classList.remove('pulse-highlight'), 1500);
      }
    }
  };
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
