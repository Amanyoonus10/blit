// Voltix Landing Page Interactions

const PRODUCTS_DATA = [
  {
    id: "switches",
    name: "Switches",
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
    id: "fans",
    name: "Fans",
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
    id: "pipes",
    name: "Pipes & Fittings",
    items: [
      {
        name: "PVC Self-Adhesive Trunking",
        img: "./assets/products/cable_management/trunking.jpg",
        desc: "Clean white PVC self-adhesive trunking channels, hiding surface-run cables with a tidy aesthetic.",
        specs: ["Self-Adhesive option", "Strong Snap Lid", "Fire Resistant PVC"],
        range: "Trunking"
      },
      {
        name: "GI Conduits (Galvanized Iron)",
        img: "./assets/product_pipes_new.png",
        desc: "Galvanized Iron conduit pipes providing heavy-duty mechanical shielding for high-risk industrial environments.",
        specs: ["Heavy Zinc Coating", "Class 4 Corrosion protection", "Threaded Joints"],
        range: "GI Conduits"
      },
      {
        name: "PVC Conduits (Rigid)",
        img: "./assets/product_pipes_new.png",
        desc: "High-impact rigid PVC conduit pipes for safe electrical cabling routing inside concrete walls.",
        specs: ["High Impact Strength", "Easy Cold Bending", "Self-Extinguishing"],
        range: "PVC Conduits"
      },
      {
        name: "Flexible Corrugated Conduits",
        img: "./assets/product_pipes_new.png",
        desc: "Corrugated flexible plastic shielding, perfect for routing cables through tight bends and joints.",
        specs: ["High Flex Life", "Crush Resistant", "IP54 Compatible"],
        range: "Flexible Conduits"
      }
    ]
  },
  {
    id: "plugs",
    name: "Plugs & Sockets",
    items: [
      {
        name: "Heavy-Duty Industrial Plug & Socket Set",
        img: "./assets/products/industrial_plug_socket/industrial_plug_socket.png",
        desc: "Heavy-duty 3-pin and 5-pin industrial plug and connector sets, featuring secure lock-ring seals and splashproof shells.",
        specs: ["IP67 Rated", "High Load 16A-63A", "Impact Protected Case"],
        range: "Industrial Plug & Socket"
      },
      {
        name: "IP66 Weatherproof Socket Enclosure",
        img: "./assets/products/weatherproof/ip66_switch_2g.jpg",
        desc: "Full weatherproof switches and socket boxes designed to withstand heavy rainfall, jet spray, and harsh climates.",
        specs: ["IP66 Certified", "Corrosion Resistant", "Impact Proof"],
        range: "IP66"
      },
      {
        name: "Outdoor Rotary Isolator",
        img: "./assets/products/weatherproof/isolator.jpg",
        desc: "Outdoor rotary isolator switches with IP66 lockable handle, ensuring safe disconnection of air conditioning or heavy machinery.",
        specs: ["IP66 Weatherproof", "Lockable Handle", "35A - 63A Ratings"],
        range: "Isolator"
      },
      {
        name: "IP55 Semi-Weatherproof Socket Cover",
        img: "./assets/products/weatherproof/ip55_cover.jpg",
        desc: "Semi-weatherproof socket covers and enclosures with rubber gasket seals, ideal for balconies, lawns, and utility zones.",
        specs: ["IP55 Rated", "Transparent Lid", "Dust Protection"],
        range: "IP55"
      },
      {
        name: "UV Stabilized Terminal Enclosure Box",
        img: "./assets/products/weatherproof/enclosure_box.jpg",
        desc: "Durable terminal enclosure boxes with knockouts, perfect for outdoor connection joints and junction housings.",
        specs: ["UV Stabilized", "Impact Resistant", "Gasket Sealed"],
        range: "Enclosure Box"
      }
    ]
  },
  {
    id: "cables",
    name: "Cables & Accessories",
    items: [
      {
        name: "Premium Multicore Copper Cable",
        img: "./assets/product_cables_new.png",
        desc: "High conductivity copper wire core with heat resistant flame-retardant PVC outer sleeve.",
        specs: ["99.9% Pure Copper Core", "Flame Retardant PVC", "Low Smoke Halogen Free Option"],
        range: "Copper Cables"
      },
      {
        name: "Pure Copper Crimping Cable Lugs",
        img: "./assets/products/cable_termination/lug.jpg",
        desc: "Heavy-duty pure copper crimping cable lugs, guaranteeing solid electrical conductivity for power cables.",
        specs: ["99.9% Pure Copper", "Tin-Plated Finish", "Heavy Duty Barrel"],
        range: "Lugs"
      },
      {
        name: "Nylon and Brass Cable Glands",
        img: "./assets/products/cable_termination/gland.png",
        desc: "Nylon and brass cable glands providing mechanical strain relief and IP68 dust-waterproof seals for panels.",
        specs: ["IP68 Waterproof", "Strain Relief", "Brass/Nylon Options"],
        range: "Gland"
      },
      {
        name: "Tubular Copper Ferrules",
        img: "./assets/products/cable_termination/ferrule.jpg",
        desc: "Tubular copper ferrule sleeves for reliable electrical splicing and crimping connections.",
        specs: ["Tinned Copper", "Solid Crimping joints", "BS Standard"],
        range: "Ferrule"
      },
      {
        name: "Insulated Terminal Pin & Ring Connectors",
        img: "./assets/products/cable_termination/insulated_terminals.jpg",
        desc: "Color-coded insulated pin, ring, and spade terminal connectors, preventing short circuits and flashovers.",
        specs: ["Color Coded Sizes", "PVC Insulated sleeves", "High Conductivity Brass"],
        range: "Insulated Terminals"
      },
      {
        name: "High-Grade 13A Plug Top",
        img: "./assets/products/wiring_accessories/plug_top.jpg",
        desc: "High-grade 13A plug tops fitted with standard safety fuses, ideal for safe household appliance cabling.",
        specs: ["13A Fused", "BS1363 Compliant", "Ergonomic Grip"],
        range: "Plug Top"
      },
      {
        name: "Universal Multi Adaptor",
        img: "./assets/products/wiring_accessories/multi_adaptor.jpg",
        desc: "Universal multi-plug adaptors allowing multiple appliances to run from a single outlet safely.",
        specs: ["Shatterproof Casing", "Safety Shutters", "Compact Design"],
        range: "Multi Adaptor"
      },
      {
        name: "Ceiling Rose Mount Base",
        img: "./assets/products/wiring_accessories/ceiling_rose.png",
        desc: "Elegant round white ceiling mount base plate for standard pendant lights and electrical wiring cover.",
        specs: ["High Polycarbonate", "3-Terminal Standard", "Clean Finish"],
        range: "Ceiling Rose"
      },
      {
        name: "Batten Lamp Holder",
        img: "./assets/products/wiring_accessories/lamp_holder.png",
        desc: "Durable brass-lined plastic batten lamp holders, providing perfect electrical contact and thermal insulation.",
        specs: ["Brass Contacts", "B22/E27 Base compatibility", "High Temperature Rating"],
        range: "Lamp Holder"
      },
      {
        name: "Surge Protected Extension Socket",
        img: "./assets/products/wiring_accessories/extension_socket.jpg",
        desc: "Premium extension cord reels and boards with surge protectors and illuminated power indicators.",
        specs: ["Surge Protection", "Individually Switched", "Overload Protection"],
        range: "Extension Socket"
      },
      {
        name: "Heavy Duty Cable Reel",
        img: "./assets/products/wiring_accessories/cable_reel.jpg",
        desc: "Heavy-duty outdoor extension cable reels on a metal stand with integrated thermal cut-out switch.",
        specs: ["Heavy Duty Cable", "Metal Frame stand", "Thermal Trip Switch"],
        range: "Cable Reel"
      },
      {
        name: "Compact Cassette Reel",
        img: "./assets/products/wiring_accessories/cassette_reel.jpg",
        desc: "Compact cassette-style extension cords, perfect for residential use and easy cord management.",
        specs: ["Compact cassette", "Tangle-free storage", "Safety shutters"],
        range: "Cassette Reel"
      },
      {
        name: "Elite UV Insect Killer",
        img: "./assets/products/insect_killer/elite_series.jpg",
        desc: "Premium anodized aluminium insect exterminator featuring twin high-output UV lamps and a slide-out waste tray.",
        specs: ["Anodized Aluminium shell", "High Voltage killing grid", "Sleek Slim Design"],
        range: "Elite Series"
      },
      {
        name: "Prime Mesh Insect Killer",
        img: "./assets/products/insect_killer/prime_series.jpg",
        desc: "Heavy-duty steel mesh insect killer designed for continuous operation in shops, bakeries, and residences.",
        specs: ["Powder-coated steel mesh", "Energy Efficient UV Lamps", "Wall Mount or Hanging"],
        range: "Prime Series"
      }
    ]
  },
  {
    id: "solar",
    name: "Solar Solutions",
    items: [
      {
        name: "Monocrystalline Solar Panel",
        img: "./assets/product_solar_new.png",
        desc: "High-efficiency monocrystalline solar panels with tempered glass coating and anodized aluminium frames.",
        specs: ["22.4% Cell Efficiency", "Anti-Reflective Coating", "IP68 Junction Box"],
        range: "Solar Panels"
      },
      {
        name: "Smart Solar Grid Inverter",
        img: "./assets/product_solar_new.png",
        desc: "Smart on-grid solar inverter with dual MPPT tracking and real-time WiFi cloud monitoring systems.",
        specs: ["Dual MPPT Trackers", "98.6% Peak Efficiency", "Smart App Monitoring"],
        range: "Inverters"
      },
      {
        name: "Solar LiFePO4 Battery Storage",
        img: "./assets/product_solar_new.png",
        desc: "Lithium Iron Phosphate energy storage battery pack for reliable residential and commercial backup storage.",
        specs: ["LiFePO4 Chemistry", "5.12kWh Unit Capacity", "6000+ Long Cycle Life"],
        range: "Battery Storage"
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

    categoryData.items.forEach(item => {
      const card = document.createElement('div');
      card.className = 'modal-product-card';
      card.style.cursor = 'pointer';

      const specsList = item.specs.map(spec => `<li>${spec}</li>`).join('');

      card.innerHTML = `
        <div class="modal-card-img-box">
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
            Inquire via WhatsApp
          </button>
        </div>
      `;

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

    // Make the entire card click open WhatsApp
    modalGrid.querySelectorAll('.modal-product-card').forEach((cardEl, idx) => {
      cardEl.addEventListener('click', () => {
        const item = categoryData.items[idx];
        const productLink = window.location.origin + "?category=" + categoryId + "&product=" + encodeURIComponent(item.name);
        const text = encodeURIComponent(`Hello, I'm interested in the following product from Blit:\n*Product*: ${item.name}\n*Range*: ${item.range}\n*Link*: ${productLink}`);
        const whatsappUrl = `https://wa.me/971501995589?text=${text}`;
        window.open(whatsappUrl, '_blank');
        closeModal();
      });
    });
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
      if (categoryVal === 'fans') selectVal = 'fans';
      else if (categoryVal === 'pipes') selectVal = 'pipes';
      else if (categoryVal === 'plugs') selectVal = 'plugs';
      else if (categoryVal === 'cables') selectVal = 'glands';
      else if (categoryVal === 'solar') selectVal = 'switches'; // Fallback to switches or we can prefill text

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
