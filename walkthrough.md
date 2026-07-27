# Walkthrough - Switches Hero Image Shroud Fix

Fixed dark/dim hero background image visibility on [switches.html](file:///Users/amanyoonus/Desktop/Blit/switches.html).

## Why It Looked Dark & What Was Fixed

1. **Heavy Gradient Overlay Opacity**:
   - The `.switches-hero` CSS class previously had an 85% opacity dark overlay (`rgba(0,0,0,0.85)`), which heavily obscured the background image and made it look pitch black / un-changed.
   - Reduced overlay opacity to a subtle, crystal-clear gradient (`rgba(0,0,0,0.45)` to `rgba(0,0,0,0.05)`).

2. **Image Brightness & Vibrancy**:
   - Processed `switches_sockets_hero.jpg` and `switches_sockets_hero.webp` with enhanced brightness (+8%) and contrast (+5%) at 98% quality.

---

## Deployment Status

- **Git Commit**: `35518ce`
- **GitHub Push**: Successfully pushed to `origin main` at `https://github.com/Amanyoonus10/blit.git` (Vercel deployment auto-updated).
