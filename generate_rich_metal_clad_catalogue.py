import os
import shutil
from PIL import Image
from fpdf import FPDF

# Convert webp/png to temporary thumbnail for FPDF compatibility & performance
os.makedirs('/tmp/blit_metal_clad_thumbnails', exist_ok=True)

def prepare_thumb(path):
    if not os.path.exists(path):
        return None
    thumb_name = os.path.splitext(os.path.basename(path))[0] + '_thumb.jpg'
    out_path = os.path.join('/tmp/blit_metal_clad_thumbnails', thumb_name)
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
        self.cell(40, 8, 'BLIT ELECTRIC')
        
        # Header subtitle
        self.set_font('Helvetica', '', 8.5)
        self.set_text_color(100, 116, 139)
        self.set_xy(110, 10)
        self.cell(85, 8, 'METAL CLAD SPECIFICATION CATALOGUE 2026')
        
        # Separator line
        self.set_draw_color(226, 232, 240)
        self.line(15, 20, 195, 20)
        self.ln(16)

    def footer(self):
        self.set_y(-14)
        self.set_font('Helvetica', '', 8)
        self.set_text_color(148, 163, 184)
        self.cell(90, 8, 'Blit Electrical Hardware | info@blitelectric.com')
        self.cell(90, 8, f'Page {self.page_no()}')

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=18)

METAL_CLAD_CATEGORIES = [
    {
        "cat_title": "1. Plate Switches Collection (10AX 250V~ BS EN 60669-1)",
        "items": [
            {"code": "M301", "desc": "1-Gang 1-Way Metal Clad Switch Plate", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/metal_clad/M301.webp"},
            {"code": "M302", "desc": "1-Gang 2-Way Metal Clad Switch Plate", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/metal_clad/M302.webp"},
            {"code": "M304", "desc": "2-Gang 2-Way Metal Clad Switch Plate", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/metal_clad/M304.webp"},
            {"code": "M306", "desc": "3-Gang 2-Way Metal Clad Switch Plate", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/metal_clad/M306.webp"}
        ]
    },
    {
        "cat_title": "2. High Power Double Pole Isolator Switches",
        "items": [
            {"code": "M324", "desc": "20A DP Switch with Illuminated Neon", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/metal_clad/M324.webp"},
            {"code": "M327", "desc": "45A DP Heavy Duty Isolator with Red Neon", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/metal_clad/M327.webp"}
        ]
    },
    {
        "cat_title": "3. 13A & 15A Socket Outlets",
        "items": [
            {"code": "M405", "desc": "13A 1-Gang Single Switched Socket", "dim": "86 x 86 mm", "std": "BS 1363-2", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/metal_clad/M405.webp"},
            {"code": "M406", "desc": "13A 2-Gang Twin Switched Socket Plate", "dim": "146 x 86 mm", "std": "BS 1363-2", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/metal_clad/M406.webp"},
            {"code": "M429", "desc": "15A Round Pin AC Switched Power Socket", "dim": "86 x 86 mm", "std": "BS 546", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/metal_clad/M429.webp"}
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
pdf.cell(170, 8, 'METAL CLAD INDUSTRIAL ACCESSORIES COLLECTION')
pdf.set_font('Helvetica', '', 9.5)
pdf.set_text_color(71, 85, 105)
pdf.set_xy(20, 36)
pdf.cell(170, 6, 'Complete Specifications for Heavy Duty Galvanized Steel Surface Mount Wiring Devices')
pdf.set_y(54)

for cat in METAL_CLAD_CATEGORIES:
    if pdf.get_y() > 240:
        pdf.add_page()
    
    pdf.set_fill_color(15, 23, 42)
    pdf.rect(15, pdf.get_y(), 180, 7.5, 'F')
    pdf.set_font('Helvetica', 'B', 9.5)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(18, pdf.get_y() + 1)
    pdf.cell(174, 5.5, cat["cat_title"])
    pdf.set_y(pdf.get_y() + 6.5)
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

        pdf.set_font('Helvetica', 'B', 8.5)
        pdf.set_text_color(255, 26, 26)
        pdf.set_xy(40.5, row_y + 5)
        pdf.cell(31, 6, item["code"])

        pdf.set_font('Helvetica', '', 8)
        pdf.set_text_color(15, 23, 42)
        pdf.set_xy(75, row_y + 5)
        pdf.cell(58, 6, item["desc"])

        pdf.set_font('Helvetica', '', 8)
        pdf.set_text_color(71, 85, 105)
        pdf.set_xy(135, row_y + 5)
        pdf.cell(26, 6, item["dim"])

        pdf.set_font('Helvetica', 'B', 7.5)
        pdf.set_text_color(51, 65, 85)
        pdf.set_xy(161, row_y + 5)
        pdf.cell(34, 6, item["std"])

        pdf.set_y(row_y + row_h)

    pdf.ln(5)

os.makedirs('/Users/amanyoonus/Desktop/Blit/assets/catalogues', exist_ok=True)
out_pdf = '/Users/amanyoonus/Desktop/Blit/assets/catalogues/BLIT_Metal_Clad_Catalogue_2026.pdf'
pdf.output(out_pdf)

public_pdf = '/Users/amanyoonus/Desktop/Blit/public/assets/catalogues/BLIT_Metal_Clad_Catalogue_2026.pdf'
os.makedirs(os.path.dirname(public_pdf), exist_ok=True)
shutil.copyfile(out_pdf, public_pdf)

size_mb = os.path.getsize(out_pdf) / (1024 * 1024)
print(f"Metal Clad PDF catalogue successfully generated: {size_mb:.2f} MB")
