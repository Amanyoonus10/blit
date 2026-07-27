import os
from PIL import Image

def crop_catalog_items():
    img53_path = '/Users/amanyoonus/Desktop/Blit/assets/catalogues/w_range_catalog_page_053.jpg'
    img54_path = '/Users/amanyoonus/Desktop/Blit/assets/catalogues/w_range_catalog_page_054.jpg'
    
    out_dir = '/Users/amanyoonus/Desktop/Blit/assets/products/w_range'
    pub_out_dir = '/Users/amanyoonus/Desktop/Blit/public/assets/products/w_range'
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(pub_out_dir, exist_ok=True)
    
    img53 = Image.open(img53_path)
    img54 = Image.open(img54_path)
    
    w53, h53 = img53.size
    w54, h54 = img54.size
    
    # Define bounding boxes for individual items (x1_pct, y1_pct, x2_pct, y2_pct, filename)
    crops_53 = [
        # 10Amp Plate Switches
        (0.13, 0.08, 0.26, 0.21, 'W301_plate_switch_1g.png'),
        (0.27, 0.08, 0.40, 0.21, 'W303_plate_switch_2g.png'),
        (0.41, 0.08, 0.53, 0.21, 'W305_plate_switch_3g.png'),
        (0.53, 0.08, 0.74, 0.21, 'W307_plate_switch_4g.png'),
        (0.74, 0.08, 0.95, 0.21, 'W309_plate_switch_6g.png'),
        
        # Bell & Key Switches
        (0.13, 0.23, 0.26, 0.35, 'W317_bell_switch_1g.png'),
        (0.27, 0.23, 0.40, 0.35, 'W319_bell_switch_neon.png'),
        (0.41, 0.23, 0.53, 0.35, 'W360_bell_switch_press.png'),
        (0.53, 0.23, 0.67, 0.35, 'W361_bell_switch_press_neon.png'),
        (0.67, 0.23, 0.81, 0.35, 'W316_bell_switch_rocker.png'),
        (0.81, 0.23, 0.95, 0.35, 'W318_bell_switch_rocker_neon.png'),
        
        # 20A & 45A Switches
        (0.13, 0.37, 0.26, 0.46, 'W324_20a_dp_neon.png'),
        (0.27, 0.37, 0.40, 0.46, 'W327_45a_dp_neon.png'),
        (0.41, 0.37, 0.53, 0.46, 'W328_45a_dp.png'),
        (0.53, 0.37, 0.74, 0.46, 'W329_45a_dp_neon_large.png'),
        (0.74, 0.37, 0.95, 0.46, 'W330_45a_dp_large.png'),
        (0.13, 0.47, 0.37, 0.57, 'W331_cooker_control_neon_socket.png'),
        (0.37, 0.47, 0.57, 0.57, 'W332_cooker_control_socket.png'),
        
        # Dimmers & Speed Switches
        (0.13, 0.60, 0.26, 0.70, 'W350_dimmer_1g_400w.png'),
        (0.27, 0.60, 0.40, 0.70, 'W359_dimmer_600w_1000w.png'),
        (0.41, 0.60, 0.53, 0.70, 'W3552_dimmer_500w_2way.png'),
        (0.53, 0.60, 0.67, 0.70, 'W5552_dimmer_1000w_2way.png'),
        (0.67, 0.60, 0.81, 0.70, 'W353_dimmer_2g_400w.png'),
        (0.81, 0.60, 0.95, 0.70, 'W3542_dimmer_2g_400w_2way.png'),
        (0.13, 0.71, 0.26, 0.81, 'W3562_dimmer_2g_500w_2way.png'),
        (0.27, 0.71, 0.40, 0.81, 'W556_dimmer_2g_1000w.png'),
        (0.41, 0.71, 0.53, 0.81, 'W351_speed_switch_400w.png'),
        (0.53, 0.71, 0.67, 0.81, 'W368_speed_switch_500w.png'),
        (0.67, 0.71, 0.81, 0.81, 'W5572_speed_switch_1000w_2way.png'),
        
        # 13Amp Socket Outlets
        (0.13, 0.83, 0.27, 0.96, 'W405_socket_1g_13a.png'),
        (0.27, 0.83, 0.48, 0.96, 'W406_socket_2g_13a.png'),
        (0.48, 0.83, 0.62, 0.96, 'W407_socket_1g_neon.png'),
        (0.62, 0.83, 0.83, 0.96, 'W408_socket_2g_neon.png')
    ]
    
    crops_54 = [
        # Round Pin Sockets
        (0.13, 0.11, 0.27, 0.25, 'W429_round_pin_15a.png'),
        (0.27, 0.11, 0.41, 0.25, 'W431_round_pin_15a_neon.png'),
        
        # Multi-function Sockets
        (0.13, 0.26, 0.26, 0.38, 'W460_multi_socket_10a.png'),
        (0.26, 0.26, 0.39, 0.38, 'W445_multi_socket_20a_switch.png'),
        (0.39, 0.26, 0.52, 0.38, 'W445N_multi_socket_20a_switch_shutter.png'),
        (0.52, 0.26, 0.65, 0.38, 'W446_multi_socket_20a_dp.png'),
        (0.65, 0.26, 0.79, 0.38, 'W444_multi_socket_2g.png'),
        (0.79, 0.26, 0.93, 0.38, 'W447_multi_socket_2g_switch.png'),
        (0.13, 0.39, 0.26, 0.51, 'W447N_multi_socket_2g_switch_shutter.png'),
        (0.26, 0.39, 0.39, 0.51, 'W407M_multi_socket_13a_neon.png'),
        (0.39, 0.39, 0.52, 0.51, 'W482_multi_socket_13a_neon_switched.png'),
        (0.52, 0.39, 0.75, 0.51, 'W458_shaver_socket.png'),
        
        # Fused Connection Units (FCUs)
        (0.13, 0.53, 0.26, 0.65, 'W418_fcu_3a_5a_13a.png'),
        (0.26, 0.53, 0.39, 0.65, 'W415_fcu_neon.png'),
        (0.39, 0.53, 0.52, 0.65, 'W424_fcu_switched.png'),
        (0.52, 0.53, 0.65, 0.65, 'W422_fcu_switched_13a.png'),
        (0.65, 0.53, 0.79, 0.65, 'W421_fcu_switched_neon.png'),
        (0.79, 0.53, 0.93, 0.65, 'W419_fcu_switched_13a_neon.png'),
        
        # Co-axial & Satellite Outlets
        (0.13, 0.66, 0.26, 0.78, 'W166_satellite_socket_1g.png'),
        (0.26, 0.66, 0.39, 0.78, 'W168_satellite_socket_2g.png'),
        (0.39, 0.66, 0.52, 0.78, 'W167_satellite_coax_socket.png'),
        (0.52, 0.66, 0.65, 0.78, 'W169_coax_rj45_socket.png'),
        (0.65, 0.66, 0.79, 0.78, 'W432_coax_socket_1g.png'),
        (0.79, 0.66, 0.93, 0.78, 'W433_coax_socket_2g.png'),
        
        # Tel & Data Outlets
        (0.13, 0.79, 0.26, 0.90, 'W438_tel_socket_1g.png'),
        (0.26, 0.79, 0.39, 0.90, 'W440_tel_socket_2g.png'),
        (0.39, 0.79, 0.52, 0.90, 'W464_rj11_data_socket_1g.png'),
        (0.52, 0.79, 0.65, 0.90, 'W465_rj11_data_socket_2g.png'),
        (0.65, 0.79, 0.79, 0.90, 'W443_rj45_data_socket_2g.png'),
        
        # Connection Plate & Blank Plate
        (0.13, 0.91, 0.26, 1.00, 'W401_blank_plate_1g.png'),
        (0.26, 0.91, 0.45, 1.00, 'W402_blank_plate_2g.png'),
        (0.45, 0.91, 0.58, 1.00, 'W501_blank_plate_hole.png'),
        (0.58, 0.91, 0.72, 1.00, 'W820_connection_plate_20a.png'),
        (0.72, 0.91, 0.86, 1.00, 'W821_connection_plate_45a.png')
    ]
    
    for x1, y1, x2, y2, fname in crops_53:
        box = (int(x1 * w53), int(y1 * h53), int(x2 * w53), int(y2 * h53))
        cropped = img53.crop(box)
        cropped.save(os.path.join(out_dir, fname))
        cropped.save(os.path.join(pub_out_dir, fname))
        
    for x1, y1, x2, y2, fname in crops_54:
        box = (int(x1 * w54), int(y1 * h54), int(x2 * w54), int(y2 * h54))
        cropped = img54.crop(box)
        cropped.save(os.path.join(out_dir, fname))
        cropped.save(os.path.join(pub_out_dir, fname))
        
    print("All individual product thumbnails cropped successfully!")

if __name__ == '__main__':
    crop_catalog_items()
