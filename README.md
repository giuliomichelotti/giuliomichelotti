<div align="center">

<!-- ANIMATED HEADER -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=180&section=header&text=Giulio%20Michelotti&fontSize=42&fontColor=fff&animation=twinkling&fontAlignY=32&desc=Full%20Stack%20Developer%20%7C%20Product%20Designer%20%7C%20UX%20Engineer&descAlignY=52&descSize=18"/>

<!-- TYPING SVG -->
<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=6EE7B7&center=true&vCenter=true&multiline=true&repeat=true&width=800&height=100&lines=Crafting+seamless+digital+experiences+%F0%9F%9A%80;Building+products+that+solve+real+problems+%F0%9F%92%A1;Code+%2B+Design+%3D+Magic+%E2%9C%A8" alt="Typing SVG" /></a>

<!-- PROFILE VIEWS & SOCIAL BADGES -->
<p>
<img src="https://komarev.com/ghpvc/?username=giuliomichelotti&label=Profile%20Views&color=6EE7B7&style=for-the-badge" alt="Profile Views" />
<a href="https://github.com/giuliomichelotti?tab=followers"><img src="https://img.shields.io/github/followers/giuliomichelotti?label=Followers&style=for-the-badge&color=60A5FA" alt="Followers"/></a>
<img src="https://img.shields.io/badge/Focus-Full%20Stack-C084FC?style=for-the-badge" alt="Focus"/>
</p>

</div>

---

## 🧠 La Mia Filosofia di Sviluppo

<table>
<tr>
<td width="50%">

### 🎯 Product-First Thinking

Non scrivo codice per il gusto di farlo. **Ogni riga di codice deve risolvere un problema reale**. Prima di toccare la tastiera, mi chiedo sempre:

- *Chi userà questo prodotto?*
- *Quale problema stiamo risolvendo?*
- *Qual è l'esperienza ideale per l'utente?*

Questo approccio mi ha portato a sviluppare **Equi Budget** e **Reminder Max** — due applicazioni nate da esigenze concrete, non da esercizi tecnici.

</td>
<td width="50%">

### ⚡ Full Stack con Passione

```javascript
const giulio = {
  frontend: ["React", "React Native", "TypeScript", "CSS Animations"],
  backend: ["Node.js", "Express", "WebSockets", "REST APIs"],
  database: ["SQLite", "Firebase", "localStorage"],
  philosophy: "Ship fast, iterate faster",
  superpower: "Turning complex problems into elegant UIs"
};
```

</td>
</tr>
</table>

### 🔮 I Tre Pilastri del Mio Codice

<div align="center">

| 🏗️ **Architettura Solida** | 🎨 **Design Intenzionale** | 🚀 **Performance Ossessiva** |
|:---:|:---:|:---:|
| Offline-first, sync quando possibile | Ogni pixel ha uno scopo | Ogni millisecondo conta |
| Modularità e riusabilità | Microinterazioni che guidano | Bundle size ottimizzato |
| Error handling elegante | Accessibilità by default | Lazy loading strategico |

</div>

---

## 🏆 Progetti Flagship

<div align="center">
<img src="assets/hero-demo.gif" alt="Hero Animation" width="90%"/>
</div>

---

### 💰 Equi Budget — *"La Finanza Personale, Semplificata"*

<table>
<tr>
<td width="45%">
<img src="assets/equi-budget-demo.gif" alt="Equi Budget Demo" width="100%"/>
</td>
<td width="55%">

#### 🎯 Il Problema
Gestire le spese condivise è un incubo: chi ha pagato cosa, chi deve a chi, quanto resta del budget. Fogli Excel confusi, note sul telefono, discussioni infinite.

#### ✨ La Soluzione
**Equi Budget** è un'app di budgeting che ho progettato e sviluppato con un obiettivo chiaro: **rendere la gestione finanziaria condivisa così semplice da essere piacevole**.

#### 🛠️ Stack Tecnologico
```
Frontend:    React Native + TypeScript
State:       Context API + useReducer  
Storage:     SQLite (offline-first)
Sync:        WebSockets (real-time)
Animations:  Reanimated 2 + Moti
```

#### 🌟 Features Chiave
- **Fair-Split Algorithm** — Distribuzione equa automatica
- **Category Breakdown** — Visualizzazione spending per categoria
- **Offline-First** — Funziona senza internet, sync quando disponibile
- **Real-time Sync** — Aggiornamenti istantanei tra dispositivi
- **Export/Import** — Backup JSON per portabilità totale

</td>
</tr>
</table>

<details>
<summary><b>📐 Architettura Tecnica di Equi Budget</b></summary>

