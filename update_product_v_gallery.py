import re

v_section_replacement = """        <!-- Categories & Products Header -->
        <div style="text-align: center; margin-bottom: 35px;">
          <h3 style="font-size: 24px; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; color: #0F172A; margin-bottom: 10px;">V RANGE PRODUCT COLLECTION</h3>
          <p style="font-size: 14.5px; color: #64748B; max-width: 650px; margin: 0 auto 20px auto;">Browse all 33 distinct models in the luxury brushed metal collection. Click any product image to zoom.</p>
          <div style="width: 44px; height: 3px; background-color: var(--primary-red); margin: 0 auto 30px auto; border-radius: 2px;"></div>
          
          <!-- Category Filter Tabs -->
          <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 8px;" id="v-gallery-filters">
            <button class="v-filter-btn active" onclick="filterVRangeProducts('all', event)" style="background: var(--primary-red); color: #FFFFFF; border: none; padding: 9px 20px; border-radius: 20px; font-size: 13px; font-weight: 700; cursor: pointer; transition: all 0.2s ease;">All (33)</button>
            <button class="v-filter-btn" onclick="filterVRangeProducts('plate_switches', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Plate Switches (6)</button>
            <button class="v-filter-btn" onclick="filterVRangeProducts('high_power', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">20A & 45A Switches (4)</button>
            <button class="v-filter-btn" onclick="filterVRangeProducts('dimmers', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Dimmers & Fan (3)</button>
            <button class="v-filter-btn" onclick="filterVRangeProducts('socket_outlets', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Sockets & USB (4)</button>
            <button class="v-filter-btn" onclick="filterVRangeProducts('multi_sockets', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Multi-Function (7)</button>
            <button class="v-filter-btn" onclick="filterVRangeProducts('fcus', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">FCUs & Blank Plates (6)</button>
            <button class="v-filter-btn" onclick="filterVRangeProducts('data_tv', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Data & Telecom (2)</button>
            <button class="v-filter-btn" onclick="filterVRangeProducts('bell_switches', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Bell Push (1)</button>
          </div>
        </div>

        <!-- 33 Unique Products Grid (Each image shown once without duplicates) -->
        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 24px; margin-bottom: 60px;" id="v-products-grid">
          <!-- Populated dynamically by script -->
        </div>"""

