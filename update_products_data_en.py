import json

en_raw = [
    # 1. Plate Switches
    {"code_base": "BTEN302", "name_base": "1-Gang 2-Way Plate Switch", "desc_base": "10AX 250V~ 1-Gang 2-Way Switch with Architectural Profile", "size": "86 x 86 mm", "std": "BS EN 60669-1", "cat": "plate_switches"},
    {"code_base": "BTEN304", "name_base": "2-Gang 2-Way Plate Switch", "desc_base": "10AX 250V~ 2-Gang Dual Circuit Rocker Switch Plate", "size": "86 x 86 mm", "std": "BS EN 60669-1", "cat": "plate_switches"},
    {"code_base": "BTEN306", "name_base": "3-Gang 2-Way Plate Switch", "desc_base": "10AX 250V~ 3-Gang Multi-Zone Light Switch Plate", "size": "86 x 86 mm", "std": "BS EN 60669-1", "cat": "plate_switches"},
    {"code_base": "BTEN308", "name_base": "4-Gang 2-Way Wide Switch", "desc_base": "10AX 250V~ 4-Gang Quad Control Rocker Switch on Wide Plate", "size": "146 x 86 mm", "std": "BS EN 60669-1", "cat": "plate_switches"},

    # 2. Bell & Special Switches
    {"code_base": "BTEN317", "name_base": "1-Gang Bell Push Switch", "desc_base": "10A 250V~ Retractive Momentary Bell Push with Bell Symbol", "size": "86 x 86 mm", "std": "BS EN 60669-1", "cat": "bell_switches"},

    # 3. 20A & 45A High Power Isolator Switches
    {"code_base": "BTEN324", "name_base": "20A DP Switch + Neon", "desc_base": "20A Double Pole Heavy Duty Isolator Switch with Illuminated Neon", "size": "86 x 86 mm", "std": "BS EN 60669-2-1", "cat": "high_power"},
    {"code_base": "BTEN327", "name_base": "45A DP Switch + Neon", "desc_base": "45A Double Pole Main Isolator Switch with Red Neon Indicator", "size": "86 x 86 mm", "std": "BS EN 60669-2-1", "cat": "high_power"},
    {"code_base": "BTEN329", "name_base": "45A DP Large Plate Switch + Neon", "desc_base": "45A Large Rocker Double Pole Cooker Isolator Switch with Neon", "size": "86 x 146 mm", "std": "BS EN 60669-2-1", "cat": "high_power"},

    # 4. Rotary Dimmers & Fan Speed Controllers
    {"code_base": "BTEN350-2", "name_base": "1-Gang Rotary Dimmer (400W)", "desc_base": "400W Rotary Lighting Dimmer Switch with Smooth Push-On Action", "size": "86 x 86 mm", "std": "BS EN 60669-2-1", "cat": "dimmers"},
    {"code_base": "BTEN351", "name_base": "1-Gang Fan Speed Controller", "desc_base": "400W Stepless Fan Speed Regulator Controller Switch", "size": "86 x 86 mm", "std": "IEC 60669", "cat": "dimmers"},
    {"code_base": "BTEN353-2", "name_base": "2-Gang Rotary Dimmer", "desc_base": "Dual Channel 400W Rotary Lighting Dimmer Switch Plate", "size": "86 x 86 mm", "std": "BS EN 60669-2-1", "cat": "dimmers"},
    {"code_base": "BTEN355-2", "name_base": "1-Gang 1000W Heavy Duty Dimmer", "desc_base": "1000W High Power Rotary Lighting Dimmer for Commercial Spaces", "size": "86 x 86 mm", "std": "BS EN 60669-2-1", "cat": "dimmers"},

    # 5. 13A & 15A Socket Outlets & Dual USB Fast Chargers
    {"code_base": "BTEN405", "name_base": "13A Single Switched Socket", "desc_base": "13A 1-Gang BS 1363-2 Single Switched Power Outlet with Child Shutters", "size": "86 x 86 mm", "std": "BS 1363-2", "cat": "socket_outlets"},
    {"code_base": "BTEN406", "name_base": "13A Twin Switched Socket", "desc_base": "13A 2-Gang BS 1363-2 Double Switched Socket with Safety Shutters", "size": "146 x 86 mm", "std": "BS 1363-2", "cat": "socket_outlets"},
    {"code_base": "BTHY4113H-B-3.1A", "name_base": "13A Single Socket + Dual USB 3.1A", "desc_base": "13A Single Switched Socket with Integrated Dual 3.1A USB Fast Charging", "size": "86 x 86 mm", "std": "BS 1363-2 / IEC 62368", "cat": "socket_outlets"},
    {"code_base": "BTHY4121-B-3.1A", "name_base": "13A Twin Socket + Dual USB 3.1A", "desc_base": "Twin 13A Double Switched Socket with Integrated Dual 3.1A Fast USB Ports", "size": "146 x 86 mm", "std": "BS 1363-2 / IEC 62368", "cat": "socket_outlets"},
    {"code_base": "BTEN429", "name_base": "15A Round Pin Switched Socket", "desc_base": "15A Heavy Duty BS 546 Round Pin AC Switched Power Socket Outlet", "size": "86 x 86 mm", "std": "BS 546", "cat": "socket_outlets"},

    # 6. Blank Connection Plates
    {"code_base": "BTEN401", "name_base": "1-Gang Blank Cover Plate", "desc_base": "86 x 86 mm Flush Architectural Blank Cover Plate", "size": "86 x 86 mm", "std": "BS 5733", "cat": "fcus"},
    {"code_base": "BTEN402", "name_base": "2-Gang Wide Blank Cover Plate", "desc_base": "146 x 86 mm Double Width Flush Architectural Blank Cover Plate", "size": "146 x 86 mm", "std": "BS 5733", "cat": "fcus"},

    # 7. Data & Telecom Outlets
    {"code_base": "BTEN442", "name_base": "1-Gang RJ45 Cat6 Data Outlet", "desc_base": "1-Port Gigabit Ethernet Cat6 Data Wall Plate with Shutter", "size": "86 x 86 mm", "std": "TIA/EIA-568", "cat": "data_tv"},
    {"code_base": "BTEN443", "name_base": "2-Gang RJ45 Cat6 Data Outlet", "desc_base": "2-Port Dual Gigabit Ethernet Cat6 Data Wall Plate with Shutters", "size": "86 x 86 mm", "std": "TIA/EIA-568", "cat": "data_tv"}
]

