import re

cw_section_html = """  <!-- Embedded CW Range Catalogue Section (Full Screen Width Catalog Layout) -->
  <section class="cw-catalog-section-embed" id="cw-catalog-section" style="background: #F8F9FA; padding: 0 0 60px 0; border-top: 1px solid #EAEAEA; display: none;">
    <!-- Full Screen Hero Banner Image -->
    <div class="cw-hero-fullscreen" style="width: 100%; max-width: 100%; max-height: 520px; margin: 0 0 40px 0; padding: 0; position: relative; overflow: hidden; cursor: pointer;" onclick="openFullscreenLightbox('/assets/products/switches/cw_range_hero_full.webp')">
      <img src="/assets/products/switches/cw_range_hero_full.webp" alt="CW Range Architectural Switches & Sockets" width="1920" height="820" loading="eager" fetchpriority="high" decoding="async" style="width: 100%; height: 100%; max-height: 520px; display: block; border-radius: 0; object-fit: cover; object-position: center;">
    </div>

    <div class="container" style="max-width: 1440px; margin: 0 auto; padding: 0 20px;">
      
      <!-- Outer Catalog Box Frame -->
      <div class="cw-catalog-outer-box" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 20px; padding: 32px 28px; box-shadow: 0 12px 35px rgba(0,0,0,0.04);">
        
        <!-- CW Range Hero Description & Badges -->
        <div class="cw-hero-container" style="display: flex; flex-direction: column; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 20px; margin-bottom: 50px; overflow: hidden;">

          <!-- Bottom: Description & Value Proposition Badges -->
          <div class="cw-hero-content" style="padding: 36px 40px; display: flex; flex-direction: column;">
            <span style="display: inline-block; color: var(--primary-red); font-weight: 700; font-size: 13px; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 10px;">CW RANGE</span>
            <h2 style="font-size: 38px; font-weight: 800; line-height: 1.15; color: #0F172A; margin-bottom: 14px; letter-spacing: -0.5px;">Architectural. Refined. Timeless.</h2>
            <p style="font-size: 15.5px; color: #475569; line-height: 1.6; margin-bottom: 30px; max-width: 800px;">
              CW Range is an architectural collection of precision-crafted switches, switched sockets with USB-C 20W PD, rotary dimmers, and multimedia connectivity modules designed for high-end modern residences, luxury villas, and executive spaces.
            </p>

            <!-- 5 Feature Value Prop Badges -->
            <div class="cw-features-row" style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 12px;">
              <div class="cw-feature-pill" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px 6px; text-align: center;">
                <div class="cw-feature-icon" style="width: 26px; height: 26px; margin: 0 auto 6px; display: flex; align-items: center; justify-content: center; color: #334155;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                    <path d="m9 12 2 2 4-4"/>
                  </svg>
                </div>
                <div style="font-size: 10.5px; font-weight: 600; color: #334155; line-height: 1.25;">BS Standard<br>Certified</div>
              </div>

              <div class="cw-feature-pill" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px 6px; text-align: center;">
                <div class="cw-feature-icon" style="width: 26px; height: 26px; margin: 0 auto 6px; display: flex; align-items: center; justify-content: center; color: #334155;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
                  </svg>
                </div>
                <div style="font-size: 10.5px; font-weight: 600; color: #334155; line-height: 1.25;">Architectural<br>Profile</div>
              </div>

              <div class="cw-feature-pill" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px 6px; text-align: center;">
                <div class="cw-feature-icon" style="width: 26px; height: 26px; margin: 0 auto 6px; display: flex; align-items: center; justify-content: center; color: #334155;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 3.5z"/>
                  </svg>
                </div>
                <div style="font-size: 10.5px; font-weight: 600; color: #334155; line-height: 1.25;">Flame Retardant<br>Enclosure</div>
              </div>

              <div class="cw-feature-pill" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px 6px; text-align: center;">
                <div class="cw-feature-icon" style="width: 26px; height: 26px; margin: 0 auto 6px; display: flex; align-items: center; justify-content: center; color: #334155;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
                  </svg>
                </div>
                <div style="font-size: 10.5px; font-weight: 600; color: #334155; line-height: 1.25;">20W Type-C<br>Fast Charge</div>
              </div>

              <div class="cw-feature-pill" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px 6px; text-align: center;">
                <div class="cw-feature-icon" style="width: 26px; height: 26px; margin: 0 auto 6px; display: flex; align-items: center; justify-content: center; color: #334155;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="2" y="7" width="20" height="14" rx="2" ry="2"/>
                    <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>
                  </svg>
                </div>
                <div style="font-size: 10.5px; font-weight: 600; color: #334155; line-height: 1.25;">Complete Range<br>25 Models</div>
              </div>
            </div>

          </div>
        </div>

        <!-- Categories & Products Header -->
        <div style="text-align: center; margin-bottom: 35px;">
          <h3 style="font-size: 24px; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; color: #0F172A; margin-bottom: 10px;">CW RANGE PRODUCT COLLECTION</h3>
          <p style="font-size: 14.5px; color: #64748B; max-width: 650px; margin: 0 auto 20px auto;">Browse all 25 distinct models in the prestigious architectural collection. Click any product image to zoom.</p>
          <div style="width: 44px; height: 3px; background-color: var(--primary-red); margin: 0 auto 30px auto; border-radius: 2px;"></div>
          
          <!-- Category Filter Tabs -->
          <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 8px;" id="cw-gallery-filters">
            <button class="cw-filter-btn active" onclick="filterCWRangeProducts('all', event)" style="background: var(--primary-red); color: #FFFFFF; border: none; padding: 9px 20px; border-radius: 20px; font-size: 13px; font-weight: 700; cursor: pointer; transition: all 0.2s ease;">All (25)</button>
            <button class="cw-filter-btn" onclick="filterCWRangeProducts('plate_switches', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Plate Switches (6)</button>
            <button class="cw-filter-btn" onclick="filterCWRangeProducts('high_power', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">20A & 45A Switches (2)</button>
            <button class="cw-filter-btn" onclick="filterCWRangeProducts('dimmers', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Dimmers & Speed (2)</button>
            <button class="cw-filter-btn" onclick="filterCWRangeProducts('socket_outlets', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Sockets & USB (5)</button>
            <button class="cw-filter-btn" onclick="filterCWRangeProducts('multi_sockets', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Multi-Function (2)</button>
            <button class="cw-filter-btn" onclick="filterCWRangeProducts('fcus', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">FCUs & Connection Plates (4)</button>
            <button class="cw-filter-btn" onclick="filterCWRangeProducts('data_tv', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Data & Telecom (3)</button>
            <button class="cw-filter-btn" onclick="filterCWRangeProducts('bell_switches', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Bell Push (1)</button>
          </div>
        </div>

        <!-- 25 Unique CW Products Grid -->
        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 24px; margin-bottom: 60px;" id="cw-products-grid">
          <!-- Populated dynamically by script -->
        </div>

        <!-- Bottom Downloads & Price Support Cards -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; margin-top: 20px; padding-top: 35px; border-top: 1px solid #E2E8F0;">
          <!-- Left Download Catalogue Card -->
          <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 20px; padding: 32px 28px; display: flex; align-items: flex-start; gap: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.03); transition: all 0.3s ease;">
            <div style="width: 54px; height: 54px; min-width: 54px; background: rgba(255, 26, 26, 0.08); border-radius: 14px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="var(--primary-red)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                <polyline points="14 2 14 8 20 8"/>
                <line x1="12" y1="18" x2="12" y2="12"/>
                <line x1="9" y1="15" x2="15" y2="15"/>
              </svg>
            </div>
            <div style="flex-grow: 1;">
              <h4 style="font-size: 18px; font-weight: 700; color: #0F172A; margin-bottom: 6px;">Download Complete CW Range Catalogue</h4>
              <p style="font-size: 13.5px; color: #64748B; line-height: 1.5; margin-bottom: 20px;">Get the complete official collection catalogue with all 25 model codes, dimensions, specifications, and wiring diagrams in PDF format.</p>
              <a id="cw-catalogue-download-link" href="/assets/catalogues/BLIT_CW_Range_Catalogue_2026.pdf" download="BLIT_CW_Range_Catalogue_2026.pdf" style="display: inline-flex; align-items: center; gap: 10px; background-color: #FF1A1A; color: #FFFFFF; border: none; padding: 12px 26px; border-radius: 30px; font-size: 14px; font-weight: 700; text-decoration: none; box-shadow: 0 8px 20px rgba(255, 26, 26, 0.28); transition: all 0.3s ease;">
                <span>Download Catalogue</span>
                <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                  <polyline points="7 10 12 15 17 10"/>
                  <line x1="12" y1="15" x2="12" y2="3"/>
                </svg>
              </a>
            </div>
          </div>

          <!-- Right Price Request Card -->
          <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 20px; padding: 32px 28px; display: flex; align-items: flex-start; gap: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.03); transition: all 0.3s ease;">
            <div style="width: 54px; height: 54px; min-width: 54px; background: rgba(15, 23, 42, 0.06); border-radius: 14px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#0F172A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M3 18v-6a9 9 0 0 1 18 0v6"/>
                <path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"/>
              </svg>
            </div>
            <div style="flex-grow: 1;">
              <h4 style="font-size: 18px; font-weight: 700; color: #0F172A; margin-bottom: 6px;">Need Price List or Project Support?</h4>
              <p style="font-size: 13.5px; color: #64748B; line-height: 1.5; margin-bottom: 20px;">Our sales & engineering team is ready to assist you with CW Range project specifications, BOQ pricing, and sample approvals.</p>
              <a href="javascript:void(0)" onclick="document.getElementById('cw-price-modal').style.display='flex'" style="display: inline-flex; align-items: center; gap: 8px; border: 1.5px solid #0F172A; color: #0F172A; background: #FFFFFF; padding: 11px 22px; border-radius: 30px; font-size: 14px; font-weight: 700; text-decoration: none; transition: all 0.3s ease;">
                Request Price List <span class="arrow">→</span>
              </a>
            </div>
          </div>
        </div>

      </div> <!-- End cw-catalog-outer-box -->
    </div>
  </section>"""

