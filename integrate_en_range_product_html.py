import re

en_section_html = """  <!-- Embedded EN Range Catalogue Section (Full Screen Width Catalog Layout) -->
  <section class="en-catalog-section-embed" id="en-catalog-section" style="background: #F8F9FA; padding: 0 0 60px 0; border-top: 1px solid #EAEAEA; display: none;">
    <!-- Full Screen Hero Banner Image / Showcase -->
    <div class="en-hero-fullscreen" style="width: 100%; max-width: 100%; margin: 0 0 40px 0; padding: 0; position: relative; overflow: hidden; cursor: pointer; background: linear-gradient(135deg, #0F172A 0%, #1E293B 50%, #334155 100%); display: flex; align-items: center; justify-content: center;" onclick="openFullscreenLightbox('/assets/products/en_range/BTEN302STB.webp')">
      <div style="display: flex; align-items: center; justify-content: space-between; gap: 40px; padding: 50px 40px; width: 100%; max-width: 1280px; flex-wrap: wrap;">
        <div style="flex: 1; min-width: 320px; max-width: 600px; color: #FFFFFF; text-align: left;">
          <span style="display: inline-block; background: rgba(255, 26, 26, 0.2); color: #FF4D4D; font-weight: 700; font-size: 12px; letter-spacing: 1.5px; text-transform: uppercase; padding: 5px 14px; border-radius: 20px; margin-bottom: 14px;">EN RANGE COLLECTION</span>
          <h1 style="font-size: 40px; font-weight: 800; line-height: 1.15; color: #FFFFFF; margin-bottom: 14px; letter-spacing: -0.5px;">Sleek. Minimalist.<br>Satin Steel.</h1>
          <p style="font-size: 15.5px; color: #94A3B8; line-height: 1.6; margin-bottom: 24px;">Architectural flat-profile wiring accessories precision-crafted in Satin Brushed Steel (Silver) and Brushed Brass (Gold) for luxury villas, commercial developments, and modern residences.</p>
          <div style="display: flex; gap: 12px; flex-wrap: wrap;">
            <span style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); color: #E2E8F0; font-size: 12.5px; font-weight: 600; padding: 6px 14px; border-radius: 20px;">BS Standard Certified</span>
            <span style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); color: #E2E8F0; font-size: 12.5px; font-weight: 600; padding: 6px 14px; border-radius: 20px;">Satin Brushed Steel</span>
            <span style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); color: #E2E8F0; font-size: 12.5px; font-weight: 600; padding: 6px 14px; border-radius: 20px;">Dual USB 3.1A</span>
          </div>
        </div>
        <div style="display: flex; gap: 24px; align-items: center; justify-content: center; flex: 1; min-width: 320px;">
          <img src="/assets/products/en_range/BTEN302STB.webp" alt="EN Range 1-Gang Switch Silver" style="height: 230px; max-width: 230px; object-fit: contain; filter: drop-shadow(0 20px 35px rgba(0,0,0,0.5)); transform: rotate(-3deg); transition: transform 0.3s ease;">
          <img src="/assets/products/en_range/BTHY4121-B-3.1ASTB.webp" alt="EN Range Twin Socket + Dual USB Silver" style="height: 230px; max-width: 290px; object-fit: contain; filter: drop-shadow(0 20px 35px rgba(0,0,0,0.5)); transform: rotate(3deg); transition: transform 0.3s ease;">
        </div>
      </div>
    </div>

    <div class="container" style="max-width: 1440px; margin: 0 auto; padding: 0 20px;">
      
      <!-- Outer Catalog Box Frame -->
      <div class="en-catalog-outer-box" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 20px; padding: 32px 28px; box-shadow: 0 12px 35px rgba(0,0,0,0.04);">
        
        <!-- EN Range Hero Description & Badges -->
        <div class="en-hero-container" style="display: flex; flex-direction: column; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 20px; margin-bottom: 50px; overflow: hidden;">

          <!-- Bottom: Description & Value Proposition Badges -->
          <div class="en-hero-content" style="padding: 36px 40px; display: flex; flex-direction: column;">
            <span style="display: inline-block; color: var(--primary-red); font-weight: 700; font-size: 13px; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 10px;">EN RANGE</span>
            <h2 style="font-size: 38px; font-weight: 800; line-height: 1.15; color: #0F172A; margin-bottom: 14px; letter-spacing: -0.5px;">Precision Engineering. Contemporary Edge.</h2>
            <p style="font-size: 15.5px; color: #475569; line-height: 1.6; margin-bottom: 30px; max-width: 800px;">
              The EN Range delivers refined modern functionality with ultra-slim flat borders, smooth rocker switches, high-amperage double-pole isolators, smart dual-USB 3.1A fast charging outlets, and high-performance lighting dimmers.
            </p>

            <!-- 5 Feature Value Prop Badges -->
            <div class="en-features-row" style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 12px;">
              <div class="en-feature-pill" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px 6px; text-align: center;">
                <div class="en-feature-icon" style="width: 26px; height: 26px; margin: 0 auto 6px; display: flex; align-items: center; justify-content: center; color: #334155;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                    <path d="m9 12 2 2 4-4"/>
                  </svg>
                </div>
                <div style="font-size: 10.5px; font-weight: 600; color: #334155; line-height: 1.25;">BS Standard<br>Certified</div>
              </div>

              <div class="en-feature-pill" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px 6px; text-align: center;">
                <div class="en-feature-icon" style="width: 26px; height: 26px; margin: 0 auto 6px; display: flex; align-items: center; justify-content: center; color: #334155;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
                  </svg>
                </div>
                <div style="font-size: 10.5px; font-weight: 600; color: #334155; line-height: 1.25;">Satin Brushed<br>Steel Finish</div>
              </div>

              <div class="en-feature-pill" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px 6px; text-align: center;">
                <div class="en-feature-icon" style="width: 26px; height: 26px; margin: 0 auto 6px; display: flex; align-items: center; justify-content: center; color: #334155;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 3.5z"/>
                  </svg>
                </div>
                <div style="font-size: 10.5px; font-weight: 600; color: #334155; line-height: 1.25;">Flame Retardant<br>Enclosure</div>
              </div>

              <div class="en-feature-pill" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px 6px; text-align: center;">
                <div class="en-feature-icon" style="width: 26px; height: 26px; margin: 0 auto 6px; display: flex; align-items: center; justify-content: center; color: #334155;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
                  </svg>
                </div>
                <div style="font-size: 10.5px; font-weight: 600; color: #334155; line-height: 1.25;">Dual USB 3.1A<br>Fast Charging</div>
              </div>

              <div class="en-feature-pill" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px 6px; text-align: center;">
                <div class="en-feature-icon" style="width: 26px; height: 26px; margin: 0 auto 6px; display: flex; align-items: center; justify-content: center; color: #334155;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="2" y="7" width="20" height="14" rx="2" ry="2"/>
                    <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>
                  </svg>
                </div>
                <div style="font-size: 10.5px; font-weight: 600; color: #334155; line-height: 1.25;">Satin Steel (Silver)<br>21 Models</div>
              </div>
            </div>

          </div>
        </div>

        <!-- Categories & Products Header -->
        <div style="text-align: center; margin-bottom: 35px;">
          <h3 style="font-size: 24px; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; color: #0F172A; margin-bottom: 10px;">EN RANGE PRODUCT COLLECTION</h3>
          <p style="font-size: 14.5px; color: #64748B; max-width: 650px; margin: 0 auto 20px auto;">Browse all 21 distinct models in the Satin Brushed Steel (Silver) collection. Click any product image to zoom.</p>
          <div style="width: 44px; height: 3px; background-color: var(--primary-red); margin: 0 auto 30px auto; border-radius: 2px;"></div>
          
          <!-- Category Filter Tabs -->
          <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 8px;" id="en-gallery-filters">
            <button class="en-filter-btn active" onclick="filterENRangeProducts('all', event)" style="background: var(--primary-red); color: #FFFFFF; border: none; padding: 9px 20px; border-radius: 20px; font-size: 13px; font-weight: 700; cursor: pointer; transition: all 0.2s ease;">All (21)</button>
            <button class="en-filter-btn" onclick="filterENRangeProducts('plate_switches', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Plate Switches (4)</button>
            <button class="en-filter-btn" onclick="filterENRangeProducts('high_power', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">20A & 45A Switches (3)</button>
            <button class="en-filter-btn" onclick="filterENRangeProducts('dimmers', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Dimmers & Fan (4)</button>
            <button class="en-filter-btn" onclick="filterENRangeProducts('socket_outlets', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Sockets & USB (5)</button>
            <button class="en-filter-btn" onclick="filterENRangeProducts('fcus', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Blank Plates (2)</button>
            <button class="en-filter-btn" onclick="filterENRangeProducts('data_tv', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Data & Telecom (2)</button>
            <button class="en-filter-btn" onclick="filterENRangeProducts('bell_switches', event)" style="background: #F1F5F9; color: #334155; border: none; padding: 9px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s ease;">Bell Push (1)</button>
          </div>
        </div>

        <!-- 21 Unique EN Products Grid -->
        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 24px; margin-bottom: 60px;" id="en-products-grid">
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
              <h4 style="font-size: 18px; font-weight: 700; color: #0F172A; margin-bottom: 6px;">Download Complete EN Range Catalogue</h4>
              <p style="font-size: 13.5px; color: #64748B; line-height: 1.5; margin-bottom: 20px;">Get the complete official collection catalogue featuring all 42 Silver & Gold model codes, dimensions, specifications, and wiring diagrams in PDF format.</p>
              <a id="en-catalogue-download-link" href="/assets/catalogues/BLIT_EN_Range_Catalogue_2026.pdf" download="BLIT_EN_Range_Catalogue_2026.pdf" style="display: inline-flex; align-items: center; gap: 10px; background-color: #FF1A1A; color: #FFFFFF; border: none; padding: 12px 26px; border-radius: 30px; font-size: 14px; font-weight: 700; text-decoration: none; box-shadow: 0 8px 20px rgba(255, 26, 26, 0.28); transition: all 0.3s ease;">
                <span>Download Catalogue (PDF)</span>
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
              <p style="font-size: 13.5px; color: #64748B; line-height: 1.5; margin-bottom: 20px;">Our sales & engineering team is ready to assist you with EN Range project specifications, BOQ pricing, and sample approvals.</p>
              <a href="javascript:void(0)" onclick="document.getElementById('en-price-modal').style.display='flex'" style="display: inline-flex; align-items: center; gap: 8px; border: 1.5px solid #0F172A; color: #0F172A; background: #FFFFFF; padding: 11px 22px; border-radius: 30px; font-size: 14px; font-weight: 700; text-decoration: none; transition: all 0.3s ease;">
                Request Price List <span class="arrow">→</span>
              </a>
            </div>
          </div>
        </div>

      </div> <!-- End en-catalog-outer-box -->
    </div>
  </section>
"""