v_script_replacement = """  <script>
    const UNIQUE_V_PRODUCTS = [
      { code: "BTV301 / BTV302 / BTV313", cat: "plate_switches", name: "1-Gang Plate Switch", desc: "10AX 250V~ 1-Gang Switch (1-Way, 2-Way, Intermediate)", size: "86 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/v_range/BTV301.webp" },
      { code: "BTV303 / BTV304", cat: "plate_switches", name: "2-Gang Plate Switch", desc: "10AX 250V~ 2-Gang Switch (1-Way & 2-Way)", size: "86 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/v_range/BTV303.webp" },
      { code: "BTV305 / BTV306", cat: "plate_switches", name: "3-Gang Plate Switch", desc: "10AX 250V~ 3-Gang Switch (1-Way & 2-Way)", size: "86 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/v_range/BTV305.webp" },
      { code: "BTV307", cat: "plate_switches", name: "4-Gang 1-Way Switch (Wide)", desc: "10AX 250V~ 4-Gang Wide Plate Switch", size: "146 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/v_range/BTV307.webp" },
      { code: "BTV307X", cat: "plate_switches", name: "4-Gang 2-Way Switch (Square)", desc: "10AX 250V~ 4-Gang Square Profile Switch", size: "86 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/v_range/BTV307X.webp" },
      { code: "BTV309", cat: "plate_switches", name: "6-Gang 1-Way Switch (Wide)", desc: "10AX 250V~ 6-Gang Master Switch", size: "146 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/v_range/BTV309.webp" },
      
      { code: "BTV317", cat: "bell_switches", name: "1-Gang Bell Push Switch", desc: "10A Momentary Retractive Bell Push Switch", size: "86 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/v_range/BTV317.webp" },
      
      { code: "BTV324", cat: "high_power", name: "20A DP Switch + Neon", desc: "20A Double Pole Heavy Duty Isolator Switch", size: "86 x 86 mm", std: "BS EN 60669-2-1", img: "/assets/products/v_range/BTV324.webp" },
      { code: "BTV327", cat: "high_power", name: "45A DP Switch + Neon", desc: "45A Double Pole Main Isolator Switch", size: "86 x 86 mm", std: "BS EN 60669-2-1", img: "/assets/products/v_range/BTV327.webp" },
      { code: "BTV329", cat: "high_power", name: "45A DP Switch (Large Plate)", desc: "45A Large Rocker Double Pole Isolator Switch", size: "86 x 86 mm", std: "BS EN 60669-2-1", img: "/assets/products/v_range/BTV329.webp" },
      { code: "BTV331", cat: "high_power", name: "45A Cooker Control Unit + Socket", desc: "45A Cooker Switch + 13A Socket + Dual Neons", size: "146 x 86 mm", std: "BS 4177", img: "/assets/products/v_range/BTV331.webp" },
      
      { code: "BTV350-2 / BTV355 / BTV359", cat: "dimmers", name: "1-Gang Rotary Dimmer (400W-1000W)", desc: "Rotary Dimmer Switch (400W, 500W & 1000W)", size: "86 x 86 mm", std: "BS EN 60669-2-1", img: "/assets/products/v_range/BTV350-2.webp" },
      { code: "BTV351", cat: "dimmers", name: "1-Gang 400W Fan Speed Controller", desc: "Stepless Fan Speed Controller Switch", size: "86 x 86 mm", std: "IEC 60669", img: "/assets/products/v_range/BTV351.webp" },
      { code: "BTV353-2", cat: "dimmers", name: "2-Gang 400W Rotary Dimmer", desc: "Dual Channel Rotary Lighting Dimmer Switch", size: "86 x 86 mm", std: "BS EN 60669-2-1", img: "/assets/products/v_range/BTV353-2.webp" },
      
      { code: "BTV4010B", cat: "socket_outlets", name: "13A Single Switched Socket", desc: "13A 1-Gang BS 1363-2 Switched Power Outlet", size: "86 x 86 mm", std: "BS 1363-2", img: "/assets/products/v_range/BTV4010B.webp" },
      { code: "BTV4030B", cat: "socket_outlets", name: "13A Twin Switched Socket", desc: "13A 2-Gang BS 1363-2 Double Switched Socket", size: "146 x 86 mm", std: "BS 1363-2", img: "/assets/products/v_range/BTV4030B.webp" },
      { code: "BTV4113-3.1A", cat: "socket_outlets", name: "13A Single Socket + Dual USB 3.1A", desc: "13A Switched Socket + 3.1A Fast USB Ports", size: "86 x 86 mm", std: "BS 1363-2 / IEC 62368", img: "/assets/products/v_range/BTV4113-3.1A.webp" },
      { code: "BTV4121-3.1A", cat: "socket_outlets", name: "13A Twin Socket + Dual USB 3.1A", desc: "Twin 13A Switched Socket + 3.1A Fast USB Ports", size: "146 x 86 mm", std: "BS 1363-2 / IEC 62368", img: "/assets/products/v_range/BTV4121-3.1A.webp" },
      
      { code: "BTV4243-3.1A", cat: "multi_sockets", name: "13A Multi-Socket + Dual USB 3.1A", desc: "Universal Multi-Standard Socket + 3.1A USB", size: "86 x 86 mm", std: "IEC 60884 / IEC 62368", img: "/assets/products/v_range/BTV4243-3.1A.webp" },
      { code: "BTV4250", cat: "multi_sockets", name: "2-Gang Universal Multi-Socket", desc: "Twin Universal Multi-Pin Standard Socket", size: "146 x 86 mm", std: "IEC 60884", img: "/assets/products/v_range/BTV4250.webp" },
      { code: "BTV4253-3.1A", cat: "multi_sockets", name: "2-Gang Multi-Socket + Dual USB 3.1A", desc: "Twin Multi Socket + Dual 3.1A USB Ports", size: "146 x 86 mm", std: "IEC 60884 / IEC 62368", img: "/assets/products/v_range/BTV4253-3.1A.webp" },
      { code: "BTV429", cat: "multi_sockets", name: "15A Round Pin Switched Socket", desc: "15A Heavy Duty BS 546 Round Pin AC Socket", size: "86 x 86 mm", std: "BS 546", img: "/assets/products/v_range/BTV429.webp" },
      { code: "BTV480", cat: "multi_sockets", name: "10A/13A Universal Multi-Socket", desc: "Universal Multi-Standard Receptacle Outlet", size: "86 x 86 mm", std: "IEC 60884", img: "/assets/products/v_range/BTV480.webp" },
      { code: "BTV482", cat: "multi_sockets", name: "13A Switched Multi-Socket + Neon", desc: "13A Switched Multi-Standard Socket + Neon", size: "86 x 86 mm", std: "BS 1363 / IEC 60884", img: "/assets/products/v_range/BTV482.webp" },
      { code: "BTV484", cat: "multi_sockets", name: "13A 2-Gang Switched Multi-Socket", desc: "Twin Switched Universal Multi-Standard Socket", size: "146 x 86 mm", std: "BS 1363 / IEC 60884", img: "/assets/products/v_range/BTV484.webp" },
      
      { code: "BTV416", cat: "fcus", name: "13A Fused Connection Unit (FCU)", desc: "13A Unswitched Fused Spur Connection Unit", size: "86 x 86 mm", std: "BS 1363-4", img: "/assets/products/v_range/BTV416.webp" },
      { code: "BTV422", cat: "fcus", name: "13A Switched FCU + Neon", desc: "13A DP Switched FCU with Neon Indicator", size: "86 x 86 mm", std: "BS 1363-4", img: "/assets/products/v_range/BTV422.webp" },
      { code: "BTV401", cat: "fcus", name: "1-Gang Blank Plate (86x86mm)", desc: "86 x 86 mm Flush Blank Cover Plate", size: "86 x 86 mm", std: "BS 5733", img: "/assets/products/v_range/BTV401.webp" },
      { code: "BTV402", cat: "fcus", name: "2-Gang Blank Plate (146x86mm)", desc: "146 x 86 mm Double Width Blank Cover Plate", size: "146 x 86 mm", std: "BS 5733", img: "/assets/products/v_range/BTV402.webp" },
      { code: "BTV820", cat: "fcus", name: "20A Cable Connection Plate", desc: "20A Heavy Duty Cable Outlet Connection Plate", size: "86 x 86 mm", std: "BS 5733", img: "/assets/products/v_range/BTV820.webp" },
      { code: "BTV821", cat: "fcus", name: "45A Cable Connection Plate", desc: "45A High Current Cable Outlet Plate", size: "86 x 86 mm", std: "BS 5733", img: "/assets/products/v_range/BTV821.webp" },
      
      { code: "BTV442", cat: "data_tv", name: "1-Gang RJ45 Cat6 Data Outlet", desc: "1-Port Gigabit Ethernet Cat6 Data Wall Plate", size: "86 x 86 mm", std: "TIA/EIA-568", img: "/assets/products/v_range/BTV442.webp" },
      { code: "BTV443", cat: "data_tv", name: "2-Gang RJ45 Cat6 Data Outlet", desc: "2-Port Dual Gigabit Cat6 Data Wall Plate", size: "86 x 86 mm", std: "TIA/EIA-568", img: "/assets/products/v_range/BTV443.webp" }
    ];

    function renderVRangeProducts(filter = 'all') {
      const grid = document.getElementById('v-products-grid');
      if (!grid) return;

      const items = filter === 'all' ? UNIQUE_V_PRODUCTS : UNIQUE_V_PRODUCTS.filter(p => p.cat === filter);
      grid.innerHTML = items.map(p => `
        <div class="v-product-card-item" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 16px; padding: 20px; display: flex; flex-direction: column; justify-content: space-between; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(0,0,0,0.02);" onmouseover="this.style.transform='translateY(-5px)'; this.style.borderColor='rgba(255,26,26,0.35)'; this.style.boxShadow='0 14px 28px rgba(255,26,26,0.09)';" onmouseout="this.style.transform='none'; this.style.borderColor='#E2E8F0'; this.style.boxShadow='0 4px 15px rgba(0,0,0,0.02)';">
          
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

    function filterVRangeProducts(filterKey, e) {
      if (e) {
        const btns = document.querySelectorAll('#v-gallery-filters .v-filter-btn');
        btns.forEach(b => {
          b.style.background = '#F1F5F9';
          b.style.color = '#334155';
          b.classList.remove('active');
        });
        e.target.style.background = 'var(--primary-red)';
        e.target.style.color = '#FFFFFF';
        e.target.classList.add('active');
      }
      renderVRangeProducts(filterKey);
    }

    document.addEventListener('DOMContentLoaded', () => {
      renderVRangeProducts('all');
    });
  </script>"""

with open('/Users/amanyoonus/Desktop/Blit/product.html', 'r') as f:
    html = f.read()

# Replace the categories grid in V section
cat_header_start = html.find('<!-- Categories Header -->', html.find('id="v-catalog-section"'))
cat_grid_end = html.find('<!-- Bottom Downloads & Price Support Cards -->', cat_header_start)

if cat_header_start != -1 and cat_grid_end != -1:
    html = html[:cat_header_start] + v_section_replacement + '\n\n        ' + html[cat_grid_end:]
    print("V section HTML updated with 33 unique products grid!")

# Replace the script section for V Range
v_modal_start = html.find('<script>\n    const V_MODAL_DATA = {')
if v_modal_start == -1:
    v_modal_start = html.find('<script>\n    const UNIQUE_V_PRODUCTS')

footer_start = html.find('<!-- Footer -->')
if v_modal_start != -1 and footer_start != -1:
    html = html[:v_modal_start] + v_script_replacement + '\n\n' + html[footer_start:]
    print("V script updated successfully!")

with open('/Users/amanyoonus/Desktop/Blit/product.html', 'w') as f:
    f.write(html)

print("product.html updated completely!")
