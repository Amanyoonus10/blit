import os, sys, shutil, re
from PIL import Image
from fpdf import FPDF

# Ensure target directories exist
for folder in ['assets/datasheets', 'public/assets/datasheets', 'dist/assets/datasheets', '/tmp/blit_ds_thumbs']:
    os.makedirs(folder, exist_ok=True)

def sanitize_slug(name):
    clean = re.sub(r'[^a-zA-Z0-9_\- ]', '', name)
    clean = clean.replace(' ', '_').replace('-', '_')
    while '__' in clean:
        clean = clean.replace('__', '_')
    return clean.strip('_')

def prepare_image(src_path):
    if not os.path.exists(src_path):
        return None
    thumb_name = os.path.splitext(os.path.basename(src_path))[0] + '_ds.png'
    out_path = os.path.join('/tmp/blit_ds_thumbs', thumb_name)
    with Image.open(src_path) as img:
        img = img.convert('RGBA')
        bg = Image.new('RGB', img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[3])
        bg.save(out_path, 'PNG', quality=95)
    return out_path

class BLITDatasheetPDF(FPDF):
    def __init__(self, product, category):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.product = product
        self.category = category
        self.set_auto_page_break(auto=False)

    def header(self):
        # Top Red Accent Bar
        self.set_fill_color(138, 11, 14) # Primary Red #8A0B0E
        self.rect(0, 0, 210, 5, 'F')
        
        # Header Brand
        self.set_font('Helvetica', 'B', 15)
        self.set_text_color(138, 11, 14)
        self.set_xy(14, 9)
        self.cell(65, 7, 'BLIT ELECTRICAL')
        
        self.set_font('Helvetica', '', 8)
        self.set_text_color(100, 116, 139)
        self.set_xy(14, 15)
        self.cell(80, 4, 'British Standard Electrical Accessories & Industrial Equipment')
        
        # Header Right - Document Reference
        self.set_font('Helvetica', 'B', 9)
        self.set_text_color(30, 41, 59)
        self.set_xy(110, 9)
        self.cell(86, 5, 'TECHNICAL SPECIFICATION SHEET', align='R')
        
        self.set_font('Helvetica', '', 7.5)
        self.set_text_color(100, 116, 139)
        self.set_xy(110, 14.5)
        self.cell(86, 4, 'Doc Ref: BLIT-TDS-2026 | British Standard Specification', align='R')
        
        # Divider Line
        self.set_draw_color(226, 232, 240)
        self.line(14, 21, 196, 21)

    def footer(self):
        self.set_y(-14)
        self.set_draw_color(226, 232, 240)
        self.line(14, 283, 196, 283)
        
        self.set_font('Helvetica', 'B', 7.5)
        self.set_text_color(100, 116, 139)
        self.set_xy(14, 285)
        self.cell(90, 4, 'BLIT Electrical Hardware | www.blitelectric.com')
        
        self.set_font('Helvetica', '', 7.5)
        self.set_text_color(148, 163, 184)
        self.set_xy(110, 285)
        self.cell(86, 4, 'Technical Inquiries: info@blit.com  |  Official Specification', align='R')

