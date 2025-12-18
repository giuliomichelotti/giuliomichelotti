👋 Ciao, sono Giulio Michelotti
Full Stack Developer & Mobile App Creator

📧 Email • 🐙 GitHub

🚀 I Miei Progetti
💰 EquiBudget — Gestione Finanziaria Personale
Version React Native Expo Platform

EquiBudget è un'applicazione mobile cross‑platform per la gestione delle finanze personali, sviluppata con React Native ed Expo. L'app punta a offrire un'esperienza utente premium con design in stile glassmorphism, animazioni fluide e funzioni avanzate di budgeting.

✨ Caratteristiche Principali
Persistenza dati locale (SQLite su mobile, AsyncStorage su web)
Dashboard in tempo reale con grafici interattivi
Aggiunta/gestione rapida delle transazioni (quick amounts)
Categorie personalizzabili, cronologia con filtri e ricerca
Obiettivi con barre di progresso e notifiche
Budget mensile per categoria con alert automatici
Privacy first: nessun tracking esterno e dati salvati localmente
🎨 Design & Animazioni (Animations & UX)
EquiBudget integra un set di animazioni e micro‑interazioni per migliorare l'usabilità e il "delight" dell'utente:

Micro‑interazioni sui bottoni (scale / press feedback) con Haptics
FAB (pulsante centrale +) animata: pop / rotate / morph
Lottie per onboarding, success states e empty states
Confetti al raggiungimento di un obiettivo (effetto celebrativo)
Progress bar circolare animata (SVG + Reanimated)
Skeleton loaders e shimmer per liste (caricamento percepito migliore)
Swipe-to-delete con animazioni e Undo
Animated gradients e glass‑blur dinamico per le card
Transizioni schermata → schermata più morbide (shared element / spring)
Dipendenze consigliate (compatible con Expo — usa expo install dove raccomandato):

react-native-reanimated
moti
lottie-react-native
react-native-gesture-handler
react-native-svg
expo-linear-gradient
react-native-confetti-cannon
Esempio comandi:

expo install react-native-reanimated react-native-gesture-handler react-native-svg expo-linear-gradient
npm install moti lottie-react-native react-native-confetti-cannon
Note: dopo aver installato react-native-reanimated, assicurati di avere il plugin Babel configurato (vedi babel.config.js).

🧩 Componenti Animati Inclusi (esempi pronti)
Nella cartella src/components/ ci sono esempi pronti:

AnimatedFAB.js — FAB con Moti + Haptics
LottieOnboarding.js — wrapper Lottie
GoalReachedConfetti.js — confetti per successi
AnimatedProgressBar.js — progress circolare SVG + Reanimated
SkeletonTransactionItem.js — shimmer loader per lista transazioni
Questi componenti sono esempi plug‑and‑play: integra direttamente in HomeScreen, GoalsScreen, AddTransactionModal.

📁 Architettura del Progetto (sintesi)
EquiBudget/
├── src/
│   ├── components/
│   │   ├── AnimatedFAB.js
│   │   ├── AnimatedProgressBar.js
│   │   ├── GoalReachedConfetti.js
│   │   ├── LottieOnboarding.js
│   │   └── SkeletonTransactionItem.js
│   ├── context/
│   ├── database/
│   ├── navigation/
│   ├── screens/
│   │   ├── HomeScreen.js
│   │   ├── GoalsScreen.js
│   │   └── AddTransactionModal.js
│   └── utils/
├── assets/
│   ├── lottie/
│   └── images/
├── App.js
├── package.json
└── babel.config.js
🚀 Quick Start
# Clone il repository (sostituisci con il tuo repo se diverso)
git clone https://github.com/giuliomichelotti/giuliomichelotti.git
cd giuliomichelotti

# Installa dipendenze
npm install
expo install react-native-reanimated react-native-gesture-handler react-native-svg expo-linear-gradient
npm install moti lottie-react-native react-native-confetti-cannon

# Avvia l'app (pulizia cache consigliata)
npx expo start -c
📝 Changelog Recenti
v2.2.0 (Dicembre 2024)

Redesign UI/UX con tema premium
Nuovo tab Obiettivi e FAB centrale
Migliorata persistenza obiettivi
v2.3.0 (Prossimo rilascio — animazioni)

Introduzione delle animazioni (Lottie, Reanimated, confetti)
Skeleton loaders e animated progress
Micro‑interazioni e miglioramenti UX
🔗 Link Utili
📦 Repository GitHub: https://github.com/giuliomichelotti/giuliomichelotti
📫 Contattami
Email GitHub

Made with ❤️ in Italy 🇮🇹
© 2025 Giulio Michelotti. Tutti i diritti riservati.