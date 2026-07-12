import numpy as np
import sounddevice as sd

# Configuración de 432Hz
fs = 44100
duration = 2.0
freq = 432.0
t = np.linspace(0, duration, int(fs * duration), endpoint=False)
signal = 0.5 * np.sin(2 * np.pi * freq * t)

print("[-] Ejecutando prueba de salida sónica...")
sd.play(signal, fs)
sd.wait()
print("[+] Salida finalizada.")