ALL_DATASHEETS = [
    # 1. Ventilation
    {
        "category": "Air & Ventilation",
        "name": "BLIT Industrial Stand Fan – 3 Blade",
        "models": "BT100 – 24\" | BT102 – 26\" | BT101 – 30\"",
        "img": "assets/products/ventilation/industrial_stand_fan.webp",
        "desc": "Heavy-duty industrial stand fan engineered for powerful air circulation, dependable performance, and robust commercial ventilation.",
        "overview": "The BLIT Industrial Stand Fan is engineered to deliver high-velocity air circulation across demanding commercial, industrial, and workshop environments. Powered by a high-efficiency copper-wound motor and balanced three-blade design, it ensures continuous, heavy-duty airflow. Its sturdy telescopic pedestal provides adjustable height positioning with smooth wide oscillation.",
        "keyFeatures": [
            "Copper-Wound Motor",
            "Heavy-Duty Construction",
            "Three-Blade Airflow Design",
            "Adjustable Height & Three-Speed Control"
        ],
        "specs_table": [
            ("Model Designation", "BT100 (24\" / 600mm) | BT102 (26\" / 650mm) | BT101 (30\" / 750mm)"),
            ("Operating Voltage / Frequency", "220-240V ~ 50/60 Hz (Single Phase AC)"),
            ("Motor Specification", "100% Pure Copper-Wound Industrial Motor with Thermal Protection"),
            ("Fan Blade Configuration", "3-Blade Precision-Balanced High-Velocity Metal Blades"),
            ("Pedestal & Base", "Heavy Cast-Iron / Weighted Base with Anti-Vibration Dampening"),
            ("Speed & Height Adjustment", "3-Speed Heavy-Duty Rotary Switch | Telescopic Height Adjustment"),
            ("Safety Guard & Material", "Reinforced Close-Mesh Steel Wire Guard with Anti-Corrosion Coating"),
            ("Recommended Applications", "Commercial Workshops, Logistics Centers, Warehouses, Assembly Halls")
        ]
    },
    {
        "category": "Air & Ventilation",
        "name": "BLIT Industrial Wall Fan – 3 Blade",
        "models": "BT110 – 24\" | BT108 – 26\" | BT109 – 30\"",
        "img": "assets/products/ventilation/industrial_wall_fan.webp",
        "desc": "Heavy-duty wall-mounted industrial fan designed for efficient air distribution, space-saving installation, and continuous industrial operation.",
        "overview": "The BLIT Industrial Wall Fan is designed to deliver powerful air circulation while saving floor space in busy environments. Featuring a high-torque copper motor and three balanced metal blades, the fan provides uniform air distribution with 90° smooth oscillation. Built with a rigid steel wall bracket and vibration-damped anchors for maximum safety.",
        "keyFeatures": [
            "Copper-Wound Motor",
            "Heavy-Duty Construction",
            "Three-Blade Airflow Design",
            "Oscillating & Space-Saving Design"
        ],
        "specs_table": [
            ("Model Designation", "BT110 (24\" / 600mm) | BT108 (26\" / 650mm) | BT109 (30\" / 750mm)"),
            ("Operating Voltage / Frequency", "220-240V ~ 50/60 Hz (Single Phase AC)"),
            ("Motor Specification", "100% Pure Copper-Wound High-Torque Motor"),
            ("Fan Blade Configuration", "3-Blade Aerodynamically Balanced High-Flow Metal Blades"),
            ("Wall Mounting Bracket", "Rigid Heavy-Duty Steel Wall Bracket with Anti-Vibration Bushings"),
            ("Speed Control & Oscillation", "3-Speed Selection with 90° Smooth Wide-Angle Automatic Oscillation"),
            ("Safety Guard", "Close-Pitch Powder-Coated Industrial Steel Mesh Guard"),
            ("Recommended Applications", "Factories, Warehouses, Production Lines, Commercial Kitchens")
        ]
    },
    {
        "category": "Air & Ventilation",
        "name": "BLIT Heavy-Duty Industrial Stand Fan – 2 Blade",
        "models": "BT271 – 24\" | BT273 – 30\"",
        "img": "assets/products/ventilation/industrial_stand_fan_2blade.webp",
        "desc": "High-performance industrial stand fan featuring a heavy-duty two-blade design for powerful airflow and dependable operation.",
        "overview": "The BLIT Heavy-Duty Industrial Stand Fan is developed for demanding environments requiring powerful airflow and durable construction. Featuring a distinctive two-blade aerodynamic configuration and copper-wound motor, the range provides maximum air throwing distance across workshops, warehouses, and manufacturing facilities.",
        "keyFeatures": [
            "Copper-Wound Motor",
            "Heavy-Duty Construction",
            "High-Airflow Two-Blade Design",
            "Stable & Adjustable Pedestal Stand"
        ],
        "specs_table": [
            ("Model Designation", "BT271 (24\" / 600mm) | BT273 (30\" / 750mm)"),
            ("Operating Voltage / Frequency", "220-240V ~ 50/60 Hz (Single Phase AC)"),
            ("Motor Technology", "100% Pure Copper-Wound Heavy-Duty Industrial Motor"),
            ("Blade Configuration", "2-Blade Aerodynamic High-Airflow Metal Blade Profile"),
            ("Pedestal & Base", "Telescopic Steel Pole with Heavy-Duty Cast Base (Adjustable Height)"),
            ("Speed Control & Oscillation", "3-Speed Heavy-Duty Switch with Smooth Wide Oscillation"),
            ("Safety Guard", "High-Density Industrial Steel Grille with Protective Epoxy Coating"),
            ("Recommended Applications", "Manufacturing Facilities, Workshops, Warehouses, Sports Complexes")
        ]
    },
    {
        "category": "Air & Ventilation",
        "name": "BLIT Heavy-Duty Industrial Wall Fan – 2 Blade",
        "models": "BT275 – 24\" | BT277 – 30\"",
        "img": "assets/products/ventilation/industrial_wall_fan_2blade.webp",
        "desc": "Heavy-duty wall-mounted industrial fan combining powerful two-blade airflow with durable construction and space-efficient installation.",
        "overview": "The BLIT Heavy-Duty Industrial Wall Fan delivers powerful air circulation through a robust two-blade configuration. Its heavy-duty wall-mounted bracket provides rigid installation without occupying floor space, making it ideal for environments where space utilisation and ventilation throughput are essential.",
        "keyFeatures": [
            "Copper-Wound Motor",
            "Heavy-Duty Construction",
            "High-Airflow Two-Blade Design",
            "Space-Saving Wall-Mounted Design"
        ],
        "specs_table": [
            ("Model Designation", "BT275 (24\" / 600mm) | BT277 (30\" / 750mm)"),
            ("Operating Voltage / Frequency", "220-240V ~ 50/60 Hz (Single Phase AC)"),
            ("Motor Technology", "100% Pure Copper-Wound Industrial Motor"),
            ("Fan Blade Configuration", "Aerodynamically Balanced 2-Blade High-Velocity Metal Profile"),
            ("Mounting Assembly", "Heavy-Duty Rigid Wall Bracket with Vibration-Damped Anchors"),
            ("Speed Control & Oscillation", "3-Speed Selection with Smooth Wide-Angle Automatic Oscillation"),
            ("Safety Guard & Material", "Reinforced Close-Mesh Steel Wire Guard with Anti-Corrosion Coating"),
            ("Recommended Applications", "Workshops, Factories, Warehouses, Logistics Bays, Commercial Kitchens")
        ]
    },
    {
        "category": "Air & Ventilation",
        "name": "BLIT Mist Fan Series",
        "models": "BT155 – 24\" | BT156 – 26\"",
        "img": "assets/products/ventilation/mist_fan.webp",
        "desc": "Heavy-duty industrial mist fan combining powerful airflow with fine mist cooling for effective temperature control and enhanced comfort.",
        "overview": "The BLIT Mist Fan Series is designed to deliver effective cooling comfort through a combination of powerful air circulation and centrifugal water mist dispersion. Equipped with a sealed copper-wound motor and adjustable mist regulator, the fan provides evaporative temperature reduction across large open spaces.",
        "keyFeatures": [
            "Copper-Wound Motor",
            "Fine Mist Cooling Technology",
            "Adjustable Mist Output",
            "Stand & Wall-Mounted Options"
        ],
        "specs_table": [
            ("Model Designation", "BT155 (24\" / 600mm) | BT156 (26\" / 650mm)"),
            ("Operating Voltage / Frequency", "220-240V ~ 50/60 Hz (Single Phase AC)"),
            ("Cooling Principle", "Centrifugal Ultra-Fine Water Atomiser (No Clogging Nozzles)"),
            ("Motor Specification", "Sealed Water-Resistant Copper-Wound Motor"),
            ("Water Reservoir Capacity", "High-Capacity Heavy-Duty Integrated Water Tank (Up to 40L)"),
            ("Regulation & Control", "Adjustable Mist Output Volume & 3-Speed Airflow Adjustment"),
            ("Mobility & Base", "Heavy-Duty Pedestal Stand with Smooth Locking Swivel Castors"),
            ("Recommended Applications", "Outdoor Patios, Event Venues, Greenhouses, Commercial Terraces, Workshops")
        ]
    },
    {
        "category": "Air & Ventilation",
        "name": "BLIT Super Duty Metal Exhaust Fan",
        "models": "BT121 – 12\" | BT122 – 16\" | BT123 – 18\" | BT124 – 24\"",
        "img": "assets/products/ventilation/metal_exhaust_fan.webp",
        "desc": "Heavy-duty metal exhaust fan engineered for powerful air extraction, efficient ventilation, and reliable industrial performance.",
        "overview": "The BLIT Super Duty Metal Exhaust Fan delivers high-volume air extraction and dependable ventilation across demanding commercial and industrial settings. Featuring robust galvanised steel construction and high-efficiency ball-bearing copper motor, it rapidly extracts heat, smoke, and stale air.",
        "keyFeatures": [
            "Copper-Wound Motor",
            "Heavy-Duty Metal Construction",
            "Powerful Air Extraction",
            "Robust Industrial Fan Blade Design"
        ],
        "specs_table": [
            ("Model Designation", "BT121 (12\") | BT122 (16\") | BT123 (18\") | BT124 (24\")"),
            ("Operating Voltage / Frequency", "220-240V ~ 50/60 Hz (Single Phase AC)"),
            ("Motor Specification", "Ball-Bearing Sealed 100% Copper-Wound Motor"),
            ("Blade Impeller", "High-Capacity Pressed Steel Impeller Blades"),
            ("Shutter & Louvers", "Automatic Gravity Backdraught Louvers (Airflow Activated)"),
            ("Housing Material", "Heavy-Gauge Galvanised Steel Frame with Anti-Corrosion Epoxy Coating"),
            ("Ingress Protection", "IP44 Dust and Splash Resistant Motor Housing"),
            ("Recommended Applications", "Commercial Kitchens, Chemical Stores, Warehouses, Workshops, Utility Rooms")
        ]
    },

    # 2. Wiring Accessories
    {
        "category": "Wiring Accessories",
        "name": "BLIT Cable Reel",
        "img": "assets/products/wiring_accessories/cable_reel.webp",
        "desc": "Durable cable reels designed for convenient power distribution, efficient cable management, and dependable performance.",
        "overview": "BLIT Cable Reels provide organised, portable electrical power access across residential, commercial, and professional worksites. Combining durable construction with practical winding functionality, it allows cables to be extended smoothly when needed and stored securely after use.",
        "keyFeatures": [
            "Durable Construction",
            "Convenient Cable Winding",
            "Portable Power Access",
            "Organised Cable Storage"
        ],
        "specs_table": [
            ("Product Series", "BLIT Professional Cable Reel Series"),
            ("Socket Configuration", "4x 13A British Standard Sockets (BS 1363) with Safety Shutters"),
            ("Voltage & Current Rating", "230-250V~ | 13A Maximum Rated Current (3120W Max)"),
            ("Cable Specification", "Heavy-Duty 3-Core Flexible Copper Conductor (BS 6500 Approved)"),
            ("Safety Features", "Integrated Thermal Cut-Out Trip Switch & Neon Power Indicator"),
            ("Drum & Frame Construction", "High-Impact Engineering Polypropylene Drum with Steel Tubular Stand"),
            ("Handle & Cable Guide", "Ergonomic Insulated Grip Handle with Smooth Cable Guide System"),
            ("Recommended Applications", "Construction Worksites, Mobile Workshops, Events, Maintenance Teams")
        ]
    },
    {
        "category": "Wiring Accessories",
        "name": "BLIT Cassette Reel",
        "img": "assets/products/wiring_accessories/cassette_reel.webp",
        "desc": "Compact cassette cable reels designed for convenient power access, organised cable storage, and practical everyday use.",
        "overview": "BLIT Cassette Reels provide convenient electrical extension through a compact, space-saving format. Combining a fully enclosed ABS housing with smooth internal cable retraction, the range offers an accessible power extension solution for residential, office, and commercial environments.",
        "keyFeatures": [
            "Compact Cassette Design",
            "Convenient Cable Winding",
            "Portable & Space-Saving",
            "Organised Cable Storage"
        ],
        "specs_table": [
            ("Product Series", "BLIT Enclosed Cassette Cable Reel Series"),
            ("Socket Configuration", "4x 13A British Standard Sockets (BS 1363)"),
            ("Voltage & Current Rating", "230-250V~ | 13A Maximum Total Current Rating"),
            ("Enclosure Material", "High-Impact Shock-Resistant Virgin ABS Body"),
            ("Cable Specification", "Flexible 3-Core PVC Insulated Copper Cord"),
            ("Safety Protection", "Built-In Reset Thermal Overload Switch & Shuttered Outlets"),
            ("Winding Mechanism", "Recessed Ergonomic Flush-Fit Hand Crank Winder"),
            ("Recommended Applications", "Home Offices, Audio-Visual Systems, Retail Desks, Domestic Extensions")
        ]
    },
    {
        "category": "Wiring Accessories",
        "name": "BLIT Extension Socket",
        "img": "assets/products/wiring_accessories/extension_socket.webp",
        "desc": "Versatile extension sockets designed for convenient power access, dependable electrical connections, and everyday practicality.",
        "overview": "BLIT Extension Sockets provide dependable multi-gang power distribution across residential, commercial, and professional spaces. Featuring high-conductivity copper alloy internal conductors, safety shutters, and flame-retardant housings, they ensure safe and reliable electrical throughput.",
        "keyFeatures": [
            "Multiple Socket Outlets",
            "Durable Construction",
            "Convenient Power Access",
            "Practical & Functional Design"
        ],
        "specs_table": [
            ("Product Series", "BLIT Multi-Gang Trailing Extension Sockets"),
            ("Socket Standard", "13A British Standard Outlets (BS 1363 Compliant)"),
            ("Voltage & Total Rating", "230-250V~, 13A, 3250W Maximum Total Load Capacity"),
            ("Internal Busbars", "High-Conductivity Integrated Phosphor Bronze Busbars"),
            ("Casing Material", "Flame-Retardant Polycarbonate (Self-Extinguishing Grade)"),
            ("Indicators & Switches", "Individual Neon Power Indicators with Dedicated Rocker Switches"),
            ("Safety Features", "Child Safety Shutter Mechanism on All Socket Gangs"),
            ("Recommended Applications", "Offices, Commercial Workstations, IT Centers, Entertainment Systems")
        ]
    },
    {
        "category": "Wiring Accessories",
        "name": "BLIT Multi Adaptor",
        "img": "assets/products/wiring_accessories/multi_adaptor.webp",
        "desc": "Compact multi adaptors designed for convenient power connections, practical functionality, and space-efficient operation.",
        "overview": "BLIT Multi Adaptors provide immediate expansion of single wall sockets into multiple connection points without cumbersome cords. Designed with space efficiency and electrical safety in mind, they feature flame-retardant enclosures and high-conductivity solid brass contacts.",
        "keyFeatures": [
            "Multi-Outlet Configuration",
            "Compact Plug-In Design",
            "Convenient Power Access",
            "Space-Saving Construction"
        ],
        "specs_table": [
            ("Product Series", "BLIT Direct Plug-In Multi Adaptor Series"),
            ("Socket Compatibility", "Multiple 13A British Standard Sockets (BS 1363)"),
            ("Voltage & Total Rating", "230-250V~, 13A, 3250W Maximum Total Load"),
            ("Plug Pin Configuration", "Solid Brass Fused 3-Pin Plug (BS 1363/A Standard)"),
            ("Casing Construction", "Flame-Retardant UV-Stabilised Engineering Polymer"),
            ("Safety Mechanism", "Internal Safety Shuttering on Every Gang Outlet"),
            ("Form Factor", "Low-Profile Wall-Hugger Design for Tight Spaces"),
            ("Recommended Applications", "Residential Living, Workstation Desks, Hospitality Rooms, Conference Tables")
        ]
    },

    # 3. Cable Management
    {
        "category": "Cable Management",
        "name": "BLIT Heavy-Duty PVC Trunking",
        "img": "assets/products/cable_management/trunking.webp",
        "desc": "Heavy-duty PVC trunking designed for organised cable routing, reliable protection, and clean surface installation.",
        "overview": "BLIT Heavy-Duty PVC Trunking provides clean, professional surface routing and mechanical concealment for electrical and data cables. Made from high-grade virgin uPVC with self-extinguishing fire properties and precision snap-on lids for effortless cable accessibility.",
        "keyFeatures": [
            "Heavy-Duty PVC Construction",
            "Organised Cable Routing",
            "Strong & Secure Adhesion",
            "Clean & Professional Finish"
        ],
        "specs_table": [
            ("Material Composition", "Premium Virgin Rigid uPVC (Unplasticized Polyvinyl Chloride)"),
            ("Flammability Standard", "Self-Extinguishing, UL 94 V-0 Rated (Non-Flame Propagating)"),
            ("Lid Latching Mechanism", "Precision Interlocking Snap-On Tight-Fit Lid"),
            ("Adhesive Mounting Option", "High-Bond Industrial Double-Sided Foam Tape Backing"),
            ("Operating Temperature", "-5°C to +60°C Service Temperature Range"),
            ("Standard Lengths", "2.0 Metres / 2.9 Metres Standard Industry Lengths"),
            ("Chemical Resistance", "Resistant to Acids, Alkalis, Grease, and Household Solvents"),
            ("Recommended Applications", "Commercial Offices, Surface Cable Concealment, Residential Refurbishment")
        ]
    },
    {
        "category": "Cable Management",
        "name": "BLIT Rigid PVC Conduits",
        "img": "assets/products/cable_management/pvc_conduits.webp",
        "desc": "Durable rigid PVC conduits engineered for dependable cable protection, structured wiring, and long-term durability.",
        "overview": "BLIT Rigid PVC Conduits deliver superior crush and impact resistance for concealed and surface-mounted electrical installations. Resistant to corrosion, moisture, and chemical attack, they ensure long-term conductor safety in concrete, masonry, and open runs.",
        "keyFeatures": [
            "Durable Rigid PVC Construction",
            "Reliable Cable Protection",
            "Organised Wiring Installation",
            "Multiple Size Options"
        ],
        "specs_table": [
            ("Material Composition", "High-Impact High-Density Virgin uPVC"),
            ("Impact & Crush Resistance", "Heavy-Duty Mechanical Classification (BS EN 61386-21)"),
            ("Fire Performance", "Non-Flame Propagating, Self-Extinguishing Grade"),
            ("Corrosion Resistance", "100% Rust-Proof & Inert in Concrete / Mortar Environments"),
            ("Outer Diameters", "20mm, 25mm, 32mm Outer Diameters (3.0m Standard Length)"),
            ("Bending Capability", "Cold Bending with Standard Internal Bending Springs"),
            ("Wall Structure", "Uniform Heavy-Gauge Extruded Wall Thickness"),
            ("Recommended Applications", "Concealed Wall Chasing, Concrete Floor Screeds, Exposed Surface Conduit")
        ]
    },
    {
        "category": "Cable Management",
        "name": "BLIT Heavy-Duty GI Flexible Conduits",
        "img": "assets/products/cable_management/flexible_conduits.webp",
        "desc": "Heavy-duty galvanised flexible conduits designed for flexible cable routing, mechanical protection, and demanding installations.",
        "overview": "BLIT Heavy-Duty GI Flexible Conduits are manufactured from helically-wound interlocked galvanised steel strips, offering dynamic flexibility and superior crush protection. Designed for routing cables to motors, vibrating equipment, and intricate architectural bends.",
        "keyFeatures": [
            "Heavy-Duty Galvanised Metal Construction",
            "Flexible Cable Routing",
            "Mechanical Cable Protection",
            "Multiple Size Options"
        ],
        "specs_table": [
            ("Core Material", "Helically-Wound Hot-Dip Galvanised Mild Steel Strip (Interlocked Core)"),
            ("Outer Coating", "Available in Bare Galvanised Metal or Smooth Black PVC Over-Sheath"),
            ("Mechanical Performance", "Exceptional Crush Resistance, Tensile Strength, and Impact Toughness"),
            ("Flexibility Rating", "High Dynamic Bending Flexibility for Tight-Radius Routing"),
            ("Temperature Range", "-20°C to +105°C Service Temperature"),
            ("Conduit Sizes (ID)", "16mm, 20mm, 25mm, 32mm, 40mm, 50mm Internal Diameters"),
            ("Ingress Protection", "Up to IP66 with Matched Brass Compression Glands"),
            ("Recommended Applications", "Electric Motor Terminations, Industrial Machinery, HVAC, Vibrating Feeds")
        ]
    },

    # 4. Cable Termination
    {
        "category": "Cable Termination",
        "name": "BLIT Copper Cable Lugs",
        "img": "assets/products/cable_termination/lug.webp",
        "desc": "High-conductivity copper cable lugs designed for secure crimp termination, dependable electrical throughput, and lasting durability.",
        "overview": "BLIT Copper Cable Lugs are forged from seamless 99.9% electrolytic copper tube with thick electro-tin plating to ensure maximum electrical conductivity and corrosion prevention. Features chamfered entry for quick cable insertion and a visual inspection hole.",
        "keyFeatures": [
            "High-Conductivity Copper",
            "Durable Construction",
            "Secure Crimp Termination",
            "Multiple Size Options"
        ],
        "specs_table": [
            ("Base Material", "99.9% Pure Seamless Electrolytic Copper Tube"),
            ("Surface Treatment", "Heavy Electro-Tin Plated for Oxidation Resistance (BS EN 61238)"),
            ("Conductor Entry", "Precision Chamfered Internal Bore for Smooth Wire Feeding"),
            ("Inspection Feature", "Integral Visual Inspection Hole for Verified Conductor Depth"),
            ("Conductor Range", "1.5 mm² to 630 mm² Cable Cross-Sections (Stud Holes M5 to M16)"),
            ("Crimping Compatibility", "Compatible with Hexagonal and Indent Compression Crimping Tools"),
            ("Current Rating", "Full Rated Current Capacity of Matched Copper Conductors"),
            ("Recommended Applications", "Main Switchboards, Transformers, Motor Terminals, Power Distribution")
        ]
    },
    {
        "category": "Cable Termination",
        "name": "BLIT Bimetallic Cable Lugs",
        "img": "assets/products/cable_termination/bimetallic_lug.webp",
        "desc": "Bimetallic cable lugs engineered for reliable copper-to-aluminium connections, secure crimping, and stable electrical conductivity.",
        "overview": "BLIT Bimetallic Cable Lugs are designed for joining aluminium stranded cables to copper electrical busbars. The solid friction-welded joint eliminates galvanic electrolysis and contact resistance. Barrels are pre-filled with neutral antioxidant contact paste.",
        "keyFeatures": [
            "Copper & Aluminium Construction",
            "Bimetallic Connection Design",
            "Secure Crimp Termination",
            "Multiple Size Options"
        ],
        "specs_table": [
            ("Joint Construction", "Friction-Welded Molecular Bond between Aluminium & Copper"),
            ("Palm Material", "Electrolytic Copper (99.9% Cu)"),
            ("Barrel Material", "High-Conductivity Aluminium (99.5% Al)"),
            ("Internal Compound", "Factory Pre-Filled with Neutral Antioxidant Contact Paste & Capped"),
            ("Galvanic Protection", "Prevents Electrolytic Corrosion between Dissimilar Metals"),
            ("Conductor Range", "16 mm² to 500 mm² Aluminium Conductors"),
            ("Standards Compliance", "IEC 61238-1 Class A Electrical & Mechanical Standards"),
            ("Recommended Applications", "Low & Medium Voltage Feeder Lines, Solar Inverter Substations, Main Panels")
        ]
    },
    {
        "category": "Cable Termination",
        "name": "BLIT Pin-Type Cable Lugs",
        "img": "assets/products/cable_termination/pin_lug.webp",
        "desc": "Pin-type cable lugs designed for secure terminal block connections, precise fitment, and dependable electrical contact.",
        "overview": "BLIT Pin-Type Cable Lugs provide reliable, vibration-proof terminations for screw-clamp and spring-clamp terminal blocks. Precision-manufactured from high-purity copper with serrated barrels for optimal pull-out tensile grip.",
        "keyFeatures": [
            "Pin-Type Connection Design",
            "Durable Construction",
            "Secure Crimp Termination",
            "Multiple Size Options"
        ],
        "specs_table": [
            ("Pin Material", "High-Conductivity Electrolytic Copper"),
            ("Surface Finish", "Bright Electro-Tin Plated for Oxidation Resistance"),
            ("Insulation Sleeve", "Available in Uninsulated or Colour-Coded Vinyl / Polyamide"),
            ("Barrel Interior", "Serrated Internal Bore for Enhanced Conductor Tensile Grip"),
            ("Conductor Sizes", "0.5 mm² to 95 mm² Conductor Cross-Sections"),
            ("Pin Profile", "Solid Cylindrical Pin for Contactors & Clamp Terminals"),
            ("Standards Compliance", "Conforms to DIN 46231 & British Standards"),
            ("Recommended Applications", "Control Panels, Relays, Automation PLCs, DIN Rail Terminal Blocks")
        ]
    },
    {
        "category": "Cable Termination",
        "name": "BLIT Brass Cable Glands",
        "img": "assets/products/cable_termination/gland.webp",
        "desc": "Machined brass cable glands engineered for secure cable retention, environmental sealing, and reliable mechanical anchoring.",
        "overview": "BLIT Brass Cable Glands provide mechanical cable anchoring and environmental ingress sealing for industrial enclosures. Available in A2 (unarmoured), BW (indoor armoured), and CW (outdoor weatherproof armoured) configurations.",
        "keyFeatures": [
            "Premium Brass Construction",
            "Secure Cable Entry",
            "Reliable Cable Retention",
            "Multiple Size Options"
        ],
        "specs_table": [
            ("Body Material", "Precision-Machined High-Tensile Brass (CZ121 / CW614N)"),
            ("Available Configurations", "A2 (Unarmoured) | BW (Indoor Armoured) | CW (Outdoor Weatherproof)"),
            ("Ingress Protection", "IP66 with Weatherproof Neoprene Sealing Rings"),
            ("Armor Clamping", "Conical Three-Part Armor Clamping Cone and Ring"),
            ("Thread Standards", "Metric ISO (M16 to M75) and Imperial NPT Threads"),
            ("Accessories Included", "Supplied Complete with Brass Locknut, Earth Tag, and PVC Shroud"),
            ("Standards Compliance", "BS 6121 Part 1 / EN 50262 / IEC 62444"),
            ("Recommended Applications", "Industrial Junction Boxes, Marine Enclosures, Outdoor Switchboards, Substations")
        ]
    },
    {
        "category": "Cable Termination",
        "name": "BLIT Cable Ferrules",
        "img": "assets/products/cable_termination/ferrule.webp",
        "desc": "Precision-formed cable ferrules designed for secure wire end termination, organized conductor strands, and reliable connections.",
        "overview": "BLIT Cable Ferrules consolidate multi-stranded flexible copper conductors into durable solid pins, preventing wire splaying, strand breakage, and short circuits under screw-clamp terminals.",
        "keyFeatures": [
            "Precision-Formed Construction",
            "Secure Crimp Termination",
            "Organised Conductor Strands",
            "Multiple Size Options"
        ],
        "specs_table": [
            ("Tube Material", "High-Purity Seamless Copper Tube, Bright Tin-Plated"),
            ("Insulation Collar", "Halogen-Free Flame-Retardant Polypropylene (DIN 46228-4)"),
            ("Wire Range", "0.5 mm² to 50 mm² (Single Entry & Twin Conductor Variants)"),
            ("Termination Function", "Consolidates Stranded Wires, Prevents Fraying & High Resistance"),
            ("Temperature Rating", "Continuous Operating Range up to 105°C"),
            ("Connection Integrity", "Forms Gas-Tight High-Conductivity Crimp Joint"),
            ("Standards Compliance", "DIN 46228 Part 4 / UL Standards"),
            ("Recommended Applications", "Industrial Control Enclosures, PLC Wiring, Switchgear Terminal Blocks")
        ]
    },

    # 5. Insect Killers
    {
        "category": "Insect Killer",
        "name": "BLIT Elite Series Insect Killer",
        "img": "assets/products/insect_killer/elite_series.webp",
        "desc": "Durable electronic insect killer combining effective UV insect attraction technology with versatile mounting and easy maintenance.",
        "overview": "The BLIT Elite Series Insect Killer provides reliable insect management across residential, commercial, and professional indoor environments. Featuring dual UV attraction tubes, a high-voltage discharge grid, and a slide-out catchment tray for effortless hygiene maintenance.",
        "keyFeatures": [
            "Durable Construction",
            "UV Insect Attraction Technology",
            "Versatile Mounting Options",
            "Removable Collection Tray"
        ],
        "specs_table": [
            ("Product Series", "BLIT Elite Series Electronic Insect Killer"),
            ("UV Attraction Technology", "Dual High-Efficiency BL368 UVA Tubes (365nm Peak Wavelength)"),
            ("High-Voltage Discharge Grid", "2200V - 2500V Heavy-Duty Electrocution Grid"),
            ("Enclosure Construction", "Flame-Retardant ABS Side Housings with Steel Finger Guards"),
            ("Catchment System", "Slide-Out Washable Bottom Debris Collection Tray"),
            ("Mounting Configurations", "Ceiling Suspension (Chain Included), Wall-Mounted, or Free-Standing"),
            ("Electrical Rating", "220-240V ~ 50/60 Hz (Low Energy 20W - 40W Consumption)"),
            ("Recommended Applications", "Restaurants, Bakeries, Food Prep Areas, Supermarkets, Domestic Spaces")
        ]
    },
    {
        "category": "Insect Killer",
        "name": "BLIT Prime Series Insect Killer",
        "img": "assets/products/insect_killer/prime_series.webp",
        "desc": "Premium aluminium-body insect killer featuring a wide-open grille design and effective UV insect attraction technology.",
        "overview": "The BLIT Prime Series Insect Killer features a commercial-grade satin aluminium body with a 360° wide-open grille for maximum UV attraction dispersion. Engineered for demanding commercial kitchens, food processing facilities, and hospitality venues.",
        "keyFeatures": [
            "Premium Aluminium Body",
            "UV Insect Attraction Technology",
            "Versatile Mounting Options",
            "Removable Collection Tray"
        ],
        "specs_table": [
            ("Product Series", "BLIT Prime Series Architectural Aluminium Insect Control"),
            ("Casing Material", "Commercial-Grade Anodised Satin-Finish Aluminium Alloy Body"),
            ("Grille Architecture", "360° Wide-Open Grille Design for Maximum Attraction Coverage"),
            ("UV Lamps", "2x 15W / 2x 20W High-Intensity Shatterproof UVA Fluorescent Tubes"),
            ("High-Voltage Grid", "2500V Heavy-Duty Zinc-Plated Rust-Proof Electrocution Grid"),
            ("Safety Standards", "Conforms to CE, British Safety Directives & RoHS Regulations"),
            ("Maintenance & Cleaning", "Tool-Free Slide-Out Heavy-Duty Removable Collection Tray"),
            ("Recommended Applications", "Commercial Kitchens, Food Processing Plants, Hospitality, Warehouses")
        ]
    },

    # 6. Installation Boxes
    {
        "category": "Installation Boxes",
        "name": "BLIT Waterproof Enclosure Box With Knob",
        "availableColours": "White | Grey",
        "img": "assets/products/installation_boxes/enclosure_box_with_knob.webp",
        "desc": "Durable waterproof enclosure box with quick-release knobs for secure, weatherproof protection and easy component access.",
        "overview": "The BLIT Waterproof Enclosure Box With Knob provides IP65 dust and moisture protection for electrical connections and modular controls. Features quick-release locking knobs for tool-free cover removal and seamless formed polyurethane sealing gaskets.",
        "keyFeatures": [
            "Durable ABS Construction",
            "Dust & Moisture Protection",
            "Convenient Cable Entry",
            "Multiple Sizes & Colour Options"
        ],
        "specs_table": [
            ("Enclosure Material", "High-Impact Shock-Resistant Virgin ABS (UV-Stabilised Grade)"),
            ("Ingress Protection Rating", "IP65 Rated (Dust-Tight and Protected Against Water Jets)"),
            ("Fastening Mechanism", "Ergonomic Quarter-Turn Quick-Release Locking Knobs"),
            ("Sealing Gasket", "Continuous Formed-in-Place Polyurethane (PU) Elastic Foam Gasket"),
            ("Cable Knockouts", "Metric Pre-Scored Knockouts on All Four Enclosure Walls"),
            ("Operating Temperature", "-25°C to +85°C Ambient Service Temperature"),
            ("Available Colours", "Clean Alpine White | Industrial Light Grey (RAL 7035)"),
            ("Recommended Applications", "Outdoor Lighting Junctions, HVAC Relays, Sensor Housings, Irrigation")
        ]
    },
    {
        "category": "Installation Boxes",
        "name": "BLIT Waterproof Enclosure Box Without Knob",
        "availableColours": "White | Grey",
        "img": "assets/products/installation_boxes/enclosure_box_without_knob.webp",
        "desc": "High-durability waterproof enclosure box with a clean flush design, providing reliable environmental protection for electrical connections.",
        "overview": "The BLIT Waterproof Enclosure Box Without Knob offers tamper-resistant IP65 protection for sensitive electrical and automation equipment. Features flush stainless steel captive screws, heavy shock resistance (IK08), and moulded internal bosses for DIN rails.",
        "keyFeatures": [
            "Durable ABS Construction",
            "Dust & Moisture Protection",
            "Clean Exterior Design",
            "Multiple Sizes & Colour Options"
        ],
        "specs_table": [
            ("Enclosure Material", "Heavy-Gauge High-Impact Virgin ABS Body & Lid"),
            ("Ingress Protection Rating", "IP65 Rated (Dust-Tight & Water-Jet Proof)"),
            ("Cover Fastening", "Flush Stainless Steel Captive Screws (Tamper-Resistant Seal)"),
            ("Sealing Gasket", "Continuous Neoprene Rubber Elastic Gasket in Lid Recess"),
            ("Internal Mounting", "Moulded-in Internal Bosses for DIN Rails & Component Mounting"),
            ("Mechanical Resistance", "IK08 High Mechanical Impact Protection Rating"),
            ("Available Colours", "Clean Alpine White | Industrial Light Grey (RAL 7035)"),
            ("Recommended Applications", "Concealed Outdoor Splices, Security CCTV Junctions, Power Distribution")
        ]
    }
]

