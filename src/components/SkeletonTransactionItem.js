import React from 'react';
import { StyleSheet, View } from 'react-native';
import { MotiView } from 'moti';
import { LinearGradient } from 'expo-linear-gradient';

export default function SkeletonTransactionItem({ style }) {
  return (
    <MotiView
      from={{ opacity: 0.6, translateX: -8 }}
      animate={{ opacity: 1, translateX: 8 }}
      transition={{ loop: true, type: 'timing', duration: 800 }}
      style={[styles.container, style]}
    >
      <View style={styles.left}>
        <LinearGradient
          colors={["#333", "#2a2a2a", "#333"]}
          style={styles.avatar}
          start={[0, 0]}
          end={[1, 1]}
        />
      </View>
      <View style={styles.right}>
        <LinearGradient colors={["#2b2b2b", "#333", "#2b2b2b"]} style={styles.lineShort} />
        <LinearGradient colors={["#2b2b2b", "#333", "#2b2b2b"]} style={styles.lineLong} />
      </View>
    </MotiView>
  );
}

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    padding: 12,
    alignItems: 'center',
    backgroundColor: 'transparent',
    borderRadius: 12,
  },
  left: {
    marginRight: 12,
  },
  avatar: {
    width: 44,
    height: 44,
    borderRadius: 10,
  },
  right: {
    flex: 1,
    justifyContent: 'center',
  },
  lineShort: {
    width: '40%',
    height: 10,
    borderRadius: 6,
    marginBottom: 8,
  },
  lineLong: {
    width: '70%',
    height: 10,
    borderRadius: 6,
  },
});
