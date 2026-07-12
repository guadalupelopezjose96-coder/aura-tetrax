#!/bin/bash
# Script de despliegue protegido JEGL-ADT

echo "[JEGL-ADT] Iniciando compilación segura..."
cargo build --release --locked || { echo "Error en compilación"; exit 1; }

echo "[JEGL-ADT] Firmando y preparando despliegue..."
# Asegura que el binario sea trackeado por LFS
git lfs track "*.bin"

# Firma y commit del nuevo binario protegido
git add .
git commit -S -m "Deploy: Versión Pro/Elite [$(date +%Y-%m-%d)] - Protección JEGL-ADT activa"

echo "[JEGL-ADT] Despliegue completado satisfactoriamente."