def draw_checkmark(pdf, x, y, size=3.2):
    pdf.set_draw_color(138, 11, 14)
    pdf.set_line_width(0.6)
    pdf.line(x, y + size * 0.5, x + size * 0.4, y + size)
    pdf.line(x + size * 0.4, y + size, x + size, y)
    pdf.set_line_width(0.2)

def generate_pdf_for_product(p):
    pdf = BLITDatasheetPDF(p, p['category'])
    pdf.add_page()
    
    # Category badge
    pdf.set_xy(14, 24)
    pdf.set_fill_color(254, 242, 242) # light red tint
    pdf.set_text_color(138, 11, 14)
    pdf.set_font('Helvetica', 'B', 8)
    cat_tag = f"  {p['category'].upper()}  "
    pdf.cell(len(cat_tag) * 2.2, 5, cat_tag, fill=True)
    
    # Title
    pdf.set_xy(14, 30)
    pdf.set_font('Helvetica', 'B', 14.5)
    pdf.set_text_color(15, 23, 42)
    name_clean = p['name'].replace('–', '-').replace('—', '-')
    pdf.cell(182, 7, name_clean)
    
    cur_y = 37
    # Models or Colours line
    if p.get('models'):
        pdf.set_xy(14, cur_y)
        pdf.set_font('Helvetica', 'B', 8.5)
        pdf.set_text_color(138, 11, 14)
        models_clean = p['models'].replace('–', '-').replace('—', '-')
        pdf.cell(182, 4.5, f"Available Models: {models_clean}")
        cur_y += 5.5
    elif p.get('availableColours'):
        pdf.set_xy(14, cur_y)
        pdf.set_font('Helvetica', 'B', 8.5)
        pdf.set_text_color(138, 11, 14)
        pdf.cell(182, 4.5, f"Available Colours: {p['availableColours']}")
        cur_y += 5.5

    # Short Description
    pdf.set_xy(14, cur_y)
    pdf.set_font('Helvetica', 'I', 8.5)
    pdf.set_text_color(71, 85, 105)
    pdf.multi_cell(182, 4.2, p['desc'].replace('–', '-'))
    
    mid_y = pdf.get_y() + 3
    
    # Middle Block: Left = Product Image (Box), Right = Key Features Card
    img_box_w = 62
    img_box_h = 62
    
    # Image frame
    pdf.set_draw_color(226, 232, 240)
    pdf.set_fill_color(255, 255, 255)
    pdf.rect(14, mid_y, img_box_w, img_box_h, 'DF')
    
    img_path = prepare_image(p['img'])
    if img_path:
        pdf.image(img_path, 16, mid_y + 2, img_box_w - 4, img_box_h - 4)
        
    # Right Box: Key Features (X = 80, W = 116)
    pdf.set_draw_color(226, 232, 240)
    pdf.set_fill_color(248, 250, 252)
    pdf.rect(80, mid_y, 116, img_box_h, 'DF')
    
    pdf.set_xy(84, mid_y + 4)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(138, 11, 14)
    pdf.cell(108, 5, 'KEY PRODUCT FEATURES')
    
    feat_y = mid_y + 11.5
    for feat in p['keyFeatures']:
        draw_checkmark(pdf, 85, feat_y + 0.8)
        pdf.set_xy(91, feat_y)
        pdf.set_font('Helvetica', 'B', 8.5)
        pdf.set_text_color(30, 41, 59)
        pdf.cell(102, 5, f"{feat}")
        feat_y += 7.5
        
    # Extra summary note in key features box
    pdf.set_xy(84, feat_y + 1)
    pdf.set_font('Helvetica', 'I', 7.5)
    pdf.set_text_color(100, 116, 139)
    pdf.multi_cell(108, 3.8, 'Manufactured to strict British Standards, ensuring high durability, verified ratings, and dependable operation.')
    
    # Overview Section
    overview_y = mid_y + img_box_h + 4
    pdf.set_xy(14, overview_y)
    pdf.set_font('Helvetica', 'B', 9.5)
    pdf.set_text_color(138, 11, 14)
    pdf.cell(182, 5, 'PRODUCT OVERVIEW & ENGINEERING DESIGN')
    
    pdf.set_draw_color(138, 11, 14)
    pdf.line(14, overview_y + 5.5, 95, overview_y + 5.5)
    
    pdf.set_xy(14, overview_y + 7.5)
    pdf.set_font('Helvetica', '', 8)
    pdf.set_text_color(51, 65, 85)
    clean_overview = p['overview'].replace('\n\n', ' ').replace('–', '-').replace('—', '-')
    # Keep overview concise so it fits perfectly on A4
    if len(clean_overview) > 420:
        clean_overview = clean_overview[:417] + '...'
    pdf.multi_cell(182, 3.8, clean_overview)
    
    # Technical Specifications Table
    table_y = pdf.get_y() + 4
    pdf.set_xy(14, table_y)
    pdf.set_font('Helvetica', 'B', 9.5)
    pdf.set_text_color(138, 11, 14)
    pdf.cell(182, 5, 'TECHNICAL SPECIFICATIONS')
    
    pdf.set_draw_color(138, 11, 14)
    pdf.line(14, table_y + 5.5, 75, table_y + 5.5)
    
    cur_y = table_y + 8
    
    # Table Header
    pdf.set_xy(14, cur_y)
    pdf.set_fill_color(30, 41, 59) # Slate 800
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.cell(62, 5.5, '  TECHNICAL PARAMETER', fill=True)
    pdf.cell(120, 5.5, '  SPECIFICATION & RATING VALUE', fill=True)
    cur_y += 5.5
    
    pdf.set_font('Helvetica', '', 7.5)
    for idx, (label, val) in enumerate(p['specs_table']):
        if idx % 2 == 0:
            pdf.set_fill_color(248, 250, 252)
        else:
            pdf.set_fill_color(255, 255, 255)
            
        pdf.set_xy(14, cur_y)
        pdf.set_text_color(30, 41, 59)
        pdf.set_font('Helvetica', 'B', 7.5)
        pdf.cell(62, 5.2, f"  {label}", 'B', fill=True)
        
        pdf.set_font('Helvetica', '', 7.5)
        pdf.set_text_color(51, 65, 85)
        clean_val = val.replace('–', '-').replace('—', '-')
        pdf.cell(120, 5.2, f"  {clean_val}", 'B', fill=True)
        cur_y += 5.2
        
    slug = sanitize_slug(p['name'])
    filename = f"BLIT_Technical_Sheet_{slug}.pdf"
    
    primary_out = os.path.join('assets/datasheets', filename)
    public_out = os.path.join('public/assets/datasheets', filename)
    dist_out = os.path.join('dist/assets/datasheets', filename)
    
    pdf.output(primary_out)
    shutil.copy2(primary_out, public_out)
    shutil.copy2(primary_out, dist_out)
    
    print(f"Generated: {filename}")
    return filename

if __name__ == '__main__':
    print(f"Generating technical datasheets for {len(ALL_DATASHEETS)} products...")
    manifest = {}
    for item in ALL_DATASHEETS:
        fn = generate_pdf_for_product(item)
        manifest[item['name']] = f"/assets/datasheets/{fn}"
    
    print("\nDatasheet generation complete!")
    print(f"Total datasheets generated: {len(manifest)}")