cw_modals_html = """  <!-- CW Range Price List Request Modal -->
  <div id="cw-price-modal" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(15, 23, 42, 0.6); backdrop-filter: blur(5px); display: none; align-items: center; justify-content: center; z-index: 2000;">
    <div style="background: #FFFFFF; border-radius: 20px; max-width: 520px; width: 90%; padding: 32px; position: relative; box-shadow: 0 25px 50px rgba(0,0,0,0.25);">
      <button onclick="document.getElementById('cw-price-modal').style.display='none'" style="position: absolute; top: 20px; right: 20px; background: #F1F5F9; border: none; width: 34px; height: 34px; border-radius: 50%; cursor: pointer; font-weight: 700;">✕</button>
      <h3 style="font-size: 22px; font-weight: 800; color: #0F172A; margin-bottom: 6px;">Request CW Range Price List & Support</h3>
      <p style="font-size: 13.5px; color: #64748B; margin-bottom: 20px;">Submit your project requirements and our engineering team will provide wholesale BOQ pricing.</p>

      <form onsubmit="event.preventDefault(); alert('Thank you! Your request for the CW Range Catalogue & Price List has been submitted.'); document.getElementById('cw-price-modal').style.display='none';" style="display: flex; flex-direction: column; gap: 14px;">
        <div>
          <label style="font-size: 12.5px; font-weight: 600; color: #334155; display: block; margin-bottom: 4px;">Full Name *</label>
          <input type="text" required placeholder="John Doe" style="width: 100%; padding: 10px; border: 1px solid #CBD5E1; border-radius: 8px; font-size: 13.5px; box-sizing: border-box;">
        </div>
        <div>
          <label style="font-size: 12.5px; font-weight: 600; color: #334155; display: block; margin-bottom: 4px;">Email Address *</label>
          <input type="email" required placeholder="john@company.com" style="width: 100%; padding: 10px; border: 1px solid #CBD5E1; border-radius: 8px; font-size: 13.5px; box-sizing: border-box;">
        </div>
        <div>
          <label style="font-size: 12.5px; font-weight: 600; color: #334155; display: block; margin-bottom: 4px;">Phone / WhatsApp *</label>
          <input type="tel" required placeholder="+971 50 123 4567" style="width: 100%; padding: 10px; border: 1px solid #CBD5E1; border-radius: 8px; font-size: 13.5px; box-sizing: border-box;">
        </div>
        <div>
          <label style="font-size: 12.5px; font-weight: 600; color: #334155; display: block; margin-bottom: 4px;">Project Details / BOQ</label>
          <textarea rows="3" placeholder="Mention project type (Hotel, Villa, Residential) and estimated item counts..." style="width: 100%; padding: 10px; border: 1px solid #CBD5E1; border-radius: 8px; font-size: 13.5px; box-sizing: border-box;"></textarea>
        </div>
        <button type="submit" style="background: var(--primary-red); color: #FFFFFF; border: none; padding: 12px; border-radius: 25px; font-weight: 700; font-size: 14px; cursor: pointer; margin-top: 6px;">
          Submit Inquiry →
        </button>
      </form>
    </div>
  </div>"""

