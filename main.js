// Blit Landing Page Interactions

const PRODUCTS_DATA = [
  {
    id: "switches",
    name: "Switch & Socket",
    icon: `<svg class="category-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="3" width="14" height="18" rx="2" ry="2"/><line x1="12" y1="8" x2="12" y2="16"/></svg>`,
    items: [
      {
        name: "White Range 1-Gang Switch",
        img: "./assets/products/switches/white_range_switch_1g.jpg",
        desc: "Classic white 1-gang light switch with smooth toggle click operation, built with flame-retardant casing.",
        specs: ["Flame Retardant Polycarbonate", "Smooth Toggle Action", "10A 250V Rating"],
        range: "White Range"
      },
      {
        name: "White Range Single Switched Socket",
        img: "./assets/products/switches/white_range_single_socket.jpg",
        desc: "Classic white 13A single switched socket outlet, featuring internal safety shutters and integrated neon indicator.",
        specs: ["13A Switched Outlet", "Safety Shutters Included", "Neon Power Indicator"],
        range: "White Range"
      },
      {
        name: "White Range Twin Switched USB Socket",
        img: "./assets/products/switches/white_range_usb_twin_socket.jpg",
        desc: "Double switched 13A socket outlet with integrated dual USB-C charging slots, minimal flat borders.",
        specs: ["Twin 13A Outlets", "Dual USB-C Charger Ports", "Smart Load Balancing"],
        range: "White Range"
      },
      {
        name: "EN Range Single Switched Socket",
        img: "./assets/products/switches/en_range_single_socket.jpg",
        desc: "Minimalist square single switched socket from the EN Range, featuring flat profile clip-on covers.",
        specs: ["Screwless Flat Cover", "High Conductivity Terminals", "13A Switched Rating"],
        range: "EN Range"
      },
      {
        name: "EN Range Twin Switched Socket",
        img: "./assets/products/switches/en_range_twin_socket.jpg",
        desc: "Elegant square double socket with smooth red toggle switches, sleek screwless clip-on cover panel.",
        specs: ["Double Switched", "Screwless Cover Design", "ISO9001 Quality Standard"],
        range: "EN Range"
      },
      {
        name: "EN Range 1-Gang Switch",
        img: "./assets/products/switches/en_range_switch_1g.jpg",
        desc: "Sleek EN Range single gang light switch plate, flat matte border layout.",
        specs: ["Flat Minimal Profile", "Easy Clip-on Faceplate", "10AX Inductive Rating"],
        range: "EN Range"
      },
      {
        name: "EN Range 3-Gang Switch",
        img: "./assets/products/switches/en_range_switch_3g.jpg",
        desc: "Multi-gang light switch control board, featuring three individual toggles in a clean square cover frame.",
        specs: ["3-Gang Independent Controls", "Sleek Matte Finish", "Fire Resistant Case"],
        range: "EN Range"
      },
      {
        name: "Metal Clad 2-Gang Switch",
        img: "./assets/products/switches/metal_clad_switch_2g.jpg",
        desc: "Heavy-duty industrial grade metal-clad switch block, ideal for workshops, garages, and plant rooms.",
        specs: ["Galvanized Steel Housing", "IK08 Impact Rated", "Surface Mount Plate"],
        range: "Metal Clad"
      },
      {
        name: "V Range Brushed Switch (2-Gang)",
        img: "./assets/products/switches/v_range_brushed_switch_2g_alt.jpg",
        desc: "Premium V Range 2-gang switch plate finished in brushed silver metal with modern dark borders.",
        specs: ["Brushed Silver finish", "Anti-fingerprint Lacquer", "Luxury Residential Standard"],
        range: "V Range"
      },
      {
        name: "V Range Switched Outlet (Single)",
        img: "./assets/products/switches/v_range_single_socket.jpg",
        desc: "Luxury single switched socket plate in a matte dark anthracite or brushed silver finish.",
        specs: ["Luxury Anthracite Plate", "Silver Alloy Terminals", "13A Switched BS Standard"],
        range: "V Range"
      },
      {
        name: "V Range USB Switched Socket",
        img: "./assets/products/switches/v_range_usb_socket.jpg",
        desc: "Sophisticated brushed metal double socket panel, containing fast charging USB ports and black switches.",
        specs: ["Dual Switched Sockets", "Integrated Fast USB Port", "Premium Brushed Finish"],
        range: "V Range"
      },
      {
        name: "V Range Switch Detailed Views",
        img: "./assets/products/switches/v_range_brushed_switch_views.jpg",
        desc: "Detailed profile and rear configuration design views of the premium V Range brushed metallic switch plates.",
        specs: ["Multi-angle Design Views", "Visual installation guide", "Rear component details"],
        range: "V Range"
      },
      {
        name: "CW Range Gold Switch (1-Gang)",
        img: "./assets/products/switches/cw_range_gold_switch_1g.jpg",
        desc: "Exquisite champagne gold single switch, offering ultimate prestige and high conductivity contacts.",
        specs: ["Champagne Gold coating", "Polished Bezel Edges", "Silver Alloy Switches"],
        range: "CW Range"
      },
      {
        name: "CW Range Gold Switch (3-Gang)",
        img: "./assets/products/switches/cw_range_gold_switch_3g_alt.jpg",
        desc: "Polished champagne gold 3-gang switch plate with gold toggle buttons, high-gloss premium look.",
        specs: ["3-Gang Gold Toggles", "Polished Metallic Bezel", "Luxury Residence Spec"],
        range: "CW Range"
      },
      {
        name: "CW Range Gold Twin Switched Socket",
        img: "./assets/products/switches/cw_range_gold_twin_socket.jpg",
        desc: "Luxurious double switched socket board in a champagne gold finish, combining absolute style and child safety.",
        specs: ["Champagne Gold Dual Sockets", "Premium Insulation Barrier", "13A Switched Standard"],
        range: "CW Range"
      }
    ]
  },
  {
    id: "weatherproof",
    name: "Weatherproof Solutions",
    icon: `<svg class="category-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>`,
    items: [
      {
        name: "Isolator",
        img: "./assets/products/weatherproof/isolator.jpg",
        desc: "Outdoor rotary isolator switches with IP66 lockable handle, ensuring safe disconnection of air conditioning or heavy machinery.",
        specs: ["IP66 Weatherproof", "Lockable Handle", "35A - 63A Ratings"],
        range: "Isolator"
      },
      {
        name: "IP55",
        img: "./assets/products/weatherproof/ip55_cover.jpg",
        desc: "Semi-weatherproof socket covers and enclosures with rubber gasket seals, ideal for balconies, lawns, and utility zones.",
        specs: ["IP55 Rated", "Transparent Lid", "Dust Protection"],
        range: "IP55"
      },
      {
        name: "IP66",
        img: "./assets/products/weatherproof/ip66_switch_2g.jpg",
        desc: "Full weatherproof switches and socket boxes designed to withstand heavy rainfall, jet spray, and harsh climates.",
        specs: ["IP66 Certified", "Corrosion Resistant", "Impact Proof"],
        range: "IP66"
      },
      {
        name: "Enclosure Box",
        img: "./assets/products/weatherproof/enclosure_box.jpg",
        desc: "Durable terminal enclosure boxes with knockouts, perfect for outdoor connection joints and junction housings.",
        specs: ["UV Stabilized", "Impact Resistant", "Gasket Sealed"],
        range: "Enclosure Box"
      }
    ]
  },
  {
    id: "wiring_accessories",
    name: "Wiring Accessories",
    icon: `<svg class="category-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="9" y1="7" x2="9" y2="10"/><line x1="15" y1="7" x2="15" y2="10"/></svg>`,
    items: [
      {
        name: "Plug Top",
        img: "./assets/products/wiring_accessories/plug_top.jpg",
        desc: "High-grade 13A plug tops fitted with standard safety fuses, ideal for safe household appliance cabling.",
        specs: ["13A Fused", "BS1363 Compliant", "Ergonomic Grip"],
        range: "Plug Top"
      },
      {
        name: "Multi Adaptor",
        img: "./assets/products/wiring_accessories/multi_adaptor.jpg",
        desc: "Universal multi-plug adaptors allowing multiple appliances to run from a single outlet safely.",
        specs: ["Shatterproof Casing", "Safety Shutters", "Compact Design"],
        range: "Multi Adaptor"
      },
      {
        name: "Ceiling Rose",
        img: "./assets/products/wiring_accessories/ceiling_rose.png",
        desc: "Elegant round white ceiling mount base plate for standard pendant lights and electrical wiring cover.",
        specs: ["High Polycarbonate", "3-Terminal Standard", "Clean Finish"],
        range: "Ceiling Rose"
      },
      {
        name: "Lamp Holder",
        img: "./assets/products/wiring_accessories/lamp_holder.png",
        desc: "Durable brass-lined plastic batten lamp holders, providing perfect electrical contact and thermal insulation.",
        specs: ["Brass Contacts", "B22/E27 Base compatibility", "High Temperature Rating"],
        range: "Lamp Holder"
      },
      {
        name: "Extension Socket",
        img: "./assets/products/wiring_accessories/extension_socket.jpg",
        desc: "Premium extension cord reels and boards with surge protectors and illuminated power indicators.",
        specs: ["Surge Protection", "Individually Switched", "Overload Protection"],
        range: "Extension Socket"
      },
      {
        name: "Cable Reel",
        img: "./assets/products/wiring_accessories/cable_reel.jpg",
        desc: "Heavy-duty outdoor extension cable reels on a metal stand with integrated thermal cut-out switch.",
        specs: ["Heavy Duty Cable", "Metal Frame stand", "Thermal Trip Switch"],
        range: "Cable Reel"
      },
      {
        name: "Cassette Reel",
        img: "./assets/products/wiring_accessories/cassette_reel.jpg",
        desc: "Compact cassette-style extension cords, perfect for residential use and easy cord management.",
        specs: ["Compact cassette", "Tangle-free storage", "Safety shutters"],
        range: "Cassette Reel"
      }
    ]
  },
  {
    id: "cable_management",
    name: "Cable Management",
    icon: `<svg class="category-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 15V9a4 4 0 0 1 4-4h5"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/></svg>`,
    items: [
      {
        name: "Trunking",
        img: "./assets/products/cable_management/trunking.jpg",
        desc: "Clean white PVC self-adhesive trunking channels, hiding surface-run cables with a tidy aesthetic.",
        specs: ["Self-Adhesive option", "Strong Snap Lid", "Fire Resistant PVC"],
        range: "Trunking"
      },
      {
        name: "GI Conduits",
        img: "./assets/products/cable_management/gi_conduits.png",
        desc: "Galvanized Iron conduit pipes providing heavy-duty mechanical shielding for high-risk industrial environments.",
        specs: ["Heavy Zinc Coating", "Class 4 Corrosion protection", "Threaded Joints"],
        range: "GI Conduits"
      },
      {
        name: "PVC Conduits",
        img: "./assets/products/cable_management/pvc_conduits.png",
        desc: "High-impact rigid PVC conduit pipes for safe electrical cabling routing inside concrete walls.",
        specs: ["High Impact Strength", "Easy Cold Bending", "Self-Extinguishing"],
        range: "PVC Conduits"
      },
      {
        name: "Flexible Conduits",
        img: "./assets/products/cable_management/flexible_conduits.png",
        desc: "Corrugated flexible plastic shielding, perfect for routing cables through tight bends and joints.",
        specs: ["High Flex Life", "Crush Resistant", "IP54 Compatible"],
        range: "Flexible Conduits"
      }
    ]
  },
  {
    id: "cable_termination",
    name: "Cable Termination",
    icon: `<svg class="category-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>`,
    items: [
      {
        name: "Lugs",
        img: "./assets/products/cable_termination/lug.jpg",
        desc: "Heavy-duty pure copper crimping cable lugs, guaranteeing solid electrical conductivity for power cables.",
        specs: ["99.9% Pure Copper", "Tin-Plated Finish", "Heavy Duty Barrel"],
        range: "Lugs"
      },
      {
        name: "Gland",
        img: "./assets/products/cable_termination/gland.png",
        desc: "Nylon and brass cable glands providing mechanical strain relief and IP68 dust-waterproof seals for panels.",
        specs: ["IP68 Waterproof", "Strain Relief", "Brass/Nylon Options"],
        range: "Gland"
      },
      {
        name: "Ferrule",
        img: "./assets/products/cable_termination/ferrule.jpg",
        desc: "Tubular copper ferrule sleeves for reliable electrical splicing and crimping connections.",
        specs: ["Tinned Copper", "Solid Crimping joints", "BS Standard"],
        range: "Ferrule"
      },
      {
        name: "Insulated Terminals",
        img: "./assets/products/cable_termination/insulated_terminals.jpg",
        desc: "Color-coded insulated pin, ring, and spade terminal connectors, preventing short circuits and flashovers.",
        specs: ["Color Coded Sizes", "PVC Insulated sleeves", "High Conductivity Brass"],
        range: "Insulated Terminals"
      }
    ]
  },
  {
    id: "industrial_plug_socket",
    name: "Industrial Plug & Socket",
    icon: `<svg class="category-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>`,
    items: [
      {
        name: "Industrial Plug & Socket",
        img: "./assets/products/industrial_plug_socket/industrial_plug_socket.png",
        desc: "Heavy-duty 3-pin and 5-pin industrial plug and connector sets, featuring secure lock-ring seals and splashproof shells.",
        specs: ["IP67 Rated", "High Load 16A-63A", "Impact Protected Case"],
        range: "Industrial Plug & Socket"
      }
    ]
  },
  {
    id: "ventilation",
    name: "Air & Ventilation",
    icon: `<svg class="category-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>`,
    items: [
      {
        name: "24\" Industrial Stand Fan",
        img: "./assets/products/ventilation/industrial_stand_fan.jpg",
        desc: "High-velocity heavy duty 24-inch stand fan with height-adjustable metal pole and 3 aerodynamic steel blades.",
        specs: ["24-inch Diameter", "Heavy Duty Motor", "Aerodynamic Blades"],
        range: "Industrial Stand Fan"
      },
      {
        name: "26\" Industrial Stand Fan",
        img: "./assets/products/ventilation/industrial_stand_fan.jpg",
        desc: "Powerful 26-inch industrial pedestal fan designed to deliver maximum cooling airflow across large factory zones.",
        specs: ["26-inch Pedestal", "3-Speed Regulation", "Tilt Adjustable Header"],
        range: "Industrial Stand Fan"
      },
      {
        name: "39\" Industrial Stand Fan",
        img: "./assets/products/ventilation/industrial_stand_fan.jpg",
        desc: "Ultra-high output 39-inch industrial pedestal stand fan, built for massive warehouse cooling and circulation.",
        specs: ["39-inch Diameter", "Cast Iron Base stability", "High Volume Output"],
        range: "Industrial Stand Fan"
      },
      {
        name: "24\" Industrial Wall Fan",
        img: "./assets/products/ventilation/industrial_wall_fan.jpg",
        desc: "Space-saving wall-mounted industrial 24-inch fan with oscillation control and protective mesh safety cage.",
        specs: ["24-inch Wall Mounted", "Wide Angle Oscillation", "Solid Bracket Support"],
        range: "Industrial Wall Fan"
      },
      {
        name: "26\" Industrial Wall Fan",
        img: "./assets/products/ventilation/industrial_wall_fan.jpg",
        desc: "Durable 26-inch wall-mounted cooling fan, perfect for warehouses, shops, and outdoor events.",
        specs: ["26-inch Diameter", "Double Ball Bearing Motor", "Low Noise Blades"],
        range: "Industrial Wall Fan"
      },
      {
        name: "39\" Industrial Wall Fan",
        img: "./assets/products/ventilation/industrial_wall_fan.jpg",
        desc: "High-capacity 39-inch industrial wall circulation fan, designed to handle continuous cooling in commercial areas.",
        specs: ["39-inch Fan Blade", "Premium Pull Cord Control", "Corrosion Resistant Casing"],
        range: "Industrial Wall Fan"
      }
    ]
  },
  {
    id: "insect_killer",
    name: "Insect Killer",
    icon: `<svg class="category-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/></svg>`,
    items: [
      {
        name: "Elite Series",
        img: "./assets/products/insect_killer/elite_series.jpg",
        desc: "Premium anodized aluminium insect exterminator featuring twin high-output UV lamps and a slide-out waste tray.",
        specs: ["Anodized Aluminium shell", "High Voltage killing grid", "Sleek Slim Design"],
        range: "Elite Series"
      },
      {
        name: "Prime Series",
        img: "./assets/products/insect_killer/prime_series.jpg",
        desc: "Heavy-duty steel mesh insect killer designed for continuous operation in shops, bakeries, and residences.",
        specs: ["Powder-coated steel mesh", "Energy Efficient UV Lamps", "Wall Mount or Hanging"],
        range: "Prime Series"
      }
    ]
  }
];

