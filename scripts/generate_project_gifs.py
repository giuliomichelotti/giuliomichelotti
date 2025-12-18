#!/usr/bin/env python3
"""Genera GIF demo semplificate per i progetti Equi Budget e Reminder Max."""
from math import sin, pi
import os
from cairosvg import svg2png
import imageio

OUT_DIR = 'assets'
os.makedirs(OUT_DIR, exist_ok=True)
FPS = 12
DURATION_S = 2.5
FRAMES = int(FPS * DURATION_S)

def make_gif_for_project(name, filename, animate_func):
    frames = []
    for i in range(FRAMES):
        t = i / FRAMES * DURATION_S
        svg = f'''<svg width="600" height="240" viewBox="0 0 600 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="240" rx="12" fill="#071021" />
  <text x="24" y="46" fill="#e6eef6" font-size="28" font-family="Verdana, Geneva, sans-serif" font-weight="700">{name}</text>
  <text x="24" y="80" fill="#9aa6b2" font-size="14">Semplice demo animata</text>
  {animate_func(t)}
</svg>'''
        png = svg2png(bytestring=svg.encode('utf-8'), output_width=600, output_height=240)
        frames.append(imageio.v2.imread(png, format='PNG'))
    imageio.mimsave(os.path.join(OUT_DIR, filename), frames, format='GIF', duration=1.0/FPS)

# Equi Budget: animate a pie slice / bar growing
def equi_anim(t):
    # progress 0..1 oscillating
    p = 0.3 + 0.7 * (0.5 + 0.5 * sin(2 * pi * t / 2.5))
    w = 520 * p
    return f'<rect x="24" y="120" width="520" height="28" rx="8" fill="#2ec4b6" opacity="0.95" transform="scale({p},1) translate({(1-p)*260},0)"/>'

# Reminder Max: animate list items fading in/out
def reminder_anim(t):
    items = ''
    for i in range(4):
        off = (i*0.12 + (0.5 + 0.5 * sin(2*pi*t/2.5))*0.4)
        y = 110 + i*28
        op = 0.3 + 0.7 * max(0, 1 - abs(off-0.2)*3)
        items += f'<rect x="24" y="{y}" width="520" height="20" rx="6" fill="#7b61ff" opacity="{op:.2f}" />\n'
    return items

if __name__ == '__main__':
    make_gif_for_project('Equi Budget', 'equi-budget-demo.gif', equi_anim)
    make_gif_for_project('Reminder Max', 'reminder-max-demo.gif', reminder_anim)
    print('Project GIFs generated in assets/')
