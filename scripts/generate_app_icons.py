#!/usr/bin/env python3
"""Genera icone per Equi Budget e Reminder Max."""
import os
from cairosvg import svg2png

OUT_DIR = 'assets'
os.makedirs(OUT_DIR, exist_ok=True)

# EQUI BUDGET ICON
equi_icon_svg = '''<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="eqGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#A855F7"/>
      <stop offset="100%" stop-color="#6366F1"/>
    </linearGradient>
  </defs>
  <rect width="120" height="120" rx="28" fill="url(#eqGrad)"/>
  <circle cx="60" cy="50" r="24" fill="none" stroke="#fff" stroke-width="6" opacity="0.9"/>
  <path d="M60 30 L60 50 L75 50" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity="0.9"/>
  <text x="60" y="95" fill="#fff" font-family="SF Pro Display, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">€</text>
</svg>'''

# REMINDER MAX ICON
reminder_icon_svg = '''<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rmGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#06b6d4"/>
      <stop offset="100%" stop-color="#3b82f6"/>
    </linearGradient>
  </defs>
  <rect width="120" height="120" rx="28" fill="url(#rmGrad)"/>
  <circle cx="60" cy="55" r="28" fill="none" stroke="#fff" stroke-width="5" opacity="0.9"/>
  <path d="M60 35 L60 55 L75 65" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity="0.9"/>
  <circle cx="60" cy="20" r="6" fill="#fff" opacity="0.9"/>
  <path d="M35 90 Q60 75 85 90" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity="0.7"/>
</svg>'''

svg2png(bytestring=equi_icon_svg.encode('utf-8'), write_to=os.path.join(OUT_DIR, 'equi-budget-icon.png'), output_width=120, output_height=120)
svg2png(bytestring=reminder_icon_svg.encode('utf-8'), write_to=os.path.join(OUT_DIR, 'reminder-max-icon.png'), output_width=120, output_height=120)

print('Icone generate:')
print('  - assets/equi-budget-icon.png')
print('  - assets/reminder-max-icon.png')