en_modal_html = """  <!-- EN Range Price List Request Modal -->
  <div id="en-price-modal" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(15, 23, 42, 0.6); backdrop-filter: blur(5px); display: none; align-items: center; justify-content: center; z-index: 2000;">
    <div style="background: #FFFFFF; border-radius: 20px; max-width: 520px; width: 90%; padding: 32px; position: relative; box-shadow: 0 25px 50px rgba(0,0,0,0.25);">
      <button onclick="document.getElementById('en-price-modal').style.display='none'" style="position: absolute; top: 20px; right: 20px; background: #F1F5F9; border: none; width: 34px; height: 34px; border-radius: 50%; cursor: pointer; font-weight: 700;">✕</button>
      <h3 style="font-size: 22px; font-weight: 800; color: #0F172A; margin-bottom: 6px;">Request EN Range Price List & Support</h3>
      <p style="font-size: 13.5px; color: #64748B; margin-bottom: 20px;">Submit your project requirements and our engineering team will provide wholesale BOQ pricing.</p>

      <form onsubmit="event.preventDefault(); alert('Thank you! Your request for the EN Range Catalogue & Price List has been submitted.'); document.getElementById('en-price-modal').style.display='none';" style="display: flex; flex-direction: column; gap: 14px;">
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
  </div>
"""

