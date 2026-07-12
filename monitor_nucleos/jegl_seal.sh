#!/bin/bash
# Sellado de Propiedad Aura Intel - 100% Privado

FILE=$1
IDENTITY="José Emanuel Guadalupe López (JEGL)"
LAW_STANDARD="Ley ADT / Standard 1979"

echo "--- Sellando Activo Digital: $FILE ---"

# Inyectar metadatos de autoría y estándar legal
exiftool -Author="$IDENTITY" -Copyright="$LAW_STANDARD" -Comment="Propiedad Privada Aura Intel" $FILE

# Generar verificación SHA-512 para el registro de activos
sha512sum $FILE > "${FILE}.jegl_auth"

echo "[OK] Activo protegido al 100% bajo el estándar JEGL."
