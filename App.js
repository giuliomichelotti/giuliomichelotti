import React, { useState } from 'react';
import { SafeAreaView, View, Text, StyleSheet, TouchableOpacity } from 'react-native';
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
        <Text style={styles.title}>EquiBudget — Demo Animazioni</Text>

        <View style={styles.lottie}>
          <LottieOnboarding source={lottieFinance} />
        </View>

        <View style={styles.progressRow}>
          <AnimatedProgressBar size={140} progress={progress} />
          <View style={styles.progressInfo}>
            <Text style={styles.progressText}>{Math.round(progress * 100)}%</Text>
            <TouchableOpacity style={styles.btn} onPress={increaseProgress}>
              <Text style={styles.btnText}>Aumenta</Text>
            </TouchableOpacity>
          </View>
        </View>

        <Text style={styles.hint}>Premi il pulsante centrale + per aggiungere una transazione (demo FAB)</Text>
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
