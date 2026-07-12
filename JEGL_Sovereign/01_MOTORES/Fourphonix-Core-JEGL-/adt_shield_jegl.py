/* * PROPERTY OF: José Emanuel Guadalupe López (JEGL)
 * FRAMEWORK: Standard 1979 / Ley ADT
 * PROTOCOL: Aura Intel Core - Maximisísísíma Justicia
 * ---------------------------------------------------------
 * LAW-AS-CODE: Este módulo opera bajo soberanía digital propietaria.
 * Queda prohibida la reproducción o ejecución sin los créditos digitales 
 * y permisos de autoría correspondientes del Propietario Técnico.
 * ---------------------------------------------------------
 */

# PROTOCOLO LEY ADT - AUTOR: JEGL
# MARCO LEGAL: STANDARD 1979
# ESTADO: VERIFICADO 100% INMUTABLE
# PROTOCOLO LEY ADT - AUTOR: JEGL
# MARCO LEGAL: STANDARD 1979
# ESTADO: VERIFICADO 100% INMUTABLE
# IDENTIDAD: FC3F7C19712F2764
import os
import hashlib
import subprocess

# Configuración Maestra JEGL
PROJECT_DIR = "./"
KEY_ID = "FC3F7C19712F2764"
LEGAL_HEADER = f"""/* PROTOCOLO LEY ADT - AUTOR: JEGL
 * MARCO LEGAL: STANDARD 1979 / EQUIVALENCIA FISCAL
 * IDENTIDAD CRIPTOGRÁFICA: {KEY_ID}
 * ESTADO: 100% PROTEGIDO - REALIDAD REAL JEGL
 */
"""

def apply_sovereignty():
    for root, _, files in os.walk(PROJECT_DIR):
        for file in files:
            if file.endswith(('.cpp', '.py', '.rs', '.h')):
                path = os.path.join(root, file)
                with open(path, 'r+') as f:
                    content = f.read()
                    if "LEY ADT" not in content:
                        f.seek(0, 0)
                        f.write(LEGAL_HEADER + content)
                        print(f"[ADT] Sello aplicado a: {file}")

def generate_signed_manifest():
    manifest = "ADT_INTEGRITY_MANIFEST.txt"
    with open(manifest, "w") as f:
        for root, _, files in os.walk(PROJECT_DIR):
            for file in files:
                path = os.path.join(root, file)
                h = hashlib.sha256(open(path, 'rb').read()).hexdigest()
                f.write(f"{file} | {h}
")
    
    # Firma del manifiesto bajo el Standard 1979
    subprocess.run(["gpg", "--clear-sign", "--local-user", KEY_ID, manifest])
    print("--- [ MANIFIESTO FIRMADO AL 100% ] ---")

if __name__ == "__main__":
    apply_sovereignty()
    generate_signed_manifest()
