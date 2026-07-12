# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Carga de identidad criptografica
load_dotenv(os.path.expanduser("~/bunker/security/.env"))
MASTER_KEY = os.getenv('JEGL_MASTER_KEY')

if not MASTER_KEY:
    print("[-] Error: Llave maestra no encontrada en el iPad.")
    exit(1)

cipher_suite = Fernet(MASTER_KEY.encode())
SENSITIVE_EXTS = [".key", ".conf", ".secret", ".db", ".jegl"]

def decrypt_file(file_path):
    """Restaura la legibilidad del codigo para desarrollo."""
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        decrypted = cipher_suite.decrypt(data)
        with open(file_path, "wb") as f:
            f.write(decrypted)
        print(f"🔓 [100% v] Descifrado: {file_path}")
    except Exception as e:
        print(f"[-] No se pudo liberar {file_path}: {e}")

def release_all():
    """Procesamiento masivo del repositorio."""
    for root, _, files in os.walk("."):
        if ".git" in root: continue
        for file in files:
            if any(file.endswith(ext) for ext in SENSITIVE_EXTS):
                decrypt_file(os.path.join(root, file))

if __name__ == "__main__":
    release_all()