cw_script_html = """  <script>
    const UNIQUE_CW_PRODUCTS = [
      { code: "BTCW3011-WHI", cat: "plate_switches", name: "1-Gang 1-Way Plate Switch", desc: "10AX 250V~ 1-Gang Switch with Architectural White Finish", size: "86 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/cw_range/BTCW3011-WHI.webp" },
      { code: "BTCW3012-WHI", cat: "plate_switches", name: "1-Gang 2-Way Plate Switch", desc: "10AX 250V~ 1-Gang 2-Way Switch for Multi-Location Circuits", size: "86 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/cw_range/BTCW3012-WHI.webp" },
      { code: "BTCW3213-WHI", cat: "plate_switches", name: "1-Gang Intermediate Switch", desc: "10AX 250V~ 1-Gang Cross-Over Intermediate Plate Switch", size: "86 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/cw_range/BTCW3213-WHI.webp" },
      { code: "BTCW3022-WHI", cat: "plate_switches", name: "2-Gang 2-Way Plate Switch", desc: "10AX 250V~ 2-Gang Dual Circuit Rocker Switch Plate", size: "86 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/cw_range/BTCW3022-WHI.webp" },
      { code: "BTCW3032-WHI", cat: "plate_switches", name: "3-Gang 2-Way Plate Switch", desc: "10AX 250V~ 3-Gang Multi-Zone Light Switch Plate", size: "86 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/cw_range/BTCW3032-WHI.webp" },
      { code: "BTCW3042-WHI", cat: "plate_switches", name: "4-Gang 2-Way Plate Switch", desc: "10AX 250V~ 4-Gang Quad Control Rocker Switch Plate", size: "86 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/cw_range/BTCW3042-WHI.webp" },
      
      { code: "BTCW3016BEL-WHI", cat: "bell_switches", name: "1-Gang Bell Push Switch", desc: "10A 250V~ Retractive Bell Push Switch with Engraved Bell Symbol", size: "86 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/cw_range/BTCW3016BEL-WHI.webp" },
      
      { code: "BTCW3341-WHI", cat: "high_power", name: "20A DP Switch + Neon", desc: "20A Double Pole Isolator Switch with Illuminated Neon Indicator", size: "86 x 86 mm", std: "BS EN 60669-2-1", img: "/assets/products/cw_range/BTCW3341-WHI.webp" },
      { code: "BTCW3267-WHI", cat: "high_power", name: "45A DP Switch + Neon", desc: "45A Double Pole Main Isolator Switch with Red Neon Indicator", size: "86 x 86 mm", std: "BS EN 60669-2-1", img: "/assets/products/cw_range/BTCW3267-WHI.webp" },
      
      { code: "BTCW3501-WHI", cat: "dimmers", name: "1-Gang Rotary Dimmer (400W)", desc: "400W/500W Rotary Dimmer Switch & Precision Fan Speed Controller", size: "86 x 86 mm", std: "BS EN 60669-2-1", img: "/assets/products/cw_range/BTCW3501-WHI.webp" },
      { code: "BTCW3502-WHI", cat: "dimmers", name: "2-Gang Rotary Dimmer", desc: "Dual Channel Rotary Lighting Dimmer Switch on Wide Plate", size: "146 x 86 mm", std: "BS EN 60669-2-1", img: "/assets/products/cw_range/BTCW3502-WHI.webp" },
      
      { code: "BTCW4010C-WHI", cat: "socket_outlets", name: "13A Single Switched Socket", desc: "13A 1-Gang BS 1363-2 Switched Power Outlet with Child Shutters", size: "86 x 86 mm", std: "BS 1363-2", img: "/assets/products/cw_range/BTCW4010C-WHI.webp" },
      { code: "BTCW4030L-WHI", cat: "socket_outlets", name: "13A Twin Switched Socket + Neon", desc: "13A 2-Gang BS 1363-2 Double Switched Socket with Dual Neons", size: "146 x 86 mm", std: "BS 1363-2", img: "/assets/products/cw_range/BTCW4030L-WHI.webp" },
      { code: "BTCW4113H-3.1A-WHI", cat: "socket_outlets", name: "13A Single Socket + Dual USB 3.1A", desc: "13A Switched Single Socket + Dual 3.1A Fast USB Charging Ports", size: "86 x 86 mm", std: "BS 1363-2 / IEC 62368", img: "/assets/products/cw_range/BTCW4113H-3.1A-WHI.webp" },
      { code: "BTCW4120-3.1A-WHI", cat: "socket_outlets", name: "13A Twin Socket + Dual USB 3.1A", desc: "Twin 13A Double Switched Socket + Dual 3.1A Fast USB Charging Ports", size: "146 x 86 mm", std: "BS 1363-2 / IEC 62368", img: "/assets/products/cw_range/BTCW4120-3.1A-WHI.webp" },
      { code: "BTCW4210-WHI", cat: "socket_outlets", name: "15A Round Pin Switched Socket", desc: "15A Heavy Duty BS 546 Round Pin AC Switched Socket Outlet", size: "86 x 86 mm", std: "BS 546", img: "/assets/products/cw_range/BTCW4210-WHI.webp" },
      
      { code: "BTCW4242-20W-WHI", cat: "multi_sockets", name: "1-Gang Multi-Socket + 20W PD Type-C", desc: "Universal Multi-Pin Socket with 20W USB Type-C & Type-A Fast Charger", size: "86 x 86 mm", std: "IEC 60884 / IEC 62368", img: "/assets/products/cw_range/BTCW4242-20W-WHI.webp" },
      { code: "BTCW4252-20W-WHI", cat: "multi_sockets", name: "2-Gang Multi-Socket + 20W PD Type-C", desc: "Twin Universal Multi-Pin Sockets + 20W Type-C Power Delivery Fast Charger", size: "146 x 86 mm", std: "IEC 60884 / IEC 62368", img: "/assets/products/cw_range/BTCW4252-20W-WHI.webp" },
      
      { code: "BTCW3415-WHI", cat: "fcus", name: "13A Unswitched FCU Spur", desc: "13A Unswitched Fused Connection Unit with Front Fuse Carrier", size: "86 x 86 mm", std: "BS 1363-4", img: "/assets/products/cw_range/BTCW3415-WHI.webp" },
      { code: "BTCW3416LED-WHI", cat: "fcus", name: "13A Switched FCU + LED", desc: "13A DP Switched Fused Connection Spur Unit with LED Neon Indicator", size: "86 x 86 mm", std: "BS 1363-4", img: "/assets/products/cw_range/BTCW3416LED-WHI.webp" },
      { code: "BTCW4620-WHI", cat: "fcus", name: "20A Cable Connection / Blank Plate", desc: "20A Heavy Duty Cable Outlet Connection Plate with Internal Terminals", size: "86 x 86 mm", std: "BS 5733", img: "/assets/products/cw_range/BTCW4620-WHI.webp" },
      { code: "BTCW4645-WHI", cat: "fcus", name: "45A Cable Connection Plate", desc: "45A High Current Cable Connection Plate for Large Cooker Units", size: "86 x 86 mm", std: "BS 5733", img: "/assets/products/cw_range/BTCW4645-WHI.webp" },
      
      { code: "BTCW4311-WHI", cat: "data_tv", name: "TV / Satellite Multimedia Outlet", desc: "Coaxial TV and Satellite Antenna Outlet on Wide Plate", size: "146 x 86 mm", std: "BS 3041", img: "/assets/products/cw_range/BTCW4311-WHI.webp" },
      { code: "BTCW442-WHI", cat: "data_tv", name: "1-Gang RJ45 Cat6 Data Outlet", desc: "1-Port Gigabit Ethernet Cat6 Data Wall Plate with Dust Shutter", size: "86 x 86 mm", std: "TIA/EIA-568", img: "/assets/products/cw_range/BTCW442-WHI.webp" },
      { code: "BTCW443-WHI", cat: "data_tv", name: "2-Gang RJ45 Cat6 Data Outlet", desc: "2-Port Dual Gigabit Ethernet Cat6 Data Wall Plate", size: "86 x 86 mm", std: "TIA/EIA-568", img: "/assets/products/cw_range/BTCW443-WHI.webp" }
    ];

    function renderCWRangeProducts(filter = 'all') {
      const grid = document.getElementById('cw-products-grid');
      if (!grid) return;

      const items = filter === 'all' ? UNIQUE_CW_PRODUCTS : UNIQUE_CW_PRODUCTS.filter(p => p.cat === filter);
      grid.innerHTML = items.map(p => `
        <div class="cw-product-card-item" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 16px; padding: 20px; display: flex; flex-direction: column; justify-content: space-between; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(0,0,0,0.02);" onmouseover="this.style.transform='translateY(-5px)'; this.style.borderColor='rgba(255,26,26,0.35)'; this.style.boxShadow='0 14px 28px rgba(255,26,26,0.09)';" onmouseout="this.style.transform='none'; this.style.borderColor='#E2E8F0'; this.style.boxShadow='0 4px 15px rgba(0,0,0,0.02)';">
          
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

    function filterCWRangeProducts(filterKey, e) {
      if (e) {
        const btns = document.querySelectorAll('#cw-gallery-filters .cw-filter-btn');
        btns.forEach(b => {
          b.style.background = '#F1F5F9';
          b.style.color = '#334155';
          b.classList.remove('active');
        });
        e.target.style.background = 'var(--primary-red)';
        e.target.style.color = '#FFFFFF';
        e.target.classList.add('active');
      }
      renderCWRangeProducts(filterKey);
    }

    document.addEventListener('DOMContentLoaded', () => {
      renderCWRangeProducts('all');
    });
  </script>"""