document.addEventListener('DOMContentLoaded', () => {
  initHeroSlider();
  initProductExplorer();
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
    if (index >= slides.length) index = 0;
    if (index < 0) index = slides.length - 1;

    slides.forEach(slide => slide.classList.remove('active'));
    dots.forEach(dot => dot.classList.remove('active'));

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
 * Interactive Product Catalog Explorer Logic
 */
function initProductExplorer() {
  const categoryListContainer = document.getElementById('catalog-category-list');
  const productsGrid = document.getElementById('catalog-products-grid');
  const searchInput = document.getElementById('catalog-search-input');
  const rangeFiltersContainer = document.getElementById('catalog-range-filters-container');
  const emptyState = document.getElementById('catalog-empty-state');
  const headerCategories = document.querySelectorAll('.categories-bar .category-item');

  if (!categoryListContainer || !productsGrid) return;

  let activeCategoryId = PRODUCTS_DATA[0].id;
  let activeRangeFilter = 'all';
  let searchQuery = '';

  // Render categories in sidebar
  const renderCategories = () => {
    categoryListContainer.innerHTML = '';
    PRODUCTS_DATA.forEach(cat => {
      const button = document.createElement('button');
      button.className = `category-btn ${cat.id === activeCategoryId ? 'active' : ''}`;
      button.setAttribute('data-id', cat.id);
      button.innerHTML = `
        ${cat.icon}
        <span>${cat.name}</span>
      `;
      button.addEventListener('click', () => {
        searchQuery = '';
        searchInput.value = '';
        setActiveCategory(cat.id);
      });
      categoryListContainer.appendChild(button);
    });
  };

  // Set active category and sync header navigation
  const setActiveCategory = (categoryId) => {
    activeCategoryId = categoryId;
    activeRangeFilter = 'all';
    
    // Update sidebar buttons active state
    document.querySelectorAll('.category-btn').forEach(btn => {
      if (btn.getAttribute('data-id') === categoryId) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });

    // Update header navigation active state
    headerCategories.forEach(item => {
      const itemCat = item.getAttribute('data-category');
      if (itemCat === categoryId) {
        item.classList.add('active');
      } else {
        item.classList.remove('active');
      }
    });

    renderRangeFilters();
    renderProducts();
  };

  // Render range filters based on active category
  const renderRangeFilters = () => {
    rangeFiltersContainer.innerHTML = '';
    
    const activeCategory = PRODUCTS_DATA.find(cat => cat.id === activeCategoryId);
    if (!activeCategory) return;

    // Get unique ranges
    const ranges = ['all', ...new Set(activeCategory.items.map(item => item.range))];

    ranges.forEach(range => {
      const chip = document.createElement('button');
      chip.className = `filter-chip ${range === activeRangeFilter ? 'active' : ''}`;
      chip.textContent = range === 'all' ? 'All Ranges' : range;
      chip.addEventListener('click', () => {
        activeRangeFilter = range;
        document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        renderProducts();
      });
      rangeFiltersContainer.appendChild(chip);
    });
  };

  // Render product cards based on active category, range filter, and search query
  const renderProducts = () => {
    productsGrid.innerHTML = '';
    
    const titleEl = document.getElementById('catalog-active-category-title');
    if (titleEl) {
      if (searchQuery.trim() !== '') {
        titleEl.textContent = `Search Results for "${searchQuery}"`;
      } else {
        const activeCategory = PRODUCTS_DATA.find(cat => cat.id === activeCategoryId);
        titleEl.textContent = activeCategory ? activeCategory.name : 'Products';
      }
    }
    
    let itemsToRender = [];

    if (searchQuery.trim() !== '') {
      // Search across ALL categories
      PRODUCTS_DATA.forEach(cat => {
        cat.items.forEach(item => {
          const nameMatch = item.name.toLowerCase().includes(searchQuery.toLowerCase());
          const descMatch = item.desc.toLowerCase().includes(searchQuery.toLowerCase());
          const rangeMatch = item.range.toLowerCase().includes(searchQuery.toLowerCase());
          const catMatch = cat.name.toLowerCase().includes(searchQuery.toLowerCase());
          if (nameMatch || descMatch || rangeMatch || catMatch) {
            itemsToRender.push({
              ...item,
              categoryId: cat.id,
              categoryName: cat.name
            });
          }
        });
      });
      
      // Hide range filters in search mode
      rangeFiltersContainer.style.opacity = '0.3';
      rangeFiltersContainer.style.pointerEvents = 'none';
    } else {
      // Normal category display
      rangeFiltersContainer.style.opacity = '1';
      rangeFiltersContainer.style.pointerEvents = 'all';

      const activeCategory = PRODUCTS_DATA.find(cat => cat.id === activeCategoryId);
      if (activeCategory) {
        itemsToRender = activeCategory.items.filter(item => {
          return activeRangeFilter === 'all' || item.range === activeRangeFilter;
        }).map(item => ({
          ...item,
          categoryId: activeCategory.id,
          categoryName: activeCategory.name
        }));
      }
    }

    if (itemsToRender.length === 0) {
      emptyState.style.display = 'flex';
      productsGrid.style.display = 'none';
    } else {
      emptyState.style.display = 'none';
      productsGrid.style.display = 'flex';

      itemsToRender.forEach((item, index) => {
        const card = document.createElement('div');
        card.className = 'catalog-card animate-card';
        card.style.animationDelay = `${index * 40}ms`;
        
        const specsList = item.specs.map(spec => `<li><span class="bullet">•</span> ${spec}</li>`).join('');

        card.innerHTML = `
          <div class="card-image-box">
            <img src="${item.img}" alt="${item.name}" loading="lazy" class="card-img">
            <span class="range-badge">${item.range}</span>
          </div>
          <div class="card-body">
            <span class="card-cat-label">${item.categoryName}</span>
            <h4 class="card-title">${item.name}</h4>
            <p class="card-desc">${item.desc}</p>
            <ul class="card-specs">
              ${specsList}
            </ul>
            <button class="card-inquiry-btn" data-category="${item.categoryId}" data-product="${item.name}">
              Quick Inquiry <span class="arrow">→</span>
            </button>
          </div>
        `;

        // Inquiry button click listener
        card.querySelector('.card-inquiry-btn').addEventListener('click', (e) => {
          const cat = e.currentTarget.getAttribute('data-category');
          const prod = e.currentTarget.getAttribute('data-product');
          triggerInquiry(cat, prod);
        });

        productsGrid.appendChild(card);
      });
    }
  };

  const triggerInquiry = (categoryVal, productVal) => {
    const quoteFormSelect = document.getElementById('client-needs');
    const quoteFormTextarea = document.getElementById('client-message');
    const quoteSection = document.getElementById('quote');

    if (quoteFormSelect) {
      // Map catalog category to form select value
      // Option values: switches, fans, pipes, plugs, glands, solderless
      let selectVal = 'switches';
      if (categoryVal === 'ventilation') selectVal = 'fans';
      else if (categoryVal === 'cable_management') selectVal = 'pipes';
      else if (categoryVal === 'weatherproof') selectVal = 'plugs';
      else if (categoryVal === 'wiring_accessories') selectVal = 'plugs';
      else if (categoryVal === 'cable_termination') selectVal = 'glands';
      else if (categoryVal === 'industrial_plug_socket') selectVal = 'plugs';

      quoteFormSelect.value = selectVal;
    }

    if (quoteFormTextarea) {
      quoteFormTextarea.value = `I am interested in requesting a quote for: ${productVal}.\n\nPlease provide specifications, pricing, and minimum order quantity.`;
    }

    if (quoteSection) {
      quoteSection.scrollIntoView({ behavior: 'smooth' });
      // Pulse animation on the form
      const quoteBox = quoteSection.querySelector('.quote-box');
      if (quoteBox) {
        quoteBox.classList.add('pulse-highlight');
        setTimeout(() => quoteBox.classList.remove('pulse-highlight'), 1500);
      }
    }
  };

  // Connect Top Header navigation categories click
  headerCategories.forEach(item => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      const cat = item.getAttribute('data-category');
      searchQuery = '';
      searchInput.value = '';
      setActiveCategory(cat);
      
      const prodSec = document.getElementById('products');
      if (prodSec) {
        prodSec.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  // Search input change handler
  searchInput.addEventListener('input', (e) => {
    searchQuery = e.target.value;
    renderProducts();
  });

  // Wire up horizontal scrolling navigation buttons
  const scrollPrevBtn = document.getElementById('catalog-scroll-prev');
  const scrollNextBtn = document.getElementById('catalog-scroll-next');
  if (scrollPrevBtn && scrollNextBtn) {
    scrollPrevBtn.addEventListener('click', () => {
      productsGrid.scrollBy({ left: -344, behavior: 'smooth' }); // card width 320 + gap 24
    });
    scrollNextBtn.addEventListener('click', () => {
      productsGrid.scrollBy({ left: 344, behavior: 'smooth' });
    });
  }

  // Initialize
  renderCategories();
  renderRangeFilters();
  renderProducts();
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
