import os
import shutil
from PIL import Image
from collections import deque

def remove_black_background(img_path, out_dim=1200, margin=60):
    img = Image.open(img_path).convert('RGBA')
    w, h = img.size
    pixels = img.load()
    
    # 1. Flood-fill from outer perimeter to identify outer black background only
    visited = [[False]*w for _ in range(h)]
    is_bg = [[False]*w for _ in range(h)]
    queue = deque()
    
    # Seed all 4 edges of the image
    for x in range(w):
        queue.append((x, 0))
        queue.append((x, h-1))
        visited[0][x] = True
        visited[h-1][x] = True
    for y in range(h):
        queue.append((0, y))
        queue.append((w-1, y))
        visited[y][0] = True
        visited[y][w-1] = True
        
    BG_THRESH = 35
    
    while queue:
        cx, cy = queue.popleft()
        r, g, b, a = pixels[cx, cy]
        brightness = max(r, g, b)
        if brightness < BG_THRESH:
            is_bg[cy][cx] = True
            for nx, ny in [(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)]:
                if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((nx, ny))
                    
    # 2. Construct clean alpha mask
    alpha_img = Image.new('L', (w, h), 255)
    alpha_pix = alpha_img.load()
    for y in range(h):
        for x in range(w):
            if is_bg[y][x]:
                alpha_pix[x, y] = 0
            else:
                alpha_pix[x, y] = 255
                    
    img.putalpha(alpha_img)
    
    # 3. Crop tightly to the switch bounding box
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
        
    # 4. Center into clean square transparent canvas
    max_w = out_dim - (margin * 2)
    max_h = out_dim - (margin * 2)
    cw, ch = img.size
    scale = min(max_w / cw, max_h / ch)
    new_w = int(round(cw * scale))
    new_h = int(round(ch * scale))
    
    resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    canvas = Image.new('RGBA', (out_dim, out_dim), (0, 0, 0, 0))
    pos_x = (out_dim - new_w) // 2
    pos_y = (out_dim - new_h) // 2
    canvas.paste(resized, (pos_x, pos_y), resized)
    
    return canvas

def main():
    base_dir = '/Users/amanyoonus/Desktop/Blit'
    upload_dir = '/Users/amanyoonus/.gemini/antigravity-ide/brain/009e38d1-1740-4961-a624-e7dc9775094e/.user_uploaded'
    
    dest_dirs = [
        os.path.join(base_dir, 'assets/products/weatherproof'),
        os.path.join(base_dir, 'public/assets/products/weatherproof'),
        os.path.join(base_dir, 'dist/assets/products/weatherproof'),
        os.path.join(base_dir, '66'),
        os.path.join(base_dir, 'rep')
    ]
    
    for d in dest_dirs:
        os.makedirs(d, exist_ok=True)
        
    mapping = {
        'BTAG3022WHI': ('media_1789801715747.jpg', ['ip66_switch_2g']),
        'BTAG3012WHI': ('media_1789801715756.jpg', ['ip66_switch_1g']),
        'BTAG3013WHI': ('media_1789801715772.jpg', []),
        'BTAG3214WHI': ('media_1789801715786.jpg', []),
        'BTAG3016WHI-BEL': ('media_1789801715793.jpg', [])
    }
    
    for code, (uploaded_file, aliases) in mapping.items():
        src_path = os.path.join(upload_dir, uploaded_file)
        print(f"Removing black background for {code} from {src_path}...")
        processed = remove_black_background(src_path, out_dim=1200, margin=60)
        
        all_names = [code] + aliases
        for name in all_names:
            for dest_dir in dest_dirs:
                if not os.path.exists(dest_dir):
                    continue
                png_path = os.path.join(dest_dir, f"{name}.png")
                webp_path = os.path.join(dest_dir, f"{name}.webp")
                jpg_path = os.path.join(dest_dir, f"{name}.jpg")
                
                # Save transparent PNG
                processed.save(png_path, 'PNG', optimize=True)
                # Save transparent WebP
                processed.save(webp_path, 'WEBP', quality=95, method=6)
                # Save clean white-background JPG
                bg = Image.new('RGB', processed.size, (255, 255, 255))
                bg.paste(processed, mask=processed.split()[3])
                bg.save(jpg_path, 'JPEG', quality=95, optimize=True)
                
        print(f"✓ Successfully processed and saved transparent assets for {code} (and {aliases})")

if __name__ == '__main__':
    main()