en_script_html = """  <script>
    const UNIQUE_EN_PRODUCTS = [
      // 1. Plate Switches
      { code: "BTEN302STB", cat: "plate_switches", name: "1-Gang 2-Way Plate Switch (Silver)", desc: "10AX 250V~ 1-Gang 2-Way Switch with Architectural Profile", size: "86 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/en_range/BTEN302STB.webp" },
      { code: "BTEN304STB", cat: "plate_switches", name: "2-Gang 2-Way Plate Switch (Silver)", desc: "10AX 250V~ 2-Gang Dual Circuit Rocker Switch Plate", size: "86 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/en_range/BTEN304STB.webp" },
      { code: "BTEN306STB", cat: "plate_switches", name: "3-Gang 2-Way Plate Switch (Silver)", desc: "10AX 250V~ 3-Gang Multi-Zone Light Switch Plate", size: "86 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/en_range/BTEN306STB.webp" },
      { code: "BTEN308STB", cat: "plate_switches", name: "4-Gang 2-Way Wide Switch (Silver)", desc: "10AX 250V~ 4-Gang Quad Control Rocker Switch on Wide Plate", size: "146 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/en_range/BTEN308STB.webp" },
      
      // 2. Bell & Special Switches
      { code: "BTEN317STB", cat: "bell_switches", name: "1-Gang Bell Push Switch (Silver)", desc: "10A 250V~ Retractive Momentary Bell Push with Bell Symbol", size: "86 x 86 mm", std: "BS EN 60669-1", img: "/assets/products/en_range/BTEN317STB.webp" },
      
      // 3. 20A & 45A High Power Isolator Switches
      { code: "BTEN324STB", cat: "high_power", name: "20A DP Switch + Neon (Silver)", desc: "20A Double Pole Heavy Duty Isolator Switch with Illuminated Neon", size: "86 x 86 mm", std: "BS EN 60669-2-1", img: "/assets/products/en_range/BTEN324STB.webp" },
      { code: "BTEN327STB", cat: "high_power", name: "45A DP Switch + Neon (Silver)", desc: "45A Double Pole Main Isolator Switch with Red Neon Indicator", size: "86 x 86 mm", std: "BS EN 60669-2-1", img: "/assets/products/en_range/BTEN327STB.webp" },
      { code: "BTEN329STB", cat: "high_power", name: "45A DP Large Plate Switch + Neon (Silver)", desc: "45A Large Rocker Double Pole Cooker Isolator Switch with Neon", size: "86 x 146 mm", std: "BS EN 60669-2-1", img: "/assets/products/en_range/BTEN329STB.webp" },
      
      // 4. Rotary Dimmers & Fan Speed Controllers
      { code: "BTEN350-2STB", cat: "dimmers", name: "1-Gang Rotary Dimmer (400W) (Silver)", desc: "400W Rotary Lighting Dimmer Switch with Smooth Push-On Action", size: "86 x 86 mm", std: "BS EN 60669-2-1", img: "/assets/products/en_range/BTEN350-2STB.webp" },
      { code: "BTEN351STB", cat: "dimmers", name: "1-Gang Fan Speed Controller (Silver)", desc: "400W Stepless Fan Speed Regulator Controller Switch", size: "86 x 86 mm", std: "IEC 60669", img: "/assets/products/en_range/BTEN351STB.webp" },
      { code: "BTEN353-2STB", cat: "dimmers", name: "2-Gang Rotary Dimmer (Silver)", desc: "Dual Channel 400W Rotary Lighting Dimmer Switch Plate", size: "86 x 86 mm", std: "BS EN 60669-2-1", img: "/assets/products/en_range/BTEN353-2STB.webp" },
      { code: "BTEN355-2STB", cat: "dimmers", name: "1-Gang 1000W Heavy Duty Dimmer (Silver)", desc: "1000W High Power Rotary Lighting Dimmer for Commercial Spaces", size: "86 x 86 mm", std: "BS EN 60669-2-1", img: "/assets/products/en_range/BTEN355-2STB.webp" },
      
      // 5. 13A & 15A Socket Outlets & Dual USB Fast Chargers
      { code: "BTEN405STB", cat: "socket_outlets", name: "13A Single Switched Socket (Silver)", desc: "13A 1-Gang BS 1363-2 Single Switched Power Outlet with Child Shutters", size: "86 x 86 mm", std: "BS 1363-2", img: "/assets/products/en_range/BTEN405STB.webp" },
      { code: "BTEN406STB", cat: "socket_outlets", name: "13A Twin Switched Socket (Silver)", desc: "13A 2-Gang BS 1363-2 Double Switched Socket with Safety Shutters", size: "146 x 86 mm", std: "BS 1363-2", img: "/assets/products/en_range/BTEN406STB.webp" },
      { code: "BTHY4113H-B-3.1ASTB", cat: "socket_outlets", name: "13A Single Socket + Dual USB 3.1A (Silver)", desc: "13A Single Switched Socket with Integrated Dual 3.1A USB Fast Charging", size: "86 x 86 mm", std: "BS 1363-2 / IEC 62368", img: "/assets/products/en_range/BTHY4113H-B-3.1ASTB.webp" },
      { code: "BTHY4121-B-3.1ASTB", cat: "socket_outlets", name: "13A Twin Socket + Dual USB 3.1A (Silver)", desc: "Twin 13A Double Switched Socket with Integrated Dual 3.1A Fast USB Ports", size: "146 x 86 mm", std: "BS 1363-2 / IEC 62368", img: "/assets/products/en_range/BTHY4121-B-3.1ASTB.webp" },
      { code: "BTEN429STB", cat: "socket_outlets", name: "15A Round Pin Switched Socket (Silver)", desc: "15A Heavy Duty BS 546 Round Pin AC Switched Power Socket Outlet", size: "86 x 86 mm", std: "BS 546", img: "/assets/products/en_range/BTEN429STB.webp" },
      
      // 6. Blank Connection Plates
      { code: "BTEN401STB", cat: "fcus", name: "1-Gang Blank Cover Plate (Silver)", desc: "86 x 86 mm Flush Architectural Blank Cover Plate", size: "86 x 86 mm", std: "BS 5733", img: "/assets/products/en_range/BTEN401STB.webp" },
      { code: "BTEN402STB", cat: "fcus", name: "2-Gang Wide Blank Cover Plate (Silver)", desc: "146 x 86 mm Double Width Flush Architectural Blank Cover Plate", size: "146 x 86 mm", std: "BS 5733", img: "/assets/products/en_range/BTEN402STB.webp" },
      
      // 7. Data & Telecom Outlets
      { code: "BTEN442STB", cat: "data_tv", name: "1-Gang RJ45 Cat6 Data Outlet (Silver)", desc: "1-Port Gigabit Ethernet Cat6 Data Wall Plate with Shutter", size: "86 x 86 mm", std: "TIA/EIA-568", img: "/assets/products/en_range/BTEN442STB.webp" },
      { code: "BTEN443STB", cat: "data_tv", name: "2-Gang RJ45 Cat6 Data Outlet (Silver)", desc: "2-Port Dual Gigabit Ethernet Cat6 Data Wall Plate with Shutters", size: "86 x 86 mm", std: "TIA/EIA-568", img: "/assets/products/en_range/BTEN443STB.webp" }
    ];

    function renderENRangeProducts(filter = 'all') {
      const grid = document.getElementById('en-products-grid');
      if (!grid) return;

      const items = filter === 'all' ? UNIQUE_EN_PRODUCTS : UNIQUE_EN_PRODUCTS.filter(p => p.cat === filter);
      grid.innerHTML = items.map(p => `
        <div class="en-product-card-item" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 16px; padding: 20px; display: flex; flex-direction: column; justify-content: space-between; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(0,0,0,0.02);" onmouseover="this.style.transform='translateY(-5px)'; this.style.borderColor='rgba(255,26,26,0.35)'; this.style.boxShadow='0 14px 28px rgba(255,26,26,0.09)';" onmouseout="this.style.transform='none'; this.style.borderColor='#E2E8F0'; this.style.boxShadow='0 4px 15px rgba(0,0,0,0.02)';">
          
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

    function filterENRangeProducts(filterKey, e) {
      if (e) {
        const btns = document.querySelectorAll('#en-gallery-filters .en-filter-btn');
        btns.forEach(b => {
          b.style.background = '#F1F5F9';
          b.style.color = '#334155';
          b.classList.remove('active');
        });
        e.target.style.background = 'var(--primary-red)';
        e.target.style.color = '#FFFFFF';
        e.target.classList.add('active');
      }
      renderENRangeProducts(filterKey);
    }

    document.addEventListener('DOMContentLoaded', () => {
      renderENRangeProducts('all');
    });
  </script>
"""

