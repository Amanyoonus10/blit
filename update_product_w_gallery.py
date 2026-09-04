import re

w_section_replacement = """        <!-- Categories & Products Header -->
        <div style="text-align: center; margin-bottom: 35px;">
          <h3 style="font-size: 24px; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; color: #0F172A; margin-bottom: 10px;">W RANGE PRODUCT COLLECTION</h3>
          <p style="font-size: 14.5px; color: #64748B; max-width: 650px; margin: 0 auto 20px auto;">Browse the complete collection of classic moulded-white switches and sockets. Click any product image to zoom.</p>
          <div style="width: 44px; height: 3px; background-color: var(--primary-red); margin: 0 auto 30px auto; border-radius: 2px;"></div>
          
          <!-- Category Filter Tabs -->
          <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 8px;" id="w-gallery-filters">
            <button class="w-filter-btn active" onclick="filterWRangeProducts('all', event)" style="background: var(--primary-red); color: #FFFFFF; border: none; padding: 9px 20px; border-radius: 20px; font-size: 13px; font-weight: 700; cursor: pointer; transition: all 0.2s ease;">All Products</button>
            <button class="w-filter-btn" onclick="filterWRangeProducts('plate_switches', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Plate Switches</button>
            <button class="w-filter-btn" onclick="filterWRangeProducts('high_power', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">20A & 45A Switches</button>
            <button class="w-filter-btn" onclick="filterWRangeProducts('dimmers', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Dimmers & Fan</button>
            <button class="w-filter-btn" onclick="filterWRangeProducts('socket_outlets', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Sockets & USB</button>
            <button class="w-filter-btn" onclick="filterWRangeProducts('multi_sockets', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Multi-Function</button>
            <button class="w-filter-btn" onclick="filterWRangeProducts('fcus', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">FCUs & Blank Plates</button>
            <button class="w-filter-btn" onclick="filterWRangeProducts('data_tv', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Data & Telecom</button>
            <button class="w-filter-btn" onclick="filterWRangeProducts('bell_switches', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Bell Push</button>
          </div>
        </div>

        <!-- W Range Products Grid -->
        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 24px; margin-bottom: 60px;" id="w-products-grid">
          <!-- Populated dynamically by script -->
        </div>"""

