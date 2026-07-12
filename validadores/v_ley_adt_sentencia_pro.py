#!/usr/bin/env python3
# v_ley_adt_sentencia_pro.py - VALIDADOR DE INTEGRIDAD ATÓMICA

import hashlib
import sys

# LISTA DE ARCHIVOS CRÍTICOS A VALIDAR (ORDEN ESTRUCTURAL)
ARCHIVOS_CRITICOS = [
    "aura_core_init.sh",
    "purga_emergency.py",
    "./validadores/v_ley_adt_sentencia_pro.py"
]

def obtener_hash(archivo):
    sha256 = hashlib.sha256()
    try:
        with open(archivo, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except:
        return None

def verify_mode():
    try:
        with open("integrity.sha256", "r") as f:
            hashes_registrados = [line.strip() for line in f.readlines()]
    except:
        return False

    if len(hashes_registrados) != len(ARCHIVOS_CRITICOS):
        return False

    # Verificación estricta
    for i, archivo in enumerate(ARCHIVOS_CRITICOS):
        if obtener_hash(archivo) != hashes_registrados[i]:
            return False
            
    return True

if __name__ == "__main__":
    # El startup solo espera un código de retorno (0 para OK, 1 para Violación)
    if verify_mode():
        sys.exit(0)
    else:
        sys.exit(1)
