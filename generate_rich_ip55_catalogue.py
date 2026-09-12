import os
import shutil
from PIL import Image
from fpdf import FPDF

os.makedirs('/tmp/blit_ip55_thumbnails', exist_ok=True)

def prepare_thumb(path):
    if not os.path.exists(path):
        return None
    thumb_name = os.path.splitext(os.path.basename(path))[0] + '_thumb.jpg'
    out_path = os.path.join('/tmp/blit_ip55_thumbnails', thumb_name)
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
        self.set_xy(100, 10)
        self.cell(95, 8, 'IP55 SPLASHPROOF SPECIFICATION CATALOGUE 2026', 0, 0, 'R')
        
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

IP55_CATEGORIES = [
    {
        "cat_title": "1. IP55 Splashproof Switches (10AX / 20A Heavy Duty)",
        "items": [
            {"code": "BTSP304", "desc": "1 Gang 2 Way Splashproof Switch Plate (10AX)", "dim": "86 x 86 mm", "std": "BS EN 60669-1 / IP55", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/weatherproof/BTSP304.webp"},
            {"code": "BTSP306", "desc": "2 Gang 2 Way Splashproof Switch Plate (10AX)", "dim": "86 x 86 mm", "std": "BS EN 60669-1 / IP55", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/weatherproof/BTSP306.webp"},
            {"code": "BTSP317", "desc": "1 Gang Splashproof Bell Push Switch (10A)", "dim": "86 x 86 mm", "std": "BS EN 60669-1 / IP55", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/weatherproof/BTSP317.webp"},
            {"code": "BTSP324", "desc": "20A Double Pole Heavy-Duty Splashproof Switch + Neon", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1 / IP55", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/weatherproof/BTSP324.webp"}
        ]
    },
    {
        "cat_title": "2. IP55 Switched Socket Outlets (13A BS 1363 / 15A BS 546)",
        "items": [
            {"code": "BTSP405", "desc": "13A 1 Gang Single Switched Socket with IP55 Spring Lid", "dim": "86 x 86 mm", "std": "BS 1363-2 / IP55", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/weatherproof/BTSP405.webp"},
            {"code": "BTSP406", "desc": "13A 2 Gang Twin Switched Socket with Dual IP55 Spring Lids", "dim": "146 x 86 mm", "std": "BS 1363-2 / IP55", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/weatherproof/BTSP406.webp"},
            {"code": "BTSP429", "desc": "15A 1 Gang Round Pin Switched Socket with IP55 Spring Lid", "dim": "86 x 86 mm", "std": "BS 546 / IP55", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/weatherproof/BTSP429.webp"}
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
pdf.cell(170, 8, 'IP55 SPLASHPROOF WIRING ACCESSORIES', 0, 1, 'L')
pdf.set_font('Helvetica', '', 9.5)
pdf.set_text_color(71, 85, 105)
pdf.set_x(20)
pdf.cell(170, 6, 'Built for Everyday Exterior Safety, Balconies, Garages & Semi-Sheltered Utility Zones', 0, 1, 'L')
pdf.ln(8)

for cat in IP55_CATEGORIES:
    if pdf.get_y() > 220:
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
    pdf.cell(34, 6, "STANDARD / IP", 1, 1, 'C', True)

    for item in cat["items"]:
        if pdf.get_y() > 250:
            pdf.add_page()
            pdf.set_fill_color(241, 245, 249)
            pdf.set_font('Helvetica', 'B', 8)
            pdf.set_text_color(51, 65, 85)
            pdf.set_x(15)
            pdf.cell(24, 6, "IMAGE", 1, 0, 'C', True)
            pdf.cell(32, 6, "MODEL CODE", 1, 0, 'L', True)
            pdf.cell(64, 6, "DESCRIPTION", 1, 0, 'L', True)
            pdf.cell(26, 6, "DIMENSION", 1, 0, 'C', True)
            pdf.cell(34, 6, "STANDARD / IP", 1, 1, 'C', True)

        row_y = pdf.get_y()
        row_h = 24
        
        pdf.set_draw_color(226, 232, 240)
        pdf.rect(15, row_y, 180, row_h)
        
        # Product Image
        thumb = prepare_thumb(item["img"])
        if thumb and os.path.exists(thumb):
            pdf.image(thumb, x=17, y=row_y + 2, w=20, h=20)
        
        # Model Code
        pdf.set_xy(39, row_y + 8)
        pdf.set_font('Helvetica', 'B', 9)
        pdf.set_text_color(15, 23, 42)
        pdf.cell(32, 6, item["code"])
        
        # Description
        pdf.set_xy(71, row_y + 5)
        pdf.set_font('Helvetica', '', 8.5)
        pdf.set_text_color(71, 85, 105)
        pdf.multi_cell(62, 4.5, item["desc"])
        
        # Dimensions
        pdf.set_xy(135, row_y + 8)
        pdf.set_font('Helvetica', '', 8.5)
        pdf.set_text_color(15, 23, 42)
        pdf.cell(26, 6, item["dim"], 0, 0, 'C')
        
        # Standards
        pdf.set_xy(161, row_y + 8)
        pdf.set_font('Helvetica', 'B', 8)
        pdf.set_text_color(255, 26, 26)
        pdf.cell(34, 6, item["std"], 0, 0, 'C')
        
        pdf.set_y(row_y + row_h)

    pdf.ln(6)

os.makedirs('/Users/amanyoonus/Desktop/Blit/assets/catalogues', exist_ok=True)
os.makedirs('/Users/amanyoonus/Desktop/Blit/public/assets/catalogues', exist_ok=True)

out_pdf = '/Users/amanyoonus/Desktop/Blit/assets/catalogues/BLIT_IP55_Range_Catalogue_2026.pdf'
pdf.output(out_pdf)

public_pdf = '/Users/amanyoonus/Desktop/Blit/public/assets/catalogues/BLIT_IP55_Range_Catalogue_2026.pdf'
shutil.copyfile(out_pdf, public_pdf)

print(f"IP55 PDF catalogue generated successfully: {out_pdf}")
