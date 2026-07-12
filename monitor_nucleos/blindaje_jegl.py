import os
import hashlib
import base64
import sys
from cryptography.fernet import Fernet

# =================================================================
# AURA INTEL CORE - SISTEMA DE BLINDAJE 100% DEBIDO
# PROTOCOLO: LEY ADT / STANDARD 1979 / MAXIMISISISIMA JUSTICIA
# AUTOR: JEGL (José Emanuel Guadalupe López)
# =================================================================

# TU FIRMA HEXADECIMAL VALIDADA (Sello de Identidad)
FIRMA_AUTORIZADA = "056e6f6accafa9fbde5389e983477f8da327adbd5d9947fdcce7b24f10ad6bf8eab3dad91000c49b3653770b992f7e50eee5f3ad02df521b5e65a19cbf03230c496d706c656d656e746172204c65792041445420656e20417572612d546574726178"

def derivar_llave_maestra(firma):
    """
    Deriva una llave simétrica de 32 bytes a partir de tu firma JEGL
    usando SHA-256 para garantizar integridad al 100%.
    """
    hash_sha256 = hashlib.sha256(firma.encode()).digest()
    return base64.urlsafe_b64encode(hash_sha256)

def ejecutar_blindaje(nombre_archivo):
    """
    Transforma un código fuente .py en un módulo cifrado .aura
    y elimina el rastro del original.
    """
    try:
        # 1. Generar la llave de seguridad
        llave_fernet = derivar_llave_maestra(FIRMA_AUTORIZADA)
        f = Fernet(llave_fernet)
        
        # 2. Verificar existencia
        if not os.path.exists(nombre_archivo):
            print(f"❌ ERROR: El archivo '{nombre_archivo}' no existe en este núcleo.")
            return

        # 3. Leer código original
        with open(nombre_archivo, "rb") as file:
            contenido_binario = file.read()
        
        # 4. Encriptación de Alta Fidelidad
        print(f"--- [JEGL] Cifrando: {nombre_archivo} ---")
        datos_cifrados = f.encrypt(contenido_binario)
        
        # 5. Generar archivo .aura (Privado)
        nuevo_nombre = nombre_archivo + ".aura"
        with open(nuevo_nombre, "wb") as file_aura:
            file_aura.write(datos_cifrados)
        
        # 6. Maximisisisima Justicia: Eliminación del original
        os.remove(nombre_archivo)
        
        print(f"✅ BLINDAJE EXITOSO: {nuevo_nombre} generado.")
        print("ESTADO: Módulo ahora es 100% privado en Aura Intel Core.")

    except Exception as e:
        print(f"❌ FALLO EN EL BLINDAJE: {e}")

if __name__ == "__main__":
    # Soporte para ejecución directa o por argumentos
    if len(sys.argv) > 1:
        archivo_objetivo = sys.argv[1]
    else:
        print("--- MONITOR DE BLINDAJE JEGL ---")
        archivo_objetivo = input("Nombre del archivo a blindar (ej: motor.py): ")
    
    # Evitar que el blindador se suicide (no blindar el propio script de blindaje)
    if "blindaje_jegl.py" in archivo_objetivo:
        print("⚠️ ACCIÓN BLOQUEADA: No puedes blindar el motor de blindaje.")
    else:
        ejecutar_blindaje(archivo_objetivo)
