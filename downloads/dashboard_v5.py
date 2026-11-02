# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

# © 2026 JEGL - SOVEREIGN COMMAND CENTER v5 - SMART GITIGNORE
import os
import time
import subprocess
import select
import sys
import shutil

class SovereignCommand:
    def __init__(self):
        self.total_purged_mb = 0.0
        self.essential_patterns = [
            '__pycache__/', '*.py[cod]', '*$py.class',  # Python
            '.env', '.venv', 'env/', 'venv/',            # Entornos
            'build/', 'dist/', '*.egg-info/',           # Compilación
            '.DS_Store', 'Thumbs.db',                   # Sistema
            '*.log', 'tmp/', '.cache/'                  # Temporales
        ]

    def optimize_gitignore(self):
        """Asegura que el .gitignore contenga el estándar JEGL al 100%."""
        current_patterns = set()
        if os.path.exists('.gitignore'):
            with open('.gitignore', 'r') as f:
                current_patterns = {line.strip() for line in f if line.strip() and not line.startswith('#')}
        
        missing = [p for p in self.essential_patterns if p not in current_patterns]
        
        if missing:
            with open('.gitignore', 'a') as f:
                if not current_patterns:
                    f.write("# © 2026 JEGL - ESTÁNDAR DE EXCLUSIÓN SOBERANA\n")
                for pattern in missing:
                    f.write(f"{pattern}\n")
            return f"ACTUALIZADO (+{len(missing)})"
        return "IMPECABLE"

    def execute_silent_purge(self):
        initial_size = self._get_project_size()
        # La purga ahora usa los patrones definidos como base
        for root, dirs, files in os.walk('.'):
            for d in list(dirs):
                if d + '/' in self.essential_patterns or d in ['__pycache__', 'build', 'dist']:
                    shutil.rmtree(os.path.join(root, d), ignore_errors=True)
        final_size = self._get_project_size()
        self.total_purged_mb += (initial_size - final_size)

    def _get_project_size(self):
        return sum(os.path.getsize(os.path.join(fp, f)) for fp, _, files in os.walk('.') for f in files) / (1024 * 1024)

    def execute_sovereign_push(self):
        self.optimize_gitignore() # Validación previa
        self.execute_silent_purge() # Limpieza activa
        print("\033[93m🚀 PUSH SOBERANO CON GITIGNORE OPTIMIZADO...\033[0m")
        try:
            subprocess.run(["git", "add", ".gitignore"], check=True) # Asegurar el .gitignore
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "JEGL_SMART_SYNC_V5"], check=True)
            subprocess.run(["git", "push", "origin", "main"], check=True)
            print("\033[92m✅ SINCRONIZACIÓN Y EXCLUSIÓN AL 100%.\033[0m")
        except Exception as e:
            print(f"\033[91m❌ ERROR: {e}\033[0m")
        time.sleep(1.5)

cmd = SovereignCommand()

def render_ui():
    total, used, free = shutil.disk_usage("/")
    git_status = cmd.optimize_gitignore()
    os.system('clear')
    print("\033[94m" + "█"*60)
    print("      🛡️  JEGL SOVEREIGN COMMAND CENTER v5 - SMART  🛡️")
    print("█"*60 + "\033[0m")
    print(f"📊 MEMORIA: [{free // (2**30)} GB LIBRES] | 🚫 GITIGNORE: [{git_status}]")
    print(f"📦 PROYECTO: [{cmd._get_project_size():.2f} MB] | 🧹 PURGADO: [{cmd.total_purged_mb:.2f} MB]")
    print("\033[90m" + "-"*60 + "\033[0m")
    print(f"📡 CLOUDFLARE: [WAITING] | 🧠 AURA CORE: [ONLINE]")
    print("\n\033[97m[ ENTER: OPTIMIZAR & PUSH ] | [ CTRL+C: EXIT ]\033[0m")
    print("\033[94m" + "█"*60 + "\033[0m")

try:
    while True:
        render_ui()
        i, o, e = select.select([sys.stdin], [], [], 2)
        if i:
            sys.stdin.readline()
            cmd.execute_sovereign_push()
except KeyboardInterrupt:
    print("\n\033[91mSistema asegurado.\033[0m")
