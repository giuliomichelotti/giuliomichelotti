import React from 'react';
import { StyleSheet, Platform } from 'react-native';
import { MotiPressable } from 'moti';
import { Ionicons } from '@expo/vector-icons';
import * as Haptics from 'expo-haptics';

export default function AnimatedFAB({ onPress, style }) {
  return (
    <MotiPressable
      onPress={() => {
        Haptics.selectionAsync();
        onPress && onPress();
      }}
      style={[styles.container, style]}
      animate={({ pressed }) => ({
        scale: pressed ? 0.94 : 1,
        rotate: pressed ? '12deg' : '0deg',
        shadowRadius: pressed ? 2 : 8,
      })}
      transition={{
        type: 'timing',
        duration: 120,
      }}
      pressTransition={{
        type: 'timing',
        duration: 80,
      }}
    >
      <Ionicons name="add" size={28} color="#fff" />
    </MotiPressable>
  );
}

const styles = StyleSheet.create({
  container: {
    width: 64,
    height: 64,
    borderRadius: 32,
    backgroundColor: '#8B5CF6',
    alignItems: 'center',
    justifyContent: 'center',
    ...Platform.select({
      android: { elevation: 6 },
      ios: {
        shadowColor: '#000',
        shadowOpacity: 0.18,
        shadowOffset: { width: 0, height: 6 },
        shadowRadius: 8,
      },
    }),
  },
});
