/**
 * Blit Electrical - Mobile Navigation Drawer Handler
 */
document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('.main-header');
  const toggleBtn = document.querySelector('.mobile-menu-toggle');
  
  if (!toggleBtn || !header) return;
  
  toggleBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    header.classList.toggle('menu-open');
    if (header.classList.contains('menu-open')) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
    }
  });

  // Close menu when any link inside nav-menu-wrapper is clicked
  const menuLinks = document.querySelectorAll('.nav-menu-wrapper a');
  menuLinks.forEach(link => {
    link.addEventListener('click', () => {
      header.classList.remove('menu-open');
      document.body.style.overflow = '';
    });
  });

  // Close menu when clicking outside the menu wrapper
  document.addEventListener('click', (e) => {
    if (header.classList.contains('menu-open')) {
      const menuWrapper = document.querySelector('.nav-menu-wrapper');
      if (menuWrapper && !menuWrapper.contains(e.target) && !toggleBtn.contains(e.target)) {
        header.classList.remove('menu-open');
        document.body.style.overflow = '';
      }
    }
  });
});
