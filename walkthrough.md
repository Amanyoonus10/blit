# Walkthrough - Switches Hero Full-Screen Image Update

Updated the Switches & Sockets page hero section on [switches.html](file:///Users/amanyoonus/Desktop/Blit/switches.html) so your uploaded studio photograph fills the screen **100% full screen edge-to-edge**.

## Layout Updates

1. **Edge-to-Edge Full-Screen Photography**:
   - Expanded background photography to span **100% viewport width and full height** (`width: 100%`, `min-height: calc(100vh - 70px)`).
   - Removed all inner card margins, border radii, and dark padding boxes around the image.
   - Text overlay is cleanly positioned over a dark slate gradient fade (`rgba(11, 15, 23, 0.95)` to `transparent`) on the left side, allowing the full studio photograph to fill the screen edge-to-edge.

2. **Deployed to Production**:
   - Committed (`5a43e3a`) and pushed to `main` on GitHub for Vercel deployment.
