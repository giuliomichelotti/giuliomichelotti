````markdown name=README.md
# Hi — I'm Giulio Michelotti 👋

<svg width="100%" height="120" viewBox="0 0 1200 120" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg" style="display:block;margin-bottom:18px">
  <defs>
    <linearGradient id="g" x1="0" x2="1">
      <stop offset="0" stop-color="#6EE7B7"/>
      <stop offset="0.5" stop-color="#60A5FA"/>
      <stop offset="1" stop-color="#C084FC"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="120" fill="url(#g)"/>
  <g font-family="Verdana, Geneva, sans-serif" font-weight="700" font-size="36" fill="white">
    <text x="40" y="70">Giulio Michelotti — Web Developer & Product-focused Designer</text>
  </g>
  <!-- subtle moving circles -->
  <g fill="white" opacity="0.06">
    <circle cx="1100" cy="30" r="40">
      <animate attributeName="cx" from="1100" to="1150" dur="6s" repeatCount="indefinite" />
      <animate attributeName="cy" from="30" to="60" dur="6s" repeatCount="indefinite" />
    </circle>
    <circle cx="1000" cy="90" r="70">
      <animate attributeName="cx" from="1000" to="950" dur="8s" repeatCount="indefinite" />
    </circle>
  </g>
</svg>

![Hero animation](assets/hero-demo.gif)

> ✅ Ho aggiunto una GIF animata dell'intestazione e demo GIF per i progetti: queste animazioni sono visibili direttamente su GitHub.

[![HTML5](https://img.shields.io/badge/HTML-Expert-orange?style=for-the-badge&logo=html5)]
[![CSS3](https://img.shields.io/badge/CSS-Advanced-blue?style=for-the-badge&logo=css3)]
[![JavaScript](https://img.shields.io/badge/JavaScript-Expert-yellow?style=for-the-badge&logo=javascript)]
[![Responsive](https://img.shields.io/badge/Responsive-Design-9cf?style=for-the-badge)]

Welcome to my portfolio repository. I build clean, accessible, and performant web experiences using modern HTML, CSS and JavaScript. I care about design detail, thoughtful UX, and delivering products that solve real problems.

---

## About me

I design and develop front-end applications and web tools with a product mindset. My focus is on turning ideas into polished, usable interfaces that are responsive and maintainable. I like clear code, reusable components (where appropriate), and shipping features that users actually find valuable.

Core strengths:
- Pixel-perfect responsive layouts with modern CSS (Flexbox, Grid)
- Interactive UI built with vanilla JavaScript and progressive enhancement
- UX-first approach: accessibility, performance, and clarity
- Practical tooling: Git, npm, build scripts, and simple deployment flows

---

## Skills & Technologies

Languages
- HTML5 — semantic markup, accessibility best practices
- CSS3 — modern layout (Grid/Flexbox), transitions, animations, responsive patterns
- JavaScript (ES6+) — DOM manipulation, event handling, modular code, async flows

Frontend Practices
- Responsive Design & Mobile-first Development
- CSS Animations & Microinteractions
- Form validation and client-side state handling
- Local persistence (localStorage) and graceful degradation

Tools & Workflow
- Git & GitHub for version control
- npm / basic build tooling
- Browser devtools, Lighthouse for performance & accessibility audits

Design & Prototyping
- Wireframing, layout composition, iterative UI improvements
- Focus on clarity, accessibility (WCAG-minded), and user flows

---

## Featured Projects

Below are two highlighted projects available in this repository. Each project includes a short overview, the main features, and notes on how to run or demo them locally.

### Equi Budget
A clean, intuitive budgeting tool focused on fairness and clarity.

What it does
- Track incomes and expenses in a simple ledger-style interface
- Split shared expenses fairly across participants
- Visualize spending categories (pie/bar charts) and recent trends
- Export and import simple JSON backups

Key features
- Fair-split algorithm for shared costs (Equitable distribution per participant)
- Category breakdown and recent transactions list
- Mobile-first layout with smooth CSS microinteractions

Tech & approach
- Built with semantic HTML, modular CSS, and vanilla JavaScript
- Data persisted locally (localStorage) for instant, offline-friendly use
- Designed for easy extension to backend sync or CSV/JSON export

How to run locally
1. Clone the repo
2. Open `index.html` in a browser (no build step required)
3. Optionally run a static server to enable relative file requests:
   - `npx http-server .` and open `http://localhost:8080`

![Equi Budget demo](assets/equi-budget-demo.gif)

Suggested improvements (ideas for future versions)
- Add user accounts and cloud sync
- Integrate charting library for more advanced visuals
- Add multi-currency and recurring payments support

---

### Reminder Max
A lightweight, reliable reminders and tasks app focused on recurring reminders and notification clarity.

What it does
- Create one-off and recurring reminders with title, notes, and due date/time
- Snooze and complete actions with clear visual feedback
- Filter and search reminders by date, priority and tags

Key features
- Recurrence patterns (daily, weekly, monthly) and snooze functionality
- Clear, keyboard-friendly UI for rapid entry and management
- Mobile-friendly layout and accessible controls

Tech & approach
- Implemented with HTML, CSS and JavaScript for maximum portability
- Client-side storage for quick persistence and offline usage
- Emphasis on UX details: focus states, clear affordances, and confirmation flows

How to run locally
- Same as Equi Budget: open `index.html` or run a simple static server

![Reminder Max demo](assets/reminder-max-demo.gif)

Suggested improvements
- Desktop or mobile notifications (Service Workers + Push)
- Sync across devices and calendar integration (iCal / Google Calendar)
- Reminders grouped by project and enriched with attachments

---

## Visuals & Assets

To present polished visuals and animated previews, include:
- GIF or MP4 demos inside `assets/` (e.g., `assets/equi-budget-demo.gif`, `assets/reminder-max-demo.gif`)
- High-resolution screenshots in `assets/screenshots/` for the README showcase

Example markdown to embed a demo once assets are added:
![Equi Budget demo](assets/equi-budget-demo.gif)

---

## Design & Animation Philosophy

I use subtle animations and microinteractions to increase clarity, not distract:
- Animated affordances (hover states, pressed states)
- Smooth transitions when content reflows
- Animations that communicate state (saving, error, success)

The goal is delightful, but purposeful, motion.

---

## How to explore this repo

- index.html — entry/demo page to preview the projects
- styles.css — global styling and responsive rules
- scripts.js / App.js — interactive behavior and app logic
- assets/ — place screenshots and demos here for the README to reference

Run locally:
- Open `index.html` directly, or
- Serve the repository with a static server: `npx http-server .`

---

## Contact & Next steps

I'm always open to interesting projects, collaboration or roles where I can both design and implement delightful front-end experiences.

- GitHub: https://github.com/giuliomichelotti
- Email: (add your preferred contact email here)
- LinkedIn / Portfolio: (add links here)

---

## License

This portfolio content and associated sample code are available under the MIT License. Replace or adapt license text as you prefer.

---

If you'd like, I can:
- Replace the existing README.md in the repository with this version (open a pull request),
- Generate optimized animated GIF previews for the projects and place them in `assets/`,
- Or tailor content to include additional languages, frameworks, or links you'd like highlighted.

Tell me which of those you'd like me to do next and I will proceed.
````
