/* * PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
 * PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
 * MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
 * ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
 */

import React, { useState } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Alert } from 'react-native';
import AudioRecorderPlayer from 'react-native-audio-recorder-player';
// Nota: Usaremos expo-av o react-native-sound para los tonos

const audioRecorderPlayer = new AudioRecorderPlayer();

export default function App() {
  const [db, setDb] = useState(0);

  // FUNCIÓN PARA MEDIR RUIDO AMBIENTAL
  const iniciarEscucha = async () => {
    const result = await audioRecorderPlayer.startRecorder();
    audioRecorderPlayer.addRecordBackListener((e) => {
      // Calculamos decibelios aproximados
      let rdb = Math.floor(e.currentMetering); 
      // Ajuste de sensibilidad (los valores suelen ser negativos)
      setDb(rdb + 100); 
    });
  };

  const detenerEscucha = async () => {
    await audioRecorderPlayer.stopRecorder();
    audioRecorderPlayer.removeRecordBackListener();
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Salud Auditiva Pro 🎧</Text>
      
      <View style={styles.dbCard}>
        <Text style={styles.dbValue}>{db} dB</Text>
        <Text style={styles.label}>Ruido Ambiente</Text>
      </View>

      <TouchableOpacity style={styles.btnStart} onPress={iniciarEscucha}>
        <Text style={styles.btnText}>MEDIR RUIDO</Text>
      </TouchableOpacity>

      <TouchableOpacity style={styles.btnStop} onPress={detenerEscucha}>
        <Text style={styles.btnText}>DETENER</Text>
      </TouchableOpacity>

      <TouchableOpacity 
        style={styles.btnTest} 
        onPress={() => Alert.alert("Prueba", "Iniciando barrido de frecuencias...")}>
        <Text style={styles.btnText}>INICIAR TEST AUDITIVO</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#000', justifyContent: 'center', alignItems: 'center' },
  header: { color: '#0f0', fontSize: 24, marginBottom: 30, fontWeight: 'bold' },
  dbCard: { backgroundColor: '#111', padding: 40, borderRadius: 100, borderWidth: 2, borderColor: '#0f0' },
  dbValue: { color: '#0f0', fontSize: 48, textAlign: 'center' },
  label: { color: '#888', textAlign: 'center' },
  btnStart: { backgroundColor: '#222', marginTop: 20, padding: 15, borderRadius: 10, width: 250 },
  btnStop: { backgroundColor: '#400', marginTop: 10, padding: 15, borderRadius: 10, width: 250 },
  btnTest: { backgroundColor: '#05a', marginTop: 20, padding: 15, borderRadius: 10, width: 250 },
  btnText: { color: '#fff', textAlign: 'center', fontWeight: 'bold' }
});
