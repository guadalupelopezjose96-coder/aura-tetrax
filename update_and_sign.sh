#!/bin/bash
set -e

echo "🔄 [1/4] Accediendo al entorno de desarrollo..."
cd /data/data/com.termux/files/home/JEGL_PROJECTS/Aura_Premium/dist/law_core_engine

echo "🧹 [2/4] Limpiando residuos y compilando núcleo optimizado..."
cargo clean && cargo build --release

# Asegurar directorios de destino
mkdir -p ./dist

echo "📦 [3/4] Empaquetando y aplicando reducción de símbolos (strip)..."
cp "target/release/law_core_engine" "./dist/licencia_premium"
strip "./dist/licencia_premium"

echo "🔐 [4/4] Generando manifiesto de Verdad Digital (SHA-256)..."
sha256sum "./dist/licencia_premium" > "./dist/checksums.txt"

# Intento de respaldo externo si el almacenamiento ya está montado
if [ -d "~/storage/shared/Download" ]; then
    cp "./dist/checksums.txt" ~/storage/shared/Download/jegl_audit_checksums.txt
    echo "💾 Respaldo de manifiesto copiado a Almacenamiento/Download."
fi

echo "✅ Proceso completado al 100% con estricta integridad."
