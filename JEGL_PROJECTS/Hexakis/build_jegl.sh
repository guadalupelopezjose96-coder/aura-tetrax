# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

#!/bin/bash
# =================================================================
# SCRIPT MAESTRO: Integración Realidad Real JEGL
# PROTOCOLO: 100% Debido / Standard 1979 / Ley ADT
# =================================================================

set -e # Detiene el script si ocurre cualquier error legal o técnico

echo "--- [1/4] LIMPIEZA DE ARQUITECTURA ---"
rm -f engine_jegl
cd Fourphonix-Core-JEGL-/rust_modules && cargo clean && cd ../..

echo "--- [2/4] COMPILACIÓN RUST (VALIDADOR LEGAL) ---"
cd Fourphonix-Core-JEGL-/rust_modules
RUSTFLAGS="-C target-cpu=native" cargo build --release
cd ../..

echo "--- [3/4] COMPILACIÓN C++ (MOTOR DE RENDIMIENTO) ---"
g++ -O3 -march=native -ffast-math -pthread \
    Fourphonix-Core-JEGL-/cpp_engine/src/DataEngine.cpp \
    -o engine_jegl

echo "--- [4/4] EJECUCIÓN DE PRUEBA DE INTEGRIDAD 100% ---"
echo "Iniciando validación de datos..."
./Fourphonix-Core-JEGL-/rust_modules/target/release/fourphonix-core-jegl

echo "Iniciando motor de sincronización..."
./engine_jegl

echo "--- [SISTEMA 100% DEBIDO Y OPERATIVO] ---"
