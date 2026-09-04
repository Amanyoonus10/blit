import os
from PIL import Image
from fpdf import FPDF

os.makedirs('/tmp/blit_w_thumbnails', exist_ok=True)

def prepare_thumb(path):
    if not os.path.exists(path):
        return None
    thumb_name = os.path.splitext(os.path.basename(path))[0] + '_thumb.jpg'
    out_path = os.path.join('/tmp/blit_w_thumbnails', thumb_name)
    with Image.open(path) as img:
        img = img.convert('RGBA')
        bg = Image.new('RGB', img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[3])
        bg.thumbnail((320, 320), Image.Resampling.LANCZOS)
        bg.save(out_path, 'JPEG', quality=85, optimize=True)
    return out_path

class PDF(FPDF):
    def header(self):
        self.set_fill_color(255, 26, 26)
        self.rect(0, 0, 210, 5, 'F')
        
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(15, 23, 42)
        self.set_xy(15, 10)
        self.cell(40, 8, 'BLIT ELECTRIC', 0, 0, 'L')
        
        self.set_font('Helvetica', '', 8.5)
        self.set_text_color(100, 116, 139)
        self.set_xy(110, 10)
        self.cell(85, 8, 'W RANGE SPECIFICATION CATALOGUE 2026', 0, 0, 'R')
        
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