with open('/Users/amanyoonus/Desktop/Blit/product.html', 'r') as f:
    html = f.read()

# 1. Insert CW section after V section
v_sec_end = html.find('</section>', html.find('id="v-catalog-section"'))
if v_sec_end != -1:
    v_sec_end += len('</section>')
    html = html[:v_sec_end] + '\n\n' + cw_section_html + html[v_sec_end:]
    print("CW section HTML inserted!")

# 2. Insert CW modal after V price modal
v_price_end = html.find('</div>', html.find('id="v-price-modal"'))
# Find the actual closing </div> of v-price-modal
v_price_start = html.find('id="v-price-modal"')
if v_price_start != -1:
    v_price_block_end = html.find('<!-- Category Options Modal -->', v_price_start)
    if v_price_block_end != -1:
        html = html[:v_price_block_end] + cw_modals_html + '\n\n  ' + html[v_price_block_end:]
        print("CW modal inserted!")

# 3. Insert CW scripts before UNIQUE_V_PRODUCTS script or UNIQUE_W_PRODUCTS script
v_script_pos = html.find('<script>\n    const UNIQUE_V_PRODUCTS')
if v_script_pos != -1:
    html = html[:v_script_pos] + cw_script_html + '\n\n  ' + html[v_script_pos:]
    print("CW script inserted!")