with open('product.html', 'r') as f:
    html = f.read()

# 1. Insert EN Section right after </section> of CW Range
cw_section_end = html.find('</section>', html.find('id="cw-catalog-section"')) + len('</section>')
html = html[:cw_section_end] + '\n\n' + en_section_html + html[cw_section_end:]

# 2. Insert EN Modal right after CW price modal
cw_modal_end = html.find('</div>\n  </div>', html.find('id="cw-price-modal"')) + len('</div>\n  </div>')
html = html[:cw_modal_end] + '\n\n' + en_modal_html + html[cw_modal_end:]

# 3. Insert EN Script right after CW Script
cw_script_end = html.find('</script>', html.find('const UNIQUE_CW_PRODUCTS = [')) + len('</script>')
html = html[:cw_script_end] + '\n\n' + en_script_html + html[cw_script_end:]

# 4. Update router logic in renderProductDetails and initialization
# Look for const cwCatalogSection = document.getElementById('cw-catalog-section');
html = html.replace(
    "const cwCatalogSection = document.getElementById('cw-catalog-section');",
    "const cwCatalogSection = document.getElementById('cw-catalog-section');\n        const enCatalogSection = document.getElementById('en-catalog-section');"
)

# In renderProductDetails:
old_routing_block = """        const reqRange = params.get('range');
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

new_routing_block = """        const reqRange = params.get('range');
        const isENRangeMain = (reqRange === 'EN Range' || product.range === 'EN Range' || product.name.startsWith('EN Range') || product.name.includes('BTEN') || product.name.includes('BTHY'));
        const isCWRangeMain = (reqRange === 'CW Range' || product.range === 'CW Range' || product.name.startsWith('CW Range') || product.name.includes('BTCW'));
        const isVRangeMain = (reqRange === 'V Range' || product.range === 'V Range' || product.name.startsWith('V Range'));
        const isWhiteRangeMain = (reqRange === 'W Range' || product.range === 'W Range' || product.name.startsWith('W Range') || product.name.startsWith('White Range'));

        if (isENRangeMain) {
          if (detailMain) detailMain.style.display = 'none';
          if (wCatalogSection) wCatalogSection.style.display = 'none';
          if (vCatalogSection) vCatalogSection.style.display = 'none';
          if (cwCatalogSection) cwCatalogSection.style.display = 'none';
          if (enCatalogSection) {
            enCatalogSection.style.display = 'block';
            renderENRangeProducts('all');
          }
          window.scrollTo(0, 0);
        } else if (isCWRangeMain) {
          if (detailMain) detailMain.style.display = 'none';
          if (wCatalogSection) wCatalogSection.style.display = 'none';
          if (vCatalogSection) vCatalogSection.style.display = 'none';
          if (enCatalogSection) enCatalogSection.style.display = 'none';
          if (cwCatalogSection) {
            cwCatalogSection.style.display = 'block';
            renderCWRangeProducts('all');
          }
          window.scrollTo(0, 0);
        } else if (isVRangeMain) {
          if (detailMain) detailMain.style.display = 'none';
          if (wCatalogSection) wCatalogSection.style.display = 'none';
          if (cwCatalogSection) cwCatalogSection.style.display = 'none';
          if (enCatalogSection) enCatalogSection.style.display = 'none';
          if (vCatalogSection) vCatalogSection.style.display = 'block';
          window.scrollTo(0, 0);
        } else if (isWhiteRangeMain) {
          if (detailMain) detailMain.style.display = 'none';
          if (vCatalogSection) vCatalogSection.style.display = 'none';
          if (cwCatalogSection) cwCatalogSection.style.display = 'none';
          if (enCatalogSection) enCatalogSection.style.display = 'none';
          if (wCatalogSection) wCatalogSection.style.display = 'block';
          window.scrollTo(0, 0);
        } else {
          if (detailMain) detailMain.style.display = 'block';
          if (wCatalogSection) wCatalogSection.style.display = 'none';
          if (vCatalogSection) vCatalogSection.style.display = 'none';
          if (cwCatalogSection) cwCatalogSection.style.display = 'none';
          if (enCatalogSection) enCatalogSection.style.display = 'none';
        }"""

html = html.replace(old_routing_block, new_routing_block)

# Initial query check routing
old_init_check = """      const isCWRange = (reqRange.toLowerCase().includes('cw range') || productName.toLowerCase().includes('cw range') || productName.toUpperCase().includes('BTCW') || reqRange.toLowerCase() === 'cw');
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
      }"""

new_init_check = """      const isENRange = (reqRange.toLowerCase().includes('en range') || productName.toLowerCase().includes('en range') || productName.toUpperCase().includes('BTEN') || productName.toUpperCase().includes('BTHY') || reqRange.toLowerCase() === 'en');
      const isCWRange = (reqRange.toLowerCase().includes('cw range') || productName.toLowerCase().includes('cw range') || productName.toUpperCase().includes('BTCW') || reqRange.toLowerCase() === 'cw');
      const isVRange = (reqRange.toLowerCase().includes('v range') || productName.toLowerCase().includes('v range') || productName.toUpperCase().includes('BTV') || reqRange.toLowerCase() === 'v');
      const isWRange = (reqRange.toLowerCase().includes('w range') || productName.toLowerCase().includes('w range') || productName.toLowerCase().includes('white range') || productName.toUpperCase().includes('W3') || productName.toUpperCase().includes('W4') || reqRange.toLowerCase() === 'w');

      if (isENRange) {
        if (detailMain) detailMain.style.display = 'none';
        if (wCatalogSection) wCatalogSection.style.display = 'none';
        if (vCatalogSection) vCatalogSection.style.display = 'none';
        if (cwCatalogSection) cwCatalogSection.style.display = 'none';
        if (enCatalogSection) {
          enCatalogSection.style.display = 'block';
          renderENRangeProducts('all');
        }
        window.scrollTo(0, 0);
        return;
      }

      if (isCWRange) {
        if (detailMain) detailMain.style.display = 'none';
        if (wCatalogSection) wCatalogSection.style.display = 'none';
        if (vCatalogSection) vCatalogSection.style.display = 'none';
        if (enCatalogSection) enCatalogSection.style.display = 'none';
        if (cwCatalogSection) {
          cwCatalogSection.style.display = 'block';
          renderCWRangeProducts('all');
        }
        window.scrollTo(0, 0);
        return;
      }"""

html = html.replace(old_init_check, new_init_check)

with open('product.html', 'w') as f:
    f.write(html)

print("Successfully integrated EN Range into product.html!")
