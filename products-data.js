export const IMAGE_BG_MAP = {
  "./assets/product_cables_new.png": "#181b1d",
  "./assets/products/cable_management/flexible_conduits.png": "#f8f9f8",
  "./assets/products/cable_management/gi_conduits.png": "#ebeceb",
  "./assets/products/cable_management/pvc_conduits.png": "#2b2e31",
  "./assets/products/cable_management/trunking.jpg": "#f2f2f2",
  "./assets/products/cable_termination/ferrule.jpg": "#f7f7f7",
  "./assets/products/cable_termination/gland.png": "#fdfdfd",
  "./assets/products/cable_termination/insulated_terminals.jpg": "#ffffff",
  "./assets/products/cable_termination/lug.jpg": "#f7f7f7",
  "./assets/products/industrial_plug_socket/industrial_plug_socket.png": "#dededd",
  "./assets/products/switches/cw_range_gold_switch_1g.jpg": "#2f2d2f",
  "./assets/products/switches/cw_range_gold_switch_3g_alt.jpg": "#313131",
  "./assets/products/switches/cw_range_gold_twin_socket.jpg": "#ffffff",
  "./assets/products/switches/en_range_single_socket.jpg": "#000000",
  "./assets/products/switches/en_range_switch_1g.jpg": "#000000",
  "./assets/products/switches/en_range_switch_3g.jpg": "#ffffff",
  "./assets/products/switches/en_range_twin_socket.jpg": "#000000",
  "./assets/products/switches/metal_clad_switch_2g.jpg": "#f7f7f7",
  "./assets/products/switches/v_range_brushed_switch_2g_alt.jpg": "#fefefe",
  "./assets/products/switches/v_range_single_socket.jpg": "#000000",
  "./assets/products/switches/v_range_usb_socket.jpg": "#000000",
  "./assets/products/switches/white_range_single_socket.jpg": "#000000",
  "./assets/products/switches/white_range_switch_1g.jpg": "#f7f7f7",
  "./assets/products/switches/white_range_usb_twin_socket.jpg": "#000000",
  "./assets/products/weatherproof/enclosure_box.jpg": "#f7f7f7",
  "./assets/products/weatherproof/ip55_cover.jpg": "#ffffff",
  "./assets/products/weatherproof/ip55_double_socket.jpg": "#fefefe",
  "./assets/products/weatherproof/ip66_switch_1g.jpg": "#fffeff",
  "./assets/products/weatherproof/ip66_switch_2g.jpg": "#fffeff",
  "./assets/products/weatherproof/isolator.jpg": "#f7f7f7",
  "./assets/products/wiring_accessories/cable_reel.jpg": "#f7f7f7",
  "./assets/products/wiring_accessories/cassette_reel.jpg": "#f7f7f7",
  "./assets/products/wiring_accessories/ceiling_rose.png": "#eaebea",
  "./assets/products/wiring_accessories/extension_socket.jpg": "#f7f7f7",
  "./assets/products/wiring_accessories/lamp_holder.png": "#f2f3f2",
  "./assets/products/wiring_accessories/multi_adaptor.jpg": "#f7f7f7",
  "./assets/products/wiring_accessories/plug_top.jpg": "#f7f7f7"
};

export const PRODUCTS_DATA = [
  {
    id: "switches",
    name: "Switches & Sockets",
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
    id: "weatherproof",
    name: "Weatherproof Products",
    items: [
      {
        name: "IP66 Weatherproof Socket Enclosure",
        img: "./assets/products/weatherproof/ip66_switch_2g.jpg",
        desc: "Full weatherproof switches and socket boxes designed to withstand heavy rainfall, jet spray, and harsh climates.",
        specs: ["IP66 Certified", "Corrosion Resistant", "Impact Proof"],
        range: "IP66"
      },
      {
        name: "IP66 Weatherproof Switch (1-Gang)",
        img: "./assets/products/weatherproof/ip66_switch_1g.jpg",
        desc: "Single gang outdoor switch enclosure with waterproof seal, ideal for gardens, balconies, and wet areas.",
        specs: ["IP66 Rated", "UV Resistant Casing", "10A Switch Control"],
        range: "IP66"
      },
      {
        name: "IP55 Weatherproof Double Socket",
        img: "./assets/products/weatherproof/ip55_double_socket.jpg",
        desc: "Double socket outlet with weatherproof spring-loaded cover and heavy rubber lining.",
        specs: ["IP55 Splashproof", "Twin 13A Outlets", "Lockable Cover Feature"],
        range: "IP55"
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
      }
    ]
  },
  {
    id: "wiring_accessories",
    name: "Wiring Accessories",
    items: [
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
      }
    ]
  },
  {
    id: "cable_management",
    name: "Cable Management",
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
        img: "./assets/products/cable_management/gi_conduits.png",
        desc: "Galvanized Iron conduit pipes providing heavy-duty mechanical shielding for high-risk industrial environments.",
        specs: ["Heavy Zinc Coating", "Class 4 Corrosion protection", "Threaded Joints"],
        range: "GI Conduits"
      },
      {
        name: "PVC Conduits (Rigid)",
        img: "./assets/products/cable_management/pvc_conduits.png",
        desc: "High-impact rigid PVC conduit pipes for safe electrical cabling routing inside concrete walls.",
        specs: ["High Impact Strength", "Easy Cold Bending", "Self-Extinguishing"],
        range: "PVC Conduits"
      },
      {
        name: "Flexible Corrugated Conduits",
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
      }
    ]
  },
  {
    id: "industrial_plug_socket",
    name: "Industrial Plugs & Sockets",
    items: [
      {
        name: "Heavy-Duty Industrial Plug & Socket Set",
        img: "./assets/products/industrial_plug_socket/industrial_plug_socket.png",
        desc: "Heavy-duty 3-pin and 5-pin industrial plug and connector sets, featuring secure lock-ring seals and splashproof shells.",
        specs: ["IP67 Rated", "High Load 16A-63A", "Impact Protected Case"],
        range: "Industrial Plug & Socket"
      },
      {
        name: "Industrial Wall Socket Outlet",
        img: "./assets/products/industrial_plug_socket/industrial_plug_socket.png",
        desc: "Wall-mounted industrial socket with mechanical interlock for extra safety, ideal for factory settings.",
        specs: ["IP44/IP67 Splashproof", "Mechanical Interlock", "3-Pin 16A/32A"],
        range: "Interlocked Sockets"
      }
    ]
  },
  {
    id: "installation_boxes",
    name: "Installation Boxes & Accessories",
    items: [
      {
        name: "UV Stabilized Terminal Enclosure Box",
        img: "./assets/products/weatherproof/enclosure_box.jpg",
        desc: "Durable terminal enclosure boxes with knockouts, perfect for outdoor connection joints and junction housings.",
        specs: ["UV Stabilized", "Impact Resistant", "Gasket Sealed"],
        range: "Enclosure Box"
      },
      {
        name: "Metal Knockout Junction Box",
        img: "./assets/products/weatherproof/enclosure_box.jpg",
        desc: "Galvanized steel junction box with multiple knockouts for standard electrical conduits and cabling.",
        specs: ["Galvanized Steel", "20mm/25mm Knockouts", "Earth Terminal Included"],
        range: "Metal Boxes"
      }
    ]
  }
];
