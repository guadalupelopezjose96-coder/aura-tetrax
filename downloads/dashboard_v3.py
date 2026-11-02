# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

# © 2026 JEGL - SOVEREIGN COMMAND CENTER v3
import os
import time
import subprocess
import select
import sys
import shutil

def get_storage_metrics():
    """Calcula el uso de memoria del iPad de 256GB y el proyecto."""
    total, used, free = shutil.disk_usage("/")
    # Cálculo del tamaño del proyecto actual (en el directorio activo)
    project_size = sum(os.path.getsize(os.path.join(fp, f)) for fp, _, files in os.walk('.') for f in files)
    return {
        "total_gb": total // (2**30),
        "free_gb": free // (2**30),
        "project_mb": project_size / (1024 * 1024)
    }

def execute_sovereign_push():
    print("\n\033[93m🚀 INICIANDO PUSH SOBERANO...\033[0m")
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "JEGL_STORAGE_OPTIMIZED_UPDATE"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("\033[92m✅ SINCRONIZACIÓN COMPLETA.\033[0m")
    except Exception as e:
        print(f"\033[91m❌ ERROR: {e}\033[0m")
    time.sleep(1.5)

def render_ui():
    metrics = get_storage_metrics()
    os.system('clear')
    print("\033[94m" + "█"*55)
    print("      🛡️  JEGL SOVEREIGN COMMAND CENTER v3  🛡️")
    print("█"*55 + "\033[0m")
    
    # Métricas de Memoria Activa
    print(f"📊 MEMORIA ACTIVA:  [{metrics['free_gb']} GB LIBRES / {metrics['total_gb']} GB TOTAL]")
    print(f"📦 PESO PROYECTO:   [{metrics['project_mb']:.2f} MB]")
    print(f"🧬 TETRAX CORE:     [v. PERFECTA]")
    
    print("\033[90m" + "-"*55 + "\033[0m")
    print(f"📡 CLOUDFLARE: [WAITING] | 🧠 AURA CORE: [STABLE]")
    print("\n\033[97m[ ENTER: PUSH SOBERANO ]  |  [ CTRL+C: EXIT ]\033[0m")
    print("\033[94m" + "█"*55 + "\033[0m")

try:
    while True:
        render_ui()
        i, o, e = select.select([sys.stdin], [], [], 2)
        if i:
            sys.stdin.readline()
            execute_sovereign_push()
except KeyboardInterrupt:
    print("\n\033[91mCierre de Emergencia ejecutado.\033[0m")
