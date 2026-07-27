import os
from fpdf import FPDF

class TAOSWRangePDF(FPDF):
    def header(self):
        # Red Header Bar
        self.set_fill_color(255, 26, 26)
        self.rect(0, 0, 210, 6, 'F')
        
        self.set_font('Helvetica', 'B', 16)
        self.set_text_color(17, 24, 39)
        self.set_xy(14, 11)
        self.cell(0, 7, 'BLIT ELECTRIC  |  WHITE RANGE CATALOGUE', 0, 1, 'L')
        
        self.set_font('Helvetica', '', 8.5)
        self.set_text_color(100, 116, 139)
        self.set_xy(14, 18)
        self.cell(0, 4, 'Complete Specification Catalogue for Moulded White Wiring Accessories', 0, 1, 'L')
        
        self.set_draw_color(226, 232, 240)
        self.line(14, 24, 196, 24)
        self.ln(6)

    def footer(self):
        self.set_y(-14)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(148, 163, 184)
        self.cell(0, 8, f'BLIT Electric White Range Official Catalogue  |  Page {self.page_no()}/{{nb}}  |  www.blitelectric.com', 0, 0, 'C')

def generate_full_pdf():
    pdf = TAOSWRangePDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    pdf.ln(12)
    pdf.set_font('Helvetica', 'B', 18)
    pdf.set_text_color(255, 26, 26)
    pdf.cell(0, 8, 'TAOS WHITE RANGE COLLECTION', 0, 1, 'L')
    
    pdf.set_font('Helvetica', '', 9.5)
    pdf.set_text_color(71, 85, 105)
    pdf.multi_cell(0, 4.5, 'TAOS White Range is a comprehensive line-up of high-quality moulded white wiring accessories with proven quality and value for over 24 years. Suitable for new build housing, commercial spaces, and retrofit applications.')
    pdf.ln(4)
    
    # Complete Product Categories List from PDF
    full_catalog = [
        ("10Amp Plate Switches", [
            ("W301", "1 gang 1 way switch", "86 x 86 mm", "BS EN 60669-1"),
            ("W302", "1 gang 2 way switch", "86 x 86 mm", "BS EN 60669-1"),
            ("W313", "1 gang 2 way intermediate switch", "86 x 86 mm", "BS EN 60669-1"),
            ("W303", "2 gang 1 way switch", "86 x 86 mm", "BS EN 60669-1"),
            ("W304", "2 gang 2 way switch", "86 x 86 mm", "BS EN 60669-1"),
            ("W305", "3 gang 1 way switch", "86 x 86 mm", "BS EN 60669-1"),
            ("W306", "3 gang 2 way switch", "86 x 86 mm", "BS EN 60669-1"),
            ("W307", "4 gang 1 way switch", "146 x 86 mm", "BS EN 60669-1"),
            ("W308", "4 gang 2 way switch", "146 x 86 mm", "BS EN 60669-1"),
            ("W309", "6 gang 1 way switch", "146 x 86 mm", "BS EN 60669-1"),
            ("W310", "6 gang 2 way switch", "146 x 86 mm", "BS EN 60669-1")
        ]),
        ("Bell & Key Switches", [
            ("W317", "1 gang bell switch", "86 x 86 mm", "BS EN 60669-1"),
            ("W319", "1 gang bell switch + neon", "86 x 86 mm", "BS EN 60669-1"),
            ("W360", "1 gang bell switch (press symbol)", "86 x 86 mm", "BS EN 60669-1"),
            ("W361", "1 gang bell switch + neon (press symbol)", "86 x 86 mm", "BS EN 60669-1"),
            ("W316", "1 gang bell switch (large rocker)", "86 x 86 mm", "BS EN 60669-1"),
            ("W318", "1 gang bell switch + neon (large rocker)", "86 x 86 mm", "BS EN 60669-1")
        ]),
        ("20 & 45Amp Switches", [
            ("W324", "20A 1 gang switch, DP + neon", "86 x 86 mm", "BS EN 60669-2-1"),
            ("W327", "45A 1 gang switch, DP + neon", "86 x 86 mm", "BS EN 60669-2-1"),
            ("W328", "45A 1 gang switch, DP", "86 x 86 mm", "BS EN 60669-2-1"),
            ("W329", "45A 1 gang switch, DP + neon (large plate)", "86 x 86 mm", "BS EN 60669-2-1"),
            ("W330", "45A 1 gang switch, DP (large plate)", "86 x 86 mm", "BS EN 60669-2-1"),
            ("W331", "45A 1 gang switch + neon + 13A switched socket + neon", "146 x 86 mm", "BS 4177"),
            ("W332", "45A 1 gang switch + 13A switched socket", "146 x 86 mm", "BS 4177")
        ]),
        ("Dimmer & Speed Switches", [
            ("W350", "1 gang 250W dimmer switch", "86 x 86 mm", "BS EN 60669-2-1"),
            ("W352", "1 gang 400W dimmer switch", "86 x 86 mm", "BS EN 60669-2-1"),
            ("W355", "1 gang 500W dimmer switch", "86 x 86 mm", "BS EN 60669-2-1"),
            ("W359", "1 gang 600W dimmer switch", "86 x 86 mm", "BS EN 60669-2-1"),
            ("W555", "1 gang 1000W dimmer switch", "86 x 86 mm", "BS EN 60669-2-1"),
            ("W3552", "1 gang 500W dimmer switch, 2 way", "86 x 86 mm", "BS EN 60669-2-1"),
            ("W5552", "1 gang 1000W dimmer switch, 2 way", "86 x 86 mm", "BS EN 60669-2-1"),
            ("W353", "2 gang 250W dimmer switch", "86 x 86 mm", "BS EN 60669-2-1"),
            ("W354", "2 gang 400W dimmer switch", "86 x 86 mm", "BS EN 60669-2-1"),
            ("W356", "2 gang 500W dimmer switch", "86 x 86 mm", "BS EN 60669-2-1"),
            ("W3542", "2 gang 400W dimmer switch, 2 way", "86 x 86 mm", "BS EN 60669-2-1"),
            ("W3562", "2 gang 500W dimmer switch, 2 way", "86 x 86 mm", "BS EN 60669-2-1"),
            ("W556", "2 gang 1000W dimmer switch", "146 x 86 mm", "BS EN 60669-2-1"),
            ("W5562", "2 gang 1000W dimmer switch, 2 way", "146 x 86 mm", "BS EN 60669-2-1"),
            ("W351", "1 gang 250W speed switch (fan control)", "86 x 86 mm", "IEC 60669"),
            ("W371", "1 gang 400W speed switch (fan control)", "86 x 86 mm", "IEC 60669"),
            ("W368", "1 gang 500W speed switch", "86 x 86 mm", "IEC 60669"),
            ("W557", "1 gang 1000W speed switch", "86 x 86 mm", "IEC 60669"),
            ("W5572", "1 gang 1000W speed switch, 2 way", "86 x 86 mm", "IEC 60669")
        ]),
        ("13Amp & Round Pin Socket Outlets", [
            ("W405", "1 gang switched socket 13A", "86 x 86 mm", "BS 1363-2"),
            ("W4052", "1 gang switched socket, SP, double earthing", "86 x 86 mm", "BS 1363-2"),
            ("W409", "1 gang switched socket, DP", "86 x 86 mm", "BS 1363-2"),
            ("W406", "2 gang switched socket 13A", "146 x 86 mm", "BS 1363-2"),
            ("W410", "2 gang switched socket, DP", "146 x 86 mm", "BS 1363-2"),
            ("W407", "1 gang switched socket + neon", "86 x 86 mm", "BS 1363-2"),
            ("W411", "1 gang switched socket, DP + neon", "86 x 86 mm", "BS 1363-2"),
            ("W408", "2 gang switched socket + neon", "146 x 86 mm", "BS 1363-2"),
            ("W412", "2 gang switched socket, DP + neon", "146 x 86 mm", "BS 1363-2"),
            ("W429", "15A 1 gang switched round-pin socket", "86 x 86 mm", "BS 546"),
            ("W431", "15A 1 gang switched round-pin socket + neon", "86 x 86 mm", "BS 546")
        ]),
        ("Multi-function Socket Outlets & Others", [
            ("W460", "10A 1 gang multi socket", "86 x 86 mm", "IEC 60884"),
            ("W460N", "10A 1 gang multi socket + shutter", "86 x 86 mm", "IEC 60884"),
            ("W445", "10A 1 gang multi socket + 20A 1 gang switch", "86 x 86 mm", "IEC 60884"),
            ("W445N", "10A 1 gang multi socket + 20A 1 gang switch + shutter", "86 x 86 mm", "IEC 60884"),
            ("W446", "10A 1 gang multi socket + 20A 1 gang switch, DP", "86 x 86 mm", "IEC 60884"),
            ("W444", "10A 2 gang multi socket", "146 x 86 mm", "IEC 60884"),
            ("W447", "10A 1 gang multi socket + 10A 2 gang switch", "86 x 86 mm", "IEC 60884"),
            ("W447N", "10A 1 gang multi socket + 10A 2 gang switch + shutter", "86 x 86 mm", "IEC 60884"),
            ("W407M", "13A 1 gang switched multi socket + neon", "86 x 86 mm", "BS 1363"),
            ("W482", "13A switched multi socket + neon", "86 x 86 mm", "BS 1363"),
            ("W458", "Shaver socket dual voltage 115V/230V", "146 x 86 mm", "BS EN 61558-2-5")
        ]),
        ("Fused Connection Units (FCUs)", [
            ("W418", "3A FCU", "86 x 86 mm", "BS 1363-4"),
            ("W417", "5A FCU", "86 x 86 mm", "BS 1363-4"),
            ("W416", "13A FCU", "86 x 86 mm", "BS 1363-4"),
            ("W415", "3A FCU + neon", "86 x 86 mm", "BS 1363-4"),
            ("W414", "5A FCU + neon", "86 x 86 mm", "BS 1363-4"),
            ("W413", "13A FCU + neon", "86 x 86 mm", "BS 1363-4"),
            ("W424", "3A switched FCU", "86 x 86 mm", "BS 1363-4"),
            ("W423", "5A switched FCU", "86 x 86 mm", "BS 1363-4"),
            ("W422", "13A switched FCU", "86 x 86 mm", "BS 1363-4"),
            ("W421", "3A switched FCU + neon", "86 x 86 mm", "BS 1363-4"),
            ("W420", "5A switched FCU + neon", "86 x 86 mm", "BS 1363-4"),
            ("W419", "13A switched FCU + neon", "86 x 86 mm", "BS 1363-4")
        ]),
        ("Co-axial & Satellite Outlets", [
            ("W166", "1 gang satellite socket", "86 x 86 mm", "BS 3041"),
            ("W168", "2 gang satellite socket", "86 x 86 mm", "BS 3041"),
            ("W167", "Satellite socket & isolated co-axial socket", "86 x 86 mm", "BS 3041"),
            ("W169", "Co-axial & RJ45 data socket (8 terminal)", "86 x 86 mm", "BS 3041 & TIA-568"),
            ("W432", "1 gang co-axial socket", "86 x 86 mm", "BS 3041"),
            ("W434", "1 gang isolated co-axial socket", "86 x 86 mm", "BS 3041"),
            ("W435", "1 gang isolated co-axial socket with one branch", "86 x 86 mm", "BS 3041"),
            ("W433", "2 gang co-axial socket", "86 x 86 mm", "BS 3041"),
            ("W436", "2 gang isolated co-axial socket", "86 x 86 mm", "BS 3041"),
            ("W437", "2 gang isolated co-axial socket with one branch", "86 x 86 mm", "BS 3041")
        ]),
        ("Tel & Data Outlets", [
            ("W438", "1 gang telephone socket, secondary", "86 x 86 mm", "BS 6312"),
            ("W439", "1 gang telephone socket, master", "86 x 86 mm", "BS 6312"),
            ("W440", "2 gang telephone socket, secondary", "86 x 86 mm", "BS 6312"),
            ("W441", "2 gang telephone socket, master", "86 x 86 mm", "BS 6312"),
            ("W464", "1 gang RJ11 data socket (4 terminal)", "86 x 86 mm", "FCC Part 68"),
            ("W462", "1 gang RJ11 data socket (6 terminal)", "86 x 86 mm", "FCC Part 68"),
            ("W442", "1 gang RJ45 data socket (8 terminal)", "86 x 86 mm", "TIA/EIA-568"),
            ("W465", "2 gang RJ11 data socket (4 terminal)", "86 x 86 mm", "FCC Part 68"),
            ("W463", "2 gang RJ11 data socket (6 terminal)", "86 x 86 mm", "FCC Part 68"),
            ("W443", "2 gang RJ45 data socket (8 terminal)", "86 x 86 mm", "TIA/EIA-568")
        ]),
        ("Connection Plate & Blank Plates", [
            ("W401", "1 gang blank plate", "86 x 86 mm", "BS 5733"),
            ("W402", "2 gang blank plate", "146 x 86 mm", "BS 5733"),
            ("W501", "1 gang blank plate (with a 25mm hole)", "86 x 86 mm", "BS 5733"),
            ("W820", "20A connection plate", "86 x 86 mm", "BS 5733"),
            ("W821", "45A connection plate", "86 x 86 mm", "BS 5733")
        ])
    ]

    for cat_title, items in full_catalog:
        if pdf.get_y() > 230:
            pdf.add_page()
            pdf.ln(10)
            
        pdf.set_font('Helvetica', 'B', 10)
        pdf.set_text_color(255, 26, 26)
        pdf.cell(0, 5.5, cat_title.upper(), 0, 1, 'L')
        
        pdf.set_fill_color(241, 245, 249)
        pdf.set_font('Helvetica', 'B', 7.5)
        pdf.set_text_color(30, 41, 59)
        pdf.cell(24, 5.5, 'Model Code', 1, 0, 'C', True)
        pdf.cell(98, 5.5, 'Item Description & Specification', 1, 0, 'L', True)
        pdf.cell(28, 5.5, 'Dimensions', 1, 0, 'C', True)
        pdf.cell(32, 5.5, 'Standard Compliance', 1, 1, 'C', True)
        
        pdf.set_font('Helvetica', '', 7.5)
        pdf.set_text_color(71, 85, 105)
        fill = False
        for code, desc, size, std in items:
            if fill:
                pdf.set_fill_color(250, 250, 252)
            else:
                pdf.set_fill_color(255, 255, 255)
            
            pdf.cell(24, 5, code, 1, 0, 'C', fill)
            pdf.cell(98, 5, desc, 1, 0, 'L', fill)
            pdf.cell(28, 5, size, 1, 0, 'C', fill)
            pdf.cell(32, 5, std, 1, 1, 'C', fill)
            fill = not fill
            
        pdf.ln(3)

    os.makedirs('/Users/amanyoonus/Desktop/Blit/public/assets/catalogues', exist_ok=True)
    os.makedirs('/Users/amanyoonus/Desktop/Blit/assets/catalogues', exist_ok=True)
    
    pdf.output('/Users/amanyoonus/Desktop/Blit/public/assets/catalogues/BLIT_W_Range_Catalogue_2026.pdf')
    pdf.output('/Users/amanyoonus/Desktop/Blit/assets/catalogues/BLIT_W_Range_Catalogue_2026.pdf')
    print("Full PDF catalog updated successfully.")

if __name__ == '__main__':
    generate_full_pdf()