# 4. Update the router & product detail toggling logic
old_toggle_str = """        // Toggle visibility between Single Product Detail View, W Range, and V Range Catalogue Pages
        const detailMain = document.getElementById('product-detail-main');
        const wCatalogSection = document.getElementById('w-catalog-section');
        const vCatalogSection = document.getElementById('v-catalog-section');
        
        const reqRange = params.get('range');
        const isVRangeMain = (reqRange === 'V Range' || product.range === 'V Range' || product.name.startsWith('V Range'));
        const isWhiteRangeMain = (reqRange === 'W Range' || product.range === 'W Range' || product.name.startsWith('W Range') || product.name.startsWith('White Range'));

        if (isVRangeMain) {
          if (detailMain) detailMain.style.display = 'none';
          if (wCatalogSection) wCatalogSection.style.display = 'none';
          if (vCatalogSection) vCatalogSection.style.display = 'block';
          window.scrollTo(0, 0);
        } else if (isWhiteRangeMain) {
          if (detailMain) detailMain.style.display = 'none';
          if (vCatalogSection) vCatalogSection.style.display = 'none';
          if (wCatalogSection) wCatalogSection.style.display = 'block';
          window.scrollTo(0, 0);
        } else {
          if (detailMain) detailMain.style.display = 'block';
          if (wCatalogSection) wCatalogSection.style.display = 'none';
          if (vCatalogSection) vCatalogSection.style.display = 'none';
        }"""

