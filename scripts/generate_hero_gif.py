#!/usr/bin/env python3
"""Genera un GIF animato dall'header SVG definito internamente.
Usa cairosvg per conversione SVG->PNG e imageio per creare il GIF.
"""
from math import sin, pi
import os
from cairosvg import svg2png
import imageio

OUT_DIR = 'assets'
OUT_GIF = os.path.join(OUT_DIR, 'hero-demo.gif')
FRAME_W = 1200
FRAME_H = 120
FPS = 12
DURATION_S = 3.0
FRAMES = int(FPS * DURATION_S)

SVG_TEMPLATE = '''<svg width="{w}" height="{h}" viewBox="0 0 1200 120" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="g" x1="0" x2="1">
      <stop offset="0" stop-color="#6EE7B7"/>
      <stop offset="0.5" stop-color="#60A5FA"/>
      <stop offset="1" stop-color="#C084FC"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="120" fill="url(#g)"/>
  <g font-family="Verdana, Geneva, sans-serif" font-weight="700" font-size="36" fill="white">
    <text x="40" y="70">Giulio Michelotti — Web Developer &amp; Product-focused Designer</text>
  </g>
  <!-- moving circles rendered per-frame -->
  <g fill="white" opacity="0.06">
    <circle cx="{cx1:.2f}" cy="{cy1:.2f}" r="40"/>
    <circle cx="{cx2:.2f}" cy="{cy2:.2f}" r="70"/>
  </g>
</svg>'''

os.makedirs(OUT_DIR, exist_ok=True)

frames = []
for i in range(FRAMES):
    t = i / FRAMES * DURATION_S
    # Simulate the two animations: slow small orbit for circle1, slower horizontal back-and-forth for circle2
    cx1 = 1100 + 40 * sin(2 * pi * t / 3.0)
    cy1 = 30 + 20 * sin(2 * pi * t / 4.0)
    cx2 = 1000 + 60 * sin(2 * pi * t / 4.0)
    cy2 = 90

    svg = SVG_TEMPLATE.format(w=FRAME_W, h=FRAME_H, cx1=cx1, cy1=cy1, cx2=cx2, cy2=cy2)
    png_bytes = svg2png(bytestring=svg.encode('utf-8'), output_width=FRAME_W, output_height=FRAME_H)
    frames.append(imageio.v2.imread(png_bytes, format='PNG'))

# Save GIF
imageio.mimsave(OUT_GIF, frames, format='GIF', duration=1.0 / FPS)
print('Saved', OUT_GIF)
