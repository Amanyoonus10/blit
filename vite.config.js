import { resolve } from 'path';
import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        product: resolve(__dirname, 'product.html'),
        switches: resolve(__dirname, 'switches.html'),
        weatherproof: resolve(__dirname, 'weatherproof.html'),
        'wiring-accessories': resolve(__dirname, 'wiring-accessories.html'),
        'cable-management': resolve(__dirname, 'cable-management.html'),
        'cable-termination': resolve(__dirname, 'cable-termination.html'),
        'installation-boxes': resolve(__dirname, 'installation-boxes.html'),
        'air-ventilation': resolve(__dirname, 'air-ventilation.html'),
      },
    },
  },
});
