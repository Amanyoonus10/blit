import os
import shutil
from PIL import Image

def process_ip66_authentic(src_path, out_dim=1200, margin=50):
    if not os.path.exists(src_path):
        print(f"Warning: source file not found: {src_path}")
        return None
    
    img = Image.open(src_path).convert('RGBA')
    
    # 1. Trim transparency bounding box
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
    
    # 2. Fit into clean square canvas preserving 100% authentic original pixels and colors
    max_w = out_dim - (margin * 2)
    max_h = out_dim - (margin * 2)
    w, h = img.size
    scale = min(max_w / w, max_h / h)
    new_w = int(round(w * scale))
    new_h = int(round(h * scale))
    
    resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
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
        os.path.join(base_dir, 'dist/assets/products/weatherproof'),
        os.path.join(base_dir, '66'),
        os.path.join(base_dir, 'rep')
    ]
    
    for d in dest_dirs:
        os.makedirs(d, exist_ok=True)
    
    # Authentic product mappings
    items = [
        {
            'code': 'BTAG3012WHI',
            'src': '/Users/amanyoonus/Downloads/BTAG3012WHI.png',
            'aliases': ['ip66_switch_1g']
        },
        {
            'code': 'BTAG3022WHI',
            'src': '/Users/amanyoonus/Downloads/BTAG3022WHI.png',
            'aliases': ['ip66_switch_2g']
        },
        {
            'code': 'BTAG3013WHI',
            'src': '/Users/amanyoonus/Downloads/BTAG3013WHI.png',
            'aliases': []
        },
        {
            'code': 'BTAG3016WHI-BEL',
            'src': '/Users/amanyoonus/Downloads/BTAG3016WHI-BEL.png',
            'aliases': []
        },
        {
            'code': 'BTAG3214WHI',
            'src': '/Users/amanyoonus/Downloads/BTAG3214WHI.png',
            'aliases': []
        },
        # Sockets
        {
            'code': 'BTAGZ4010L',
            'src': os.path.join(base_dir, 'rep/BTAGZ4010L.png'),
            'aliases': ['ip66_socket_cover']
        },
        {
            'code': 'BTAGZ4030L',
            'src': os.path.join(base_dir, 'rep/BTAGZ4030L.png'),
            'aliases': []
        },
        {
            'code': 'BTAG401',
            'src': os.path.join(base_dir, 'rep/BTAG401.png'),
            'aliases': []
        },
        {
            'code': 'BTAG402',
            'src': os.path.join(base_dir, 'rep/BTAG402.png'),
            'aliases': []
        },
        {
            'code': 'BTAG401_INSIDE',
            'src': os.path.join(base_dir, 'rep/BTAG401 INSIDE VIEW.png'),
            'aliases': []
        },
        {
            'code': 'BTAGZ4030L_INSIDE',
            'src': os.path.join(base_dir, 'rep/BTAGZ4030L INSIDE VIEW.png'),
            'aliases': []
        }
    ]
    
    for item in items:
        code = item['code']
        src = item['src']
        
        print(f"Processing authentic {code} from {src}...")
        processed = process_ip66_authentic(src, out_dim=1200, margin=50)
        
        if processed is None:
            print(f"Skipped {code}")
            continue
        
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
                # Save WebP with maximum quality / fidelity
                processed.save(webp_path, 'WEBP', quality=95, method=6)
                
                # Save white bg JPG for fallback
                bg = Image.new('RGB', processed.size, (255, 255, 255))
                bg.paste(processed, mask=processed.split()[3])
                bg.save(jpg_path, 'JPEG', quality=95, optimize=True)
        
        print(f"✓ Completed authentic {code}")

if __name__ == '__main__':
    main()
