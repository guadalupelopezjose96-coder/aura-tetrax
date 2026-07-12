import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, TouchableOpacity, Alert, ScrollView } from 'react-native';
import { Audio } from 'expo-av';

export default function HomeScreen() {
  const [dbLevel, setDbLevel] = useState(0);
  const [testResult, setTestResult] = useState('Sin realizar');

  // Simulador de sensor de ruido ambiental
  useEffect(() => {
    const interval = setInterval(() => {
      const mockDb = Math.floor(Math.random() * (95 - 40) + 40);
      setDbLevel(mockDb);
    }, 1500);
    return () => clearInterval(interval);
  }, []);

  const playTone = async (hz: number) => {
    try {
      setTestResult(`Probando ${hz} Hz...`);
      const { sound } = await Audio.Sound.createAsync(
        require('../../assets/beep-01a.mp3')
      );
      await sound.playAsync();
      
      Alert.alert(
        "Audiometría",
        `¿Escuchaste el tono de ${hz}Hz?`,
        [
          { text: "No", onPress: () => setTestResult(`${hz}Hz: No audible`) },
          { text: "Sí", onPress: () => setTestResult(`${hz}Hz: Audible ✅`) }
        ]
      );
    } catch (e) {
      Alert.alert("Error", "Asegúrate de que beep-01a.mp3 esté en la carpeta assets");
    }
  };

  const getStatusColor = () => {
    if (dbLevel > 85) return '#FF5252'; // Rojo: Peligro
    if (dbLevel > 70) return '#FFD740'; // Amarillo: Precaución
    return '#69F0AE'; // Verde: Seguro
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.header}>SALUD AUDITIVA PRO 🎧</Text>
      
      <View style={[styles.gauge, {borderColor: getStatusColor()}]}>
        <Text style={[styles.dbText, {color: getStatusColor()}]}>{dbLevel}</Text>
        <Text style={styles.dbUnit}>dB SPL</Text>
      </View>

      <View style={styles.infoBox}>
        <Text style={styles.infoTitle}>Resultado del Test:</Text>
        <Text style={styles.infoValue}>{testResult}</Text>
      </View>

      <Text style={styles.sectionLabel}>PRUEBAS DE FRECUENCIA</Text>

      <TouchableOpacity style={styles.btn} onPress={() => playTone(1000)}>
        <Text style={styles.btnText}>1000 Hz (Habla Humana)</Text>
      </TouchableOpacity>

      <TouchableOpacity style={[styles.btn, {backgroundColor: '#2196F3'}]} onPress={() => playTone(4000)}>
        <Text style={styles.btnText}>4000 Hz (Frec. de Riesgo)</Text>
      </TouchableOpacity>

      <TouchableOpacity style={[styles.btn, {backgroundColor: '#9C27B0'}]} onPress={() => playTone(8000)}>
        <Text style={styles.btnText}>8000 Hz (Test Agudo)</Text>
      </TouchableOpacity>

      <View style={styles.footer}>
        <Text style={styles.footerText}>
          {dbLevel > 85 ? "⚠️ RUIDO EXCESIVO DETECTADO" : "Ambiente seguro para tus oídos."}
        </Text>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { flexGrow: 1, backgroundColor: '#000', alignItems: 'center', padding: 25, paddingTop: 50 },
  header: { color: '#FFF', fontSize: 22, fontWeight: 'bold', marginBottom: 30, letterSpacing: 1 },
  gauge: { width: 160, height: 160, borderRadius: 80, borderWidth: 4, justifyContent: 'center', alignItems: 'center', marginBottom: 30 },
  dbText: { fontSize: 48, fontWeight: 'bold' },
  dbUnit: { color: '#888', fontSize: 14 },
  infoBox: { backgroundColor: '#1a1a1a', width: '100%', padding: 15, borderRadius: 12, marginBottom: 30 },
  infoTitle: { color: '#666', fontSize: 12, textTransform: 'uppercase' },
  infoValue: { color: '#00ff88', fontSize: 18, fontWeight: 'bold', marginTop: 5 },
  sectionLabel: { color: '#444', alignSelf: 'flex-start', marginBottom: 10, fontWeight: 'bold' },
  btn: { backgroundColor: '#4CAF50', width: '100%', padding: 18, borderRadius: 12, marginVertical: 8 },
  btnText: { color: '#fff', textAlign: 'center', fontWeight: 'bold' },
  footer: { marginTop: 20 },
  footerText: { color: '#888', fontSize: 13, fontStyle: 'italic' }
});
