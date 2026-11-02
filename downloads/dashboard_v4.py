# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

# © 2026 JEGL - SOVEREIGN COMMAND CENTER v4 - CLEAN & SYNC
import os
import time
import subprocess
import select
import sys
import shutil

class SovereignCommand:
    def __init__(self):
        self.total_purged_mb = 0.0

    def execute_silent_purge(self):
        """Elimina archivos temporales y basura antes del push."""
        initial_size = self._get_project_size()
        patterns = ['__pycache__', '*.pyc', '*.pyo', '.DS_Store', 'build/', 'dist/', '*.egg-info']
        
        print("\033[90m🧹 Iniciando purga silenciosa...\033[0m")
        for root, dirs, files in os.walk('.'):
            # Eliminar directorios basura
            for d in list(dirs):
                if d in ['__pycache__', 'build', 'dist']:
                    shutil.rmtree(os.path.join(root, d))
            # Eliminar archivos basura
            for f in files:
                if f.endswith(('.pyc', '.pyo', '.DS_Store')):
                    os.remove(os.path.join(root, f))
        
        final_size = self._get_project_size()
        self.total_purged_mb += (initial_size - final_size)
        print(f"\033[92m✨ Purga completada. Ahorro: {initial_size - final_size:.2f} MB\033[0m")

    def _get_project_size(self):
        return sum(os.path.getsize(os.path.join(fp, f)) for fp, _, files in os.walk('.') for f in files) / (1024 * 1024)

    def execute_sovereign_push(self):
        self.execute_silent_purge() # Limpieza automática previa
        print("\033[93m🚀 PUSH SOBERANO EN CURSO...\033[0m")
        try:
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "JEGL_CLEAN_SYNC_2026"], check=True)
            subprocess.run(["git", "push", "origin", "main"], check=True)
            print("\033[92m✅ SINCRONIZACIÓN IMPECABLE AL 100%.\033[0m")
        except Exception as e:
            print(f"\033[91m❌ ERROR: {e}\033[0m")
        time.sleep(1.5)

cmd = SovereignCommand()

def render_ui():
    total, used, free = shutil.disk_usage("/")
    os.system('clear')
    print("\033[94m" + "█"*55)
    print("      🛡️  JEGL SOVEREIGN COMMAND CENTER v4  🛡️")
    print("█"*55 + "\033[0m")
    print(f"📊 MEMORIA: [{free // (2**30)} GB LIBRES] | 🧹 PURGADO: [{cmd.total_purged_mb:.2f} MB]")
    print(f"📦 PROYECTO: [{cmd._get_project_size():.2f} MB] | 🧬 STATUS: [v]")
    print("\033[90m" + "-"*55 + "\033[0m")
    print(f"📡 CLOUDFLARE: [WAITING] | 🧠 AURA CORE: [STABLE]")
    print("\n\033[97m[ ENTER: PURGAR & PUSH ] | [ CTRL+C: EXIT ]\033[0m")
    print("\033[94m" + "█"*55 + "\033[0m")

try:
    while True:
        render_ui()
        i, o, e = select.select([sys.stdin], [], [], 2)
        if i:
            sys.stdin.readline()
            cmd.execute_sovereign_push()
except KeyboardInterrupt:
    print("\n\033[91mSistema en reposo.\033[0m")
