import express from 'express';
import cors from 'cors';
import path from 'path';
import { fileURLToPath } from 'url';
import { PRODUCTS_DATA, IMAGE_BG_MAP } from './products-data.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;

// Enable CORS and JSON body parsing
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static assets from public, assets, and root directories
app.use('/public', express.static(path.join(__dirname, 'public')));
app.use('/assets', express.static(path.join(__dirname, 'assets')));
app.use('/assets', express.static(path.join(__dirname, 'public', 'assets')));
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.static(__dirname));

// HTML Page Routes
const pageRoutes = {
  '/': 'index.html',
  '/switches': 'switches.html',
  '/product': 'product.html',
  '/weatherproof': 'weatherproof.html',
  '/wiring-accessories': 'wiring-accessories.html',
  '/cable-management': 'cable-management.html',
  '/cable-termination': 'cable-termination.html',
  '/installation-boxes': 'installation-boxes.html',
  '/air-ventilation': 'air-ventilation.html',
  '/insect-killer': 'insect-killer.html'
};

Object.entries(pageRoutes).forEach(([route, file]) => {
  app.get(route, (req, res) => {
    res.sendFile(path.join(__dirname, file));
  });
  if (route !== '/') {
    app.get(`${route}.html`, (req, res) => {
      res.sendFile(path.join(__dirname, file));
    });
  }
});

// REST API Endpoints

// Health Check API
app.get('/api/health', (req, res) => {
  res.json({
    status: 'online',
    server: 'Node.js / Express',
    uptime: process.uptime(),
    timestamp: new Date().toISOString()
  });
});

// Get all product categories
app.get('/api/categories', (req, res) => {
  const categories = PRODUCTS_DATA.map(cat => ({
    id: cat.id,
    name: cat.name,
    tagline: cat.tagline,
    productCount: cat.products ? cat.products.length : 0,
    ranges: cat.ranges || []
  }));
  res.json(categories);
});

// Get products (optionally filter by category)
app.get('/api/products', (req, res) => {
  const { category } = req.query;
  
  if (category) {
    const foundCategory = PRODUCTS_DATA.find(c => c.id.toLowerCase() === category.toLowerCase());
    if (!foundCategory) {
      return res.status(404).json({ error: `Category '${category}' not found.` });
    }
    return res.json(foundCategory);
  }
  
  res.json(PRODUCTS_DATA);
});

// Get specific product by name or code
app.get('/api/products/:name', (req, res) => {
  const targetName = decodeURIComponent(req.params.name).toLowerCase();
  
  for (const category of PRODUCTS_DATA) {
    const product = category.products.find(p => p.name.toLowerCase() === targetName);
    if (product) {
      return res.json({
        category: { id: category.id, name: category.name },
        product,
        imageBg: IMAGE_BG_MAP[product.img] || '#FAFAFA'
      });
    }
  }
  
  res.status(404).json({ error: `Product '${req.params.name}' not found.` });
});

// Process product inquiries
app.post('/api/inquire', (req, res) => {
  const { fullName, email, phone, message, productName, category } = req.body;
  
  if (!fullName || !email) {
    return res.status(400).json({ error: 'Full name and email address are required.' });
  }

  console.log(`[INQUIRY RECEIVED] Name: ${fullName} | Email: ${email} | Phone: ${phone || 'N/A'} | Product: ${productName || 'General'}`);

  res.json({
    success: true,
    message: 'Thank you! Your product inquiry has been logged successfully.',
    inquiryData: { fullName, email, phone, productName, timestamp: new Date().toISOString() }
  });
});

// Start Node.js Express Web Server
app.listen(PORT, () => {
  console.log(`====================================================`);
  console.log(`🚀 BLIT Electrical Node.js Server is active!`);
  console.log(`📡 Listening on http://localhost:${PORT}`);
  console.log(`====================================================`);
});
