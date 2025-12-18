import React from 'react';
import { View, StyleSheet } from 'react-native';
import LottieView from 'lottie-react-native';

export default function LottieOnboarding({ source, loop = true, autoPlay = true, style }) {
  if (!source) return null;
  return (
    <View style={[styles.wrapper, style]}>
      <LottieView source={source} autoPlay={autoPlay} loop={loop} style={styles.anim} />
    </View>
  );
}

const styles = StyleSheet.create({
  wrapper: { alignItems: 'center', justifyContent: 'center' },
  anim: { width: 220, height: 220 },
});
