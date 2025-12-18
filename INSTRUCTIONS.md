# Istruzioni di integrazione — EquiBudget (Animazioni & README)

Passi rapidi per integrare tutto e far partire l’app:

1) Creare/aggiornare il repository
- Se vuoi che il README sia visibile sul profilo GitHub, il repo deve chiamarsi esattamente: `giuliomichelotti` (nome utente).
- Crea il repo (web UI) oppure usa `gh repo create giuliomichelotti/giuliomichelotti --public --confirm`.

2) Copia i file nella struttura
- Crea le cartelle `src/components/` e `assets/lottie/`.
- Incolla i file forniti (components, App.js, README.md, package.json, babel.config.js, INSTRUCTIONS.md).

3) Aggiungi le animazioni Lottie
- Metti i JSON Lottie in `assets/lottie/` (es. `assets/lottie/finance.json`).

4) Installa dipendenze
```bash
npm install
expo install react-native-reanimated react-native-gesture-handler react-native-svg expo-linear-gradient
npm install moti lottie-react-native react-native-confetti-cannon
```

5) Configura Babel (necessario per Reanimated)
- Assicurati che `babel.config.js` contenga il plugin `react-native-reanimated/plugin` come ultimo plugin.
- Riavvia Metro: `npx expo start -c`.

6) Esempio d'uso
- Apri `App.js` d'esempio incluso per vedere come integrare FAB, Lottie, progress bar e confetti.

7) Commit e push
```bash
git add .
git commit -m "Add animated components, App demo and updated README"
git push origin main
```

8) Se vuoi che io esegua il push:
- Aggiungi `@copilot` come collaboratore con permessi di scrittura su `giuliomichelotti/giuliomichelotti` oppure
- Crea il repo e poi concedimi accesso. Dimmi quando è pronto e provo io il push.

Consiglio: esegui `expo start -c` la prima volta per pulire la cache dopo aver installato Reanimated.
