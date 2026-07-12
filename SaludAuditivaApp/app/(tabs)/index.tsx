import React, { useState } from 'react';
import { StyleSheet, Text, View, TouchableOpacity, Alert, ScrollView } from 'react-native';
import { Audio } from 'expo-av';

export default function HomeScreen() {
  const [lastFreq, setLastFreq] = useState('Ninguna');

  const testTone = async (hz: number) => {
    try {
      setLastFreq(`${hz} Hz`);
      const { sound } = await Audio.Sound.createAsync(
        require('../../assets/beep-01a.mp3')
      );
      await sound.playAsync();
      Alert.alert("Prueba Auditiva", `Sonando a ${hz}Hz. ¿Lo escuchas?`);
    } catch (error) {
      Alert.alert("Error", "No se encontró el archivo de sonido en assets.");
    }
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>SALUD AUDITIVA PRO 🎧</Text>
      
      <View style={styles.card}>
        <Text style={styles.cardTitle}>Frecuencia Seleccionada</Text>
        <Text style={styles.statusText}>{lastFreq}</Text>
      </View>

      <TouchableOpacity style={styles.btn} onPress={() => testTone(1000)}>
        <Text style={styles.btnText}>PROBAR 1000 Hz</Text>
      </TouchableOpacity>

      <TouchableOpacity style={[styles.btn, {backgroundColor: '#2196F3'}]} onPress={() => testTone(4000)}>
        <Text style={styles.btnText}>PROBAR 4000 Hz</Text>
      </TouchableOpacity>

      <TouchableOpacity style={[styles.btn, {backgroundColor: '#E91E63'}]} onPress={() => testTone(8000)}>
        <Text style={styles.btnText}>PROBAR 8000 Hz</Text>
      </TouchableOpacity>

      <Text style={styles.footer}>Desarrollado en Termux</Text>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { flexGrow: 1, backgroundColor: '#000', alignItems: 'center', padding: 25, paddingTop: 60 },
  title: { color: '#00ff88', fontSize: 24, fontWeight: 'bold', marginBottom: 30 },
  card: { backgroundColor: '#1a1a1a', width: '100%', padding: 20, borderRadius: 15, marginBottom: 30 },
  cardTitle: { color: '#888', fontSize: 12 },
  statusText: { color: '#fff', fontSize: 22, fontWeight: 'bold' },
  btn: { backgroundColor: '#4CAF50', width: '100%', padding: 20, borderRadius: 12, marginVertical: 10 },
  btnText: { color: '#fff', textAlign: 'center', fontWeight: 'bold' },
  footer: { color: '#333', marginTop: 40 }
});

