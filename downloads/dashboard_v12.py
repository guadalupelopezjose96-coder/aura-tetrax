# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

# © 2026 JEGL - SOVEREIGN COMMAND CENTER v12 - TOTAL ISOLATION
import os, subprocess, datetime

class SovereignSentinel:
    def __init__(self):
        self.repo = "guadalupelopezjose96-coder/FourPhonix-Core-JEGL-"
        self.access_revoked = False

    def revoke_all_access(self):
        """Elimina llaves de despliegue y cierra el repositorio."""
        print(f"\n\033[91m🔥 INICIANDO PROTOCOLO DE AISLAMIENTO TOTAL...\033[0m")
        try:
            # 1. Obtener y eliminar todas las Deploy Keys
            keys = subprocess.check_output(["gh", "repo", "deploy-key", "list", "-R", self.repo]).decode()
            for line in keys.splitlines()[1:]: # Omitir encabezado
                key_id = line.split()[0]
                subprocess.run(["gh", "repo", "deploy-key", "delete", key_id, "-R", self.repo, "-y"])
                print(f"🗑️  Deploy Key {key_id} revocada.")

            # 2. Convertir en Privado (Modo Ghost)
            subprocess.run(["gh", "repo", "edit", self.repo, "--visibility", "private"])
            
            self.access_revoked = True
            print("\033[92m✅ MURO DE FUEGO ACTIVO: El código ya no existe para el mundo exterior.\033[0m")
        except Exception as e:
            print(f"\033[91m❌ ERROR EN REVOCACIÓN: {e}\033[0m")

    def monitor(self, deadline):
        if datetime.datetime.now() >= deadline and not self.access_revoked:
            self.revoke_all_access()
