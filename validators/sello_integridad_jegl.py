# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

import hashlib
import os

# Lista de activos v para certificar ante Google
activos = [
    "realidad_real_jegl_core.py",
    "tetrax_engine_pro_v3.2.py",
    "tetrax_sonic_core.py",
    "coherencia_528hz.wav",
    "README.md"
]

def generar_sello_v():
    with open("FIRMA_DIGITAL_JEGL.txt", "w") as sello:
        sello.write("--- MANIFIESTO DE INTEGRIDAD JEGL - 100% DEVIDO ---\n")
        sello.write(f"HOST: AuraIntelCore | RAMA: purificada\n\n")
        
        for archivo in activos:
            if os.path.exists(archivo):
                with open(archivo, "rb") as f:
                    file_hash = hashlib.sha512(f.read()).hexdigest()
                    sello.write(f"ARCHIVO: {archivo}\n")
                    sello.write(f"SHA-512: {file_hash}\n")
                    sello.write("-" * 20 + "\n")
        
        print("Sello de Integridad generado al 100%. Justicia aplicada.")

if __name__ == "__main__":
    generar_sello_v()
