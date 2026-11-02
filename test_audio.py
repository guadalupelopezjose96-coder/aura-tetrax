# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
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
