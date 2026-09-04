import os
from PIL import Image
from fpdf import FPDF

# Convert webp to temporary jpg/png for FPDF compatibility if needed
os.makedirs('/tmp/blit_pdf_assets', exist_ok=True)

def prepare_img(path):
    if not os.path.exists(path):
        return None
    out_path = os.path.join('/tmp/blit_pdf_assets', os.path.basename(path).replace('.webp', '.png'))
    with Image.open(path) as img:
        # If RGBA, paste on white background for clean PDF rendering
        if img.mode == 'RGBA':
            bg = Image.new('RGB', img.size, (255, 255, 255))
            bg.paste(img, mask=img.split()[3])
            bg.save(out_path, 'PNG')
        else:
            img.convert('RGB').save(out_path, 'PNG')
    return out_path

class PDF(FPDF):
    def header(self):
        # Top Red Accent Bar
        self.set_fill_color(255, 26, 26)
        self.rect(0, 0, 210, 5, 'F')
        
        # Logo text
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(15, 23, 42)
        self.set_xy(15, 10)
        self.cell(40, 8, 'BLIT ELECTRIC', 0, 0, 'L')
        
        # Header subtitle
        self.set_font('Helvetica', '', 8.5)
        self.set_text_color(100, 116, 139)
        self.set_xy(110, 10)
        self.cell(85, 8, 'V RANGE SPECIFICATION CATALOGUE 2026', 0, 0, 'R')
        
        # Separator line
        self.set_draw_color(226, 232, 240)
        self.line(15, 20, 195, 20)
        self.ln(16)

    def footer(self):
        self.set_y(-14)
        self.set_font('Helvetica', '', 8)
        self.set_text_color(148, 163, 184)
        self.cell(90, 8, 'Blit Electrical Hardware | info@blitelectric.com', 0, 0, 'L')
        self.cell(90, 8, f'Page {self.page_no()}', 0, 0, 'R')

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=18)

