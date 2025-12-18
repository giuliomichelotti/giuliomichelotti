#!/usr/bin/env python3
"""Genera screenshot realistici per Equi Budget e Reminder Max basati sul codice effettivo."""
import os
from cairosvg import svg2png

OUT_DIR = 'assets'
os.makedirs(OUT_DIR, exist_ok=True)

# ===============================
# EQUI BUDGET SCREENSHOT
# ===============================
equi_budget_svg = '''<svg width="400" height="720" viewBox="0 0 400 720" xmlns="http://www.w3.org/2000/svg">
  <!-- Phone Frame -->
  <defs>
    <linearGradient id="fabGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#A855F7"/>
      <stop offset="100%" stop-color="#8B5CF6"/>
    </linearGradient>
    <linearGradient id="progressGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#A855F7"/>
      <stop offset="100%" stop-color="#6366F1"/>
    </linearGradient>
    <linearGradient id="cardGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1a1a24"/>
      <stop offset="100%" stop-color="#12121a"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#000" flood-opacity="0.3"/>
    </filter>
  </defs>
  
  <!-- Background -->
  <rect width="400" height="720" rx="40" fill="#0A0A0F"/>
  
  <!-- Status Bar -->
  <text x="24" y="44" fill="#888" font-family="SF Pro Display, -apple-system, sans-serif" font-size="14" font-weight="500">9:41</text>
  <g fill="#888">
    <rect x="320" y="34" width="24" height="12" rx="3"/>
    <rect x="322" y="36" width="18" height="8" rx="2" fill="#4ade80"/>
    <circle cx="300" cy="40" r="4"/>
    <circle cx="280" cy="40" r="4"/>
  </g>
  
  <!-- Header -->
  <text x="24" y="100" fill="#fff" font-family="SF Pro Display, -apple-system, sans-serif" font-size="24" font-weight="700">EquiBudget</text>
  <text x="24" y="124" fill="#888" font-family="SF Pro Display, -apple-system, sans-serif" font-size="14">Dicembre 2025</text>
  
  <!-- Balance Card -->
  <rect x="16" y="150" width="368" height="140" rx="20" fill="url(#cardGrad)" filter="url(#shadow)"/>
  <text x="36" y="185" fill="#888" font-family="SF Pro Display, -apple-system, sans-serif" font-size="13">Saldo disponibile</text>
  <text x="36" y="230" fill="#fff" font-family="SF Pro Display, -apple-system, sans-serif" font-size="42" font-weight="700">€ 2.847</text>
  <text x="180" y="230" fill="#4ade80" font-family="SF Pro Display, -apple-system, sans-serif" font-size="16" font-weight="600">.50</text>
  
  <!-- Progress Ring (42% come nel codice) -->
  <g transform="translate(300, 220)">
    <circle cx="0" cy="0" r="35" fill="none" stroke="#222" stroke-width="8"/>
    <circle cx="0" cy="0" r="35" fill="none" stroke="url(#progressGrad)" stroke-width="8" 
            stroke-dasharray="220 220" stroke-dashoffset="127" stroke-linecap="round"
            transform="rotate(-90)"/>
    <text x="0" y="5" fill="#fff" font-family="SF Pro Display, -apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">42%</text>
  </g>
  
  <!-- Fair Split Section -->
  <text x="24" y="330" fill="#fff" font-family="SF Pro Display, -apple-system, sans-serif" font-size="18" font-weight="600">Fair Split</text>
  
  <!-- Participants -->
  <rect x="16" y="345" width="368" height="70" rx="14" fill="url(#cardGrad)"/>
  <circle cx="50" cy="380" r="20" fill="#6366F1"/>
  <text x="50" y="385" fill="#fff" font-family="SF Pro Display, -apple-system, sans-serif" font-size="14" font-weight="600" text-anchor="middle">G</text>
  <text x="80" y="372" fill="#fff" font-family="SF Pro Display, -apple-system, sans-serif" font-size="14" font-weight="500">Giulio</text>
  <text x="80" y="392" fill="#4ade80" font-family="SF Pro Display, -apple-system, sans-serif" font-size="13">+€124.00</text>
  
  <circle cx="200" cy="380" r="20" fill="#EC4899"/>
  <text x="200" y="385" fill="#fff" font-family="SF Pro Display, -apple-system, sans-serif" font-size="14" font-weight="600" text-anchor="middle">M</text>
  <text x="230" y="372" fill="#fff" font-family="SF Pro Display, -apple-system, sans-serif" font-size="14" font-weight="500">Marco</text>
  <text x="230" y="392" fill="#f87171" font-family="SF Pro Display, -apple-system, sans-serif" font-size="13">-€62.00</text>
  
  <circle cx="330" cy="380" r="20" fill="#FBBF24"/>
  <text x="330" y="385" fill="#000" font-family="SF Pro Display, -apple-system, sans-serif" font-size="14" font-weight="600" text-anchor="middle">L</text>
  <text x="360" y="372" fill="#fff" font-family="SF Pro Display, -apple-system, sans-serif" font-size="14" font-weight="500">Luca</text>
  <text x="360" y="392" fill="#f87171" font-family="SF Pro Display, -apple-system, sans-serif" font-size="13">-€62.00</text>
  
  <!-- Recent Transactions -->
  <text x="24" y="455" fill="#fff" font-family="SF Pro Display, -apple-system, sans-serif" font-size="18" font-weight="600">Transazioni recenti</text>
  
  <!-- Transaction 1 -->
  <rect x="16" y="470" width="368" height="64" rx="12" fill="url(#cardGrad)"/>
  <rect x="28" y="482" width="40" height="40" rx="10" fill="#22c55e" opacity="0.2"/>
  <text x="48" y="508" fill="#22c55e" font-family="SF Pro Display, -apple-system, sans-serif" font-size="18">🛒</text>
  <text x="80" y="498" fill="#fff" font-family="SF Pro Display, -apple-system, sans-serif" font-size="14" font-weight="500">Spesa settimanale</text>
  <text x="80" y="518" fill="#666" font-family="SF Pro Display, -apple-system, sans-serif" font-size="12">Oggi, 14:32</text>
  <text x="350" y="502" fill="#f87171" font-family="SF Pro Display, -apple-system, sans-serif" font-size="15" font-weight="600" text-anchor="end">-€87.50</text>
  
  <!-- Transaction 2 -->
  <rect x="16" y="544" width="368" height="64" rx="12" fill="url(#cardGrad)"/>
  <rect x="28" y="556" width="40" height="40" rx="10" fill="#3b82f6" opacity="0.2"/>
  <text x="48" y="582" fill="#3b82f6" font-family="SF Pro Display, -apple-system, sans-serif" font-size="18">🍕</text>
  <text x="80" y="572" fill="#fff" font-family="SF Pro Display, -apple-system, sans-serif" font-size="14" font-weight="500">Cena pizzeria</text>
  <text x="80" y="592" fill="#666" font-family="SF Pro Display, -apple-system, sans-serif" font-size="12">Ieri, 21:15</text>
  <text x="350" y="576" fill="#f87171" font-family="SF Pro Display, -apple-system, sans-serif" font-size="15" font-weight="600" text-anchor="end">-€42.00</text>
  
  <!-- Transaction 3 -->
  <rect x="16" y="618" width="368" height="64" rx="12" fill="url(#cardGrad)"/>
  <rect x="28" y="630" width="40" height="40" rx="10" fill="#a855f7" opacity="0.2"/>
  <text x="48" y="656" fill="#a855f7" font-family="SF Pro Display, -apple-system, sans-serif" font-size="18">💰</text>
  <text x="80" y="646" fill="#fff" font-family="SF Pro Display, -apple-system, sans-serif" font-size="14" font-weight="500">Stipendio ricevuto</text>
  <text x="80" y="666" fill="#666" font-family="SF Pro Display, -apple-system, sans-serif" font-size="12">15 Dic, 09:00</text>
  <text x="350" y="650" fill="#4ade80" font-family="SF Pro Display, -apple-system, sans-serif" font-size="15" font-weight="600" text-anchor="end">+€1,850.00</text>
  
  <!-- FAB Button -->
  <circle cx="350" cy="650" r="28" fill="url(#fabGrad)" filter="url(#shadow)"/>
  <text x="350" y="658" fill="#fff" font-family="SF Pro Display, -apple-system, sans-serif" font-size="28" font-weight="300" text-anchor="middle">+</text>
  
  <!-- Home Indicator -->
  <rect x="140" y="700" width="120" height="5" rx="2.5" fill="#444"/>
</svg>'''

