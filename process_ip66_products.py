import os
import shutil
from PIL import Image, ImageEnhance, ImageFilter

def process_ip66_image(src_path, out_dim=1200, margin=55, is_bell=False, is_2g=False):
    if not os.path.exists(src_path):
        print(f"Warning: source file not found: {src_path}")
        return None
    
    img = Image.open(src_path).convert('RGBA')
    
    # 1. Trim transparency bounding box
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
    
    r, g, b, a = img.split()
    
    # Custom 3-channel tone mapping LUT to transform cold underexposed plastic (RGB ~160, 169, 173)
    # into bright, clean, studio-grade neutral white (RGB ~238-245) while preserving deep shadows (gaskets, seams, logos)
    # and vibrant reds (neon indicator).
    def make_lut(in_mid, out_mid, in_dark=30, out_dark=18, in_high=245, out_high=253):
        lut = []
        for i in range(256):
            if i <= in_dark:
                val = i * (out_dark / in_dark)
            elif i <= in_mid:
                val = out_dark + (i - in_dark) * ((out_mid - out_dark) / (in_mid - in_dark))
            elif i <= in_high:
                val = out_mid + (i - in_mid) * ((out_high - out_mid) / (in_high - in_mid))
            else:
                val = out_high + (i - in_high) * ((255 - out_high) / (255 - in_high))
            lut.append(int(round(min(255, max(0, val)))))
        return lut

    lut_r = make_lut(160, 238, in_dark=35, out_dark=18)
    lut_g = make_lut(169, 238, in_dark=35, out_dark=18)
    lut_b = make_lut(173, 238, in_dark=35, out_dark=18)
    
    r_corr = r.point(lut_r)
    g_corr = g.point(lut_g)
    b_corr = b.point(lut_b)
    
    rgb = Image.merge('RGB', (r_corr, g_corr, b_corr))
    
    # Color balance and saturation
    enh_col = ImageEnhance.Color(rgb)
    rgb = enh_col.enhance(1.22)
    
    # Contrast enhancement
    enh_con = ImageEnhance.Contrast(rgb)
    rgb = enh_con.enhance(1.08)
    
    # Subtle Unsharp Mask for crisp tactile embossing, text, gasket definition
    rgb = rgb.filter(ImageFilter.UnsharpMask(radius=2.2, percent=135, threshold=2))
    
    enhanced = Image.merge('RGBA', (*rgb.split(), a))
    
    # 2. Fit into clean square canvas with uniform margin
    max_w = out_dim - (margin * 2)
    max_h = out_dim - (margin * 2)
    w, h = enhanced.size
    scale = min(max_w / w, max_h / h)
    new_w = int(round(w * scale))
    new_h = int(round(h * scale))
    
    resized = enhanced.resize((new_w, new_h), Image.Resampling.LANCZOS)
    canvas = Image.new('RGBA', (out_dim, out_dim), (0, 0, 0, 0))
    pos_x = (out_dim - new_w) // 2
    pos_y = (out_dim - new_h) // 2
    canvas.paste(resized, (pos_x, pos_y), resized)
    
    return canvas

