#!/bin/bash
set -e

APP_NAME="aura_premium"
OUTPUT_DIR="./dist"

echo "🚀 [1/3] Iniciando compilación de alta eficiencia..."
cargo build --release

mkdir -p "$OUTPUT_DIR"
cp "target/release/$APP_NAME" "$OUTPUT_DIR/licencia_premium"

echo "📦 [2/3] Binario empaquetado con éxito en $OUTPUT_DIR/licencia_premium"
echo "📜 [3/3] Creando manifiesto de verificación SHA-256..."
cd "$OUTPUT_DIR"
sha256sum "licencia_premium" > "checksums.txt"

echo "=============================================================================="
echo "🏆 EMPIEZO DE RENTA SEGURO: Aplicación lista para distribución SaaS."
echo "=============================================================================="
