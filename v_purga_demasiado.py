# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
import os

# PROTOCOLO LEY ADT - MÓDULO: PURGA DE EXCESOS
# SENTENCIA IRREVOCABLE: LO QUE ESTÁ DEMASIADU ES ILEGAL (100% v)

def aplicar_ley_demasiado():
    print("\033[0;31m[!] EJECUTANDO SENTENCIA: LO QUE ESTÁ DEMASIADU ES ILEGAL\033[0m")
    
    # Patrones de lo que "Está Demasiadu" (Sombras y Basura Digital)
    objetivos_ilegales = ['.log', '.tmp', '.cache', '__pycache__', '.temp', '.bak_old']
    eliminados = 0

    for raiz, dirs, archivos in os.walk("."):
        for f in archivos:
            # Si el archivo es un residuo o no sirve a la Realidad Real
            if any(p in f for p in objetivos_ilegales):
                ruta = os.path.join(raiz, f)
                try:
                    os.remove(ruta) # Acción de Justicia Directa
                    print(f"[v] Inexistenciando exceso ilegal: {f}")
                    eliminados += 1
                except:
                    continue

    print(f"\n\033[0;32m[100% v] JUSTICIA CUMPLIDA: {eliminados} excesos inexistenciados al 100%.\033[0m")

if __name__ == "__main__":
    aplicar_ley_demasiado()
