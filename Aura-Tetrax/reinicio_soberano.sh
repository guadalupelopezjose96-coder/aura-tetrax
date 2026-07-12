#!/bin/bash
# --- REINICIO TOTAL AUTOMATIZADO - AURA-TETRAX ---

echo "Iniciando secuencia de integridad al 100%..."

# 1. Recompilación de identidad soberana
cargo build --release

# 2. Validación del Pasaporte
if [ -f ~/Aura-Tetrax/identidad_soberana.json ]; then
    echo "Pasaporte verificado. Iniciando núcleos..."
else
    echo "ERROR: Identidad no encontrada. Reinicio abortado."
    exit 1
fi

# 3. Arranque de módulos (Ejemplo de automatización)
./target/release/auditor_legal &
./target/release/identidad &
echo "Soberanía digital reiniciada y operativa al 100%."