new_toggle_str = """        // Toggle visibility between Single Product Detail View, W Range, V Range, and CW Range Catalogue Pages
        const detailMain = document.getElementById('product-detail-main');
        const wCatalogSection = document.getElementById('w-catalog-section');
        const vCatalogSection = document.getElementById('v-catalog-section');
        const cwCatalogSection = document.getElementById('cw-catalog-section');
        
        const reqRange = params.get('range');
        const isVRangeMain = (reqRange === 'V Range' || product.range === 'V Range' || product.name.startsWith('V Range'));
        const isWhiteRangeMain = (reqRange === 'W Range' || product.range === 'W Range' || product.name.startsWith('W Range') || product.name.startsWith('White Range'));
        const isCWRangeMain = (reqRange === 'CW Range' || product.range === 'CW Range' || product.name.startsWith('CW Range') || product.name.includes('BTCW'));

        if (isCWRangeMain) {
          if (detailMain) detailMain.style.display = 'none';
          if (wCatalogSection) wCatalogSection.style.display = 'none';
          if (vCatalogSection) vCatalogSection.style.display = 'none';
          if (cwCatalogSection) {
            cwCatalogSection.style.display = 'block';
            renderCWRangeProducts('all');
          }
          window.scrollTo(0, 0);
        } else if (isVRangeMain) {
          if (detailMain) detailMain.style.display = 'none';
          if (wCatalogSection) wCatalogSection.style.display = 'none';
          if (cwCatalogSection) cwCatalogSection.style.display = 'none';
          if (vCatalogSection) vCatalogSection.style.display = 'block';
          window.scrollTo(0, 0);
        } else if (isWhiteRangeMain) {
          if (detailMain) detailMain.style.display = 'none';
          if (vCatalogSection) vCatalogSection.style.display = 'none';
          if (cwCatalogSection) cwCatalogSection.style.display = 'none';
          if (wCatalogSection) wCatalogSection.style.display = 'block';
          window.scrollTo(0, 0);
        } else {
          if (detailMain) detailMain.style.display = 'block';
          if (wCatalogSection) wCatalogSection.style.display = 'none';
          if (vCatalogSection) vCatalogSection.style.display = 'none';
          if (cwCatalogSection) cwCatalogSection.style.display = 'none';
        }"""