# Product catalog data grouped by category
CATEGORIES = [
    {
        "cat_title": "1. Plate Switches Collection (10AX 250V~ BS EN 60669-1)",
        "items": [
            {"code": "BTV301", "desc": "1 Gang 1 Way Switch", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV301.png"},
            {"code": "BTV302", "desc": "1 Gang 2 Way Switch", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV302.png"},
            {"code": "BTV313", "desc": "1 Gang Intermediate Switch", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV313.png"},
            {"code": "BTV303", "desc": "2 Gang 1 Way Switch", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV303.png"},
            {"code": "BTV304", "desc": "2 Gang 2 Way Switch", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV304.png"},
            {"code": "BTV305", "desc": "3 Gang 1 Way Switch", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV305.png"},
            {"code": "BTV306", "desc": "3 Gang 2 Way Switch", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV306.png"},
            {"code": "BTV307", "desc": "4 Gang 1 Way Switch (Wide)", "dim": "146 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV307.png"},
            {"code": "BTV307X", "desc": "4 Gang 2 Way Switch (Square)", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV307X.png"},
            {"code": "BTV309", "desc": "6 Gang 1 Way Switch (Wide)", "dim": "146 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV309.png"}
        ]
    },
    {
        "cat_title": "2. Bell & Special Switches",
        "items": [
            {"code": "BTV317", "desc": "1 Gang Retractive Bell Switch", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV317.png"}
        ]
    },
    {
        "cat_title": "3. 20A & 45A High Power Switches & Cooker Units",
        "items": [
            {"code": "BTV324", "desc": "20A DP Switch + Neon Indicator", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV324.png"},
            {"code": "BTV327", "desc": "45A DP Switch + Neon Indicator", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV327.png"},
            {"code": "BTV329", "desc": "45A DP Switch (Large Plate)", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV329.png"},
            {"code": "BTV331", "desc": "45A Cooker Unit + 13A Socket", "dim": "146 x 86 mm", "std": "BS 4177", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV331.png"}
        ]
    },
    {
        "cat_title": "4. Dimmers & Fan Speed Controllers",
        "items": [
            {"code": "BTV350-2", "desc": "400W/500W Rotary Dimmer", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV350-2.png"},
            {"code": "BTV351", "desc": "400W Fan Speed Controller", "dim": "86 x 86 mm", "std": "IEC 60669", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV351.png"},
            {"code": "BTV353-2", "desc": "2 Gang 400W Rotary Dimmer", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV353-2.png"},
            {"code": "BTV355", "desc": "500W Rotary Dimmer Switch", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV355.png"},
            {"code": "BTV359", "desc": "1000W Master Rotary Dimmer", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV359.png"}
        ]
    },
    {
        "cat_title": "5. 13A Socket Outlets & Dual USB 3.1A Fast Chargers",
        "items": [
            {"code": "BTV4010B", "desc": "1 Gang 13A Switched Socket", "dim": "86 x 86 mm", "std": "BS 1363-2", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV4010B.png"},
            {"code": "BTV4030B", "desc": "2 Gang 13A Twin Switched Socket", "dim": "146 x 86 mm", "std": "BS 1363-2", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV4030B.png"},
            {"code": "BTV4113-3.1A", "desc": "13A Socket + Dual USB 3.1A", "dim": "86 x 86 mm", "std": "BS 1363-2 / IEC 62368", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV4113-3.1A.png"},
            {"code": "BTV4121-3.1A", "desc": "Twin 13A Socket + Dual USB 3.1A", "dim": "146 x 86 mm", "std": "BS 1363-2 / IEC 62368", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV4121-3.1A.png"}
        ]
    },
    {
        "cat_title": "6. Universal Multi-Function & Round Pin Sockets",
        "items": [
            {"code": "BTV4243-3.1A", "desc": "13A Multi-Socket + 3.1A USB", "dim": "86 x 86 mm", "std": "IEC 60884 / IEC 62368", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV4243-3.1A.png"},
            {"code": "BTV4250", "desc": "2 Gang Universal Multi-Socket", "dim": "146 x 86 mm", "std": "IEC 60884", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV4250.png"},
            {"code": "BTV4253-3.1A", "desc": "Twin Multi-Socket + 3.1A USB", "dim": "146 x 86 mm", "std": "IEC 60884 / IEC 62368", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV4253-3.1A.png"},
            {"code": "BTV429", "desc": "15A Round Pin Switched Socket", "dim": "86 x 86 mm", "std": "BS 546", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV429.png"},
            {"code": "BTV480", "desc": "10A/13A 1G Multi-Socket", "dim": "86 x 86 mm", "std": "IEC 60884", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV480.png"},
            {"code": "BTV482", "desc": "13A 1G Switched Multi + Neon", "dim": "86 x 86 mm", "std": "BS 1363 / IEC 60884", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV482.png"},
            {"code": "BTV484", "desc": "13A 2G Switched Multi-Socket", "dim": "146 x 86 mm", "std": "BS 1363 / IEC 60884", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV484.png"}
        ]
    },
    {
        "cat_title": "7. FCUs & Cable Connection Plates",
        "items": [
            {"code": "BTV416", "desc": "13A Unswitched FCU Spur", "dim": "86 x 86 mm", "std": "BS 1363-4", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV416.png"},
            {"code": "BTV422", "desc": "13A Switched FCU + Neon", "dim": "86 x 86 mm", "std": "BS 1363-4", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV422.png"},
            {"code": "BTV401", "desc": "1 Gang Blank Cover Plate", "dim": "86 x 86 mm", "std": "BS 5733", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV401.png"},
            {"code": "BTV402", "desc": "2 Gang Blank Cover Plate", "dim": "146 x 86 mm", "std": "BS 5733", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV402.png"},
            {"code": "BTV820", "desc": "20A Cable Connection Plate", "dim": "86 x 86 mm", "std": "BS 5733", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV820.png"},
            {"code": "BTV821", "desc": "45A Cable Connection Plate", "dim": "86 x 86 mm", "std": "BS 5733", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV821.png"}
        ]
    },
    {
        "cat_title": "8. Data & Multimedia Outlets",
        "items": [
            {"code": "BTV442", "desc": "1G RJ45 Cat6 Data Outlet", "dim": "86 x 86 mm", "std": "TIA/EIA-568", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV442.png"},
            {"code": "BTV443", "desc": "2G RJ45 Cat6 Data Outlet", "dim": "86 x 86 mm", "std": "TIA/EIA-568", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/v_range/BTV443.png"}
        ]
    }
]

pdf.add_page()

# Title Header on Page 1
pdf.set_fill_color(248, 250, 252)
pdf.rect(15, 24, 180, 24, 'F')
pdf.set_font('Helvetica', 'B', 16)
pdf.set_text_color(15, 23, 42)
pdf.set_xy(20, 28)
pdf.cell(170, 8, 'V RANGE LUXURY BRUSHED METAL COLLECTION', 0, 1, 'L')
pdf.set_font('Helvetica', '', 9.5)
pdf.set_text_color(71, 85, 105)
pdf.set_x(20)
pdf.cell(170, 6, 'Complete Product Specifications, High-Resolution Imagery & International Compliance Reference', 0, 1, 'L')
pdf.ln(8)

for cat in CATEGORIES:
    # Category Header Bar
    if pdf.get_y() > 240:
        pdf.add_page()
    
    pdf.set_fill_color(15, 23, 42)
    pdf.rect(15, pdf.get_y(), 180, 7.5, 'F')
    pdf.set_font('Helvetica', 'B', 9.5)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(18, pdf.get_y() + 1)
    pdf.cell(174, 5.5, cat["cat_title"], 0, 1, 'L')
    pdf.ln(3)

    # Table Header
    pdf.set_fill_color(241, 245, 249)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_text_color(51, 65, 85)
    
    pdf.set_x(15)
    pdf.cell(24, 6, "IMAGE", 1, 0, 'C', True)
    pdf.cell(28, 6, "MODEL CODE", 1, 0, 'L', True)
    pdf.cell(68, 6, "DESCRIPTION", 1, 0, 'L', True)
    pdf.cell(26, 6, "DIMENSION", 1, 0, 'C', True)
    pdf.cell(34, 6, "STANDARD", 1, 1, 'C', True)

    # Rows
    for item in cat["items"]:
        if pdf.get_y() > 255:
            pdf.add_page()
            # Re-draw Table Header
            pdf.set_fill_color(241, 245, 249)
            pdf.set_font('Helvetica', 'B', 8)
            pdf.set_text_color(51, 65, 85)
            pdf.set_x(15)
            pdf.cell(24, 6, "IMAGE", 1, 0, 'C', True)
            pdf.cell(28, 6, "MODEL CODE", 1, 0, 'L', True)
            pdf.cell(68, 6, "DESCRIPTION", 1, 0, 'L', True)
            pdf.cell(26, 6, "DIMENSION", 1, 0, 'C', True)
            pdf.cell(34, 6, "STANDARD", 1, 1, 'C', True)

        row_y = pdf.get_y()
        row_h = 16

        # Draw cell borders
        pdf.set_draw_color(226, 232, 240)
        pdf.rect(15, row_y, 24, row_h)
        pdf.rect(39, row_y, 28, row_h)
        pdf.rect(67, row_y, 68, row_h)
        pdf.rect(135, row_y, 26, row_h)
        pdf.rect(161, row_y, 34, row_h)

        # Image thumbnail
        img_path = prepare_img(item["img"])
        if img_path and os.path.exists(img_path):
            pdf.image(img_path, x=17.5, y=row_y + 1, w=19, h=14)

        # Model Code
        pdf.set_font('Helvetica', 'B', 8.5)
        pdf.set_text_color(255, 26, 26)
        pdf.set_xy(41, row_y + 5)
        pdf.cell(24, 6, item["code"], 0, 0, 'L')

        # Description
        pdf.set_font('Helvetica', '', 8)
        pdf.set_text_color(15, 23, 42)
        pdf.set_xy(69, row_y + 5)
        pdf.cell(64, 6, item["desc"], 0, 0, 'L')

        # Dimension
        pdf.set_font('Helvetica', '', 8)
        pdf.set_text_color(71, 85, 105)
        pdf.set_xy(135, row_y + 5)
        pdf.cell(26, 6, item["dim"], 0, 0, 'C')

        # Standard
        pdf.set_font('Helvetica', 'B', 7.5)
        pdf.set_text_color(51, 65, 85)
        pdf.set_xy(161, row_y + 5)
        pdf.cell(34, 6, item["std"], 0, 0, 'C')

        pdf.set_y(row_y + row_h)

    pdf.ln(5)

out_pdf = '/Users/amanyoonus/Desktop/Blit/assets/catalogues/BLIT_V_Range_Catalogue_2026.pdf'
pdf.output(out_pdf)

# Also copy to public directory for production build
public_pdf = '/Users/amanyoonus/Desktop/Blit/public/assets/catalogues/BLIT_V_Range_Catalogue_2026.pdf'
os.makedirs(os.path.dirname(public_pdf), exist_ok=True)
import shutil
shutil.copyfile(out_pdf, public_pdf)

print(f"Rich PDF catalogue with all images created successfully at {out_pdf} and {public_pdf}!")
print(f"PDF file size: {os.path.getsize(out_pdf)} bytes")
