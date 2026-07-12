#!/bin/bash
# ==============================================================================
# SCRIPT DE COMPILACIÓN Y FIRMADO MAESTRO - LEY ADT / STANDARD 1979
# AUTOR: José Emanuel Guadalupe López (JEGL)
# ==============================================================================

set -e

# 1. Definición de rutas y variables de la Bóveda Aura Intel
APP_NAME="licencia_premium"
OUTPUT_DIR="./dist"
KEY_ID="guadalupelopezjose96-coder"

echo "🚀 [1/4] Iniciando compilación de alta eficiencia para 88 núcleos..."
# Compilación optimizada para el hardware móvil del Arquitecto
cargo build --release

# Crear el directorio de distribución si no existe
mkdir -p "$OUTPUT_DIR"

# Copiar el binario compilado a la zona de distribución
cp "target/release/$APP_NAME" "$OUTPUT_DIR/"

echo "📦 [2/4] Binario empaquetado con éxito en $OUTPUT_DIR/$APP_NAME"

echo "🔐 [3/4] Cargando llave maestra GPG para el sellado digital..."
# Generar una firma en un archivo separado para validar la autenticidad del binario
gpg --batch --yes --local-user "$KEY_ID" --detach-sign --armor "$OUTPUT_DIR/$APP_NAME"

echo "📜 [4/4] Creando manifiesto de verificación de rastro..."
# Generar suma de verificación SHA-256 para control de integridad estricto
cd "$OUTPUT_DIR"
sha256sum "$APP_NAME" > "checksums.txt"

echo "=============================================================================="
echo "🏆 EMPIEZO DE RENTA SEGURO: Aplicación firmada y lista para distribución SaaS."
echo "🛡️ Rastro Cero asegurado bajo la Ley ADT. ¡SÍ x4!"
echo "=============================================================================="
