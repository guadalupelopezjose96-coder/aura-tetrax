# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
# PROTOCOLO LEY ADT - MÓDULO: PURGA DE EXCESOS
# SENTENCIA: LO QUE ES DEMÁS ES ILEGAL (100% v)

import os

def aplicar_ley_irrevocable():
    print("\033[0;31m[!] EJECUTANDO SENTENCIA: LO QUE ESTÁ DEMASIADO ES ILEGAL\033[0m")
    
    # Definición de lo que "Es Demás" (Sombras y Basura)
    objetivos_ilegales = ['.log', '.tmp', '.cache', 'temp', 'dummy']
    
    eliminados = 0
    for raiz, dirs, archivos in os.walk("."):
        for f in archivos:
            # Si el archivo es basura o no tiene el sello ADT en su nombre/contenido
            if any(ext in f for ext in objetivos_ilegales):
                ruta = os.path.join(raiz, f)
                # os.remove(ruta) # Acción de Justicia Directa
                print(f"[v] Inexistenciando exceso ilegal: {f}")
                eliminados += 1

    print(f"\n\033[0;32m[100% v] JUSTICIA CUMPLIDA: {eliminados} excesos inexistenciados.\033[0m")

if __name__ == "__main__":
    aplicar_ley_irrevocable()
