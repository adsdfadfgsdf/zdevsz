import glob
import re
import os

css_old = r'''.mobile-menu-toggle { display: none; }'''

css_media_old = r'''.mobile-menu-toggle {
        display: flex; flex-direction: column; gap: 4px;
        background: none; border: none; cursor: pointer; padding: 4px;
        position: relative; z-index: 200;
      }
      .mobile-menu-toggle .bar {
        width: 20px; height: 2px; background: var(--bone); transition: 0.3s;
      }
      .mobile-menu-toggle.active .bar:nth-child(1) { transform: translateY(6px) rotate(45deg); }
      .mobile-menu-toggle.active .bar:nth-child(2) { opacity: 0; }
      .mobile-menu-toggle.active .bar:nth-child(3) { transform: translateY(-6px) rotate(-45deg); }'''

js_old = r'''const mobileMenuToggle = document.getElementById('mobileMenuToggle');
    const navLinks = document.getElementById('navLinks');
    if (mobileMenuToggle && navLinks) {
      mobileMenuToggle.addEventListener('click', () => {
        mobileMenuToggle.classList.toggle('active');
        navLinks.classList.toggle('active');
      });
      navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
          mobileMenuToggle.classList.remove('active');
          navLinks.classList.remove('active');
        });
      });
    }'''

html_old = r'''<button class="mobile-menu-toggle" id="mobileMenuToggle" aria-label="Menu">
      <div class="bar"></div><div class="bar"></div><div class="bar"></div>
    </button>'''

for f in glob.glob('*.html'):
    content = open(f, encoding='utf-8').read()
    
    # 1. Remove HTML
    content = content.replace(html_old, '')
    
    # 2. Remove CSS globally
    content = content.replace(css_old, '')
    
    # 3. Remove CSS in media query
    content = content.replace(css_media_old, '')
    
    # 4. Remove JS
    content = content.replace(js_old, '')
    
    with open(f, 'w', encoding='utf-8') as out:
        out.write(content)
        
    print(f"Removed hamburger from {f}")
