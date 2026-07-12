# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

#!/bin/bash
# Protocolo de Validación JEGL - Optimizado para Velocidad 100%
set -e
echo "--- [100% v] Iniciando Validación Rápida ---"

# 1. Python Check (Ignorando carpetas de dependencias)
find . -maxdepth 3 -name "*.py" -not -path '*/.*' | while read -r file; do
    sed -i 's/[[:space:]]*$//' "$file"
    python3 -m py_compile "$file" || { echo "Error en $file"; exit 1; }
done

# 2. C++ Check
find . -maxdepth 3 -name "*.cpp" -not -path '*/.*' | while read -r file; do
    g++ -fsyntax-only "$file" 2>/dev/null || { echo "Error en $file"; exit 1; }
done

# 3. Ciberseguridad (Solo en archivos de código, no en binarios)
if find . -maxdepth 2 -type f -not -path '*/.*' -exec grep -lE "password|api_key|token" {} +; then
    echo "[CRÍTICO] Riesgo detectado en los archivos listados arriba."
    exit 1
fi

echo "--- [100% v] Integridad Confirmada en Tiempo Récord ---"
