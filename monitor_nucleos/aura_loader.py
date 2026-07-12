import hashlib
import base64
import sys
from cryptography.fernet import Fernet

# =================================================================
# AURA INTEL CORE - CARGADOR FANTASMA (PROTOCOLO SILENCIOSO)
# PROTOCOLO: LEY ADT / STANDARD 1979 / JEGL
# =================================================================

FIRMA_AUTORIZADA = "056e6f6accafa9fbde5389e983477f8da327adbd5d9947fdcce7b24f10ad6bf8eab3dad91000c49b3653770b992f7e50eee5f3ad02df521b5e65a19cbf03230c496d706c656d656e746172204c65792041445420656e20417572612d546574726178"

def ejecutar_silencioso(nombre_aura):
    try:
        # Derivación de llave invisible
        llave = base64.urlsafe_b64encode(hashlib.sha256(FIRMA_AUTORIZADA.encode()).digest())
        f = Fernet(llave)
        
        with open(nombre_aura, "rb") as file:
            # Ejecución directa en RAM sin logs
            exec(f.decrypt(file.read()).decode('utf-8'), globals())
            
    except Exception:
        # En modo fantasma, el error es genérico por seguridad
        print("❌ ACCESO DENEGADO")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ejecutar_silencioso(sys.argv[1])