# Generate both Silver (STB) and Gold (BRC) items
products_js = []
image_bg_entries = []

for item in en_raw:
    # Silver (STB)
    code_stb = f"{item['code_base']}STB"
    img_stb = f"/assets/products/en_range/{code_stb}.webp"
    products_js.append(f"""      {{
        name: "EN Range {item['name_base']} (Silver)",
        img: "{img_stb}",
        desc: "{item['desc_base']} in Satin Brushed Steel finish (Model {code_stb}).",
        specs: ["{item['std']} Compliant", "{item['size']}", "Satin Brushed Steel"],
        range: "EN Range"
      }}""")
    image_bg_entries.append(f'  "{img_stb}": "#ffffff",')

    # Gold (BRC)
    code_brc = f"{item['code_base']}BRC"
    img_brc = f"/assets/products/en_range/{code_brc}.webp"
    products_js.append(f"""      {{
        name: "EN Range {item['name_base']} (Gold)",
        img: "{img_brc}",
        desc: "{item['desc_base']} in Brushed Brass / Gold finish (Model {code_brc}).",
        specs: ["{item['std']} Compliant", "{item['size']}", "Brushed Brass Gold"],
        range: "EN Range"
      }}""")
    image_bg_entries.append(f'  "{img_brc}": "#ffffff",')

with open('products-data.js', 'r') as f:
    content = f.read()

# Replace EN Range block in switches category
start_marker = 'name: "EN Range Single Switched Socket",'
start_idx = content.rfind('{', 0, content.find(start_marker))
end_marker = 'name: "EN Range 3-Gang Switch",'
end_idx = content.find('},\n', content.find(end_marker)) + 3

new_items_block = ',\n'.join(products_js) + ',\n'
updated_content = content[:start_idx] + new_items_block + content[end_idx:]

# Insert IMAGE_BG_MAP entries right after IMAGE_BG_MAP = {
bg_insert_pos = updated_content.find('export const IMAGE_BG_MAP = {\n') + len('export const IMAGE_BG_MAP = {\n')
bg_block = '\n'.join(image_bg_entries) + '\n'
updated_content = updated_content[:bg_insert_pos] + bg_block + updated_content[bg_insert_pos:]

with open('products-data.js', 'w') as f:
    f.write(updated_content)

print(f"Successfully updated products-data.js with {len(products_js)} EN Range items and image BG maps!")
