import os
from PIL import Image
from fpdf import FPDF
import shutil

os.makedirs('/tmp/blit_en_thumbnails', exist_ok=True)

def prepare_thumb(path):
    if not os.path.exists(path):
        return None
    thumb_name = os.path.splitext(os.path.basename(path))[0] + '_thumb.jpg'
    out_path = os.path.join('/tmp/blit_en_thumbnails', thumb_name)
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
        self.cell(85, 8, 'EN RANGE SPECIFICATION CATALOGUE 2026', 0, 0, 'R')
        
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

EN_CATEGORIES = [
    {
        "cat_title": "1. Plate Switches Collection (10AX 250V~ BS EN 60669-1)",
        "items": [
            {"code": "BTEN302STB", "desc": "1 Gang 2 Way Switch (Silver)", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN302STB.webp"},
            {"code": "BTEN302BRC", "desc": "1 Gang 2 Way Switch (Gold)", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN302BRC.webp"},
            {"code": "BTEN304STB", "desc": "2 Gang 2 Way Switch (Silver)", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN304STB.webp"},
            {"code": "BTEN304BRC", "desc": "2 Gang 2 Way Switch (Gold)", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN304BRC.webp"},
            {"code": "BTEN306STB", "desc": "3 Gang 2 Way Switch (Silver)", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN306STB.webp"},
            {"code": "BTEN306BRC", "desc": "3 Gang 2 Way Switch (Gold)", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN306BRC.webp"},
            {"code": "BTEN308STB", "desc": "4 Gang 2 Way Wide Switch (Silver)", "dim": "146 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN308STB.webp"},
            {"code": "BTEN308BRC", "desc": "4 Gang 2 Way Wide Switch (Gold)", "dim": "146 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN308BRC.webp"}
        ]
    },
    {
        "cat_title": "2. Bell & Special Switches",
        "items": [
            {"code": "BTEN317STB", "desc": "1 Gang Retractive Bell Push (Silver)", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN317STB.webp"},
            {"code": "BTEN317BRC", "desc": "1 Gang Retractive Bell Push (Gold)", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN317BRC.webp"}
        ]
    },
    {
        "cat_title": "3. 20A & 45A High Power Isolator Switches",
        "items": [
            {"code": "BTEN324STB", "desc": "20A DP Switch + Neon (Silver)", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN324STB.webp"},
            {"code": "BTEN324BRC", "desc": "20A DP Switch + Neon (Gold)", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN324BRC.webp"},
            {"code": "BTEN327STB", "desc": "45A DP Switch + Neon (Silver)", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN327STB.webp"},
            {"code": "BTEN327BRC", "desc": "45A DP Switch + Neon (Gold)", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN327BRC.webp"},
            {"code": "BTEN329STB", "desc": "45A DP Large Plate Switch + Neon (Silver)", "dim": "86 x 146 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN329STB.webp"},
            {"code": "BTEN329BRC", "desc": "45A DP Large Plate Switch + Neon (Gold)", "dim": "86 x 146 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN329BRC.webp"}
        ]
    },
    {
        "cat_title": "4. Rotary Dimmers & Fan Speed Controllers",
        "items": [
            {"code": "BTEN350-2STB", "desc": "1 Gang 400W Rotary Dimmer (Silver)", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN350-2STB.webp"},
            {"code": "BTEN350-2BRC", "desc": "1 Gang 400W Rotary Dimmer (Gold)", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN350-2BRC.webp"},
            {"code": "BTEN351STB", "desc": "1 Gang 400W Fan Speed Controller (Silver)", "dim": "86 x 86 mm", "std": "IEC 60669", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN351STB.webp"},
            {"code": "BTEN351BRC", "desc": "1 Gang 400W Fan Speed Controller (Gold)", "dim": "86 x 86 mm", "std": "IEC 60669", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN351BRC.webp"},
            {"code": "BTEN353-2STB", "desc": "2 Gang 400W Rotary Dimmer (Silver)", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN353-2STB.webp"},
            {"code": "BTEN353-2BRC", "desc": "2 Gang 400W Rotary Dimmer (Gold)", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN353-2BRC.webp"},
            {"code": "BTEN355-2STB", "desc": "1 Gang 1000W Heavy Duty Dimmer (Silver)", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN355-2STB.webp"},
            {"code": "BTEN355-2BRC", "desc": "1 Gang 1000W Heavy Duty Dimmer (Gold)", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN355-2BRC.webp"}
        ]
    },
    {
        "cat_title": "5. 13A & 15A Socket Outlets & Dual USB Fast Chargers",
        "items": [
            {"code": "BTEN405STB", "desc": "1 Gang 13A Single Switched Socket (Silver)", "dim": "86 x 86 mm", "std": "BS 1363-2", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN405STB.webp"},
            {"code": "BTEN405BRC", "desc": "1 Gang 13A Single Switched Socket (Gold)", "dim": "86 x 86 mm", "std": "BS 1363-2", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN405BRC.webp"},
            {"code": "BTEN406STB", "desc": "2 Gang 13A Twin Switched Socket (Silver)", "dim": "146 x 86 mm", "std": "BS 1363-2", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN406STB.webp"},
            {"code": "BTEN406BRC", "desc": "2 Gang 13A Twin Switched Socket (Gold)", "dim": "146 x 86 mm", "std": "BS 1363-2", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN406BRC.webp"},
            {"code": "BTHY4113H-B-3.1ASTB", "desc": "13A Single Socket + Dual USB 3.1A (Silver)", "dim": "86 x 86 mm", "std": "BS 1363-2 / IEC 62368", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTHY4113H-B-3.1ASTB.webp"},
            {"code": "BTHY4113H-B-3.1ABRC", "desc": "13A Single Socket + Dual USB 3.1A (Gold)", "dim": "86 x 86 mm", "std": "BS 1363-2 / IEC 62368", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTHY4113H-B-3.1ABRC.webp"},
            {"code": "BTHY4121-B-3.1ASTB", "desc": "Twin 13A Socket + Dual USB 3.1A (Silver)", "dim": "146 x 86 mm", "std": "BS 1363-2 / IEC 62368", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTHY4121-B-3.1ASTB.webp"},
            {"code": "BTHY4121-B-3.1ABRC", "desc": "Twin 13A Socket + Dual USB 3.1A (Gold)", "dim": "146 x 86 mm", "std": "BS 1363-2 / IEC 62368", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTHY4121-B-3.1ABRC.webp"},
            {"code": "BTEN429STB", "desc": "15A Round Pin Switched Socket (Silver)", "dim": "86 x 86 mm", "std": "BS 546", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN429STB.webp"},
            {"code": "BTEN429BRC", "desc": "15A Round Pin Switched Socket (Gold)", "dim": "86 x 86 mm", "std": "BS 546", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN429BRC.webp"}
        ]
    },
    {
        "cat_title": "6. Blank Connection Plates",
        "items": [
            {"code": "BTEN401STB", "desc": "1 Gang Flush Blank Plate (Silver)", "dim": "86 x 86 mm", "std": "BS 5733", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN401STB.webp"},
            {"code": "BTEN401BRC", "desc": "1 Gang Flush Blank Plate (Gold)", "dim": "86 x 86 mm", "std": "BS 5733", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN401BRC.webp"},
            {"code": "BTEN402STB", "desc": "2 Gang Wide Blank Plate (Silver)", "dim": "146 x 86 mm", "std": "BS 5733", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN402STB.webp"},
            {"code": "BTEN402BRC", "desc": "2 Gang Wide Blank Plate (Gold)", "dim": "146 x 86 mm", "std": "BS 5733", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN402BRC.webp"}
        ]
    },
    {
        "cat_title": "7. Data & Telecom Outlets",
        "items": [
            {"code": "BTEN442STB", "desc": "1 Gang RJ45 Cat6 Data Outlet (Silver)", "dim": "86 x 86 mm", "std": "TIA/EIA-568", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN442STB.webp"},
            {"code": "BTEN442BRC", "desc": "1 Gang RJ45 Cat6 Data Outlet (Gold)", "dim": "86 x 86 mm", "std": "TIA/EIA-568", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN442BRC.webp"},
            {"code": "BTEN443STB", "desc": "2 Gang RJ45 Cat6 Data Outlet (Silver)", "dim": "86 x 86 mm", "std": "TIA/EIA-568", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN443STB.webp"},
            {"code": "BTEN443BRC", "desc": "2 Gang RJ45 Cat6 Data Outlet (Gold)", "dim": "86 x 86 mm", "std": "TIA/EIA-568", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/en_range/BTEN443BRC.webp"}
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
pdf.cell(170, 8, 'EN RANGE ARCHITECTURAL SWITCHES & SOCKETS', 0, 1, 'L')
pdf.set_font('Helvetica', '', 9.5)
pdf.set_text_color(71, 85, 105)
pdf.set_x(20)
pdf.cell(170, 6, 'Complete Product Specifications, High-Resolution Imagery & International Compliance Reference', 0, 1, 'L')
pdf.ln(8)

for cat in EN_CATEGORIES:
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
    pdf.cell(34, 6, "MODEL CODE", 1, 0, 'L', True)
    pdf.cell(62, 6, "DESCRIPTION", 1, 0, 'L', True)
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
            pdf.cell(34, 6, "MODEL CODE", 1, 0, 'L', True)
            pdf.cell(62, 6, "DESCRIPTION", 1, 0, 'L', True)
            pdf.cell(26, 6, "DIMENSION", 1, 0, 'C', True)
            pdf.cell(34, 6, "STANDARD", 1, 1, 'C', True)

        row_y = pdf.get_y()
        row_h = 16

        pdf.set_draw_color(226, 232, 240)
        pdf.rect(15, row_y, 24, row_h)
        pdf.rect(39, row_y, 34, row_h)
        pdf.rect(73, row_y, 62, row_h)
        pdf.rect(135, row_y, 26, row_h)
        pdf.rect(161, row_y, 34, row_h)

        img_path = prepare_thumb(item["img"])
        if img_path and os.path.exists(img_path):
            pdf.image(img_path, x=17.5, y=row_y + 1, w=19, h=14)

        pdf.set_font('Helvetica', 'B', 8)
        pdf.set_text_color(255, 26, 26)
        pdf.set_xy(40.5, row_y + 5)
        pdf.cell(31, 6, item["code"], 0, 0, 'L')

        pdf.set_font('Helvetica', '', 8)
        pdf.set_text_color(15, 23, 42)
        pdf.set_xy(75, row_y + 5)
        pdf.cell(58, 6, item["desc"], 0, 0, 'L')

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
out_pdf = '/Users/amanyoonus/Desktop/Blit/assets/catalogues/BLIT_EN_Range_Catalogue_2026.pdf'
pdf.output(out_pdf)

public_pdf = '/Users/amanyoonus/Desktop/Blit/public/assets/catalogues/BLIT_EN_Range_Catalogue_2026.pdf'
os.makedirs(os.path.dirname(public_pdf), exist_ok=True)
shutil.copyfile(out_pdf, public_pdf)

size_mb = os.path.getsize(out_pdf) / (1024 * 1024)
print(f"EN Range PDF catalogue successfully generated: {size_mb:.2f} MB")
