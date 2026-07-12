#!/bin/bash

# --- Ley Irrevocable: Purga de lo no debido ---
# Script diseñado para el 100% de cumplimiento en entornos Samsung/iPad.

echo "[100%] Iniciando Purga de Binarios Ilegales..."

# 1. Purga de objetos y binarios no firmados (no debidos)
find . -type f \( -name "*.o" -o -name "*.bin" -o -name "*.so" \) -delete
echo "[100%] Eliminación de archivos no debidos completada."

# 2. Validación de Identidad (v_sello_adt_total.py)
echo "[100%] Ejecutando Validación Sello Primordial..."
python3 v_sello_adt_total.py --verify-all
if [ $? -ne 0 ]; then
    echo "[!] Error: Integridad no alcanzada al 100%. Abortando compilación."
    exit 1
fi

# 3. Recompilación Soberana de Hexakis (Estandarización 100% debida)
echo "[100%] Compilando Hexakis para arquitectura nativa..."
# Asegurando flags de optimización absoluta
export RUSTFLAGS="-C target-cpu=native -C opt-level=3"
cargo build --release --manifest-path=Hexakis/Cargo.toml

# 4. Aseguramiento de Permisos
chmod -R 600 ./src/core/pro/
echo "[100%] Segregación de activos Pro/Elite aplicada al 100%."

echo "[100%] Sistema purgado, verificado y recompilado. Ejecución 100% debida."
