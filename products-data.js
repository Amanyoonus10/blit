export const IMAGE_BG_MAP = {
  "/assets/product_cables_new.webp": "#181b1d",
  "/assets/products/cable_management/flexible_conduits.webp": "#f8f9f8",
  "/assets/products/cable_management/gi_conduits.webp": "#ebeceb",
  "/assets/products/cable_management/pvc_conduits.webp": "#2b2e31",
  "/assets/products/cable_management/trunking.webp": "#f2f2f2",
  "/assets/products/cable_termination/ferrule.webp": "#f7f7f7",
  "/assets/products/cable_termination/gland.webp": "#fdfdfd",
  "/assets/products/cable_termination/insulated_terminals.webp": "#ffffff",
  "/assets/products/cable_termination/lug.webp": "#f7f7f7",
  "/assets/products/switches/cw_range_gold_switch_1g.webp": "#2f2d2f",
  "/assets/products/switches/cw_range_gold_switch_3g_alt.webp": "#313131",
  "/assets/products/switches/cw_range_gold_twin_socket.webp": "#000000",
  "/assets/products/switches/en_range_single_socket.webp": "#000000",
  "/assets/products/switches/en_range_switch_1g.webp": "#000000",
  "/assets/products/switches/en_range_switch_3g.webp": "#ffffff",
  "/assets/products/switches/en_range_twin_socket.webp": "#000000",
  "/assets/products/switches/metal_clad_switch_2g.webp": "#f7f7f7",
  "/assets/products/switches/metal_clad_socket_double.webp": "#f7f7f7",
  "/assets/products/switches/v_range_brushed_switch_2g_alt.webp": "#000000",
  "/assets/products/switches/v_range_single_socket.webp": "#000000",
  "/assets/products/switches/v_range_usb_socket.webp": "#000000",
  "/assets/products/switches/white_range_single_socket.webp": "#000000",
  "/assets/products/switches/white_range_switch_1g.webp": "#ffffff",
  "/assets/products/switches/white_range_usb_twin_socket.webp": "#000000",
  "/assets/products/weatherproof/enclosure_box.webp": "#f7f7f7",
  "/assets/products/weatherproof/ip55_cover.webp": "#ffffff",
  "/assets/products/weatherproof/ip55_double_socket.webp": "#fefefe",
  "/assets/products/weatherproof/ip66_switch_1g.webp": "#fffeff",
  "/assets/products/weatherproof/ip66_switch_2g.webp": "#fffeff",
  "/assets/products/weatherproof/ip66_socket_cover.webp": "#fffeff",
  "/assets/products/weatherproof/isolator.webp": "#f7f7f7",
  "/assets/products/industrial_plug_socket/industrial_plug_socket.webp": "#f7f7f7",
  "/assets/products/wiring_accessories/cable_reel.webp": "#f7f7f7",
  "/assets/products/wiring_accessories/cassette_reel.webp": "#f7f7f7",
  "/assets/products/wiring_accessories/ceiling_rose.webp": "#eaebea",
  "/assets/products/wiring_accessories/extension_socket.webp": "#f7f7f7",
  "/assets/products/wiring_accessories/lamp_holder.webp": "#f2f3f2",
  "/assets/products/wiring_accessories/multi_adaptor.webp": "#f7f7f7",
  "/assets/products/wiring_accessories/plug_top.webp": "#f7f7f7",
  "/assets/products/wiring_accessories/plug_top_alt.webp": "#FFFFFF",
  "/assets/products/ventilation/industrial_stand_fan.webp": "#ffffff",
  "/assets/products/ventilation/industrial_wall_fan.webp": "#ffffff",
  "/assets/products/insect_killer/elite_series.webp": "#ffffff",
  "/assets/products/insect_killer/prime_series.webp": "#ffffff"
};

