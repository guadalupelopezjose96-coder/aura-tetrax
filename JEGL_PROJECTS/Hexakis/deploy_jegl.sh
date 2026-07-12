# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

#!/bin/bash

echo "--- Iniciando Compilación al 100% ---"

# 1. Compilar Rust (Modo Release para máxima potencia)
cd rust_modules
cargo build --release
cd ..

# 2. Compilar C++ (Optimización O3 y Arquitectura Nativa)
g++ -O3 -march=native -pthread cpp_engine/src/DataEngine.cpp -o engine_bin

echo "--- Despliegue de Arquitectura Legal Completado ---"
