import os
from PIL import Image
from concurrent.futures import ThreadPoolExecutor

src_dir = '/Users/amanyoonus/Desktop/Blit/mkmkmk'
dst_assets = '/Users/amanyoonus/Desktop/Blit/assets/products/en_range'
dst_public = '/Users/amanyoonus/Desktop/Blit/public/assets/products/en_range'

os.makedirs(dst_assets, exist_ok=True)
os.makedirs(dst_public, exist_ok=True)

files = [f for f in sorted(os.listdir(src_dir)) if f.endswith('.png')]

def process_file(f):
    src_path = os.path.join(src_dir, f)
    base_name = os.path.splitext(f)[0]
    with Image.open(src_path) as img:
        img = img.convert('RGBA')
        bbox = img.getbbox()
        if bbox:
            w = bbox[2] - bbox[0]
            h = bbox[3] - bbox[1]
            pad_x = int(w * 0.03)
            pad_y = int(h * 0.03)
            crop_box = (
                max(0, bbox[0] - pad_x),
                max(0, bbox[1] - pad_y),
                min(img.width, bbox[2] + pad_x),
                min(img.height, bbox[3] + pad_y)
            )
            cropped = img.crop(crop_box)
        else:
            cropped = img
        
        max_dim = max(cropped.width, cropped.height)
        if max_dim > 1200:
            scale = 1200.0 / max_dim
            new_w = int(cropped.width * scale)
            new_h = int(cropped.height * scale)
            cropped = cropped.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        out_asset = os.path.join(dst_assets, f'{base_name}.webp')
        out_pub = os.path.join(dst_public, f'{base_name}.webp')
        
        cropped.save(out_asset, 'WEBP', quality=88, method=4)
        cropped.save(out_pub, 'WEBP', quality=88, method=4)
        print(f'Processed {base_name}.webp')
        return f'{base_name}.webp'

with ThreadPoolExecutor(max_workers=8) as executor:
    results = list(executor.map(process_file, files))

print(f'Successfully processed all {len(results)} EN Range images to WebP!')
