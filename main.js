// Blit Landing Page Interactions

document.addEventListener('DOMContentLoaded', () => {
  initHeroSlider();
  initCategoryFilter();
  initQuoteForm();
  initFeaturedSlider();
});

/**
 * Hero Slider Logic
 */
function initHeroSlider() {
  const slides = document.querySelectorAll('.hero-slide');
  const dots = document.querySelectorAll('.hero-dots .dot');
  let currentSlide = 0;
  let slideInterval;

  const showSlide = (index) => {
    // Wrap index around
    if (index >= slides.length) index = 0;
    if (index < 0) index = slides.length - 1;

    // Reset classes
    slides.forEach(slide => slide.classList.remove('active'));
    dots.forEach(dot => dot.classList.remove('active'));

    // Set active
    slides[index].classList.add('active');
    dots[index].classList.add('active');
    currentSlide = index;
  };

  const nextSlide = () => {
    showSlide(currentSlide + 1);
  };

  const startInterval = () => {
    clearInterval(slideInterval);
    slideInterval = setInterval(nextSlide, 5000);
  };

  // Add click events to dots
  dots.forEach(dot => {
    dot.addEventListener('click', (e) => {
      const slideIndex = parseInt(e.target.getAttribute('data-slide'), 10);
      showSlide(slideIndex);
      startInterval(); // Reset interval
    });
  });

  // Start rotation
  startInterval();
}

/**
 * Category & Grid Filtering Logic
 */
function initCategoryFilter() {
  const headerCategories = document.querySelectorAll('.category-item');
  const sectionFilterBtns = document.querySelectorAll('.filter-btn');
  const productCards = document.querySelectorAll('.category-card');

  const applyFilter = (filterVal) => {
    // Sync header categories
    headerCategories.forEach(item => {
      const itemCat = item.getAttribute('data-category');
      if (itemCat === filterVal) {
        item.classList.add('active');
      } else {
        item.classList.remove('active');
      }
    });

    // Sync section filters
    sectionFilterBtns.forEach(btn => {
      const btnFilter = btn.getAttribute('data-filter');
      if (btnFilter === filterVal) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });

    // Filter grid cards
    productCards.forEach(card => {
      const cardCategory = card.getAttribute('data-category');
      
      // Start fade out animation
      card.style.opacity = '0';
      card.style.transform = 'scale(0.95)';
      
      setTimeout(() => {
        if (filterVal === 'all' || cardCategory === filterVal) {
          card.style.display = 'flex';
          setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'scale(1)';
          }, 50);
        } else {
          card.style.display = 'none';
        }
      }, 300);
    });
  };

  // Header category clicks
  headerCategories.forEach(item => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      const cat = item.getAttribute('data-category');
      applyFilter(cat);
      
      const prodSec = document.getElementById('products');
      if (prodSec) {
        prodSec.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  // Section filter button clicks
  sectionFilterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const filter = btn.getAttribute('data-filter');
      applyFilter(filter);
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
  const prevBtn = document.querySelector('.featured-slide-nav.prev');
  const nextBtn = document.querySelector('.featured-slide-nav.next');

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

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      goToSlide(currentSlide - 1);
      startAutoSlide();
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      goToSlide(currentSlide + 1);
      startAutoSlide();
    });
  }

  dots.forEach((dot, idx) => {
    dot.addEventListener('click', () => {
      goToSlide(idx);
      startAutoSlide();
    });
  });

  startAutoSlide();
}