html = html.replace(old_toggle_str, new_toggle_str)

old_parse_str = """      const detailMain = document.getElementById('product-detail-main');
      const wCatalogSection = document.getElementById('w-catalog-section');
      const vCatalogSection = document.getElementById('v-catalog-section');

      const isVRange = (reqRange.toLowerCase().includes('v range') || productName.toLowerCase().includes('v range') || productName.toUpperCase().includes('BTV') || reqRange.toLowerCase() === 'v');
      const isWRange = (reqRange.toLowerCase().includes('w range') || productName.toLowerCase().includes('w range') || productName.toLowerCase().includes('white range') || productName.toUpperCase().includes('W3') || productName.toUpperCase().includes('W4') || reqRange.toLowerCase() === 'w');

      if (isVRange) {
        if (detailMain) detailMain.style.display = 'none';
        if (wCatalogSection) wCatalogSection.style.display = 'none';
        if (vCatalogSection) vCatalogSection.style.display = 'block';
        window.scrollTo(0, 0);
        return;
      }

      if (isWRange) {
        if (detailMain) detailMain.style.display = 'none';
        if (vCatalogSection) vCatalogSection.style.display = 'none';
        if (wCatalogSection) wCatalogSection.style.display = 'block';
        window.scrollTo(0, 0);
        return;
      }"""