W_CATEGORIES = [
    {
        "cat_title": "1. Plate Switches Collection (10AX 250V~ BS EN 60669-1)",
        "items": [
            {"code": "W301", "desc": "1 Gang 1 Way Switch", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/w_range/W301.png"},
            {"code": "W303 / W304", "desc": "2 Gang 1 Way / 2 Way Switch", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/w_range/W303.png"},
            {"code": "W305 / W306", "desc": "3 Gang 1 Way / 2 Way Switch", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/w_range/W305.png"},
            {"code": "W307", "desc": "4 Gang 1 Way Switch (Wide)", "dim": "146 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/w_range/W307.png"},
            {"code": "W309", "desc": "6 Gang 1 Way Switch (Wide)", "dim": "146 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/w_range/W309.png"},
            {"code": "W313", "desc": "1 Gang 2 Way Intermediate Switch", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/w_range/W313.png"}
        ]
    },
    {
        "cat_title": "2. Bell Push Switch",
        "items": [
            {"code": "W317", "desc": "1 Gang Retractive Bell Push Switch", "dim": "86 x 86 mm", "std": "BS EN 60669-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/w_range/W317.png"}
        ]
    },
    {
        "cat_title": "3. 20A & 45A High Power Switches & Cooker Units",
        "items": [
            {"code": "W324", "desc": "20A DP Switch + Neon Indicator", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/w_range/W324.png"},
            {"code": "W327", "desc": "45A DP Switch + Neon Indicator", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/w_range/W327.png"},
            {"code": "W329", "desc": "45A DP Switch (Large Plate + Neon)", "dim": "86 x 86 mm", "std": "BS EN 60669-2-1", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/w_range/W329.png"},
            {"code": "W331", "desc": "45A Cooker Unit + 13A Switched Socket + Dual Neons", "dim": "146 x 86 mm", "std": "BS 4177", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/w_range/W331.png"}
        ]
    },
    {
        "cat_title": "4. 13A & 15A Socket Outlets",
        "items": [
            {"code": "W405", "desc": "1 Gang 13A Single Switched Socket", "dim": "86 x 86 mm", "std": "BS 1363-2", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/w_range/W405.png"},
            {"code": "W406", "desc": "2 Gang 13A Twin Switched Socket", "dim": "146 x 86 mm", "std": "BS 1363-2", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/w_range/W406.png"},
            {"code": "W429", "desc": "15A 1 Gang Switched Round Pin Socket", "dim": "86 x 86 mm", "std": "BS 546", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/w_range/W429.png"}
        ]
    },
    {
        "cat_title": "5. FCUs, Blank Plates & Connection Units",
        "items": [
            {"code": "W401", "desc": "1 Gang Blank Cover Plate", "dim": "86 x 86 mm", "std": "BS 5733", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/w_range/W401.png"},
            {"code": "W402", "desc": "2 Gang Blank Cover Plate", "dim": "146 x 86 mm", "std": "BS 5733", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/w_range/W402.png"},
            {"code": "W419", "desc": "13A Switched FCU Spur + Neon", "dim": "86 x 86 mm", "std": "BS 1363-4", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/w_range/W419.png"},
            {"code": "W820", "desc": "20A Heavy Duty Connection Plate", "dim": "86 x 86 mm", "std": "BS 5733", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/w_range/W820.png"},
            {"code": "W821", "desc": "45A Heavy Duty Connection Plate", "dim": "86 x 86 mm", "std": "BS 5733", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/w_range/W821.png"}
        ]
    },
    {
        "cat_title": "6. Data, Telecom & TV Multimedia Outlets",
        "items": [
            {"code": "W432", "desc": "1 Gang Co-axial TV Socket", "dim": "86 x 86 mm", "std": "BS 3041", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/w_range/W432.png"},
            {"code": "W438", "desc": "1 Gang RJ11 Telephone Socket", "dim": "86 x 86 mm", "std": "BS 6312", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/w_range/W438.png"},
            {"code": "W442", "desc": "1 Gang Cat6 RJ45 Gigabit Data Outlet", "dim": "86 x 86 mm", "std": "TIA/EIA-568", "img": "/Users/amanyoonus/Desktop/Blit/assets/products/w_range/W442.png"}
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
pdf.cell(170, 8, 'W RANGE MOULDED WHITE ELECTRICAL ACCESSORIES', 0, 1, 'L')
pdf.set_font('Helvetica', '', 9.5)
pdf.set_text_color(71, 85, 105)
pdf.set_x(20)
pdf.cell(170, 6, 'Complete Product Specifications, High-Resolution Imagery & International Compliance Reference', 0, 1, 'L')
pdf.ln(8)

for cat in W_CATEGORIES:
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
    pdf.cell(28, 6, "MODEL CODE", 1, 0, 'L', True)
    pdf.cell(68, 6, "DESCRIPTION", 1, 0, 'L', True)
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
            pdf.cell(28, 6, "MODEL CODE", 1, 0, 'L', True)
            pdf.cell(68, 6, "DESCRIPTION", 1, 0, 'L', True)
            pdf.cell(26, 6, "DIMENSION", 1, 0, 'C', True)
            pdf.cell(34, 6, "STANDARD", 1, 1, 'C', True)

        row_y = pdf.get_y()
        row_h = 16

        pdf.set_draw_color(226, 232, 240)
        pdf.rect(15, row_y, 24, row_h)
        pdf.rect(39, row_y, 28, row_h)
        pdf.rect(67, row_y, 68, row_h)
        pdf.rect(135, row_y, 26, row_h)
        pdf.rect(161, row_y, 34, row_h)

        img_path = prepare_thumb(item["img"])
        if img_path and os.path.exists(img_path):
            pdf.image(img_path, x=17.5, y=row_y + 1, w=19, h=14)

        pdf.set_font('Helvetica', 'B', 8.5)
        pdf.set_text_color(255, 26, 26)
        pdf.set_xy(41, row_y + 5)
        pdf.cell(24, 6, item["code"], 0, 0, 'L')

        pdf.set_font('Helvetica', '', 8)
        pdf.set_text_color(15, 23, 42)
        pdf.set_xy(69, row_y + 5)
        pdf.cell(64, 6, item["desc"], 0, 0, 'L')

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

out_pdf = '/Users/amanyoonus/Desktop/Blit/assets/catalogues/BLIT_W_Range_Catalogue_2026.pdf'
pdf.output(out_pdf)

public_pdf = '/Users/amanyoonus/Desktop/Blit/public/assets/catalogues/BLIT_W_Range_Catalogue_2026.pdf'
os.makedirs(os.path.dirname(public_pdf), exist_ok=True)
import shutil
shutil.copyfile(out_pdf, public_pdf)

size_mb = os.path.getsize(out_pdf) / (1024 * 1024)
print(f"Optimized visual W Range PDF catalogue generated: {size_mb:.2f} MB")