def main():
    base_dir = '/Users/amanyoonus/Desktop/Blit'
    dest_dirs = [
        os.path.join(base_dir, 'assets/products/weatherproof'),
        os.path.join(base_dir, 'public/assets/products/weatherproof'),
        os.path.join(base_dir, 'dist/assets/products/weatherproof')
    ]
    
    for d in dest_dirs:
        os.makedirs(d, exist_ok=True)
    
    # Define products to process with source paths and aliases
    items = [
        {
            'code': 'BTAG3012WHI',
            'src': '/Users/amanyoonus/Downloads/BTAG3012WHI.png',
            'aliases': ['ip66_switch_1g'],
            'is_bell': False,
            'is_2g': False
        },
        {
            'code': 'BTAG3022WHI',
            'src': '/Users/amanyoonus/Downloads/BTAG3022WHI.png',
            'aliases': ['ip66_switch_2g'],
            'is_bell': False,
            'is_2g': True
        },
        {
            'code': 'BTAG3013WHI',
            'src': '/Users/amanyoonus/Downloads/BTAG3013WHI.png',
            'aliases': [],
            'is_bell': False,
            'is_2g': False
        },
        {
            'code': 'BTAG3016WHI-BEL',
            'src': '/Users/amanyoonus/Downloads/BTAG3016WHI-BEL.png',
            'aliases': [],
            'is_bell': True,
            'is_2g': False
        },
        {
            'code': 'BTAG3214WHI',
            'src': '/Users/amanyoonus/Downloads/BTAG3214WHI.png',
            'aliases': [],
            'is_bell': False,
            'is_2g': False
        },
        # Sockets
        {
            'code': 'BTAGZ4010L',
            'src': os.path.join(base_dir, 'rep/BTAGZ4010L.png'),
            'aliases': ['ip66_socket_cover'],
            'is_bell': False,
            'is_2g': False
        },
        {
            'code': 'BTAGZ4030L',
            'src': os.path.join(base_dir, 'rep/BTAGZ4030L.png'),
            'aliases': [],
            'is_bell': False,
            'is_2g': False
        },
        {
            'code': 'BTAG401',
            'src': os.path.join(base_dir, 'rep/BTAG401.png'),
            'aliases': [],
            'is_bell': False,
            'is_2g': False
        },
        {
            'code': 'BTAG402',
            'src': os.path.join(base_dir, 'rep/BTAG402.png'),
            'aliases': [],
            'is_bell': False,
            'is_2g': False
        },
        {
            'code': 'BTAG401_INSIDE',
            'src': os.path.join(base_dir, 'rep/BTAG401 INSIDE VIEW.png'),
            'aliases': [],
            'is_bell': False,
            'is_2g': False
        },
        {
            'code': 'BTAGZ4030L_INSIDE',
            'src': os.path.join(base_dir, 'rep/BTAGZ4030L INSIDE VIEW.png'),
            'aliases': [],
            'is_bell': False,
            'is_2g': False
        }
    ]
    
    for item in items:
        code = item['code']
        src = item['src']
        if not os.path.exists(src):
            # Fallback to rep or 66
            fallback_rep = os.path.join(base_dir, f"rep/{code}.png")
            fallback_66 = os.path.join(base_dir, f"66/{code}.png")
            if os.path.exists(fallback_rep):
                src = fallback_rep
            elif os.path.exists(fallback_66):
                src = fallback_66
        
        print(f"Processing {code} from {src}...")
        processed = process_ip66_image(
            src,
            out_dim=1200,
            margin=55,
            is_bell=item.get('is_bell', False),
            is_2g=item.get('is_2g', False)
        )
        
        if processed is None:
            print(f"Skipped {code}")
            continue
        
        # Save PNG and WebP to each destination directory
        all_names = [code] + item.get('aliases', [])
        for name in all_names:
            for dest_dir in dest_dirs:
                if not os.path.exists(dest_dir):
                    continue
                png_path = os.path.join(dest_dir, f"{name}.png")
                webp_path = os.path.join(dest_dir, f"{name}.webp")
                jpg_path = os.path.join(dest_dir, f"{name}.jpg")
                
                # Save transparent PNG
                processed.save(png_path, 'PNG', optimize=True)
                # Save WebP with high quality
                processed.save(webp_path, 'WEBP', quality=95, method=6)
                
                # Save white background JPG for any legacy references
                bg = Image.new('RGB', processed.size, (255, 255, 255))
                bg.paste(processed, mask=processed.split()[3])
                bg.save(jpg_path, 'JPEG', quality=92, optimize=True)
        
        print(f"✓ Completed {code} (and aliases: {item.get('aliases', [])})")

if __name__ == '__main__':
    main()