new_parse_str = """      const detailMain = document.getElementById('product-detail-main');
      const wCatalogSection = document.getElementById('w-catalog-section');
      const vCatalogSection = document.getElementById('v-catalog-section');
      const cwCatalogSection = document.getElementById('cw-catalog-section');

      const isCWRange = (reqRange.toLowerCase().includes('cw range') || productName.toLowerCase().includes('cw range') || productName.toUpperCase().includes('BTCW') || reqRange.toLowerCase() === 'cw');
      const isVRange = (reqRange.toLowerCase().includes('v range') || productName.toLowerCase().includes('v range') || productName.toUpperCase().includes('BTV') || reqRange.toLowerCase() === 'v');
      const isWRange = (reqRange.toLowerCase().includes('w range') || productName.toLowerCase().includes('w range') || productName.toLowerCase().includes('white range') || productName.toUpperCase().includes('W3') || productName.toUpperCase().includes('W4') || reqRange.toLowerCase() === 'w');

      if (isCWRange) {
        if (detailMain) detailMain.style.display = 'none';
        if (wCatalogSection) wCatalogSection.style.display = 'none';
        if (vCatalogSection) vCatalogSection.style.display = 'none';
        if (cwCatalogSection) {
          cwCatalogSection.style.display = 'block';
          renderCWRangeProducts('all');
        }
        window.scrollTo(0, 0);
        return;
      }

      if (isVRange) {
        if (detailMain) detailMain.style.display = 'none';
        if (wCatalogSection) wCatalogSection.style.display = 'none';
        if (cwCatalogSection) cwCatalogSection.style.display = 'none';
        if (vCatalogSection) vCatalogSection.style.display = 'block';
        window.scrollTo(0, 0);
        return;
      }

      if (isWRange) {
        if (detailMain) detailMain.style.display = 'none';
        if (vCatalogSection) vCatalogSection.style.display = 'none';
        if (cwCatalogSection) cwCatalogSection.style.display = 'none';
        if (wCatalogSection) wCatalogSection.style.display = 'block';
        window.scrollTo(0, 0);
        return;
      }"""

html = html.replace(old_parse_str, new_parse_str)

with open('/Users/amanyoonus/Desktop/Blit/product.html', 'w') as f:
    f.write(html)

print("product.html completely updated for CW Range!")