# ===============================
# REMINDER MAX SCREENSHOT
# ===============================
reminder_max_svg = '''<svg width="400" height="720" viewBox="0 0 400 720" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rmAccent" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#06b6d4"/>
      <stop offset="100%" stop-color="#3b82f6"/>
    </linearGradient>
    <linearGradient id="rmCard" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1a1a24"/>
      <stop offset="100%" stop-color="#12121a"/>
    </linearGradient>
    <linearGradient id="rmUrgent" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#f97316"/>
    </linearGradient>
    <filter id="rmShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#000" flood-opacity="0.3"/>
    </filter>
  </defs>
  
  <!-- Background -->
  <rect width="400" height="720" rx="40" fill="#0A0A0F"/>
  
  <!-- Status Bar -->
  <text x="24" y="44" fill="#888" font-family="SF Pro Display, -apple-system, sans-serif" font-size="14" font-weight="500">9:41</text>
  <g fill="#888">
    <rect x="320" y="34" width="24" height="12" rx="3"/>
    <rect x="322" y="36" width="18" height="8" rx="2" fill="#4ade80"/>
    <circle cx="300" cy="40" r="4"/>
    <circle cx="280" cy="40" r="4"/>
  </g>
  
  <!-- Header -->
  <text x="24" y="100" fill="#fff" font-family="SF Pro Display, -apple-system, sans-serif" font-size="24" font-weight="700">Reminder Max</text>
  <text x="24" y="124" fill="#888" font-family="SF Pro Display, -apple-system, sans-serif" font-size="14">4 promemoria attivi</text>
  
  <!-- Search Bar -->
  <rect x="16" y="145" width="368" height="44" rx="12" fill="#1a1a24"/>
  <text x="48" y="173" fill="#666" font-family="SF Pro Display, -apple-system, sans-serif" font-size="15">🔍  Cerca promemoria...</text>
  
  <!-- Filter Pills -->
  <rect x="16" y="200" width="70" height="32" rx="16" fill="url(#rmAccent)"/>
  <text x="51" y="221" fill="#fff" font-family="SF Pro Display, -apple-system, sans-serif" font-size="13" font-weight="600" text-anchor="middle">Tutti</text>
  <rect x="96" y="200" width="70" height="32" rx="16" fill="#1a1a24"/>
  <text x="131" y="221" fill="#888" font-family="SF Pro Display, -apple-system, sans-serif" font-size="13" text-anchor="middle">Oggi</text>
  <rect x="176" y="200" width="90" height="32" rx="16" fill="#1a1a24"/>
  <text x="221" y="221" fill="#888" font-family="SF Pro Display, -apple-system, sans-serif" font-size="13" text-anchor="middle">Ricorrenti</text>
  <rect x="276" y="200" width="90" height="32" rx="16" fill="#1a1a24"/>
  <text x="321" y="221" fill="#888" font-family="SF Pro Display, -apple-system, sans-serif" font-size="13" text-anchor="middle">Completati</text>
  
  <!-- Section: Urgenti -->
  <text x="24" y="270" fill="#ef4444" font-family="SF Pro Display, -apple-system, sans-serif" font-size="13" font-weight="600">⚠️ URGENTI</text>
  
  <!-- Reminder 1 - Urgent -->
  <rect x="16" y="285" width="368" height="80" rx="14" fill="url(#rmCard)" filter="url(#rmShadow)"/>
  <rect x="16" y="285" width="4" height="80" rx="2" fill="url(#rmUrgent)"/>
  <circle cx="44" cy="325" r="12" fill="#ef4444" opacity="0.2"/>
  <text x="44" y="330" fill="#ef4444" font-family="SF Pro Display, -apple-system, sans-serif" font-size="14" text-anchor="middle">🔔</text>
  <text x="68" y="315" fill="#fff" font-family="SF Pro Display, -apple-system, sans-serif" font-size="15" font-weight="600">Riunione con il team</text>
  <text x="68" y="335" fill="#888" font-family="SF Pro Display, -apple-system, sans-serif" font-size="12">Oggi, 15:00 • Sala conferenze B</text>
  <rect x="68" y="345" width="60" height="18" rx="4" fill="#ef4444" opacity="0.2"/>
  <text x="98" y="358" fill="#ef4444" font-family="SF Pro Display, -apple-system, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Tra 2 ore</text>
  <text x="360" y="330" fill="#666" font-family="SF Pro Display, -apple-system, sans-serif" font-size="18" text-anchor="end">⏰</text>
  
  <!-- Section: Oggi -->
  <text x="24" y="400" fill="#06b6d4" font-family="SF Pro Display, -apple-system, sans-serif" font-size="13" font-weight="600">📅 OGGI</text>
  
  <!-- Reminder 2 -->
  <rect x="16" y="415" width="368" height="80" rx="14" fill="url(#rmCard)"/>
  <rect x="16" y="415" width="4" height="80" rx="2" fill="#06b6d4"/>
  <circle cx="44" cy="455" r="12" fill="#06b6d4" opacity="0.2"/>
  <text x="44" y="460" fill="#06b6d4" font-family="SF Pro Display, -apple-system, sans-serif" font-size="14" text-anchor="middle">💊</text>
  <text x="68" y="445" fill="#fff" font-family="SF Pro Display, -apple-system, sans-serif" font-size="15" font-weight="600">Prendere vitamine</text>
  <text x="68" y="465" fill="#888" font-family="SF Pro Display, -apple-system, sans-serif" font-size="12">Ogni giorno, 08:00</text>
  <rect x="68" y="475" width="70" height="18" rx="4" fill="#06b6d4" opacity="0.2"/>
  <text x="103" y="488" fill="#06b6d4" font-family="SF Pro Display, -apple-system, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Ricorrente</text>
  <rect x="320" y="443" width="50" height="26" rx="6" fill="#22c55e"/>
  <text x="345" y="461" fill="#fff" font-family="SF Pro Display, -apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Fatto</text>
  
  <!-- Reminder 3 -->
  <rect x="16" y="505" width="368" height="80" rx="14" fill="url(#rmCard)"/>
  <rect x="16" y="505" width="4" height="80" rx="2" fill="#a855f7"/>
  <circle cx="44" cy="545" r="12" fill="#a855f7" opacity="0.2"/>
  <text x="44" y="550" fill="#a855f7" font-family="SF Pro Display, -apple-system, sans-serif" font-size="14" text-anchor="middle">🏋️</text>
  <text x="68" y="535" fill="#fff" font-family="SF Pro Display, -apple-system, sans-serif" font-size="15" font-weight="600">Allenamento palestra</text>
  <text x="68" y="555" fill="#888" font-family="SF Pro Display, -apple-system, sans-serif" font-size="12">Lun, Mer, Ven • 18:30</text>
  <rect x="68" y="565" width="70" height="18" rx="4" fill="#a855f7" opacity="0.2"/>
  <text x="103" y="578" fill="#a855f7" font-family="SF Pro Display, -apple-system, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Ricorrente</text>
  <rect x="320" y="533" width="50" height="26" rx="6" fill="#1a1a24" stroke="#444" stroke-width="1"/>
  <text x="345" y="551" fill="#888" font-family="SF Pro Display, -apple-system, sans-serif" font-size="11" text-anchor="middle">Snooze</text>
  
  <!-- Reminder 4 - Location based -->
  <rect x="16" y="595" width="368" height="80" rx="14" fill="url(#rmCard)"/>
  <rect x="16" y="595" width="4" height="80" rx="2" fill="#f59e0b"/>
  <circle cx="44" cy="635" r="12" fill="#f59e0b" opacity="0.2"/>
  <text x="44" y="640" fill="#f59e0b" font-family="SF Pro Display, -apple-system, sans-serif" font-size="14" text-anchor="middle">📍</text>
  <text x="68" y="625" fill="#fff" font-family="SF Pro Display, -apple-system, sans-serif" font-size="15" font-weight="600">Comprare il latte</text>
  <text x="68" y="645" fill="#888" font-family="SF Pro Display, -apple-system, sans-serif" font-size="12">Quando arrivi al supermercato</text>
  <rect x="68" y="655" width="70" height="18" rx="4" fill="#f59e0b" opacity="0.2"/>
  <text x="103" y="668" fill="#f59e0b" font-family="SF Pro Display, -apple-system, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Geofence</text>
  
  <!-- FAB Button -->
  <circle cx="350" cy="650" r="28" fill="url(#rmAccent)" filter="url(#rmShadow)"/>
  <text x="350" y="658" fill="#fff" font-family="SF Pro Display, -apple-system, sans-serif" font-size="28" font-weight="300" text-anchor="middle">+</text>
  
  <!-- Home Indicator -->
  <rect x="140" y="700" width="120" height="5" rx="2.5" fill="#444"/>
</svg>'''

# Generate PNG files
svg2png(bytestring=equi_budget_svg.encode('utf-8'), write_to=os.path.join(OUT_DIR, 'equi-budget-screenshot.png'), output_width=400, output_height=720)
svg2png(bytestring=reminder_max_svg.encode('utf-8'), write_to=os.path.join(OUT_DIR, 'reminder-max-screenshot.png'), output_width=400, output_height=720)

print('Screenshots generati:')
print('  - assets/equi-budget-screenshot.png')
print('  - assets/reminder-max-screenshot.png')
