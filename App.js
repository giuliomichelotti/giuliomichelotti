import React, { useState } from 'react';
import { SafeAreaView, View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { MotiView, MotiText } from 'moti';
import AnimatedFAB from './src/components/AnimatedFAB';
import LottieOnboarding from './src/components/LottieOnboarding';
import AnimatedProgressBar from './src/components/AnimatedProgressBar';
import GoalReachedConfetti from './src/components/GoalReachedConfetti';

// NOTE: aggiungi un file Lottie in assets/lottie/finance.json
const lottieFinance = require('./assets/lottie/finance.json');

export default function App() {
  const [progress, setProgress] = useState(0.42);
  const [showConfetti, setShowConfetti] = useState(false);

  const increaseProgress = () => {
    const next = Math.min(1, +(progress + 0.18).toFixed(2));
    setProgress(next);
    if (next >= 1) {
      setShowConfetti(true);
      setTimeout(() => setShowConfetti(false), 3500);
    }
  };

  return (
    <SafeAreaView style={styles.safe}>
      <View style={styles.container}>
        <MotiText
          style={styles.title}
          from={{ opacity: 0, translateY: -20 }}
          animate={{ opacity: 1, translateY: 0 }}
          transition={{ type: 'timing', duration: 800 }}
        >
          EquiBudget — Demo Animazioni
        </MotiText>

        <MotiView
          style={styles.lottie}
          from={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ type: 'timing', duration: 800, delay: 200 }}
        >
          <LottieOnboarding source={lottieFinance} />
        </MotiView>

        <MotiView
          style={styles.progressRow}
          from={{ opacity: 0, translateX: -30 }}
          animate={{ opacity: 1, translateX: 0 }}
          transition={{ type: 'timing', duration: 800, delay: 400 }}
        >
          <AnimatedProgressBar size={140} progress={progress} />
          <View style={styles.progressInfo}>
            <Text style={styles.progressText}>{Math.round(progress * 100)}%</Text>
            <TouchableOpacity style={styles.btn} onPress={increaseProgress}>
              <Text style={styles.btnText}>Aumenta</Text>
            </TouchableOpacity>
          </View>
        </MotiView>

        <MotiText
          style={styles.hint}
          from={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ type: 'timing', duration: 800, delay: 600 }}
        >
          Premi il pulsante centrale + per aggiungere una transazione (demo FAB)
        </MotiText>
      </View>

      <AnimatedFAB
        onPress={() => {
          // Simula aggiunta transazione e incremento leggero
          setProgress(prev => Math.min(1, +(prev + 0.08).toFixed(2)));
        }}
        style={styles.fab}
      />

      <GoalReachedConfetti show={showConfetti} />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safe: { flex: 1, backgroundColor: '#0A0A0F' },
  container: { padding: 20, flex: 1 },
  title: { color: '#fff', fontSize: 20, fontWeight: '700', marginBottom: 12 },
  lottie: { alignItems: 'center', marginVertical: 10 },
  progressRow: { flexDirection: 'row', alignItems: 'center', marginTop: 16 },
  progressInfo: { marginLeft: 18, alignItems: 'center' },
  progressText: { color: '#fff', fontSize: 20, fontWeight: '700', marginBottom: 12 },
  btn: {
    backgroundColor: '#6366F1',
    paddingHorizontal: 14,
    paddingVertical: 8,
    borderRadius: 10,
  },
  btnText: { color: '#fff', fontWeight: '700' },
  hint: { color: '#ccc', marginTop: 18, fontSize: 13 },
  fab: {
    position: 'absolute',
    right: 18,
    bottom: 28,
  },
});
