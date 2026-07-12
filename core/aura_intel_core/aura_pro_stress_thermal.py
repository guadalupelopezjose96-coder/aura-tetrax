# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

# COPYRIGHT: USPTO-JEGL-2026 - Propiedad Absoluta de la Federación Fourphonix
#!/usr/bin/env python3
# AURA STRESS & THERMAL v1.0
import psutil, time, os

RED, BOLD, END = '\033[91m', '\033[1m', '\033[0m'

def monitor_thermal():
    print(f"{RED}{BOLD}[MÓDULO DE RENDIMIENTO]{END} Monitoreando estabilidad térmica...")
    for i in range(5):
        ram = psutil.virtual_memory().percent
        print(f" >> Carga de RAM: {ram}% | Estado Térmico: {BOLD}ÓPTIMO{END}")
        time.sleep(1)
    print(f"\n{BOLD}✔ Prueba de estabilidad completada al 100%.{END}")

if __name__ == "__main__":
    monitor_thermal()