```
┌─────────────────────────────────────────────────────────────┐
│                      PRESENTATION LAYER                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │  Dashboard  │  │ Transaction │  │   Category Charts   │  │
│  │   Screen    │  │   List      │  │   (Pie/Bar)         │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                      BUSINESS LOGIC                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │ Fair-Split  │  │   Budget    │  │   Sync Manager      │  │
│  │  Calculator │  │   Engine    │  │   (WebSocket)       │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                      DATA LAYER                              │
│  ┌─────────────────────┐  ┌─────────────────────────────┐   │
│  │   SQLite (Local)    │  │   Firebase (Cloud Backup)   │   │
│  └─────────────────────┘  └─────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

</details>

---

### ⏰ Reminder Max — *"Mai Più un Promemoria Dimenticato"*

<table>
<tr>
<td width="55%">

#### �� Il Problema
Le app di reminder esistenti sono o troppo semplici (mancano le ricorrenze) o troppo complesse (interfacce confuse, troppe opzioni). Serviva qualcosa nel mezzo perfetto.

#### ✨ La Soluzione
**Reminder Max** è un'app di promemoria che ho costruito con un'ossessione: **potenza sotto il cofano, semplicità in superficie**.

#### 🛠️ Stack Tecnologico
```
Frontend:    React Native + TypeScript
Notifications: Firebase Cloud Messaging
Background:  Background Tasks API
Storage:     AsyncStorage + SQLite
Animations:  Lottie + CSS Keyframes
```

#### 🌟 Features Chiave
- **Smart Recurrence** — Daily, weekly, monthly, custom patterns
- **Geofencing** — Reminder basati sulla posizione
- **Snooze Intelligence** — Snooze adattivo che impara le tue abitudini
- **Keyboard-First** — Inserimento rapido per power users
- **Zero Battery Drain** — Ottimizzato per consumi minimi

</td>
<td width="45%">
<img src="assets/reminder-max-demo.gif" alt="Reminder Max Demo" width="100%"/>
</td>
</tr>
</table>

<details>
<summary><b>📐 Architettura Tecnica di Reminder Max</b></summary>

```
┌─────────────────────────────────────────────────────────────┐
│                    NOTIFICATION SYSTEM                       │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │   Local     │  │   Push      │  │   Geofence          │  │
│  │   Notif.    │  │   (FCM)     │  │   Triggers          │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                    SCHEDULING ENGINE                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │ Recurrence  │  │   Snooze    │  │   Priority          │  │
│  │  Parser     │  │   Manager   │  │   Queue             │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                    PERSISTENCE                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         SQLite + AsyncStorage (Hybrid)              │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

</details>

---

## 🛠️ Tech Arsenal

<div align="center">

### Languages & Core
<p>
<img src="https://skillicons.dev/icons?i=html,css,js,ts,python&theme=dark" />
</p>

### Frontend & Mobile
<p>
<img src="https://skillicons.dev/icons?i=react,nextjs,tailwind,sass,bootstrap&theme=dark" />
</p>

### Backend & Database
<p>
<img src="https://skillicons.dev/icons?i=nodejs,express,firebase,sqlite,mongodb&theme=dark" />
</p>

### Tools & DevOps
<p>
<img src="https://skillicons.dev/icons?i=git,github,vscode,figma,webpack,docker&theme=dark" />
</p>

</div>

---

## 📊 GitHub Analytics

<div align="center">

<img width="49%" src="https://github-readme-stats.vercel.app/api?username=giuliomichelotti&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=6EE7B7&icon_color=60A5FA&text_color=FFFFFF" />
<img width="49%" src="https://github-readme-streak-stats.herokuapp.com/?user=giuliomichelotti&theme=tokyonight&hide_border=true&background=0D1117&stroke=6EE7B7&ring=60A5FA&fire=C084FC&currStreakLabel=6EE7B7" />

<img width="40%" src="https://github-readme-stats.vercel.app/api/top-langs/?username=giuliomichelotti&layout=compact&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=6EE7B7&text_color=FFFFFF" />

</div>

---

## 🐍 Contribution Graph

<div align="center">
<img src="https://raw.githubusercontent.com/giuliomichelotti/giuliomichelotti/output/snake.svg" alt="Snake animation" />
</div>

---

## 📫 Let's Connect

<div align="center">

<p>
<a href="https://github.com/giuliomichelotti"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" /></a>
<a href="https://linkedin.com/in/giuliomichelotti"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
<a href="https://instagram.com/giuliomichelotti"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" /></a>
<a href="mailto:giuliomichelottioutlook.it"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
</p>

### 💬 Open to...
**Collaborazioni** • **Freelance Projects** • **Full-time Opportunities** • **Open Source**

<br>

*"Il codice migliore è quello che non devi scrivere. Il secondo migliore è quello che chiunque può capire."*

</div>

---

<div align="center">

<!-- FOOTER WAVE -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer"/>

<sub>Crafted with ❤️ and lots of ☕ by Giulio Michelotti</sub>

</div>
