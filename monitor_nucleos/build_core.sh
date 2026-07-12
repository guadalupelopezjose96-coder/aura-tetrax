#!/bin/bash

# Configuración de optimización para 76 núcleos
export CXXFLAGS="-O3 -march=native -ffast-math -funroll-loops -mfpu=neon-vfpv4"
export RUSTFLAGS="-C opt-level=3 -C target-cpu=native -C codegen-units=1"

echo "--- Iniciando Compilación del Módulo de Frecuencias JEGL ---"

# 1. Compilación del núcleo en C++ (Tetrax Engine Component)
g++ $CXXFLAGS -shared -fPIC core_oscillator.cpp -o libfrequency_core.so
if [ $? -eq 0 ]; then
    echo "[OK] Módulo C++ compilado con éxito."
else
    echo "[ERROR] Fallo en la compilación de C++."
    exit 1
fi

# 2. Compilación del módulo de seguridad en Rust
cargo build --release
if [ $? -eq 0 ]; then
    echo "[OK] Módulo de Seguridad Rust (Ley ADT) listo."
else
    echo "[ERROR] Fallo en la compilación de Rust."
    exit 1
fi

echo "--- Proceso 100% Completado ---"