w_script_content = """  <script>
    const UNIQUE_W_PRODUCTS = [
      { code: "W301 / W302 / W313", cat: "plate_switches", name: "1-Gang Plate Switch", desc: "10AX 250V~ 1-Gang Switch (1-Way, 2-Way, Intermediate)", size: "86 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/switches/white_range_switch_1g.webp" },
      { code: "W303 / W304", cat: "plate_switches", name: "2-Gang Plate Switch", desc: "10AX 250V~ 2-Gang Switch (1-Way & 2-Way)", size: "86 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/switches/w_range_switch_2g.webp" },
      { code: "W305 / W306", cat: "plate_switches", name: "3-Gang Plate Switch", desc: "10AX 250V~ 3-Gang Switch (1-Way & 2-Way)", size: "86 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/switches/w_range_plate_switches.webp" },
      { code: "W307 / W308", cat: "plate_switches", name: "4-Gang Plate Switch (Wide)", desc: "10AX 250V~ 4-Gang Wide Plate Switch", size: "146 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/switches/w_range_plate_switches.webp" },
      { code: "W309 / W310", cat: "plate_switches", name: "6-Gang Plate Switch (Wide)", desc: "10AX 250V~ 6-Gang Master Switch", size: "146 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/switches/w_range_plate_switches.webp" },
      
      { code: "W316 / W317 / W319", cat: "bell_switches", name: "1-Gang Bell Push Switch", desc: "10A Momentary Retractive Bell Push Switch", size: "86 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/switches/w_range_bell_switches.webp" },
      
      { code: "W324", cat: "high_power", name: "20A DP Switch + Neon", desc: "20A Double Pole Heavy Duty Isolator Switch", size: "86 x 86 mm", std: "BS EN 60669-2-1", img: "/assets/products/switches/w_range_high_power.webp" },
      { code: "W327 / W328", cat: "high_power", name: "45A DP Switch + Neon", desc: "45A Double Pole Main Isolator Switch", size: "86 x 86 mm", std: "BS EN 60669-2-1", img: "/assets/products/switches/w_range_high_power.webp" },
      { code: "W329 / W330", cat: "high_power", name: "45A DP Switch (Large Plate)", desc: "45A Large Rocker Double Pole Isolator Switch", size: "86 x 86 mm", std: "BS EN 60669-2-1", img: "/assets/products/switches/w_range_high_power.webp" },
      { code: "W331 / W332", cat: "high_power", name: "45A Cooker Control Unit + Socket", desc: "45A Cooker Switch + 13A Socket + Dual Neons", size: "146 x 86 mm", std: "BS 4177", img: "/assets/products/switches/w_range_cooker_control.webp" },
      
      { code: "W350 / W352 / W355", cat: "dimmers", name: "1-Gang Rotary Dimmer (250W-500W)", desc: "Rotary Lighting Dimmer Switch", size: "86 x 86 mm", std: "BS EN 60669-2-1", img: "/assets/products/switches/w_range_dimmers.webp" },
      { code: "W354 / W356", cat: "dimmers", name: "2-Gang Rotary Dimmer", desc: "Dual Channel Rotary Lighting Dimmer Switch", size: "86 x 86 mm", std: "BS EN 60669-2-1", img: "/assets/products/w_range/W3542_dimmer_2g_400w_2way.png" },
      { code: "W351 / W371 / W557", cat: "dimmers", name: "1-Gang Fan Speed Controller", desc: "Stepless Precision Fan Speed Controller Switch", size: "86 x 86 mm", std: "IEC 60669", img: "/assets/products/w_range/W5572_speed_switch_1000w_2way.png" },
      
      { code: "W405 / W407 / W409", cat: "socket_outlets", name: "13A Single Switched Socket", desc: "13A 1-Gang BS 1363-2 Switched Power Outlet", size: "86 x 86 mm", std: "BS 1363-2", img: "/assets/products/switches/white_range_single_socket.webp" },
      { code: "W406 / W408 / W410", cat: "socket_outlets", name: "13A Twin Switched Socket", desc: "13A 2-Gang BS 1363-2 Double Switched Socket", size: "146 x 86 mm", std: "BS 1363-2", img: "/assets/products/switches/w_range_socket_outlets.webp" },
      { code: "W503", cat: "socket_outlets", name: "Twin 13A Socket + Dual USB", desc: "Twin 13A Switched Socket + Dual USB Charger", size: "146 x 86 mm", std: "BS 1363-2 / IEC 62368", img: "/assets/products/switches/white_range_usb_twin_socket.webp" },
      { code: "W429 / W431", cat: "socket_outlets", name: "15A Round Pin Switched Socket", desc: "15A Heavy Duty BS 546 Round Pin AC Socket", size: "86 x 86 mm", std: "BS 546", img: "/assets/products/switches/w_range_socket_1g.webp" },
      
      { code: "W460 / W460N", cat: "multi_sockets", name: "10A 1-Gang Universal Multi Socket", desc: "Universal Multi-Standard Receptacle Outlet", size: "86 x 86 mm", std: "IEC 60884", img: "/assets/products/switches/w_range_multi_sockets.webp" },
      { code: "W444", cat: "multi_sockets", name: "10A 2-Gang Universal Multi Socket", desc: "Twin Universal Multi-Pin Standard Socket", size: "146 x 86 mm", std: "IEC 60884", img: "/assets/products/switches/w_range_multi_sockets.webp" },
      { code: "W445 / W446", cat: "multi_sockets", name: "10A Multi Socket + 20A Switch", desc: "Universal Multi Socket with Dedicated Switch", size: "86 x 86 mm", std: "IEC 60884", img: "/assets/products/switches/w_range_multi_sockets.webp" },
      { code: "W407M / W482", cat: "multi_sockets", name: "13A Switched Multi-Socket + Neon", desc: "13A Switched Multi-Standard Socket + Neon", size: "86 x 86 mm", std: "BS 1363 / IEC 60884", img: "/assets/products/switches/w_range_multi_sockets.webp" },
      { code: "W458", cat: "multi_sockets", name: "Dual Voltage Shaver Socket", desc: "Dual Voltage 115V/230V Shaver Outlet Unit", size: "146 x 86 mm", std: "BS EN 61558-2-5", img: "/assets/products/switches/w_range_shaver_socket.webp" },
      
      { code: "W416 / W417 / W418", cat: "fcus", name: "13A Unswitched FCU Spur", desc: "13A Fused Connection Unit (Front Fuse)", size: "86 x 86 mm", std: "BS 1363-4", img: "/assets/products/switches/w_range_fcus.webp" },
      { code: "W413 / W414 / W415", cat: "fcus", name: "13A FCU Spur + Neon", desc: "13A Fused Spur Unit with Neon Power Light", size: "86 x 86 mm", std: "BS 1363-4", img: "/assets/products/switches/w_range_fcus.webp" },
      { code: "W419 / W422", cat: "fcus", name: "13A Switched FCU + Neon", desc: "13A DP Switched FCU with Neon Indicator", size: "86 x 86 mm", std: "BS 1363-4", img: "/assets/products/switches/w_range_fcus.webp" },
      { code: "W401 / W402 / W501", cat: "fcus", name: "1-Gang & 2-Gang Blank Plates", desc: "Flush Architectural Blank Cover Plates", size: "86 x 86 mm", std: "BS 5733", img: "/assets/products/switches/w_range_fcus.webp" },
      { code: "W820 / W821", cat: "fcus", name: "20A & 45A Connection Plates", desc: "Heavy Duty Cable Outlet Connection Plates", size: "86 x 86 mm", std: "BS 5733", img: "/assets/products/switches/w_range_fcus.webp" },
      
      { code: "W166 / W432", cat: "data_tv", name: "1-Gang Satellite / TV Socket", desc: "Co-axial / Satellite TV Antenna Outlet", size: "86 x 86 mm", std: "BS 3041", img: "/assets/products/switches/w_range_data_tv.webp" },
      { code: "W438 / W439", cat: "data_tv", name: "1-Gang RJ11 Telephone Socket", desc: "Standard BT/RJ11 Telephone Wall Plate", size: "86 x 86 mm", std: "BS 6312", img: "/assets/products/switches/w_range_data_tv.webp" },
      { code: "W442 / W443", cat: "data_tv", name: "Cat6 RJ45 Gigabit Data Outlet", desc: "1-Gang & 2-Gang Gigabit Network Wall Plate", size: "86 x 86 mm", std: "TIA/EIA-568", img: "/assets/products/switches/w_range_data_tv.webp" }
    ];

    function renderWRangeProducts(filter = 'all') {
      const grid = document.getElementById('w-products-grid');
      if (!grid) return;

      const items = filter === 'all' ? UNIQUE_W_PRODUCTS : UNIQUE_W_PRODUCTS.filter(p => p.cat === filter);
      grid.innerHTML = items.map(p => `
        <div class="w-product-card-item" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 16px; padding: 20px; display: flex; flex-direction: column; justify-content: space-between; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(0,0,0,0.02);" onmouseover="this.style.transform='translateY(-5px)'; this.style.borderColor='rgba(255,26,26,0.35)'; this.style.boxShadow='0 14px 28px rgba(255,26,26,0.09)';" onmouseout="this.style.transform='none'; this.style.borderColor='#E2E8F0'; this.style.boxShadow='0 4px 15px rgba(0,0,0,0.02)';">
          
          <!-- Image Box with Click to Enlarge -->
          <div style="width: 100%; height: 190px; background: #FAFAFA; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 16px; position: relative; overflow: hidden; cursor: pointer;" onclick="openFullscreenLightbox('${p.img}')" title="Click to enlarge image">
            <span style="position: absolute; top: 10px; left: 10px; background: #0F172A; color: #FFFFFF; font-size: 11px; font-weight: 700; padding: 4px 9px; border-radius: 6px; letter-spacing: 0.5px;">${p.code}</span>
            <img src="${p.img}" alt="${p.name}" loading="lazy" style="max-width: 82%; max-height: 82%; object-fit: contain; transition: transform 0.3s ease;">
          </div>

          <!-- Product Details -->
          <div style="margin-bottom: 16px;">
            <h4 style="font-size: 16px; font-weight: 700; color: #0F172A; margin-bottom: 6px; line-height: 1.3;">${p.name}</h4>
            <p style="font-size: 13px; color: #64748B; line-height: 1.45; margin-bottom: 10px;">${p.desc}</p>
            <div style="display: flex; flex-wrap: wrap; gap: 6px;">
              <span style="background: #F1F5F9; color: #475569; font-size: 11.5px; font-weight: 600; padding: 3px 8px; border-radius: 5px;">${p.size}</span>
              <span style="background: rgba(255,26,26,0.08); color: var(--primary-red); font-size: 11.5px; font-weight: 700; padding: 3px 8px; border-radius: 5px;">${p.std}</span>
            </div>
          </div>

          <!-- Action Button -->
          <button onclick="openFullscreenLightbox('${p.img}')" style="background: #F8FAFC; border: 1px solid #E2E8F0; color: #334155; font-size: 12.5px; font-weight: 600; padding: 10px 14px; border-radius: 20px; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 6px; transition: all 0.2s ease; width: 100%;" onmouseover="this.style.background='var(--primary-red)'; this.style.color='#FFFFFF'; this.style.borderColor='var(--primary-red)';" onmouseout="this.style.background='#F8FAFC'; this.style.color='#334155'; this.style.borderColor='#E2E8F0';">
            <span>Enlarge & View Specs</span> 🔍
          </button>
        </div>
      `).join('');
    }

    function filterWRangeProducts(filterKey, e) {
      if (e) {
        const btns = document.querySelectorAll('#w-gallery-filters .w-filter-btn');
        btns.forEach(b => {
          b.style.background = '#F1F5F9';
          b.style.color = '#334155';
          b.classList.remove('active');
        });
        e.target.style.background = 'var(--primary-red)';
        e.target.style.color = '#FFFFFF';
        e.target.classList.add('active');
      }
      renderWRangeProducts(filterKey);
    }

    document.addEventListener('DOMContentLoaded', () => {
      renderWRangeProducts('all');
    });
  </script>"""

with open('/Users/amanyoonus/Desktop/Blit/product.html', 'r') as f:
    html = f.read()

# Replace the categories grid in W section
w_cat_start = html.find('<!-- Categories Header -->', html.find('id="w-catalog-section"'))
w_cat_end = html.find('<!-- Bottom Downloads & Price Support Cards -->', w_cat_start)

if w_cat_start != -1 and w_cat_end != -1:
    html = html[:w_cat_start] + w_section_replacement + '\n\n      ' + html[w_cat_end:]
    print("W section HTML updated with products grid!")

# Insert W script before UNIQUE_V_PRODUCTS script
v_script_pos = html.find('<script>\n    const UNIQUE_V_PRODUCTS')
if v_script_pos != -1:
    html = html[:v_script_pos] + w_script_content + '\n\n  ' + html[v_script_pos:]
    print("W script inserted successfully!")

with open('/Users/amanyoonus/Desktop/Blit/product.html', 'w') as f:
    f.write(html)

print("product.html updated completely for W Range!")
