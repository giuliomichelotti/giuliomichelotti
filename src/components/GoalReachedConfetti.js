import React from 'react';
import { View, StyleSheet } from 'react-native';
import ConfettiCannon from 'react-native-confetti-cannon';

export default function GoalReachedConfetti({ show = false, count = 150 }) {
  if (!show) return null;
  return (
    <View style={styles.container} pointerEvents="none">
      <ConfettiCannon count={count} origin={{ x: -10, y: 0 }} fadeOut />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    height: 0,
    zIndex: 999,
  },
});