export const PRODUCTS_DATA = [
  {
    id: "switches",
    name: "Switches & Sockets",
    items: [
      {
        name: "White Range 1-Gang Switch",
        img: "/assets/products/switches/white_range_switch_1g.webp",
        desc: "Classic white 1-gang 10AX light switch with smooth toggle click operation (Model W301/W302).",
        specs: ["Flame Retardant Polycarbonate", "Smooth Toggle Action", "10A 250V Rating"],
        range: "White Range"
      },
      {
        name: "White Range 2-Gang 2-Way Switch",
        img: "/assets/products/switches/w_range_switch_2g.png",
        desc: "White 2-gang 2-way light switch plate engineered for dual circuit control (Model W304).",
        specs: ["Dual Gang Independent Control", "2-Way Circuit Switching", "10AX 250V Rating"],
        range: "White Range"
      },
      {
        name: "White Range Bell Push Switch",
        img: "/assets/products/switches/w_range_bell_switches.png",
        desc: "Retractive 10A bell push switch featuring crisp indicator bell symbol (Model W317/W319).",
        specs: ["Retractive Momentary Push", "Optional Neon Indicator", "BS EN 60669-1"],
        range: "White Range"
      },
      {
        name: "White Range Single Switched Socket",
        img: "/assets/products/switches/white_range_single_socket.webp",
        desc: "Classic white 13A single switched socket outlet with safety shutters (Model W405/W407).",
        specs: ["13A Switched Outlet", "Safety Shutters Included", "Neon Power Indicator"],
        range: "White Range"
      },
      {
        name: "White Range Twin Switched USB Socket",
        img: "/assets/products/switches/white_range_usb_twin_socket.webp",
        desc: "Double switched 13A socket outlet with integrated dual USB charging slots (Model W503).",
        specs: ["Twin 13A Outlets", "Dual USB Charger Ports", "Smart Load Balancing"],
        range: "White Range"
      },
      {
        name: "White Range 45A Cooker Control Unit",
        img: "/assets/products/switches/w_range_cooker_control.png",
        desc: "Heavy duty 45A cooker control unit with red neon indicator and integrated 13A switched socket outlet (Model W331).",
        specs: ["45A Double Pole Rating", "Integrated 13A Socket", "BS 4177 Compliant"],
        range: "White Range"
      },
      {
        name: "White Range 400W Rotary Dimmer",
        img: "/assets/products/switches/w_range_dimmers.png",
        desc: "1-gang 400W rotary push ON/OFF dimmer switch for smooth lighting adjustment (Model W352/W401).",
        specs: ["400W Load Rating", "Push ON/OFF Rotary Action", "BS EN 60669-2-1"],
        range: "White Range"
      },
      {
        name: "White Range Universal Multi Socket",
        img: "/assets/products/switches/w_range_multi_sockets.png",
        desc: "10A/13A universal multi-standard socket accepting international plug pin configurations (Model W460/W407M).",
        specs: ["Universal Pin Compatibility", "Internal Safety Shutter", "IEC 60884 Compliant"],
        range: "White Range"
      },
      {
        name: "White Range 13A Switched FCU + Neon",
        img: "/assets/products/switches/w_range_fcus.png",
        desc: "13A switched fused connection spur unit with front-accessible fuse drawer and neon indicator (Model W413/W419).",
        specs: ["13A BS1362 Fuse Fitted", "Front Access Fuse Carrier", "BS 1363-4 Compliant"],
        range: "White Range"
      },
      {
        name: "White Range RJ45 Cat6 Data Outlet",
        img: "/assets/products/switches/w_range_data_tv.png",
        desc: "Cat6 RJ45 high-speed data network wall plate with shuttered connector port (Model W442/W443).",
        specs: ["Cat6 Gigabit Performance", "Shuttered Data Port", "TIA/EIA-568 Standard"],
        range: "White Range"
      },
      {
        name: "EN Range Single Switched Socket",
        img: "/assets/products/switches/en_range_single_socket.webp",
        desc: "Minimalist square single switched socket from the EN Range, featuring flat profile clip-on covers.",
        specs: ["Screwless Flat Cover", "High Conductivity Terminals", "13A Switched Rating"],
        range: "EN Range"
      },
      {
        name: "EN Range Twin Switched Socket",
        img: "/assets/products/switches/en_range_twin_socket.webp",
        desc: "Elegant square double socket with smooth red toggle switches, sleek screwless clip-on cover panel.",
        specs: ["Double Switched", "Screwless Cover Design", "ISO9001 Quality Standard"],
        range: "EN Range"
      },
      {
        name: "EN Range 1-Gang Switch",
        img: "/assets/products/switches/en_range_switch_1g.webp",
        desc: "Sleek EN Range single gang light switch plate, flat matte border layout.",
        specs: ["Flat Minimal Profile", "Easy Clip-on Faceplate", "10AX Inductive Rating"],
        range: "EN Range"
      },
      {
        name: "EN Range 3-Gang Switch",
        img: "/assets/products/switches/en_range_switch_3g.webp",
        desc: "Multi-gang light switch control board, featuring three individual toggles in a clean square cover frame.",
        specs: ["3-Gang Independent Controls", "Sleek Matte Finish", "Fire Resistant Case"],
        range: "EN Range"
      },
      {
        name: "Metal Clad 2-Gang Switch",
        img: "/assets/products/switches/metal_clad_switch_2g.webp",
        desc: "Heavy-duty industrial grade metal-clad switch block, ideal for workshops, garages, and plant rooms.",
        specs: ["Galvanized Steel Housing", "IK08 Impact Rated", "Surface Mount Plate"],
        range: "Metal Clad"
      },
      {
        name: "Metal Clad 2-Gang Switched Socket",
        img: "/assets/products/switches/metal_clad_socket_double.webp",
        desc: "Rugged double switched 13A socket outlet enclosed in an impact-resistant metal clad housing, designed for heavy industrial use.",
        specs: ["Double 13A Switched Sockets", "Heavy Duty Steel Enclosure", "Earth Terminal Included"],
        range: "Metal Clad"
      },
      {
        name: "V Range Brushed Switch (2-Gang)",
        img: "/assets/products/switches/v_range_brushed_switch_2g_alt.webp",
        desc: "Premium V Range 2-gang switch plate finished in brushed silver metal with modern dark borders.",
        specs: ["Brushed Silver finish", "Anti-fingerprint Lacquer", "Luxury Residential Standard"],
        range: "V Range"
      },
      {
        name: "V Range Switched Outlet (Single)",
        img: "/assets/products/switches/v_range_single_socket.webp",
        desc: "Luxury single switched socket plate in a matte dark anthracite or brushed silver finish.",
        specs: ["Luxury Anthracite Plate", "Silver Alloy Terminals", "13A Switched BS Standard"],
        range: "V Range"
      },
      {
        name: "V Range USB Switched Socket",
        img: "/assets/products/switches/v_range_usb_socket.webp",
        desc: "Sophisticated brushed metal double socket panel, containing fast charging USB ports and black switches.",
        specs: ["Dual Switched Sockets", "Integrated Fast USB Port", "Premium Brushed Finish"],
        range: "V Range"
      },
      {
        name: "CW Range Gold Switch (1-Gang)",
        img: "/assets/products/switches/cw_range_gold_switch_1g.webp",
        desc: "Exquisite champagne gold single switch, offering ultimate prestige and high conductivity contacts.",
        specs: ["Champagne Gold coating", "Polished Bezel Edges", "Silver Alloy Switches"],
        range: "CW Range"
      },
      {
        name: "CW Range Gold Switch (3-Gang)",
        img: "/assets/products/switches/cw_range_gold_switch_3g_alt.webp",
        desc: "Polished champagne gold 3-gang switch plate with gold toggle buttons, high-gloss premium look.",
        specs: ["3-Gang Gold Toggles", "Polished Metallic Bezel", "Luxury Residence Spec"],
        range: "CW Range"
      },
      {
        name: "CW Range Gold Twin Switched Socket",
        img: "/assets/products/switches/cw_range_gold_twin_socket.webp",
        desc: "Luxurious double switched socket board in a champagne gold finish, combining absolute style and child safety.",
        specs: ["Champagne Gold Dual Sockets", "Premium Insulation Barrier", "13A Switched Standard"],
        range: "CW Range"
      }
    ]
  },
  {
    id: "weatherproof",
    name: "Weatherproof Solutions",
    items: [
      {
        name: "IP66 Weatherproof Switched Socket Enclosure",
        img: "/assets/products/weatherproof/ip66_socket_cover.webp",
        desc: "Full weatherproof double socket box designed to withstand heavy rainfall, jet spray, and harsh outdoor climates.",
        specs: ["IP66 Certified Waterproof", "Impact Resistant Cover", "Spring-loaded Lid Lock"],
        range: "IP66"
      },
      {
        name: "IP66 Weatherproof Switch (1-Gang)",
        img: "/assets/products/weatherproof/ip66_switch_1g.webp",
        desc: "Single gang outdoor switch enclosure with waterproof seal, ideal for gardens, balconies, and wet areas.",
        specs: ["IP66 Rated", "UV Resistant Casing", "10A Switch Control"],
        range: "IP66"
      },
      {
        name: "IP66 Weatherproof Switch (2-Gang)",
        img: "/assets/products/weatherproof/ip66_switch_2g.webp",
        desc: "Two gang outdoor switch enclosure with waterproof seal, designed for convenient dual lighting control.",
        specs: ["IP66 Rated Waterproof", "UV Stabilized Case", "Dual 10A Controls"],
        range: "IP66"
      },
      {
        name: "IP55 Weatherproof Double Socket",
        img: "/assets/products/weatherproof/ip55_double_socket.webp",
        desc: "Double socket outlet with weatherproof spring-loaded cover and heavy rubber lining.",
        specs: ["IP55 Splashproof", "Twin 13A Outlets", "Lockable Cover Feature"],
        range: "IP55"
      },
      {
        name: "Outdoor Rotary Isolator",
        img: "/assets/products/weatherproof/isolator.webp",
        desc: "Outdoor rotary isolator switches with IP66 lockable handle, ensuring safe disconnection of air conditioning or heavy machinery.",
        specs: ["IP66 Weatherproof", "Lockable Handle", "35A - 63A Ratings"],
        range: "Isolator"
      },
      {
        name: "IP55 Semi-Weatherproof Socket Cover",
        img: "/assets/products/weatherproof/ip55_cover.webp",
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
        img: "/assets/products/wiring_accessories/plug_top.webp",
        desc: "High-grade 13A plug tops fitted with standard safety fuses, ideal for safe household appliance cabling.",
        specs: ["13A Fused", "BS1363 Compliant", "Ergonomic Grip"],
        range: "Plug Top"
      },
      {
        name: "Standard 13A UK Plug Top",
        img: "/assets/products/wiring_accessories/plug_top_alt.webp",
        desc: "Premium white 13A UK plug top with solid brass pins, compliant with BS1363/A standards, perfect for appliance and industrial power replacement connections.",
        specs: ["13A Fused", "BS1363/A Compliant", "Solid Brass Pins"],
        range: "Plug Top"
      },
      {
        name: "Universal Multi Adaptor",
        img: "/assets/products/wiring_accessories/multi_adaptor.webp",
        desc: "Universal multi-plug adaptors allowing multiple appliances to run from a single outlet safely.",
        specs: ["Shatterproof Casing", "Safety Shutters", "Compact Design"],
        range: "Multi Adaptor"
      },
      {
        name: "Ceiling Rose Mount Base",
        img: "/assets/products/wiring_accessories/ceiling_rose.webp",
        desc: "Elegant round white ceiling mount base plate for standard pendant lights and electrical wiring cover.",
        specs: ["High Polycarbonate", "3-Terminal Standard", "Clean Finish"],
        range: "Ceiling Rose"
      },
      {
        name: "Batten Lamp Holder",
        img: "/assets/products/wiring_accessories/lamp_holder.webp",
        desc: "Durable brass-lined plastic batten lamp holders, providing perfect electrical contact and thermal insulation.",
        specs: ["Brass Contacts", "B22/E27 Base compatibility", "High Temperature Rating"],
        range: "Lamp Holder"
      },
      {
        name: "Surge Protected Extension Socket",
        img: "/assets/products/wiring_accessories/extension_socket.webp",
        desc: "Premium extension cord reels and boards with surge protectors and illuminated power indicators.",
        specs: ["Surge Protection", "Individually Switched", "Overload Protection"],
        range: "Extension Socket"
      },
      {
        name: "Heavy Duty Cable Reel",
        img: "/assets/products/wiring_accessories/cable_reel.webp",
        desc: "Heavy-duty outdoor extension cable reels on a metal stand with integrated thermal cut-out switch.",
        specs: ["Heavy Duty Cable", "Metal Frame stand", "Thermal Trip Switch"],
        range: "Cable Reel"
      },
      {
        name: "Compact Cassette Reel",
        img: "/assets/products/wiring_accessories/cassette_reel.webp",
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
        img: "/assets/products/cable_management/trunking.webp",
        desc: "Clean white PVC self-adhesive trunking channels, hiding surface-run cables with a tidy aesthetic.",
        specs: ["Self-Adhesive option", "Strong Snap Lid", "Fire Resistant PVC"],
        range: "Trunking"
      },
      {
        name: "GI Conduits (Galvanized Iron)",
        img: "/assets/products/cable_management/gi_conduits.webp",
        desc: "Galvanized Iron conduit pipes providing heavy-duty mechanical shielding for high-risk industrial environments.",
        specs: ["Heavy Zinc Coating", "Class 4 Corrosion protection", "Threaded Joints"],
        range: "GI Conduits"
      },
      {
        name: "PVC Conduits (Rigid)",
        img: "/assets/products/cable_management/pvc_conduits.webp",
        desc: "High-impact rigid PVC conduit pipes for safe electrical cabling routing inside concrete walls.",
        specs: ["High Impact Strength", "Easy Cold Bending", "Self-Extinguishing"],
        range: "PVC Conduits"
      },
      {
        name: "Flexible Corrugated Conduits",
        img: "/assets/products/cable_management/flexible_conduits.webp",
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
        img: "/assets/product_cables_new.webp",
        desc: "High conductivity copper wire core with heat resistant flame-retardant PVC outer sleeve.",
        specs: ["99.9% Pure Copper Core", "Flame Retardant PVC", "Low Smoke Halogen Free Option"],
        range: "Lugs"
      },
      {
        name: "Pure Copper Crimping Cable Lugs",
        img: "/assets/products/cable_termination/lug.webp",
        desc: "Heavy-duty pure copper crimping cable lugs, guaranteeing solid electrical conductivity for power cables.",
        specs: ["99.9% Pure Copper", "Tin-Plated Finish", "Heavy Duty Barrel"],
        range: "Lugs"
      },
      {
        name: "Nylon and Brass Cable Glands",
        img: "/assets/products/cable_termination/gland.webp",
        desc: "Nylon and brass cable glands providing mechanical strain relief and IP68 dust-waterproof seals for panels.",
        specs: ["IP68 Waterproof", "Strain Relief", "Brass/Nylon Options"],
        range: "Gland"
      },
      {
        name: "Tubular Copper Ferrules",
        img: "/assets/products/cable_termination/ferrule.webp",
        desc: "Tubular copper ferrule sleeves for reliable electrical splicing and crimping connections.",
        specs: ["Tinned Copper", "Solid Crimping joints", "BS Standard"],
        range: "Ferrule"
      },
      {
        name: "Insulated Terminal Pin & Ring Connectors",
        img: "/assets/products/cable_termination/insulated_terminals.webp",
        desc: "Color-coded insulated pin, ring, and spade terminal connectors, preventing short circuits and flashovers.",
        specs: ["Color Coded Sizes", "PVC Insulated sleeves", "High Conductivity Brass"],
        range: "Insulated Terminals"
      }
    ]
  },
  {
    id: "ventilation",
    name: "Air & Ventilation",
    items: [
      {
        name: "BLIT 24 Industrial Stand Fan",
        img: "/assets/products/ventilation/industrial_stand_fan.webp",
        desc: "High velocity 24-inch industrial stand fan with heavy duty cross iron base, adjustable height, and 3-speed control.",
        specs: ["24-Inch Fan Blade", "100% Copper Wire Motor", "Heavy Duty Cross Iron Base"],
        range: "Industrial Stand Fan"
      },
      {
        name: "BLIT 26 Industrial Stand Fan",
        img: "/assets/products/ventilation/industrial_stand_fan.webp",
        desc: "Professional grade 26-inch industrial pedestal fan with premium chrome finish grills and high throughput aerodynamically balanced blades.",
        specs: ["26-Inch Blade Diameter", "Balanced Aluminum Blades", "Height Adjustable Pedestal"],
        range: "Industrial Stand Fan"
      },
      {
        name: "BLIT 39 Industrial Stand Fan",
        img: "/assets/products/ventilation/industrial_stand_fan.webp",
        desc: "Large scale 39-inch industrial stand fan designed for high volume air circulation in warehouses, factories, and outdoor venues.",
        specs: ["Super-sized 39-Inch Blade", "Cast Iron Pedestal Base", "Thermo-Protected Motor"],
        range: "Industrial Stand Fan"
      },
      {
        name: "BLIT 24 Industrial Wall Fan",
        img: "/assets/products/ventilation/industrial_wall_fan.webp",
        desc: "Space-saving 24-inch wall-mounted industrial bracket fan with smooth 90-degree oscillation and heavy-duty steel wall arm.",
        specs: ["24-Inch Wall Mount", "Pull Cord Speed Control", "90-Degree Oscillation Sweep"],
        range: "Industrial Wall Fan"
      },
      {
        name: "BLIT 26 Industrial Wall Fan",
        img: "/assets/products/ventilation/industrial_wall_fan.webp",
        desc: "High efficiency 26-inch industrial wall-mount fan, featuring whisper-quiet high efficiency blades and solid concrete mounting bracket.",
        specs: ["26-Inch Steel Bracket Fan", "Reinforced Mesh Cage Safety", "Maintenance-Free Bearings"],
        range: "Industrial Wall Fan"
      },
      {
        name: "BLIT 39 Industrial Wall Fan",
        img: "/assets/products/ventilation/industrial_wall_fan.webp",
        desc: "Ultra-heavy-duty 39-inch industrial wall fan for cooling large commercial workshops and agricultural environments.",
        specs: ["39-Inch Large Bracket Fan", "Double Reinforced Wall Mount", "Multi-Speed Pull Switch Control"],
        range: "Industrial Wall Fan"
      }
    ]
  },
  {
    id: "insect_killer",
    name: "Insect Killer",
    items: [
      {
        name: "Elite Series Insect Killer",
        img: "/assets/products/insect_killer/elite_series.webp",
        desc: "Premium electric insect killer with professional high-voltage transformer grid and UV attraction light tubes.",
        specs: ["High Voltage Kill Grid", "Dual UV Attraction Tubes", "Wall, Ceiling or Free-stand Mount"],
        range: "Elite Series"
      },
      {
        name: "Prime Series Insect Killer",
        img: "/assets/products/insect_killer/prime_series.webp",
        desc: "Efficient commercial-grade electric insect killer with protective safety mesh outer frame and slide-out cleaning tray.",
        specs: ["Outer Protective Mesh Cage", "Energy-saving UV Lamps", "Easy Clean Removable Tray"],
        range: "Prime Series"
      }
    ]
  },

  {
    id: "installation_boxes",
    name: "Installation Boxes",
    items: [
      {
        name: "UV Stabilized Terminal Enclosure Box",
        img: "/assets/products/weatherproof/enclosure_box.webp",
        desc: "Durable terminal enclosure boxes with knockouts, perfect for outdoor connection joints and junction housings.",
        specs: ["UV Stabilized", "Impact Resistant", "Gasket Sealed"],
        range: "Enclosure Box"
      },
      {
        name: "Metal Knockout Junction Box",
        img: "/assets/products/weatherproof/enclosure_box.webp",
        desc: "Galvanized steel junction box with multiple knockouts for standard electrical conduits and cabling.",
        specs: ["Galvanized Steel", "20mm/25mm Knockouts", "Earth Terminal Included"],
        range: "Metal Boxes"
      }
    ]
  }
];
