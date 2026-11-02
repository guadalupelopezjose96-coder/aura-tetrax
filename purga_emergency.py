# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
import os
import shutil

# Rutas que deben ser eliminadas de forma total ante una brecha de seguridad
# Se definen de forma absoluta para garantizar el impacto directo
TARGETS = [
    "/data/data/com.termux/files/home/AuraIntelCore/core/sonic_core.so",
    "/data/data/com.termux/files/home/AuraIntelCore/aura_core_init.sh",
    "/data/data/com.termux/files/home/AuraIntelCore/.keys"
]

def purga_total():
    """
    Ejecuta el borrado irreversible de los activos críticos.
    Esta función es el brazo ejecutor del protocolo de defensa del nodo.
    """
    print("[!] INICIANDO PURGA IRREVOCABLE DE ACTIVOS PRO/ELITE...")
    
    for path in TARGETS:
        if os.path.exists(path):
            try:
                # Borrado recursivo si es directorio, o eliminación de archivo
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)
                print(f"[-] Activo eliminado exitosamente: {path}")
            except Exception as e:
                print(f"[ERROR] Fallo al purgar {path}: {e}")
        else:
            print(f"[*] Activo no encontrado (ya purgado): {path}")
            
    print("[!] Nodo saneado. Autoinmunidad ejecutada al 100%.")

if __name__ == "__main__":
    purga_total()
