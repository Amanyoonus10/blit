import os
from PIL import Image
from fpdf import FPDF

# Convert webp/png to temporary thumbnail for FPDF compatibility & performance
os.makedirs('/tmp/blit_cw_thumbnails', exist_ok=True)

def prepare_thumb(path):
    if not os.path.exists(path):
        return None
    thumb_name = os.path.splitext(os.path.basename(path))[0] + '_thumb.jpg'
    out_path = os.path.join('/tmp/blit_cw_thumbnails', thumb_name)
    with Image.open(path) as img:
        img = img.convert('RGBA')
        bg = Image.new('RGB', img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[3])
        bg.thumbnail((320, 320), Image.Resampling.LANCZOS)
        bg.save(out_path, 'JPEG', quality=88, optimize=True)
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
        self.cell(85, 8, 'CW RANGE SPECIFICATION CATALOGUE 2026', 0, 0, 'R')
        
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

CW_CATEGORIES = [
    {
        "cat_title": "1. Plate Switches Collection (10AX 250V~ BS EN 60669-1)",
        "items": [
            {"code": "BTCW3011-WHI", "desc": "1 Gang 1 Way Switch", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW3011-WHI.webp"},
            {"code": "BTCW3012-WHI", "desc": "1 Gang 2 Way Switch", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW3012-WHI.webp"},
            {"code": "BTCW3213-WHI", "desc": "1 Gang Intermediate Switch", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW3213-WHI.webp"},
            {"code": "BTCW3022-WHI", "desc": "2 Gang 2 Way Switch", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW3022-WHI.webp"},
            {"code": "BTCW3032-WHI", "desc": "3 Gang 2 Way Switch", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW3032-WHI.webp"},
            {"code": "BTCW3042-WHI", "desc": "4 Gang 2 Way Switch", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW3042-WHI.webp"}
        ]
    },
    {
        "cat_title": "2. Bell & Special Switches",
        "items": [
            {"code": "BTCW3016BEL-WHI", "desc": "1 Gang Retractive Bell Push Switch", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW3016BEL-WHI.webp"}
        ]
    },
    {
        "cat_title": "3. 20A & 45A High Power Isolator Switches",
        "items": [
            {"code": "BTCW3341-WHI", "desc": "20A DP Switch + Neon Indicator", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW3341-WHI.webp"},
            {"code": "BTCW3267-WHI", "desc": "45A DP Switch + Neon Indicator", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW3267-WHI.webp"}
        ]
    },
    {
        "cat_title": "4. Rotary Dimmers & Speed Controllers",
        "items": [
            {"code": "BTCW3501-WHI", "desc": "1 Gang 400W/500W Rotary Dimmer", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW3501-WHI.webp"},
            {"code": "BTCW3502-WHI", "desc": "2 Gang Rotary Dimmer (Wide Plate)", "dim": "146 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW3502-WHI.webp"}
        ]
    },
    {
        "cat_title": "5. 13A & 15A Socket Outlets & Dual USB Fast Chargers",
        "items": [
            {"code": "BTCW4010C-WHI", "desc": "1 Gang 13A Single Switched Socket", "dim": "86 x 86 mm", "std": "BS 1363-2", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW4010C-WHI.webp"},
            {"code": "BTCW4030L-WHI", "desc": "2 Gang 13A Twin Switched Socket + Neon", "dim": "146 x 86 mm", "std": "BS 1363-2", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW4030L-WHI.webp"},
            {"code": "BTCW4113H-3.1A-WHI", "desc": "13A Single Socket + Dual USB 3.1A", "dim": "86 x 86 mm", "std": "BS 1363-2 / IEC 62368", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW4113H-3.1A-WHI.webp"},
            {"code": "BTCW4120-3.1A-WHI", "desc": "Twin 13A Socket + Dual USB 3.1A", "dim": "146 x 86 mm", "std": "BS 1363-2 / IEC 62368", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW4120-3.1A-WHI.webp"},
            {"code": "BTCW4210-WHI", "desc": "15A Round Pin Switched Socket", "dim": "86 x 86 mm", "std": "BS 546", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW4210-WHI.webp"}
        ]
    },
    {
        "cat_title": "6. Universal Multi-Function & Type-C PD Fast Charging Sockets",
        "items": [
            {"code": "BTCW4242-20W-WHI", "desc": "1G Multi-Socket + 20W PD Type-C & USB", "dim": "86 x 86 mm", "std": "IEC 60884 / IEC 62368", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW4242-20W-WHI.webp"},
            {"code": "BTCW4252-20W-WHI", "desc": "2G Multi-Socket + 20W PD Type-C & USB", "dim": "146 x 86 mm", "std": "IEC 60884 / IEC 62368", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW4252-20W-WHI.webp"}
        ]
    },
    {
        "cat_title": "7. Fused Connection Units (FCUs) & Cable Outlet Plates",
        "items": [
            {"code": "BTCW3415-WHI", "desc": "13A Unswitched Fused Connection Unit", "dim": "86 x 86 mm", "std": "BS 1363-4", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW3415-WHI.webp"},
            {"code": "BTCW3416LED-WHI", "desc": "13A Switched FCU Spur + LED Indicator", "dim": "86 x 86 mm", "std": "BS 1363-4", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW3416LED-WHI.webp"},
            {"code": "BTCW4620-WHI", "desc": "20A Heavy Duty Cable Connection Plate", "dim": "86 x 86 mm", "std": "BS 5733", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW4620-WHI.webp"},
            {"code": "BTCW4645-WHI", "desc": "45A High Current Cable Connection Plate", "dim": "86 x 86 mm", "std": "BS 5733", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW4645-WHI.webp"}
        ]
    },
    {
        "cat_title": "8. Data, Telecom & TV Multimedia Outlets",
        "items": [
            {"code": "BTCW4311-WHI", "desc": "Coaxial TV & Satellite Multimedia Socket", "dim": "146 x 86 mm", "std": "BS 3041", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW4311-WHI.webp"},
            {"code": "BTCW442-WHI", "desc": "1 Gang RJ45 Cat6 Gigabit Data Outlet", "dim": "86 x 86 mm", "std": "TIA/EIA-568", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW442-WHI.webp"},
            {"code": "BTCW443-WHI", "desc": "2 Gang RJ45 Cat6 Gigabit Data Outlet", "dim": "86 x 86 mm", "std": "TIA/EIA-568", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/cw_range/BTCW443-WHI.webp"}
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
pdf.cell(170, 8, 'CW RANGE ARCHITECTURAL SWITCHES & SOCKETS', 0, 1, 'L')
pdf.set_font('Helvetica', '', 9.5)
pdf.set_text_color(71, 85, 105)
pdf.set_x(20)
pdf.cell(170, 6, 'Complete Product Specifications, High-Resolution Imagery & International Compliance Reference', 0, 1, 'L')
pdf.ln(8)

for cat in CW_CATEGORIES:
    if pdf.get_y() > 240:
        pdf.add_page()
    
    pdf.set_fill_color(15, 23, 42)
    pdf.rect(15, pdf.get_y(), 180, 7.5, 'F')
    pdf.set_font('Helvetica', 'B', 9.5)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(18, pdf.get_y() + 1)
    pdf.cell(174, 5.5, cat["cat_title"], 0, 1, 'L')
    pdf.ln(3)

    pdf.set_fill_color(241, 245, 249)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_text_color(51, 65, 85)
    
    pdf.set_x(15)
    pdf.cell(24, 6, "IMAGE", 1, 0, 'C', True)
    pdf.cell(32, 6, "MODEL CODE", 1, 0, 'L', True)
    pdf.cell(64, 6, "DESCRIPTION", 1, 0, 'L', True)
    pdf.cell(26, 6, "DIMENSION", 1, 0, 'C', True)
    pdf.cell(34, 6, "STANDARD", 1, 1, 'C', True)

    for item in cat["items"]:
        if pdf.get_y() > 255:
            pdf.add_page()
            pdf.set_fill_color(241, 245, 249)
            pdf.set_font('Helvetica', 'B', 8)
            pdf.set_text_color(51, 65, 85)
            pdf.set_x(15)
            pdf.cell(24, 6, "IMAGE", 1, 0, 'C', True)
            pdf.cell(32, 6, "MODEL CODE", 1, 0, 'L', True)
            pdf.cell(64, 6, "DESCRIPTION", 1, 0, 'L', True)
            pdf.cell(26, 6, "DIMENSION", 1, 0, 'C', True)
            pdf.cell(34, 6, "STANDARD", 1, 1, 'C', True)

        row_y = pdf.get_y()
        row_h = 16

        pdf.set_draw_color(226, 232, 240)
        pdf.rect(15, row_y, 24, row_h)
        pdf.rect(39, row_y, 32, row_h)
        pdf.rect(71, row_y, 64, row_h)
        pdf.rect(135, row_y, 26, row_h)
        pdf.rect(161, row_y, 34, row_h)

        img_path = prepare_thumb(item["img"])
        if img_path and os.path.exists(img_path):
            pdf.image(img_path, x=17.5, y=row_y + 1, w=19, h=14)

        pdf.set_font('Helvetica', 'B', 8.5)
        pdf.set_text_color(255, 26, 26)
        pdf.set_xy(40.5, row_y + 5)
        pdf.cell(29, 6, item["code"], 0, 0, 'L')

        pdf.set_font('Helvetica', '', 8)
        pdf.set_text_color(15, 23, 42)
        pdf.set_xy(73, row_y + 5)
        pdf.cell(60, 6, item["desc"], 0, 0, 'L')

        pdf.set_font('Helvetica', '', 8)
        pdf.set_text_color(71, 85, 105)
        pdf.set_xy(135, row_y + 5)
        pdf.cell(26, 6, item["dim"], 0, 0, 'C')

        pdf.set_font('Helvetica', 'B', 7.5)
        pdf.set_text_color(51, 65, 85)
        pdf.set_xy(161, row_y + 5)
        pdf.cell(34, 6, item["std"], 0, 0, 'C')

        pdf.set_y(row_y + row_h)

    pdf.ln(5)

os.makedirs('/Users/amanyoonus/Desktop/Blit/assets/catalogues', exist_ok=True)
out_pdf = '/Users/amanyoonus/Desktop/Blit/assets/catalogues/BLIT_CW_Range_Catalogue_2026.pdf'
pdf.output(out_pdf)

public_pdf = '/Users/amanyoonus/Desktop/Blit/public/assets/catalogues/BLIT_CW_Range_Catalogue_2026.pdf'
os.makedirs(os.path.dirname(public_pdf), exist_ok=True)
import shutil
shutil.copyfile(out_pdf, public_pdf)

size_mb = os.path.getsize(out_pdf) / (1024 * 1024)
print(f"CW Range PDF catalogue successfully generated: {size_mb:.2f} MB")
