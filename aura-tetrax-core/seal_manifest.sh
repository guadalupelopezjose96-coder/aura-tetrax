#!/bin/bash
# =========================================================================
# PIPELINE DE PERSISTENCIA Y SELLO CRIPTOGRÁFICO (JEGL_SYSTEM)
# =========================================================================

set -e
cd "$(dirname "$0")"

# 1. Generar marca de tiempo actual para el indexado del archivo
TIMESTAMP=$(date +%s)
BACKUP_DIR=".backup_seguro"
TARGET_JSON="$BACKUP_DIR/audit_$TIMESTAMP.json"

echo "[+] Capturando telemetría del motor..."

# 2. Ejecutar binario en modo silencioso y aislar el objeto JSON
RAW_OUTPUT=$(cargo run --quiet)
JSON_MANIFEST=$(echo "$RAW_OUTPUT" | sed -n '/{/,/}/p')

if [ -z "$JSON_MANIFEST" ]; then
    echo "[-] Error: No se detectó la estructura del FiscalAuditLog."
    exit 1
fi

# 3. Guardar el manifiesto en el búnker seguro
echo "$JSON_MANIFEST" > "$TARGET_JSON"
echo "[+] Manifiesto indexado guardado en: $TARGET_JSON"

# 4. Firmar asimétricamente con tu llave GPG local
echo "[+] Aplicando firma digital inmutable Ley ADT..."
gpg --clearsign --yes "$TARGET_JSON"

# 5. Limpieza del archivo intermedio en texto claro (opcional para máxima seguridad)
# Deja activo únicamente el archivo firmado (.asc) si deseas blindar el entorno
rm "$TARGET_JSON"

echo "========================================================================="
echo "   [!] Sello Consolidado: $TARGET_JSON.asc"
echo "========================================================================="

