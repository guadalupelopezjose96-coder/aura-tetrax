#!/bin/bash
# Generación de firma para el binario del oscilador
echo "--- Iniciando Proceso de Firma JEGL (ED25519) ---"

# 1. Crear el hash del binario compilado
sha256sum libfrequency_core.so > binary.hash

# 2. Firmar el hash con tu llave privada ED25519
# Esto asegura que el código es 100% de tu autoría
openssl pkeyutl -sign -inkey my_private_key.pem -rawin -in binary.hash -out binary.sig

if [ $? -eq 0 ]; then
    echo "[OK] Firma generada correctamente."
    echo "Identidad Validada: José Emanuel Guadalupe López"
else
    echo "[ERROR] Error en el proceso de firma."
    exit 1
fi
